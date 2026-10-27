**Serves:** spec-audit TOOL-dRankedPlan-50@rev-1 TOOL-dRankedPlan-51@rev-1 TOOL-dRankedPlan-46@rev-1 TOOL-dRankedPlan-47@rev-1 TOOL-dRankedPlan-48@rev-1 TOOL-dRankedPlan-49@rev-1 TOOL-dRankedPlan-52@rev-1

# Tier-2 spec audit — dRankedPlan, the round-4 audit promotions, units 46 to 52 (round 1)

Provenance: a Tier-2 adversarial review of the seven specs that the fourth spec audit promoted. The finders were gov-spec-reviewer on five lenses, the skeptic batches were gov-skeptic, and the synthesis was gov-synthesizer. The build's purpose is taken from memory/builds/dRankedPlan/README.md and its run mandate.

Reviewed: memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-50.md@63a12d70645882e4566f9a348a6d82369f96fc06, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-51.md@a1ba0de7f1879dd459bb96ef14995f0f4ecfaff8, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-46.md@682ecb953d93566c87d07bb04059c6faa038b32b, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-47.md@0eec070751b996c7f722852306a16e829652c1ec, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-48.md@b371040afecaeb8a05e0ddad5c6fe46cf5a8c649, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-49.md@2226564b8fe3249bedd9609588dcce1f3d5e5145, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md@345100929233a938b0e2e57f6adacff34026d04e

ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers. Nine high findings stand, grouped into eight items. The skeptic judged every high fix sound except id 22, whose corrected fix is written below. The specs should not go to build until items H1 to H8 are folded in. Seven of the eight high items let a hook, script or JS caller invoke `ratify.py` and still pass the deny-by-default always-run ban. H8 leaves a criterion, unit 52's AC11, that cannot go green as written. Every subject drew at least one confirmed finding.

## Review shape

Review shape: intensity full, raw 34, confirmed 32, refuted 2, unverified 0 (0 uncertain), precision 0.94.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 11 | 9 | 2 | 0 | 0 | 0.82 |
| grounding | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 8 | 8 | 0 | 0 | 0 | 1.00 |

By item, the adjudicated tally is 29 items: 0 blocker, 8 high, 14 medium and 7 low.

By raw confirmed finding, the tally is 32: 0 blocker, 9 high, 16 medium and 7 low.

Four defects are split across items because their findings carry different binding grades, and findings are merged only within one grade. Each pair should be fixed by one edit.

- Unit 52's AC11 selection is H8 (id 22, high) and M2 (id 2, medium).
- Unit 49 S2's narrow resolution scope is H5 (id 29, high) and M6 (id 8, medium).
- Unit 52's AC3/AC5 over an empty population is M3 (ids 4 and 14, medium) and L2 (id 26, low).
- Unit 46's staged break is M12 (id 15, medium) and L3 (id 33, low).

### Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified.
- Discards: 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 30 judged sound, 2 judged UNSOUND (ids 22 and 34; the skeptic's corrected fixes are written below), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic, 6 RE-GRADED by the skeptic (ids 1, 2, 12 and 13 from high to medium; ids 5 and 33 from medium to low).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 44 spec documents were supplied as `specs`, as sibling context.
- Checklist: 10 items, each assigned to exactly one of 5 lenses (coherence 2, grounding 2, reuse 2, blast-radius 2, failure-envelope 2).
- By design: none supplied, with no caller byDesign and a block of 0.
- Move check: no checked subject moved.

Every count above is clean, so the run is complete on its own terms.

## High

### H1 — S13's `heredoc-expanded` kind has no shell-arm reader (ids 3, 23)

- **Where:** TOOL-dRankedPlan-52 §2 S13 and S23, §4 'Token kinds in separators mode'; against TOOL-dRankedPlan-46 S1.
- **What:** S13 splits the heredoc token into `heredoc` and `heredoc-expanded`, and gives a reading rule only for an expanded body that unit 47 S1 routes to Python. Unit 46's shell arm is built at order 21, before unit 52 at order 22, against unit 45 S10's single `heredoc` kind. All three of unit 46's plants use a quoted `<<'EOF'`.
- **Consequence:** After unit 52 lands, an unquoted `bash <<EOF` body running `"$py" "$d/ratify.py" "$slug"` arrives under a kind unit 46's router was never told to read. It falls to unit 38's textual rule, which matches only the predicate's name, so the caller passes the ban. No criterion goes red. The tree has no shell-fed heredoc today, so the path is narrow.
- **Fix (skeptic judged it SOUND):** State in S13 that a `heredoc-expanded` body whose command word is in SHELL_BODY_WORDS is read by read_shell_callers, or by S13's line rule. Add an edge to TOOL-dRankedPlan-46. Add plant `caller-heredoc-shell-unquoted` (`bash <<EOF` with the `"$py" "$d/ratify.py" "$slug"` body), refused with exit 1, under a new AC. Stage its failing case with a router that matches only `heredoc`.
- **Left-shift gate:** A spec-token check that a unit splitting a token kind names every sibling unit whose reader consumes that kind.

### H2 — A shell-fed heredoc body never sees the outer file's bindings (id 32)

- **Where:** TOOL-dRankedPlan-46 §2 S1 ('read ... as a file of its own'); with TOOL-dRankedPlan-49 S1 and TOOL-dRankedPlan-52 S13.
- **What:** Unit 46 reads a shell-fed body as a file of its own, so unit 49 S1's bindings, collected 'in the file', never reach it. With an unquoted delimiter the outer shell expands `$r` before bash runs the body, and an exported `r` is visible to the child. No spec says how outer bindings reach a body.
- **Consequence:** `r="$d/ratify.py"` followed by `bash <<EOF` holding `"$py" "$r" "$slug"` passes the ban, and so does `export r=...` with `<<'EOF'`. The body reader sees an unbound `$r`, and the textual rule does not match `ratify.py`. This is a narrow fail-open path.
- **Fix (skeptic judged it SOUND):** State in 46 S1 that the body is resolved against the enclosing file's bindings (49 S1) as well as its own. For a `heredoc-expanded` shell body, also apply 52 S13's line rule. Add plant `caller-heredoc-shell-bound` (outer `r="$d/ratify.py"`, `bash <<EOF` body `"$py" "$r" "$slug"`), refused.
- **Left-shift gate:** A bug-class checklist entry: any reader that treats an embedded body as its own file states which enclosing-scope facts it inherits.

### H3 — `bash -c` and `bash <<<` reach no reader that compares against ratify.py (id 27)

- **Where:** TOOL-dRankedPlan-46 §2 S1 and §3 Non-goals; with TOOL-dRankedPlan-52 S14.
- **What:** Unit 46 covers only a heredoc body fed to bash, sh or $BASH. Its §3 sends `-c` and here-strings to unit 52, but 52 S14 reads them only for command words in unit 47's Python class. Unit 32 S2 sees `bash` as a non-interpreter word, and the quoted `-c` word does not end in ratify.py.
- **Consequence:** `bash -c '"$py" "$d/ratify.py" "$slug"'` and `bash <<< '…'` pass the ban. The tree writes `bash -c`/`sh -c` 158 times, so a new hook is likely to copy the shape.
- **Fix (skeptic judged it SOUND):** In 46 S1, extend the shell arm to the class. For a command word in SHELL_BODY_WORDS, a single-quoted `-c` word and a `<<<` here-string are read by read_shell_callers as files of their own, and any other quoting goes to 52 S13's textual line rule. Add plants `caller-shell-c` (`bash -c '"$py" "$d/ratify.py" "$slug"'`, refused) and `caller-shell-herestring`, each with an AC that exits 1. Alternatively, have 52 S14 name the shell class beside the Python class.
- **Left-shift gate:** A checklist entry: every inline-source channel (heredoc, `-c`, here-string) is listed per interpreter class, and a spec covering one names the others.

### H4 — A resolver substitution binding `g=$(resolve_kit_gate … ratify.py)` is unread (id 28)

- **Where:** TOOL-dRankedPlan-49 §2 S1/S2 and §3 first bullet.
- **What:** Unit 49 compares a literal assignment value against ratify.py and never says what the value of `g=$(…)` is. Under 52 S7 the outer word rebuilds as `g=$()`, which does not end in ratify.py. §3 excludes only a substitution 'whose text does not end in ratify.py', which implies this form is in scope.
- **Consequence:** `if g=$(resolve_kit_gate loop ratify.py); then "$py" "$g" "$slug"; fi` passes the ban. That is the bound shape the repository's hooks write: .githooks/pre-commit:199 and :212, with more resolver bindings in pre-push and manifest-check.sh.
- **Fix (skeptic judged it SOUND):** Add to S1: an assignment whose value is or holds a `$(…)` span takes as its value the span's own words. The value names ratify.py when any word inside the span ends in `ratify.py` with quotes stripped. Add plant `caller-shell-bound-subst` (`if g=$(resolve_kit_gate loop ratify.py); then "$py" "$g" "$slug"; fi`, refused) with its AC and a §4 table row.
- **Left-shift gate:** A checklist entry: a binding rule states its value for every value shape the tokenizer emits, including a nested `$(` span.

### H5 — Unit 49 S2 resolves `$name` only at unit 32's two sites (id 29)

- **Where:** TOOL-dRankedPlan-49 §2 S2. The same defect's `timeout` instance is M6 (id 8).
- **What:** S2 resolves a `$name` word only 'wherever unit 32 S2 compares a word with ratify.py'. Unit 50 S1's wrapper-call test, unit 46's shell-body reading and 52 S13's textual line rule each compare a word with ratify.py separately, and S2 names none of them. Unit 50 is built at order 9 and unit 49 at order 21.
- **Consequence:** `with_hook_index "$py" "$r" "$slug"` and `timeout 60 "$py" "$r" "$slug"` with `r="$d/ratify.py"` pass the ban. This is the tree's own pre-commit:212 shape. It is a narrow fail-open path in a deny-by-default ban.
- **Fix (skeptic judged it SOUND):** Restate S2 for the class: every rule of read_shell_callers that tests whether a word ends in `ratify.py` tests the resolved word. That covers unit 32 S2's two forms, unit 50 S1's wrapper call and 52 S13's line rule. Add plant `caller-shell-bound-wrapper` (`r="$d/ratify.py"`, then `with_hook_index "$py" "$r" "$slug"` under a same-file `$@` function, refused) with an AC.
- **Left-shift gate:** A spec-token check that a cross-cutting rule naming 'wherever unit N compares' also names every later unit that adds a comparison of the same kind.

### H6 — An interpreter option breaks unit 50's wrapper rule (id 30)

- **Where:** TOOL-dRankedPlan-50 §2 S1.
- **What:** The rule accepts the `ratify.py` word only when it follows an interpreter word directly, or when it is the first argument that is neither a dash word nor a duration. In `timeout 60 "$py" -B "$d/ratify.py" "$slug"` the script follows `-B`, and the first qualifying argument is `"$py"`, so neither arm matches. Unit 32 S2 skips `-` words after the interpreter, and the wrapper rule drops that skip.
- **Consequence:** A wrapped call with a Python option passes the ban. The tree writes `"$PY" -B script.py` 27 times (e.g. tools/policy/adopt-policy.sh:87).
- **Fix (skeptic judged it SOUND):** Restate S1's first arm: the `ratify.py` word is the first word not beginning `-` after an interpreter word of unit 32 S2's class. That is the same reading unit 32 S2 gives a bare call. Add plant `caller-shell-timeout-opt` (`timeout 60 "$py" -B "$d/ratify.py" "$slug"`, refused) and a §4 table row.
- **Left-shift gate:** A checklist entry: a rule that restates another unit's invocation reading cites it rather than retyping it.

### H7 — A JS script path bound by `path.join` is unread and not named as unread (id 31)

- **Where:** TOOL-dRankedPlan-48 §2 S3 and §3 Non-goals.
- **What:** An array element names ratify.py only through its `str` tokens. A const bound by `path.join(...)` reaches the array as a `word` token and never matches. Unit 49 adds the shell twin of unit 45 S3's bound-name rule, but no spec gives the JS twin, and §3 lists only template literals as unread.
- **Consequence:** `const s = path.join(kit, "ratify.py"); spawnSync(py, [s, slug])` passes the ban, and no word says the form is unread. The tree's JS hooks pass scripts exactly this way (tools/policy/policy-mirror.js:48/:85, tools/unattended/stop-guard.js:108/:111). No tracked JS invokes a kit Python script at base, so the path is narrow.
- **Fix (skeptic judged it SOUND):** Add an S4 to 48: an element that is a single `word` token naming a `const`/`let`/`var` binding in the same file resolves to that binding's tokens. It names ratify.py when one of their `str` tokens ends `ratify.py` (file-wide, fail closed, as 49 S2). Add plant `caller-js-bound` with an AC. Failing that, list the bound-name form as unread in §3 and in the §4 table.
- **Left-shift gate:** A checklist entry: a rule added for one language's reader is checked against every sibling language reader of the same ban.

### H8 — AC11 is red by construction at unit 52's tip (id 22)

- **Where:** TOOL-dRankedPlan-52 §2 S10 and S11, §6 AC11. The selection-mismatch half is M2 (id 2).
- **What:** AC11 selects every spec of units 30 to 52 containing the text `py.function`: units 30, 32, 33, 34, 35, 37, 44 and 52. Unit 52 matches on prose alone (line 244 reads 'No item mints a function'). S10 carries the symbols.json and freshness-leg fix only to units 5, 41 and 44, and only unit 37 carries unit 45 S30.
- **Consequence:** The other selected specs keep leg lines without `codebase-map coverage + freshness` and Files touched lists without `memory/map/generated/symbols.json`. Units 30 to 35 land at orders 5 to 7, and a landed spec is frozen, so AC11 cannot go green without rewriting landed records.
- **Fix (skeptic judged the finder's fix UNSOUND; the corrected fix):** Do both, not either. Narrow AC11's selection to specs whose §4 Inventory has a function Kind row, which drops unit 52's prose match. Also add hands-off edges from units 30, 32, 33, 34 and 35 to this unit, each carrying S11's leg and symbols.json Files touched line into its pass. Name in S11 every unit the rule reaches (30, 32 to 35, 37, 44).
- **Left-shift gate:** A spec-token check that an AC's selector over sibling specs reads a structured section such as an Inventory row, never a whole-file grep.

## Medium

### M1 — AC4 requires the deferral sentence on units 30 to 37, which nothing adds (ids 1, 13)

- **Where:** TOOL-dRankedPlan-52 §2 S3 and S4, §4 Evidence M3, §6 AC3 and AC4.
- **What:** S3 selects units 30 to 52 whose Files touched names a `tools/loop/` path, and AC4 requires each to hold the deferral sentence once. Units 30 to 37 all touch `tools/loop/` and hold it 0 times. No item or hands-off edge reaches them, and §4 M3 counts only units 38 to 45. §3's non-goal 'Rewriting a landed spec' stops unit 52 editing them.
- **Consequence:** AC4 is red at unit 52's tip on eight specs it never edits, and AC3 goes the same way once the leg lands. The build stalls or quietly narrows the criterion.
- **Fix (skeptic judged it SOUND):** Narrow S3 and S4's population to units 38 to 52, the specs that carry the sentence, and say why units 30 to 37 are exempt. Or give units 30 to 37 a hands-off edge to this unit that carries the deferral sentence into each pass, and name them in S4.
- **Left-shift gate:** A spec-token check that every spec an AC asserts over is either edited by the unit or reached by a hands-off edge.

### M2 — AC11 selects by grep while S11 selects by §4 Inventory (id 2)

- **Where:** TOOL-dRankedPlan-52 §2 S11, §6 AC11. Same defect as H8 (id 22).
- **What:** AC11's whole-file `grep -l 'py.function'` selects unit 52 itself and units 30, 32, 33, 34, 35 and 37, none of which carries the leg. S11 says the selection is by §4 Inventory, so the criterion and the scope disagree.
- **Consequence:** The criterion is red at the tip on a correct build.
- **Fix (skeptic judged it SOUND):** Make AC11 select by the §4 Inventory table, as S11 says: an awk over `### Inventory` rows whose kind cell is `py.function`. Then either give units 30 to 37 a carried item adding `codebase-map coverage + freshness` and `symbols.json`, or narrow the population to units 38 to 52. Fold this with H8, whose corrected fix requires both halves.
- **Left-shift gate:** As H8.

### M3 — AC3 and AC5 are green on today's tree and cannot fail during this build (ids 4, 14)

- **Where:** TOOL-dRankedPlan-52 §2 S3/S5, §6 AC3 and AC5. The related unreachable-rule observation is L2 (id 26).
- **What:** AC3 holds only once gate-legs.json names `loop selftest`, which it does not. AC5 counts legs guarding `{prefix}/loop/`, which is 0, and 0 is at most 5 (BROAD_LEG_FLOOR, check-spec-tokens.py:362). S5's claim that the guards join 'reds a tools/loop/ spec whose leg line omits the leg' is false today, because no leg guards loop/.
- **Consequence:** Two criteria certify the M3 item over an empty population. Neither says it cannot be observed against today's tree, as TEMPLATE-SPEC asks.
- **Fix (skeptic judged it SOUND):** State in AC3 and AC5 that each cannot be observed against today's tree, and name the trigger: gate-legs.json gaining a guard on `{prefix}/loop/`. Make AC5 require at least one leg whose guard holds `{prefix}/loop/`, with that count at most BROAD_LEG_FLOOR, gated on `loop selftest` being in gate-legs.json. Stage the break on a fixture. Either a tools/loop/ spec whose leg line omits `loop selftest`, run through check-spec-tokens' guards join, must red, or a fixture manifest whose loop leg's guard is carried by 6 legs must red.
- **Left-shift gate:** A spec-token check that an AC whose population is empty at base carries a `fixture:` line or a NOT OBSERVED note.

### M4 — The §7 deferral and S3/AC3 name only `loop selftest` (id 24)

- **Where:** TOOL-dRankedPlan-52 §2 S3 and S4, §6 AC3 and AC4; §7 of units 46, 47, 48, 49, 50 and 51.
- **What:** Every subject defers only `loop selftest`, and S3/AC3 check for it alone. The planned manifest also guards `tools/loop/` with `loop breakpoints fixtures` (dDeclaredLoop-79 S8). Unit 45 S18 adds `{prefix}/loop/` to `build-index selftest`, and unit 45 S17 owes 'every other leg whose guard is {prefix}/loop/'.
- **Consequence:** S3/AC3 can go green while those legs are missing, which narrows 45 S17. Once the legs land, the guards join reds every subject spec at its pass.
- **Fix (skeptic judged it SOUND):** Restate the §7 deferral in units 46 to 52 as 'every leg whose guard trips tools/loop/ (loop selftest, loop breakpoints fixtures, and build-index selftest once unit 45 S18 lands)'. Make S3/AC3 compare each selected spec's leg line with the legs check_guard_trips derives from tools/gate-legs.json, not with one hard-coded name. Name both added legs on the leg lines of 46, 47, 49, 50 and 51.
- **Left-shift gate:** A spec-token check that a leg deferral is derived from check_guard_trips over the planned manifest, never typed as a single name.

### M5 — Step 12 dispatches as parallel before symbols.json reaches the write lists (id 25)

- **Where:** TOOL-dRankedPlan-52 §2 S10, §6 AC10.
- **What:** S10 has units 5 and 44 add `memory/map/generated/symbols.json` to Files touched 'in their own pass'. The README's step-12 row is generated from those Files touched and reads `| 12 | TOOL-dRankedPlan-44, TOOL-dRankedPlan-5 | yes |` (line 190). BUILD-METHOD M6 decides concurrency from write lists written before dispatch.
- **Consequence:** The two symbols.json writers can be dispatched concurrently, which is the M6 clause 3 hazard S10 exists to prevent. AC10 reads the row only at unit 52's tip, after the fact.
- **Fix (skeptic judged it SOUND):** Fold the symbols.json Files touched line into specs 5 and 44 now, during the spec run, so the build-order render reads `no` before step 12 dispatches. Or state in S10 that step 12 is sequenced at dispatch whatever the render says, and observe the README row before step 12 rather than at 52's tip.
- **Left-shift gate:** A checklist entry: a write-list change that alters a parallel decision is folded before the step it governs dispatches.

### M6 — Unit 49 S2 does not resolve a bound path behind `timeout` (id 8)

- **Where:** TOOL-dRankedPlan-49 §2 S2. Same defect as H5 (id 29).
- **What:** S2 resolves `$name` only at unit 32 S2's two invocation forms. Unit 50 S1's wrapper call is a third comparison site, and S2 never names it.
- **Consequence:** `timeout 60 "$py" "$r"` with `r="$d/ratify.py"` passes the ban, and so does a bound path behind a `$@` wrapper function. That combines the hook shape at .githooks/commit-msg:76/:104 with the wrapper shape at pre-commit:212.
- **Fix (skeptic judged it SOUND):** Extend S2 to every ratify.py word comparison of units 32 S2, 50 S1 and 46 S1. Add plant `caller-shell-bound-timeout` (`r="$d/ratify.py"; timeout 60 "$py" "$r" "$slug"`), refused with exit 1. Fold this with H5.
- **Left-shift gate:** As H5.

### M7 — A `$(…)/ratify.py` binding reads as an empty value (id 12)

- **Where:** TOOL-dRankedPlan-49 §2 S1, §3 first bullet, §6.
- **What:** The shared tokenizer splits `r="$(cd "$(dirname "$0")" && pwd)/ratify.py"` into `r="` plus separate words, so S1's assignment collector sees an empty value. §3 leaves this form in scope. Unit 52 S7's piece rebuild lands later, at order 22, and its plant covers only the direct form. Nothing says the assignment collector reads rebuilt words.
- **Consequence:** The ban fails open between orders 21 and 22, and the combined form is tested by no plant. The idiom appears 120 times in the tree (e.g. .githooks/pre-commit:111), but none of those lines binds a ratify.py path today.
- **Fix (skeptic judged it SOUND):** State in S1 that an assignment word is read as unit 52 S7 rebuilds a `$(`-interrupted word, so `r="$()/ratify.py"` binds. Add plant `caller-shell-bound-subst` holding `r="$(cd "$(dirname "$0")" && pwd)/ratify.py"` then `"$py" "$r" "$slug"`, refused with exit 1, as an AC. Or move this case to unit 52 with that plant there. H4 proposes the same plant name, so give the two plants distinct names.
- **Left-shift gate:** As H4.

### M8 — Unit 50 S1's direct-script branch is observed by no criterion (id 9)

- **Where:** TOOL-dRankedPlan-50 §2 S1, §6.
- **What:** S1's second branch fires when the first argument that neither begins `-` nor is a duration ends in ratify.py. It has a §4 row, `timeout -k 5s 60 "$d/ratify.py" "$slug"`. But all three S4 plants put `"$py"` right before the path, and AC1 to AC3 observe only those plants.
- **Consequence:** A builder can omit the direct branch and the duration grammar with every AC green. `timeout 60 "$d/ratify.py"` then passes the ban.
- **Fix (skeptic judged it SOUND):** Add plant `caller-shell-timeout-direct` with `timeout -k 5s 60 "$d/ratify.py" "$slug"` and an AC that it exits 1, listed on the New arm line.
- **Left-shift gate:** A spec-token check that every branch of a rule and every §4 table row marked 'caller' maps to at least one plant.

### M9 — Unit 50's §4 table calls a caller 'not a caller' (id 17)

- **Where:** TOOL-dRankedPlan-50 §4 'The reading after this unit', row `with_hook_index cp "$s" "$d/ratify.py"`.
- **What:** `"$s"` is a `$` variable, which puts it in unit 32 S2's interpreter class, and `"$d/ratify.py"` follows it directly. S1 therefore makes the row a caller. The table says 'not a caller', and §5 risks says this shape is refused.
- **Consequence:** A builder writing tests from the table gets an assertion that contradicts S1.
- **Fix (skeptic judged it SOUND):** Change the row's answer to 'caller, fails closed'. Or pick a non-caller example with no `$` word before the path, such as `with_hook_index cp src.py "$d/ratify.py"`.
- **Left-shift gate:** M8's gate catches this if it also asserts each table row's verdict.

### M10 — `parse_shell_defs` is cited as finding a function body it does not return (id 20)

- **Where:** TOOL-dRankedPlan-50 §2 S2 and §10; TOOL-dRankedPlan-51 §10.
- **What:** S2 finds a wrapper function's body through `parse_shell_defs(text)`. But tools/lexicon/lexicon.py:747-803 returns only `(name, line)` pairs over the default-mode stream, and never the opener or the body's end. Unit 51 §10 repeats the overstatement.
- **Consequence:** The builder re-matches the four definition forms over unit 41's `seps=True` stream in `ratify.py`. That is a second recognizer next to the shared one, and the two can drift. A body opening on a later line could be missed, and that wrapper's calls would pass the ban.
- **Fix (skeptic judged it SOUND):** Choose one seam and write it into S2. Option (a): extend `parse_shell_defs` in the canonical block with an opt-in keyword that also returns each definition's body span, mirroring unit 48's `strs` and unit 41's `seps`. The default return stays unchanged, the copies go under the parity row, and the block files go in Files touched. Option (b): drop the citation and state the four forms S2 matches over the `seps=True` stream itself, with a plant whose body opens on a later line. Correct unit 51 §10 to match.
- **Left-shift gate:** A checklist entry: a cited seam is quoted by its return signature, and a spec needing more than it returns says so.

### M11 — Unit 46 S1's two normalizations are observed by no criterion (id 10)

- **Where:** TOOL-dRankedPlan-46 §2 S1, §6.
- **What:** S1 respells `${name}` as `$name` and compares a literal path by its last segment, and the routing table lists `${BASH}` and `/bin/bash`. The plants and AC1 to AC3 use only bare `bash` and `"$BASH"`.
- **Consequence:** A builder can skip both normalizations with every AC green. A `/bin/bash <<'EOF'` or `"${BASH}" -s <<'EOF'` body then falls to the Python reader or the textual rule. The textual rule passes a ratify.py caller.
- **Fix (skeptic judged it SOUND):** Add plant `caller-heredoc-shell-path` feeding `/bin/bash <<'EOF'` the same body, plus a `${BASH}` case, with an AC that each exits 1. Name both on the New arm line.
- **Left-shift gate:** As M8.

### M12 — Unit 46's staged break cannot turn AC2 red (id 15)

- **Where:** TOOL-dRankedPlan-46 §7 New arm line, §6 AC2; with TOOL-dRankedPlan-47 S1. The related AC1 overclaim is L3 (id 33).
- **What:** Unit 47 S1 already excludes `SHELL_BODY_WORDS` from the Python arm, which settles how `"$BASH"` is routed. Unit 46 S2 also orders the shell test first, and its staged break is 'a router that tests the interpreter class before the shell words'. Because of 47's exclusion, a reordered router still rejects `"$BASH"` from the Python arm, and it falls through to the shell test.
- **Consequence:** The new arm is never seen red. S2's ordering rule reads as covered while nothing exercises it.
- **Fix (skeptic judged it SOUND):** Pick one mechanism. Either drop 'and is not in SHELL_BODY_WORDS' from unit 47 S1 and rely on S2's order, or keep the exclusion and drop S2. Then change unit 46's staged break to one that reds AC2, such as removing `$BASH` from SHELL_BODY_WORDS.
- **Left-shift gate:** A checklist entry (class guard-above-a-fold-makes-its-fallback-dead): a staged break is checked against every sibling guard that already decides the same input.

### M13 — The 'fails closed' premise for a shell body read as Python is false (id 16)

- **Where:** TOOL-dRankedPlan-47 §4 'The routing after this unit', §5 risks; TOOL-dRankedPlan-46 AC2's Red-when.
- **What:** Unit 47 says reading a non-Python `$`-variable body as Python fails closed. But `"$py" "$d/ratify.py" "$slug"` parses as Python, as three adjacent string literals, holds no argv list, and passes. Unit 46 AC2's 'the Python reader, which exits 2 on shell source' rests on the same false premise.
- **Consequence:** A heredoc fed to a shell through any `$` variable other than `$BASH` that runs the predicate's CLI fails open. The tree writes none at base. The justification for the catch-all routing is wrong, and AC2's stated failure mode misleads its builder.
- **Fix (skeptic judged it SOUND):** Correct §4 and §5 to say a shell-syntax body can parse as Python and pass. Either route a `$` variable outside the Python names through both readers, or state the fail-open as the ceiling. Respell unit 46 AC2's Red-when to match.
- **Left-shift gate:** A checklist entry: a 'fails closed' claim is backed by a probe of the actual input, recorded in §4 Evidence.

### M14 — Unit 51 reads an array value `name=(…)` and `((…))` as commands (id 34)

- **Where:** TOOL-dRankedPlan-51 §2 S1, §4 'The reading after this unit'.
- **What:** S1 makes every `(` and `)` op end a command, and says nothing about array assignments or arithmetic. `cmd=("$py" "$d/ratify.py" "$slug")` becomes a command invoking ratify.py with no mode flag, and `((n > 0))` becomes a junk command `n 0`.
- **Consequence:** An array built for a later `"${cmd[@]}" --exit` is falsely refused, on the tree's own idiom (tools/lib/lib-selftest.sh:151-154). Both cases fail closed, but the spec states neither.
- **Fix (skeptic judged the finder's fix UNSOUND; the corrected fix):** State in 51 S1 and §4 that the words of an array value `name=(…)` are read as a command of their own. Such an array that invokes ratify.py is refused unless its own words hold a mode flag. §4 records as the ceiling that a mode flag added only at the `"${name[@]}"` call site is not read. Add plant `caller-shell-array-exit` (`cmd=("$py" "$d/ratify.py" "$slug"); "${cmd[@]}" --exit`), refused, as that ceiling. Also state that `((`…`))` is arithmetic, and its words are not a command.
- **Left-shift gate:** A checklist entry: a rule keyed on an op token lists every construct the tokenizer emits that op for.

## Low

### L1 — AC10's grep prints two README rows (id 5)

- **Where:** TOOL-dRankedPlan-52 §6 AC10.
- **What:** `grep -n '^| 12 |' memory/builds/dRankedPlan/README.md` prints the roster row for unit 12 (line 71) and the build-order row (line 190). Line 71 never ends `| no |`.
- **Consequence:** A literal check over every printed row reds on a correct build. The intended row is obvious to a reader, and no shipped behaviour is affected.
- **Fix (skeptic judged it SOUND):** Scope the grep to the gen:build-order block, e.g. `sed -n '/gen:build-order/,/\/gen:build-order/p' README.md | grep '^| 12 |'`, or match `'^| 12 | `TOOL-dRankedPlan-44`'`.
- **Left-shift gate:** A checklist entry: an AC's grep is run once at spec time and must print exactly the rows it names.

### L2 — AC5 can be turned red only by a manifest edit outside this unit (id 26)

- **Where:** TOOL-dRankedPlan-52 §2 S5, §6 AC5. Same population as M3.
- **What:** AC5 is green at base (count 0) and stays green after the build, because unit 52's Files touched never edits tools/gate-legs.json. It checks that a count stays under a floor. It does not check S5's claim that the join reds a tools/loop/ spec whose leg line omits the leg.
- **Consequence:** The criterion looks like coverage of the guards-join hold, but it never fires on the defect S5 names.
- **Fix (skeptic judged it SOUND):** Replace AC5 with an observation that can fail. One option is to run check_guard_trips('tools/loop/ratify.py', g) over the manifest and assert that at least one non-broad leg trips. A better option is for the build to stage a copy of one subject spec with `loop selftest` removed from its leg line, and observe the spec-tokens join report `loop selftest <- tools/loop/ratify.py`. This is a described probe, not run here. Fold this with M3.
- **Left-shift gate:** As M3 (class armed-but-unreachable-rule).

### L3 — Unit 46's New arm line claims AC1 under a break that leaves it green (id 33)

- **Where:** TOOL-dRankedPlan-46 §7 New arm line. Related to M12.
- **What:** The staged break 'a router that tests the interpreter class before the shell words' cannot redden AC1 or AC3. `bash` is not in unit 32 S2's interpreter class, so AC1's body still reaches the shell reader. Only AC2's `"$BASH"` moves, yet the line says it covers AC1, AC2 and AC3.
- **Consequence:** The red-first observation is weaker than claimed. AC1 itself still fails on a build missing the shell arm, so behaviour is unaffected.
- **Fix (skeptic judged it SOUND):** Stage two breaks. Break (a) is a router with no SHELL_BODY_WORDS test, so bash bodies go to the textual rule only, and it reddens AC1 and AC2. Break (b) is a router that tests the interpreter class first, and it reddens AC2. List per break which AC goes red, and keep AC3 as green-only. Fold this with M12.
- **Left-shift gate:** A checklist entry: each staged break lists the ACs it reddens, checked against the class definitions it relies on.

### L4 — Unit 48 AC1 asks for equality with a stream §4 does not fully pin (id 11)

- **Where:** TOOL-dRankedPlan-48 §6 AC1, §4 Evidence.
- **What:** AC1 requires the default stream to 'equal the §4 probe's output', but §4 pins only five tokens, 'among its tokens'. The real stream also holds `const`, `a`, `=` and `;`.
- **Consequence:** The 'default stream unchanged' guard is decided by whatever baseline the builder picks.
- **Fix (skeptic judged it SOUND):** Pin the full stream in §4: [('word','const',1), ('word','a',1), ('op','=',1), ('op','[',1), ('op',',',1), ('op',',',2), ('word','slug',2), ('op',']',2), ('op',';',2)].
- **Left-shift gate:** A checklist entry: an AC asserting equality points at a fully pinned value.

### L5 — Unit 47's heredoc count includes three test-input strings (id 18)

- **Where:** TOOL-dRankedPlan-47 §4 Evidence third bullet, §4 Alternatives rejected first bullet.
- **What:** The three bare `python` hits at tools/unattended/gate-guard.test.sh:417, :427 and :430 are quoted strings passed to `run`, not heredocs. So 'thirty of the thirty-three Python heredocs' overcounts. The bare-form regex is not stated, so the count cannot be re-run.
- **Consequence:** The effect is contained, because the `$`-form majority still holds.
- **Fix (skeptic judged it SOUND):** State the bare-form regex, and record that its 3 hits are single-quoted test-input strings.
- **Left-shift gate:** A checklist entry: every count in §4 Evidence is stated with its exact command.

### L6 — Units 46 and 47 cite stale lines for unit 45's reader table (id 19)

- **Where:** TOOL-dRankedPlan-46 §4 Evidence first bullet; TOOL-dRankedPlan-47 §4 Evidence first bullet.
- **What:** Both cite unit 45's 'File kinds and readers' table at lines 256-263. The heading is at line 260, and the two heredoc rows these units supersede are at 267-268.
- **Consequence:** Cosmetic only.
- **Fix (skeptic judged it SOUND):** Cite unit 45's table at lines 260-269, or cite it by heading and row content.
- **Left-shift gate:** A checklist entry: cite a sibling spec by heading and row, not by line.

### L7 — Unit 49 §10 misses two sibling assignment readers (id 21)

- **Where:** TOOL-dRankedPlan-49 §10, §2 S1/S2.
- **What:** §10 says no existing reader reads a shell assignment. Two already do: tools/gate-lint/sh_hygiene.py:160-163 (ASSIGNMENT with the same five leaders plus `+?=`, and EXPANSION) and tools/process-monitor/scope.py:38-39. sh_hygiene.py:325 clears a name on re-assignment. S2 makes the opposite choice without saying why, and S1 is silent on `NAME+=`.
- **Consequence:** Documentation and reuse only. It repeats the missed-sibling gap that unit 52 S20/S21 repair elsewhere.
- **Fix (skeptic judged it SOUND):** In §10, cite `tools/gate-lint/sh_hygiene.py:160-163` and `tools/process-monitor/scope.py:38-39` as sibling readers that are cited and not imported, since a copy-installed kit imports from no sibling. In Alternatives rejected, state why S2 keeps every assignment instead of clearing on re-assignment (fail closed). In S1, say whether `NAME+=value` counts as an assignment, and add a criterion that observes it.
- **Left-shift gate:** A reuse-audit step that greps every kit under tools/ for the rule's regex before §10 claims no seam fits.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=34 confirmed=32 refuted=2 unverified=0 blocker=0 high=9 medium=16 low=7 agents=11 out-tokens=161013

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S4 / section 6 AC4 | high | medium | confirmed | I re-ran the probe over units 30 to 52. Each of units 30 to 37 has a tools/loop/ path in Files touched (loopFT 1 to 4), but its count of "is owed once dDeclaredLoop's loop legs are in the manifest" is 0. Every one of units 38 to 52 except 42, which has no loop path, has the sentence once. Running grep -ln for 'hands-off** `TOOL-dRankedPlan-52`' lists only units 5, 38-41, 43-47, 50 and 51, so no edge reaches units 30 to 37. Unit 52's §3 non-goal 'Rewriting a landed spec' stops unit 52 from editing them. So AC4 over S3's population is red on a correct build. The effect is a red or quietly narrowed criterion, not shipped behaviour, so I grade it medium. | sound | - |
| 2 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S11 / section 6 AC11 | high | medium | confirmed | Re-probed. Whole-file grep -l 'py.function' over units 30 to 52 selects 30, 32, 33, 34, 35, 37, 44 and 52. Unit 52 has 4 prose hits but 0 py.function rows in its Inventory, and its line 244 reads 'No item mints a function.' Units 30, 32, 33, 34, 35 and 37 each have one py.function Inventory row, and 0 hits for both 'codebase-map coverage + freshness' and symbols.json. S10 carries the render only to units 5, 41 and 44. AC11 selects by grep while S11 selects by §4 Inventory, so the two disagree, and AC11 cannot pass at the tip. | sound | - |
| 3 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S13 | high | high | confirmed | Read unit 52 S13 (lines 121-129). It splits the heredoc token into `heredoc` and `heredoc-expanded`, but gives a reading rule only for an expanded body that unit 47 S1 routes to Python. Unit 46 S1 (order 21) consumes unit 45 S10's single `heredoc` token (its Edges line 62), and all three of its plants use quoted `<<'EOF'`. Nothing in S13, and no criterion of unit 52, says the shell arm also reads `heredoc-expanded` bodies, and no plant covers an unquoted `bash <<EOF`. A router keyed on the `heredoc` kind would send such a body to unit 38's name-only textual rule. That rule does not match ratify.py, so a caller passes the deny-by-default ban. The tree has no shell-fed heredoc (unit 46 §4), so the path is narrow, which makes it high. | sound | - |
| 4 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S3/S5, section 6 AC3 and AC5 | medium | medium | confirmed | grep -c '"loop selftest"' tools/gate-legs.json printed 0. A python scan of the 144 legs found 0 whose guard holds 'loop/'. check-spec-tokens.py:362 has BROAD_LEG_FLOOR = 5. So AC3's condition is false today and the AC decides nothing, and AC5's 0 <= 5 is green before the unit is built. S5's claim that the join 'reds a tools/loop/ spec whose leg line omits the leg' does not hold, because no leg guards loop/. Neither AC states this. TEMPLATE-SPEC (lines 525-532) asks a criterion that cannot be observed against today's tree to say so, with a fixture: line. | sound | fixture-passes-by-finding-nothing |
| 5 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 6 AC10 | medium | low | confirmed | grep -n '^\| 12 \|' memory/builds/dRankedPlan/README.md printed two rows: line 71, the roster row for TOOL-dRankedPlan-12, and line 190, the build-order row. Line 71 never ends `\| no \|`, so a literal check over every printed row reds on a correct build. The intended row is obvious to a reader and no shipped behaviour is affected, so I grade it low. | sound | - |
| 6 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S24 against S17-S21 and AC17-AC21 | medium | - | refuted | The cited section already states one rule (case 2), and part of the premise is false (case 3). Unit 52 §3 reads: 'Rewriting a landed spec. Every correction here names the sentence it supersedes, and the earlier unit's builder carries it out in its own pass.' So a unit edits its own spec in its own pass, reached by a hands-off edge, and a later unit never edits another unit's spec. Units 39, 40 and 45 each carry a hands-off edge to 52 that names S17/S21, S20 and S18/S19 respectively. S24 withdraws unit 43's edit of unit 34's spec, which is exactly a later unit editing another's spec. Unit 49 S4 has no carry edge from unit 39, so 'not edited' agrees with the rule. S19 does not have unit 45 edit unit 31's spec. It amends unit 45's own AC10, which greps unit 31's spec, and unit 31's line 66 hands-off to 45 carries the corrections into unit 31's own pass. AC17 to AC21 printing 0 today is expected before those units build. | unsound | two-answers-to-one-question |
| 7 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-51.md:section 6 AC4 / section 4 Rollout (order 9 against unit 40 at order 8) | medium | - | refuted | The premise is false on re-read (case 3). Unit 40 S2 (lines 36-38) reads 'up to a word ending in an unquoted `)`, or up to a `)` token'. The `)` op alternative lets unit 40 AC2 pass on a faithful build at order 8, even though the word clause matches nothing. Unit 51 AC4 is not vacuous either. Unit 51 S1 changes the command model so that `)` ends a command, which removes the in-command `)` token that unit 40's rule reads. AC4 re-observes `caller-shell-case` under the new model, and it goes red if S1 is built without S3's restatement. It is a real regression check on this unit's change. | unsound | - |
| 8 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-49.md:section 2 S2 | medium | medium | confirmed | Unit 49 S2 (lines 35-40) limits resolution to the places where 'unit 32 S2 compares a word with ratify.py' and to 'both invocation forms of unit 32 S2'. Unit 50 S1 (lines 31-37) adds its own comparison: a wrapper call's argument word that 'ends in ratify.py', either next to an interpreter word or as the first non-option, non-duration argument. Unit 49 never names that site, and its Edges list only units 45 and 41. Read literally, `timeout 60 "$py" "$r"` with r bound to a ratify.py path is not resolved. The effect is limited to one combined form. | sound | - |
| 9 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-50.md:section 2 S1 / section 6 | medium | medium | confirmed | In unit 50, S1 line 35-36 gives a second branch (the first argument that neither begins `-` nor is a duration), and the §4 row at line 107 says `timeout -k 5s 60 "$d/ratify.py" "$slug"` is a caller. But all three S4 plants (lines 50-54) put "$py" right before the path, and AC1-AC3 (lines 160-168) observe only those plants. A builder could leave out the direct branch and the duration grammar and every criterion would stay green. | sound | - |
| 10 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-46.md:section 2 S1 / section 6 | medium | medium | confirmed | Unit 46 S1 (lines 33-34) requires two normalizations: `${name}` respelled as `$name`, and a literal path compared by its last segment. The routing table at line 81 lists `${BASH}` and `/bin/bash`. Yet the plants and AC1-AC3 (lines 43-49, 124-133) use only bare `bash` and `"$BASH"`, so neither normalization is tested by any criterion. | sound | - |
| 11 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-48.md:section 6 AC1 against section 4 Evidence | low | low | confirmed | I re-ran scan_ts_tokens on the §4 input in tools/lexicon. It printed [('word','const',1),('word','a',1),('op','=',1),('op','[',1),('op',',',1),('op',',',2),('word','slug',2),('op',']',2),('op',';',2)]. Unit 48 §4 (lines 68-70) pins only five of these tokens, 'among its tokens'. AC1 (lines 128-131) asks the default stream to 'equal the §4 probe's output', which the spec does not fully pin, so that equality cannot be taken literally. | sound | - |
| 12 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-49.md:section 2 S1, section 3 first bullet, section 6 | high | medium | confirmed | I re-ran the probe. scan_shell_tokens splits `r="$(dirname "$0")/ratify.py"` into the words 'r="', 'dirname', '"$0"' and '/ratify.py"', so unit 49 S1's assignment collector would see the value as empty. Unit 49 §3 excludes only a substitution 'whose text does not end in ratify.py', so this form is in scope, and nothing observes it. The git grep count of 120 reproduces, and pre-commit:111 is the idiom. Two things lower the grade. None of the 120 lines binds a ratify.py path (adding grep -c ratify.py printed 0). And unit 52 S7 says read_shell_callers itself rebuilds a `$(`-interrupted outer word, which would plausibly cover the assignment collector from order 22 on. What remains is a fail-open window between order 21 and order 22, plus a combined form no plant tests, rather than a shipped hole on a live shape. | sound | - |
| 13 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S3 and S4, section 4 Evidence M3, section 6 AC3 and AC4 | high | medium | confirmed | Unit 52 S3 selects units 30 to 52 whose Files touched names a tools/loop/ path, and AC4 requires the deferral sentence exactly once while gate-legs.json lacks the leg (grep -c '"loop selftest"' printed 0). My loop over units 30-52 printed owed=0 for units 30-37, each with tools/loop/ paths in Files touched, and owed=1 for 38-41, 43-52. Unit 42 has no loop path. None of units 30-37 has a hands-off edge to unit 52 or carries the sentence, and §4 M3 counts only units 38-45. AC4 is therefore red at the tip on specs this unit does not edit. | sound | - |
| 14 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S5, section 6 AC5 | medium | medium | confirmed | I loaded tools/gate-legs.json: 144 legs, and none has a guard containing 'loop/'. grep -c '"loop selftest"' printed 0, and check-spec-tokens.py:362 has BROAD_LEG_FLOOR = 5. AC5 ('at most 5') already passes at base over an empty set, and S5's claim that the join reds a tools/loop/ spec without the leg does not hold while no leg carries that guard. | sound | - |
| 15 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-46.md:section 7 New arm line, section 6 AC2 (with TOOL-dRankedPlan-47 S1) | medium | medium | confirmed | Read 47:31-34. S1's Python arm takes a word that is in unit 32's class 'and is not in TOOL-dRankedPlan-46's SHELL_BODY_WORDS'. 46:37-38 (S2) also orders the shell test first, and 46:142 stages its new arm with 'a router that tests the interpreter class before the shell words'. Because of 47's exclusion, a router that runs the interpreter test first still rejects "$BASH", which then falls through to the shell test. The staged break cannot turn AC2 red, so S2's ordering rule is never observed by a failing run. | sound | guard-above-a-fold-makes-its-fallback-dead |
| 16 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-47.md:section 4 'The routing after this unit' paragraph, section 5 risks | medium | medium | confirmed | I re-ran the probe. ast.parse of '"$py" "$d/ratify.py" "$slug"' printed Module(body=[Expr(value=Constant(value='$py$d/ratify.py$slug'))]): the line is valid Python with no argv list. Yet 47:80-82 and its risks at :114-115 say that reading a non-Python `$` body as Python 'fails closed'. A shell body of this shape parses and passes, so that justification is false. 46 AC2's 'exits 2 on shell source' is false for its own plant body, the same line. AC2's 'or passes' clause keeps AC2 able to go red, but the text about the failure mode is wrong. | sound | - |
| 17 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-50.md:section 4 'The reading after this unit', row `with_hook_index cp "$s" "$d/ratify.py"` | medium | medium | confirmed | 50:34-38 (S1) says a wrapper call invokes ratify.py when an argument word ending in ratify.py 'follows an interpreter word of unit 32 S2's class directly'. 32:53-54 puts any `$` variable in that class. with_hook_index is a wrapper function under S2, and in `with_hook_index cp "$s" "$d/ratify.py"` the word "$d/ratify.py" directly follows "$s". S1 therefore makes it a caller, but the table at :104 says 'not a caller'. The risks line at :152-153 itself says this shape is refused. | sound | - |
| 18 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-47.md:section 4 Evidence third bullet, section 4 Alternatives rejected first bullet | low | low | confirmed | I re-ran the `$`-form git grep and it printed 30. A bare-form grep printed only gate-guard.test.sh:417, :427 and :430. All three are quoted strings passed as payload arguments to `run` (e.g. `run "AC5 ..." 0 "$B" 'python - <<EOF`), not heredocs the file runs. 47:101's 'thirty of the thirty-three Python heredocs' therefore overcounts, and the bare-form regex is not stated at :66-69. | sound | - |
| 19 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-46.md:section 4 Evidence first bullet (and TOOL-dRankedPlan-47 section 4 Evidence first bullet) | low | low | confirmed | grep on unit 45 printed S10 at 108, '### File kinds and readers' at 260, and the python and bash/sh heredoc rows at 267-268. 46:70 and 47:63 cite the table as lines 256-263, which come before the heading and miss the rows they name. The error is cosmetic. | sound | - |
| 20 | reuse | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-50.md:section 2 S2, and section 10 (also TOOL-dRankedPlan-51 section 10) | medium | medium | confirmed | In tools/lexicon/lexicon.py:747-803, parse_shell_defs calls scan_shell_tokens(src) in default mode, appends only (name, line) and returns out, [], []. Nothing in it returns a body opener or the body's tokens. 50:39-42 (S2) relies on it to find the body, and 51:165 says it 'reads the same ops to find a function's body'. In fact it finds only the opener and never the body's end. git grep found def parse_shell_defs only in lexicon.py, and there is no tracked tools/loop/extract_code.py, so the builder would re-implement the four definition forms over the seps=True stream. | sound | - |
| 21 | reuse | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-49.md:section 10, and section 2 S1/S2 | low | low | confirmed | tools/gate-lint/sh_hygiene.py:160-163 has ASSIGNMENT with the same five leader words plus `\+?=`, and an EXPANSION follower. Its :325 says a re-assignment CLEARS the name. tools/process-monitor/scope.py:38-39 has ASSIGNMENT and ASSIGNMENT_LEADERS. Unit 49 §10 cites neither and concludes that no seam fits beyond the reader. S1 (49:31-34) lists the same leaders, but does not say whether `NAME+=` counts and does not record why it keeps every assignment instead of clearing on re-assignment. This is the same missed-sibling gap that unit 52 S20/S21 repair elsewhere. The consequence is documentation and reuse only. | sound | - |
| 22 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S10 and S11, section 6 AC11 | high | high | confirmed | I looped over specs 30 to 52 and kept those where grep -q 'py.function' matched: 30, 32, 33, 34, 35, 37, 44 and 52. For each I counted 'codebase-map coverage + freshness' on the third line of grep -A2 '^## 7. Gates'. The count was 0 for all of them. symbols.json was also 0 for 30 to 37; 44 had 1 (its hands-off edge) and 52 had 5, all in prose, none in Files touched. Spec 52 line 244 says 'No item mints a function', so it is selected only by its prose. S10 reaches only units 5, 41 and 44. The hands-off edges show 30 carrying S1/S4, 34 carrying nothing to 45, and only 37 carrying S30. README rows 5 to 7 put units 30 to 35 at orders 5 to 7, and 52 §3 makes rewriting a landed spec a non-goal. So AC11 is red by construction at 52's tip. | unsound | - |
| 23 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S13 and S23, section 4 'Token kinds in separators mode' | high | high | confirmed | Spec 52 S13 (lines 121-129) splits the heredoc token into `heredoc` and `heredoc-expanded`. It says only how a body that unit 47 S1 routes to Python is read when expanded. Spec 46 S1 routes shell bodies on the heredoc token of 45 S10 (45 lines 108-111 emit one `heredoc` kind). All three of 46's plants (lines 43-49) use `<<'EOF'`, a quoted delimiter. Nothing in 52 says that a `heredoc-expanded` body with a SHELL_BODY_WORDS command word goes to read_shell_callers. Unit 38's textual rule matches only read_plan_ratification. README orders 46 at 21 and 52 at 22, so the shell router is built against the single kind. An unquoted `bash <<EOF` body that runs ratify.py is left unspecified and unplanted. | sound | - |
| 24 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S3 and S4, section 6 AC3 and AC4, and section 7 of units 46, 47, 48, 49, 50 and 51 | medium | medium | confirmed | 52 S3 and AC3 check only `loop selftest`. The §7 deferral in 46 to 51 (I read each Gates block) names only `loop selftest`. 45 S17 (lines 138-142) owes `loop selftest` and every other leg whose guard is {prefix}/loop/. dDeclaredLoop-79 S8 gives `loop breakpoints fixtures` the guard {prefix}/loop/ + memory-tree + lib. 45 S18 adds {prefix}/loop/ to `build-index selftest`. Each subject's Files touched names tools/loop/ratify.py, so S3 narrows S17. The effect is contained: check-spec-tokens' guards join (SPEC_GUARD_LEGS_CUTOFF, BROAD_LEG_FLOOR=5 at line 362) would red at the pass once those legs are in the manifest. Today grep -c '{prefix}/loop/' tools/gate-legs.json prints 0. | sound | - |
| 25 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S10, section 6 AC10 | medium | medium | confirmed | README line 190 reads '\| 12 \| `TOOL-dRankedPlan-44`, `TOOL-dRankedPlan-5` \| yes \|'. Specs 5 (line 83) and 44 (line 73) only carry S10 'into this unit's pass', and neither Files touched names symbols.json yet. BUILD-METHOD M6 (lines 209-216) decides concurrency from write lists 'written down before dispatch'. S10 asks that the --dispatch --writes list name the file, but nothing puts it in the specs' Files touched before step 12 is dispatched. So the generated row shows the two symbols.json writers as parallel at dispatch time. AC10 reads the row only at 52's tip. The hazard is real and its effect contained (a conflicting generated render). | sound | - |
| 26 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-52.md:section 2 S5, section 6 AC5 | low | low | confirmed | grep -c '{prefix}/loop/' tools/gate-legs.json prints 0, so AC5's 'at most 5' is green at base. 52's Files touched (lines 253-256) never edits tools/gate-legs.json, so nothing this unit builds can turn AC5 red. Under the probe policy, a criterion already green before the unit is built cannot fail. AC5 does not observe S5's claim that the join reds a tools/loop/ spec whose leg line omits the leg. | sound | armed-but-unreachable-rule |
| 27 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-46.md:section 2 S1 and section 3 Non-goals (with TOOL-dRankedPlan-52 S14) | high | high | confirmed | 46 §3 (lines 55-56) sends only `python -c` and here-strings to 52. 52 S14 (lines 130-134) reads `-c` words and here-strings only for command words in 47 S1's Python class. 32 S2 (lines 49-57) treats `bash` as a non-interpreter first word, and the quoted `-c` word does not end in ratify.py. 38 S1 matches only read_plan_ratification. So `bash -c '"$py" "$d/ratify.py" "$slug"'` and `bash <<< '…'` reach no reader that compares against ratify.py. Grepping the specs for `bash -c` or `sh -c` found no unit covering it. Rerunning the finder's git grep from the repo root printed 158. | sound | - |
| 28 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-49.md:section 2 S1/S2 and section 3 first bullet | high | high | confirmed | 49 S1/S2 (lines 31-40) compare a literal assignment value, quotes stripped, against ratify.py. 49 §3 excludes only a substitution 'whose text does not end in ratify.py', which implies that `g=$(resolve_kit_gate loop ratify.py)` is in scope. No rule says what such a value is, and no plant covers it. Under 52 S7 the outer word rebuilds as `g=$()`, which does not end in ratify.py. .githooks/pre-commit:199 has `if g=$(resolve_kit_gate "$pg_kit" guard.py); then` and :212 has `with_hook_index "$py" "$g" --staged`. git grep -c found resolver bindings in pre-commit (5), pre-push (4), manifest-check.sh (4) and more. | sound | - |
| 29 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-49.md:section 2 S2 | high | high | confirmed | 49.md:35-40 limits the resolution to 'Wherever unit 32 S2 compares a word with ratify.py' and to 'Both invocation forms of unit 32 S2'. 32.md:52-55 defines exactly those two forms. 50.md:34-37 adds a separate wrapper-call test ('one of its argument words ends in ratify.py and either follows an interpreter word ... directly, or is the first argument word ...'), and 49 never names it. 50 is order 9 and 49 is order 21, so a builder of 49 who reads S2 literally leaves the wrapper test unresolved. That builder would let `with_hook_index "$py" "$r" "$slug"` and `timeout 60 "$py" "$r" "$slug"` through. .githooks/pre-commit:11 defines with_hook_index with "$@", and :212 reads `elif ! with_hook_index "$py" "$g" --staged; then`, which is a bound script word behind the wrapper. The tree already writes this shape. It is a narrow fail-open path in a deny-by-default ban. | sound | - |
| 30 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-50.md:section 2 S1 | high | high | confirmed | 50.md:34-37 accepts the ratify.py word only when it follows an interpreter word directly, or when it is the first argument that is neither a dash word nor a duration. Take `timeout 60 "$py" -B "$d/ratify.py" "$slug"`. The script word follows `-B`, so the first arm fails. In the second arm `60` is a duration, so the first qualifying argument is `"$py"`, and that arm fails too. The call passes the ban. 32.md:54-55 skips `-` words after the interpreter, and the wrapper rule drops that skip. Re-running the finder's git grep printed 27, e.g. tools/policy/adopt-policy.sh:87 `"$PY" -B "$HERE/check_policy.py"`. The interpreter-option shape is the tree's habit. | sound | - |
| 31 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-48.md:section 2 S3 and section 3 Non-goals | high | high | confirmed | 48.md:43-45 says an element names ratify.py only through its `str` tokens, and §3 (48.md:50-52) lists only template literals as unread. A const bound by path.join() reaches the array as a `word` token, so it never matches. No spec in the set gives a JS bound-name rule: grep for 'bound name/path.join' found only 45 and 49, which are Python and shell. The tree's JS hooks pass scripts in exactly this way: tools/policy/policy-mirror.js:48 `const SHIM = path.join(__dirname, "policy-shim.sh")` with :85 `spawnSync(bash, [SHIM, ...args]`, and tools/unattended/stop-guard.js:108 `const driver = path.join(kitDir, 'unattended.sh')` with :111 `spawnSync('bash', [driver, '--liveness', slug]`. The ban would certify an absence over the shape the next JS caller copies, and no word records that the shape is unread. No tracked JS invokes a kit Python script at base, so the path is narrow. | sound | - |
| 32 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-46.md:section 2 S1 ('read ... as a file of its own') | high | high | confirmed | 46.md:35-36 reads a shell-fed body 'as a file of its own'. 49.md:31-33 collects bindings 'in the file', so the outer `r="$d/ratify.py"` never reaches the body. 52.md:121-126 S13 gives the heredoc-expanded line rule only for a body 'TOOL-dRankedPlan-47 S1 routes to Python', so a shell body has no textual ratify.py rule. The 38 name rule matches only the predicate's name. Re-running `scan_shell_tokens('bash <<EOF\n"$py" "$r" "$slug"\nEOF\n')` printed `[('word', 'bash', 1)]`, which shows the body is consumed as a separate unit. With an unquoted delimiter, or an exported variable, the real run invokes ratify.py and the ban passes it. This is a narrow fail-open path. | sound | - |
| 33 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-46.md:section 7 New arm line | medium | low | confirmed | 46.md:142 stages the arm with 'a router that tests the interpreter class before the shell words'. 32.md:53-54's interpreter class holds python, python3, py and `$` variables, not `bash`. Under that break, AC1's `bash <<'EOF'` body (46.md:43-44) fails the interpreter test, still reaches SHELL_BODY_WORDS, and is still refused. AC3 stays admitted. Only AC2's "$BASH" moves. So the staged break never reproduces the defect 46 exists for, a bash body that never reaches the shell reader. TEMPLATE-SPEC.md:283-285 says `covers` lists the criteria the arm re-observes, and BUILD-METHOD records the arm red, not each AC, so the claim that 'the pass records AC1 as seen red' is overstated. AC1 itself would still fail on a build missing the shell arm. What remains is a weaker red-first observation with no effect on behaviour. | sound | - |
| 34 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-51.md:section 2 S1 and section 4 'The reading after this unit' | medium | medium | confirmed | 51.md:31-34 makes every `(`/`)` op end a command, and the spec says nothing about array assignments or `((`. Re-running the probe printed `('word','cmd=',1) ('op','(',1) ('word','"$py"',1) ('word','"$d/ratify.py"',1) ('word','"$slug"',1) ('op',')',1) ('word','"${cmd[@]}"',2) ('word','--exit',2)`. The array value therefore becomes a command that invokes ratify.py with no mode flag, and the `--exit` call site is refused falsely. `if ((n > 0))` yields ops plus the words `n 0`, a junk command. tools/lib/lib-selftest.sh:152-154 shows the `local -a cmd=(...)` / `"${cmd[@]}"` idiom. Both cases fail closed, so the effect is contained. | unsound | - |
