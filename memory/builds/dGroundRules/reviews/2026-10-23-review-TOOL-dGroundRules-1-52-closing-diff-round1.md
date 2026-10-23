**Serves:** diff-review TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52

# Closing diff review, round 1: dGroundRules' spec run (the Policy build of the dClosedLoop chain)

2026-10-23 · Tier-2 · on `branch/unattended-dgroundrules-0e6f4a` · adversarial fan through `tier2-review.js`: five finder lenses (gov-diff-reviewer), five skeptic batches (gov-skeptic), synthesis by gov-synthesizer. The range is the spec run that README rule 1 defines, and it adds no product code. It holds 51 unit specs (TOOL-dGroundRules-1 to -11 and -13 to -52), six spec-audit records, 40 departure records, the shared spec brief, the owner's round-6 audit cap, RUN.md and the regenerated indexes. Units 44-52 are unaudited under the owner's cap and close under a specs-audited override. The intent supplied was 5 spec documents plus the range's commit messages.

**Reviewed range:** `3708a705e834709f340a2d160f9acdf9c18b699f...7810198ad2b39223cb959dcd6d8201679945251b`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker. Four HIGH items hold 10 raw findings. In each, a builder who follows the specs as written meets a criterion that cannot pass, or a check that grades the wrong file. Two of the four sit in units 44 and 45, which the owner's cap leaves unaudited. No later spec round will catch them, so they must be fixed before the build run's first pass, or carried into it as known-red. The run is complete: 5/5 lenses and 5/5 skeptic batches returned, and none died.

## Review shape

Intensity full, raw 23, confirmed 18, refuted 5, unverified 0 (0 uncertain), precision 0.78.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 3 | 1 | 2 | 0 | 0 | 0.33 |
| correctness | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| seams | yes | 4 | 3 | 1 | 0 | 0 | 0.75 |
| verification | yes | 7 | 5 | 2 | 0 | 0 | 0.71 |
| intent | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |

Adjudicated tally:

| severity | items | raw confirmed findings |
|---|---|---|
| BLOCKER | 0 | 0 |
| HIGH | 4 | 10 (ids 1, 4, 5, 8, 9, 12, 13, 14, 19, 20) |
| MEDIUM | 2 | 4 (ids 6, 15, 21, 22) |
| LOW | 1 | 4 (ids 7, 11, 18, 23) |
| total | 7 | 18 |

