**Serves:** spec-audit TOOL-dDeclaredLoop-89@rev-1 TOOL-dDeclaredLoop-90@rev-1

# Tier-2 review: the round-1 spec audit of dDeclaredLoop's 2 round-8 promoted unit specs (TOOL-dDeclaredLoop-89 and -90)

Provenance: a Tier-2 spec audit at full intensity, run on 2026-10-24. It covered the 2 unit specs that the round-8 audit's promotions added to build dDeclaredLoop, at the blobs pinned on the line below. Five lenses ran (finders gov-spec-reviewer), then five skeptic batches (gov-skeptic), then synthesis (gov-synthesizer). Eighty-eight spec documents were supplied as sibling context.

Reviewed: memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md@1fd7a3cffff906833f27bf1f51c8bd4b6c3e911d, memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md@ce617b5222b82b999d6bd29a88a9f777c1cb807b

ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker survived. One high and thirteen lower items need to be fixed in the specs before the build starts.

The adjudicated tally comes to 14 items. By item: 0 blocker, 1 high, 6 medium, 7 low. By raw confirmed finding: 0 blocker, 1 high, 9 medium, 8 low, 18 in all.

Every confirmed finding keeps its binding grade. No grade was changed.

## Review shape

Intensity full, raw 22, confirmed 18, refuted 4, unverified 0 (0 uncertain), precision 0.82.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 5 | 3 | 2 | 0 | 0 | 0.60 |
| reuse | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 3 | 1 | 2 | 0 | 0 | 0.33 |
| failure-envelope | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |

### Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Demotions: 0 contradictory verdicts and 0 orphaned duplicate refutations were demoted to unverified.
- Discards: 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 16 were judged sound and 2 were judged UNSOUND (ids 20 and 21). None lacked a proposal and none went unjudged.
- Severity on confirmed findings: 0 were ungraded by the skeptic and 0 were re-graded.
- Unverified findings: 0 were answered UNCERTAIN and 0 had no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 88 spec documents were supplied as `specs`, as sibling context.
- Checklist: 22 items, each assigned to exactly one of 5 lenses (coherence 5, grounding 5, reuse 4, blast-radius 4, failure-envelope 4).
- By design: none was supplied. There was no caller byDesign and the block held 0 entries.
- Move check: no checked subject moved.

Every count above is zero where zero is required, and every lens and batch returned, so the run is complete.

## High

### H1. 89 S1/S5: three module-name binding forms are neither caught nor priced (id 20)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-89.md` §2 S1 and S5, read with §1, which claims the unit prices every other binding form as a non-goal.
- **What is wrong:** Three forms bind a module name in loop_lib.py and fall outside both passes of S1:
  - a `global` declared in a class body, such as `class Cfg: global CONF; CONF = ROOT / ".unattended.conf"`;
  - a walrus in a module-level function's default argument, such as `def f(x=(CONF := ...)): ...`;
  - a walrus in a lambda's default argument.

  S1's global-loader rule only looks at FunctionDef and AsyncFunctionDef. Its module-level walk never enters a ClassDef, FunctionDef or Lambda, but defaults and class bodies run in module scope. The skeptic confirmed by exec that all three forms bind module names. S5's priced list names five forms and none of these three.
- **Consequence:** A loop module that reads `ll.CONF` bound by one of these forms passes `no-own-conf-read` and is certified as reading no conf of its own. That is the outcome this unit exists to close, reached on a narrow path. 87 §3 would also claim a complete list of binding forms that is not complete.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):**
  - Treat a ClassDef as a loader the way a function is treated: a class whose body holds a Global and a conf constant answers the globals that body stores.
  - In the module-level walk, also descend into every part of a FunctionDef, AsyncFunctionDef, Lambda and ClassDef that runs in module scope: decorator_list, args.defaults and args.kw_defaults, plus a ClassDef's bases and keywords.
  - Add plant rows and AC2 names for the class-body global, the default-argument walrus and a class-base walrus.
  - The alternative is to name every one of these forms in S5's §3 bullet, each with its reason.
- **Left-shift gate:** Add an entry to the project's bug-class checklist: "a binding-form walk must enumerate every AST position evaluated in module scope (class bodies, defaults, decorators, bases), each with a plant row". Back it with a fixture leg that execs each planted row and checks that the walk answers the name the exec bound.

## Medium

