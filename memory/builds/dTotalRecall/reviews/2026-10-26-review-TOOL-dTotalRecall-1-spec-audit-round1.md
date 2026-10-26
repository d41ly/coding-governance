**Serves:** spec-audit TOOL-dTotalRecall-1@rev-1 TOOL-dTotalRecall-13@rev-1 TOOL-dTotalRecall-8@rev-1 TOOL-dTotalRecall-18@rev-1 TOOL-dTotalRecall-16@rev-1 TOOL-dTotalRecall-25@rev-1 TOOL-dTotalRecall-5@rev-1 TOOL-dTotalRecall-4@rev-1 TOOL-dTotalRecall-6@rev-1 TOOL-dTotalRecall-22@rev-1 TOOL-dTotalRecall-3@rev-1 TOOL-dTotalRecall-2@rev-1 TOOL-dTotalRecall-7@rev-1 TOOL-dTotalRecall-11@rev-1 TOOL-dTotalRecall-10@rev-1 TOOL-dTotalRecall-19@rev-1 TOOL-dTotalRecall-21@rev-1 TOOL-dTotalRecall-9@rev-1 TOOL-dTotalRecall-23@rev-1 TOOL-dTotalRecall-24@rev-1 TOOL-dTotalRecall-20@rev-1 TOOL-dTotalRecall-17@rev-1 TOOL-dTotalRecall-14@rev-1 TOOL-dTotalRecall-15@rev-1 TOOL-dTotalRecall-26@rev-1 TOOL-dTotalRecall-12@rev-1

# Tier-2 review: the spec audit of dTotalRecall's 26 unit specs (TOOL-dTotalRecall-1 to -26)

Provenance: a Tier-2 spec audit at full intensity, run on 2026-10-26 over dTotalRecall's spec commit `581a761f8`. Five lenses ran first (finders gov-spec-reviewer). Five skeptic batches followed (gov-skeptic), then synthesis (gov-synthesizer). One spec document was supplied as sibling context.

Reviewed: memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md@60d2c607b8be1852cdb5adcd6c59bae372050efb, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-13.md@a6f13463c9ec01068ed98efe95bca91de982696a, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-8.md@addaf0ac3df891f51306f933fc8c781157b32d6f, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-18.md@27851d85ee603237131c1a9a6b4119b36e130d6e, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-16.md@f0fb34352c1ded726472ec53b37d3a8b91914731, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-25.md@86e1b94d97d50803f6cb0dc5184087f3a8853e4f, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-5.md@e343d132f1db869e5c301389adebf8b4253d33a1, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-4.md@7699ed667c3efd8acde49962001e884cdd00e5f4, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-6.md@de6e7960d7abd835de36fd735657f39289203b5b, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-22.md@a2bc597d6c6837641f149c1a98a960618b2cf0f6, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-3.md@d6d10de94b98076b264a98ba332fbcde1beb365d, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md@f92224649a98411cd1e28c5ea1870da90325ab89, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-7.md@f4d6d626e1a87dd298dc12e56258c2554bf576af, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-11.md@9672984f3a28a1f02368d132b76f65b37383e79a, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-10.md@e04c0d648f3b12c5ef146ea8eacf8bf5dd35f602, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-19.md@0750a900add539ea0ee6f49ddaf8a57e36f85309, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-21.md@d6824a53b0ce1b9afa9f24f08271545f18fe475a, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-9.md@46971b8d5b905b32a0d46d59bd87855b55d7c8f6, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-23.md@cc2bf9d8c7a8eef1dd37ddd74346e72134929b61, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-24.md@6d115e7f3ca62eb19c5abedcecfebc87262af381, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-20.md@1260fd3a5df0baa17968c4473912d31c531dd0c9, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-17.md@a5a5221c9ef66b60db34da23e63daf23e75e7eb7, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-14.md@bc6a5214908accb8466a9dd35b6077306ef57250, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-15.md@ac703e976e3e56382bfa73ebe93bb5ec07273398, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-26.md@2570033f3b2e3a23ee301842445b647e7eadce60, memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-12.md@f2f2673cedcd5ed6ee8c90680119bf8eaeee9981

ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker survived. Seven high, 44 medium and 13 low items stand, and each has a fix. Every item amends spec text before its unit builds.

The highs share two themes. Units 1, 11 and 19 grade records in ways that red the build's own later records (H1, H7). Units 4, 5, 7, 8 and 19 each miss a reader, a writer or an existing seam that the rest of the set depends on (H2 to H6).

The set also has three cross-cutting gaps worth fixing once at build level rather than spec by spec:
- the registry-row grammar (M3, M5, H7, M11);
- the memory-tree kit boundary (M10);
- §7 leg lines that omit unguarded or broad-guard legs (M26 to M30, L7).

## Review shape

The review ran at intensity full: raw 68, confirmed 66, refuted 2, unverified 0 (0 uncertain), precision 0.97.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 15 | 14 | 1 | 0 | 0 | 0.93 |
| grounding | yes | 7 | 7 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 12 | 12 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 21 | 20 | 1 | 0 | 0 | 0.95 |

Adjudicated tally by item: 0 blocker, 7 high, 44 medium, 13 low (64 items).

Adjudicated tally by raw confirmed finding: 0 blocker, 7 high, 46 medium, 13 low (66 findings).

The two counts differ because M10 merges findings 11, 32 and 33, which describe one defect.

Findings 9 (medium) and 36 (high) describe the same defect, the routing region's `journal` row. Their binding grades differ, so they stay in separate items (M8 and H5). Findings 19 (medium) and 67 (low) are kept apart for the same reason (M14 and L12), and so are 12 (medium) and 51 (high) (M11 and H7).

### Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Verdict hygiene: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified. 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 63 judged sound, 3 judged UNSOUND (findings 25, 53 and 59), 0 none proposed, 0 NOT JUDGED. The skeptic's corrected fix is written below for each of the three.
- Severity: 0 confirmed findings were UNGRADED by the skeptic. 8 were RE-GRADED by the skeptic: 2, 3, 4, 37, 48 and 50 from high to medium, and 54 and 59 from medium to low.
- Unverified: 0 answered UNCERTAIN, and 0 had no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 1 spec document was supplied as `specs`, as sibling context.
- By design: none was supplied, either as a caller byDesign or as a block.
- Move check: no checked subject moved.

Checklist: NONE swept, because the checklist is absent. A zero count is not evidence that the project's recurring bug classes are absent.

## High

### H1 — Unit 19's causes check reds the build's next review record (id 1)

- **Where:** spec-19 §2 S7 and S8, and §3.
- **What is wrong:** S8 reds every tracked record without a `Caused-by` that is not a root kind and has no legacy row. S7's legacy ledger is seeded once and only shrinks. The writers that keep producing records are never changed to write a cause: tier2-review.js (spec-audit and diff-review records), unattended-build's prompt writer, handoff.py, and hand-written logs and research. Only the door (unit 2) and the factory kinds write one.
- **Consequence:** the first diff-review record written for unit 19 itself reds `record causes (causes and orphans over the legacy population)`. Every later review, verdict record and prompt does the same, so the build cannot land its later units without a deviation.
- **Fix (skeptic: SOUND):** Add a scope item to unit 19, or a named follow-on unit ordered right after it, that makes every current record writer emit `**Caused-by:**`. That covers tier2-review.template.js's record writer, unattended-build's prompt writer, handoff.py, and the hand-written log and research paths (or route those through `gov_record.py new`). Alternatively, grade only the kinds whose `writer` is the door, and list the other writers as exempt with an ask each. Add a criterion that renders one review record through the harness after the seed and runs `record_causes.py --check` green. The build run must stage this probe, because it writes a record.
- **Left-shift gate:** a spec-set check that a leg grading a record field, for every kind it grades, either has a writer that emits that field or an exemption.

### H2 — Unit 8's `linguist-generated` glob drops real workflow source from the code record (id 16)

- **Where:** spec-8 §4 "Bounds" (the paragraph after the table), with S9 and §8 F2.
- **What is wrong:** the spec registers `tools/workflows/*.js` as generated in `.gitattributes`. That glob matches all 11 tracked JS files. Four of them are `.template.js` sources, and three are hand-written: `check-workflow-syntax.js`, `orient-counterfactual.js` and `unattended-unit.js`.
- **Consequence:** the Bounds row excludes every `linguist-generated` path. The code record would silently hold no definitions, calls or edges for the canonical workflow sources. Every reader of the record (the map, `symbols`, the reuse lookups) would then answer wrongly about workflow code.
- **Fix (skeptic: SOUND):** Name only the four rendered outputs as `linguist-generated`: `tier2-review.js`, `unattended-build.js`, `drift-audit-code.js` and `drift-audit-state.js`. Alternatively, derive the list from the workflows kit's render rows (`include = ["*.template.js"]`). Add a criterion that `git check-attr linguist-generated` is unset on every `*.template.js` and on the three hand-written scripts. The same criterion should check that the code record holds a `code_row` for `renderShapeLine` in `tier2-review.template.js`.
- **Left-shift gate:** a parity arm checking that the `linguist-generated` paths equal the union of the kits' render outputs.

### H3 — Unit 5's reader inventory misses `split("-")` id readers, and the flip probe certifies them (id 17)

- **Where:** spec-5 §4 "The readers" and "The flips".
- **What is wrong:** the inventory is called "derived, never typed", but its `--readers` predicate finds only regex literals. It misses the id readers that split on hyphens:
  - backlog.py:1042, :1407 and :1664;
  - gen_build_index.py:3541 and :4073;
  - check-recall.py:511;
  - query.py:1463;
  - drift_report.py:708;
  - migrate_backlog.py:329 and :337.
- **Consequence:** under the hyphenated `in-slug` flip, `TOOL-d2026-10-26ClosedLoop-3` gives `split("-")[1] == "d2026"`. Those readers then file, match or grade against the wrong slug. The flip probe checks only `mint_re`, `BUILD_SLUG_RE` and `ID_RE`, so it still prints `ok`. The clause is unmet, and a check certifies that it is met.
- **Fix (skeptic: SOUND):**
  - Widen `--readers` to report non-regex id splitting applied to a name containing `id`, `slug` or `unit`: `.split("-")`, `.rsplit("-"`, `cut -d-`, `IFS=-`, and `${x%-*}`/`${x#*-}`.
  - Give each hit a disposition. The fix for a split reader is to parse through `grammar_for().ID_RE`.
  - Add a flip-probe check that runs each re-pointed reader's slug extraction on `TOOL-d2026-10-26ClosedLoop-3` and expects `d2026-10-26ClosedLoop`.
- **Left-shift gate:** add "id parsed by `split('-')`" to the project's bug-class checklist and to the `--readers` predicate.

### H4 — Unit 19 mints a second `read_header_edges` beside PLAY-dOrderedCharter-28's (id 23)

- **Where:** spec-19 §2 S1, §4 Inventory and §10.
- **What is wrong:** S1 creates `read_header_edges` in `tools/memory-tree/tree_lib.py`. PLAY-dOrderedCharter-28 S5 already specs an adapter with that name in `tools/playbook/edge_grammar.py`, reading the same three header keys. Spec 19 cites 28 S2 but not S5. Spec 19's reader accepts the bulleted `- **Caused-by:**` form, which 666 landed records carry. 28's adapter reads only the bare form.
- **Consequence:** two readers would see different cause edges. `edge_grammar.py --check` (spec 19 AC10) and spec 22's caused-by count would disagree with `record_causes.py`.
- **Fix (skeptic: SOUND):** Extend PLAY-dOrderedCharter-28 S5's adapter so it admits the optional `- ` form. Alternatively, make `tree_lib.read_header_edges` the one reader, have edge_grammar's header site call it, and record the respelling as a deviation from dOrderedCharter-28. Then name the shared reader in §10 and in spec 22's sites. Add a probe: a fixture carrying `- **Caused-by:** X`, read by both the edge check and `record_causes.py --check`, returns the same edge from each.
- **Left-shift gate:** a reuse check that refuses a function name minted twice across kits.

### H5 — Unit 4's routing region drops every `log` record written after unit 18 (id 36)

- **Where:** spec-4 §4 "The routing region" (journals row), against spec-18 §2 S7 and S8. Spec-2 S9 has the same problem.
- **What is wrong:** the row routes "each build/ record whose kind is `journal`". Unit 18 (order 4) renames the kind to `log` before unit 4 (order 8) builds, and every writer emits `log` from then on. `read_bindings` keeps the written token. Spec 4 never mentions `canonical_kind` or unit 18. Spec-2 S9 still cites "unit 1's `journal`" row.
- **Consequence:** `render_routes` shows only legacy `journal` records, so the README's routing region answers wrongly. Unit 18's reader inventory cannot catch this, because unit 4's code does not exist yet when unit 18 builds.
- **Fix (skeptic: SOUND):** Route "each build/ record whose `canonical_kind(...)` is `log`", and add a consumes-from edge to TOOL-dTotalRecall-18. Re-spell unit 2 S9's row list as `log`. Add a criterion that plants one `**Serves:** log` record and one `**Serves:** journal` record and expects both under journals.
- **Left-shift gate:** a spec-set check that no spec ordered after a rename compares the retired token raw.
- **Note:** M8 (finding 9) reports the same defect at a medium binding grade.

### H6 — Unit 7's `new ask --text` injects BACKLOG rows and bypasses the acceptance gate (id 49)

- **Where:** spec-7 §2 S2 and §4 "The door verb".
- **What is wrong:** `--text` is rendered verbatim into the BACKLOG row. The door grades the mapping it built from the `--clause` arguments, not the bytes it writes. The read-back only confirms that one ask with the minted id exists.
- **Consequence:** `--text $'x\n- <id2> · filed …'` with `--clause accept y` passes the grade. It writes the minted ask with no acceptance, and the accept clause lands on an injected row. The `refuse` default bypasses itself, and ungraded rows enter BACKLOG.md. The check certifies a clause the row does not carry.
- **Fix (skeptic: SOUND):**
  - Refuse at the door any `--text`, `--clause` value or `--pointer` holding a newline or CR, or holding `SEP` (' · ') or `ARROW` (' → ').
  - Grade the clauses parsed back from the rendered row (`backlog.parse_file` over the would-be file), not the argument mapping.
  - Make the read-back assert that exactly one row was added and that it is the minted id.
  - Add AC cases for a newline in the text and for ' · accept y' in the text with no `--clause`. Each exits 2 and writes nothing.