Run integrity:

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 16 judged sound, 2 judged UNSOUND (ids 1 and 8, where the skeptic's corrected fix is given below), 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 left ungraded by the skeptic. 1 was re-graded by the skeptic: id 7, from medium to low.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Checklist: 16 items, each assigned to exactly one of 5 lenses (security 4, correctness 3, seams 3, verification 3, intent 3).
- By design: the caller's byDesign.

## HIGH

### H1. Unit 44's acceptance literals are stripped, so AC2 and AC3 cannot pass on a correct build (ids 5, 9, 12, 14, 19)

**Where:**
- `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-44.md:129` (TRAP_SH)
- `:132` (NOT_A_TRAP)
- `:141` (AC3)

**What is wrong:** there are three separate faults in this unit's literals.
- TRAP_SH is `bash -c '. lib-unattended.sh; overlaps tools/policy/a ab.py; echo $?'`, which sources the library by its bare name. The library is tracked only at `tools/unattended/lib-unattended.sh`. Run from the root, the literal printed `lib-unattended.sh: No such file or directory`, then `overlaps: command not found`, then `127`.
- TRAP_SH also strips the trap row's second operand to `ab.py`, where the trap row (`:32`, `:77`) and TRAP_PY (`:128`) use `tools/policy/ab.py`. Under RAW_BOTH, a raw prefix `covers` compares `tools/policy/a` with `ab.py`. Neither is a prefix of the other, so the call returns 1. The `0` that AC2 expects on its red case can never be observed.
- NOT_A_TRAP respells the disjoint row as `a.py tools/policy/ab.py`. That leaves one `tools/policy/` on the line, and TRAP_PROBE keeps only lines where `count('tools/policy/') == 2`. TRAP_PROBE therefore prints nothing, while AC3 expects one line ending `False False`.
- Even once respelled, AC3 only reads the table in Python. It never runs the suite, so S2's refusal (`not a string-prefix trap`) goes unobserved. AC3 is the only criterion that names S2.

**Consequence:** unit 44 was promoted from round 6's only blocker (review id 29) to prove that the trap row tells a raw compare from containment. As written, it can show neither its green case nor its red case. A builder must either park the unit or respell the literals on a path no audit reviews. Respelling is the class that units 42, 46 and 47 were promoted to close.

**Fix (skeptic judged SOUND):**
- Spell the literals whole inside the §6 fenced block. Write `TRAP_SH = bash -c '. tools/unattended/lib-unattended.sh; overlaps tools/policy/a tools/policy/ab.py; echo $?'`. Probed at base, it prints `1`. The better option is to drop TRAP_SH and TRAP_PY and observe AC2 through unit 45's PAIRS_TABLE once H2 is repaired, so the pair is spelled only once.
- Set `NOT_A_TRAP` to the disjoint row respelled `tools/policy/a.py tools/policy/ab.py`.
- Restate AC3 as: run `bash tools/check-spec-tokens.test.sh` in that copy. It exits non-zero and prints a failure line that names the row and `not a string-prefix trap`. It is red when the row check is absent or silent.
- Bump the unit to rev-2. Run every literal verbatim from the root before the spec commits, as unit 47 S1 requires.

**Left-shift gate:** unit 46's bare-source join, once built, catches the TRAP_SH source. Extend it, or add a spec-tokens arm, so that every path operand in a §6 fenced literal must resolve against the tree or be declared as created by a named unit. That would also catch the stripped `ab.py` and the `a.py` respelling. A spec whose criteria name a scope item must observe it through the shipped suite and not through a side read of its fixture. Add that to the bug-class checklist as "criterion reads the fixture, never runs the check".

### H2. Unit 45's PAIRS_TABLE sources the library by bare name, so its shell column is always 127 (ids 4, 13, 20)

**Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-45.md:124`.

**What is wrong:** PAIRS_TABLE is the single probe unit 45 creates so that no criterion restates a pair. It runs `sh=$(bash -c ". lib-unattended.sh; overlaps '$a' '$b'; echo \$?")`. From the root the source fails and `overlaps` is undefined, so every row's last field is `127`. This is the same stripped-library defect (round-6 review ids 1, 10 and 20) that unit 45 exists to remove. Unit 46 forbids exactly this bare source, but it measured only 34:509 and 40:129.

**Consequence:** unit 45 AC2 (`True 0` / `False 1`, line 134) cannot pass on a correct build. Every criterion routed through PAIRS_TABLE inherits the failure:
- unit 40 AC1-AC3 (via `:59`)
- unit 43 AC1 (`:123`)
- unit 52 S5, S12, S21 and AC5 (`:78`, `:103`, `:166`, `:324`)

Seam finding id 9 also notes this as the second drifted spelling beside H1's TRAP_SH. Id 9 is counted under H1.

**Fix (skeptic judged SOUND):** in the fenced block, spell line 124 as `sh=$(bash -c ". tools/unattended/lib-unattended.sh; overlaps '$a' '$b'; echo \$?")`. Bump unit 45 to rev-2. Run PAIRS_TABLE verbatim from the root before the spec commits (unit 47 S1). With the whole path sourced, the two rows answer 0 and 1 as AC2 expects.

**Left-shift gate:** the same as H1. Unit 46's `[source]` join must run over the specs of every round, units 44-52 included. Unit 47's "run each literal verbatim before commit" should become a gate the spec commit passes, not a prose instruction.

### H3. Unit 21 S34 points agent-limit rule 7 at a declared settings file instead of the files the harness applies (id 1)

**Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-21.md:210` (S34), with AC34 at `:545-547`.

**What is wrong:** S34 has the render and rule 7 resolve "the settings file" the way `tools/check-wiring.sh:94-117` does. That resolver is either/or: when `GOV_SETTINGS_JSON` is set, the declared file is the only file it reads. Unit 10 S5 (`spec-10.md:79-88`) and AC11 have rule 7 read `.claude/settings.json` and `.claude/settings.local.json` and take the value the harness applies, local first. Whenever the variable is set, S34 silently replaces that reading.

**Consequence:** `GOV_SETTINGS_JSON` is a supported layout, honoured by `check-wiring.sh`, `adopt-unattended.sh:867` and `govkit.py:6132`. Hooks inherit the harness environment. So in a session where the variable is set, a project-level or local env value above `runtime.agents-in-flight` is never compared with the limit, and rule 7 stays green. Unit 10 retires agent-cap's clamp and slot ledger, which leaves rule 7 as the only check. The result is a check that certifies what it does not check. The path is narrow, because it needs both the variable and a project-level override.

**Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):**
- Rule 7 builds the value the harness applies by precedence. It reads `.claude/settings.local.json`, then `.claude/settings.json` under the checkout root, then the `GOV_SETTINGS_JSON` file (the user-level layer) when one is declared.
- For each variable, rule 7 takes the highest-precedence file that sets it. It refuses, naming the file, when no layer sets the variable or the value is above the limit.
- The render keeps writing the declared file when the variable is set.
- Add case `limit-settings-elsewhere-project-over`: the declared file is at the limit and the project file sets either variable above it. The expected result is exit 2, naming the project file.
- Add case `limit-settings-elsewhere-only`: the declared file is at the limit and there is no project or local env. The expected result is exit 0.

