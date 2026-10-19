**Serves:** diff-review TOOL-dRenderedAnchor-1 TOOL-dRenderedAnchor-2

# Closing diff review, round 2: dRenderedAnchor unit 2, the round-1 fixes, the marker predicate and the /build Skill's citation pass

2026-10-19 · Tier-2 · on `branch/frosty-feistel-42acd4` · adversarial fan through `tier2-review.js`: 5 finder lenses, then 5 skeptic batches, then this synthesis. This round reads the FIX for the 8 round-1 findings (record `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-1-closing-diff-round1.md`), all promoted as batch unit TOOL-dRenderedAnchor-2 and built at 54344d9a7. The fix also carries an owner-added gap: the rendered /build Skill's harness citations now go through `roles_lib.resolve_cited_paths` and the kit resolver, where before they used plain `{{TOOL_ROOT}}` substitution.

**Reviewed range:** `033b15f240f740fdd3df219d94f8fc42bcaf7420...c66a3663d7ed06a92cca8dc32bc81c17fa54dfec`. **ROUND 2.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker or a high. No finding reopens a round-1 defect. The marker predicate, the guard-term rows, the derive_kit_paths section and the wording fixes all stand. Two medium defects need fixing before the close.

- The new citation pass in `adopt-roles.sh` resolves every `{{TOOL_ROOT}}` citation, not just the harnesses. That lets the /build Skill name an adopter's repo-root `run-gates/run-gates.sh` as the merge bar.
- Arm 14 gets its population from the regex it guards, so if that regex narrows, a harness drops out of the arm silently.

The other items are latent defects, gate gaps and documentation.

## Review shape

Intensity **full** · raw **13** · confirmed **13** · refuted **0** · unverified **0** (0 uncertain) · precision **1.00**.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| intent | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: **9 items**, 0 blocker, 0 high, 2 medium, 7 low. By raw confirmed finding: 0 blocker, 0 high, 2 medium (ids 1, 10), 11 low.

I merged findings in two places, and each merge joins findings of one binding grade.

- Ids 2, 4, 6 and 11 are one defect: help/roles.md's list of note printers leaves out check_roles.py.
- Ids 7 and 12 are one defect: no gate covers the new remedy tail of check-wiring's absent-harness note.

One grade changed. The skeptic re-graded id 5 from medium to low, and the low grade binds.

**Run integrity.**

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Verdict handling: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 10 judged sound, 3 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-diff-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: 3 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 12 items, each assigned to exactly one of 5 lenses (security 3, correctness 3, seams 2, verification 2, intent 2).
- By design: the caller's byDesign.

The run is complete, so a zero count here is evidence.

## Medium

### M1. The citation pass resolves every `{{TOOL_ROOT}}` citation, so the /build Skill can name a file outside the kits as the merge bar (id 1)

**Where:** `tools/roles/adopt-roles.sh:176`, with `roles_lib.resolve_cited_paths`.

**What is wrong:** The pass calls `resolve_cited_paths(text, kit.parent, root)`, which makes `here` the tool root. resolve_kit_dir's second probe, `here.parent/<home>/<file>`, therefore looks at `<repo>/<home>/<file>`, outside the tool root. Spec 2 §4 C6 resolves every citation, not just the harnesses. So the merge-bar citation `{{TOOL_ROOT}}run-gates/run-gates.sh` (SKILL.template.md:84) and the `unattended/unattended.sh` citation (:12) now go through that probe as well. derive_kit_paths passes the kit dir as `here` and so gives a different answer for the same citation.

**Consequence:** The roles kit does not require run-gates (kit.toml:12). Take an install at prefix `tools/` with no `tools/run-gates/` and an adopter's own `run-gates/run-gates.sh` at the repo root. Its /build Skill tells the orchestrator to run that adopter file as the merge bar, while BUILD-METHOD falls through to `tools/run-gates/run-gates.sh`. A scratch fixture reproduced this. Arm 14 checks only harness citations, so no gate sees it. The path is narrow, and before this change the citation already named a dead path there, so the effect is contained.

**Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Limit the citation pass to the (home, file) pairs that workflows.toml lists as workflow-driver harnesses. Read those pairs from the catalogue, never typed. Leave every other `{{TOOL_ROOT}}` citation to plain substitution. Keep `here` as the tool root, so harness citations still agree with `resolve_harness_path`. Add an arm-14 row with a repo-root `run-gates/run-gates.sh` and no `tools/run-gates`, and assert that the Skill still names `tools/run-gates/run-gates.sh`.

**Left-shift gate:** Add an adopt-roles.test.sh row: for every non-harness `{{TOOL_ROOT}}` citation in the template, plant a decoy at the repo root and assert the rendered Skill carries the plain-prefix path.

### M2. Arm 14 reads its population through the regex it guards (id 10)

**Where:** `tools/roles/adopt-roles.test.sh:524`, with the floor at :548.

**What is wrong:** Arm 14 picks which harnesses to plant and assert by running the subject's own `roles_lib.TOOL_ROOT_CITE_RE` over SKILL.template.md. It skips matches that are not in the workflow table (:527). Its only floor is `[ "$_i" -ge 2 ]`, which a single pair satisfies. This breaks the charter's [class] rule, because the guard shares state with what it guards.

**Consequence:** Narrow the regex to `[A-Za-z.-]+` and the tier2-review.js cite matches only `workflows/tier`, so that pair drops out of the arm. `resolve_cited_paths` uses the same regex and stops resolving that cite, and plain substitution writes `tools/workflows/tier2-review.js` into the Skill. Arm 14 stays green and still claims that "each cited harness" is named under the renamed directory. The spec says the arm reads homes and names "from the template, never typed". In practice it reads them through the regex under test. The effect is a weaker gate, not a wrong shipped result.

**Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Take the population from the workflow table alone: every driver=workflow harness that HARNESS_RE matches and whose literal `{{TOOL_ROOT}}<home>/<name>` appears in the template text. Plant and assert each one. Require the planted count to equal that literally cited count, and also to be at least 2, the number of workflow harnesses the template cites, so the population can never be empty. Staged break: narrow `TOOL_ROOT_CITE_RE` to `[A-Za-z.-]+` and observe RED.

**Left-shift gate:** Add a bug-class checklist entry: a test's population must never be enumerated through the code under test. Pair it with a floor equal to the independently derived count.

## Low

### L1. help/roles.md leaves the catalogue checker out of the tools that print the missing-harness note (ids 2, 4, 6, 11)

**Where:** `help/roles.md:136-137`.

**What is wrong:** The new text lists the note printers as `render_agents.py` and check-wiring's session-start report. It leaves out `check_roles.py`, which also prints `roles: note: %s harness %s is not held by this tree` (check_roles.py:293-296) under the `roles catalogue` leg (tools/gate-legs.json:1709). `tools/roles/README.md:285` and kit.toml:19 name all three readers. The base text said only "each tool prints a note", so this diff introduced the incomplete list.

**Consequence:** The help page and the kit README give two different answers to one question. An adopter who sees the catalogue leg's note finds no tool on the help page that explains it. Behaviour is unaffected.

**Fix (the skeptic judged it SOUND):** Name all three readers, as the README does: the catalogue checker (`check_roles.py`), `render_agents.py` and check-wiring's session-start report. Keep the next sentence, which says render_agents.py is the one that prints `misplaced`. An optional extra: have check_roles.py's note point at `adopt-roles.sh --check`, as check-wiring's note now does.

**Left-shift gate:** Add a bug-class checklist entry, two-answers-to-one-question: any enumeration added to help/ must be cross-read against the kit README's enumeration of the same fact.

### L2. No gate covers the new remedy tail of check-wiring's absent-harness note (ids 7, 12)

**Where:** `tools/check-wiring.sh:1746`, asserted only at `tools/check-wiring.test.sh:2173`.