- **Left-shift gate:** add "write door grades its arguments, not the bytes it writes" to the bug-class checklist. Add a shared CR/LF/separator refusal in the door's argument layer.

### H7 — Unit 11's shape-run `home` is the whole build folder (id 51)

- **Where:** spec-11 §4 "The row" (`home`), with spec-1 §5 and S4.
- **What is wrong:** the `home` is `memory/builds/<slug>/build/`, on a `fields` row with 15 required fields, and the unit lands with zero records.
- **Consequence:** the outcome depends on how `home` is read.
  - **As a glob:** unit 1 S4 grades every non-legacy build record against the 15 shape-run fields and reds them. Unit 9's `record` extractor cannot separate shape-run from deviation, log or research.
  - **Literally:** the home matches no file, and unit 1 §5 and unit 18's column rule red the empty home of a `fields` kind.
  
  Either way `record-kinds --check` reds or misgrades at unit 11's landing.
- **Fix (skeptic: SOUND):** Set the home to `memory/builds/*/build/*-shape-run-*.md`, the id-rule's shape, as unit 25 does for stream-plan. State in unit 11 that the empty population reads `unarmed` and exits 0 at landing, like unit 25 S5, and have unit 1's empty-home rule admit that. Unit 9 S1 should state the rule for a path that two homes match: the most specific glob wins, or `check_record_kinds` refuses the overlap.
- **Left-shift gate:** `check_record_kinds` refuses overlapping `fields` homes, and refuses a home that is a bare directory.

## Medium

### M1 — gap-mem-16 is owned by the build but carried by no spec (id 2)

- **Where:** README.md, "The problem this build exists to solve" and Expected improvements, against every subject spec.
- **What is wrong:** the README lists gap-mem-16 ("Records that belong to no build have no home") among the 22 owned gaps. No spec names it, carries it, or has a criterion that closes it.
- **Consequence:** built as specced, the build closes with gap-mem-16 open and no unit accountable for it. A close certifying 22 closed gaps would be wrong.
- **Fix (skeptic: SOUND):** Assign gap-mem-16 to the unit whose clause covers it, most likely TOOL-dTotalRecall-18 (homes on every kind row) or -1. Name it in that spec's §1. Add scope that declares a `home` for the period-, SHA- and adopter-keyed record kinds. Add a criterion that is red on a planted out-of-build record with no registered home. If no clause covers the gap, file the ask or departure that moves it out of this build.
- **Left-shift gate:** a build-level check that every owned gap id appears in at least one spec's §1.

### M2 — Unit 21's AC1 grep forbids the call S4 and S8 require (id 3)

- **Where:** spec-21 §6 AC1, against §2 S4 and S8.
- **What is wrong:** AC1 requires `git grep -n "build_index(" -- tools/memory-recall tools/memory-tree/row_grammar.py` to print nothing. But S4 (query.py's `ensure_index`) and S8 (check-recall.py's `build_served_dir`) both call `tag_index.build_index`.
- **Consequence:** AC1 stays red on a correct build. The alternative is that the builder hides the one writer behind an alias, which is the opposite of what S1 asks.
- **Fix (skeptic: SOUND):** Narrow AC1 to the retired FTS builder. For example, `git grep -nE "(bench|B)\.build_index\(|def build_index" -- tools/memory-recall tools/memory-tree/row_grammar.py` prints nothing, and `git grep -n "def build_fts_rows" -- tools` prints one line.
- **Left-shift gate:** a spec lint that runs each "prints nothing" grep criterion against the §2 call sites the spec mandates.

### M3 — Four registry rows break units 16 and 18's column grammar (id 4)

- **Where:** spec-11 §4 "The row" and AC7. The same rows appear in spec-7 §4 "The ask row" and AC8, spec-3 §4 "The registry row", and spec-4 §4 "The registry row".
- **What is wrong:** unit 18 (order 4) and unit 16 (order 5) land before these rows. Unit 18 requires a `lifecycle` from `append-only|current-state|frozen|generated|out`, `layer = "layer.memory"`, read-key readers or `[]` with `readers-none`, and a glob `home`. Unit 16 requires `purpose`. Against that:
  - **Unit 11 (order 14):** writes `layer = "memory"`, a prose lifecycle, script-name readers and a directory home, and has no purpose.
  - **Unit 7 (order 13):** writes a prose lifecycle and script-name readers.
  - **Units 3 (order 11) and 4 (order 8):** write `layer = "core"` and `readers = []` with no `readers-none`. Unit 4's home `<memory-root>/builds/<slug>/README.md` is not a glob.
- **Consequence:** unit 11 AC7 and unit 7 AC8 cannot pass, and the `record-kinds` leg reds at each of those passes.
- **Fix (skeptic: SOUND):** Rewrite each row to units 16 and 18's grammar:
  - `layer = "layer.memory"`;
  - `lifecycle` from the closed set (`append-only` for shape-run, `current-state` for ask and build-readme);
  - `readers` as read keys, or `[]` with `readers-none = "<reason>"`;
  - `home` as a glob (`memory/builds/*/build/*-shape-run-*.md`, `memory/builds/*/BACKLOG.md`, `memory/builds/*/README.md`, `refs/gov/claims/*`);
  - a `purpose` table.
  
  Say how a newly registered fields kind with no records yet passes the home and empty-home rules, for example through an `unarmed` exemption in units 1 and 18 like unit 25's S5. Before writing the rows, run `record_kinds.py --check` over each planted row.
- **Left-shift gate:** a spec lint that parses every TOML registry row quoted in a spec and runs it through the grammar of the units ordered before it.

### M4 — Unit 1 registers `deviation` twice, with conflicting writer cells (id 5)

- **Where:** spec-1 §4 "The rows" (the deviation row and the "each build_records.py kind" row) and §2 S2; spec-2 S2, S9 and AC9.
- **What is wrong:** `deviation` has its own row, with writer `hand` and source `deviation_join.py:REQUIRED`. It is also covered by the factory-kinds row, with writer `build_records.py new <kind>`, because PLAY-dOrderedCharter-42 puts it in `TYPED_RECORD_KINDS`. Unit 2 rewrites only `hand` rows (S9) but expects deviation's writer to be `gov_record.py new deviation` (AC9). S2 refuses a kind whose writer names another door.
- **Consequence:** S9 refuses a duplicate name, so the builder cannot tell which row exists. AC9 may be unpassable, and `gov_record.py new deviation` may be refused, along with the exception, override and change kinds. `deviation_join.py:REQUIRED` may also stop being a literal once -7 S7 lands.
- **Fix (skeptic: SOUND):** In unit 1, register `deviation` once, as a factory kind whose `source` is the factory's per-kind table. Drop the separate `hand` row, and note that S2's "five Serves kinds" becomes seven or more once -42 lands. In unit 2, either make the factory kinds' writer cell `gov_record.py new <kind>`, with `build_records.py new` documented as an alias that S2's refusal accepts, or widen S9 to every factory row. AC9 then follows.
- **Left-shift gate:** `check_record_kinds` refuses a kind covered by both a named row and a family row.

### M5 — Unit 1's field check has no locator while every `home` is empty (id 6)

- **Where:** spec-1 §2 S4, §4 Data model and §6 AC1.
- **What is wrong:** S4 grades "every tracked record under its `home`", but unit 1 sets `home = ""` on every row, and `home` is required only from unit 18. AC1 requires per-kind graded and legacy counts, with a non-zero legacy count for deviation.
- **Consequence:** S4 grades nothing at unit 1's pass, so AC1 cannot be produced. The alternative is that the builder invents a path rule, which unit 18's homes later change silently.
- **Fix (skeptic: SOUND):** Require `home` on `fields` rows from unit 1, filling it for unit 1's own rows (for example `memory/builds/*/build/*-deviation-*.md`), and leave only `layer`, `readers` and `lifecycle` to unit 18. Alternatively, state S4's locator explicitly, for example `git ls-files` filtered by the `id-rule` translated to a glob.
- **Left-shift gate:** `check_record_kinds` reds a `fields` row with an empty `home`.

### M6 — Units 20 and 9 spell the authored section tag two ways (id 7)

- **Where:** spec-20 §2 S5 and §6 AC5.
- **What is wrong:** unit 20's retag writes `## [<anchor>] <heading>`, and AC5 expects `[notes-2]`. Unit 9 S1 reads an authored tag only as `## [section.<seg>] Title`.
- **Consequence:** under `memory.legacy-anchors = retag`, retagged sections are not read as authored, because spec-19 S10 and spec-9 read authored tags only. `record show <id>#<tag>` then fails to address them, or they fold to a derived anchor such as `notes-2-notes`.
- **Fix (skeptic: SOUND):** Pick one spelling and use it in both specs. Either unit 20 writes `## [section.<anchor>] <heading>` (AC5 expects `[section.notes-2]`), or unit 9 S1 reads a bare `[<seg>]`. Add a unit 20 criterion that runs unit 9's `extract_section` over a retagged fixture and finds `section.notes-2`.
- **Left-shift gate:** a round-trip arm in which a writer's output is read back through the reader of the same interface.

### M7 — Unit 19's AC1 and AC2 call a `--serves` flag the door does not have (id 8)

- **Where:** spec-19 §6 AC1 and AC2.
- **What is wrong:** both criteria call `gov_record.py new log --build <slug> --serves <unit id>`. Unit 2 defines `--unit`, and unit 19 adds only `--caused-by` and `--edge`.
- **Consequence:** AC1 fails at argument parsing with exit 2, naming neither `log` nor `Caused-by`, and AC2 cannot pass. The alternative is an undeclared alias.
- **Fix (skeptic: SOUND):** Use `gov_record.py new log --build <slug> --unit <unit id>`. If a `--serves` alias is wanted, add it to unit 2's §4 "The command" and to unit 19's inventory.
- **Left-shift gate:** a spec lint that checks every flag in a §6 command against the flags declared in the set.

### M8 — Unit 4's journals row and unit 2's S9 still name the retired `journal` kind (id 9)

- **Where:** spec-4 §4 "The routing region" (journals row) and spec-2 §2 S9.
- **What is wrong and consequence:** this is the same defect as H5, at a medium binding grade. Log records written after unit 18 fall out of the journals row, and unit 2 S9 names a registry row that no longer exists under that name.
- **Fix (skeptic: SOUND):** In unit 4, render the row as "logs: each `build/` record whose `canonical_kind` is `log`", read through unit 18's `canonical_kind`, and add a `consumes-from TOOL-dTotalRecall-18 — canonical_kind` edge. In unit 2 S9, name the row `log`.
- **Left-shift gate:** as for H5.

### M9 — The `stream-plan` kind token is never registered (id 10)

- **Where:** spec-25 §4 Data model and §2 S1.
- **What is wrong:** a stream-plan record opens with a `**Serves:**` line, but `stream-plan` is added to neither `RECORD_KIND_TOKENS` nor `TYPED_RECORD_KINDS`. `read_bindings` marks an unregistered first token as malformed. The spec never states which token the record uses.
- **Consequence:** the first stream-plan record dIndexedDesign's planner writes reds memory hygiene's binding check.
- **Fix (skeptic: SOUND):** State the Serves line, for example `**Serves:** stream-plan <ids>`. Add `stream-plan` to the kind vocabulary: I3's tuple, or `TYPED_RECORD_KINDS` with its factory table, as unit 11 does for shape-run. Add a criterion that plants a stream-plan record and runs `gen_build_index.py --check` green.
- **Left-shift gate:** `check_record_kinds` cross-checks every registered kind against `RECORD_KIND_TOKENS`.

### M10 — The set contradicts itself on the memory-tree kit boundary (ids 11, 32, 33)

- **Where:** spec-26 §2 preconditions and S5; spec-14 §2 preamble, S6 and §3 Edges; spec-9 S3 and S5; spec-8 S7.
- **What is wrong:** units 7 and 8 hold that memory-tree imports no sibling kit, so policy is read through the memory-tree adapter `tools/memory-tree/policy_value.py` (unit 8 S10, F4). Other units break that rule:
  - Unit 26's `gen_atlas.py` (memory-tree) reads `read_policy_value` from `tools/playbook/policy_value.py`, with no edge to unit 8.
  - Unit 14's `gov_map.py` reads `memory.map-budget` and `memory.map-overflow` through the playbook reader, with no edge to unit 8.
  - Units 14, 9 and 8 put memory-tree modules on playbook's `tag_index.py` (`read_namespaces`, `build_index`).
  
  memory-tree's `requires = []`, and no unit adds `playbook`. Only unit 21 declares a cross-kit dependency (memory-recall requires playbook).
- **Consequence:** the builder either imports across kits, which breaks a copy-installed adopter with memory-tree and no playbook, or writes yet another adapter that no spec names.
- **Fix (skeptic: SOUND, all three findings):** Settle the boundary once. Either add `requires = ["playbook"]` to memory-tree under the grant, recorded in one unit (for example unit 8, the first to write through `build_index`) with a §8 fork, or name memory-tree-side adapters for the namespace reader and the index, the way `policy_value.py` is handled. Re-point unit 26 S5 and unit 14 S6 to `tools/memory-tree/policy_value.py` (TOOL-dTotalRecall-8 S10). Add `consumes-from TOOL-dTotalRecall-8 — policy_value.py` edges in both specs, with the reciprocal `hands-off` edges in spec 8.
- **Left-shift gate:** a kit-boundary check that every cross-kit import resolves to a `requires` or `requires_if` row in kit.toml.

### M11 — Unit 9's `record` extractor picks a kind by `home`, which several kinds share (id 12)