**Left-shift gate:** bug-class checklist entry: "a check that reads configuration must read every layer the consumer applies, in the consumer's precedence; a resolver built for locating a write target is never the reader for an enforcement check". Each such check carries a fixture in which a higher-precedence layer violates while the graded layer is clean.

### H4. Units 21 and 9 disagree on what `resolve` returns for an unset `budgets.<cap>` (id 8)

**Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-21.md:123` (S12), against `spec-9` S2 (`:44-51`) and its consumes-from edge `spec-9:107` (the reciprocal of `spec-3:65`).

**What is wrong:**
- Unit 21 S12 makes `read_default_value` return a Refusal for any `{ derived = ... }` default.
- Unit 9 expects an unset `budgets.<cap>` to come back with source `default`, which it reads as "no file value".
- `RESOLUTION_ORDER` (`spec-3:100`) sends an unset key to `read_default_value`.
- v2's `budgets.*` Default cell is prose, so under unit 1's grammar (`spec-1:120`) it must be a derived default. No spec gives `budgets.*` a literal default.

**Consequence:** gov's policy file sets no `budgets.<cap>`. Once unit 21 (order 7) is built on top of unit 9 (order 5), every `resolve_caps` read raises the derived-default refusal. S31 (`spec-21:195-201`) then turns that refusal into `mode = refuse` for every cap, so the `budgets.enforce = warn` default never takes effect. Unit 9 AC5 and AC8 (source `default`, mode `warn`, `spec-9:297`) cannot pass on a build that follows both specs. No record reconciles the two answers.

**Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):**
- Restate unit 9 S2 and the `spec-3:65` / `spec-9:107` edge pair so that a `budgets.<cap>` whose resolution ends in `read_default_value`'s derived-default Refusal is read as "no file value".
- Alternatively, give `resolve` a flag that returns `None` for an unset derived default, and call it through the full `resolve` so that unit 4's last-valid ladder still applies.
- In either case, exempt that specific refusal from unit 21 S31's `mode=refuse` rule.
- Add a `budgets-` fixture case that resolves an unset switch cap under the shipped catalogue and expects mode `warn`, source `default`.

**Left-shift gate:** a spec-tokens arm, or a step in the build-run entry check, that pairs each consumes-from edge with its hands-off reciprocal. When a later unit restates the producer's return contract, it must name the edge and re-state the consumer's expectation. Until that exists, add a checklist entry: "a later unit that changes a shared function's return for a case must grep every consumes-from edge on that function".

## MEDIUM

### M1. Unit 46's evidence population is stale: its bare-source join also hits units 44 and 45, which share its order (ids 6, 15, 21)

**Where:** `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-46.md`:
- Goal: line 26, "hits exactly the two"
- non-goal: line 54
- §4 Evidence: line 69, measured at `0ced625e1`
- Rollout: lines 110-111
- AC3 fixture: line 169, "units 34 and 40 terminal"

**What is wrong:** unit 46 says its join "meets no live hit at its own close", because only units 34 and 40 carry the bare form and both are terminal by then. Its own SOURCE_CMD regex, run over the spec directory, also hits `spec-44:129` and `spec-45:124`. Those units were written in the same commit (d794a81bc), sit at the same order 14 (Parallel yes), and were measured after the evidence pin.

**Consequence:** if units 44 and 45 are still live when 46 closes, AC3 (`--list` prints no `[source]` hit) is red on a correct build of 46. That is likely, because their own ACs cannot pass (H1, H2). The alternative is that the new join reds two specs of this same build, which falsifies the Rollout's reason for dropping a cutoff key. The effect is contained: AC3 or the spec-tokens leg would catch it.

**Fix (skeptic judged SOUND):**
- Repair the unit 44 and unit 45 literals first (H1, H2).
- Re-measure the predicate at the commit that carries units 44-52, and record all four hits.
- Restate Goal, Evidence, Rollout and the AC3 fixture against that measurement, with units 34, 40, 44 and 45 either terminal or carrying whole paths.

**Left-shift gate:** checklist entry: "a spec's §4 population claim is re-measured at the spec's own commit whenever a sibling of the same order is written in the same disposal". A cheaper version is for the disposal step to re-run each new gate unit's predicate over the disposal's own output before committing.

### M2. The moved as-built view leaves dGroundRules' packet red under `packet.py --check` (id 22)

**Where:** `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md:5`, against the dGroundRules packet's pin at its line 57.

**What is wrong:** the range re-renders the as-built view. Its blob moves from 11e4ed05 to 08a323bb, and the view now covers 81 deviation records instead of 41. The range also grows the roster to 51 units. The packet still pins 11e4ed05, and its Obligations name only TOOL-dGroundRules-1 to -11. As a result:
- `check_text`'s byte compare goes red.
- `check_complete`'s roster arm reports 40 findings for TOOL-dGroundRules-13 to -52.
- `cmd_check` exits 1.

The dDeclaredLoop and dSafePassage packets also turned byte-red.

**Consequence:** the packet's Gates (line 41), its item 4 (line 171) and README line 36 all require `--check dGroundRules` to be green before the build run's first pass. No gate leg or driver runs `packet.py`, so the spec run lands with the build run's entry check silently red. The skeptic judged this from the source and did not run the check.

**Fix (skeptic judged SOUND):** before the close, run `packet.py --write dGroundRules` and confirm that `--check dGroundRules` is green. The write keeps the instrument pins (pin arm 0 findings), and the moved blob belongs to the view, so no "never re-rendered away" rule blocks it. dTrueNorth did the same in 0893e7225. File an ask for the other chain packets that the moved view leaves byte-red.

**Left-shift gate:** wire `packet.py --check` for every open build in the chain into a gate leg, guarded on changes to the as-built view, a build README roster or a packet. Then a re-render that invalidates a sibling packet goes red at the commit that moves it.

## LOW

### L1. The owner-cap record miscounts the promoted units as forty-one (ids 7, 11, 18, 23)

**Where:** `memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md:16`.

**What is wrong:** the record says the roster is "the eleven the README opened with and the forty-one the audit promoted". The six rounds promoted 9 + 4 + 7 + 2 + 9 + 9 = 40 units (TOOL-dGroundRules-13 to -52), which is the record's own round list. The roster is therefore 51 units, matching the README build index (`OPEN · 51 unit(s)`) and RUN.md:18 ("51 on the roster").

**Consequence:** this record is the authority the close cites for the specs-audited override and for deferring every unit. A reconciliation against it would expect 52 units, or would count the TOOL-dGroundRules-12 ask as a unit. No tool reads the number, and "every unit of the roster" still picks out the right set, so behaviour is unaffected. Id 7 was graded medium by its finder and re-graded low by the skeptic. The binding grade is low.

**Fix (skeptic judged SOUND):** change "forty-one" to "forty", or name the range TOOL-dGroundRules-13 to TOOL-dGroundRules-52, so that the record, the README index and RUN.md agree on 51 units plus the run unit TOOL-dGroundRules-12.

**Left-shift gate:** none fits a prose count. Add a checklist entry: "an authority record that states a population names it by id range, never by a spelled-out count".

## Refuted (5, not carried)

These are ids 2, 3, 10, 16 and 17. Id 10 duplicated id 6 (M1), and its one extra claim, about a stale `40:125` citation, was correct for its pinned commit. The appendix gives every skeptic reason.

review-shape kind=diff-review round=1 intensity=full at=synth raw=23 confirmed=18 refuted=5 unverified=0 blocker=0 high=10 medium=4 low=4 agents=11 out-tokens=180987
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-21.md:210 | high | high | confirmed | Unit 21 S34 (spec-21.md:210-213) says the render and rule 7 resolve "the settings file" the way tools/check-wiring.sh:94-117 does. That resolver is either/or: when GOV_SETTINGS_JSON is set it is the only file read (cand=$GOV_SETTINGS_JSON), and .claude/settings.json is never consulted. AC34 (spec-21.md:545-547) then requires rule 7 to grade the declared file. Unit 10 S5 (spec-10.md:79-88) and AC11 have rule 7 read .claude/settings.json and .claude/settings.local.json and take the value the harness applies, local first. S34 replaces that reading whenever the variable is set. check-wiring's own comment (:79-81) says the variable exists for an adopter whose live settings sit outside the worktree, i.e. a lower-precedence user-level layer. In such a session, a project or local env value above the limit is never compared with runtime.agents-in-flight and rule 7 stays green. Unit 10 retires the clamp, so nothing else catches it. The path is narrow: it needs the variable set plus a project-level override. That makes this a check certifying what it does not check on a narrow path, graded high. | unsound | - |
| 2 | security | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-6.md:129 | medium | - | refuted | The probe holds: `git cat-file -e HEAD:memory/` exits 0 and `git cat-file -t HEAD:memory/guides/` prints tree, while `HEAD:docs/*/` exits 128. But the path cannot be reached from this diff. The only class row in tools/template-size-limits.txt is `memory/builds/*/spec/`, and check-spec-tokens.py's read_size_ceilings reads exactly one class key, the constant SIZE_CLASS_KEY, which carries a `*`. Units 6 F5 and 9 F7 key every cap by its measured file's path, and unit 9's census lists no glob-free directory row. So no enforcer reads a glob-free directory key. Raising such a key would change no enforced limit, and adding one is a new row, which the guard already refuses to agents. The finder concedes the path is latent. That is a medium finding with no reachable consequence, so it is refuted. | sound | - |
| 3 | security | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-10.md:306 | medium | - | refuted | AC12 (spec-10.md:306-308) is a bullet paragraph, and the literal wraps inside an inline code span. In Markdown a line ending inside a code span reads as one space, and continuation-line indentation is stripped, so the span reads `grep -c "const MAX_VERIFIERS = 5" tools/workflows/tier2-review.js`. memory/TEMPLATE-SPEC.md:96 sets a hard wrap at about 100 columns, and :574 and :505 call wrapping across a line break this corpus's house style. Unit 47 S1 (spec-47.md:33-38) requires a literal to be run verbatim from the root, and says nothing about a wrapped span being two patterns. The gotcha record criterion-asserts-what-its-own-command-cannot-show.md lists no wrapped-literal form. The two-pattern reading comes only from pasting raw source lines into a shell, so the literal is not corrupted by the corpus's own rules. | sound | C6 |
| 4 | correctness | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-45.md:124 | high | high | confirmed | spec-45.md:124 has PAIRS_TABLE run `bash -c ". lib-unattended.sh; overlaps '$a' '$b'; echo \$?"`, and the library is tracked only at tools/unattended/lib-unattended.sh. Run from the root, the bare-name probe printed `lib-unattended.sh: No such file or directory`, `overlaps: command not found` and `127`. So the sh column is always 127, and AC2's `True 0` / `False 1` can never pass on a correct build. Unit 43 (:123), unit 40 (:59) and unit 52 (:78, :103, :166, AC5 :324) all route through PAIRS_TABLE. Unit 46 (spec-46.md:22-26, :70-71) forbids exactly this bare source, but it measured only 34:509 and 40:129, and no later unit respells 45:124. The range introduces this. | sound | - |
| 5 | correctness | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-44.md:129 | high | high | confirmed | spec-44.md:129 has `TRAP_SH = bash -c '. lib-unattended.sh; overlaps tools/policy/a ab.py; echo $?'`. Run from the root it printed 127, so AC2's built-tree `1` fails. The second operand is also stripped: the trap row and TRAP_PY (:128) both use tools/policy/ab.py. With the library sourced by path, `overlaps tools/policy/a ab.py` returned 1. Under a raw prefix compare, `ab.py` and `tools/policy/a` share no prefix in either direction, so it still returns 1. AC2's RAW_BOTH half, which wants `0`, can never be seen. The criterion therefore cannot show its own red case, which is the purpose unit 44 states. No later unit respells 44:129. | sound | - |
| 6 | correctness | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-46.md:111 | medium | medium | confirmed | Confirmed. Spec-46 Rollout (:111) and AC3's fixture (:169) say the only bare-source hits are units 34 and 40 (orders 12 and 13), so the join 'meets no live hit at its own close'. I ran the spec's own pattern over the spec/ directory. It hits 34:509, 40:129, 44:129 and 45:124, plus 46:104, which is 46's own fixture text in a fenced design block. Units 44 and 45 are OPEN at order 14, the same order as 46, and were added in the same commit as 46 (d794a81bc). So nothing makes them terminal before 46 builds, and AC3 goes red on a tree where they are still live. The §4 evidence is pinned at 0ced625e1, before 44 and 45 existed. The effect is contained: the build run's AC3 or the spec-tokens leg would catch it. | sound | - |
| 7 | correctness | memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md:16 | medium | low | confirmed | Confirmed. Cap record line 16 says 'the eleven the README opened with and the forty-one the audit promoted'. The same record's line 10 lists rounds promoting 9, 4, 7, 2, 9 and 9, which sum to 40. spec/ holds 51 files (1-11 and 13-52), README.md:113 reads 'OPEN · 51 unit(s)', and RUN.md:18 says '51 on the roster'. The record contradicts itself and both indexes. The deferral wording 'every unit of the roster' still picks out the right set, so the miscount is a prose error with no effect on behaviour. | sound | - |
| 8 | seams | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-21.md:123 | high | high | confirmed | Confirmed by reading the specs. Spec-9 S2 (:44-51) reads each cap's value 'all of it through policy.resolve'. Its edge at :107, the reciprocal of spec-3:65, expects an unset budgets.<cap> to come back with source `default`, which S2 reads as 'no file value'. Spec-3:100 sets RESOLUTION_ORDER = (read_file_value, read_default_value), so an unset key falls through to read_default_value. Spec-21 S12 (:123-126) makes read_default_value return a Refusal for any `{ derived = ... }` default. Spec-1:120 gives `default` as a TOML value or `{ derived = "<v2's Default cell>" }`, and v2's budgets.* Default cell (packet:120) is prose ('the value its legacy home held ... re-derived from evidence'). No spec gives budgets.* a literal default: spec-1:30's literal rows are the four switches, not budgets.*. Spec-21 S31 (:195-201) then turns any refusal inside resolve_caps into mode=refuse. Unit 21 (order 7) builds after unit 9 (order 5), so it breaks unit 9's warn default and AC8's expected 'mode warn, source default' (spec-9:297). All of these specs were added in this range; the base tree holds only the README, BACKLOG and packet. A build following both specs would go red at unit 9's ACs, so this is high rather than blocker. | unsound | C3 |
| 9 | seams | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-44.md:129 | high | high | confirmed | Confirmed by running the probe. spec-44:129 is TRAP_SH = `bash -c '. lib-unattended.sh; overlaps tools/policy/a ab.py; echo $?'` and spec-45:124 runs `. lib-unattended.sh` inside PAIRS_TABLE. Run from the repository root, TRAP_SH printed 'lib-unattended.sh: No such file or directory', 'overlaps: command not found' and 127. No lib-unattended.sh exists at the root. With the whole path, `. tools/unattended/lib-unattended.sh`, overlaps printed 1 for the trap pair and 0 for the directory pair. TRAP_SH also strips the second path to `ab.py`, while S1's row is `tools/policy/ab.py`. Under RAW_BOTH, a raw startswith of 'tools/policy/a' against 'ab.py' is False, so even a sourced library could not print the 0 AC2 expects. Unit 44 AC2 and unit 45 AC2 cannot pass, and unit 52 consumes PAIRS_TABLE for S5, S12, S21 and AC5 (spec-52:78, :103, :166, :324). Units 44-52 go unaudited under the owner's cap, so no audit round would catch this. A correct build would show red criteria, which is why this is high and not blocker. | sound | C3 |
| 10 | seams | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-46.md:111 | medium | - | refuted | This duplicates id 6: the same spec-46 Rollout claim (:54, :111) and AC3, broken by the same bare-source literals at spec-44:129 and spec-45:124, which I confirmed under id 6. Its one extra claim, that the '40:125' citation is stale, does not hold. Spec-46 §4 pins its evidence at 0ced625e1, and `git show 0ced625e1:.../spec-40.md` puts PAIRS_SH at line 125, so the citation is correct for the commit it is pinned to. | none | C3 |
| 11 | seams | memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md:16 | low | low | confirmed | The record is new in this range; it is absent at base. Line 16 says 'the eleven the README opened with and the forty-one the audit promoted'. Its own line 10 lists 9, 4, 7, 2, 9 and 9, which sum to 40. The spec directory holds 51 files: 1-11 and 13-52. RUN.md:18 also says '51 on the roster'. The count is wrong in prose that no tool reads, so behaviour is unaffected. | sound | C3 |
| 12 | verification | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-44.md:129 | high | high | confirmed | Spec 44:129 reads TRAP_SH = bash -c '. lib-unattended.sh; overlaps tools/policy/a ab.py; echo $?'. The library lives only at tools/unattended/lib-unattended.sh. Run from the root, the literal printed 'lib-unattended.sh: No such file or directory', then 'overlaps: command not found', then 127, where AC2 expects 1. With the full source path, `overlaps tools/policy/a ab.py` and `overlaps tools/policy/a tools/policy/ab.py` both printed 1. Under a raw startswith, 'tools/policy/a' against 'ab.py' is not a prefix in either direction, so AC2's RAW_BOTH expectation of 0 cannot occur either. The bare basename is not forced by the spec-tokens paths join. The adjacent TRAP_PY (line 128) and unit 40's ARM_ROWS spell tools/policy/ab.py whole, and the library is a tracked file, not one the build creates, so the BY DESIGN basename note does not cover it. AC2 cannot pass on a correct build. | sound | - |
| 13 | verification | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-45.md:124 | high | high | confirmed | Spec 45:124 reads sh=$(bash -c ". lib-unattended.sh; overlaps '$a' '$b'; echo \$?"). Run from the root, the bare source fails and `overlaps` is undefined, giving exit 127, as I observed for the identical bare source in TRAP_SH. Every row's last field is therefore 127, never the 0 or 1 that AC2 at line 134 requires. The same bare form is the H1 defect, recorded in round 6 as ids 1, 10 and 20. With tools/unattended/lib-unattended.sh sourced, the two table rows answer 0 and 1 as AC2 expects. | sound | - |
| 14 | verification | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-44.md:141 | high | high | confirmed | In spec 44, NOT_A_TRAP (line 132) respells the row 'a.py tools/policy/ab.py', so the table line (form `check_overlap_pair <a> <b> disjoint`, per unit 45:79) holds one 'tools/policy/'. TRAP_PROBE keeps only lines with l.count('tools/policy/') == 2, so it prints nothing, and AC3, which expects one line ending 'False False', cannot pass. AC3 is the only criterion S2 names ('Observed by AC3'), and it runs only a standalone Python read of the table, never the suite. Once respelled, it would certify S2's refusal without ever exercising it. The section-7 arm line declares the refusal by name, but no criterion observes it. | sound | - |
| 15 | verification | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-46.md:169 | medium | medium | confirmed | I ran spec 46's SOURCE_CMD regex over every section 6 under memory/builds/*/spec/, keeping operands without '/'. It printed four hits: TOOL-dGroundRules-34, -40, -44 and -45, each lib-unattended.sh. Spec 46's Goal (line 26: 'hits exactly the two'), Evidence (line 69, measured at 0ced625e1), Rollout (line 110) and AC3's fixture ('units 34 and 40 terminal') all assume two hits. Units 44 and 45 sit at order 14, the same order as 46, so nothing makes them terminal before 46 builds. Their own unpassable ACs (ids 12 and 13) make a park, which leaves them live, likely. AC3 would then red on a correct build of 46. The effect stays inside one criterion. | sound | - |
| 16 | verification | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-52.md:337 | medium | - | refuted | The moved rule does get observed failing, by a mechanism the finding leaves out. Unit 52 §7 line 389 declares `New arm: tools/run-gates/run-gates.test.sh (arm 1b) · covers none · PYC_GUARD appended to a scratch copy's policy fixtures guard ...`. memory/guides/BUILD-METHOD.md:280-282 requires that, for each `New arm:` line of the build's specs, the main loop observes the arm RED on its staged break and GREEN once restored, and records both in the unit's acceptance ledger. S9 (lines 88-94) also says the unit-37 arm line 'is observed at the close on that arm, staged with the same PYC_GUARD'. `covers none` is legal per TEMPLATE-SPEC.md:283-285, for an arm that observes scope no criterion names. AC9 only certifies the removal half of S9. Arm 1b (run-gates.test.sh:619-660) is generic over every leg's guard, with no per-leg branch, so the owed-arm observation is the red check the finding says is missing. | unsound | - |
| 17 | verification | memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md:10 | low | - | refuted | The record is accurate, not defective. The cap record line 10 and RUN.md:18 quote the per-round promotion counts (9, 4, 7, 2, 9, 9) and a precision range. That range matches the six audit records' 'Intensity full' lines: 0.88, 0.93, 0.90, 1.00, 0.85, 0.87, so 0.85-1.00. The raw and confirmed denominators are stated in each audit record under reviews/. The question the cap settles, whether the promotion chain shrinks, is answered by the promotion counts the record does quote. Leaving out data that is recorded elsewhere is a presentation preference, not a defect with an effect. | sound | C14 |
| 18 | verification | memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md:16 | low | low | confirmed | The cap record (added in this range, commit 7810198ad) says at line 16 'the eleven the README opened with and the forty-one the audit promoted'. The promotion counts on its own line 10 sum to 9+4+7+2+9+9 = 40, and the promoted units TOOL-dGroundRules-13 to -52 are 40. The spec/ directory holds 51 files, and README.md:113 reads '51 unit(s)'. So the record implies 52 deferred units where 51 exist. The error is in prose only. No machine check reads this count, so the effect is a misleading figure in the authority record. | sound | - |
| 19 | intent | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-44.md:129 | high | high | confirmed | Unit 44 line 129 spells `TRAP_SH = bash -c '. lib-unattended.sh; overlaps tools/policy/a ab.py; echo $?'`. Run from the root, it printed 'lib-unattended.sh: No such file or directory', then 'overlaps: command not found', then 127, where AC2 expects 1. With the library path fixed, `overlaps tools/policy/a ab.py` returned 1. Neither `ab.py` nor `tools/policy/a` is a raw string prefix of the other, so the RAW_BOTH half of AC2 (expecting 0) cannot occur. NOT_A_TRAP (line 132) respells the row as 'a.py tools/policy/ab.py'. TRAP_PROBE keeps only rows with `l.count('tools/policy/') == 2`, so that row is filtered out and AC3's expected 'False False' line never prints. The same fence already spells whole paths elsewhere (TRAP_PY has `tools/policy/ab.py`; unit 46:105 spells `tools/unattended/lib-unattended.sh`). So the bare spelling is not forced by the basename convention. A correct build therefore fails AC2 and AC3, and no later spec round will audit unit 44, which misleads the build run. | sound | - |
| 20 | intent | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-45.md:124 | high | high | confirmed | Unit 45 line 124 runs `sh=$(bash -c ". lib-unattended.sh; overlaps '$a' '$b'; echo \$?")`. The same bare-name source exits 127 from the repository root (observed above), so the sh column is 127 on every row. AC2's `True 0` / `False 1` therefore fails on a correct build. Unit 52 AC5 (line 324) and the hands-off edges in units 40:59 and 43:123 route their criteria through this PAIRS_TABLE, so those inherited observations fail too. The corrected spelling, `. tools/unattended/lib-unattended.sh`, sources cleanly and `overlaps` returns its exit code. | sound | - |
| 21 | intent | memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-46.md:110 | medium | medium | confirmed | I grepped the specs for lib-unattended.sh. Bare-name sources sit inside acceptance fences at spec-34:509, spec-40:129, spec-44:129 (TRAP_SH = bash -c '. lib-unattended.sh; ...') and spec-45:124 (bash -c ". lib-unattended.sh; overlaps ..."). Unit 46's SOURCE_CMD regex accepts a leading quote or whitespace and keeps operands with no '/', so it catches both of the new lines. Specs 44, 45 and 46 all carry 'order 14' in their status headers. That means 44 and 45 can still be live (OPEN) when 46 builds, and AC3 ('--list prints no [source] hit') reds. That contradicts 46's Rollout (line 110) and its cutoff-key non-goal (line 54). 46's §4 Evidence was measured at 0ced625e1, before 44 and 45 existed, and it counts only the two hits in 34 and 40. All five specs are added in this range, so the defect is not pre-existing. | sound | - |
| 22 | intent | memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md:5 | medium | medium | confirmed | The range changes the as-built view blob from 11e4ed05 to 08a323bb, 41 to 81 deviation records according to the generator line. The dGroundRules packet still pins 11e4ed05 at line 57. render_text writes the view_blob from HEAD, so in packet.py, check_text's byte compare (text != rerendered) goes red. The README roster:units now holds 51 ids, up from 11 at the base. The packet's Obligations name only TOOL-dGroundRules-1 to -11, so check_complete's roster arm reports 40 findings, and cmd_check returns 1 whenever there is any finding. The packet's Gates (line 41), its item 4 (line 171) and README line 36 all require '--check dGroundRules green before the first pass'. The moved blob belongs to the view, not to an instrument, so the 'never re-rendered away' rule does not stop a --write. Commit 0893e7225 shows dTrueNorth re-rendering its own packet in exactly this situation. I judged this from the source and did not run the check. | sound | - |
| 23 | intent | memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md:16 | low | low | confirmed | Line 16 of the owner-cap record says 'the forty-one the audit promoted'. The same record's line 9 lists the rounds as 9, 4, 7, 2, 9 and 9, which sum to 40. The promoted range TOOL-dGroundRules-13 to -52 is also 40 ids, and the README roster holds 51 unique ids: 11 clause units plus 40. The miscount is in prose only, and no tool reads it. | sound | - |