**What is wrong:** The note now ends `bash $kit/adopt-roles.sh --check says whether its kit holds it elsewhere`. The only runtime assertion matches the unchanged prefix `^note     roles     — nowhere/absent-harness.js is named by the role index`. AC9 greps the source for `adopt-roles.sh --check`, and the comment at :1689 satisfies that grep by itself.

**Consequence:** Revert the tail to its 033b15f2 text, or let `$kit` come out empty (`bash /adopt-roles.sh --check`), and every gate stays green. The round-1 L3 fix could regress with no red. Only a diagnostic note's remedy text is at stake, not a verdict.

**Fix (the skeptic judged it SOUND):** Beside :2173, assert the whole remedy on the note line, for example `grep -F "${KP}$RL/adopt-roles.sh --check says whether its kit holds it elsewhere"`, as the UNWIRED arms do for `--scaffold`. Observe RED with the tail dropped from the echo, or with line 1746 restored to its 033b15f2 text.

**Left-shift gate:** Add a bug-class checklist entry, line-claim-matched-over-the-whole-output: an acceptance check on a printed line must match the printed line, never a grep of the source.

### L3. The citation pass substitutes as an unanchored substring, so a shorter held citation corrupts a longer one (id 3)

**Where:** `tools/roles/adopt-roles.sh:186-187`.

**What is wrong:** Each held cite is applied with `${out//"$kp"/"$kv"}`. A held `{{TOOL_ROOT}}w/t.js` also rewrites the front of `{{TOOL_ROOT}}w/t.json`. A probe printed `a x&y/k/t.js b x&y/k/t.json`. `resolve_cited_paths` returns cites in first-seen order, so the longer citation gets the shorter one's resolved directory whenever the shorter comes first. The probe also showed that a quoted `&` in a path is safe.

**Consequence:** The defect is latent. Today's template citations (SKILL.template.md lines 12, 45, 76, 84) contain no prefix pair, but a template edit would trigger it. render-doc.sh:46-48 has the same loop shape, and this diff adds a new instance of it.

