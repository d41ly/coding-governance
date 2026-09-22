**Serves:** spec-audit TOOL-dPromptedSeam-1 TOOL-dPromptedSeam-2

## Verdict: BLOCKED

# Spec audit round 2 — the fold — TOOL-dPromptedSeam-1 (rev-4) · TOOL-dPromptedSeam-2 (rev-3)

**Verdict: BLOCKED · 6 blockers · 8 majors · 7 minors.** Node d, 2026-08-25, tree at `45aa86d7`, base `ee6554c3`. Every claim below was re-derived against the tree; commands and line numbers are given so a skeptic can check rather than believe.

Round 1 returned BLOCKED with six blockers. Two are genuinely fixed. One is fixed in the scope text and refuted by the evidence section beneath it. Three were answered in prose while the mechanism stayed wrong. The fold also introduced three defects of its own, one of which makes an acceptance criterion fail on a correct build.

## Fold audit — what happened to round 1's six blockers

| R1 | Subject | Now |
|---|---|---|
| B1 | Conditional-block mechanism absent from `render_skill()` | **FIXED.** rev-4 drops the condition outright; S3, D3, §10 and §9 all now describe the renderer accurately (`adopt-lexicon.sh:95-123`, six literal substitutions, no fence parser). |
| B2 | AC3 named a renderer, a `deploy.toml` and a target mode that do not exist | **MOVED.** The nonexistent subjects are gone; the replacement asserts a prose property no command returns → **M2**. |
| B3 | Liveness predicate one rule short | **HALF.** S1 now states both rules — correct, including that the length test applies to the RAW subtoken before stemming (matches `map_lib.py:626-628`). The membership is still unwritten (**B1**) and the evidence for the length half was taken over a population that excludes its only instance (**B4**). |
| B4 | §4 measured 231 off-table SYMBOLS | **MOVED.** Re-measured over a different wrong population and mislabelled → **B4**. |
| B5 | S2 vs D3 contradictory return contracts | **NOT FIXED.** S2 was rewritten to three states; D3 was left at two → **B3**. |
| B6 | Fallback with no mechanism, consumer or AC | **FIXED.** D2 cuts it. Residue: §3 does not carry the cut → **m6**. |

---

## TOOL-dPromptedSeam-2 — `read_object`

### B1 — blocker · §3 bullet 2 · §8 Q1 vs §2 S1 — two sections assert an enumeration the spec does not contain
*(lenses U1, C4, P2 — three independent hits)*

§3: the kit "must carry its own list — which S1 enumerates rather than gestures at, because the membership IS the contract". §8 Q1: "it ships its own, ENUMERATED in S1 rather than described." S1's entire text on membership is "the inline stopword set" plus "`map_lib._STOPWORDS` is 21 words and holds no single letters." No word of the set appears anywhere in either spec.