### M1. 90: the shared `load_tree_lib()` loader is a new public def that the Write set and §7 say does not exist (ids 4, 9, 15, 17)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-90.md` §2 S4 ("86 S21's route, extended in place"), the §4 Write set, the §4 sketch "The tree_lib route, after this unit (S4)", and the §7 leg line.
- **What is wrong:**
  - S4 requires one loader that derive_conf_reads, derive_conf_constants (and 89's derive_conf_rebinds) all call, so it has to be a module-level function.
  - The sketch gives it a public name, `load_tree_lib()`.
  - 86 S21's route, which S4 says it extends in place, is inline code inside derive_conf_reads. No such function exists today, and `grep load_tree_lib` matches only the 90 spec.
  - The Write set nevertheless says "The pass mints no public module-level def, so memory/map/generated/symbols.json does not move".
  - §7 leaves out `codebase-map coverage + freshness`, while 89 §7 lists it for its own public def.
- **Consequence:** The codebase-map symbol tier (map_lib.py:350-356) indexes every public module-level FunctionDef. Built as sketched, symbols.json goes stale outside the unit's write set. The unguarded freshness leg then reds at the merge bar, or the pre-commit hook refuses the commit, while the unit's hand-named gate list stays green. The builder is also misled into treating the loader as existing code.
- **Fix (judged sound):** Choose one.
  - (a) Name the loader `_load_tree_lib` in S4 and the sketch. Say that it replaces the inline resolve in derive_conf_reads and derive_conf_constants, and that the private name is what keeps symbols.json unmoved.
  - (b) Keep the public name and say S4 mints it. Add `memory/map/generated/symbols.json` to the Write set and Files touched, add an Inventory line for the new symbol row, add `codebase-map coverage + freshness` to §7, and correct the "mints no public module-level def" sentence.
- **Left-shift gate:** Add a spec-lint leg that collects every `def <public name>` in a spec's sketches that is absent from symbols.json. The leg fails when such a def exists and the Write set omits symbols.json or §7 omits the codebase-map leg. Better still, derive §7's leg list from tools/gate-legs.json instead of typing it by hand. This is the recurring hand-named-gate-list-green-while-the-bar-reds class.

### M2. 90 S3/AC3: S3 points at a sentence 88 S13 does not hold, and AC3 cannot see the real ones (id 1)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-90.md` §2 S3 and §6 AC3.
- **What is wrong:** S3 tells the builder to retire "88 S13's sentence that the slice leaves 87's answer unchanged". 88 S13 (lines 112-120) has no such sentence. The claim actually sits in two places:
  - 88 §3 Edges line 221: "AC2's answer unchanged (id 17)";
  - 87's hands-off 88 edge, line 79: "with AC2's answer unchanged".

  AC3 reads only 88's AC13 range.
- **Consequence:** The builder finds nothing in 88 S13. Under 90 §3's third non-goal, an item whose target reads as stated is recorded as already done. Both specs then keep claiming the answer is unchanged beside a slice that answers more names, which is the two-answers defect M1 named. AC3 stays green throughout.
- **Fix (judged sound):** Point S3 at 88 §3 Edges line 221 (the consumes-from 87 bullet) and at 87 §3 Edges' hands-off 88 bullet. Extend AC3 so that `grep -c "answer unchanged"` over the 88 spec and over the 87 spec each prints 0. Each prints 1 at HEAD.
- **Left-shift gate:** Add a spec-lint check: when a scope item names "<unit> S<n>'s sentence", require the quoted phrase to appear in that range at HEAD. A missing target is a red, not something to observe and record.

### M3. 90 S1/AC1 (and 89 S4/AC3): no criterion reads 87 §3's false "moves no answer" sentence (id 2)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-90.md` §2 S1 and §6 AC1, plus `2026-10-24-spec-TOOL-dDeclaredLoop-89.md` §2 S4 and §6 AC3.
- **What is wrong:** 90 S1 and 89 S4 both restate 87 §3's first non-goal. That bullet holds the false equality that M1 confirmed (87:64): "S1's class is charge rule 2's own predicate restricted to module level, so the lift moves no answer AC2 reads". The criteria read other places:
  - 90 AC1 reads 87's S1 range plus a whole-file grep that matches lines 38, 111 and 113, never line 64;
  - 89 AC3 reads 87's S1 and sketch ranges;
  - 89 AC4 reads 87 §3, but only for except/capture/globals().
- **Consequence:** The false sentence can survive both rev bumps with every criterion of 89 and 90 green. 87 keeps telling the next reader that the slice and S1 agree.
- **Fix (judged sound):** Add a range check to 90 AC1 over the 87 spec, `awk '/^## 3/,/^### Edges/'`:
  - piped to `grep -c "moves no answer"`, it must print 0 (it prints 1 at HEAD);
  - piped to `grep -c "annotation"`, it must print at least 1 (it prints 0 at HEAD).

  The alternative is to make 89 AC3 range over 87 §3's first bullet for `derive_conf_rebinds`.
- **Left-shift gate:** Add a checklist entry: "every passage a scope item puts in scope is read by at least one criterion's range". Back it with a lint that maps each "<unit> §n" a scope item cites to an AC range covering it.

### M4. 90 S5/AC5: AC5 passes on S4's loader refusal whether or not S5's plant row exists (id 3)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-90.md` §2 S5, §6 AC5, and the §7 New arm.
- **What is wrong:** S5 adds a plant row over a scratch copy whose tree_lib lacks `derive_constant_charges`. AC5 instead deletes the symbol from a hand-made scratch copy and expects the whole `no-own-conf-read` plant to exit non-zero. S4's loader refusal produces that outcome whether or not S5's row exists. The §7 arm's staged break, "the loader checking one symbol", also exercises only S4.
- **Consequence:** A build that ships S4 but never adds S5's row passes AC5, so the version-skew row M2 asked for is certified without existing.
- **Fix (judged sound):**
  - Have AC5 run the unmodified plant (`python budget.py --fixture --plant no-own-conf-read` in tools/loop/) and require exit 0 with the named row, for example the label `tree_lib lacking derive_constant_charges`, in its output.
  - Keep the hand-made scratch copy as a second half that observes S4.
  - Stage the break: delete the row and see AC5 go red.
- **Left-shift gate:** Add a checklist entry for the fixture-passes-by-finding-nothing class: every criterion that certifies a plant row must name the row in the plant's output, and its staged break must remove that row, not a neighbouring mechanism.

### M5. 90 S4/AC4: loop_witness.py's tree_lib route bypasses the shared loader and its symbol check (id 14)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-90.md` §2 S4, the §4 sketch "The tree_lib route, after this unit (S4)", and §6 AC4.
- **What is wrong:** S4 says "Every route that reaches tree_lib takes the loader", and the sketch calls 86 S21's route "the only one". 75 S35 already has a second route: tools/loop/loop_witness.py imports `GIT_ENV_LEAKS` from tree_lib through resolve_kit_dir. That route is not moved onto the loader, and `TREE_LIB_SYMBOLS` lists only `derive_docstring_ids` and `derive_constant_charges`. AC4's Red-when is kit-wide, but its probe collects only `ast.Attribute` names in loop_lib.py.
- **Consequence:** GIT_ENV_LEAKS entered tree_lib on 2026-10-22 (d6f824049), so it has the same version skew S5 targets. Against an older memory-tree kit, loop_witness.py still crashes with an ImportError traceback instead of the named refusal. AC4 stays green.
- **Fix (judged sound):**
  - Extend S4 so loop_witness.py's GIT_ENV_LEAKS import goes through the same loader, and add GIT_ENV_LEAKS to `TREE_LIB_SYMBOLS`. The alternative is to name 75 S35's route as a priced non-goal.
  - Make AC4 collect tree_lib names from every `*.py` under tools/loop/, counting both `from tree_lib import X` and `tl.X`.
- **Left-shift gate:** Add a loop-kit test that walks every tools/loop/*.py for tree_lib imports and attribute reads. It fails when any name is missing from `TREE_LIB_SYMBOLS` or is reached outside the shared loader.

### M6. 89 AC4: one alternation grep certifies a list of five priced forms (id 21)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-89.md` §6 AC4.
- **What is wrong:** S5 requires five forms to be priced in 87 §3: import, `except ... as`, match capture, def/class, and globals()/setattr. AC4 runs a single `grep -c "except\|capture pattern\|globals()"` that must print at least 1, so it goes green as soon as any one form is written.
- **Consequence:** A 87 bullet that names only the `except` form passes AC4 while four forms stay unpriced. By S5's own Red-when, the next reader then takes the class as total.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** Run one grep per form over 87's `awk '/^## 3/,/^### Edges/'` range, each required to print at least 1. Use tokens that print 0 at HEAD: `except`, `capture`, `globals()`, `setattr`, `import`, and for the def/class form the backticked `` `def` ``. Do not use `reader call`, which already prints 1.
- **Left-shift gate:** Add a spec-lint rule that flags a criterion using a `\|` alternation with a `>= 1` threshold when its scope item enumerates several required forms. It should demand one count per form, each with a token that is red at HEAD.

## Low

### L1. 90 AC1: the pinned baseline says 2 where the grep prints 3 (ids 7, 12)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-90.md` §6 AC1, the figure line ("the second grep prints 2 at HEAD, PINNED 2026-10-24").
- **What is wrong:** The grep prints 3 at HEAD: 87 line 38 (S1), line 111 (`AnnAssign-with-value`) and line 113 (`ast.walk(binding.value)`).
- **Consequence:** Whoever checks that the criterion was seen red finds a mismatch and cannot tell which spelling the figure left out. Behaviour is unaffected.
- **Fix (judged sound):** Correct the figure to 3 and name the three lines: 87 S1, the sketch's walk header and the sketch's value walk.
- **Left-shift gate:** Add a lint that re-runs every "prints N at HEAD, PINNED" figure against its pinned blob and fails on a mismatch.

### L2. 90 S12/AC12: no half of AC12 greps 88 for the `_scan_table23` consumer (id 5)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-90.md` §2 S12 and §6 AC12.
- **What is wrong:** S12 requires 88 S13 and 88's lifted-walk sketch to name TOOL-dTrueNorth-23's AC5 arm (`_scan_table23`) as a consumer the lift keeps green. AC12 only checks that the old literal lambda is gone.
- **Consequence:** 88 can stay silent about the selftest arm that scans the walker, the omission M6 named, while AC12 is green.
- **Fix (judged sound):** Add to AC12: `awk '/^### The lifted charge walk/,/^### Evidence/'` over 88, piped to `grep -c "_scan_table23\|TOOL-dTrueNorth-23"`, prints at least 1, and the same check over 88's S13 range. Both print 0 at HEAD.
- **Left-shift gate:** Use the same lint as M3: every positive requirement in a scope item needs a positive count in its criterion, not only a negative one.

### L3. 90 S11/AC11: the 88-criteria half of S11 is observed by prose with no command (id 6)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-90.md` §2 S11 and §6 AC11.
- **What is wrong:** S11 says 88 AC1, AC6, AC12, AC13 and AC16 each gain the matching range grep. AC11 observes this only with the sentence "each name their sibling's spec text", which has no command and no count.
- **Consequence:** No criterion fails if 88's criteria never gain the greps. AC11's six listed greps do still observe the sibling passages themselves.
- **Fix (judged sound):** Give each criterion a command, for example `awk '/^- \*\*AC6\*\*/,/^- \*\*AC7\*\*/'` over 88 piped to `grep -c "same object"` prints at least 1, with the same pattern for AC1, AC12, AC13 and AC16. The alternative is to drop the 88 half from S11.
- **Left-shift gate:** Add a spec-lint rule that every AC observation line carries a runnable command and an expected count.

### L4. 89 S3: the `with`-held loader row is not valid Python as written (id 8)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-89.md` §2 S3, second row (89.md:56).
- **What is wrong:** `def read_kit_conf(): global KIT_CONF; with open(...) as fh: KIT_CONF = fh.read()` raises SyntaxError, because a compound `with` cannot follow `;`. Nothing in S3 says the rows are shown flattened.
- **Consequence:** Pasted as written into the scratch loop_lib.py, the row gives the unparseable-loop_lib refusal instead of the planted hit. Once noticed, the fix is cosmetic.
- **Fix (judged sound):** Show the row as a multi-line block, matching merge-rows.py:300-323, or say that the plant writes it across lines.
- **Left-shift gate:** Add a spec-lint leg that `ast.parse`s every code row a plant scope item quotes.

### L5. 90 Evidence/F4: 75's line citations are one line off at HEAD (id 11)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-90.md` §4 Evidence, the "Baselines" bullet on 75's lines, and §8 F4 option (b).
- **What is wrong:** The bullet says 75's AC27 and guard arm "sit at 391 and 432". At HEAD they sit at 392 and 433. The figures were measured at 7391b88e6, and 0ac3cda6f then moved 75 by one line.
- **Consequence:** A reader who checks the citation, or who weighs F4's option (b), lands one line off. The outcome is unaffected, because S18 moves to anchor citation.
- **Fix (judged sound):** Restate the figures as 392 and 433 at HEAD. Better, cite by anchor ("75 §6 AC27" and "75 §7 New arm: tools/loop/guard.py · covers AC27"), as S18 itself does.
- **Left-shift gate:** Add a checklist entry: cite sibling specs by section anchor, never by line number. Add a lint that flags `sit at <n>` line citations in Evidence.

### L6. 89 S4: the rebinds union leaves 87 §10 and 86 §10 out of its list (id 16)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-89.md` §2 S4.
- **What is wrong:** S4 restates how derive_conf_constants decides membership across 87 S1, 87's sketch and §3, 88 S13 and its sketch, 86 S13 and its sketch, and 82 S1. It leaves out the §10 reuse audits of 87 and 86. 90 S19 and S11 rewrite those audits to name only the rule-2 slice of derive_constant_charges as the seam.
- **Consequence:** Once both units land, 87 §10 and 86 §10 describe the binding set without the derive_conf_rebinds pass. The next reader may rebuild or drop that pass. The effect stays in spec text, and 89 AC3 and 90 AC19 stay green.
- **Fix (judged sound):** Add 87 §10 and 86 §10 to S4's list. Give AC3 the matching range greps: `awk '/^## 10/,0'` piped to `grep -c derive_conf_rebinds` prints at least 1, over 87 and over 86. The alternative is to have 90 S11 and S19 write the union when they rewrite those sections.
- **Left-shift gate:** Add a checklist entry for the amendment-leaves-its-other-half-standing class: before listing restatement sites, grep every sibling spec for the claim's key phrase, so no site (§10 audits included) is missed.

### L7. 90 S21: a bare OSError renders an empty refusal reason (id 22)

- **Where:** `2026-10-24-spec-TOOL-dDeclaredLoop-90.md` §2 S21 and §6 AC21.
- **What is wrong:** S21 falls back from `strerror` to `str(exc)` only when `strerror` is None. Two cases still render `start failed: ` with nothing after it:
  - `OSError()`, where `str(exc)` is empty;
  - an empty-string `strerror`, such as `OSError(5, '')`, which is not None, so the fallback never fires.

  86 S22 already spells its analogous empty case `(no stderr)`.
- **Consequence:** The refusal still refuses, but with an empty reason. Only the diagnostic text is affected.
- **Fix (judged sound):** Fall back from `strerror` to `str(exc)` to the exception's class name (for example `start failed: OSError`) whenever the earlier value is None or empty. Add an AC21 probe on `OSError()` that expects a non-empty detail.
- **Left-shift gate:** Add a guard.py unit test that feeds the refusal formatter `OSError()`, `OSError(5, '')` and `OSError("boom")` and asserts that the detail is non-empty.

## Refuted findings

Ids 10, 13, 18 and 19 were refuted. Id 10 duplicated id 8. Ids 13, 18 and 19 had premises that proved false on re-probe. The appendix gives each reason.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=22 confirmed=18 refuted=4 unverified=0 blocker=0 high=1 medium=9 low=8 agents=11 out-tokens=149011

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 2 S3 / section 6 AC3 | medium | medium | confirmed | I read 88's S13 range (lines 112-120) with awk. It has no sentence saying the slice leaves 87's answer unchanged. Its only 'unchanged' is 'its four rules unchanged', which is about the lifted walk. The sentence S3 targets is in 88 Edges line 221 ('AC2's answer unchanged (id 17)') and in 87's hands-off 88 edge, line 79 ('with AC2's answer unchanged'). 90 AC3 (lines 261-265) reads only 88's AC13 range. A builder sent to 88 S13 finds nothing there, and AC3 stays green while both edge sentences survive. | sound | two-answers-to-one-question |
| 2 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 2 S1 / section 6 AC1 (and 89 section 2 S4 / AC3) | medium | medium | confirmed | 90 S1 (line 49) puts 87 §3's first non-goal in scope. 90 AC1 reads only 87's S1 range, plus a whole-file grep that matches 87 lines 38, 111 and 113 and never line 64. 89 AC3 ranges over 87 S1 and the sketch. 89 AC4 reads 87 §3, but only for except/capture/globals(). Running awk '/^## 3/,/^### Edges/' over 87 and piping to grep -c 'moves no answer' printed 1 at HEAD. So the false equality sentence on 87:64 can survive with every criterion of 89 and 90 green. Under the proposed check, the same range piped to grep -c annotation printed 0, so both halves are red at HEAD. | sound | two-answers-to-one-question |
| 3 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 2 S5 / section 6 AC5 / section 7 New arm | medium | medium | confirmed | S5 (90.md:69-72) adds a plant row over a scratch copy whose tree_lib lacks derive_constant_charges. AC5 (90.md:271-275) instead removes the symbol from a hand-made scratch copy and expects the whole no-own-conf-read plant to exit non-zero with the refusal text. That outcome comes from S4's loader refusal and is the same whether or not S5's row exists. The §7 arm (line 366) claims AC5 coverage for that row, but its staged break is 'the loader checking one symbol', which also exercises S4 only. A build that drops S5's row passes AC5. | sound | fixture-passes-by-finding-nothing |
| 4 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 4 Write set and sketch 'The tree_lib route, after this unit (S4)' / section 7 Gates | medium | medium | confirmed | 90's S4 sketch (lines 175-182) defines a shared module-level `load_tree_lib()` with a public name. S4 needs derive_conf_reads and derive_conf_constants both to call it. Yet the Write set (lines 169-170) says the pass mints no public module-level def and symbols.json does not move, and §7 (line 361) leaves out codebase-map coverage + freshness. I read tools/codebase-map/map_lib.py:350-356: the symbol tier records every module-level FunctionDef whose name does not start with '_'. grep -c '"id": "_' over symbols.json printed 0. A public load_tree_lib would therefore stale symbols.json. 89 does list symbols.json and the freshness leg for its own public def. | sound | - |
| 5 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 2 S12 / section 6 AC12 | low | low | confirmed | 90 S12 (lines 97-101) requires 88 S13 and its lifted-walk sketch to name TOOL-dTrueNorth-23's AC5 arm (`_scan_table23`). AC12 (lines 309-314) greps 88 only for the literal lambda, to show it is absent. grep -n '_scan_table23\\|TrueNorth-23' over 88 printed nothing, so the omission S12 targets passes AC12. The fix's range is sound: the heading '### The lifted charge walk (S13)' exists at 88:249 and '### Evidence' at 260. | sound | - |
| 6 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 2 S11 / section 6 AC11 | low | low | confirmed | 90.md:96 (S11) says 88 AC1, AC6, AC12, AC13 and AC16 each gain the matching range grep. AC11 at 90.md:305-306 observes that only with the sentence 'The AC1, AC6, AC12, AC13 and AC16 ranges of the 88 spec each name their sibling's spec text'. That sentence has no command and no count, so it cannot go red. The six listed greps do cover the sibling passages themselves. | sound | - |
| 7 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 6 AC1 figure | low | low | confirmed | Re-ran the grep over 87.md and it printed 3, with matches at lines 38, 111 and 113. AC1's figure (90.md, 'the second grep prints 2 at HEAD') is wrong. The criterion itself is unaffected. | sound | - |
| 8 | coherence | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md:section 2 S3, second row | low | low | confirmed | 89.md:56 writes the row as the one-liner `def read_kit_conf(): global KIT_CONF; with open(...) as fh: KIT_CONF = fh.read()`. Re-ran `python -I -c "import ast; ast.parse(...)"` on it and got SyntaxError: invalid syntax, because a compound `with` cannot follow `;`. Nothing in S3 says the rows are shown flattened. | sound | - |
| 9 | grounding | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 4 Write set, section 4 sketch 'The tree_lib route, after this unit (S4)', section 7 | medium | medium | confirmed | 90.md:169-170 says the pass mints no public module-level def, so symbols.json does not move. The S4 sketch at 90.md:177 names a top-level loader `load_tree_lib()`, and S4 requires every route to take it, `derive_conf_constants` included. That means a shared callable. 86 S21 and 88 S33 keep the resolution inline in `derive_conf_reads`, and `grep load_tree_lib` matches only the 90 spec. So the name is new. A probe of symbols.json printed True for the public functions read_kit_conf, load_kit_module and resolve_view_layer, and False for the private names _anchor_root and _KIT_CONF. Siblings 88 and 89 list symbols.json and the `codebase-map coverage + freshness` leg in §7 for public loop_lib defs. 90 §7 lists neither. A public loader would go stale outside 90's write set and red that leg at the bar. The bar still catches it, so the effect is contained. | sound | - |
| 10 | grounding | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md:section 2 S3, second row | low | - | refuted | duplicate of id=8. Same row at 89.md:56, same SyntaxError reproduced, same fix. | sound | - |
| 11 | grounding | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 4 Evidence, 'Baselines' bullet on 75's lines; section 8 F4 option (b) | low | low | confirmed | The 90 blob (ce617b52…) at line 204 says 75's AC27 and guard arm 'sit at 391 and 432', and F4 at line 384 offers '(b) 391 and 432, PINNED'. I ran grep over the 75 spec at HEAD and it printed 392 (AC27) and 433 (New arm). Over `git show 7391b88e6:` the same grep printed 391 and 432. So the figure is one line off where the subject stands now. The impact is cosmetic, because S18/AC18 move 88 to anchor citation anyway. | sound | - |
| 12 | grounding | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 6 AC1, figure line | low | low | confirmed | 90 AC1, at line 253, pins 'the second grep prints 2 at HEAD'. I ran that grep -c over the 87 spec and it printed 3: line 38 (S1, 'an `AnnAssign` with a value'), line 111 ('AnnAssign-with-value') and line 113 ('ast.walk(binding.value)'). The pinned figure is wrong. The criterion is still able to go red. | sound | - |
| 13 | grounding | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 1 Goal, first sentence | low | - | refuted | The premise is false on re-probe. 'Exited CONVERGED' describes the review loop's round-state exit, not the report's verdict heading. memory/builds/dDeclaredLoop/RUN.md:290 reads '2026-10-24T18:10:17Z review · item dDeclaredLoop-spec-set-r8 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 1 · minors 22 · disposition promote'. That matches the goal's 'one high' and the report's confirmed=23. CONVERGED is the round-state token that BUILD-METHOD.md:144-146 and UNATTENDED-VERBS.md:239 define for that exit. The report's own 'CLEAN WITH FIXES' verdict does not contradict it. | unsound | - |
| 14 | reuse | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 2 S4, section 4 'The tree_lib route, after this unit (S4)', section 6 AC4 | medium | medium | confirmed | 75 S35 has tools/loop/loop_witness.py import GIT_ENV_LEAKS from tree_lib through resolve_kit_dir. git log -S shows GIT_ENV_LEAKS was added to tree_lib.py in d6f824049 on 2026-10-22, so a memory-tree kit older than that lacks it. That is the same skew that 90 S5 says govkit cannot floor. 90 S4 says 'Every route that reaches tree_lib takes the loader'. The sketch comments the loader as '86 S21's in-function route, the only one'. TREE_LIB_SYMBOLS holds only derive_docstring_ids and derive_constant_charges. AC4's Red-when is kit-wide ('the loop kit calls a tree_lib symbol its loader never checks'), but its probe collects only ast.Attribute names in loop_lib.py that are module-level defs. A constant import in loop_witness.py is never seen, so AC4 stays green while that route can still raise an ImportError traceback. The effect is contained to the skew path. | sound | - |
| 15 | reuse | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 2 S4 ('That loader is 86 S21's route, extended in place'), section 4 Write set, section 7 | medium | medium | confirmed | 86's sketch (line 183) and S21 resolve tree_lib inline inside derive_conf_reads, and no named loader exists. 90 S4 requires one loader shared by derive_conf_reads and derive_conf_constants (and 89's derive_conf_rebinds), so it has to be a module-level callable. The sketch names it `load_tree_lib()`, a public name. 90's Write set (lines 169-170) says 'The pass mints no public module-level def, so symbols.json does not move'. I probed memory/map/generated/symbols.json: it holds 4983 symbols, public defs such as load_parse_spec_h1 among them, and 0 names starting with an underscore. A public load_tree_lib would therefore add a row this pass never regenerates. 90 §7 leaves out 'codebase-map coverage + freshness', which 89 §7 (line 237) lists for its new public def. One caveat: the sketch is pseudocode, but the name it gives and the Write-set claim contradict each other. | sound | - |
| 16 | reuse | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md:section 2 S4 | low | low | confirmed | Both pinned blobs match the files. I ran `awk '/^## 10/,0'` over spec-87 and spec-86, then `grep -c derive_conf_rebinds`: each printed 0. `grep -n '87 §10\\|86 §10'` over spec-89 printed nothing. 87 §10 already describes how derive_conf_constants decides membership ("S1's predicate is charge rule 2 ... at module level"), so it falls inside the class 89 S4 defines for itself, yet S4's list leaves it out. 90 S19 rewrites 87 §10 and 90 S11 rewrites 86 §10 to name only derive_constant_charges. 90 S1 keeps 89's sentence in 87 S1 only. AC3 of 89 and AC19 of 90 grep other ranges, so this stays green. The damage is limited to spec text. | sound | amendment-leaves-its-other-half-standing |
| 17 | blast-radius | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 4 Write set and 'The tree_lib route, after this unit (S4)'; section 7 leg line | medium | medium | confirmed | spec-90:169-170 says the pass mints no public module-level def, so symbols.json does not move. But the S4 sketch at :177 defines `load_tree_lib():`, and S4 at :67-68 requires every route, including derive_conf_constants', to go through that one loader. Today the route lives inside derive_conf_reads (86 S21: 'inside the function only'; 88 S33 is the same). A loader shared by two functions therefore has to be a new module-level def. `grep -rn load_tree_lib tools/` printed nothing. map_lib.py:351 maps every FunctionDef whose name does not start with '_', and symbols.json has 4983 entries with no id starting with '_'. gate-legs.json has 'codebase-map coverage + freshness' with no guard. The §7 leg line at spec-90:361 leaves that leg out, while 89 §7 includes it. A builder who follows the Write set as written would leave symbols.json stale. | sound | hand-named-gate-list-green-while-the-bar-reds |
| 18 | blast-radius | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md:section 2 S3 (and 90 section 2 S2, S5, S15) | medium | - | refuted | The premise is false on re-probe. 86 S10 (awk over spec-86) already places the conf-read-forms plant and its rows inside functions 80 S1 bounds, 'never as a module-level table'. It also widens 80 S4 to 'every plant a later unit adds to either module'. That class covers any row 89 S3 or 90 S2/S5 adds to that plant, or any plant they add to no-own-conf-read. 90 S15 names 87's rows in addition to that class and does not narrow it. Both specs also keep the `loop budget fixtures` leg (budget.py --fixture) green, and 88 AC9 uses that leg as the check that the no-own-conf-read plant exits 0. So no rule leaves these rows free to sit outside the boundary. | sound | - |
| 19 | blast-radius | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 2 S22 | low | - | refuted | I re-ran `git grep -n "lacks the policy file is graded"`: it shows README:147, the deviation-781 After line and spec-78:1. Deviation 781 is a dated design-to-spec record of the moment unit 78 joined the roster. At rev-1 the unit did state three states, so the After line is historically accurate. HYGIENE (check 14/15's population test, memory/HYGIENE.md:353) holds that 'a record of a moment or an append-only file is not a claim about now'. The deviation grammar (HYGIENE:658-684) corrects a landed record with a new record via Supersedes, never by editing its After text. A record that stays frozen is the repo's design, not a stale copy. | unsound | - |
| 20 | failure-envelope | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md:section 2 S1 and S5 (with section 1, which says the unit names every other binding form as a priced non-goal) | high | high | confirmed | Reproduced. I exec'd the three forms under Python 3.14.5 and got {'CONF': '.unattended.conf', 'W': '.memory-tree.conf', 'L': '.unattended.conf'}, so all three bind module names. 89 S1 (lines 36-45) has only FunctionDef/AsyncFunctionDef loaders, and its module-level walk never enters FunctionDef, ClassDef or Lambda, so it misses a class-body `global` and a walrus in a default argument. Neither set covers them. The 87 S1 binding set excludes class bodies. Charge rule 2 (gen_build_index.py:5146-5186) qualifies class-body assigns by the class (K.CONF), so 88's module-qualified slice drops them. Rule 1 charges signature constants to the function, not to W. For the lambda, the binding set answers `g` but not `L`. S5 (lines 74-80) lists five forms and none of these, while §1 claims every other form is priced. A module reading ll.CONF would be certified as reading no conf on this narrow path, and the list misleads the next reader into treating the class as total. | unsound | - |
| 21 | failure-envelope | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-89.md:section 6 AC4 | medium | medium | confirmed | I read 89.md AC4 at lines 229-232. It requires one `grep -c "except\\|capture pattern\\|globals()"` over 87's §3 range to print at least 1. S5 (lines 75-80) lists five forms that must be priced: import, `except ... as`, match capture, def/class, and globals()/setattr. Any one matching line turns AC4 green, so a bullet that names only the `except` form passes while four forms go unpriced. I re-ran the awk range over 87 at HEAD, piping to grep -c once per token: except 0, capture 0, globals() 0. That matches the finder's 0. The harm stays inside the spec text: a doc criterion under-checks a doc edit and no shipped code is wrong, so medium. | unsound | - |
| 22 | failure-envelope | memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-90.md:section 2 S21 and section 6 AC21 | low | low | confirmed | 90.md S21 (lines 127-130) gives only `strerror`, with a fallback to `str(exc)` when `strerror` is None. AC21 (346-352) probes only OSError("boom") and FileNotFoundError. I ran `python -c` on `str(OSError())` and it printed '', so a bare OSError would render `start failed: ` with nothing after it. An OSError(5,'') would hit an empty-string strerror, which is not None, so the fallback never fires. 86.md:140 does spell its empty-stderr case `(no stderr)`, so the empty detail breaks that pattern. tools/loop/guard.py does not exist at HEAD (grep found no such file), so I judged this against the spec text alone. The refusal still refuses and only the diagnostic text is affected, so low. | sound | - |