**Fix (the skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Substitute each held cite only where the next character is not one of `[\w.-]`. One way is to have the python call render the cited text itself with `re.sub(r'\{\{TOOL_ROOT\}\}([\w.-]+)/([\w.-]+)(?![\w.-])', …)`. Another is to have `resolve_cited_paths` emit every cite it sees, mapping an unheld one to its plain-prefix path, and apply the lines longest-first. Add an adopt-roles.test.sh row that cites both `h/t.js` and `h/t.json`, holds only t.js, and asserts that t.json keeps the plain prefix.

**Left-shift gate:** Add that row to adopt-roles.test.sh. Also add a checklist entry: bash `${var//pat/rep}` over citation text must be boundary-anchored.

### L4. Section 2e claims to gate both escape terms but reaches only the `..` term (id 5)

**Where:** `tools/lib/resolve-python.test.sh:335`, with row 5 at :348.

**What is wrong:** The comment says "rows 5 and 6 hold the escape and existence tests". Row 5 (`../out/w.js`) passes `root in hit.parents`, because `absolute()` does not collapse `..`, and is rejected only by `".." not in hit.parts`. No row reaches the `root in hit.parents` term. With that term deleted from a copy of the canonical, 2e printed exactly its expected answers.

**Consequence:** The section's comment claims more coverage than it gates. Without that term, a receipt row with an absolute `path` would be followed out of the tree. The term is still present and correct in every copy, so no wrong result ships. The finder graded this medium, and the skeptic re-graded it low for that reason.

**Fix (the skeptic judged it SOUND):** Add a seventh row: a `rendered` row from home h whose `path` is an absolute path to an existing file outside `$RK`, with LookupError expected. Raise the row-count check to 7. Observe RED on a staged copy of the canonical with `root in hit.parents` removed. If no row is added, narrow the comment to say row 5 holds only the `..` term, and list absolute-path escape under WHAT THIS DOES NOT CHECK.

**Left-shift gate:** Add a bug-class checklist entry, fixture-passes-by-finding-nothing: each guard term needs one row that only that term rejects, observed RED with the term removed.

### L5. Arm 14's positive check is a bare substring, so a wrong path that contains the right one passes (id 8)

**Where:** `tools/roles/adopt-roles.test.sh:344`, with the check at :543.

**What is wrong:** The arm asserts `grep -qF -- tools/renamed/<name>`. An absolute or extra-prefixed path passes. So does `tools/renamed/tier2-review.js/tier2-review.js`, which a receipt branch returning `hit` in place of `hit.parent` would produce. The `--check` half re-renders through the same code and agrees with whatever `--scaffold` wrote. The ledger records AC13's absolute-path red half as "not staged". The skeptic noted that dropping `.relative_to` everywhere would be caught by gov's `roles render wiring` leg. A regression only in the receipt branch would not be.

**Consequence:** The arm proves "contains the renamed path", not "names it repo-relative where the template cites it". Only test strength is affected.

**Fix (the skeptic judged it SOUND):** Anchor the oracle to the cited form. The template backticks each harness citation (lines 45 and 76), so grep -F for ``"`${_a14[$_i]}`"``. Stage a break in a copy of `roles_lib.resolve_cited_paths` that drops `.relative_to(...)` and observe the arm RED.

**Left-shift gate:** Add a checklist entry: path oracles in render tests match the delimited cited form, never a bare substring.

### L6. No arm reaches resolve_cited_paths' exclusion of a held path outside the repo (id 9)

**Where:** `tools/roles/roles_lib.py:605`, the `ValueError` in the except, and the "citation pass failed" exit 2 in `tools/roles/adopt-roles.sh`.

**What is wrong:** At a root install, with the kit at `<repo>/roles` and TOOL_ROOT empty, resolve_kit_dir's second probe is `<repo>/../<home>`. A sibling `<home>/<anchor>` beside the repo makes `relative_to` raise ValueError. Today the code excludes that path correctly. No adopter-suite arm and no resolve-python.test.sh section builds this layout.

**Consequence:** If `ValueError` were dropped from the except, every `--scaffold` and `--check` at such an install would exit 2, and no gate would go red. The branch is currently correct and only ungated.

**Fix (the skeptic judged it SOUND):** Add a row to adopt-roles.test.sh, or a section beside 2f. Use a TMP_ROOT fixture with `repo/.git`, `repo/roles` and a sibling `workflows/tier2-review.js`, and call `roles_lib.resolve_cited_paths` over it. Assert that it returns no line and that the Skill keeps the plain citation. Stage `except LookupError` alone and observe RED.

**Left-shift gate:** That fixture row, run under the adopt-roles leg.

### L7. The help text and docstring say a file beside neither mark "is your own", which the predicate cannot establish for a harness shipped without a template (id 13)

**Where:** `help/roles.md:142-143`, and the `tools/roles/render_agents.py` docstring at lines 39-40.

**What is wrong:** Both new sentences say a listed-name file beside neither mark is the adopter's namesake. `scan_misplaced_harnesses` (render_agents.py:182-199) counts a hit beside `<stem>.template<suffix>` or beside a kit.toml whose `home` matches. `unattended-unit.js` is a listed harness, and tools/workflows/ ships no `unattended-unit.template.js`, so kit.toml is its only mark.

**Consequence:** Take a copy-install that pruned kit.toml in a renamed directory, a case spec 2's C2 names as real. There, the kit's own `unattended-unit.js` prints the note, and the docs tell the adopter the file is theirs. The outcome is a note that exits 0, so this is wording only.

**Fix (the skeptic judged it SOUND):** Make the wording match what the scan establishes: a file beside neither mark "is not counted as the kit's and reads as the note". Alternatively, add that a harness shipped without a template (`unattended-unit.js`) is marked only by its kit's kit.toml.

**Left-shift gate:** Add a checklist entry: docs describing a predicate's outcome must state what it counts, not an inference about ownership. Cross-read them against the shipped predicate at review.

review-shape kind=diff-review round=2 intensity=full at=synth raw=13 confirmed=13 refuted=0 unverified=0 blocker=0 high=0 medium=2 low=11 agents=11 out-tokens=173887

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/roles/adopt-roles.sh:176 | medium | medium | confirmed | Reproduced in a scratch fixture with .git, an empty tools/roles, and repo-root run-gates/run-gates.sh and workflows/tier2-review.js. roles_lib.resolve_cited_paths(SKILL.template.md, root/'tools', root) returned both the workflows/tier2-review.js and the run-gates/run-gates.sh repo-root paths. adopt-roles.sh:176 passes kit.parent (the tool root) as `here`, so resolve_kit_dir's second probe (here.parent/<home>) lands at the repo root. render-doc.sh's derive_kit_paths passes the kit dir instead (`resolve_kit_dir(home, anchor, kit)`), so it gives a different answer for the same citation. For harness citations this matches the role index, because resolve_harness_path(tool_root, …) has done the same since the base. Spec 2 §4 C6 chose to resolve every citation, though, so the merge-bar citation `{{TOOL_ROOT}}run-gates/run-gates.sh` (SKILL.template.md:84) and the unattended.sh citation (:12) now go through the repo-root probe too. That is new in this diff. Before it, plain substitution named tools/run-gates/run-gates.sh. The roles kit does not require run-gates (kit.toml:12 requires only kickoff-manifest and memory-tree), so an install without run-gates that has an adopter's own run-gates/run-gates.sh at the repo root is reachable. In that case the Skill names that adopter file as the merge bar. Arm 14 checks only the harness citations. The path is narrow, and before this change the citation already pointed at a dead path, so the effect is contained: medium. | unsound | - |
| 2 | security | help/roles.md:136 | low | low | confirmed | help/roles.md:136-137 (new in this diff) lists the note printers as `render_agents.py, and check-wiring's session-start report`. check_roles.py:294-296 also appends `roles: note: … harness … is not held by this tree` when resolve_harness_path reports the harness unheld. tools/roles/README.md:285-286 and kit.toml:19 name all three readers (the catalogue checker, the agent render and check-wiring). The help page is therefore incomplete and disagrees with the README. Documentation only. | sound | fold-text-is-unreviewed-surface |
| 3 | correctness | tools/roles/adopt-roles.sh:186 | low | low | confirmed | adopt-roles.sh:186-187 applies each held cite with an unanchored `${out//"$kp"/"$kv"}`. Re-ran the probe: with out='a {{TOOL_ROOT}}w/t.js b {{TOOL_ROOT}}w/t.json' and kp='{{TOOL_ROOT}}w/t.js', the output was `a x&y/k/t.js b x&y/k/t.json`, so the longer citation picks up the shorter one's resolved directory. TOOL_ROOT_CITE_RE's greedy `[\w.-]+` captures t.json as its own cite, but the bash pass does not respect that boundary. The defect is latent: today's SKILL.template.md citations (lines 12, 45, 76, 84) contain no prefix pair, so the current render is unaffected. The same loop shape already exists in render_doc (render-doc.sh:46-48), but this diff adds a new instance in adopt-roles.sh, so it is in scope. Low. | unsound | - |
| 4 | correctness | help/roles.md:136 | low | low | confirmed | This diff added the enumeration. The bullet at base 033b15f2 read only 'each tool prints a note naming the missing harness'. The new text lists only `render_agents.py` and check-wiring's session-start report. tools/roles/check_roles.py:293-296 still appends 'roles: note: %s harness %s is not held by this tree' through lib.resolve_harness_path, and the 'roles catalogue' leg (tools/gate-legs.json:1709) runs it. tools/roles/README.md:285 names all three readers ('the catalogue checker, the agent render and `check-wiring.sh`'). The two docs now disagree. This is documentation only and changes no behaviour. | sound | - |
| 5 | seams | tools/lib/resolve-python.test.sh:335 | medium | low | confirmed | I read the canonical at tools/lib/resolve_kit_dir.py:42-43: `hit = (root / path).absolute()`, then `if hit.is_file() and root in hit.parents and "." + "." not in hit.parts` (the second term is spelled as in the source, `".." not in hit.parts`). pathlib's absolute() does not collapse '..'. I ran `(Path('C:/a/rk')/'../out/w.js').absolute()` and got `C:\a\rk\..\out\w.js`, with `root in parents` True and `'..' in parts` True. So row 5 of section 2e ('../out/w.js', resolve-python.test.sh:348) passes the `root in hit.parents` term and is rejected only by the '..' term. No row reaches the other escape term, so deleting it leaves 2e green, as the finder says. Section 2e is new in this diff, and its comment says 'rows 5 and 6 hold the escape and existence tests'. That claim overstates its coverage. The ungated term itself was ungated at the base too, and the term is still present and correct in every copy, so no wrong result ships. What is left is a test whose comment claims more than it gates. I grade it low rather than medium. | sound | fixture-passes-by-finding-nothing |
| 6 | seams | help/roles.md:136 | low | low | confirmed | This is the same observation as id 4. The enumeration this diff added at help/roles.md:136-137 lists `render_agents.py` and check-wiring's session-start report, and leaves out check_roles.py. check_roles.py:296 still prints 'roles: note: ... harness ... is not held by this tree' under the 'roles catalogue' leg, and tools/roles/README.md:285 names all three readers. The docs disagree, with no effect on behaviour. | sound | - |
| 7 | verification | tools/check-wiring.sh:1746 | low | low | confirmed | Line 1746 of tools/check-wiring.sh now ends `; /build cannot drive it; bash $kit/adopt-roles.sh --check says whether its kit holds it elsewhere`. At 033b15f2 it ended `...cannot drive it until the review harness is installed`. The only assertion on this line is at tools/check-wiring.test.sh:2173. It counts lines that match `^note     roles     — nowhere/absent-harness.js is named by the role index`, and that prefix is the same in both versions. The diff stat shows check-wiring.test.sh was not touched in this range. So if the line is reverted, or $kit comes out empty, the self-test still passes. The only other evidence is a one-time grep of the source in the acceptance ledger (line 81). The neighbouring UNWIRED arm at :2181 does assert `${KP}$RL/adopt-roles.sh --scaffold`. The gap is real, but it only affects a diagnostic note's remedy text and no verdict, so it is low. | sound | - |
| 8 | verification | tools/roles/adopt-roles.test.sh:344 | low | low | confirmed | At adopt-roles.test.sh:543, arm 14 checks each harness with a bare substring, `grep -qF -- "${_a14[$_i]}"`, where the value is `tools/renamed/<name>`. The negative check looks only for `tools/<home>/<name>`, and the `--check` half re-renders through the same render_skill, so it agrees with whatever --scaffold wrote. A wrong but containing form therefore passes. One example is a receipt-branch regression in resolve_kit_dir that returns `hit` instead of `hit.parent`. That gives `tools/renamed/tier2-review.js/tier2-review.js`, which still contains the searched string. One part of the finder's scenario is overstated. Dropping `.relative_to` everywhere would be caught by gov's `roles render wiring` leg: gov's tracked .claude/skills/build/SKILL.md cites `tools/workflows/tier2-review.js`, which the probe branch resolves through the same relative_to. The arm itself still proves only 'contains', so the oracle weakness is real. Its effect is limited to test strength, so it is low. The fix is sound. SKILL.template.md cites both workflow-driver harnesses wrapped directly in backticks (lines 45 and 76), so grepping for the backticked path matches exactly the cited form. | sound | - |
| 9 | verification | tools/roles/roles_lib.py:605 | low | low | confirmed | resolve_cited_paths is new in this range (roles_lib.py:602). It catches `(LookupError, ValueError)`, and adopt-roles.sh:178 returns 2 with 'the citation pass ... failed'. A grep of tools/ finds only one test caller of the citation pass, arm 14, which builds a receipt-hit layout inside the fixture. No section in resolve-python.test.sh calls resolve_cited_paths. The branch is reachable. At a root install, adopt-roles.sh passes kit.parent (the repo) as tool_root. resolve_kit_dir's second probe is then here.parent/<home>/<anchor> (roles_lib.py:127), which lies outside the repo, and relative_to raises ValueError. The current code handles this correctly, so the defect is only an ungated branch on a narrow layout (a sibling `<home>/<anchor>` beside the repo), which makes it low. The fix is sound. A TMP_ROOT fixture with repo/.git, repo/roles and a sibling workflows/tier2-review.js reaches the branch without touching the real tree. Narrowing the except to `except LookupError` would make the call raise, so the new row would go red. | sound | - |
| 10 | intent | tools/roles/adopt-roles.test.sh:524 | medium | medium | confirmed | At tools/roles/adopt-roles.test.sh:524 arm 14 builds its population by iterating roles_lib.TOOL_ROOT_CITE_RE.finditer over SKILL.template.md. It skips any match whose groups are not in the workflow table (line 527), and its only floor is `[ "$_i" -ge 2 ]` (line 548), which one pair satisfies. The template cites workflows/unattended-build.js (:45) and workflows/tier2-review.js (:76). If the regex were narrowed so that the second cite matched only `workflows/tier`, that pair would be skipped as not in the table, and arm 14 would plant and check only unattended-build.js. resolve_cited_paths (roles_lib.py:611) uses the same regex, so it would not list the tier2 cite, and adopt-roles.sh:188's plain substitution would write the cited-home path into the Skill without the arm going red. Grep finds no other test of TOOL_ROOT_CITE_RE in tools/. So the guard reads its population through the code under test, which is the [class] rule's shared-state failure. The effect is limited to a weaker gate, which is why I grade it medium. | unsound | - |
| 11 | intent | help/roles.md:137 | low | low | confirmed | The diff rewrote help/roles.md:136-137 so that the tools printing a note for an absent harness are listed as `render_agents.py`, and check-wiring's session-start report. tools/roles/README.md:285 (also touched by this diff) names three: the catalogue checker, the agent render and check-wiring.sh. check_roles.py:296 really does append `roles: note: %s harness %s is not held by this tree` for an unheld harness. The base help text said only 'each tool prints a note', so the incomplete list is new in this diff. This is a documentation inconsistency with no effect on behaviour, so low. | sound | two-answers-to-one-question |
| 12 | intent | tools/check-wiring.sh:1746 | low | low | confirmed | The note's new tail is at tools/check-wiring.sh:1746. The only runtime assertion on that line, tools/check-wiring.test.sh:2173, greps only the prefix `^note     roles     — nowhere/absent-harness.js is named by the role index`. AC9 (spec 2 :434) asks only that `grep -c 'adopt-roles.sh --check'` over the source prints at least 1, and the comment at check-wiring.sh:1689 already contains that string. If the pointer were dropped from the echo, every gate would stay green. The shipped text is correct today, so this is only a gate gap, graded low. | sound | line-claim-matched-over-the-whole-output |
| 13 | intent | help/roles.md:142 | low | low | confirmed | The claim holds against the code. help/roles.md:142-143 now says 'A file of its name beside neither mark is your own', and the render_agents.py docstring (lines 39-40) says such a file 'is an adopter's namesake and not the kit's'. Both sentences are new in this diff: the base help at 033b15f2 had no such sentence. scan_misplaced_harnesses (render_agents.py:182-199) counts a hit only when `<stem>.template<suffix>` or a kit.toml whose `home` equals listed.parent.name sits beside the file. In tools/workflows/ the files are unattended-build.template.js and tier2-review.template.js, and there is no unattended-unit.template.js. The kit's unattended-unit.js, which workflows.toml lists for the `build` workflow, therefore carries only the kit.toml mark. Spec 2 §98-106 records the repro install holding unattended-unit.js with no template. Spec 2's C2 row names the copy-install that pruned kit.toml as a real case. In that install the kit's own unattended-unit.js prints the note, and the docs tell the adopter the file is theirs. The effect is wording only: the outcome is the note, which exits 0, so nothing goes wrong at runtime. That makes it low. | sound | - |