**Why it bites:** the only membership any criterion pins is `of` (AC2's `pin_of`), so a one-word inline set `{"of"}` passes AC1, AC2 and AC3. Over the 16 dead-object names in this corpus the objects split `of` x8, `at` x3, `in` x2, `for` x2, `with` x1 — a set holding only `of` misreports 8 of 16 as usable and nothing observes it. Self-certifying, too: a reviewer who reads §3 is told the enumeration exists and never opens S1.

**Fix:** paste the literal set into S1 as a code fence — `a an the to of in on for and or is be as at by from into with it this that` (verified `tools/codebase-map/map_lib.py:583-586`) — plus the `len(t) >= 2` rule, and state whether the kit's set must EQUAL `map_lib`'s or may be a subset.

### B2 — blocker · §1 Goal · title · §2 S3 — the unit's stated premise is false
*(lens U — reproduced)*

§1: `read_object` "returns the empty string for two DIFFERENT reasons … an identifier with no object at all, and an object whose every token is dead to the stemmer. `--brief` filters on truthiness, so both vanish from its report."

`read_object` (`lexicon.py:856-864`) is `parts = subtokens(name); return "_".join(parts[1:]) if len(parts) > 1 else ""` — no stopword test, no length test, no stemmer. `pin_of` → `'of'`, `_scalar_at` → `'at'`, `boundedK` → `'k'`, all truthy. Only single-token names return `""`. `python tools/lexicon/lexicon.py --brief tools/lexicon/lexicon.py` prints `of: openers x2 (off-table), cache x1, ext x1, …  <-- SPELLED MORE THAN ONE WAY` — the dead group is not merely present, it is the loudest row and a false drift flag. §4 D1 contradicts §1 inside the same file: "16 (2.5%) yield an object with no live stem" — *yield*, not return empty. rev-2 made no such claim; the fold introduced it.

**Why it bites:** the truthiness filter at `:916` collapses ONE state out of the report, not three, so S3's stated cause of the bug is not the cause. An implementer building to §1 removes the filter, adds a no-object group, and leaves the `of:` row exactly as loud as it is today — having fixed the half nobody could see and not the half that is actively lying.

**Fix:** rewrite §1 and S3 to the measured behaviour — `""` for exactly one reason (single-token name), dropped by `:916`; dead-token objects returned truthy and REPORTED today, where they manufacture false `SPELLED MORE THAN ONE WAY` rows. Retitle, state which of the two defects this unit fixes, and paste the current `of:` row as the before-state.

### B3 — blocker · §2 S2 vs §4 D3 vs §6 AC2 — three states specified, two supplied, filter resurrected
*(lenses U3, C5)*

S2: the companion "reports which of the three states produced it." D3, untouched by the fold: it "says whether that string has a live stem" — two-valued, over the returned string, which cannot separate `""` from `pin_of` → `'of'`. AC2 asks only about `pin_of`, `boundedK` and `build_index`, all of which HAVE objects, so no criterion ever asks about a single-token name. No section names the companion's signature, input or return type.

**Why it bites:** an implementer following D3 ships a boolean plus a caller-side emptiness test — which is the truthiness filter S3 says goes — produces three named groups, and passes AC1 byte-for-byte while violating S3's mechanism. An implementer following S2 guesses a tri-state no section defines. Both pass every criterion. This is round 1's B5/M11 re-arranged, not closed.

**Fix:** name it once, e.g. `read_object_state(name: str) -> Literal['live','dead','none']`, taking the IDENTIFIER (the returned string cannot distinguish the two dead cases). Rewrite D3 to that shape and delete "says whether that string has a live stem". Add an AC2 arm on a real single-token function in the target file — `main`, `run`, `extract`, `__init__` — requiring `none`, distinct from `pin_of`'s `dead`.

### B4 — blocker · §4 D1 vs §2 S1/S4 · §6 AC1 — measured over a population that excludes the rule's only instance
*(lenses C2, P1, U2, U5, C3 — five hits, figures reproduced independently)*

D1: "Re-measured over all 644 tracked function definitions: 129 (20.0%) … 16 (2.5%) … 145 of 644, 22.5%." 644 is neither *definitions* nor *all*: it is the count of **distinct Python function names**. The four figures reproduce exactly under that reading and under no other. The corpus `run_brief` actually walks (`lexicon.py:930-940`, which skips only dark and unknown-pattern-set extensions, and `.lexicon.conf:23` arms `js:js-regex:probe`) is **866 definitions / 681 distinct names**; `python tools/lexicon/lexicon.py` prints `P1 verb graded=866` — 222 more than the spec's denominator. Over the population the code sees: 134 empty (19.7%), 18 dead-stem (2.6%).

The bite is not pedantry about a denominator. All 16 dead names D1 counted die by stopword MEMBERSHIP — `_scalar_at anchor_at blob_at` (`at`), `_token_of cache_of ext_of index_of message_of owners_of parent_of pin_of` (`of`), `destinations_for grammar_for`, `fan_in run_in`, `rank_with`. **Not one dies by length.** The two names the narrowing dropped are `boundedK` and `openersOf`, and `boundedK` (`tools/hooks/agent-cap.js:125`) is the single identifier S1, S4 and AC2 all hang the length rule on. So S4's guarantee — "arms over the measured population, not over hand-picked names" — is false precisely at the arm that separates S1's two rules, and D1 supplies zero evidence for the half round 1's B3 forced in. Round 1's own B3 already listed `openersOf`, so the fold narrowed relative to the review it was folding.

**Fix:** re-derive D1 over both declared extractors, publish the command, and label the basis: "866 function definitions across `.py` and `.js`, 681 distinct names; 134 empty (19.7%), 18 dead-stem (2.6%)." List all 18 so `boundedK` and `openersOf` appear, and add one sentence: 16 die by membership, 2 by length — which is the honest strength of the two-rule claim and still supports it. Have `-1` §3's "326 live offenders" state its language scope in the same pass (see **m5**).

### B5 — blocker · §6 AC4 — the criterion reds on any correct implementation of this spec
*(lens U)*

AC4 demands `P1 verb`, `P2 suffix` and `P3 layer` "report the same graded and offender counts as at base `ee6554c3`, proving no predicate moved." P1's `graded` IS the function-definition count. S2 and D3 REQUIRE adding a function ("`read_object` … gains a companion"). Measured: `graded=866` today; appending a four-line `def` to `tools/lexicon/lexicon.py` moves it to `867` (tree restored). Nested defs and methods are counted, so no placement avoids it.

**Why it bites:** an AC that fails on a correct build burns a build pass arguing with the gate, and it quietly overstates §3. "No pin movement" is separately TRUE (`LAYER_OFFENDER_PIN="0"`, `P3 layer offenders=0`); AC4 asserts an unchanged graded POPULATION and presents it as the same fact. Two claims, one sentence, one survivor.

**Fix:** split them. Keep "the three offender counts and the three pins are unchanged" as the criterion; replace the graded pin with "`P1 verb graded` rises by exactly the number of functions this unit adds, and by nothing else." Add one clause to S2: the companion leads with a declared verb, so the offender count cannot move.

### M1 — major · §6 AC3 · §5 — four arms declared, one staged failure
AC3 is byte-unchanged from rev-2 and stages exactly one break ("when the stopword-awareness is reverted … reds naming the stopword arm") while the fold doubled the predicate and S4 now declares four arms; §5 asserts "Each arm staged to fail against the code it guards." Reverting stopword membership leaves `len(t) >= 2` fully armed, so the length arm, the no-object arm and the control never have a failing case observed. The charter: a gate you have only ever seen pass is an assertion about nothing.

**Fix:** one staged break per arm with the expected red named — delete the membership test (stopword arm reds); change `len(t) >= 2` to `>= 1` (length arm reds, `boundedK`/`k` reported live); make the companion return `dead` for `""` (no-object arm reds); make it return `dead` unconditionally (control reds). State that the clean tree reds none of the four.

### M2 — major · §6 AC1 — fabricated exemplar, and non-emptiness of one group out of three
AC1: "the no-object group is non-empty for this file — which it is, since `lexicon.py` defines `_main`". `tools/lexicon/lexicon.py` defines no `_main`; the only occurrence is the `if __name__ == "__main__":` guard at `:1065`, and `_main` lives in `lexicon_conf.py:154`. The file's real groups: no-object `__init__ __str__ extract hits main run`; dead-object exactly `ext_of` (`:204`). This is the same spec-names-code-its-base-lacks class round 1's B4 blocked, reproduced in the fold that retired it — and rev-2's AC1 named a different file, so it is fold-introduced.

Separately, AC1 asserts non-emptiness of ONE group, so a branch that routes dead-object names into the no-object group, or prints an empty dead-object header, passes unchanged. The fold moved the fixture file specifically to get a dead-object case and then failed to assert it.

**Fix:** drop `_main`; assert MEMBERSHIP per group against `tools/lexicon/lexicon.py` — `main` in no-object, `ext_of` in dead-stem, `read_object` (object `object`) in usable. Three named identifiers, three named groups, so no branch can be absent and pass.

### M3 — major · §10 · §3 bullet 2 · §8 Q1 — the port is governed by a docstring, and this kit's other docstring-governed port is already lying
The unit copies a set out of `codebase-map` and makes a docstring the control. The kit already has the gated idiom one file above: `tools/lexicon/adopt-lexicon.sh:26` carries `# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)`, and `tools/lib/resolve-python.test.sh:89-109` is a generic `PARITY_ROWS` engine with a non-empty-population arm per row. Its `git grep -l` is scoped `-- '*.sh'`, so a Python row needs the glob widened. Meanwhile the kit's OTHER port took the docstring route and its documentation is already false: `tools/lexicon/subtokens.py:6` says "A parity leg asserts the two copies agree" and `memory/map/features/lexicon.md:148-151` repeats it — `PARITY_ROWS` holds only `resolve_python` and `kickoff_region`, `tools/gate-legs.json` carries no lexicon parity leg, and `selftest.py` never mentions `map_lib`.

**Fix:** add both to §10 — the `# >>>` marker idiom as the seam to extend, and the subtokens/dossier parity claim as a hit that is **STALE**. Then either land the set under `# >>> lexicon_stems — canonical copy: tools/codebase-map/map_lib.py (byte-identical; gated)` with a `PARITY_ROWS` row (widening that grep to `*.py` is part of this unit and belongs in §2), or spec an equivalent `selftest.py` arm and name the leg in §7. File the stale claim as its own backlog row rather than inheriting it.

### m1 — minor · §5 risks · §10 vs §1 — the caller count is wrong where it prices the risk
§1 now says "its one caller" (correct). §5 still says "The helper has two callers today" and §10 "its two existing callers keep working". Truth: one caller (`run_brief`), three call expressions — `lexicon.py:916` twice inside one comprehension, `:936` once — and `selftest.py` never mentions it, so zero existing coverage. The wrong number is the one pricing the blast radius as low. S3 also names `:916` and never `:936`, which applies the same truthiness test when building the corpus index.

**Fix:** one statement in §4 D1 — "one caller (`run_brief`), three call expressions at `lexicon.py:916` (twice) and `:936`, no existing selftest coverage" — pointers elsewhere. Add one sentence to S3 saying `:936` keeps its truthiness test and why (the corpus index is keyed by object string), so the omission is a decision rather than a gap.

### m2 — minor · §8 Q2 — a resolution mark the format does not contain
The fold changed Q2 from `RESOLVED (agent, 2026-08-25, delegated): NO.` to `MOOT at rev-3:`. `memory/TEMPLATE-SPEC.md:118-124` sanctions exactly two shapes. The gate cannot see it: `check-memory-hygiene.sh` computes `bmark` over the whole §8 blob and fires only on terminal status, so Q1's conforming mark shields Q2 — invisible until the spec goes CLOSED, at which point a fully-resolved spec is byte-indistinguishable from one with open forks. (`-1` §8 Q1's bare `RESOLVED:` has the same problem and predates the fold.)