- **Where:** spec-9 §2 S1 (the `record` extractor).
- **What is wrong:** the extractor takes a record's kind from "the registry row whose `home` holds the path". Deviation, research, log, shape-run and stream-plan records all live under `memory/builds/*/build/`. Log and research file names are free-form, so no glob can separate them, and the spec states no tie-break.
- **Consequence:** `record find --kind` and the `record.<kind>` tag are wrong or ambiguous for most build-folder records.
- **Fix (skeptic: SOUND):** Derive the kind from the record's Serves token through `read_bindings` and `canonical_kind` (unit 18), and use `home` only to admit the path. State the rule for a path that two homes match.
- **Left-shift gate:** as for H7, refuse overlapping homes.

### M12 — Unit 5's AC7 cannot pass while any reader hit is kept (id 13)

- **Where:** spec-5 §6 AC7, against §4 "The readers".
- **What is wrong:** §4 records non-reader hits "as kept". AC7 requires `--readers` to list no line outside the grammar's entry points, but nothing removes a kept hit from the predicate's output.
- **Consequence:** AC7 stays red on a correct build, because runlog/model.py:1571's `slug_re` is a kept hit. The alternative is that the builder rewrites harmless code to silence the predicate.
- **Fix (skeptic: SOUND):** Give the predicate an exclusion that kept hits carry: a `# slug-grammar: kept <reason>` line marker, or a kept-list file the probe reads. Reword AC7 to "lists no line that is neither an entry point nor marked kept", with a planted unmarked hit as its red case.
- **Left-shift gate:** add "census criterion with a kept disposition but no kept exclusion" to the bug-class checklist.

### M13 — Unit 13's `BUILTIN_ARMED` arms JavaScript against a measured verdict (id 18)

- **Where:** spec-13 §4 "The states" (`BUILTIN_ARMED`).
- **What is wrong:** `js`, `mjs` and `cjs` map to `ts-tokens` under `parser`. The lexicon's `KNOWN_EXTS` maps `js` to `js-regex`/`probe` (tools/lexicon/lexicon.py:117-119), and `ts-tokens` earned `parser` only against TypeScript conformance records.
- **Consequence:** default callers (unit 8's code record, unit 14's map) parse JS with an unmeasured parser. The measured verdict is reversed without a fork, and the two consumers of one primitive disagree on how JS is read.
- **Fix (skeptic: SOUND):** Either mirror `KNOWN_EXTS` (`js` as `js-regex`/`probe`, with no `mjs`, `cjs`, `jsx` or `bash` entries), or add a §8 fork that measures `parse_ts_source` against the tree's JavaScript or a JS conformance set before arming it. Then state in §4 that the default departs from `KNOWN_EXTS`.
- **Left-shift gate:** a parity arm between `BUILTIN_ARMED` and `KNOWN_EXTS`.

### M14 — Unit 12's memory-path match counts the harness's auto-memory directory (id 19)

