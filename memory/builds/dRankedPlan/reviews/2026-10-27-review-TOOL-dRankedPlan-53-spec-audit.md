**Serves:** spec-audit TOOL-dRankedPlan-59@rev-1 TOOL-dRankedPlan-55@rev-1 TOOL-dRankedPlan-57@rev-1 TOOL-dRankedPlan-58@rev-1 TOOL-dRankedPlan-60@rev-1 TOOL-dRankedPlan-53@rev-1 TOOL-dRankedPlan-54@rev-1 TOOL-dRankedPlan-56@rev-1 TOOL-dRankedPlan-61@rev-1 TOOL-dRankedPlan-62@rev-1

# Tier-2 spec audit — dRankedPlan, the round-5 audit promotions, units 53 to 62 (round 1)

Provenance: a Tier-2 adversarial review of the ten specs that the fifth spec audit promoted. The finders were gov-spec-reviewer on five lenses, the skeptic batches were gov-skeptic, and the synthesis was gov-synthesizer. The build's purpose is taken from memory/builds/dRankedPlan/README.md and its run mandate.

Reviewed: memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-59.md@f3043cb70bdd69c509285e948e8ed0aa9b2f8af0, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-55.md@cc7c9222b1f6d7e9b31c09471bed3320cc33ea90, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-57.md@101791dff9f8689adfd21f8c89cd4c6fb94553ee, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-58.md@e516e6924e2da785ce34b781d5265011e1879c21, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-60.md@fab25b04c81f2af69537852332d9a8c7a820776c, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-53.md@3c0fee4b57d83b1a1d1857879d889f4e443dd602, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-54.md@dee981292de3ed67634778bd91786ea4a47fb37d, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-56.md@87df6d041a41f180a79349c76e528819209af255, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-61.md@e133c32729da02989f9cea2b130ca30d8ad7626b, memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md@6272e21a6bfe59eea0d0a998f6f27e2311c0831f

ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers. Four high findings stand, grouped into three items. The skeptic judged every high fix sound. The specs should not go to build until items H1 to H3 are folded in. Each of the three high items lets a hook or JS caller invoke `ratify.py` and still pass the deny-by-default always-run ban. Four medium items (M1 to M4) are criteria in unit 62 that are red by construction or green before the build, so each needs its check rewritten before unit 62 can close honestly.

## Review shape

Review shape: intensity full, raw 37, confirmed 34, refuted 3, unverified 0 (0 uncertain), precision 0.92.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 14 | 13 | 1 | 0 | 0 | 0.93 |
| grounding | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 5 | 3 | 2 | 0 | 0 | 0.60 |
| failure-envelope | yes | 9 | 9 | 0 | 0 | 0 | 1.00 |

By item, the adjudicated tally is 25 items: 0 blocker, 3 high, 14 medium and 8 low.

By raw confirmed finding, the tally is 34: 0 blocker, 4 high, 20 medium and 10 low.

Three defects are split across items because their findings carry different binding grades, and findings are merged only within one grade. Each pair should be fixed by one edit.

- Unit 56's double-quoted `-c` carrier is H2 (id 29, high) and M9 (id 12, medium). I would grade id 12 high as well, since it is the same fail-open, but its binding grade is medium.
- Unit 60's binding extent and declarator lists are H1 (ids 21 and 32, high) and M11 (id 33, medium). Id 21 also names the declarator-list case; the fix in H1 covers both.
- Unit 61's AC1 selector comma is M13 (id 36, medium) and L2 (id 6, low).

### Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Demotions: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified.
- Discards: 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 32 judged sound, 2 judged UNSOUND (ids 26 and 34; the skeptic's corrected fixes are written below), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic (id 5 from medium to low).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 51 spec documents were supplied as `specs`, as sibling context.
- Checklist: 14 items, each assigned to exactly one of 5 lenses (coherence 3, grounding 3, reuse 3, blast-radius 3, failure-envelope 2).
- By design: none supplied, with no caller byDesign and a block of 0.
- Move check: no checked subject moved.

Every count above is clean, so the run is complete on its own terms.

## High

### H1 — Unit 60's JS binding ends on the declaration's first line (ids 21, 32)

- **Where:** TOOL-dRankedPlan-60 §2 S1 (binding extent), §10.
- **What:** S1 ends a binding at the first depth-0 `;` or at "the last token on the declaration's line at depth 0", whichever comes first. It writes this rule by hand instead of reusing `read_ts_expr_end` (tools/lexicon/lexicon.py:1587), the ASI-aware expression-end reader that `parse_ts_source` already calls (:1824) and that TOOL-dTotalRecall-13 S1 moves into the loop kit's `extract_code` block. §10 never names it.
- **Consequence:** `const s = path.join(\n  kit, "ratify.py");` followed by `spawnSync(py, [s, slug])` binds `s` to `path join (`. The `"ratify.py"` str sits on line 2 and is never in the binding, so the JS caller passes the ban. This is ordinary prettier output, and tracked .js files already hold multi-line declarations.
- **Fix (skeptic judged it SOUND):** Restate S1 so the binding runs from the token after `=` to `read_ts_expr_end(toks, k)` from the loop kit's `extract_code.py`. That reader ends at a depth-0 `;` or `,`, at an unbalanced closer or at an ASI line break. A declarator `,` followed by `word =` starts a new binding. Cite `read_ts_expr_end` in §10 as the reused seam. Add plant `caller-js-bound-multiline` (the two-line `path.join` with `[s, slug]`), refused, with an AC, and a declarator-list plant, refused.
- **Left-shift gate:** A reuse-audit step that greps tools/lexicon/ for an existing expression-end or extent reader before a spec writes its own extent rule in prose.

### H2 — A double-quoted `-c` carrier with escaped inner quotes passes the line rule (id 29)

- **Where:** TOOL-dRankedPlan-56 §2 S1, §4 'The reading after this unit' row 3.
- **What:** S1 sends a non-single-quoted carrier to unit 52 S13's line rule (a word ending in `ratify.py`, quotes stripped). `bash -c "\"$py\" \"$d/ratify.py\" \"$slug\""` arrives as one raw word with its escapes kept. Splitting and stripping quotes leaves `\$d/ratify.py\`, which ends in a backslash. §4 row 3 answers 'caller' for this exact form, but AC1 to AC3 plant only single-quoted carriers.
- **Consequence:** A hook written this common way calls the predicate's CLI and passes the ban. A builder who follows S1 and 52 S13 to the letter ships the hole and nothing goes red.
- **Fix (skeptic judged it SOUND):** In S1, say a non-single-quoted carrier is unquoted the way the shell does it: remove the outer double quotes, turn `\"` and `\\` into their characters, then split into words and apply the line rule. Add plant `caller-shell-c-dq` with the §4 row 3 line, refused with exit 1, and an AC observing it. Its staged break is a line rule that strips quotes and leaves backslashes.
- **Left-shift gate:** A spec-audit check that every §4 design-table row answering 'caller' names the plant or AC that observes it.

### H3 — An expanded heredoc body fed to a non-shell, non-Python command is read by nothing (id 31)

- **Where:** TOOL-dRankedPlan-53 §2 S1 and §4; TOOL-dRankedPlan-54 §4 'The router after this unit'.
- **What:** 53 S1 justifies the line rule because the outer shell expands the body before bash reads it. That expansion runs `$(…)` and backticks in an unquoted body whatever the command word is. Units 53 and 54 route an expanded body only for shell and Python command words. Units 46 and 47 map 'any other word' to TOOL-dRankedPlan-38's textual rule, which matches only `read_plan_ratification`.
- **Consequence:** `cat <<EOF` with body `$("$py" "$d/ratify.py" "$slug")` runs ratify.py during expansion and passes the ban. The router table has only `bash` and `"$py"` columns, so a builder covers exactly those.
- **Fix (skeptic judged it SOUND):** Add an item: a `heredoc-expanded` body whose command word is in neither class has every `$(…)` and backtick span read by `read_shell_callers` as nested commands, with the line rule applied beside them. Add the router row 'any other command word, heredoc-expanded'. Add plant `caller-heredoc-cat-subst`, refused, and its twin with `<<'EOF'`, admitted, since a quoted body is data.
- **Left-shift gate:** A bug-class checklist entry: every router table over a token kind carries an 'any other command word' row for each kind, stated against what the shell executes.

## Medium

### M1 — AC2's single-line grep cannot match the wrapped deferral sentence (ids 1, 15, 24)

- **Where:** TOOL-dRankedPlan-62 §6 AC2, with §2 S6 and the §7 deferral of units 53 to 60.
- **What:** AC2 needs `grep -c "is owed once dDeclaredLoop's loop legs are in the manifest"` to print 1 over every spec AC1 lists. Units 53 to 60 carry S6's long form wrapped after `dDeclaredLoop's`, so the grep prints 0 on each. Unit 62 passes only because its S6 holds the phrase on one line; its own §7 is wrapped.
- **Consequence:** AC2 is red at unit 62's tip on 8 correct specs, and on up to 7 more once units 46 to 52 adopt the wrapped form. §3 rules out rewriting units 53 to 60, so the check either blocks the close or gets waived, and a waived check certifies nothing.
- **Fix (skeptic judged it SOUND):** Match across line breaks, e.g. `tr '\n' ' ' < spec | grep -c "is owed once dDeclaredLoop's loop legs are in the manifest"`, or grep a token that never wraps, such as `owed once dDeclaredLoop` or `--legs-for tools/loop/ratify.py`. Re-run over the 23 specs AC1 lists and pin each spec's output.
- **Left-shift gate:** A spec-token check that refuses an AC grep pattern containing a space unless it joins lines first or the pattern is shown matching every spec in its population at authoring time.

### M2 — AC6 runs over units 38 to 45, which S6 never reaches (ids 2, 16, 25)

- **Where:** TOOL-dRankedPlan-62 §6 AC6, with §2 S6, §6 AC1 and §1.
- **What:** AC6 needs `loop breakpoints fixtures` in every spec AC1 lists (38 to 62, 42 aside). S6 sends the reworded deferral only to units 46 to 52, and units 38 to 41 and 43 to 45 hold no hands-off edge to unit 62.
- **Consequence:** AC6 is red on 7 specs whatever is built, so it decides nothing about units 46 to 52. Units 38 to 45 also keep the `loop selftest`-only deferral S6 calls the defect, so they will under-declare `loop breakpoints fixtures` once dDeclaredLoop adds its legs (guard `{prefix}/loop/`, TOOL-dDeclaredLoop-79 S8).
- **Fix (skeptic judged it SOUND):** Pick one. (a) Narrow AC6's population to units 46 to 62 and state in §3 that units 38 to 45 are out of scope. (b) Widen S6's carry list to units 38 to 45, add each a hands-off edge to unit 62 and record it in §1, accepting that this rewrites earlier specs, which §3 currently rules out.
- **Left-shift gate:** A spec-token check that a criterion run over carried specs has a population no wider than the item's carry list plus the unit itself.

### M3 — AC24 is already green for unit 46 because its citation wraps (ids 3, 17)

- **Where:** TOOL-dRankedPlan-62 §6 AC24, with §2 S22.
- **What:** AC24 greps `lines 256-263` and wants 0. Unit 46 writes the citation as `(lines` / `256-263)` across lines 74 and 75, so the grep prints 0 today with the stale citation still present. It works for unit 47 only.
- **Consequence:** If unit 46's builder never carries S22, AC24 still reports green.
- **Fix (skeptic judged it SOUND):** Grep the bare range `256-263`, which wraps nowhere, or join lines first. Pin today's output, 1 for each of units 46 and 47, as the red state.
- **Left-shift gate:** The same check as M1: a multi-word grep pattern must join lines or be proven against its population.

### M4 — AC19 checks its own sed, not unit 52's AC10 (id 4)

- **Where:** TOOL-dRankedPlan-62 §6 AC19, with §2 S17.
- **What:** AC19 types its own region-limited sed over the README, which prints one row today. Unit 52's AC10 (spec-52.md:313) still reads the two-table `grep -n '^| 12 |'`, which prints the roster row and the build-order row, and `grep -c 'gen:build-order'` over spec-52 prints 0.
- **Consequence:** AC19 is green before S17 is carried and stays green if it never is, so unit 52's AC10 keeps reading roster row 12 beside the order row.
- **Fix (skeptic judged it SOUND):** Observe the carried text, e.g. `grep -c 'gen:build-order' <unit 52 spec>` within AC10's line range, or `grep -A1 '^- \*\*AC10' <unit 52 spec> | grep -c 'sed -n'` printing at least 1. Pin today's 0 as the red state.
- **Left-shift gate:** A spec-audit rule: a criterion that verifies a carry greps the carried spec, and its red state is pinned at base.

### M5 — Unit 62's New arm line claims AC10, AC13 and AC14 that no staged break reddens (id 7)

- **Where:** TOOL-dRankedPlan-62 §7 New arm line (spec-62.md:378).
- **What:** The arm claims AC8 AC9 AC10 AC13 AC14 AC16 AC17 AC18 AC25 and names three staged breaks: bound words compared unresolved, a `$`-fed body kept to one reader, array words dropped. None touches AC10's plant (direct-script arm and duration grammar), AC13's (the `spans` next-line wrapper) or AC14's (`/bin/bash` and `${BASH}` normalization). This repeats the defect S19 corrects in unit 46.
- **Consequence:** Three criteria are recorded as red-proven and never are, so a regression in those paths, or a plant that passes vacuously, goes unseen.
- **Fix (skeptic judged it SOUND):** Add staged breaks that redden each: a direct-script arm with no duration skip (AC10), a body read from `parse_shell_defs` without `spans` (AC13), and a `SHELL_BODY_WORDS` test with no last-segment or `${name}` normalization (AC14). Or drop AC10, AC13 and AC14 from `covers`.
- **Left-shift gate:** An arm check that runs each named staged break and refuses a `covers` id that stays green under every break.

### M6 — Unit 53's staged break leaves AC1 and AC2 green (id 8)

- **Where:** TOOL-dRankedPlan-53 §7 New arm line, §6 AC1/AC2, §2 S1.
- **What:** The break routes every `heredoc-expanded` body to unit 52 S13's textual rules. The plant body `"$py" "$d/ratify.py" "$slug"` already matches S13's line rule, so AC1 stays refused and AC2's `--exit` variant stays admitted.
- **Consequence:** The arm is never seen red. A build that skips the shell reader for expanded bodies, the core of S1, passes both criteria.
- **Fix (skeptic judged it SOUND):** Add a plant only the shell reader refuses, e.g. a body that splits `ratify.py` across a backslash-newline inside double quotes (hidden from the line rule, not from the shell reader), and restate the break so it reddens that plant. Otherwise drop the claim that S1 reads with the shell reader.
- **Left-shift gate:** The same arm check as M5.

### M7 — Unit 54's router table narrows a `"$py"`-fed body to the Python reader alone (id 10)

- **Where:** TOOL-dRankedPlan-54 §4 'The router after this unit' (lines ~79-83).
- **What:** The table sends a `heredoc` body with command word `"$py"` to `read_python_callers` alone. Unit 62 S15, carried by units 46 and 47, says a body fed to any `$` variable outside `SHELL_BODY_WORDS` (`bash`, `sh`, `$BASH`) gets both readers, and only a literal `python`, `python3` or `py` keeps one.
- **Consequence:** Unit 54's builder at order 23 can follow this table and reopen the fail-open where a shell body fed to `$tool` parses as Python and passes. AC1 and AC2 use only `bash`, so nothing notices.
- **Fix (skeptic judged it SOUND):** Give the `"$py"` column the S15 reading (both readers), or add a column for a literal `python`. State what an expanded `$`-variable body gets. Add a `$`-variable spelling to `heredoc-kinds-routed`.
- **Left-shift gate:** A bug-class checklist entry (two answers to one question): a design table that restates a sibling unit's routing must cite the item it restates, and a spec-audit diff checks the two agree.

### M8 — Nothing passes the enclosing file's bindings to the line rule at Python-fed and non-single-quoted sites (ids 11, 35)

- **Where:** TOOL-dRankedPlan-58 §2 S1 and §4 row 4; TOOL-dRankedPlan-55 §3; TOOL-dRankedPlan-56 §2 S1.
- **What:** 58 §4 row 4 says an expanded Python-fed body line `"$r" "$slug"`, with `r` bound in the enclosing file, is a caller through 52 S13 and `resolve_ratify_word(word, bindings)`. No spec names the `bindings` passed at the line-rule site. 55 S1 inherits bindings only for bodies `read_shell_callers` reads, and 55 §3 excludes Python-fed bodies. 56 S1 grants them only to single-quoted carriers. Unit 58's plants cover only the wrapper site.
- **Consequence:** A builder passes empty bindings there, `$r` resolves to nothing, and the call passes. The design table promises the opposite and the next builder will trust it.
- **Fix (skeptic judged it SOUND):** Add to 58 S1 that every call site passes the enclosing file's bindings (unit 49 S1), including the line rule over a Python-fed expanded body and over a non-single-quoted carrier. Amend 55 §3 to match. Add a plant for row 4 (`r="$d/ratify.py"`, `python3 - <<EOF` with body `"$r" "$slug"`), refused, with an AC. Or change row 4 to 'unread' and record it as the ceiling.
- **Left-shift gate:** The same check as H2: every design-table row answering 'caller' names its observing plant.

### M9 — Unit 56's §4 row 3 answers 'caller' where S1's rule answers 'not a caller' (id 12)

- **Where:** TOOL-dRankedPlan-56 §4 'The reading after this unit' row 3, with §2 S1.
- **What:** This is the design-table half of H2. Row 3 says `bash -c "\"$py\" \"$d/ratify.py\""` is a caller by the line rule, but stripping quotes from the escaped word leaves a trailing backslash. No AC observes the row. I would grade it high with H2; its binding grade is medium.
- **Consequence:** The common double-quoted carrier passes the ban while the table says it is refused.
- **Fix (skeptic judged it SOUND):** The H2 fix: state that the line rule unescapes `\"` and `\\` in a double-quoted carrier before splitting and stripping, and add plant `caller-shell-c-dq` with an AC expecting exit 1.
- **Left-shift gate:** As H2.

### M10 — Unit 56 S1 misses `-c` inside a clustered option word (id 30)

- **Where:** TOOL-dRankedPlan-56 §2 S1 ('The word after a `-c` option word').
- **What:** The tokenizer emits `bash -ec '…'` as `bash`, `-ec` and the span. S1 names only a `-c` word, so `-ec`, `-lc` and `-xc` are never read as shell source.
- **Consequence:** `bash -ec '"$py" "$d/ratify.py" "$slug"'` passes the ban. The tree writes none of these forms at base, which keeps the effect contained.
- **Fix (skeptic judged it SOUND):** In S1, the carrier follows any option word that starts with a single `-` and contains `c` among its letters, as bash reads an option cluster. Add plant `caller-shell-ec`, refused, with an AC.
- **Left-shift gate:** A bug-class checklist entry: an option a spec names is matched as bash parses it, including clusters.

### M11 — Unit 60 S1 does not collect later declarators or destructuring (id 33)

- **Where:** TOOL-dRankedPlan-60 §2 S1 (declaration shape), §3.
- **What:** S1 collects only `const|let|var NAME =`. In `const a = 1, s = path.join(kit, "ratify.py");`, only `a` is declared and its binding swallows the str. §3 and the §4 table do not name declaration lists or destructuring as ceilings. Id 21 in H1 names the declarator case too.
- **Consequence:** `[s, slug]` is unread and passes, failing open on an uncommon JS shape.
- **Fix (skeptic judged it SOUND):** Have S1 split a declaration at depth-0 `,` ops into declarators, each `NAME =` starting its own binding (H1's `read_ts_expr_end` already ends at the `,`). Name destructuring as unread in §3 and the §4 table. Add plant `caller-js-bound-multi-decl`, refused.
- **Left-shift gate:** As H1.

### M12 — Unit 57 S1 binds a `$(…)` substitution but not a backtick one (id 34)

- **Where:** TOOL-dRankedPlan-57 §2 S1; TOOL-dRankedPlan-52 S7.
- **What:** 57 S1 binds only the nested span of a `$(…)` in a value 52 S7 rebuilds, and 52 S7 rebuilds pieces only around `$(`. Unit 41 S1 gives a backtick span its own op, so `g=`resolve_kit_gate loop ratify.py`` reads as `g=` followed by an op and names nothing. 57 §3 does not name backticks as a ceiling.
- **Consequence:** `if g=`resolve_kit_gate loop ratify.py`; then "$py" "$g" "$slug"; fi` passes the ban.
- **Fix (skeptic judged the finder's fix UNSOUND; the corrected fix follows):** Extend TOOL-dRankedPlan-52 S7's piece rule to a word that a backtick span interrupts: the text before the opening backtick op and after the closing one are `piece` tokens, rebuilt with `$()` standing for the span. Then have 57 S1 say each command substitution, `$(…)` or a backtick span, stands for its nested span's words. Add plant `caller-shell-bound-resolver-backtick`, refused, with an AC.
- **Left-shift gate:** A bug-class checklist entry: any rule over `$(…)` states the backtick spelling in the same sentence.

### M13 — Unit 61's AC1 selector requires a comma S1 does not state (id 36)

- **Where:** TOOL-dRankedPlan-61 §2 S1/S2, §6 AC1 selector.
- **What:** S1 selects a Kind cell that begins `function` or `functions`. AC1's awk needs `/^ *functions?,/`. Kind cells this build already writes, a bare 'function' (units 7, 9), 'functions' (13, 16) and 'function in `plan_fields.py`' (11, 12), are missed. Every cell in 30 to 62 happens to use the comma form, so the gap is latent.
- **Consequence:** A later function-minting unit written in one of those forms drops out of AC1's population, and AC2 never checks its symbols.json render or legs.
- **Fix (skeptic judged it SOUND):** Make the selector match the rule, e.g. `$3 ~ /^ *(Python |shell )?functions?([ ,]|$)/`, or narrow S1's wording to the comma form and say so. Add a red case: a scratch spec copy whose Kind cell reads 'function in X' must be selected.
- **Left-shift gate:** A spec-audit rule that a selector typed in an AC is run against a fixture of every phrasing its prose rule admits.

### M14 — Unit 62 S12's `close` index is wrong inside a `case` and unspecified for an unclosed body (id 37)

- **Where:** TOOL-dRankedPlan-62 §2 S12 (spans=True close index, lines 111-122).
- **What:** S12 defines `close` as the op that closes the body at the same depth in the default stream. In `w() ( case $1 in a) "$@";; esac )`, the case pattern's `)` is the first one at that depth. S12 also gives no answer for a body with no closing op; `scan_shell_tokens('w() { echo x; ')` neither closes nor raises.
- **Consequence:** The body unit 50 S2 reads omits `"$@"`, `w` is not a wrapper, and the call passes. For an unclosed body a builder may raise IndexError or return a partial span instead of the kit's exit-2 refusal.
- **Fix (skeptic judged it SOUND):** In S12, skip a `case … esac` span when matching parentheses, and make a body with no closing op raise `SyntaxError` naming the line from `parse_shell_defs(spans=True)`, as its refusal 1 does for untokenizable files. Add AC12 probe cases for both.
- **Left-shift gate:** A bug-class checklist entry: every span or close-index rule states its malformed-input answer and its nested-construct exclusions.

## Low

### L1 — AC3 passes when the selector finds nothing (id 5)

- **Where:** TOOL-dRankedPlan-62 §6 AC3, §2 S3.
- **What:** AC3 passes when unit 61's selector prints nothing over unit 52's spec, and it already does today. A selector that selects nothing for every spec passes too. The skeptic re-graded this from medium to low because unit 61's AC1 pins a non-empty list that serves as a positive control elsewhere.
- **Consequence:** AC3 has never been seen red and cannot tell a correct selector from an empty one.
- **Fix (skeptic judged it SOUND):** Pair the empty result with a positive control in the same command: the selector over unit 58's spec must print 58 (it does today), over unit 52's nothing. Describe the staged break, a selector replaced by `grep -l py.function`, and show it reddens AC3.
- **Left-shift gate:** A bug-class checklist entry (fixture passes by finding nothing): every empty-result criterion carries a positive control.

### L2 — Unit 61's AC1 is green before the unit is built (id 6)

- **Where:** TOOL-dRankedPlan-61 §6 AC1, §2 S1.
- **What:** The selector is static text and the unit builds nothing, so AC1 prints the pinned `30 32 33 34 35 37 44 58` today. Its comma requirement is the same divergence as M13.
- **Consequence:** AC1 cannot fail on this unit's work.
- **Fix (skeptic judged it SOUND):** Let AC2 carry the acceptance and label AC1 a derivation, not a criterion. Fix the comma as in M13: `/^ *functions?([ ,]|$)/`, or write the comma into S1.
- **Left-shift gate:** A spec-token check that refuses a criterion whose red state is not pinned at base.

### L3 — Several S-item record corrections in unit 62 have no observing criterion (id 13)

- **Where:** TOOL-dRankedPlan-62 §2 S12, S15, S16, S23 against §6.
- **What:** No grep observes S12's §10 sentences in units 50 and 51, S15's supersession of unit 47's 'That fails closed' sentence, its §5 risks line or unit 46's AC2 Red-when, S16's two §4 rows in unit 51, or S23's Alternatives-rejected sentence in unit 49. §5 risks still claims "the greps of §6 observe it".
- **Consequence:** A builder can skip these record edits and leave the superseded sentences as a second answer, with no criterion going red.
- **Fix (skeptic judged it SOUND):** Add one grep per carried sentence, as AC11, AC15 and AC22 to AC26 do, e.g. `grep -c 'That fails closed'` over unit 47 printing 0, `grep -c 'spans'` over §10 of units 50 and 51 printing at least 1, and `grep -cF '((n > 0))'` over unit 51 printing at least 1.
- **Left-shift gate:** A spec-token check that every S-item naming a carry into another spec is cited by at least one AC.

### L4 — Unit 62's pinned `--legs-for tools/loop/ratify.py` output is false (ids 14, 18, 26)

- **Where:** TOOL-dRankedPlan-62 §4 Evidence, bullet M1/M3 (spec-62:206-208); the same derivation in §7 of units 53 to 60 and 62.
- **What:** The evidence pins that the command "printed only legs marked `broad`". At base it prints `legs-for: REFUSING — no path given is tracked at HEAD: tools/loop/ratify.py` and exits 2, because tools/loop/ is not tracked.
- **Consequence:** Anyone re-running it gets a refusal, and S4's and S18's scratch clones and the AC4 and AC20 fixtures refuse in any tree where ratify.py is untracked. By order 24 earlier units will have created tools/loop, so behaviour is unaffected.
- **Fix (ids 14 and 18 judged SOUND; for id 26 the skeptic judged the finder's fix UNSOUND and gave the correction used here):** Re-pin the evidence as the refusal it prints, with exit 2, because tools/loop/ratify.py is untracked until unit 9 lands. State that the deferral's `--legs-for` derivation is answerable only after that, and that the S4 and S18 clones and the AC4 and AC20 fixtures must be taken at a revision where tools/loop/ratify.py is tracked at HEAD. Do not substitute tools/lexicon/lexicon.py as a baseline: it prints non-broad legs.
- **Left-shift gate:** A spec-audit step that re-runs every PINNED evidence command and diffs its output.

### L5 — Scratch clones are placed under cmd.exe's `%TEMP%` (id 19)

- **Where:** TOOL-dRankedPlan-62 §6 AC4 (spec-62:289) and AC20 (:343) fixture lines.
- **What:** `%TEMP%` is not expanded in Git Bash, so a transcribed clone creates a directory literally named `%TEMP%` in the worktree.
- **Consequence:** A dirtied tree that tree-wide scans can pick up. Contained.
- **Fix (skeptic judged it SOUND):** Name the location in bash form: the session scratch directory spelled absolute, or `$(mktemp -d)` under it.
- **Left-shift gate:** A spec-token check that refuses `%NAME%` variables in spec command text.

### L6 — Sibling-spec line citations are one line early (id 20)

- **Where:** TOOL-dRankedPlan-56 §4 Evidence first bullet; the same in 53, 54, 55 and 58 §4 Evidence and 59 §4 Evidence first bullet.
- **What:** 52 S13 is at 122-130, not 121-129; 52 S14 at 131-138, not 130-137; 46 §3 at 56-57; 46 S1 at 31-37; 49 S1 at 32-35; 49 S2 at 36-41; 50 S1 at 32-39.
- **Consequence:** Cosmetic. The quoted text is correct.
- **Fix (skeptic judged it SOUND):** Cite each sibling by its S-item or heading, as S22 prescribes for units 46 and 47, or correct the ranges.
- **Left-shift gate:** A spec-token check that refuses a line-number citation into another spec under memory/builds/.

### L7 — Unit 61's AC2 re-checks two legs the guards join already enforces (id 22)

- **Where:** TOOL-dRankedPlan-61 §2 S1, §6 AC2 and its leg-line reader, §10.
- **What:** AC2 checks `recall floor` and `recall floor arms` for any Files touched naming `memory/map/generated/symbols.json`, which `tools/check-spec-tokens.py`'s guards join (`derive_tripped_legs`, `check_guard_trips`) already enforces past the 2026-09-22 cutoff. Its awk reads §7 by ordinal, which the `extract_gates` docstring rejects.
- **Consequence:** Two checkers of one fact can drift, and the ordinal read breaks on a light-profile spec. Latent.
- **Fix (skeptic judged it SOUND):** Narrow AC2 to the leg the guards join cannot derive, `codebase-map coverage + freshness`, and the Files touched line. Cite the spec-tokens leg's guards join for the other two. Read §7 through `extract_gates` and Files touched through `design_lib.read_spec_writes`, and name both in §10.
- **Left-shift gate:** A reuse-audit step that greps tools/check-spec-tokens.py for an existing join before an AC re-derives a leg obligation.

### L8 — Unit 62's AC1 population re-reads Files touched with raw awk (id 23)

- **Where:** TOOL-dRankedPlan-62 §6 AC1 population command (spec-62:363-364), §10.
- **What:** The command greps every line under `### Files touched`, prose included, for `tools/loop/`. `design_lib.read_spec_writes` (design_lib.py:528-540) is the declared single reader of that sub-head and reads backticked words only. §10 does not name it.
- **Consequence:** A prose mention would enter AC1's population while the guards join reads that spec as declaring nothing. Today they agree.
- **Fix (skeptic judged it SOUND):** Derive the population from `design_lib.read_spec_writes(text)`, selecting a spec when any returned word starts with `tools/loop/`, e.g. a one-line `python -c` importing tools/memory-tree/design_lib.py. Name `read_spec_writes` in §10.
- **Left-shift gate:** A gate-lint rule that flags an AC awk range over `### Files touched` and points at `read_spec_writes`.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=37 confirmed=34 refuted=3 unverified=0 blocker=0 high=4 medium=20 low=10 agents=11 out-tokens=186140

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC2 (with section 2 S6) | medium | medium | confirmed | I ran AC2's single-line grep over the 23 specs AC1 lists. It printed 1 for 38-52 and 62, and 0 for each of 53-60. spec-53.md lines 126-127 (cat -A) break the phrase after "dDeclaredLoop's", and the next line starts "loop legs are in the manifest" with no indent. S6 says units 53-62 are "written in that form" and carries no edit into them. So AC2 is red at unit 62's tip on a correct build. Unit 62 passes only because its S6 holds the phrase on one line; its own §7 is wrapped. | sound | - |
| 2 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC6 (with section 2 S6 and section 6 AC1) | medium | medium | confirmed | grep -c 'loop breakpoints fixtures' printed 0 for 38-52 and 1 for 53-60. S6 sends the new wording only to units 46-52. grep -l for the hands-off edge to TOOL-dRankedPlan-62 matched 46-52, 58, 59 and 61, and none of 38-45. AC6 still runs over every spec AC1 lists, and that list includes 38-41 and 43-45. Those seven specs print 0 permanently, so AC6 is red on a correct build. | sound | - |
| 3 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC24 (with section 2 S22) | medium | medium | confirmed | spec-46.md lines 74-75 read "(lines" then "256-263)". grep -c 'lines 256-263' printed 0 for 46 and 1 for 47, while grep -c '256-263' printed 1 for each. For unit 46, AC24 is green today with the line citation still present, so it cannot observe S22 there. The bare range appears once in each spec, which makes the proposed grep's red state 1 and its fixed state 0. | sound | - |
| 4 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC19 (with section 2 S17) | medium | medium | confirmed | AC19 types its own sed over the README. Today that sed piped to grep '^\| 12 \|' printed exactly one row, the order-12 build-order row. grep -n '^\| 12 \|' printed two rows, :71 (roster) and :205 (order). Unit 52's AC10 at spec-52.md:313 still uses grep -n '^\| 12 \|', and grep -c 'gen:build-order' over spec-52 printed 0. AC19 is therefore green before S17 is carried and cannot detect that it never is. | sound | - |
| 5 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC3 (section 2 S3) | medium | low | confirmed | Unit 61's selector over spec-52 printed nothing, and grep -c 'py.function' over spec-52 is at least 1, so AC3 is green at base. A selector that selects nothing for every spec would pass AC3 as well. The consequence is contained: unit 61's AC1 pins a non-empty list (30 32 33 34 35 37 44 58), and that list acts as a positive control elsewhere. I therefore grade it low rather than medium. The proposed positive control holds today: the selector over spec-58 printed 58. | sound | fixture-passes-by-finding-nothing |
| 6 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-61.md:section 6 AC1 (with section 2 S1) | low | low | confirmed | I ran §6's selector over specs 30-62. It printed '30 32 33 34 35 37 44 58', which equals AC1's pinned figure at c22908a6d, so AC1 is green before the unit is built. The regex /^ *functions?,/ requires a comma that S1's wording ("begins `function` or `functions`") does not state. Every Kind cell that matches today has a comma, so no spec is missed now. The divergence is latent only, hence low. | sound | - |
| 7 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 7 New arm line | medium | medium | confirmed | spec-62.md line 378 says the arm covers AC8 AC9 AC10 AC13 AC14 AC16 AC17 AC18 AC25, and names three staged breaks: bound words compared unresolved, a `$`-fed body kept to one reader, and array words dropped. None of these touches the plants behind AC10, AC13 or AC14. AC10's plant is a literal `timeout -k 5s 60 "$d/ratify.py"` that exercises the direct-script arm and the duration grammar. AC13's is the spans next-line wrapper. AC14's are the `/bin/bash` and `${BASH}` command-word normalizations. This spec's own S19 and AC21 require an arm line not to claim a criterion its break leaves green, and this line does exactly that. The arm still runs these plants. The defect is that they are never red-proven, so a plant that passes vacuously would go unseen. | sound | - |
| 8 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-53.md:section 7 New arm line, section 6 AC1/AC2 (section 2 S1) | medium | medium | confirmed | Unit 52 S13's line rule (spec-52.md lines 120-124) marks as a caller any line holding a word that ends in ratify.py after quotes are stripped, unless the line holds a mode flag. The plant body `"$py" "$d/ratify.py" "$slug"` (spec-53.md S2) matches that rule. Under the staged break on line 131, AC1 is still refused with exit 1 and AC2's `--exit` variant is still admitted, so both stay green. S1 also applies the line rule to shell-fed bodies and refuses a body when any of its readers refuses. These plants therefore cannot show that the shell-reader half of S1 is present. A plant that splits `ratify.py` across a backslash-newline inside double quotes would hide it from the line rule but not from a shell reader, so the proposed fix can be built. | sound | - |
| 9 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-54.md:section 1 / section 4 Rollout (ordering against TOOL-dRankedPlan-52 AC13) | medium | medium | refuted | Premise false on re-probe. spec-52.md:122-130 (S13) itself says that when a body TOOL-dRankedPlan-47 S1 routes to Python is `heredoc-expanded`, it is read by the textual rules (the name rule and the ratify.py line rule). So unit 52's own scope tells the Python path to take the new kind, and AC13 (`caller-heredoc-unquoted` exits 1) can be met at unit 52's pass without unit 54. Unit 54 S1 then explicitly supersedes whatever selection rule 52 built and replaces it with membership in `HEREDOC_KINDS`. That is a planned repair one order up, not a backwards dependency. README build order shows 52 at step 22 and 54 at step 23, which is consistent with this. | unsound | - |
| 10 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-54.md:section 4 "The router after this unit" table | medium | medium | confirmed | spec-54.md's router table (lines ~79-83) maps `heredoc` with command word `"$py"` to `read_python_callers` alone. spec-62.md S15 (lines 132-141) says a body fed to a `$` variable outside `SHELL_BODY_WORDS` is read by both readers, and only a literal python/python3/py keeps the Python reader alone. spec-46.md:31 sets SHELL_BODY_WORDS = ("bash","sh","$BASH"), so `"$py"` is such a `$` variable. Unit 54 S1 defers routing to units 46/47 S1, but its design table gives a second, narrower answer that the order-23 router builder can follow. AC1 and AC2 use only `bash`, so they would not catch it. | sound | two-answers-to-one-question |
| 11 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-58.md:section 4 "The reading after this unit" row 4 | medium | medium | confirmed | spec-58.md row 4 claims that an expanded Python-fed body line `"$r" "$slug"` with the enclosing `r` is a caller via S13 and resolve_ratify_word. resolve_ratify_word(word, bindings) resolves only through the `bindings` passed to it. spec-55.md §3 explicitly excludes Python-fed bodies from the inherited enclosing bindings, and S1 inherits only for bodies that unit 46 S1 hands to read_shell_callers. No spec passes the enclosing file's bindings to the S13 textual rule for a Python-fed body. AC1 and AC2 in spec-58 plant only the wrapper call. So the row is unbacked, and as built `$r` resolves against nothing and fails open. | sound | - |
| 12 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-56.md:section 4 "The reading after this unit" row 3 (with section 2 S1) | medium | medium | confirmed | I re-probed with lexicon.scan_shell_tokens on `bash -c "\"$py\" \"$d/ratify.py\""`, and the -c word comes back raw: `"\"$py\" \"$d/ratify.py\""`, escapes kept. The S13 line rule (spec-52.md:125-126: a word ending in ratify.py, quotes stripped) says nothing about unescaping. Splitting on whitespace and stripping quotes leaves a word ending in a backslash, either `\$d/ratify.py\` or `\"$d/ratify.py\`, so the word does not end in ratify.py. Even so, spec-56.md row 3 answers "caller", and §6 has no plant for the double-quoted form. The design promises a refusal that the stated rule does not deliver. | sound | - |
| 13 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 2 S12, S15, S16, S23 against section 6 | low | low | confirmed | In spec-62 §6, AC12, AC13, AC16, AC17, AC18 and AC25 observe plants or the probe. AC26 greps the S23 §10 citation but not its Alternatives-rejected sentence. No grep observes S12's §10 sentences in units 50/51, S15's supersession of unit 47's 'That fails closed' sentence, its §5 risks line or unit 46's AC2 Red-when, or S16's two §4 rows in unit 51. Yet §5 risks says 'S1 to S7 and S11 to S23 depend on units 46 to 52 carrying their items; the greps of §6 observe it.' The gap affects only record text, so it is low. | sound | - |
| 14 | coherence | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 4 Evidence, M1/M3 bullet | low | low | confirmed | I ran `python -B tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`. It printed `legs-for: REFUSING — no path given is tracked at HEAD: tools/loop/ratify.py; ...` with exit=2, and `git ls-files tools/loop` printed nothing. spec-62.md §4 Evidence M1/M3 pins instead that it 'printed only legs marked `broad`'. The pinned evidence is false. The practical effect is small, because by order 24 earlier units will have created tools/loop, so I grade it low. | sound | - |
| 15 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC2 (with section 2 S6 and the section 7 deferral of units 53 to 60) | medium | medium | confirmed | I re-ran the AC2 grep over AC1's list. It prints 1 for 38-41, 43-52 and 62, and 0 for 53, 54, 55, 56, 57, 58, 59 and 60. The phrase wraps after "dDeclaredLoop's" in those specs (e.g. spec-54 §7, spec-58 §7). AC2's precondition holds today (gate-legs.json has no 'loop selftest'), so AC2 is red by construction on 8 specs. Once units 46-52 adopt S6's wrapped form, those can go red too. | sound | ledger-token-wrapped-across-a-line-joins-nothing |
| 16 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC6 against section 2 S6 | medium | medium | confirmed | `grep -c 'loop breakpoints fixtures'` printed 0 for 38-41 and 43-52, and at least 1 for 53-60 and 62. S6 (spec-62.md:85-91) has only units 46 to 52 carry the new form. `grep -c TOOL-dRankedPlan-62` printed 0 for 38-45, so those units have no hands-off edge and no carry. AC6 runs over AC1's list, which includes 38-45, so it can never go green for those 7 specs. | sound | - |
| 17 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC24 | medium | medium | confirmed | Re-ran `grep -c 'lines 256-263'`: it printed 0 for spec-46 and 1 for spec-47. Spec-46:74-75 wraps the text as `(lines` / `256-263) route by`. AC24 (spec-62:352) wants 0 from each spec, so for unit 46 it is already green before anything is built. It cannot see whether S22 was carried. | sound | ledger-token-wrapped-across-a-line-joins-nothing |
| 18 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 4 Evidence, first bullet (M1, M3); the same derivation in section 7 of units 53 to 60 and 62 | low | low | confirmed | Spec-62:206-208 says `--legs-for tools/loop/ratify.py` 'printed only legs marked `broad`. The outputs are PINNED.' Re-running it printed `legs-for: REFUSING — no path given is tracked at HEAD: tools/loop/ratify.py ...` with rc=2, and `ls tools/loop` reported no such directory. The pinned output is false. | sound | - |
| 19 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC4 and AC20 fixture lines | low | low | confirmed | Spec-62:289 reads 'a scratch clone under `%TEMP%`' and :343 reads 'the two scratch clones under `%TEMP%`'. That is cmd.exe syntax. In the Git Bash shell the build runs in, `%TEMP%` is not expanded, so a builder who copies it literally creates a directory named `%TEMP%` relative to wherever the clone runs. Contained effect. | sound | - |
| 20 | grounding | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-56.md:section 4 Evidence, first bullet (and the same in 53, 54, 55 and 58 section 4 Evidence, and 59 section 4 Evidence first bullet) | low | low | confirmed | Re-grepped the cited specs. In spec-52, S13 starts at line 122 and S14 at 131 (cited as 121 and 130). In spec-46, S1 starts at 31 (cited 30). In spec-49, S1 is at 32 and S2 at 36 (cited 31 and 35). In spec-50, S1 is at 32 (cited 31). The citations in specs 53, 54, 55, 56, 58 and 59 are each one line early. The quoted text is correct, so the effect is cosmetic. | sound | - |
| 21 | reuse | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-60.md:section 2 S1; section 10 | high | high | confirmed | Spec-60 S1 (lines 29-33) ends a binding at the first depth-0 `;` or 'the last token on the declaration's line at depth 0'. Take `const s = path.join(` followed by args on later lines: the last depth-0 token on that line is `(`, so the `"ratify.py"` str is never in the binding. S2 then lets `[s, slug]` through, and the deny-by-default ban fails open. A declarator list is not covered either. §10 (lines 147-154) does not name `read_ts_expr_end` (lexicon.py:1587). My probe of it returned 9 (`spawnSync`, line 4) for the multi-line form, so it spans lines 1 to 3, and 4 (`,`) for the declarator list. parse_ts_source calls it (:1824), and TOOL-dTotalRecall-13 S1 moves parse_ts_source and the TS helpers verbatim into the extract_code block. So the seam already exists. | sound | - |
| 22 | reuse | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-61.md:section 2 S1; section 6 AC2 and its leg-line reader; section 10 | low | low | confirmed | Spec-61 AC2 (lines 116-129) re-checks `recall floor` and `recall floor arms` with an awk reader keyed on `^## 7\. Gates`, which includes the ordinal that the `extract_gates` docstring warns against. Running `--legs-for memory/map/generated/symbols.json` printed both legs with no broad mark, and `.memory-tree.conf:356` sets the cutoff at 2026-09-22. So the guards join already enforces these two legs for these specs. AC2 is a second checker of the same fact, and its ordinal read is latent fragility. | sound | - |
| 23 | reuse | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC1 population command; section 10 | low | low | confirmed | Spec-62:363-364's population command builds the list by grepping every line under `### Files touched` for `tools/loop/`, prose included. `design_lib.read_spec_writes` (design_lib.py:528-540) reads backticked words only, and §10 does not name it. A prose mention would therefore enter AC1's population while the guards join reads that spec as declaring nothing. Today the two agree, so the defect is latent. | sound | - |
| 24 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC2 (with section 2 S6) | medium | medium | confirmed | Re-ran AC2's grep `is owed once dDeclaredLoop's loop legs are in the manifest`: it printed 0 for each of specs 53 to 60 and 1 for 62. Spec-53:125-127 carries the deferral wrapped across lines, as "is owed once dDeclaredLoop's" / 'loop legs are in the manifest'. AC2 is therefore red on 8 specs that carry the deferral correctly. | sound | amendment-leaves-its-other-half-standing |
| 25 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 6 AC6 (with section 2 S6 and section 1) | medium | medium | confirmed | I re-ran AC1's population command. It printed `38 39 40 41 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 62`. Running `grep -c 'loop breakpoints fixtures'` over each of those specs printed 0 for 38 to 52 and at least 1 for 53 to 60 and 62. Grepping for a `hands-off** \`TOOL-dRankedPlan-62\`` edge matched 46 to 52, 58, 59 and 61, and none of 38 to 45. S6 (spec-62 line 85-91) carries the form only to units 46 to 52, while AC6 runs over every spec AC1 lists. So AC6 is red by construction on units 38, 39, 40, 41, 43, 44 and 45, and nothing routes the correction to them. | sound | amendment-leaves-its-other-half-standing |
| 26 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 4 Evidence, bullet M1, M3 | low | low | confirmed | I re-ran `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`. It printed `legs-for: REFUSING — no path given is tracked at HEAD: tools/loop/ratify.py ...` and exited 2. `git ls-tree -r --name-only` over tools/loop printed nothing at HEAD and nothing at 0689e7fa. The PINNED claim in §4 Evidence (M1, M3), that the command "printed only legs marked `broad`", is therefore false. The fix's alternative is unsound: I ran `--legs-for tools/lexicon/lexicon.py` and it printed non-broad legs (`codebase-map kit selftest <- tools/lexicon/`, `lexicon selftest <- tools/lexicon/`), so it cannot serve as a broad-only baseline. | unsound | - |
| 27 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-56.md:section 2 S1, section 6 and section 7 (same omission in 53, 54, 55, 57, 59, 60, 62) | medium | - | refuted | The premise is false on re-probe. TOOL-dRankedPlan-45 S9 says a shell file is tokenized only when its text names `ratify.py` or `read_plan_ratification`. Running `git grep -lE 'ratify\.py\|read_plan_ratification' -- '*.sh' '.githooks/*'` matched no file, so tools/check-playbook-parity.test.sh is never tokenized and its lines 300, 304 and 314 cannot exit 2. Those lines are also arguments to `arm`, not commands whose command word is in SHELL_BODY_WORDS. The leg named in TOOL-dRankedPlan-31 S1 has no guard and runs on every bar, including each unit's own bar. A reading change that broke the tree would therefore red that unit's own bar before it lands, so the claimed every-commit breakage cannot slip through. | sound | - |
| 28 | blast-radius | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-61.md:section 2 S1 and S2 (selector), section 6 AC1 | medium | - | refuted | The premise is false on re-probe. Reading tools/gate-legs.json shows `codebase-map coverage + freshness` with guard None, so it runs on every bar, the unit's own bar included. A pass that leaves symbols.json stale reds there and cannot slip past to a later commit. The gotcha the finder cites concerns the guarded naming leg skipped on a branch bar, not the freshness leg. TEMPLATE-SPEC line 152 also requires `### Inventory` to name every identifier the unit will MINT. An undeclared public helper is therefore a builder's deviation from the template, not a gap in unit 61's selector. | sound | naming-leg-grades-what-python-named |
| 29 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-56.md:section 2 S1 and section 4 'The reading after this unit' row 3 | high | high | confirmed | I re-ran scan_shell_tokens on the §4 row-3 form. The carrier came back as one word, `"\"$py\" \"$d/ratify.py\""`. Splitting it and stripping `"` and `'` gave `['\\$py\\', '\\$d/ratify.py\\']`, so no word ends in `ratify.py`. Unit 52 S13's line rule ("a word ending in ratify.py, quotes stripped"), which 56 S1 applies to non-single-quoted carriers, therefore misses the form. Yet 56 §4 row 3 answers 'caller', and AC1 to AC3 plant only single-quoted carriers. | sound | - |
| 30 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-56.md:section 2 S1 ('The word after a `-c` option word') | medium | medium | confirmed | I re-ran scan_shell_tokens on `bash -ec '"$py" "$d/ratify.py" "$slug"'`. It printed the words `bash`, `-ec` and the single-quoted span. 56 S1 says only "The word after a `-c` option word" and says nothing of option clusters, so a literal reading misses `-ec`, `-lc` and `-xc`, and no plant observes them. The tree writes none of these forms at base, which keeps the effect contained. | sound | - |
| 31 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-53.md:section 2 S1 and section 4; also TOOL-dRankedPlan-54 section 4 'The router after this unit' | high | high | confirmed | I read the router tables. 46 §4 line 88 and 47 §4 line 81 map 'any other word' to TOOL-dRankedPlan-38's textual rule only, and that rule matches `read_plan_ratification` alone. 54's router table has only the columns `bash` and `"$py"`, and 53 S1 adds the line rule only for SHELL_BODY_WORDS. An unquoted `cat <<EOF` body holding `$("$py" "$d/ratify.py" "$slug")` is expanded, and so run, by the outer shell, yet no stated reader refuses it. The deny-by-default ban passes it. | sound | - |
| 32 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-60.md:section 2 S1 (binding extent) | high | high | confirmed | I re-ran scan_ts_tokens on `const s = path.join(\n  kit, "ratify.py");`. Line 1 ends at the `(` op, and `"ratify.py"` sits on line 2 at depth 1. 60 S1 ends the binding at 'the last token on the declaration's line at depth 0', so the binding stops on line 1 and holds no str token ending in ratify.py. The JS caller then passes. I also ran `git grep` for declarations ending in `(`, `,` or `[`, and it found multi-line declarations in tracked .js files. | sound | - |
| 33 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-60.md:section 2 S1 (declaration shape) and section 3 | medium | medium | confirmed | 60 S1 (lines 29-33) collects only `const\|let\|var` + one name + `=`, with the binding running to the first depth-0 `;`. §3 (lines 47-50) and the §4 table name re-assignment, members, other modules, template literals and block scoping as unread, but not declaration lists or destructuring. Re-probe: scan_ts_tokens('const a = 1, s = path.join(kit, "ratify.py");', strs=True) printed word const, word a, op =, word 1, op ',', word s, op =, ... op ';'. Under S1 only `a` is declared, and its binding swallows the ratify.py str. `s` is never collected, so S2 never resolves `[s, slug]` and it passes. That fails open, against the ban's deny-by-default intent. The effect is contained to an uncommon JS declaration shape. | sound | - |
| 34 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-57.md:section 2 S1 | medium | medium | confirmed | 57 S1 binds only the nested span of a `$()` in a value rebuilt by 52 S7, and grep over the spec dir shows 52 S7 rebuilds pieces only around `$(`/`$)`. 41 S1 (line 42) gives a backtick span its own op with a tokenized body, and nothing in 57 or 52 binds that body to the assignment. Re-probe: in default mode, scan_shell_tokens on the backtick form printed one word 'g=`resolve_kit_gate loop ratify.py`', which does not end in ratify.py. In seps mode the value is `g=` followed by a backtick op, so it names nothing. 57 §3 does not name backticks as a ceiling, so `if g=`...ratify.py`; then "$py" "$g" "$slug"; fi` passes the ban. | unsound | - |
| 35 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-58.md:section 2 S1 and section 4 table row 4; also TOOL-dRankedPlan-55 section 3 and TOOL-dRankedPlan-56 section 2 S1 | medium | medium | confirmed | 58 S1 defines resolve_ratify_word(word, bindings) and routes 52 S13's line rule through it, but no spec names the bindings passed at that site. 55 S1 gives inherited bindings only to bodies read_shell_callers reads, and 55 §3 excludes the Python-fed body ('read textually'). 56 S1 grants 55's bindings only to a single-quoted carrier and sends other quoting to the S13 line rule. 52 S13 (lines 122-130) never mentions bindings. Yet 58 §4 row 4 answers 'caller' for an expanded Python-fed body line `"$r" "$slug"`. Unit 58's two plants (S2, AC1, AC2) cover only the wrapper site, so nothing observes row 4. A builder passing empty bindings there ships a fail-open path. | sound | - |
| 36 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-61.md:section 2 S1/S2 and section 6 AC1 selector | medium | medium | confirmed | 61 S1 selects a Kind cell that 'begins `function` or `functions`'. The AC1 selector requires `/^ *functions?,/`, so it misses a bare 'function' or 'function in X', both of which S1 selects. Re-probe: the selector at HEAD printed '30 32 33 34 35 37 44 58'. Listing Kind cells across units 1-62 showed bare 'function' (units 7, 9), 'functions' (13, 16) and 'function in `plan_fields.py`' (11, 12), all of which S1 covers and the selector misses. Every cell in 30-62 happens to use the comma form, so the mismatch stays latent. AC1 is told to be re-derived by the same selector, so a later unit writing one of these forms is silently dropped and AC2 never checks it. The fix's wider regex is coherent, since map_extractors.py renders shell functions too. | sound | - |
| 37 | failure-envelope | memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-62.md:section 2 S12 (spans=True close index) | medium | medium | confirmed | 62 S12 (lines 111-122) defines `close` as 'the op that closes it at the same depth' in the default scan_shell_tokens stream. It says nothing about case patterns or an unclosed body. Re-probe: scan_shell_tokens('w() ( case $1 in a) "$@";; esac )') printed op '(' ... word a, op ')', word '"$@"', word esac, op ')'. The first `)` at the body's depth is the case pattern's, so the body read by unit 50 S2 omits `"$@"`, `w` is not a wrapper, and the call passes. scan_shell_tokens('w() { echo x; ') printed no closing op and did not raise, so spans=True has no specified answer for an unclosed body. AC12 probes only the well-formed next-line brace case. | sound | - |