**Fix:** `RESOLVED (agent, 2026-08-25, delegated): MOOT — D2 cuts the fallback…`, keeping the new reasoning as the body. Attribute `-1` Q1 the same way.

### m6 — minor · §3 — the cut fallback is recorded in §4 and nowhere in the OUT list
D2 is titled "THE FALLBACK IS CUT" and Q2 calls it moot, but §3's four bullets never mention it, and §3 is the list a reviewer greps the diff against. D2's closing sentence ("A fallback acquires a consumer only when something in this kit performs a lookup") reads as an invitation rather than a boundary. Round 1's B6 offered exactly the branch the fold took — "demote D2 to a §3 non-goal" — and the demotion was written into the Design section instead.

**Fix:** fifth §3 bullet — "No full-identifier fallback. Measured and deliberately not built here (§4 D2)."

---

## TOOL-dPromptedSeam-1 — the reuse rung

### B6 — blocker · §2 S1/S3 · §4 D1/D3 · §6 AC1 · §9 · §10 — the rung's one deliverable is a path, and no section names how it is produced
*(lenses U6, P4)*

The unit ships one sentence telling a reader to run `reuse_lookup.py`. `render_skill()` (`adopt-lexicon.sh:95-123`) substitutes six placeholders — `VERBS_TABLE SUGGEST_CLI BRIEF_CLI GATE_CLI CONF KIT_VERSION` — all derived from `KITREL`, the *lexicon's own* dir. Nothing resolves a sibling kit. D3 justifies Tier-1 with "no renderer code path moves", which excludes adding a placeholder; §3 forbids "discovery logic", which excludes a presence probe. The only branch left open is a literal path baked into `SKILL.template.md`, and **no section says what that literal is** — while the template's own neighbouring steps use the derived `{{SUGGEST_CLI}}` form. A hardcoded `tools/codebase-map/` is wrong at any other install prefix, and the spec's Tier-1 claim is what forces it.