- **Where:** spec-12 §2 S3 (the memory-path match), with §4 `derive_read_channel`.
- **What is wrong:** any word carrying `/memory/` after backslash folding counts as a memory path. That includes `C:\Users\<u>\.claude\projects\<project>\memory\`.
- **Consequence:** reads of harness notes, or of any other repository's `memory/`, inflate the median that decides the 33,000 B pass or fail.
- **Fix (skeptic: SOUND):** Anchor the match to the repository. Fold `\` to `/`, case-fold the drive letter and map `/c/` to `c:/`. Then accept a word only when it is `<root>/...` relative or starts with `<worktree path>/<root>/`, for this clone's main worktree or one of its `.claude/worktrees/*` worktrees. Add the fixture cases `harness-memory` (expected not counted) and `msys-path` (`/c/projects/<clone>/memory/x.md`, expected counted).
- **Left-shift gate:** a fixture set of path shapes for every path-classifying predicate.
- **Note:** L12 (finding 67) reports the same match at a low binding grade.

### M15 — Unit 6 builds a second cycle walker beside `backlog._scan_cycles` (id 24)

- **Where:** spec-6 §2 S6 and §10.
- **What is wrong:** §10 says no cycle check exists to extend. `tools/memory-tree/backlog.py:1271` has `_scan_cycles`, and gen_build_index.py already imports `backlog`.
- **Consequence:** two walkers can disagree on how a cycle is reported (`_scan_cycles` rotates each cycle to its smallest member, while AC2 expects `xAlpha -> xBeta -> xAlpha`), and the next change will touch only one of them.
- **Fix (skeptic: SOUND):** Lift `_scan_cycles` into a fold-independent `scan_cycles(edges, live=...)` in backlog.py or tree_lib, and make `check_relation_cycles` a thin caller that passes the `after` edges among resolved builds. Correct §10 to name the seam. Add an `ast` probe at the tip that finds one cycle-walking function in memory-tree, called by both V6 and the relation check.
- **Left-shift gate:** a §10 lint that runs a symbol search for the concept's verbs before a "no seam exists" claim is accepted.

### M16 — Unit 19 registers a second legacy ledger over unit 1's population (id 25)

- **Where:** spec-19 §2 S7 and §4 "The population".
- **What is wrong:** unit 19 adds `legacy-records`, keyed by path and section, over the same tracked records as unit 1's `record-kinds-legacy`. The brief's I22 names one population that units 1 and 19 both read.
- **Consequence:** two shrink-only ledgers are seeded at different SHAs (order 1 and order 16). A record written between the two seeds is legacy to one check and new to the other, and every drain must be applied twice.
- **Fix (skeptic: UNSOUND — the skeptic's corrected fix):** Keep one registration under I22, and record a per-check seed point in it. That can be a `check` column (kind-schema, causes) on one ledger keyed by path and section, or two named slices of one population that `legacy_ledger.py` lists together. The causes slice must be seeded at unit 19's landing. Otherwise, amend I22 to declare two populations, give the reason in spec 19 §4 Alternatives, and have spec 19 add `consumes-from TOOL-dTotalRecall-1` for the shared key shape.
- **Left-shift gate:** `legacy_ledger.py` reds two registrations with the same key shape over overlapping paths unless they declare distinct checks.

### M17 — Unit 20's front-matter grader ignores unit 4's legacy rule (id 26)

- **Where:** spec-20 §2 S4 and §8 F3.
- **What is wrong:** `tools/govkit/steps/memory_front_matter.py` grades against `FRONT_MATTER_KEYS` with its own program. Unit 4's `parse_front_matter` reads typed derived keys without refusing them inside the seeded legacy population. F3 wrongly says unit 4 refuses both cases.
- **Consequence:** an adopter's update walk stops on legacy READMEs that type `node:` (AC4 prints `node derived`) while hygiene accepts them. Every scaffolded README types `node`, `roster` and `streams` today.
- **Fix (skeptic: SOUND):** Have the step call `gen_build_index.parse_front_matter`, or a `grade_front_matter` that unit 4 exposes and that unit 4's own refusal also calls. Restate F3 to match. Add a probe: a planted legacy README typing `node:` exits 0 from both the step and `gen_build_index.py --check`.
- **Left-shift gate:** add "two graders of one schema" to the bug-class checklist.

### M18 — Unit 23 adds a per-blob store parallel to PLAY-dOrderedCharter-44's (id 27)

- **Where:** spec-23 §2 S1 and S2, and §4 "The row and its key".
- **What is wrong:** S1 and S2 add `leg_row(blob, reader, version, payload)`, a `LEG_READERS` registry and a version that includes `params(root)`. PLAY-dOrderedCharter-44 already provides the `blob_parsed` ledger, extractor registration (I12) and a module-bytes version.
- **Consequence:** the index holds two extractor registries and two version rules. Leg readers are invisible to `gov_tag.py check` and to 44's schema stamp, and a later version-rule change (PLAY-dOrderedCharter-51) must be made twice.
- **Fix (skeptic: SOUND):** Extend 44's version rule with an optional params digest. Register `unfenced-head` and `id-harvest` through the extractor mechanism, either as rows writing `blob_row` with the payload in `text` or as a declared non-tag extractor class, so `blob_parsed` is the one freshness ledger. If a separate table is kept, add it to §4 as an alternative with its reason. Add a probe: editing a reader module re-runs it through `build_index`'s own ledger.
- **Left-shift gate:** an index-schema check that refuses a second table holding the shape `(blob, *, version)`.

### M19 — Unit 21 adds `fts_blob` as a second freshness ledger (id 28)

- **Where:** spec-21 §2 S2.
- **What is wrong:** `fts_blob(blob, digest)` is recall's own ledger inside `build_index`, keyed on a hand-assembled digest. The FTS extraction is not registered as an extractor under PLAY-dOrderedCharter-44's `blob_parsed`.
- **Consequence:** the index holds two staleness rules. Unit 23's S5 copies FTS rows by `fts_blob`'s digest while every other row follows 44's versions, so recall and the tag index can disagree on whether a blob is current.
- **Fix (skeptic: SOUND):** Register the record and chunk extraction as an extractor of the namespace registry, so that `blob_parsed` is its ledger. Fold `CACHE_VERSION`, `CHUNK_MAX`, the conf digest and the alias digest into a params-aware extension of 44's version, shared with unit 23. Drop `fts_blob`, or justify keeping it in §4.
- **Left-shift gate:** as for M18.

### M20 — Unit 1's generated field check duplicates the owners' graders (id 29)

- **Where:** spec-1 §2 S4 and §6 AC7.
- **What is wrong:** S4 re-implements missing-field grading that `deviation_join.read_record`, PLAY-dOrderedCharter-7 S7's `read_record` and `read_bindings` already do. It adds a row-order rule and its own legacy ledger, and it uses a `**Key:**` grammar where `FIELD` requires `- **Key:**`.
- **Consequence:** the deviation join and the record-kinds gate grade one rule differently, so a record can pass one and red the other. AC7 plants a case the join already reports. The skeptic notes that the door runs both checks, so the divergence is between the join and the gate, not at the door.
- **Fix (skeptic: SOUND):** For rows whose `schema.source` names an owner literal, have `check_record_kinds` call that owner's reader (`build_records.read_record` or `deviation_join.read_record`) over the population, and generate a check only for kinds no owner grades. Alternatively, make S4's check the one function that `read_record` and the door both call. State the extended predicate in §10.
- **Left-shift gate:** as for M17.

### M21 — Unit 16's purpose census duplicates PLAY-dOrderedCharter-22's `purpose` arm (id 30)

- **Where:** spec-16 §2 S3, §4 "The values" (refuse row) and §6 AC5.
- **What is wrong:** `record_kinds.py --purpose-review` and `--check` build their own census over `namespaces.toml` members and `chain.toml` rows. 22's `check_namespace_purpose` and `read_chain_registry` already grade both, including the awaiting-PM-5 exemption.
- **Consequence:** under `refuse`, record_kinds.py reds while 22's arm passes the same rows as awaiting. S3's "field absent" case cannot occur, because 22 S2 already reds it.
- **Fix (skeptic: SOUND):** Have `memory.map-purpose` drive the existing `purpose` arm: under `refuse`, 22's awaiting exemption ends. Have `--purpose-review` read through `read_chain_registry` and 22's member enumeration. Name `check_namespace_purpose` in §10, and limit record_kinds.py's own grade to the registry's own rows.
- **Left-shift gate:** as for M15, a seam search before "no seam fits".

### M22 — Unit 9's `sections` column is a third copy of the spec canon (id 31)

- **Where:** spec-9 §2 S2 and §4 "The section table".
- **What is wrong:** the column re-declares §1 to §10, all with `required = true`. The canon already exists as hygiene's `SPEC_CANON`/`SPEC_CANON10` and as `gen_build_index.py`'s `SPEC_TITLE_NUMBERS`, and nothing ties the new column to either. Hygiene makes §5 and §10 optional for Tier-1 specs and date-gates §10.
- **Consequence:** a Tier-1 `new spec` through the door (AC3), or a renumbered template, is refused or tagged differently by the door and by hygiene.
- **Fix (skeptic: SOUND):** Derive the spec row's `sections` from `SPEC_TITLE_NUMBERS`, through unit 1's `schema.source` or a parity arm, with required flags taken from check 12's tier rules. Alternatively, make the registry the source and re-point check 12 and `SPEC_TITLE_NUMBERS` to it. Name the existing canon in §10.
- **Left-shift gate:** a parity arm across every spelling of the spec section canon.

### M23 — Unit 21 adds `playbook` to memory-recall's `requires` without updating the copy-install runbook (id 37)

- **Where:** spec-21 §2 S4 and §4 Files touched.
- **What is wrong:** WIRE-INTO-PROJECT.md §0 (:127) and §3c (:582-586) tell adopters that memory-recall needs only memory-tree, and they install with `cp -r`, so govkit's `requires` join never runs.
- **Consequence:** a copy-install adopter's `query.py` cannot resolve `tag_index.py`, and recall breaks on install. The skeptic graded this medium because the failure is loud.
- **Fix (skeptic: SOUND):** Add WIRE-INTO-PROJECT.md to Files touched, and state in §0 and §3c step 1 that `<prefix>/playbook/` must also sit beside memory-recall. Add a criterion: with no playbook kit beside it, `query.py` exits non-zero and names the missing kit.
- **Left-shift gate:** a parity check between each kit's `requires` and the runbook's install lines.

### M24 — Unit 21 edits verbatim-pinned files without naming the pin (id 38)

- **Where:** spec-21 §2 S1 Readers and §4 Files touched.
- **What is wrong:** `bench.py` (:88, :454) and `union.py` (:96) are renamed. Both are digest-pinned in `tools/memory-recall/verbatim.json`, and union.py is "re-pulled WHOLESALE" from upstream.
- **Consequence:** `test_verbatim_files` reds the memory-recall kit selftest, and the next upstream re-pull silently restores the old name.
- **Fix (skeptic: SOUND):** Add `verbatim.json` to Files touched, re-stamped with a stated reason the way the bench.py fork is. Either keep union.py byte-identical by having it reach the builder through a `bench.py` alias, or record the fork in the selftest docstring and the README's verbatim table.
- **Left-shift gate:** a spec lint that reds a Files-touched path pinned in any `verbatim.json` unless the pin file is also listed.

### M25 — Unit 4's front-matter refusal reds about 55 fixture READMEs (id 39)

- **Where:** spec-4 §2 S4, §4 Files touched and §7.
- **What is wrong:** fixtures in ten suites plant READMEs that type `node`, `roster` and `streams` in scratch repos, which fall outside the legacy seed. None of those fixtures is listed. §7 omits `corpus-ids selftest`, `backlog migration selftest` and `unattended-build self-test`.
- **Consequence:** check 9 refuses them, which reds the hygiene self-test, the build-index, corpus-ids and backlog-migration selftests, and the unattended suites. The fixes then happen fixture by fixture, outside the spec.
- **Fix (skeptic: SOUND):** Add the fixtures to Files touched and choose one rule: strip the three keys from fixture READMEs, or give each fixture tree its own legacy seed. Add the three legs to §7, and name the held unattended shards in prose. Run each suite once after the refusal lands and observe it green.
- **Left-shift gate:** a spec lint in which a new refusal greps `tools/` fixtures for the refused shape.

### M26 — Leg-adding specs omit the meta-gate rows every new leg needs (id 40)

- **Where:** spec-11 §2 S6, §4 Files touched and §7. The same gap is in spec-19 S12, spec-22 S6 and spec-26 S10, and partly in spec-1 and spec-8 §7.
- **What is wrong:** the specs list none or only some of the rows a new leg needs:
  - a `[[gate_leg]]` or `[[exempt_leg]]` row;
  - `subject-pins.tsv`;
  - `ceiling-evidence.txt`;
  - a dossier `gate-legs` claim;
  - a regenerated `memory/map/generated/`.
  
  §7 omits the legs that grade those rows.
- **Consequence:** govkit selfcheck, `derive-ceilings --check` and codebase-map coverage all red. None of them has a guard, so the spec-tokens join never forces them into §7.
- **Fix (skeptic: SOUND):** In each leg-adding spec, list in Files touched:
  - `tools/govkit/subject-pins.tsv` (`govkit.py selfcheck --write`);
  - `tools/run-gates/ceiling-evidence.txt`;
  - the kit.toml `[[gate_leg]]` row or a registry `[[exempt_leg]]` row;
  - the owning dossier;
  - `memory/map/generated/` (`gen_map.py --write`).
  
  Add `govkit selfcheck`, `leg ceilings clear their evidenced maximum` and `codebase-map coverage + freshness` to §7, as spec 15 does. Choose dossiers deliberately: memory-tree-hygiene.md has 194 bytes left under DOSSIER_CAP_BYTES.
- **Left-shift gate:** a spec lint that, when a spec adds a gate-legs.json row, requires the four rows in Files touched.

### M27 — No spec regenerates `symbols.json` (id 41)

- **Where:** spec-1 §4 Files touched and §7, and every spec that mints or retires a Python symbol.
- **What is wrong:** `codebase-map coverage + freshness` byte-compares `memory/map/generated/symbols.json`, but no spec lists that file or `gen_map.py`.
- **Consequence:** every such pass reds the unguarded leg until the close. The previous chain build spent TOOL-dTrueNorth-27 clearing nine red legs.
- **Fix (skeptic: SOUND):** In every spec whose inventory mints or retires a Python symbol, add `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`) to Files touched and `codebase-map coverage + freshness` to §7. Alternatively, record one build-level rule that the close regenerates it.
- **Left-shift gate:** the same Files-touched lint as M26, keyed on minted or retired symbols.

### M28 — Specs with "Naming cells" omit the lexicon leg (id 42)

- **Where:** spec-1 §4 Inventory "Naming cells" against §7, and the same in 21 other specs.
- **What is wrong:** 22 specs say their names are "asked of `--suggest`", but only specs 9 and 14 put `lexicon naming predicates` in §7. `--suggest` is advisory and fails nothing.
- **Consequence:** a bad name reds the lexicon leg only at the close. Re-probing flagged `canonical_kind` (spec 18) and `ensure_index`.
- **Fix (skeptic: SOUND):** Add `lexicon naming predicates` to the §7 leg line of every spec whose Inventory has a "Naming cells" line.
- **Left-shift gate:** a spec lint that requires the lexicon leg wherever "Naming cells" appears.

### M29 — Unit 5's §7 omits the suites of the readers it re-points (id 43)

- **Where:** spec-5 §7 (and §3, "the readers' own suites are the arms").
- **What is wrong:** spec 5 edits row_grammar.py, merge-rows.py, check-arms.py, migrate_backlog.py, routed_commits.py and run-gates.sh. §7 names none of the legs that run them. Specs 3, 7, 18, 20 and 23 edit gen_build_index.py and omit `build README slot contract`.
- **Consequence:** a broken re-point passes every named leg. The guards are broad, so the join stays silent.
- **Fix (skeptic: SOUND):** Add to spec 5's §7 leg line:
  - `row-grammar selftest`;
  - `row-keyed merge driver replay`;
  - `row-driver view refusal`;
  - `check-arms selftest`;
  - `harness arms (fail branches armed or pinned)`;
  - `backlog migration selftest`;
  - `routed commits name a specced unit`;
  - `build README slot contract`;
  - `run-gates canary`.
  
  Add `build README slot contract` to specs 3, 7, 18, 20 and 23.
- **Left-shift gate:** a spec lint that joins Files touched against each leg's argv files, not only its guards.

### M30 — Specs 26, 13 and 12 omit the leg that runs their new arm or edited file (id 44)

- **Where:** spec-26 §7, spec-13 §7 and spec-12 §7.
- **What is wrong:** each spec edits a file or adds an arm that a leg its §7 does not name would run:
  - Spec 26 declares an arm in `tools/lib/resolve-python.test.sh` (AC12) but omits `python resolver (behaviour + inline parity + idiom ban)`.
  - Spec 13 edits drift_report.py and lexicon.py but omits `drift-audit records` and `lexicon naming predicates`.
  - Spec 12 edits runlog.py but omits `runlog record schema`.
- **Consequence:** a drifted inline copy of `help_pages`, or a breakage in those files, is checked by no named leg.
- **Fix (skeptic: SOUND):** Add those legs to the three §7 leg lines.
- **Left-shift gate:** as for M29.

### M31 — Unit 9 moves `search` and `rrf` without updating the rank scenarios (id 45)

- **Where:** spec-9 §2 S3 and §4 Files touched.
- **What is wrong:** `tools/codebase-map/scen-adversarial.json` ADV-05 and ADV-06 still expect `query.py`.
- **Consequence:** the reuse-recall figure drops for a reason unrelated to ranking, which misleads dLinkedLibrary's measurement.
- **Fix (skeptic: SOUND):** Add scen-adversarial.json to Files touched, re-pointing ADV-05 and ADV-06's `expected_file` and `established_by` to `{prefix}/memory-tree/record_find.py`. Update the comment at `tools/memory-recall/selftest.py:1906`.
- **Left-shift gate:** a lint that reds a scenario whose `expected_file` lacks its symbol.

### M32 — Unit 18's rename misses SESSION-KICKOFF.md (id 46)

- **Where:** spec-18 §2 S7 Readers and the S9 prose.
- **What is wrong:** `memory/guides/SESSION-KICKOFF.md:63` still tells every session that an acceptance ledger goes in a `journal` record. AC7 greps only `tools`.
- **Consequence:** every kickoff keeps instructing agents to write the retired kind, against S8.
- **Fix (skeptic: SOUND):** Add SESSION-KICKOFF.md to S9 and to Files touched, re-spelled "in a `log` record (`journal` read as its alias)", with the manifest's `last-audit` re-stamped. Widen AC7 to `-- tools memory/guides skills`. The skeptic notes that the prose edit is what cures this, because the widened AC7 pattern does not match the prose line.
- **Left-shift gate:** rename inventories grep `memory/guides` and `skills` for the retired token in prose.

### M33 — Unit 13 hashes raw disk bytes as git's blob id (id 48)

- **Where:** spec-13 §4 "The states" (the worktree row) and AC3.
- **What is wrong:** under `core.autocrlf` or `text=auto`, which this node uses, raw-byte sha1 does not equal git's id. For lexicon.py the probe gave 56df4068… against 9625f145…. Missing-on-disk paths and symlinks are unspecified.
- **Consequence:** the `(blob, ext)` cache is never shared across states. A deleted path has no defined result, and a symlink is read as its target. AC3's fresh LF fixture cannot see the CRLF case. The skeptic graded this medium because the worktree ids feed only the cache.
- **Fix (skeptic: SOUND):** Get ids from `git hash-object --stdin-paths` (one spawn, filters applied), or from `git ls-files -s` plus `git diff --name-only` for unmodified paths. State the result for a path absent on disk and for mode 120000 (read the link text). Add an AC3 case with `core.autocrlf=true` and a CRLF checkout, expecting the id to equal `git hash-object <path>`.
- **Left-shift gate:** add "hand-computed git object id" to the bug-class checklist.

### M34 — Unit 2's `--field` values can inject record lines (id 50)

- **Where:** spec-2 §4 "The command" and S4.
- **What is wrong:** values are written verbatim with no CR/LF refusal. A multi-line value can inject `- **Key:**` lines, a second `**Serves:**` binding or a heading.
- **Consequence:** through the one sanctioned door, a caller can forge `**Supersedes:**`, `**Bound:**` or `**Surface:**` on a deviation, or bind the record to another unit. The skeptic graded this medium because callers could pass many of those keys directly.
- **Fix (skeptic: SOUND):** Refuse at the door, with exit 2 naming the field, any `--field`, `--title`, `--caused-by` or `--edge` value holding CR or LF. F2 still stands. Add an AC: `--field Reason=$'x\n- **Supersedes:** <stem>'` exits 2, and `git status --porcelain` stays empty.
- **Left-shift gate:** as for H6.

### M35 — Unit 21 reports a locked database as corruption (id 52)

- **Where:** spec-21 §5 error states and AC5, and §4 "The flow".
- **What is wrong:** `sqlite3.OperationalError` (busy or locked) is a subclass of `DatabaseError`, which the spec maps to "corrupt, run `gov_tag.py --rebuild`".
- **Consequence:** concurrent worktree queries are the normal case. In them, the operator is told to rebuild a live shared index.
- **Fix (skeptic: SOUND):** Set a busy timeout on every connection. Map a locked or busy `OperationalError` to a named `index busy` refusal or a retry, and keep `--rebuild` for any other `DatabaseError`. Add a selftest arm: one process holds a write transaction while a query runs, and the query does not print `--rebuild`.
- **Left-shift gate:** add "except a base class whose subclass means something else" to the bug-class checklist.

### M36 — Unit 21's index grows without bound (id 53)

- **Where:** spec-21 §2 S2, S3 and S6.
- **What is wrong:** FTS rows keyed by digest and dirty rows keyed by worktree are never deleted, and S6 retires eviction and the budget.
- **Consequence:** every conf, alias, `CHUNK_MAX` or `CACHE_VERSION` change adds a full corpus copy, and removed worktrees leave their rows behind. index.db grows with nothing able to shrink it.
- **Fix (skeptic: UNSOUND — the skeptic's corrected fix):** In `build_index`'s transaction:
  - (a) delete every fts_record, fts_chunk, fts_blob and fts_supersession row whose digest no live worktree's conf derives, regardless of blob;
  - (b) at a live digest, delete rows whose blob is held by no `tree_path` row of any live worktree's HEAD tree and by no `dirty_path` row;
  - (c) delete `dirty_path` and dirty fts rows whose worktree `git worktree list` no longer names.
  
  Report freed rows on the index line. Add an AC: change FAMILIES twice and assert the fts row count stays at one corpus copy.
- **Left-shift gate:** a spec lint that requires a deletion rule for any new keyed table when eviction is retired.

### M37 — Unit 4's refusing parser is silent on a repeated key (id 56)

- **Where:** spec-4 §2 S2.
- **What is wrong:** `parse_front_matter` keeps the last value of a repeated key.
- **Consequence:** a repeated `ids:` or `depends-on:` silently drops the first list, which is the silent-drop class this unit exists to close.
- **Fix (skeptic: SOUND):** A key given twice raises `StaleHeader`, naming the key and both line numbers. Add an AC2 case with two `ids:` lines.
- **Left-shift gate:** add "repeated key, last one wins" to the bug-class checklist.

### M38 — Unit 18's `GIT_OWN` omits git's transient and optional common-dir entries (id 57)

- **Where:** spec-18 §4 "The pockets" (`GIT_OWN`) and S6.
- **What is wrong:** the list lacks:
  - `*.lock`;
  - `MERGE_MSG`, `MERGE_MODE` and `AUTO_MERGE`;
  - `REBASE_HEAD`, `rebase-merge/` and `rebase-apply/`;
  - `sequencer/` and `BISECT_*`;
  - `rr-cache/`, `gc.pid` and `lfs/`.
- **Consequence:** the record-kinds leg reds during a merge, rebase, cherry-pick or bisect, races any concurrent git lock, and reds permanently under git-lfs.
- **Fix (skeptic: SOUND):** Make `GIT_OWN` a pattern set covering git's documented common-dir state. Better still, grade only entries older than the run's start, or entries not matching `*.lock`. Add an AC4 case: a planted `index.lock` and `MERGE_MSG` read green.
- **Left-shift gate:** a fixture of git's transient state run against every common-dir scanner.

### M39 — Unit 14's shared map cache is not written atomically (id 58)

- **Where:** spec-14 §2 S7 (the cache).
- **What is wrong:** `<git-common-dir>/gov/map/<tree>.map` is shared by every worktree and validated only by its first-line stamp. No atomic write is specified.
- **Consequence:** a truncated body behind a valid stamp is served, so the map loses nodes.
- **Fix (skeptic: SOUND):** Write to a temp file in the same directory and `os.replace` it into place. Have the reader check a trailing byte-count or digest line before serving. Add an AC6 case: a file truncated after its stamp line is re-rendered, not served.
- **Left-shift gate:** add "shared cache file without atomic write" to the bug-class checklist.

### M40 — Unit 2's mint can overwrite an untracked file (id 60)

- **Where:** spec-2 §4 "Minting" and "Idempotence".
- **What is wrong:** `<n>` is chosen over tracked and staged files only, and the write is not an exclusive create.
- **Consequence:** an unstaged draft, or a file left by an earlier run whose `git add` failed, is overwritten silently.
- **Fix (skeptic: SOUND):** Open with `open(path, 'x')`. On collision, take the next n or refuse naming the untracked file. Count untracked files in the home when computing the next free n. Add an AC: an untracked `-deviation-<n>.md` makes the door write `<n+1>` and leaves the draft byte-identical.
- **Left-shift gate:** as for M39, add "write without exclusive create" to the checklist.

### M41 — Unit 10's derived anchors can collide with authored tags (id 62)

- **Where:** spec-10 §2 S1 and S3.
- **What is wrong:** `seen` holds only derived anchors, and S3 grades uniqueness of authored tags alone. `## [section.findings] Notes` followed by `## Findings` therefore gives both sections the address `section.findings`.
- **Consequence:** `record show <key>#section.findings` (unit 9) can return the wrong section.
- **Fix (skeptic: SOUND):** Every caller seeds `seen` with the record's authored tags before deriving any anchor, and S1's contract says so. Extend AC1 and the repeat-heading fixture so that the untagged heading derives `findings-2`.
- **Left-shift gate:** a uniqueness check over the union of authored and derived anchors.

### M42 — Unit 22's cardinality leg certifies zero when memory-tree is absent (id 63)

- **Where:** spec-22 §2 S3 and S5, and §4 "The count".
- **What is wrong:** the playbook-kit leg depends on memory-tree's `design_lib.py` and `gen_build_index.py --print-relations`. Playbook does not require memory-tree, and the absent case is unspecified.
- **Consequence:** the leg either crashes on import or, if guarded, prints "read 0 edges" and exits 0. The check then certifies cardinality it never counted.
- **Fix (skeptic: SOUND):** With memory-tree unresolved, `--cardinality` exits 2 naming the kit, or prints `unarmed`, and never prints `0 violations`. Add an AC that runs in a scratch copy with tools/memory-tree removed.
- **Left-shift gate:** add "empty population from a missing dependency reads as a pass" to the bug-class checklist.

### M43 — Unit 26's Mermaid labels and table cells are not escaped (id 64)

- **Where:** spec-26 §4 "The pages".
- **What is wrong:** node labels and cells are emitted raw. 22 of the 142 leg names hold `(`, `)`, `[`, `]` or quotes.
- **Consequence:** those flowcharts fail to render on GitHub, and a `|` in a cell splits the table row. Byte-compare and parity stay green over unreadable pages.
- **Fix (skeptic: SOUND):** Emit labels as `id["…"]` with `"` encoded as `#quot;`. Escape `|` as `\|`, and escape backticks, in cells. Add an `--plant` case whose key holds `(x)` and `|`.
- **Left-shift gate:** a render arm that parses the emitted Mermaid.

### M44 — Unit 16's purpose write reaches files §5 does not price (id 65)

- **Where:** spec-16 §2 S4, against §5 security and Files touched.
- **What is wrong:** `--write` writes into each namespace member's `purpose-source` file, which sits in another kit or another build. §5 claims the review writes only registries and the backlog.
- **Consequence:** the review makes unreviewed cross-kit writes, or the `--dispatch --writes` set refuses them. Writes into generated files are reverted by the next render, and parity legs red.
- **Fix (skeptic: SOUND):** Name the write surface in §5. Refuse writes into generated or rendered paths and draft an ask instead. List or derive the member files in Files touched or in `--writes`. Add an AC4 case where a member's purpose sits in a generated file.
- **Left-shift gate:** a spec lint that compares every §2 write target with §5 and Files touched.

## Low

### L1 — Unit 14's AC7 measures a byte count the header does not carry (id 15)

- **Where:** spec-14 §6 AC7, against §2 S5.
- **What is wrong:** AC7 reads "the header's byte count", but S5's header grammar has no byte field.
- **Consequence:** the criterion's wording is unbuildable, although the intent (the whole map's size) is clear.
- **Fix (skeptic: SOUND):** Reword AC7 as "the byte length of `python gov_map.py`'s stdout is at most 32,768", or add `bytes <n>` to the header grammar and to unit 15's `budget` check.
- **Left-shift gate:** a lint that a criterion's observed field exists in the design.

### L2 — Unit 22 claims a playbook-to-design_lib reach that is DEFERRED (id 20)

- **Where:** spec-22 §4 "The count" and §10.
- **What is wrong:** `derive_pin_hash` and the playbook kit's design_lib reach do not exist at base. They belong to the DEFERRED PLAY-dOrderedCharter-24 S7, and F5 omits them.
- **Consequence:** a builder re-grounding on F5's list would treat the reach as landed.
- **Fix (skeptic: SOUND):** Say in §4 and §10 that the reach is 24 S7's and DEFERRED at base, and add both to §8 F5's re-ground list.
- **Left-shift gate:** a §10 "verified at base" claim must cite a grep that prints.

### L3 — Unit 7 gives a false reason for the memory-tree policy adapter (id 21)

- **Where:** spec-7 §4 "The policy read".
- **What is wrong:** the spec says memory-tree imports no sibling kit. It does: drift_report is imported through `resolve_kit_dir`, declared in `requires_if`.
- **Consequence:** the wrong rationale will mislead the next change. The design itself is unaffected.
- **Fix (skeptic: SOUND):** Restate the reason: memory-tree's `requires = []`, so a sibling import must be optional and declared in `requires_if`. The adapter keeps the policy read degradable when no policy kit resolves.
- **Left-shift gate:** as for L2.

### L4 — Unit 18's `journal` count is stale (id 22)

- **Where:** spec-18 §3 (the rewriting non-goal) and §4 "Alternatives rejected".
- **What is wrong:** the spec states 1,443 `journal` records, while 2,025 exist at base 462d20f3.
- **Consequence:** the prose understates the alias population by about 40%. No behaviour depends on the figure.
- **Fix (skeptic: SOUND):** Replace the figure with 2,025, from `git grep -lE '^\*\*Serves:\*\* *journal' 462d20f3 -- memory`, marked PINNED with its date, or drop the count.
- **Left-shift gate:** figures in specs carry a PINNED command.

### L5 — Unit 9's `class` extractor re-parses gotcha front matter (id 34)

- **Where:** spec-9 §2 S1 (the `class` extractor).
- **What is wrong:** the extractor requires a literal `kind: class`. `gotchas.build_record` defaults a missing `kind:` to `class`.
- **Consequence:** the counts agree today (145 gotchas). A future gotcha that omits the key would split between the two parsers.
- **Fix (skeptic: SOUND):** Have `extract_class` call `gotchas.build_record(rel, text)`, select `kind == "class"`, and name gotchas.py in §10.
- **Left-shift gate:** as for M17.

### L6 — Units 12 and 17 build two transcript result-byte counters (id 35)

- **Where:** spec-12 §2 S4 and §10.
- **What is wrong:** `measure_agent_memory` duplicates unit 17's `measure_bytes_before_act` over the same runlog readers.
- **Consequence:** the two counters can parse content shapes differently, so the map-replay's bytes term and the 33 KB re-measure disagree.
- **Fix (skeptic: SOUND):** Factor one `read_result_bytes(records)` into `tools/runlog/extract.py` or `memory_measure.py`, call it from both, and declare the edge between the two specs.
- **Left-shift gate:** as for M15.

### L7 — Specs editing watched files omit the kickoff re-stamp (id 47)

- **Where:** spec-19 §4 Files touched and §7, and the same in specs 1, 5, 8, 9, 11, 15, 18, 21, 22 and 26.
- **What is wrong:** these specs edit paths on SESSION-KICKOFF.md's `watch:` list without listing the `last-audit` re-stamp or the `kickoff-manifest ratchet` leg.
- **Consequence:** each such pass reds the unguarded ratchet leg (C5) until someone re-stamps the manifest.
- **Fix (skeptic: SOUND):** Add the re-stamp, with a delta line, to Files touched and `kickoff-manifest ratchet` to §7. Alternatively, state one build-level re-stamp rule.
- **Left-shift gate:** the Files-touched lint from M26, keyed on the `watch:` list.

### L8 — Unit 8 does not say what happens to a degraded tree's cached record (id 54)

- **Where:** spec-8 §2 S7, S8 and S9, and §4 "Bounds" (the time row).
- **What is wrong:** the spec does not say whether a degraded record is cached or re-derived.
- **Consequence:** a degraded tree may stay degraded until HEAD moves, which sends readers to the git-grep floor. The skeptic graded this low, noting that AC7 already covers `--check`.
- **Fix (skeptic: SOUND):** Never write a degraded record to the per-tree cache, or write it marked and re-derive it on the next run. `--check` on a degraded record reports `degraded`. Extend AC7: run twice with `--ceiling 0.01`, then once with no ceiling, and the third run re-derives fully.
- **Left-shift gate:** none beyond the AC.

### L9 — Unit 8 re-parses blobs that yield no rows on every run (id 55)

- **Where:** spec-8 §2 S7 and AC5.
- **What is wrong:** the cache-hit test is "the blob holds rows", so an empty or unparseable blob is re-parsed every time.
- **Consequence:** this costs performance at adopters only, and AC5's count reads above 1 there.
- **Fix (skeptic: SOUND):** Write a marker row such as `code_blob(blob, extractors, status)` even when a blob yields zero rows, and key the hit test on it. Add an AC5 fixture with an empty `__init__.py` and a syntax-error `.py`.
- **Left-shift gate:** add "cache keyed on presence of output" to the bug-class checklist.

### L10 — Unit 1's `record_kinds.py new` validates no name, tag or field grammar (id 59)

- **Where:** spec-1 §2 S9 and §4 "Factory".
- **What is wrong:** `new` accepts any name, any `record.<x>` tag and any field key, and writes them with no TOML escaping.
- **Consequence:** unvalidated names, tags and fields reach the registry, and a quote or newline can corrupt record-kinds.toml. The skeptic graded this low.
- **Fix (skeptic: UNSOUND — the skeptic's corrected fix):** Have `new` refuse, with exit 2 and nothing written:
  - a name, or a tag's segment after `record.`, that does not match `[a-z0-9][a-z0-9-]*` whole;
  - a tag that is not `record.<name>`;
  - a `--field` key holding `*`, `:`, a quote, a backslash or a newline.
  
  Apply FIELD's key group only to a kind whose writer is a build_records.py factory kind. Write the row through a TOML serializer. Add AC10 cases for `--tag record.Widget` and `--field 'a"b'`.
- **Left-shift gate:** registry writers go through a serializer, never string formatting.

### L11 — Unit 25's `check_stream_plan` misses three malformed shapes (id 66)

- **Where:** spec-25 §2 S3 (`check_stream_plan`).
- **What is wrong:** the check does not red a repeated stream name, a foreign or malformed unit id, or a second `toml` fence.
- **Consequence:** runtime's pick could merge streams or schedule a nonexistent unit. The population is unarmed today.
- **Fix (skeptic: SOUND):** Add the three reds. A foreign or malformed id is one that `grammar_for(root).ID_RE` does not match whole, or that the build's README `ids:` or derived units do not define. Add the fixture plants `stream-name-twice`, `stream-foreign-unit` and `stream-two-fences`.
- **Left-shift gate:** none beyond the plants.

### L12 — Unit 12's memory-path match is not anchored to this clone (id 67)

- **Where:** spec-12 §2 S3.
- **What is wrong:** any absolute path holding `/memory/` counts, while a bare `memory` word (`ls memory`) does not.
- **Consequence:** the instrument's median is skewed in either direction.
- **Fix (skeptic: SOUND):** A relative word must start with `<root>/` or equal `<root>`. An absolute word must start with the clone's main worktree, or one of its `.claude/worktrees/*` roots, followed by `/<root>/`. Add the fixture plants `foreign-memory-path` (counted zero) and `bare-root` (counted).
- **Left-shift gate:** as for M14.
- **Note:** M14 (finding 19) reports the harness-memory case of this match at a medium binding grade.

### L13 — Unit 3's replay detection looks back only 64 commits (id 68)

- **Where:** spec-3 §4 "The counter", step 2.
- **What is wrong:** replay detection reads only 64 first-parent commits.
- **Consequence:** an older replay on a busy family ref is minted a second id, which breaks S4's idempotence.
- **Fix (skeptic: SOUND):** Walk the whole first-parent history, or keep a claimant index in the tip commit's tree. Add an AC3 case with 65 intervening mints.
- **Left-shift gate:** add "bounded lookback behind an unbounded promise" to the bug-class checklist.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=68 confirmed=66 refuted=2 unverified=0 blocker=0 high=7 medium=46 low=13 agents=11 out-tokens=332820

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-19.md:section 2 S8, S7; section 3 | high | high | confirmed | In spec-19, S8 marks a tracked record red when it has no `<path> -` legacy row, is not a root kind and has no Caused-by. S3 makes only build-readme and claim roots. S7's ledger is shrink-only and seeded once. S5 says record keys cover the build, review and prompt folders, so review records are graded. In spec-1's rows, spec-audit and diff-review are written by `tier2-review.js`, and journal and research by `hand`. I grepped tools/workflows/*.js, tools/roles/handoff.py and tools/runlog/record.py for Caused-by or Made-by and got nothing. No spec in the set changes those writers to emit a cause. Unit 19's non-goals rule out rewriting landed records, but nothing covers new ones. So the next harness-written review record after the seed reds the new leg. | sound | - |
| 2 | coherence | memory/builds/dTotalRecall/README.md:section 'The problem this build exists to solve' / Expected improvements, against every subject spec | high | medium | confirmed | README.md:18 lists gap-mem-16 among the owned gaps, and so does packet line 144. `grep -rn mem-16` under memory/builds/dTotalRecall/spec printed nothing. A grep for period, maintenance or currency homes in the specs finds no scope that gives non-build records a home. No unit carries the gap, and no criterion closes it. | sound | - |
| 3 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-21.md:section 6 AC1 against section 2 S4, S8 | high | medium | confirmed | In spec-21, AC1 (line 219) requires `git grep -n "build_index("` over tools/memory-recall to print nothing. But S4 (lines 66-67) has query.py's ensure_index build through `tag_index.build_index`, and S8 (lines 102-103) has check-recall.py's build_served_dir do the same. A correct build therefore contains the substring `build_index(` in memory-recall, so AC1 cannot pass without aliasing the very writer S1 wants named once. | sound | - |
| 4 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-11.md:section 4 'The row'; section 6 AC7 (and the same rows in spec-7 §4 'The ask row' and AC8, spec-3 §4 'The registry row', spec-4 §4 'The registry row') | high | medium | confirmed | The rows break the grammar of the units that land before them: - Spec-11:154-162 writes `layer = "memory"`, `home = "memory/builds/<slug>/build/"`, script-name readers and a prose lifecycle, and has no purpose. - Spec-7:144-150 has the same shape. - Spec-3:155/160 writes `layer = "core"` and `readers = []` with no readers-none. - Spec-4:199-207 does the same, and its home is `<memory-root>/...`. Unit 18 is order 4. Its S1 and Columns table require a lifecycle from the closed set, a layer tag (`layer.memory`), read-key readers or `[]` with readers-none, and a glob home. Unit 16 is order 5, and its S2 reds a row with no purpose. Units 11, 7, 3 and 4 are orders 14, 13, 11 and 8, all after those rules land. So spec-11 AC7 and spec-7 AC8 ('row passes check_record_kinds') cannot pass as written. | sound | - |
| 5 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md:section 4 'The rows' (deviation row and 'each build_records.py kind' row); section 2 S2; spec-2 S2, S9 and AC9 | medium | medium | confirmed | Spec-1 registers `deviation` twice: - line 173 gives it its own row: writer `hand`, source `deviation_join.py:REQUIRED`; - line 178 adds 'each build_records.py kind', writer `build_records.py new <kind>`. PLAY-dOrderedCharter-42 S1-S2 puts deviation in TYPED_RECORD_KINDS, which is the factory's kind list, and -7 S7 moves each kind's required fields into the factory. So deviation is covered by both rows, with conflicting writer and source cells. Spec-2 S9 rewrites only `hand` rows, while AC9 expects deviation's writer to be `gov_record.py new deviation`. And S2 refuses a kind whose writer names another door. The set never resolves which row exists. | sound | - |
| 6 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md:section 2 S4; section 4 Data model; section 6 AC1 | medium | medium | confirmed | In spec-1, the data model (lines 130-131) sets `home = ""`, and S1 makes home required only from unit 18. Yet S4 grades 'every tracked record under its `home`', and AC1 requires per-fields-kind graded and legacy counts, with a non-zero legacy count for deviation. With every home empty, S4 has no locator, and no other rule in spec-1 tells it where a kind's records are. | sound | - |
| 7 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-20.md:section 2 S5; section 6 AC5 | medium | medium | confirmed | Spec-20 S5 (line 68) writes the retagged heading as `## [<anchor>] <heading>`, and AC5 expects `[notes-2]`. Spec-9 S1 (line 69) recognises an authored tag only as `## [section.<seg>] Title`. Spec-19 S10 says `retag` reads authored tags only. So retagged headings are not read as authored, and the same interface is spelled two ways. | sound | - |
| 8 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-19.md:section 6 AC1, AC2 | medium | medium | confirmed | Across the spec set, `--serves` appears only at spec-19:251 (AC1, reused by AC2). Unit 2 S1 defines the door's flags as `--build`, `--unit`, `--title` and `--field`, and unit 19 adds only `--caused-by` and `--edge`. So the AC1 and AC2 command lines fail at argument parsing. | sound | - |
| 9 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-4.md:section 4 'The routing region' (journals row); spec-2 section 2 S9 | medium | medium | confirmed | Spec-4 line 169 routes 'journals: each build/ record whose kind is journal', with no mention of canonical_kind or log. Spec-18 (order 4) S7 renames the row to `log`, has read_bindings keep the written token, and says no writer emits `journal` after it (line 162). Unit 4 is order 8, so log records written after unit 18 fall out of the journals row. Spec-2 S9 still names unit 1's `journal` row. | sound | - |
| 10 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-25.md:section 4 Data model; section 2 S1 | medium | medium | confirmed | Spec-25 §4 line 67 says the record opens with a Serves line 'naming the units it plans' but never states the kind token. Neither its S1-S4 nor its files touched adds `stream-plan` to RECORD_KIND_TOKENS or TYPED_RECORD_KINDS. In tree_lib.py's read_bindings (the else branch near line 565), a record whose first token is not in RECORD_KIND_TOKENS is marked malformed. Spec-18 S7's token list also lacks `stream-plan`. | sound | - |
| 11 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-26.md:section 2 preconditions and S5 (and spec-14 section 2/S6, spec-9 S3/S5, spec-8 S7) | medium | medium | confirmed | tools/memory-tree/kit.toml:7 reads `requires = []`, and memory-recall's kit.toml requires memory-tree. Spec-7's 'The policy read' and spec-8 F4 rule that memory-tree imports no sibling kit and must use its own `tools/memory-tree/policy_value.py` adapter. But spec-26 S1 puts gen_atlas.py in memory-tree, and its S5 and its consumes-from external edge (line 123) take read_policy_value from `tools/playbook/policy_value.py` (PLAY-dOrderedCharter-19). Spec-26 has no edge to unit 8's adapter. Spec-14's gov_map.py, also in memory-tree, reads `read_namespaces` from playbook and edits tools/playbook/tag_index.py. The set settles the kit-boundary question inconsistently. | sound | - |
| 12 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-9.md:section 2 S1 (`record` extractor: 'the kind the registry row whose `home` holds the path') | medium | medium | confirmed | In spec-9, S1 (lines 64-67) assigns a record's kind from 'the registry row whose `home` holds the path'. Spec-11's shape-run home is the whole `memory/builds/<slug>/build/` folder. Log, research and deviation records also sit in build/. Today's log and research file names are free-form (for example build/...-agent-ledger.md is a journal), so a glob home cannot separate them. The spec states no tie-break when two homes match. | sound | - |
| 13 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-5.md:section 6 AC7 against section 4 'The readers' | medium | medium | confirmed | The conflict is in spec-5: - §4 line 179-183: the predicate lists any line binding a name containing slug or SLUG to a regex literal. - §4 lines 203-204: a hit that is not a slug or id reader is 'recorded as kept', and the Decided trailer names kept hits. Nothing removes a kept hit from the predicate's output. - AC7 (line 348): `--readers` must list no line outside the entry points. I re-ran the finder's grep, which printed 6 hits. One is tools/runlog/model.py:1571, `slug_re = re.compile(r"\b" + re.escape(slug) ...)`, which is not a grammar reader. So a kept hit leaves AC7 red. | sound | - |
| 14 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-22.md:section 2 S2; section 4 'Files touched' | low | - | refuted | The premise is false on re-read. Spec-1 S3 (lines 52-57) lists what the gate reds: a missing required column, an empty writer, an unknown check leg, source drift, and factory-kind mismatches. It never lists an unknown column. Spec-1 also anticipates this column: its non-goals (line 97) give per-edge `cardinality` to unit 22, and its hands-off edge (line 111) names unit 22 mirroring `cardinality` into record-kinds.toml. Nothing in spec-1 says an extra column is refused, so unit 22's column does not red the record-kinds leg. | sound | - |
| 15 | coherence | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-14.md:section 6 AC7 against section 2 S5 | low | low | confirmed | Spec-14 S5 (lines 62-64) gives the header grammar `map <tree-id> · nodes <n> · lines <n> · folded ...` with no byte field. AC7 (line 214) reads 'the header's byte count is at most 32,768'. The figure it measures is not something the design produces. The figure line (31,203 B pinned) shows the intent was the whole map's size, so the effect is limited to the criterion's wording. | sound | - |
| 16 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-8.md:section 4 "Bounds" (the paragraph after the table), with S9 and section 8 F2 | high | high | confirmed | Spec-8 lines 158-159 read 'gov registers its generated code paths in `.gitattributes`: `tools/workflows/*.js`, rendered from their `.template.js`'. `git ls-files 'tools/workflows/*.js'` printed 11 files, among them four *.template.js sources and three hand-written scripts (check-workflow-syntax.js, orient-counterfactual.js, unattended-unit.js). `grep linguist .gitattributes` printed nothing, so the spec's glob is the whole registration. The Bounds table row at line 149 excludes every path set `linguist-generated`, so the real workflow sources would be dropped from the code record without any signal. | sound | - |
| 17 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-5.md:section 4 "The readers" and "The flips" | high | high | confirmed | Spec-5 §4 (lines 178-183) bases `--readers` only on regex shapes: a slug class followed by a hyphen and a digit class, or a SLUG-named regex binding. My `git grep` of `.split("-")` reproduced the readers: backlog.py:1042, :1407, :1664; gen_build_index.py:3541, :4073; check-recall.py:511; query.py:1463; drift_report.py:708; migrate_backlog.py:329/337. Line 226 includes the hyphenated `d2026-10-26ClosedLoop` flip, and F5 (line 408) even acknowledges readers that split on hyphens. With that flip, `split("-")[1]` yields `d2026`, and neither the predicate nor the flip probe would detect it. | sound | - |
| 18 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-13.md:section 4 "The states" (`BUILTIN_ARMED`) | medium | medium | confirmed | Spec-13 lines 116-118 define `BUILTIN_ARMED` with `js`, `mjs` and `cjs` mapped to `ts-tokens` under `parser`. tools/lexicon/lexicon.py:117-119 `KNOWN_EXTS` maps `js` to `("js-regex", "probe")`. The comment at :105-111 says ts-tokens earned `parser` only against TypeScript conformance records. Spec-13 does not mention KNOWN_EXTS or js-regex anywhere (grep printed nothing), so it reverses a measured verdict without stating it. | sound | - |
| 19 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-12.md:section 2 S3 (the memory-path match) with section 4 `derive_read_channel` | medium | medium | confirmed | Spec-12 S3 (lines 46-48) matches a word that 'starts `<root>/` or carries `/<root>/`' after folding backslashes. `ls -d $USERPROFILE/.claude/projects/*/memory` printed several harness auto-memory directories. A Read of `C:\Users\..\.claude\projects\P\memory\MEMORY.md` folds to a path that carries `/memory/`, so its bytes would count toward the measured median. The effect stays within one metric. | sound | - |
| 20 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-22.md:section 4 "The count" (last sentence) and section 10 | low | low | confirmed | Spec-22 line 117-118 says the playbook kit reaches design_lib 'as it reaches `derive_pin_hash`', and §10 line 259 calls design_lib 'the module the playbook kit already reaches'. `git grep -n derive_pin_hash -- tools` printed nothing, and `git grep -ln design_lib -- tools/playbook` printed nothing. F5 (line 245) lists edges.toml, edge_grammar.py, the resolver and pack as deferred, but not this reach. | sound | - |
| 21 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-7.md:section 4 "The policy read" | low | low | confirmed | Spec-7 line 128 says 'The memory-tree kit imports no sibling kit'. That is false at base. gen_build_index.py:1913-1919 resolves the drift-audit kit and runs `import drift_report`, and tools/memory-tree/kit.toml:8 `requires_if` declares the memory-recall, drift-audit, unattended, playbook-render and review-harness edges. The adapter design still works; only the stated reason is wrong. | sound | - |
| 22 | grounding | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-18.md:section 3 (the rewriting non-goal) and section 4 "Alternatives rejected" | low | low | confirmed | Spec-18 lines 96 and 193 state '1,443 `journal` records'. `git grep -lE '^\*\*Serves:\*\* *journal' 462d20f3 -- memory \| wc -l` printed 2025. The count appears only in prose and in a rejected alternative. | sound | - |
| 23 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-19.md:section 2 S1; section 4 Inventory; section 10 | high | high | confirmed | Spec-19 S1 (line 45) mints `read_header_edges(path, text)` in tree_lib.py and reads both the bare and the bulleted `- **Caused-by:**` form (line 155). PLAY-dOrderedCharter-28 S5 (lines 59-63) already assigns header reading to an adapter in edge_grammar.py, and its Inventory (:173) names that adapter `read_header_edges`. That adapter is specced on the `**Caused-by:**` header form only. Spec-19 cites 28 S2 but never S5, and its non-goal at line 112 leaves the edge checks to 24/28. The two readers can disagree on bulleted cause edges in spec 22's count. | sound | - |
| 24 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-6.md:section 2 S6; section 10 | medium | medium | confirmed | Spec-6 line 275 reads 'no cycle check exists in the tree to extend'. `sed -n 1271,1292p tools/memory-tree/backlog.py` shows `_scan_cycles(edges, fold)`, a DFS cycle finder that reports each cycle once, rotated. gen_build_index.py:307 already has `import backlog`. The spec's reuse audit claim is false, and the design adds a second walker in the same kit. | sound | - |
| 25 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-19.md:section 2 S7; section 4 The population | medium | medium | confirmed | Spec-1 S8 (lines 69-73) registers the `record-kinds-legacy` ledger, keyed by record path and section and seeded at unit 1's landing. Spec-19 S7 (lines 76-81) registers a separate `legacy-records` ledger, keyed by path and section, over the same tracked records. The brief's I22 names one population that units 1 and 19 read. So the specs contradict their own shared interface. | unsound | - |
| 26 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-20.md:section 2 S4; section 8 F3 | medium | medium | confirmed | Spec-20 S4 (lines 54-60) grades front matter against `FRONT_MATTER_KEYS` with its own program and prints `<key> derived`. AC4 (line 216) expects `node derived` for a planted `node: d`. Spec-4 S4 (line 48) refuses a typed derived key only outside the legacy population and reads it, never refusing it, inside. F3 (line 259) claims unit 4 refuses both, which ignores that exception, so the two graders disagree on legacy READMEs. | sound | - |
| 27 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-23.md:section 2 S1, S2; section 4 The row and its key | medium | medium | confirmed | Spec-23 S1-S2 (lines 36-47) add `leg_row(blob, reader, version, payload)` and a `LEG_READERS` registry in tree_lib.py, with a version derived 'as PLAY-dOrderedCharter-44 S3 derives an extractor's', plus `params(root)`. PLAY-dOrderedCharter-44 S1-S3 (lines 35-48) already defines the `blob_parsed` ledger, the extractors the registry names, and the module-bytes version. Spec-23 §4 Alternatives (lines 156-163) does not consider registering the readers as extractors. Two version rules would hold in one index. | sound | - |
| 28 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-21.md:section 2 S2 | medium | medium | confirmed | Spec-21 S2 (lines 54-60) adds `fts_blob(blob, digest)` as recall's own freshness ledger inside build_index, with a hand-assembled digest. `grep -n 'dOrderedCharter-44\|blob_parsed' spec-21` printed nothing, although 44 S1 (lines 35-38) supersedes 19 S4's freshness rule for every extraction build_index runs. The index would carry two staleness rules. | sound | - |
| 29 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md:section 2 S4; section 6 AC7 | medium | medium | confirmed | Spec 1:56-58 S4 grades every `fields` row's records for each field as a `**Key:**` line in the row's order. For `deviation`, deviation_join.py:212 `read_record` already reports `(k, "is missing") for k in REQUIRED`, using `FIELD = ^- \*\*...` (:144). AC7 (spec 1:299) plants exactly that missing-`Caused-by` case. §10 names FIELD/REQUIRED only as a literal to compare against, not as the grader to call. One part of the impact does not hold: spec 2 S4 (:47-51) runs BOTH S4's check and `read_record` at the door, so a record cannot pass the door and still red the gate. The real divergence is between the deviation join and the record-kinds gate: S4 adds a row-order requirement and a separate legacy ledger that `read_record` does not have. So two graders of one rule do disagree. | sound | - |
| 30 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-16.md:section 2 S3; section 4 The values (refuse row); section 6 AC5 | medium | medium | confirmed | Spec 16 S3 (:37-43) builds its own census of `namespaces.toml` members whose purpose field is absent or empty, and of chain.toml rows with no `purpose`. The refuse row (:85) makes `--check` red on those. PLAY-dOrderedCharter-22 S2 already reds a member that lacks its named field, and S4/S5 (:44-49) define the `purpose` arm of `gov_tag.py check`, which prints rows with no purpose as awaiting PM-5 and passes. The Inventory there names `read_chain_registry` and `check_namespace_purpose` (:109). Spec 16 §10 (:214) says no seam fits and never names that arm. Under `refuse`, the two checks give opposite verdicts on the same chain rows. The 'field absent' member case is already red under 22 S2. | sound | - |
| 31 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-9.md:section 2 S2; section 4 The section table | medium | medium | confirmed | Re-probed: gen_build_index.py:8493 defines `SPEC_TITLE_NUMBERS`. check-memory-hygiene.sh:1806/:1823 define SPEC_CANON and SPEC_CANON10, and :1791 makes the 'Production-readiness checklist and Reuse audit optional' for Tier-1. Spec 9 S2 (:79-82) and its section table add a third copy, with `{ tag = "section.reuse-audit", required = true }`. Nothing ties that copy to either existing canon, and §10 names neither, so the required flags already disagree with hygiene's Tier-1 rule. | sound | - |
| 32 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-26.md:section 2 preconditions and S5 | medium | medium | confirmed | Spec 26:35-36 cites `read_policy_value` in `tools/playbook/policy_value.py`, and S1 (:44) places the renderer at tools/memory-tree/gen_atlas.py. Spec 8 F4 (:315-318) resolved that the memory-tree kit cannot import the playbook module and built `tools/memory-tree/policy_value.py` (S10, :74-75). Spec 8's hands-off edges (:114-121) do not include 26. Spec 26's edges (:122-123) list only TOOL-dTotalRecall-14 and an external PLAY-dOrderedCharter-19 consumes-from, with no edge to unit 8. | sound | - |
| 33 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-14.md:section 2 preamble and S6; section 3 Edges | medium | medium | confirmed | Spec 14:34-36 names the policy reader as PLAY-dOrderedCharter-19 S8's `read_policy_value`, which is the playbook kit's module, and S6 (:67) reads both map keys through it for the memory-tree module gov_map.py. Spec 14 §3 (:103-106) has no edge to TOOL-dTotalRecall-8, and spec 8's hands-off list (:114-121) omits 14. Spec 8 F4 ruled that a memory-tree module must use the memory-tree adapter. | sound | - |
| 34 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-9.md:section 2 S1 (`class` extractor) | low | low | confirmed | Re-probed: gotchas.py:253 reads `kind = fm.get("kind", "class")`, and `build_record` and `records` are at :271 and :289. `grep -h ^kind:` printed 145 'kind: class' and 3 'kind: invariant', and `grep -L` printed only INDEX.md. So the counts agree today, but spec 9:74-75's extractor selects on a literal `kind: class` with no default. A future gotcha that omits the key would be read differently by the two parsers. | sound | - |
| 35 | reuse | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-12.md:section 2 S4; section 10 | low | low | confirmed | Spec 12 S4 (:49-54) specifies `measure_agent_memory`, which pairs each tool_use with its tool_result and sums the result bytes. Spec 17 (:35-38, :110-113) mints `measure_bytes_before_act`, which sums tool-result bytes over the same runlog readers. The README build order puts 17 at step 22 and 12 at step 26. Spec 12 §10 (:285-292) says no measure of result bytes exists and does not name unit 17's counter. Two counters built by the same build can parse content shapes differently. | sound | - |
| 36 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-4.md:section 4 "The routing region" (journals row), against TOOL-dTotalRecall-18 section 2 S7/S8 | high | high | confirmed | Spec 4:169 says `\| journals \| each build/ record whose kind is journal \|`, and kinds are read from `binds_all` (:175-176). Spec 18 S7/S8 (:66-72, :85-88) renames the registry row to `log`, makes every writer write `log`, and has `read_bindings` keep the written token, with comparisons going through `canonical_kind`. The README build order puts 18 at step 4, before 4 at step 8. Spec 4 never mentions `canonical_kind` or unit 18, so the routing region would drop every newly written log record. Spec 2:69 still says "unit 1's `journal`" row, although 18 (step 4) renames it before 2 (step 12). | sound | - |
| 37 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-21.md:section 2 S4 (kit.toml `requires` gains `playbook`); section 4 Files touched | high | medium | confirmed | Spec 21 S4 (:70-72) adds `playbook` to memory-recall's `requires` and reaches the playbook kit through `resolve_kit_dir`. The §5 risk (:210-211) names only govkit's refusal. tools/memory-recall/kit.toml:7 reads `requires = ["memory-tree"]`. WIRE-INTO-PROJECT.md:127 says memory-recall 'requires the memory tree', and the §3c copy-install steps (:582-586) pair only memory-tree and memory-recall via `cp -r`. Spec 21 has no WIRE-INTO-PROJECT hit, so a copy-install adopter would get a recall kit that cannot find tag_index. The failure is loud but sits on the documented install path, so I grade it medium. | sound | - |
| 38 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-21.md:section 2 S1 Readers; section 4 Files touched | medium | medium | confirmed | Re-probed: verbatim.json pins bench.py and union.py. union.py:96 calls `B.build_index`, and bench.py has :88 and :454. selftest.py:1688-1708 hashes each pinned file and documents union.py as 're-pulled WHOLESALE'. Spec 21 S1 lists both files as readers and lists them in Files touched (:177-178), but verbatim.json is absent and the spec says nothing about the pin or about forking union.py. | sound | - |
| 39 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-4.md:section 2 S4; section 4 Files touched; section 7 | medium | medium | confirmed | Spec 4 S4 (:48-51) refuses a typed node/roster/streams on any README outside a legacy population. That population (:148-155) is seeded from the tracked READMEs at the pass SHA and keyed by path, so fixture READMEs planted in scratch repos are outside it. `git grep -c -E 'roster: ?[A-Z]' -- tools` reproduced the counts (hygiene test 15, unattended.test.sh 12, corpus_ids.py 3, migrate_backlog.py 1, unattended-build.test.sh 1, ...). For example, corpus_ids.py:1012 plants 'node: a ... streams: arch\nroster: ARCH'. Spec 4 §7 (:306) lacks `corpus-ids selftest`, `backlog migration selftest` and `unattended-build self-test`, all of which exist in gate-legs.json, and Files touched lists none of the fixtures. | sound | - |
| 40 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-11.md:section 2 S6, section 4 Files touched, section 7 (same gap in spec-19 S12, spec-22 S6, spec-26 S10; partly in spec-1 and spec-8 §7) | medium | medium | confirmed | I re-ran the greps per spec, counting subject-pins/ceiling-evidence/gate_leg\|exempt_leg/dossier/codebase-map coverage/govkit selfcheck: 11 0/0/0/0/0/0; 19 0/0/0/0/0/0; 22 0/0/0/0/0/0; 26 0/1/2/0/0/0; 1 2/2/1/5/0/0; 8 2/2/0/16/0/0; 15 1/2/3/2/1/1. Specs 11 (:168) and 19 (:104) say only 'with its meta-gate rows' and do not list the files. govkit.py:2945 reds a leg 'claimed by no descriptor and carried by no [[exempt_leg]]'. `govkit selfcheck`, `leg ceilings clear their evidenced maximum` and `codebase-map coverage + freshness` all exist in gate-legs.json and are absent from those specs' §7. | sound | - |
| 41 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md:section 4 Files touched and section 7 (applies to every spec that mints or retires a Python symbol: 1, 2, 3, 5, 8, 9, 11, 13, 18, 19, 21, 22, 23, 26 and others) | medium | medium | confirmed | test_codebase_map.py:291-292 lists `symbols.json` as a conditional tier, and :310-330 byte-compares each tier's regenerated text. The leg `codebase-map coverage + freshness` has no guard in gate-legs.json. ensure_cache, corpus_digest, common_git_dir, build_index and read_bindings each appear in memory/map/generated/symbols.json. No spec in the set names memory/map/generated or gen_map, and only specs 14 and 15 name the leg in §7. d85890512 reads 'the nine bar legs this build turned red'. Every pass that mints or retires a symbol leaves symbols.json stale until the close. | sound | - |
| 42 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md:section 4 Inventory "Naming cells" vs section 7 (same in 21 other specs) | medium | medium | confirmed | 22 specs carry 'Naming cells', and only specs 9 and 14 name `lexicon naming predicates` in §7. TEMPLATE-SPEC (:263-272) excludes broad-guard legs from what §7 must name, but it does not forbid naming them. A pass that runs only its named legs (BUILD-METHOD :320, 'ran two legs, not the bar') would not see a bad name until the bar runs. Part of the evidence is wrong: re-probing `lexicon.py --suggest` gave OK for check_pockets, build_fts_rows and check_record_kinds. It flagged `canonical_kind` (spec 18) ('`canonical` is not in the declared table') and `ensure_index` ('use check_index'), so the defect is real for at least one spec in the set. | sound | - |
| 43 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-5.md:section 7 (and section 3 "the readers' own suites are the arms") | medium | medium | confirmed | Spec-5 §4 Files touched (lines 258-281) lists row_grammar.py, merge-rows.py, migrate_backlog.py, routed_commits.py, check-arms.py, gen_build_index.py and run-gates.sh. Its §3 (line 108) says the readers' own suites are the arms. The §7 leg line (line 374) names none of these legs: row-grammar selftest, row-keyed merge driver replay, row-driver view refusal, check-arms selftest, harness arms, backlog migration selftest, routed commits name a specced unit, build README slot contract, run-gates canary. tools/gate-legs.json confirms that each leg runs one of those files. Some have broad guards ({prefix}/memory-tree/, {prefix}/lib/) and others have no guard at all. TEMPLATE-SPEC §7 (lines 264-271) excludes broad guards from the join, so the join does not force these legs. Specs 3, 7, 18, 20 and 23 each mention gen_build_index, and none names build README slot contract in §7. | sound | - |
| 44 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-26.md:section 7 | medium | medium | confirmed | Spec-26 §7 (line 313) does not name `python resolver (behaviour + inline parity + idiom ban)`. Yet line 320 declares `New arm: tools/lib/resolve-python.test.sh · covers AC12`, and §4 (lines 88-89, 212) adds the help_pages PARITY_ROWS row to that suite. In gate-legs.json, that leg is the one whose argv is resolve-python.test.sh, and its guard is broad. Spec-13 §7 (line 224) omits `drift-audit records` (drift_report.py --check) and `lexicon naming predicates` (lexicon.py), although S4 and S7 edit both files. Spec-12 §7 (line 236) omits `runlog record schema` (runlog.py check-records), although it adds a verb beside check-records in runlog.py (line 62, 159). | sound | - |
| 45 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-9.md:section 2 S3 (moving `search`, `rrf` ... out of query.py); section 4 Files touched | medium | medium | confirmed | Spec-9 S3 (lines 87-89) moves `search` and `rrf` from query.py into record_find.py, and query.py keeps only a thin adapter. tools/codebase-map/scen-adversarial.json still has ADV-05 (`search`) and ADV-06 (`rrf`) with expected_file `{prefix}/memory-recall/query.py`, and their established_by cites query.py lines. rank_harness.py:89 grades against expected_file at file granularity. Spec-9 never mentions scen-adversarial or codebase-map scenarios. The selftest.py:1906 comment also names query.py's rrf as byte-identical to adopter ic's copy. | sound | - |
| 46 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-18.md:section 2 S7 Readers / S9 prose | medium | medium | confirmed | `git grep 'acceptance ledger in a'` prints memory/guides/SESSION-KICKOFF.md:63: "A CLOSED Tier-2 unit owes an acceptance ledger in a `journal` record". Spec-18 never mentions SESSION-KICKOFF. Its S9 (lines 89-92) covers only HYGIENE.template.md, HYGIENE.md, the conf example and the runlog README. AC7 (line 240) greps `Serves:** journal` over `tools` only, so the stale kickoff instruction survives the rename and contradicts S8. Note that the widened AC7 pattern would still not match this prose line, so the prose edit is what cures it; the widening does no harm. | sound | - |
| 47 | blast-radius | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-19.md:section 4 Files touched / section 7 (same in specs 1, 5, 8, 9, 11, 15, 18, 21, 22, 26) | low | low | confirmed | SESSION-KICKOFF.md line 5 `watch:` includes tools/gate-legs.json, tools/memory-tree/check-memory-hygiene.sh, .memory-tree.conf, skills/session-kickoff/manifest-check.sh and tools/run-gates/run-gates.sh. Files touched lists them: gate-legs.json in specs 1, 8, 9, 11, 15, 19, 22 and 26; check-memory-hygiene.sh in specs 5 and 18; .memory-tree.conf in specs 19 and 21; manifest-check.sh in spec 9; run-gates.sh in spec 5. A grep for 'kickoff-manifest ratchet\|last-audit\|re-stamp' over the spec set matches no file. The `kickoff-manifest ratchet` leg has no guard. manifest-check.sh:1459-1473 fails with C5 when a watched file changed after LA_SHA with no later re-stamp. The consequence is a red leg that needs a follow-up re-stamp, which is contained. | sound | - |
| 48 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-13.md:section 4 "The states" (the worktree row), AC3 | high | medium | confirmed | Spec-13 states the worktree-row blob id is git's own, computed as `sha1(b"blob %d\0" % len + bytes)` over the raw disk bytes. I re-ran the probe. core.autocrlf is true and .gitattributes holds `* text=auto`. For tools/lexicon/lexicon.py, python over the raw bytes printed 56df4068… (4434 CRLFs), while `git hash-object` printed 9625f145…. The claimed invariant is false on this node, so the (blob, ext) cache is never shared across states. AC3's red condition compares against `git hash-object`, but its fixture writes fresh LF files, so it cannot see the CRLF case. Deleted-on-disk paths and symlinks are not addressed. In this spec set, read_defs_at's worktree ids feed only the cache (spec 8 uses revision trees), so I grade the consequence as contained, not high. | sound | - |
| 49 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-7.md:section 2 S2 and section 4 "The door verb" | high | high | confirmed | I re-ran render_ask_row('EXMP-aFoo-1','2026-02-01','x\n- EXMP-aFoo-2 · filed 2026-02-01 · injected', clauses=(('accept','y'),)). It printed two rows, and the accept clause landed on the injected row. Spec-7 lines 106-108 build the graded mapping from the --clause pairs, not from the rendered row. Lines 116-118 have the read-back confirm only that one ask with the minted id exists. Neither spec 7 nor spec 2 refuses newlines or SEP/ARROW in values. The `refuse` acceptance gate is therefore bypassed through its own door: the check certifies a clause that the minted row does not carry. | sound | - |
| 50 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md:section 4 "The command" ("A `--field` value is taken verbatim") and S4 | high | medium | confirmed | Spec-2 line 136 says a --field value is taken verbatim, and line 51 says the door adds no validator of its own. deviation_join.read_record (lines 212-260) matches FIELD on each line. It refuses only a repeated key, Before/After running past one line, and closed-set or shape violations. An injected `- **Supersedes:** <valid stem>` or `**Bound:**` line through a newline in another field is therefore accepted. No CR/LF refusal exists anywhere in spec 2. The callers are agents, and many injectable keys could be passed directly, so I grade the effect as contained. | sound | - |
| 51 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-11.md:section 4 "The row" (`home`) with TOOL-dTotalRecall-1 §5 and S4 | high | high | confirmed | Spec-11 line 155 sets the home to `memory/builds/<slug>/build/` (the whole folder) on a `fields` row with 15 required fields. Its migration section (lines 179-180) adds no record, and line 209 says an empty population prints unarmed and exits 0, but only in its own shape_run leg. Spec-1 S4 (lines 56-58) grades every record under the row's home. Spec-1 §5 (line 261) reds an empty home of a fields kind. Spec-18 line 117 requires a fields-kind tracked glob to match at least one file. Spec-9 line 65 takes a record's kind from the row whose home holds the path. By contrast, spec-25 uses the narrow `memory/builds/*/build/*-stream-plan-*.md`. Under either reading, the registry check reds or misgrades at unit 11's landing. | sound | - |
| 52 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-21.md:section 5 error states and AC5; section 4 "The flow" | medium | medium | confirmed | I re-ran the subclass check: issubclass(sqlite3.OperationalError, sqlite3.DatabaseError) printed True. Spec-21 §5 (line 207-208) and AC5 (lines 237-239) name only one path: DatabaseError means corrupt, so refuse naming `gov_tag.py --rebuild`. Spec-21 never mentions busy, locked or timeout. The parent PLAY-dOrderedCharter-19 §5 says a locked database waits on the busy timeout and exits 2 naming it, but that belongs to the gov_tag/build_index side. Spec-21's own query error mapping, built as written, would catch a lock as corruption and direct the operator to rebuild a shared, live file. | sound | - |
| 53 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-21.md:section 2 S2, S3 and S6 | medium | medium | confirmed | Spec-21 S2 (lines 54-61) keys FTS rows by digest and keeps rows for other confs on purpose. S3 keys dirty rows by worktree. S6 (lines 84-87) retires eviction and the budget. I grepped spec-21 and PLAY-dOrderedCharter-19 for prune, vacuum, evict, delete and garbage: the only hits are the retirement list and the not-delete-the-file rule. No deletion rule for fts_*, fts_blob or dirty_path exists, so index.db grows without bound across digest changes and removed worktrees. The proposed fix is unsound. It deletes fts rows only when the digest is dead AND no live tree holds the blob. After a conf change, nearly every old-digest row's blob is still held by the live tree, so the main growth (a full corpus copy per digest) is never reclaimed. | unsound | - |
| 54 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-8.md:section 2 S7, S8, S9 and section 4 "Bounds" (the time row) | medium | low | confirmed | Spec-8 S7 (lines 62-66) makes the per-tree tables the cache keyed by tree hash. Line 160 says a degraded record is kept and marked. Nothing says whether a later run on the same tree re-derives or serves the degraded tables. The flake half of the claim is partly covered: AC7 (lines 272-274) says `--check` on a degraded record prints the git-grep floor line instead of comparing. What is left is that a degraded tree's record may stay degraded for that tree, which only sends readers to the correct git-grep floor until HEAD moves, so the effect is contained. | sound | - |
| 55 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-8.md:section 2 S7 ("a blob already holding `code_row` rows is never re-parsed"), AC5 | low | low | confirmed | Spec-8 S7 (line 65) and §4 line 131 key the cache hit on whether the blob already holds code_row rows. A blob that yields no row (empty, unparseable, or nothing extractable) therefore never registers and is re-parsed on every run. I re-probed gov: `git ls-files -s` showed zero code files at the empty blob e69de29b, so AC5 holds on gov but not at such an adopter. The cost is only a performance one. | sound | - |
| 56 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-4.md:section 2 S2 (the refusing parser) | medium | medium | confirmed | gen_build_index.py lines 421-438 assign `fm[k.strip()] = v.strip()` with no check for a key already seen, so the last occurrence silently wins. Spec-4 S2 (lines 37-39) adds refusals for unknown keys and bad values, but not for repeated keys. A grep of spec-4 for twice, duplicate or repeated finds only an unrelated line 328. A repeated `ids:` or `depends-on:` key would therefore drop the first list silently, which is the silent-drop class the unit targets. | sound | - |
| 57 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-18.md:section 4 "The pockets" (`GIT_OWN`) and S6 | medium | medium | confirmed | spec-18 lines 142-145 fix GIT_OWN as a closed list: HEAD, ORIG_HEAD, FETCH_HEAD, MERGE_HEAD, CHERRY_PICK_HEAD, REVERT_HEAD, COMMIT_EDITMSG, config, ... gc.log. It has no MERGE_MSG, MERGE_MODE, AUTO_MERGE, REBASE_HEAD, rebase-merge/, rebase-apply/, sequencer/, BISECT_*, *.lock or lfs. Grepping spec-18 for lfs, lock, MERGE_MSG and rebase found nothing. `ls -A` of the common dir lists the main worktree's `index`, `COMMIT_EDITMSG`, `ORIG_HEAD` and `FETCH_HEAD`, so the main checkout's transient merge, rebase and lock files land in the same directory the pocket arm lists. The leg would red during a merge, a rebase, or while another git command holds a lock, and the §5 risk line accepts reds on the node. | sound | - |
| 58 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-14.md:section 2 S7 (the cache) | medium | medium | confirmed | spec-14 S7 (lines 72-75) puts the cache at <git-common-dir>/gov/map/<tree>.map, which every worktree shares. It validates the file only by its first-line stamp. Grepping spec-14 for atomic, replace, tmp and truncat found nothing, so no atomic write and no completeness check is specified. A reader that races a writer, or a writer that dies mid-write, leaves a file whose stamp is valid and whose body is partial, and that file is served. | sound | - |
| 59 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md:section 2 S9 and section 4 "Factory" | medium | low | confirmed | spec-1 lines 196-197 list only four refusals for `new`: a duplicate name, a tag outside `record.`, an empty writer and an unknown check. Nothing checks the name or tag segment against a grammar, so `record.Widget` is accepted, and S3 (lines 50-55) has no tag-grammar red. The impact the finder gives through FIELD is overstated. S4 (lines 56-58) only requires each field as a `**Key:**` line and never says it parses with deviation_join.FIELD. Tracked records already carry keys that FIELD cannot match: grep counted 62 `**Read outside the list above:**` lines, and `**What is wrong:**` and `**To look at:**` also appear. What remains is an unvalidated name, tag or field reaching the registry, a contained effect. | unsound | - |
| 60 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md:section 4 "Minting" (`<n>`) and "Idempotence" | medium | medium | confirmed | spec-2 line 151 mints `<n>` as 'the next free <n> in the home folder, the factory's collision rule'. PLAY-dOrderedCharter-7 S7 (around line 92) defines that factory over 'the tracked population and the <n> collision'. The idempotence scan (spec-2 lines 172-174) also lists tracked and staged files only. tools/memory-tree/deviation_join.py:268-276 reads TRACKED paths only, and its docstring says an untracked draft moves nothing. No exclusive create is specified, so an untracked file already at the minted path is overwritten. | sound | - |
| 61 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-19.md:section 2 S9 and section 4 "The walk" | medium | - | refuted | The premise is false on re-probe. A README's `ids:` line is not authored. tools/memory-tree/gen_build_index.py:1820-1838 (apply_front_matter_ids) rewrites it from roster_by_slug, and the docstring at :549-551 calls that roster 'a reservation RANGE generated from citations anywhere' that 'admits backlog and decision rows'. Line 1186 lets the derived roster override the authored value once any independent source names an id. This build's own README `ids:` already lists TOOL-dTotalRecall-27 to -31, which are BACKLOG ask rows, not specs. An ask that unit 7 writes into the target's BACKLOG.md is therefore named by that README's `ids:` once the README renders, and S9 reaches it. | unsound | - |
| 62 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-10.md:section 2 S1 and S3 | medium | medium | confirmed | spec-10 S1 (lines 33-37) gives `seen` as 'the set of anchors already derived in the same document', and S3 (lines 42-43) grades uniqueness 'of authored tags alone'. spec-9 S1 (around lines 69-71) has extract_section mix three sources in one record: authored `## [section.<seg>]` tags, table-mapped tags, and `section.<derive_anchor(...)>` for every other heading. An authored [section.findings] heading and an untagged `## Findings` therefore both produce section.findings. Nothing seeds `seen` with the authored tags, and nothing grades the clash. | sound | - |
| 63 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-22.md:section 2 S3 and S5; section 4 "The count" (playbook reaches design_lib) | medium | medium | confirmed | tools/playbook/kit.toml:16 reads `requires = ["playbook"]`, with no memory-tree. spec-22 places the counter in tools/memory-tree/design_lib.py (S3, line 38), has S2 read memory-tree's record-kinds.toml, and has S5 read README edges through gen_build_index.py --print-relations. The design_lib import is reached through resolve_kit_dir (lines 117-118). The spec never states the case where memory-tree does not resolve. §5 (line 171) lets an empty population print zero counts and exit 0, so a guarded build of the leg would pass while counting nothing. | sound | - |
| 64 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-26.md:section 4 "The pages" (Mermaid node id and label; node row cells) | medium | medium | confirmed | spec-26 line 154 makes a Mermaid node's label the key, with no quoting stated, and the cell content at lines 141-148 has no escaping stated. spec-14 S3 makes a node's key its native id where the namespace declares one. spec-15 S3 routes the leg census over the names in tools/gate-legs.json against the index's node keys, so leg nodes are keyed by leg name. A python probe over tools/gate-legs.json printed 142 names, 22 of them holding ()[]{}"\| (for example 'shell hygiene (a fork spent on builtin work)'). Mermaid cannot parse unquoted parentheses inside a [label], and the parity checks never render the page. | sound | - |
| 65 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-16.md:section 2 S4 vs section 5 security and Files touched | medium | medium | confirmed | spec-16 S4 (lines 44-48) writes each derived purpose into 'the member's `purpose-source` field', which sits in the member's own file. §5 security (lines 144-145) says the review writes 'only tracked registry files and this build's backlog'. Files touched (lines 125-134) lists only registries, chain.toml, the policy files and the BACKLOG. The write surface is unpriced and contradicts §5. | sound | - |
| 66 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-25.md:section 2 S3 (`check_stream_plan`) | low | low | confirmed | spec-25 S3 (lines 39-42) reds an empty stream, a missing order, a non-integer order, a unit in two streams, and a missing or unparseable fence. The fixture plants (lines 93-95) match that list. Nothing reds a stream name given twice, a unit id that is malformed or from another build, or a second toml fence. The population is unarmed today (S5), so the effect is contained. | sound | - |
| 67 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-12.md:section 2 S3 (memory path match) | low | low | confirmed | spec-12 S3 (lines 46-48) counts a word when it 'starts `<root>/` or carries `/<root>/`', and its only exclusion is the tools/memory-tree and tools/memory-recall prefix. Any absolute path holding /memory/ counts, including another repository's memory tree or ~/.claude/projects/<proj>/memory/. A bare `memory` word does not count. The effect is skew in the measured median, contained to the instrument. | sound | - |
| 68 | failure-envelope | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-3.md:section 4 "The counter" step 2 | low | low | confirmed | spec-3 §4 'The counter' step 2 (around line 132) detects a replay only within 'first-parent history, read to 64 commits'. S4 (lines 45-47) promises without a bound that a replay whose claimant 'the ref already carries returns the earlier result'. A replay older than 64 mints on that family ref gets a second id. | sound | - |