The only check is blind to the difference: AC1 pins the bare token `reuse_lookup.py`, and `check_skill` is a render-vs-render `cmp -s`. This repo already recorded that exact failure — `adopt-drift-audit.sh:100-105`: the template hardcoded `workflows/`, the rendered Skill named two files that do not exist, "and `--check` reported 'in sync', because it diffs the render against the template and BOTH carried the same wrong spelling."

The answer already exists in this tree and §10 names none of it (round 1's M6, unfolded): `adopt-memory-tree.sh:36-37,84` derives `TOOL_ROOT` from the kit's install prefix, and **three** carriers already ship the instruction unconditionally to every memory-tree adopter — `BUILD-METHOD.template.md:140` renders `python {{TOOL_ROOT}}codebase-map/reuse_lookup.py "<behaviour phrase, not a symbol name>"` (S2's exact requirement, already worded, loaded by `/session-kickoff` at hand-back), `SPEC-TEMPLATE.template.md:227` names the same script for §10, and `check-memory-hygiene.sh:744` is the forcing function in as many words.

**Fix:** derive the sibling prefix from `KITREL` (the `case "$KIT_REL" in */*)` form drift-audit already uses), declare it as `{{MAP_KIT_DIR}}` in `tools/lexicon/kit.toml`, and update §9 to say the renderer's substitution path moves (it is still Tier-1; it is not still "no code path moves"). Rewrite AC1 to assert that the path the rendered Skill PRINTS resolves to an existing file — `[ -f ]` on the printed token — the one assertion a render-vs-render diff cannot fake. Add the three memory-tree carriers to §10 and rewrite D1 to state what the rung adds over the step that already ships: the MOMENT (a refusal, mid-code) and the AUDIENCE (an author who has already picked a name). Neither is currently written down, and both are the unit's real argument.

### M4 — major · §6 AC3 — the command and the pass condition are unrelated
*(lenses U7, C6, P5)*

AC3: "When `grep -c 'codebase-map' .claude/skills/lexicon/SKILL.md` runs, the rung's sentence names the sibling kit as one the reader may not have…". No expected count is stated, so nothing is compared; the asserted property is a prose judgement no command returns. Verified: that grep returns `0` and exits 1 today, which is §14's no-match trap — the falsifying shape makes the criterion's own command fail rather than report. A rung printing a bare path satisfies it with no hedge anywhere. Two thirds of AC3's body is a rev-3 post-mortem, which is §9's job.

Round 1's B2 fix for the branch rev-4 actually took was explicit: delete AC3 and record in §5 that no kit-absent behaviour survives to gate. The fold kept the id and swapped an unrunnable criterion for an unfalsifiable one.

**Fix:** delete AC3 and say so in §5 — or name the exact hedge string the rung must contain and assert `grep -c '<that literal>' … ` returns exactly 1, with the no-match exit an explicit FAIL. Move the post-mortem to §9.

### M5 — major · §6 AC2 · §5 vs §3/§7 — a pre-existing byte-compare presented as this unit's observed red
`check_skill`'s `cmp -s` reds on any deleted byte, so AC2 passes identically against a rung that names the wrong tool, omits the word `behaviour`, or asks for the name the author picked — the token's identity is irrelevant. Yet AC2 says "The failing case is OBSERVED, per §7's rule for a new check" while §3 says "No new gate leg" and §7 "Adds no leg". The fold added the word "existing" to §5 and left the new-check claim standing one section below. This is `staged-break-substitutes-a-synthetic-value` one level up.

**Fix:** strike "per §7's rule for a new check", and either say plainly in §5 that this unit adds no coverage and rides an existing byte-compare, or repoint AC2 at a break that violates S2 (swap `behaviour` for picked-name phrasing) and name what observes it.

### M6 — major · §6 AC4 — cannot fail, and its stated conclusion is unsound
AC4 pins `--suggest fetch_conf` byte-identical to base "proving the engine was not touched". `run_suggest` (`lexicon.py:786-791`) reads the declaration and nothing else — its docstring says "NO CORPUS PASS" — and `read_object` is referenced only at `:856`, `:916` (twice) and `:936`, all inside `run_brief`. So the pin passes with `read_object` entirely rewritten, i.e. it passes byte-identically in the order `-2`-then-`-1`, where the engine HAS been touched, while asserting the opposite. `-1` changes only markdown, so it cannot fail for `-1`'s own diff either.

**Fix:** keep the `--suggest` run as a smoke check and stop calling it proof. Replace the inference with `git diff --stat <base>...HEAD -- tools/lexicon/lexicon.py tools/lexicon/subtokens.py` returning empty — false the moment `-1` touches the engine, true otherwise.

> **M4 + M5 + M6 together are the real cost:** three of `-1`'s five criteria cannot discriminate a correct implementation from an incorrect one, which leaves AC1 — itself a bare-token grep (**B6**) — as the unit's only load-bearing check.

### M7 — major · §7 — a named leg that is structurally blind to the diff
§7 claims the unit rides `lexicon wiring` **and** `lexicon naming predicates`. `-1` touches only markdown (`SKILL.template.md`, `LEXICON.md`, the rendered `SKILL.md`); `.lexicon.conf` declares `md::dark` and the checker prints `.md=dark` in its own coverage line, so that predicate grades zero definitions from this diff. Its guard (`tools/`, `.claude/`) makes it RUN and report the numbers it would have reported without the unit — armed but unable to observe. `-2` §7 makes exactly the held-leg disclosure `-1` omits, so one build carries two standards of honesty about gates, and the more honest one is on the unit with the smaller blast radius. (`lexicon wiring` really is `guard: []` and really does byte-compare; that half is correct and worth keeping.)

**Fix:** drop the leg or qualify it in the sentence — "runs, but grades nothing here: `md` is `dark`" — and adopt `-2`'s disclosure form.

### m3 — minor · §2 S4 · §6 AC5 — edits a section that does not exist, and would falsify a prose count nothing gates
S4 names "`LEXICON.md`'s delivery section". There is none: the nearest heading is `## How the table reaches whoever is writing the name` (`:32`), whose body at `:36` reads "the declaration is delivered three ways, and none of them is the gate" above exactly three bullets. AC5's `grep -c 'reuse_lookup'` (0 today) counts lines, cannot see which shape the step took, and `md::dark` means no predicate can either. A fourth bullet makes the document state a number that is wrong on the commit that adds it — this repo's own "NO count of a derived population is written in prose", broken by the unit editing the sentence carrying the count.

**Fix:** name the section by its heading; say whether the step is a fourth bullet or a sentence inside the `--brief` bullet; if a fourth bullet, change "three ways" to "four" in the same commit and have AC5 also assert `grep -c 'three ways' … ` returns 0. Add one sentence to `tools/lexicon/README.md:163` ("Uninstalling — the ORDER matters") and to §5: after this unit, removing `codebase-map` leaves the rendered Skill naming a deleted script, and `--check` cannot see it.

### m4 — minor · §1 vs §2 S1 — the goal's trigger is wider than the mechanism's
§1 says "When the lexicon refuses a name"; S1 places the rung in `SKILL.template.md:58`'s "When a name genuinely will not fit" ladder. `--suggest` has two refusal branches, and the one that prints a named replacement (`--suggest fetch_conf` → "use `load_conf`", verified) never needs the ladder. So even a reader who reads the whole Skill meets the rung only on the will-not-fit branch. D4 prices the wrong loss, and the later "is it read" measurement §8 Q1 and the README both promise would run over the wrong denominator.

**Fix:** say it in S1 — the rung fires on the will-not-fit branch, which is where the charter says the name is "reporting an unclear responsibility or a seam in the wrong place". That is the right branch and is the unit's actual argument.

### m7 — minor · §9 — the revision log is monotonic in neither direction
The fold inserted rev-4 as the SECOND entry: `-1` §9 now reads rev-1, rev-4, rev-3, rev-2, while `-2`'s is clean newest-first. Top-down gives rev-1, bottom-up rev-2, the header says rev-4. The hygiene gate only checks that the header's rev appears somewhere in §9, so nothing reds and the whole cost lands on the next session reading the rev high-water cold. Round 1's m3 asked for one direction and this pass made it worse.

**Fix:** rev-4, rev-3, rev-2, rev-1.

---

## Cross-cutting

### M8 — major · build README `## Expected improvements` · `## Build-level rules` · `## Detriments`
The fold's commit `45aa86d7` touched only the README's GENERATED region (roster rows, record counts). Every authored slot still describes the mechanism withdrawn two revisions ago and now contradicts both specs it governs:

- "`read_object()` gains its second consumer" vs `-1` §10 "NOT used by this unit" and `-2` leaving `run_brief` sole caller — after the fold **neither unit adds a consumer**, and the matching Detriments bullet ("stays a single-caller helper") survives the build written to remove it.
- "object `conf` returns `load_conf` at fan-in 16 … Three for three" vs `-1` §3's own "Measured over 326 live offenders, a bare object surfaces a real seam 16.6% of the time".
- Rule 2 "THE HINT NEVER CHANGES A VERDICT" — there is no hint. Rule 3's taxonomy "Map absent, object empty, lookup timed out, lookup refused" vs `-1` §3 "No new conf key, timeout, discovery logic or outcome taxonomy."

BUILD-METHOD makes the rules slot what each pass is checked against, and only the GOAL slot is immutable (`gen_build_index.py:103-108`) — these were amendable and were not amended. A rule that can never fire reads as live governance certifying nothing, and the improvements slot is what a wrap-up derives its claims from: a closing message written off bullet 2 will report a second consumer that does not exist and a 3/3 hit rate the specs refuted. Round 1 raised this as R1/R2 with replacement text.

**Fix:** rewrite improvement 2 to what the build delivers (`--brief` stops silently narrowing the one drift class it measures); replace improvement 3 with a figure from the corrected D1 or delete it; keep rule 1; replace rules 2 and 3 with the one that binds rev-4 — nothing this build adds may move an exit code, a pin or a predicate, and `LAYER_OFFENDER_PIN` stays `0` (verified `.lexicon.conf:98`).

### m5 — minor · both status headers · `-2` AC4 · `-1` AC4 — one build, three answers to "what is the base"
`git rev-parse main` and `git merge-base HEAD main` are both `ee6554c3`. Both spec headers read `base 671e953d`. `-2`'s AC4 reads `ee6554c3` and calls the header value "rev-1's stale one" — a file formally disowning its own machine-readable field, which is what a resumed session actually parses. `-1`'s AC4 still pins `671e953d`, so the two units of one build measure "nothing moved" against different anchors. Harmless in fact — `git diff --name-only 671e953d HEAD` is memory-only, nothing under `tools/` moved — and that fact is written nowhere.

Also unactioned from round 1: neither header carries `ratified <date>` (`TEMPLATE-SPEC.md:118-124` requires it once §8 is fully resolved, and both §8s are), and neither carries `order <n>` — the fold *deleted* "and should land first" from `-2` §1 without adding the declared verb, so the derived region still reads "No spec under this build declares an `order` verb" and both roster rows show `—`. The ordering fix ran backwards. Related: the two specs quote figures over incommensurable sets — `-1`'s 326 spans all declared non-dark languages, `-2`'s 644 is Python-only — and neither says so, which is what makes a reader re-derive both.

**Fix:** set both headers to `base ee6554c3`, have each AC4 say "base as declared in the status header", append `· ratified 2026-08-25` to both tails, add `· order 1` to `-2` and `· order 2` to `-1`, re-run `gen_build_index.py --write` in the same commit, and label both population figures with their language scope.

---

## Clean results worth recording

- **B1 and B6 from round 1 are genuinely fixed.** rev-4's withdrawal of the conditional rung is correct and now described accurately in four places; D2's cut of the fallback is the right call and is well argued. Neither needs re-litigating.
- **S1's ordering claim is right as written.** The length test applying to the RAW subtoken before stemming matches `map_lib.py:626-628` exactly. Only the membership and its evidence are defective.
- **Security lens: clean.** `-2` is a pure string function; `-1` adds no execution, input or run-time read. §9's surfaces are untouched and both §5 security rows are correct.
- **Perf, a11y, i18n, migration/rollback rows: clean** in both specs, including `-2`'s deliberate refusal to appear to fix the carried ASCII finding.
- **`-2` §4 D2 and D4 and `-1` §3's non-goals: clean.** No lens found a defect in the fallback cut, the self-match exclusion, or the OUT list's substance (m6 is a placement defect, not a content one).
- **`-2` §7's held-leg disclosure is the model** the build should adopt everywhere; `-1` §7's `lexicon wiring` claim is correct.
- **The recall-terms blocks in both §10s satisfy M5** and were not re-raised.

## Minimum to unblock

B1 (paste 21 words), B2 (rewrite §1/S3 to the measured behaviour and retitle), B3 (name the companion's signature and tri-state return in D3, add the `none` arm to AC2), B4 (re-derive D1 over both extractors, publish the command, state the 16/2 split), B5 (split AC4's graded pin from its offender pin), B6 (derive the sibling path via a placeholder, state it, and make AC1 assert the printed path resolves). M8 in the same commit — the README is what the next pass is checked against.