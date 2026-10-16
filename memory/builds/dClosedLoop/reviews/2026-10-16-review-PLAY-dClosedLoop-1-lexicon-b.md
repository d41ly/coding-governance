**Serves:** spec-audit PLAY-dClosedLoop-1

# Spec audit of the lexicon's design record (dClosedLoop), run B

Reviewed: memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md@424d2a7dee1d47bf5cc11b8702333bb075795fd3. Round 1.

## Verdict: CLEAN WITH FIXES

There are no blockers. The record has 3 high findings in 2 items, and they must be fixed before dMindYourWords is specified. By item the tally is 0 blocker, 2 high, 22 medium and 14 low, 38 items in all. By raw confirmed finding it is 0 blocker, 3 high, 29 medium and 17 low, 49 findings in all.

Review shape: intensity full, raw 56, confirmed 49, refuted 7, unverified 0 (0 uncertain), precision 0.88.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 13 | 13 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 14 | 12 | 2 | 0 | 0 | 0.86 |
| reuse | yes | 10 | 8 | 2 | 0 | 0 | 0.80 |
| blast-radius | yes | 9 | 8 | 1 | 0 | 0 | 0.89 |
| failure-envelope | yes | 10 | 8 | 2 | 0 | 0 | 0.80 |

Run integrity:
- All 5 lenses returned and none died.
- All 5 skeptic batches returned and none died.
- Nothing was demoted to unverified: 0 contradictory verdicts, 0 orphaned duplicate refutations.
- 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 45 judged sound, 4 judged UNSOUND, 0 none proposed and 0 NOT JUDGED.
- Severity: 0 findings were left ungraded by the skeptic, and 17 were re-graded.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.
- Intent: 12 spec documents were supplied as `specs`, as sibling context.
- Checklist: 15 items, 3 for each of the 5 lenses.
- By design: the caller's byDesign.
- Move check: no checked subject moved.

Every grade below is the binding grade. Merged findings all share one grade. Where a closely related finding carries a different grade, it is a separate item, and the item says so.

## High

### H1. The canon has no verb families, so the drift rule rests on a grouping that does not exist (ids 14, 29)

- **Where:** [design] [drift], first bullet; [fit] row 5; [forks] L-3.
- **What is wrong:** The record says "the canon already groups verbs into families, such as acquire (load, read, parse)". It does not. In `canon.py` CLUSTERS, load, read and parse are separate clusters, each with its own meaning, and no family table exists. The "acquire" set is a 14-verb set (ACQ) that the dispatch-28 researcher defined for one probe. The 57-object figure rests on that set. The research's own canon-based measure finds only 6 objects with two spellings of one cluster. The record also never cites TOOL-dScaffoldedMirror-12. That ask records four precision gaps that disqualify exactly this object-keyed instrument.
- **Consequence:** The default `lexicon.drift=refuse-new` holds in three presets. Under it, "one verb per family per object" would refuse correct layered pairs that the verb table itself prescribes. One example is `load_conf` calling `parse_conf_text` in drift_report.py. A builder who reuses the canon clusters as families gets a check that never fires on the case the record cites. A builder who invents families gets a second grouping beside the canon, built at a precision the research measured as unfit.
- **Fix:** The skeptic judged id 14's fix sound. It rejected id 29's fix, and its corrected fix is folded in here.
  - State that verb families do not exist yet and must be designed. Name the artifact that will hold them: a FAMILIES layer over `canon.py` CLUSTERS, or the CANON overlay. It is declared vocabulary and changes through `instructions.edit`.
  - Define a split as two synonyms of one canon cluster on one object. Keep two declared verbs with different meanings over one object legal, for example `read_x` and then `parse_x`.
  - Cite TOOL-dScaffoldedMirror-12. Carry its prerequisite into dMindYourWords' scope as an acceptance criterion of the drift check: a real concept key, with precision hand-measured on 40 or more groups.
  - Leave L-3's settled refuse-new default unchanged.
  - Run the rule over the current tree as a fixture. The fixture must not flag `load_conf`/`parse_conf_text`.
- **Left-shift gate:** Add a checklist entry: a design claim that existing code "already" provides a structure must cite the symbol that holds it, and a spec-audit grounding arm greps for that symbol.

### H2. Inline contract declarations and site suppressions let an agent clear its own debt (id 48)

- **Where:** [design] [vocabulary], bullet 1, against [forced] items 2 and 4.
- **What is wrong:** [vocabulary] says contract declarations change only through the instruction write path (`instructions.edit`: the owner commands, agents propose). But [forced] places those declarations, and the reasoned site suppression, inline in source as `gov:` markers. `instructions.edit` guards an instruction's manifest (layer-instruction.md:673-676), not arbitrary source files. No sibling record guards inline source markers.
- **Consequence:** Any agent can add a declaration or a suppression in its own diff. That clears its debt past the at-commit refuse and the bar's by-name comparison, so both checks certify a name as forced on a stamp the agent wrote itself. This is the "stamp anyone can apply" the record says it ends.
- **Fix:** The skeptic judged this fix sound.
  - Register every contract declaration and site suppression in the lexicon declaration, which `instructions.edit` changes.
  - Refuse an inline marker that has no registered row.
  - Make an added declaration or suppression a diff the bar reds unless the owner's write-path record covers it.
  - Probe: add `gov:` suppression markers to a debt name through a plain agent edit, and show that both the commit check and the bar red.
- **Left-shift gate:** Add a checklist entry: every exemption mechanism names the write path that guards it and the check that refuses an exemption added outside that path.

## Medium

### M1. Retiring `ratified` has no inventory of its readers, and the lexicon's own drift leg goes permanently not-asked (ids 2, 30, 38)

- **Where:** [design] [vocabulary] ("`ratified` gives way to that path's record"); [classes] (the pin counts debt only).
- **What is wrong:** The stamp is retired and the pin is redefined, but the record names none of their consumers:
  - `signal_lexicon_ratified_stale` (drift_report.py:1315) returns `_build_not_asked` without the stamp. It is gateable, and v2 and layer-expansions put it in the lexicon's own leg pack (gap-lex-08).
  - kit.toml's `lexicon-ratified` hole has `blocks_gate = true`.
  - adopt-lexicon.sh S10 refuses an empty stamp.
  - govkit probes the hole.
  - scaffold_lexicon.py seeds `VERB_OFFENDER_PIN` from the raw offender count, not a debt-only count.
  - The selftests read the stamp too.
- **Consequence:** The lexicon's leg pack ships a leg that can never red. Adopters are told to stamp a key that no longer means anything and are blocked on it. The not-asked result is labelled rather than green, so the effect is contained.
- **Fix:** The skeptic judged this fix sound.
  - Add a consumer inventory to [vocabulary] and [classes] that says what each reader becomes.
  - Re-key the staleness signal to the date of the instruction write path's record. Do not drop it.
  - Retire or re-point the hole and adopt-lexicon's stamp instruction.
  - Make the scaffold seed a debt-only pin.
  - Probe: delete `ratified` from a fixture conf, and show the re-keyed signal reds on a LANGS change made after the record date.
- **Left-shift gate:** Make this a checklist entry for the class retirement-inventory-misses-readers-by-value: any retired key or redefined value lists every reader found by a grep for that key.

### M2. The lexicon now depends on the map, but nothing declares the dependency or covers a lexicon installed without the map (ids 5, 28, 42, 52)

- **Where:** [design] [integration], bullets 1-2 ("The lexicon stops walking the corpus itself, and classifies the map's definitions"; "Today's dependency inverts").
- **What is wrong:** Under KN-1, the map and the lexicon are independent optional components. Several things go unstated:
  - No record states that the lexicon requires the map.
  - No record says what the lexicon does without the map, or with a stale map index. layer-library's absence table has no row for "lexicon installed, map absent".
  - The inversion contradicts two standing decisions, TOOL-dClosedLexicon-12 and TOOL-aSurfacedLexicon-20, and the shipped `check_self_containment` (lexicon.py:2359) that enforces them. The record neither cites nor supersedes them.
  - The lexicon's kit.toml has no `requires` line.
  - The gate-legs guards still encode today's direction.
- **Consequence:** A lexicon-only install grades an empty population. That reads as zero debt and a green leg, so the gate certifies nothing, or it crashes the bar or the hook. Otherwise `check_self_containment` reds the kit at once, or a builder deletes it without an owner's decision. Changes to the map's extraction would not re-run the lexicon selftest that classifies its output.
- **Fix:** The skeptic judged all four fixes sound.
  - Name `check_self_containment` and both decisions, and state whether they are superseded.
  - Pick one route and state it. Either the lexicon declares `requires = ["codebase-map"]`, the self-containment check is re-scoped, and the lexicon is refused at install without the map. Or the lexicon keeps a fallback extractor shipped inline.
  - Make a stale or absent map index red the lexicon's legs with a reason, never an empty pass.
  - Add the "map absent" row to layer-library's absence table.
  - Flip the guards: add `{prefix}/codebase-map/` to `lexicon selftest`, and drop `{prefix}/lexicon/` from `codebase-map kit selftest` once the tokenizers move.
  - List the mirroring carriers: the kit.toml [[gate_leg]] rows and govkit/subject-pins.tsv:62-64.
  - Have the layer check see a planted lexicon-without-map install red.
- **Left-shift gate:** Extend the layer check with an arm that installs each optional component without each other optional component it reads, and requires a red or a declared refusal.

### M3. No pack covers the `mktemp` shell shim, so the pin cannot fall by 28 (ids 6, 16)

- **Where:** [current] dispatch 29 "What passes"; [classes] last bullet ("the pin falls by 28 forced"); [packs] "Shell hosts".
- **What is wrong:** The record's own table counts 6 third-party-forced names, but it says the packs "cover 5 of 5". The sixth is `mktemp() { return 1; }` at unattended.test.sh:9054. The shell packs cover only bats and bash/zsh hook functions. The "command list for shell shims" that the population research's K2b test required was dropped.
- **Consequence:** The shim, and any adopter function that shadows a command, stays debt. Its only exit is a site suppression, which the record calls a fallback. No build can meet the "falls by 28" figure, and research fixture (ii) fails.
- **Fix:** The skeptic judged this fix sound.
  - Add a curated "shadowed external commands" shell pack to the first wave. Its host is the PATH's commands, keyed by name, applied only to shell function definitions.
  - Alternatively, restate the figure as 27, with the shim under site suppression.
  - Correct "5 of 5": dispatch 29 tested 5 names.
  - Add the shim to the forced-name fixture, and carry fixture (ii) into the unit's acceptance.
- **Left-shift gate:** Add a checklist entry: a stated count a design promises to move must be reconciled, name by name, against the mechanism's coverage list.

### M4. L-4 orders dMindYourWords before the extension points it fills (id 3)

- **Where:** [forks] L-4 and the settled table (dMindYourWords as a child of dTotalRecall).
- **What is wrong:** dMindYourWords fills three extension points that builds outside its ancestry supply:
  - its commit check is a Runtime hook pack (dWellOiledMachine);
  - its leg pack registers at Test's leg-pack point (dWitnessedBar);
  - its vocabulary slice rides the work order (dBoundRoles).
  
  None of those builds is an ancestor of dMindYourWords.
- **Consequence:** dMindYourWords can be scheduled before those points exist. Its commit check and leg pack are then wired ad hoc, for example into `.githooks/pre-commit` or as core legs, and reworked later.
- **Fix:** The skeptic judged this fix sound. Set the parents to {dWellOiledMachine, dWitnessedBar}, which already cover dBoundRoles and dTotalRecall. Alternatively, name the owner of each point and order dMindYourWords after it.
- **Left-shift gate:** Add a chain-check arm: every extension point a build registers into is owned by one of its ancestors.

### M5. No build fills the tag-name vocabulary check that dOrderedCharter builds (id 7)

- **Where:** [design] (no item exists), against layer-instruction R-B and v2's dOrderedCharter roster.
- **What is wrong:** layer-instruction.md:429-430 and v2:942 say the lexicon adds its vocabulary check on namespaced tag names at an extension point. The lexicon's design and the dMindYourWords roster never fill it.
- **Consequence:** The extension point has no filler, so the tag-name check is never delivered.
- **Fix:** The skeptic judged this fix sound. Add a [design] item: the lexicon registers its tag-name vocabulary check at the instruction layer's name-check point. State what it checks (verbs or nouns in tag leaves) and its absence state ("the core's tag-shape check stands alone"). Add the item to the dMindYourWords roster.
- **Left-shift gate:** Add a chain-check arm: every extension point a roster builds names at least one filler on some build's roster.

### M6. The record never says where `lexicon.drift=refuse-new` is enforced or how it combines with `at-commit` (id 9)

- **Where:** [design] [drift]; settled L-3.
- **What is wrong:** [drift] says only "New splits are handled as L-3 says". The bar's by-name comparison covers verb offenders only. The record does not say whether a split is an offender, or whether it reds at commit, at the bar or both. The matrix of `at-commit` × `drift` values is not stated.
- **Consequence:** A builder can ship refuse-new as a commit-only check, or as nothing at the bar, and either satisfies the text.
- **Fix:** The skeptic judged this fix sound. State the enforcement points: either a split joins the debt class, so the bar comparison and the pin count it, or it forms its own set at the bar. Give the matrix of `lexicon.at-commit` × `lexicon.drift` values.
- **Left-shift gate:** Add a catalogue-check entry: every policy key names the step or steps where it is read, and every pair of keys that act on one artifact gives its value matrix.

### M7. The drift rule leaves "object" and "established verb" undefined, and says nothing about forced names (id 54)

- **Where:** [design] [drift], bullets 1-2; [forks] L-3.
- **What is wrong:**
  - "Object" is undefined: a noun subtoken, a receiver or a file.
  - The established verb is undefined when an object already carries two or more family verbs. The record's own census finds 57 such objects (conf: load 11, read 3, parse 2).
  - Nothing says whether forced names count toward the drift rule or the noun canon.
- **Consequence:** Under refuse-new, a new definition on a split object gets an arbitrary verdict. A forced name could be refused by drift even though its class exempts it. As written, the rule cannot be tested.
- **Fix:** The skeptic judged this fix sound.
  - Define the object key and the established verb, for example the most-used family verb, with ties refused and both verbs named.
  - State that forced names sit outside the drift rule and the noun canon, and do not count toward establishing a verb.
  - Add a fixture with a tied object, and one with a forced name that shares a noun.
- **Left-shift gate:** Add a checklist entry: every rule term that selects a population is defined, and its tie case is given a fixture.

### M8. The bar's by-name comparison has no base, and the seam it extends never runs in remote CI (id 15)

- **Where:** [design] [enforcement] item 3.
- **What is wrong:** The record says "the bar already computes this comparison, but only to label a red". The existing offender-set comparison has three limits:
  - it runs only on a red leg, and only when `GATE_ATTRIBUTE` is set;
  - only pre-push sets that variable, and remote-ci.yml never does;
  - its base is, by rule, the landing base.
  
  The record names no base at all.
- **Consequence:** A fixed offender plus a new one nets to zero, so the leg stays green and the seam never runs. A builder who extends the seam as written ships a check that cannot fire on the case it exists for, and that never runs in CI. With the base left open, a builder may pick the branch point, the comparison TOOL-aStagedLane-6 withdrew.
- **Fix:** The skeptic judged this fix sound.
  - Rewrite item 3 to say what exists today: `render_offender_keys` plus a subset classifier, used only for red legs under `GATE_ATTRIBUTE`.
  - State that the binding comparison is a new arm. It runs on every bar, remote CI included, whatever the leg's own verdict.
  - Name its base as the landing base, and state what CI passes as that base.
  - Probe: one branch renames one offender to a declared verb and adds one new offender. The leg must red at pre-push and in CI.
- **Left-shift gate:** Add a checklist entry: a design that reuses an existing seam states the seam's trigger conditions and the environments in which it runs.

### M9. The stdlib pack depends on the platform it is generated on (id 17)

- **Where:** [packs] first bullet ("inspect per Python minor version for the stdlib"); [current] ("All were measured ... without importing them").
- **What is wrong:** `inspect` imports modules, and what it finds depends on the platform. On this Windows node, `socketserver.ForkingMixIn` and `UnixStreamServer` are absent, and pwd, curses and fcntl fail to import. The pack header (kit, version range, generator) has no platform key. The stdlib sizing (1,270 rows) used `importlib`, so the "without importing" claim is false for that row.
- **Consequence:** The committed pack churns with whichever node regenerated it. Adopter subclasses of Unix-only bases grade as debt or as forced depending on that node, which breaks "every node grades the same".
- **Fix:** The skeptic judged this fix sound.
  - Add the platform to the pack header and key, or generate the pack from typeshed stubs by AST.
  - Regenerate on two OSes and diff the bytes.
  - Correct the [current] sentence.
- **Left-shift gate:** Add a pack-generation selftest that regenerates on two platforms and requires byte identity, or a platform key in the header.

### M10. A name that is proposed as a vocabulary change has no route while pending or after a no (id 22)

- **Where:** [vocabulary] second bullet, with [enforcement] item 2 (L-2 refuse).
- **What is wrong:** A name that will not fit may be "proposed as a vocabulary change", but only the owner's yes has a route. An agent cannot pass `instructions.proof`. So under the default `at-commit=refuse`, a commit carrying a pending name has no route, especially in an unattended run. The design also gives no outcome for a rejected proposal.
- **Consequence:** Work stalls, or the agent uses the `--no-verify` bypass that the pre-commit hook advertises. The bar then reds, and no one owns the fix.
- **Fix:** The skeptic rejected the finder's fix. Its corrected fix:
  - While the proposal is pending, route the unit as a fork under `design.forks`. The unit is parked, or built under a conforming name.
  - On the owner's no, the proposal record routes a rename to the unit that added the name.
  - State that an unattended run under refuse either picks a conforming name or parks the unit.
- **Left-shift gate:** Make this a checklist entry for the class owner-item-without-its-reject-outcome: every owner-gated item states its pending outcome and its rejected outcome.

### M11. Contract declarations claim existing readers and a write path that neither exist (ids 23, 35)

- **Where:** [forced] item 2; [integration] third bullet; [vocabulary] first bullet.
- **What is wrong:**
  - "The marker family's existing readers" do not exist. Each `gov:` gate reads only its own marker, and no reader maps a marker to "a name read by name".
  - The "stale arm" match rule is unspecified, although agent-cap.js matches names by regex, for example `/\b(chunk|splitInto)\s*\(/`.
  - A code comment is written by an ordinary commit, outside `instructions.edit`.
  - ".lexicon.conf already says the constraint belongs there" misattributes the conf, which says the tension is "still the owner's to settle".
  - The open ask TOOL-aKeyedAnnotation-5 (the `gov:` vocabulary is unclosed) is not cited.
- **Consequence:** The stale arm is a new check presented as reuse. A misspelled declaration is silent. The write-path claim cannot be enforced as written. The high-severity self-exemption consequence is item H2.
- **Fix:** The skeptic judged both fixes sound.
  - Name the reader the declarations extend: the memory round's annotation grammar over the comment lexer (map_lib.py:647), built by dTotalRecall. The declaration marker joins its closed vocabulary (TOOL-aKeyedAnnotation-5).
  - Either keep declarations in an instruction-layer manifest whose rows point at the reader file, or name the check that refuses a marker added outside the write path.
  - Specify the stale arm: the declared name must occur literally in the reader's matching code, and a staged break that removes it must red.
  - Correct the conf attribution.
- **Left-shift gate:** Add a checklist entry: a design that says it reuses "existing readers" names the reader's symbol and file.

### M12. The commit check is not move-aware, so `git mv` of a file with inherited debt is refused (id 24)

- **Where:** [design] [enforcement] item 2 (at commit).
- **What is wrong:** The commit check grades "the definitions a commit adds or renames, in its staged files", and exempts only merge commits. Move-aware keys are required only at the bar.
- **Consequence:** Under refuse, moving a graded file that carries debt is refused until every inherited offender in it is renamed, or the commit is bypassed. Dispatch 27 measured 5 such moves in 1,897 commits.
- **Fix:** The skeptic judged this fix sound. Key against HEAD's definitions with rename detection (`git diff --cached -M`). Add a fixture in which a `git mv` of a file holding an offender commits clean.
- **Left-shift gate:** Add a checklist entry: every by-key comparison states its move handling at every enforcement point, not only one.

### M13. The JavaScript reader cannot supply the class context that forced resolution needs (id 26)

- **Where:** [forced] items 1 and 3; [packs] JavaScript packs; [integration] second bullet.
- **What is wrong:** The js-regex reader is a probe and is incomplete by construction. It extracts only top-level functions and arrow consts, with no methods and no class context. The conf refuses a decorator selector on a probe language. Only ts-tokens and tsx-tokens are real parsers.
- **Consequence:** `.js` files cannot carry the base resolution or the override verification the forced rule needs. The JavaScript packs are an extension point the shipped reader cannot fill without a new parser.
- **Fix:** The skeptic judged this fix sound.
  - State that verified resolution needs a parser that emits class methods and their bases.
  - Probe languages get no forced class and are reported as unresolved.
  - Gate the JS packs behind that parser in dMindYourWords' scope.
- **Left-shift gate:** Add a checklist entry: every pack or extension point names the parser capability it needs, checked against the LANGS tier.

### M14. The site suppression designs a new exemption without the existing waiver design (id 31)

- **Where:** [design] [forced] item 4; [gaps-proposed] item 6.
- **What is wrong:** "A site suppression with a reason" gives no key and no relation to the existing waiver registry. Three things go uncited:
  - TOOL-dScaffoldedMirror-4, a deferred spec that re-keys the registries to `path::name` with a mandatory reason;
  - TOOL-aLoosenedCeiling-5, the refusal of `<path>:<line>` keys;
  - `load_waivers` (lexicon.py:2324).
- **Consequence:** A builder may build a second registry, or key sites by line, which re-opens a decided question by omission.
- **Fix:** The skeptic judged this fix sound. Extend `load_waivers` and the waiver files under TOOL-dScaffoldedMirror-4's `path::name` key with a mandatory reason. Cite TOOL-aLoosenedCeiling-5, and bring TOOL-dScaffoldedMirror-4 into dMindYourWords' gaps.
- **Left-shift gate:** Add a reuse-lens checklist entry: a new exemption or registry greps DECISIONS and the backlogs for its mechanism before it is designed.

### M15. The commit check names no seam (id 33)

- **Where:** [design] [enforcement] item 2; [forks] L-2.
- **What is wrong:** The tree already runs staged legs from `.githooks/pre-commit` (`--staged`). v2 gives the derived pre-commit list to dWitnessedBar (gap-test-07). layer-runtime lists "the lexicon's commit check" as a harness hook pack. The record says none of this, and does not say which carrier the check extends or which one `lexicon.at-commit` reads.
- **Consequence:** The check could be built three ways. A hook-pack-only build leaves commits from other harnesses ungraded. A hand-added pre-commit line repeats the hand-named list that gap-test-07 retires.
- **Fix:** The skeptic judged this fix sound.
  - Name the seam: a `--staged` mode on `lexicon.py`, registered in the derived pre-commit list.
  - Say whether Runtime's hook pack wraps that leg or is a second carrier.
  - State which carrier `lexicon.at-commit` reads.
- **Left-shift gate:** Add a checklist entry: every enforcement point names its carrier (a git hook, a harness hook pack or a bar leg).

### M16. Settled answers were folded in, but the superseded text still stands (id 37)

- **Where:** [settled] third bullet and the intro; [design] [packs] "Selection"; [enforcement] item 5; [gaps-proposed].
- **What is wrong:**
  - [settled] still says "dTotalRecall owns the lexicon's work", against L-4, which moved it to dMindYourWords.
  - [packs] Selection describes detection only, against the settled `detected-and-declared` default and custom packs.
  - [enforcement] item 5 and [gaps-proposed] still route the drift signals as Loop Review trends, with seven gaps. They omit gap-lex-08's leg pack at Test's leg-pack point.
- **Consequence:** The record a lexicon builder reads first names the wrong owner and the wrong selection rule, and omits a unit that the build's chain row requires.
- **Fix:** The skeptic judged this fix sound. Add dated revision notes at [settled] (the owner is dMindYourWords, per L-4), at [packs] Selection (detected and declared, with custom packs), and at [enforcement] item 5 and [gaps-proposed] (gap-lex-08, the leg pack, per layer-expansions).
- **Left-shift gate:** Make this a checklist entry for the class amendment-leaves-its-other-half-standing: folding an answer in greps the record for each statement it supersedes.

### M17. The two-sided pin is asserted in many more carriers than [fixes] names (id 39)

- **Where:** [current] Defects bullet 4; [fixes] ("Reconcile the Skill, the conf and the README").
- **What is wrong:** The record says the README already reads "shrink-only". README.md:650 means the waiver registry, and the README's pin text (134, 547, 591) is two-sided, as are the Skill, the engine, the conf, kit.toml's `lexicon-pins` hole, adopt-lexicon.sh and the selftests. Item L9 is the low-graded wording side of the same misreading.
- **Consequence:** A builder who reconciles only three carriers toward a README it believes is already shrink-only misses the engine's pin logic and the adopter-facing hole. The selftest arms AC10 and H2 then red, or get edited ad hoc.
- **Fix:** The skeptic rejected the finder's fix as incomplete. Its corrected fix:
  - Correct [current]: the README calls waivers shrink-only. Its pin text (134, 547, 591), the Skill, the engine, the conf and the waiver headers are all two-sided.
  - In [fixes], list every carrier the shrink-only change moves:
    - lexicon.py 3274, 3326, 3343, 3360 and 4099;
    - README 134, 547 and 591;
    - LEXICON.md:180;
    - SKILL.template.md 53 and 58;
    - kit.toml's `lexicon-pins` hole (190);
    - adopt-lexicon.sh:556;
    - scaffold_lexicon.py 292, 369 and 430;
    - line 2 of both waiver files' headers;
    - .lexicon.conf 55, 88, 454 and 556;
    - selftest AC10 (2071), 2428, 3470 and H2 (4241-4248).
  - Rewrite those selftest arms so that a fall greens and a rise reds.
- **Left-shift gate:** Add a checklist entry: a semantic change to a check lists its carriers from a grep of the old wording, not from memory.

### M18. The pre-push merge-loss refusal is stranded by the extraction inversion (id 40)

- **Where:** [design] [integration] ("The lexicon stops walking the corpus itself"); [current].
- **What is wrong:** `.githooks/pre-push` (923-965) runs `lexicon.py --merge-losses` on every default-branch push (TOOL-aMendedFleet-3). No dClosedLoop design record names it.
- **Consequence:** The inversion either breaks the check, or leaves a lander safety check inside an optional component. Adopters without the lexicon get only a skip line, which conflicts with P28. The failure is loud, but a merge loss would slip.
- **Fix:** The skeptic judged this fix sound.
  - Add `--merge-losses` to [current]'s enforcement points.
  - Home it in the map's extraction or in core memory beside the lander.
  - Add the hook, its tests (pre-push.test.sh:1766, pre-push.runlog.test.sh:1001) and the README section to the touched set.
  - Probe: a lexicon-less adopter fixture still refuses a merge that drops a definition.
- **Left-shift gate:** Add a blast-radius checklist entry: moving a kit's capability greps every hook and leg that invokes the kit's entry point.

### M19. The record never says what a site whose base cannot be resolved statically gets (id 47)

- **Where:** [design] [forced] items 1 and 5; [current] dispatch 29 "What passes".
- **What is wrong:** The record is silent on star imports, dynamic or conditional bases, mixins, and chains through an in-repo intermediate class. It drops the research's rule "Unresolved sites stay graded and are reported", the fixture K4 owes, and the "thin evidence" caveat. The 5-of-5 result was measured on 66 classes with no hard cases.
- **Consequence:** A builder resolves direct bases only, so forced names on adopter class hierarchies are refused at commit. That brings the owner's complaint back. Exempting unresolved sites would instead pass free choices.
- **Fix:** The skeptic judged this fix sound.
  - (a) Resolve transitively through in-corpus classes and the MRO.
  - (b) An unresolved site stays debt, is reported in its own tally, and is never exempted.
  - (c) Build K4's fixture: Django CBV, a React class component, NodeVisitor, a pytest plugin, a bats file, an in-repo intermediate and a star-imported base. It must clear every forced name and no free function of the same name.
  - (d) Run the cross-node byte-identity check.
- **Left-shift gate:** Add a checklist entry: a mechanism validated on a population with no hard cases carries the research's owed fixture into its acceptance.

### M20. Reclassifying existing definitions has no lawful exit under shrink-only (id 49)

- **Where:** [design] [classes] bullet 1; [vocabulary] bullets 2-3; [packs] header.
- **What is wrong:** Some changes reclassify existing definitions: removing a verb row (the record's own planned `init` removal), a pack range that no longer covers an upgraded dependency, or a regenerated pack that drops a row. Under shrink-only, with "no session raises the pin" and a bar that reds on any added offender, no route exists for that rise.
- **Consequence:** Removing `init` alone turns at least 12 conforming definitions (11 shell `init_*` functions and `init_repo`) into debt. A routine framework upgrade does the same at scale. The documented remedies do not apply, so the pin-raise habit returns, or the bar stays red.
- **Fix:** The skeptic judged this fix sound.
  - A vocabulary or pack change carries its debt delta in its write-path record, and that record re-bases the pin and the bar's base set in the same change.
  - An out-of-range dependency is reported, not silently re-graded.
  - Probe: drop the `init` row on a fixture branch, and show the bar's verdict and the pin path.
- **Left-shift gate:** Add a checklist entry: every ratchet names the lawful re-base for changes to its own classifier.

### M21. Pack selection has no defined states for uncovered inputs (id 50)

- **Where:** [design] [packs] "Selection" and header bullet; [forks] L-5 settled.
- **What is wrong:** Selection is silent on four inputs: a detected kit with no pack, a version outside every range, an unknown version (no manifest), and a project that spans several Python minors.
- **Consequence:** Those sites grade as plain debt with no signal. That is the empty-result-as-clean failure that the library round forbids for optional slots. Under refuse, forced names are refused with no hint that a pack was missing.
- **Fix:** The skeptic judged this fix sound.
  - Give selection three states: applied; detected with no pack or no matching range, reported by kit and version; not detected.
  - For an unknown version or a span of minors, apply the union of the covering packs and report the assumption.
- **Left-shift gate:** Add a checklist entry: every lookup against a curated set states its no-match outcome as a reported state.

### M22. The marker rule misstates PEP 698 and reds correct in-repo overrides (id 1)

- **Where:** [design] [forced] item 3 (markers are a fast path).
- **What is wrong:** "An unconfirmed marker reds, as PEP 698 rules" narrows "ancestor" to an outside base that a pack confirms. PEP 698 flags a marker only when no ancestor defines the member. TypeScript's `noImplicitOverride` requires `override` on every override, in-repo bases included.
- **Consequence:** Every correct `@override` or `override` on an in-repo base reds, and is refused under `at-commit=refuse`. A TypeScript adopter using `noImplicitOverride` reds on every subclass of its own classes.
- **Fix:** The skeptic judged this fix sound.
  - A marker exempts nothing on its own. It reds only when no ancestor, in-repo or packed, defines the member.
  - An in-repo override is graded like a free name and is never a marker red.
  - Fixtures: `@override` on an in-repo override does not red, and `@override` with no base anywhere does red.
- **Left-shift gate:** Add a checklist entry: a design that cites an external standard quotes the standard's rule, not the research's paraphrase.

## Low

### L1. The record omits gap-lex-08 and never places the lexicon's bar legs (ids 4, 27, 56)

- **Where:** [gaps-proposed] header; [forks] "What changed elsewhere"; [design] [enforcement] items 3-4; [settled] "The core never depends on it (P28)".
- **What is wrong:**
  - The record stops at gap-lex-07. The expansion round later added gap-lex-08: the two drift signals become the lexicon's own leg pack. No revision note records this.
  - The naming, wiring and selftest legs are core legs in gate-legs.json today, and the record never places them in the lexicon's leg pack.
- **Consequence:** The record misses a gap and a deliverable. The legs could stay core legs that read an optional component. layer-library's rule "each component's own legs install with it" limits that risk.
- **Fix:** The skeptic judged all three fixes sound.
  - Add a dated revision note citing the gap register and layer-expansions.
  - In [enforcement], state that the naming comparison, the pin backstop, the wiring, the selftest and the two drift signals form the lexicon's leg pack at Test's leg-pack point. That pack is absent from the legs manifest when the lexicon is not installed.
- **Left-shift gate:** Add a register-join check: a design record's gap list must equal the gap register's rows for its build.

### L2. The commit check names no cost budget (id 8)

- **Where:** [design] [enforcement] item 2.
- **What is wrong:** The research's losing test (more than 2 s per commit, against a 5.5 s whole-corpus run) was never run, and the record states no budget. The skeptic regraded this low: Runtime already hosts the check as a hook pack, and the by-name comparison at the bar already catches a `--no-verify` commit.
- **Consequence:** The check's cost is unmeasured.
- **Fix:** The skeptic judged this fix sound.
  - State that the check is a Runtime hook-pack fragment with a stated budget.
  - Name `core.bypass` reporting plus the bar comparison as the backstop.
  - Probe: time the staged check over the last 60 days of commits against the budget.
- **Left-shift gate:** Add a checklist entry: every per-commit check states a budget and a timing probe.

### L3. TOOL-aSurfacedLexicon-23 has two homes (ids 10, 44)

- **Where:** [history] ("no chain build counts on them"), against [classes] and [fixes] (the path selector).
- **What is wrong:** [classes] rests on the still-OPEN TOOL-aSurfacedLexicon-23 (memory/backlog/TOOL.md:322), and nothing hands it off to dMindYourWords. The `py.file` and `py.constant` cells stay declared OFF, and no item re-arms them. TOOL-aSurfacedLexicon-15 also has no disposition.
- **Consequence:** A backlog row dangles, the selector could be built twice, and two surfaces stay ungraded.
- **Fix:** The skeptic judged both fixes sound.
  - State that dMindYourWords absorbs TOOL-aSurfacedLexicon-23, and close the row with a pointer, per HYGIENE's ask rules.
  - Re-arm the two cells once the selector excludes `memory/builds/**`.
  - Drop or qualify the [history] sentence.
- **Left-shift gate:** Make this a checklist entry for the class two-answers-to-one-question: every foreign ask id a design leans on carries a hand-off.

### L4. The L-6 bullet misstates what was applied (id 11)

- **Where:** [forks] "Settled after L-1 to L-6", the L-6 bullet.
- **What is wrong:** "L-6 turned the undeclared-extension refusal off" is wrong. Commit 0ac38b016 declared `html` and `svg` dark in LANGS, and the refusal stays armed. This contradicts [now].
- **Consequence:** A later reader may take the refusal arm to be disabled.
- **Fix:** The skeptic judged this fix sound. Reword to: "L-6 declared `html` and `svg` dark in LANGS (`0ac38b016`); the undeclared-extension refusal stays armed."
- **Left-shift gate:** None fits. Record it as a bug-class checklist entry: a settled-answer bullet cites its commit's own message.

### L5. Shrink-only is stated as universal (id 12)

- **Where:** [design] [classes] ("only falls"); [vocabulary] ("No session raises the pin").
- **What is wrong:** [settled] keeps `absorb` (velocity's value) and `no-gate` as allowed values of `lexicon.pin`, but these sentences state shrink-only without qualification.
- **Consequence:** A builder could hard-code shrink-only and drop `absorb` and `no-gate`.
- **Fix:** The skeptic judged this fix sound. Qualify both sentences with "under `lexicon.pin=shrink-only`, the default", and say what `absorb` does to a debt-only pin.
- **Left-shift gate:** Add a checklist entry: every universal claim about a keyed behaviour names the key value it holds under.

### L6. Gap 2's examples drop `get_queryset` (id 13)

- **Where:** [gaps-proposed] item 2.
- **What is wrong:** The `get_queryset` → `read_queryset` example is missing, although [current] and gap-lex-02 both carry it.
- **Consequence:** None beyond the record. The difference is cosmetic.
- **Fix:** The skeptic judged this fix sound. Add the example.
- **Left-shift gate:** The register-join check from L1, extended to example lists.

### L7. "pytest is not installed on this node" is false (id 18)

- **Where:** [design] [forced] item 5.
- **What is wrong:** pytest 9.1.0 sits in the user site-packages. The researcher's probe ran with `-I`, which hides the user site. The lexicon legs run plain `python`.
- **Consequence:** The design is unaffected, because the no-live-import rule stands on determinism. A cross-node test planned on this premise would pick the wrong second environment.
- **Fix:** The skeptic judged this fix sound. Restate the reason: a live import depends on each node's packages and user site. Drop the claim that pytest is not installed.
- **Left-shift gate:** Add a checklist entry: environment claims state the interpreter flags they were probed under, matching the gate's interpreter.

### L8. "Main reads 1,088 against 1,087" is stale (id 19)

- **Where:** [now]; the L-6 bullet; [gaps-proposed] item 3.
- **What is wrong:** c7a9213d1 renamed `clean` to `renderAskQuote` and reached main in ef9c3fbab, so main reads 1,087. Only the branch's merge base, ebce889c7, carries 1,088. That rename drained an offender without raising the pin, which is counter-evidence to gap-lex-03's evidence line.
- **Consequence:** A reader takes main to be red, and gap-lex-03's evidence is stale.
- **Fix:** The skeptic judged this fix sound. Add a dated note, and restate gap-lex-03's evidence as the history of absorbed raises.
- **Left-shift gate:** None fits. Record it as a checklist entry: tree-state claims cite the sha they were read at.

### L9. The README's "shrink-only" is misread as describing the pin (id 20)

- **Where:** [current] Defects, fourth bullet; [fixes] fourth bullet / gap-lex-07.
- **What is wrong:** README.md:650 describes the waiver registry. The README's pin text, LEXICON.md:180 and SKILL.template.md:53 agree with the conf on two-sided equality, so the README-versus-conf conflict the record states does not exist. The carrier-completeness consequence is item M17.
- **Consequence:** The "reconcile" fix chases a conflict that is not there.
- **Fix:** The skeptic rejected the finder's fix. Its corrected fix:
  - Restate the defect: the conf, both waiver headers, LEXICON.md, SKILL.template.md and README.md (134, 547, 591) all describe the pin as a two-sided equality, which the settled `lexicon.pin=shrink-only` retires.
  - Rewrite every one of them with the pin change.
  - Keep README:650's waiver-registry "Shrink-only", which is correct.
- **Left-shift gate:** Covered by M17's grep-the-old-wording entry.

### L10. Three pin seams map onto one "debt-only pin" (id 34)

- **Where:** [design] [classes] bullet 1; [enforcement] item 4; [fixes] fourth bullet.
- **What is wrong:** The kit carries `VERB_OFFENDER_PIN`, `SUFFIX_OFFENDER_PIN` (`PIN_KEYS`, lexicon.py:121) and the per-cell `PINS:` block (.lexicon.conf:515). The record never maps them to the one `lexicon.pin`, and the suffix predicate has no row in the class table. The skeptic found that the claim of a decision overturned does not hold: F4-8 is the source of shrink-only.
- **Consequence:** A builder may add a fourth pin, or merge the three silently. The mapping is derivable.
- **Fix:** The skeptic judged this fix sound.
  - Map each existing pin to its fate under `lexicon.pin`.
  - Give the suffix predicate its place in the class table.
  - Cite TOOL-aSurfacedLexicon-18 as superseded by F4-8's shrink-only setting.
- **Left-shift gate:** Add a checklist entry: a redesigned ratchet maps every existing pin key to its fate.

### L11. The map's `lexicon-verbs` inventory goes unnamed (id 41)

- **Where:** [design] [vocabulary] (the `init` row); [drift] (NOUNS table).
- **What is wrong:** map_extractors.py:243 ratchets a `lexicon-verbs` inventory read from VERBS, and memory/map/features/lexicon.md claims `init`. [integration] names only the tokenizer dependency. NOUNS has no inventory.
- **Consequence:** Removing `init` reds the codebase-map coverage+freshness leg, by design. The cost is a missed touched-set entry.
- **Fix:** The skeptic judged this fix sound.
  - Name both of the map's dependencies on the lexicon: the tokenizers (map_extractors.py:306) and the verb inventory (243-271).
  - State whether the `lexicon-verbs` inventory survives, and whether NOUNS gains a sibling inventory.
  - List the dossier's claim and the coverage+freshness leg in the touched set.
- **Left-shift gate:** Covered by M18's grep-every-invoker entry.

### L12. "Becomes thirteen builds" is stale (id 45)

- **Where:** [forks] "What changed elsewhere".
- **What is wrong:** v2's [chain] now reads fifteen builds.
- **Consequence:** A reader who takes the count from this record is wrong by two.
- **Fix:** The skeptic judged this fix sound. Add a dated note, or reword the bullet as "thirteen at the time".
- **Left-shift gate:** None fits. Record it as a checklist entry: counts of another record's population cite that record, not a number.

### L13. The lexicon legs' `doc_reads` declarations go stale (id 46)

- **Where:** [classes] (records out of scope); [fixes] (the path selector).
- **What is wrong:** Once records leave the graded population, `doc_reads: ["memory/builds/"]` on the naming and wiring legs (gate-legs.json and the kit.toml mirror, 170-176) is stale.
- **Consequence:** Extra leg runs in docs mode, and a stale manifest claim.
- **Fix:** The skeptic judged this fix sound. List both carriers among dMindYourWords' touched carriers, and drop or re-justify them once the selector lands.
- **Left-shift gate:** Add a checklist entry: a change to what a leg reads re-derives that leg's `doc_reads`.

### L14. "Namespaced closed set" is undefined, and custom packs have no load validation (id 55)

- **Where:** [design] [forced] item 1; [forks] L-5 settled (custom packs).
- **What is wrong:** Nothing says what makes a set namespaced. Custom-pack rows have no validation of header, grammar, duplicates or generic tokens. The skeptic regraded this low because a custom pack changes only by the owner's command.
- **Consequence:** A custom pack declaring {run, handle, emit} would exempt by name everywhere, which is the table L-1 rejected.
- **Fix:** The skeptic judged this fix sound.
  - A by-name row must carry a namespace pattern the grammar accepts, and bare generic tokens are refused.
  - Validate every pack at load, and refuse the whole pack with the offending row named.
  - Probe: a custom pack with a bare `run` closed set and a row with no base are both refused.
- **Left-shift gate:** Add a pack-loader selftest with malformed-pack fixtures.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=56 confirmed=49 refuted=7 unverified=0 blocker=0 high=3 medium=29 low=17 agents=11 out-tokens=246830

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [forced] item 3 (markers are a fast path) | high | medium | confirmed | Blob lines 220-222 say markers are 'honoured only where the packs confirm an outside base. An unconfirmed marker reds, as PEP 698 rules.' prior-art.md:37 quotes PEP 698 as an error only 'unless that method is overriding a compatible method … in some ancestor', and :36 says noImplicitOverride requires `override` on every override. The research's own line, :155, narrows 'ancestor' to 'external base', and the record copies that. Packs cover only outside hosts, so a correct @override on an in-repo override is 'unconfirmed' and reds, which with at-commit=refuse refuses the commit. The false red is visible and limited to adopters who use markers on in-repo bases, so the defect is contained: medium. | sound | - |
| 2 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [vocabulary] ('ratified gives way to that path's record') and [classes] (pin counts debt only) | high | medium | confirmed | Re-probed. drift_report.py:1212 reads conf 'ratified', and :1332-1333 returns _build_not_asked when the stamp is empty. drift_signals.py:309 pins lexicon_ratified_older_than_language_surface at 0. v2:947 and :305 make the two lexicon drift signals dMindYourWords' own leg pack, while the record (blob :288) retires `ratified` with no inventory of its readers. kit.toml:178 has the lexicon-ratified hole, and adopt-lexicon.sh:427-433 refuses an empty stamp. scaffold_lexicon.py:269/313 seeds VERB_OFFENDER_PIN from the raw offender count. The result is a leg that turns permanently not-asked, plus stale adopter instructions. That is real and contained: medium. | sound | retirement-inventory-misses-readers-by-value |
| 3 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[forks] L-4 and the settled table (dMindYourWords, a child of dTotalRecall) | high | medium | confirmed | v2 [chain] rows: dMindYourWords has parent dTotalRecall only (:947), and dWitnessedBar (:949) and dWellOiledMachine (:948) are siblings, not ancestors. v2:947's roster registers the lexicon's leg pack 'at Test's leg-pack point'. layer-runtime.md:754 lists 'the lexicon's commit check' as a hook pack, the Runtime extension point. By contrast, dShippedRelease, which fills Test's leg-pack point with the currency leg, does descend from dWitnessedBar. L-4's parentage (blob :382, :407) therefore lets dMindYourWords be scheduled before the points it fills exist. | sound | - |
| 4 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [enforcement] items 3-4 and [settled] 'The core never depends on it (P28)' | medium | low | confirmed | gate-legs.json carries core legs 'lexicon naming predicates', 'lexicon selftest' and 'lexicon wiring'. flow-steps.md:302 names only the two drift signals among the lexicon's leg packs. The record's [enforcement] never places its legs, and [gaps-proposed] (:317) and the change list (:435) stop at gap-lex-07, while the register (:165) and v2:947 carry gap-lex-08. However, layer-library.md:314 already gives the general rule 'Each component's own legs install with it', which limits the risk of the legs staying core. What remains is mostly a stale gap list and an implicit placement: low. | sound | - |
| 5 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [integration] ('The lexicon stops walking the corpus itself, and classifies the map's definitions') | medium | medium | confirmed | Blob :299-300: 'The lexicon stops walking the corpus itself, and classifies the map's definitions.' layer-library.md:115-116 lists the map, recall and the lexicon as separate optional components. Its absence table (:305-311) and :314 cover the core's fallback and the map's own legs, and nowhere state that the lexicon requires the map or what it does without it. A lexicon-without-map install would grade an empty population. | sound | - |
| 6 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [packs] (first wave) against [classes] ('the pin falls by 28 forced') | medium | medium | confirmed | population.md:67 counts unattended.test.sh:9054 `mktemp() { return 1; }` among the 6 third-party-forced names (confirmed in the tree at line 9054), and its K2b test (:178) requires 'All 6 (a) must leave the count' through 'a command list for shell shims'. The record's shell packs (blob :240, :247) are hook functions only (prior-art.md:118: bats setup/teardown, command_not_found_handle, precmd...), and prior-art.md:147 even says 'This tree has 0 shell forced names'. The mktemp shim is therefore uncovered, and 'the pin falls by 28 forced' (:201) cannot be met by the mechanism as written. | sound | - |
| 7 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] (no section) against layer-instruction R-B and v2's dOrderedCharter roster | medium | medium | confirmed | layer-instruction.md:429-430: 'The lexicon, an expansion, adds its vocabulary check at an extension point where it is installed (P28)'. v2:942's dOrderedCharter roster has 'the lexicon's vocabulary added at an extension point'. The blob contains no tag-name item, and v2:947's dMindYourWords roster names no tag check, so the filler is owned by no build. | sound | - |
| 8 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [enforcement] item 2 (at commit) | medium | low | confirmed | Blob :261-263 names no host, budget or bypass for the commit check. layer-runtime.md:754 (a later record) already places it as a hook-pack fragment, which needs a budget. research-lexicon-kit.md left the cost test (>2 s per commit) unrun against a 5.5 s whole-corpus run. The fragment-host part is supplied by the runtime record, and the bar's by-name comparison (item 3) already catches a --no-verify commit by construction. What remains is an unmeasured cost with no stated budget: low. | sound | - |
| 9 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [drift] and settled L-3 (`lexicon.drift=refuse-new`) | medium | medium | confirmed | Blob [drift] :279 says only 'New splits are handled as L-3 says'. [enforcement] items 2-4 (:261-268) grade definitions and offenders against the verb table, and nothing says whether a split is an offender or where it reds. The settled table (:405-406) has independent at-commit and drift keys, and the velocity preset (:426) combines warn with report, but the combinations' semantics are not stated. | sound | - |
| 10 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[history] ('no chain build counts on them') against [classes] and [fixes] (path selector TOOL-aSurfacedLexicon-23) | medium | low | confirmed | Blob :62 says 'no chain build counts on them', yet :195 and :313 rest on the TOOL-aSurfacedLexicon-23 selector. memory/backlog/TOOL.md:322 shows it OPEN, and aSurfacedLexicon/BACKLOG.md:10 says the py.file and py.constant cells are 'declared OFF' pending that selector. No item absorbs the row or re-arms the cells. The effect is a dangling backlog row and two surfaces left ungraded: low. | sound | two-answers-to-one-question |
| 11 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[forks] 'Settled after L-1 to L-6', the L-6 bullet | medium | low | confirmed | git show 0ac38b016: 'declare html and svg dark in the lexicon ... both are declared dark in LANGS'. .lexicon.conf:24 carries html::dark and svg::dark, and the refusal arm itself is untouched. Blob :423 says 'L-6 turned the undeclared-extension refusal off', which contradicts :88 and :395. This is a wording defect. | sound | - |
| 12 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [classes] ('The pin ... only falls') and [vocabulary] ('No session raises the pin') | low | low | confirmed | Blob :29-31 keeps absorb (velocity) and no-gate as allowed values of lexicon.pin, and v2's catalogue row shows velocity=absorb. Yet :199 ('only falls') and :286 ('No session raises the pin') state shrink-only without qualification. This is a wording inconsistency. | sound | - |
| 13 | coherence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[gaps-proposed] item 2 | low | low | confirmed | lexicon.md:327-328 (gaps-proposed item 2) lists do_GET, emit, handle and setUp but leaves out get_queryset. The record's own [current] at :142 and gap-register.md's gap-lex-02 row both carry `get_queryset` to `read_queryset`. The two lists differ only cosmetically. | sound | two-answers-to-one-question |
| 14 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [drift], first bullet (and [fit] row 5, L-3) | high | high | confirmed | canon.py:55-83 has CLUSTERS of synonyms only. load ('read a store into memory'), read and parse are separate clusters with different meanings, and no families table exists. The 'acquire' set is ACQ at research-lexicon-instruments.md:146, a 14-verb set the probe defined for itself. The research's own canon-based measure (population.md:147) finds 6 objects with two spellings of one cluster. The record's 57 rests on the invented family. drift_report.py has load_conf returning parse_conf_text(...), a legitimate layered pair. Under refuse-new, the example family as written would refuse that pair. The false claim that the canon already groups verbs will mislead the builder. | sound | - |
| 15 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [enforcement] item 3 | high | medium | confirmed | run-gates.sh:250 reads ATTR_REV from GATE_ATTRIBUTE. Only .githooks/pre-push:2217 exports it. remote-ci.yml:106 runs run-gates.sh without it. run-gates.sh:4328-4331 says 'IT CHANGES NO EXIT CODE' and 'R IS THE LANDING BASE, never the branch point'. The research (kit.md:197,209) proposes reusing that seam. The record's item 3 says only 'its base's', which names no base and says nothing about CI. The record does require the bar to red on any added offender, which is a new arm, so wrong behaviour depends on how the builder reads it. That makes this a contained but real gap, not a certifying-false check. | sound | - |
| 16 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[current] dispatch 29 'What passes', [classes] last bullet, and [packs] 'Shell hosts' | medium | medium | confirmed | The record's table (:122) counts 6 class-(a) names, including the unattended.test.sh:9054 mktemp shim. Yet :161 says the packs 'cover 5 of 5 third-party-forced names', and :208 says the pin falls by 28 forced names. prior-art.md:140 shows the 5/5 was object.__str__ plus 4 hookspecs, and :93/:147 say the tree has 0 shell forced names. population.md:178's K2b counted mktemp under 'a command list for shell shims'. The [packs] shell host list (:240) is bats/bash/zsh hook functions only, so the shim stays debt. | sound | - |
| 17 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[packs] first bullet ('inspect per Python minor version for the stdlib') and [current] 'All were measured from wheels and .d.ts files without importing them' | medium | medium | confirmed | Re-probed here with python -I, which printed 'win32 False False' for socketserver.ForkingMixIn and UnixStreamServer, and pwd, curses and fcntl failed with ModuleNotFoundError. So inspect-generated stdlib data depends on the platform. The stdlib table probe (instruments.md, around :333-360) uses importlib.import_module, so 'All were measured ... without importing them' (:174) is false for the 1,270-row stdlib row. The header spec at :241-242 (kit, version range, generator) has no platform key. | sound | - |
| 18 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [forced] item 5 | low | low | confirmed | Plain `python -c 'import pytest'` printed 9.1.0 from the user site-packages, and `python -I -c 'import pytest'` printed ModuleNotFoundError. prior-art.md:83 shows the researcher's probe used -I. gate-legs.json:1417 runs lexicon.py under the plain interpreter. The stated reason, 'not installed on this node', is false, but the no-live-import rule stands on determinism. | sound | - |
| 19 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[now] 'Main carries a lexicon red of its own', [Settled after L-1 to L-6] L-6 bullet, and [gaps-proposed] item 3 | low | low | confirmed | git show main:tools/unattended/gate-guard.js line 689 is now `const renderAskQuote = ...`. git log ebce889c7..main shows c7a9213d1, whose message says `--measure` now reads 1087, the pin. main's .lexicon.conf:268 holds 1087. The first-parent log shows ef9c3fbab merged it. The merge base is ebce889c7. The record's [now], its L-6 bullet and gaps-proposed item 3 ('main reads 1,088 against 1,087') are stale against the tree. | sound | - |
| 20 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[current] Defects, fourth bullet, and [fixes] fourth bullet / gap-lex-07 | low | low | confirmed | README.md:644-650 sits under '## Waivers', and its 'Shrink-only.' describes the waiver registry. README.md:134 itself says 'Every pin is a TWO-SIDED equality', and LEXICON.md:180 and SKILL.template.md:53 agree. The README-versus-conf disagreement the record states does not exist. The real mismatch is between all the docs and the settled shrink-only pin. | unsound | - |
| 21 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[packs] Selection | low | - | refuted | The premise is false on re-probe. tools/lexicon/lexicon.py:425-450 (_python_defs) collects imports from ast.Import and ast.ImportFrom ('Definitions and imports from a real parse'), and PATTERN_SETS has an 'imports' part for JS (:149, :2189). The lexicon's extractor does collect imports per file today, so 'the import census the extractor already makes' is not shown false. | unsound | - |
| 22 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[vocabulary] second bullet, with [enforcement] item 2 (L-2 refuse) | medium | medium | confirmed | lexicon.md:286-287 gives only 'renamed, shown to be forced, or proposed as a vocabulary change'. It gives no outcome for a proposal that is pending or rejected, and nothing about the commit under lexicon.at-commit=refuse. layer-instruction.md:555-557 says an agent cannot pass instructions.proof and only proposes through the flow. The flow's general fork routing exists, but the lexicon record never connects the refused commit to it. | unsound | owner-item-without-its-reject-outcome |
| 23 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[forced] item 2 and [vocabulary] first bullet | medium | medium | confirmed | agent-cap.js matches the names by regex (:632 /\bchunk\s*\(.../, :925 /\b(chunk\|splitInto)\s*\(/), so a 'stale arm' needs a specified match rule. Research K3 (population.md) notes text-keyed matching would also exempt the record copy. .lexicon.conf:177-178 says the tension is 'still the owner's to settle'. No line says the constraint belongs beside the reader, so the attribution in [forced] item 2 is wrong. A gov: comment in a code file is written by an ordinary commit, and the record gives no check tying it to the instructions.edit path that [vocabulary] claims. | sound | - |
| 24 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [enforcement] item 2 (at commit) | medium | medium | confirmed | lexicon.md:261-263 grades 'the definitions a commit adds or renames, in its staged files' and exempts only merge commits. Move-awareness is required only at the bar (:266). research-lexicon-kit.md:197-199 names the false-new-on-move risk (5 renames of graded files in 1,897 commits). The commit arm as written says nothing about moves, so a git mv of a file carrying inherited debt can be refused under the default refuse. The effect is contained and rare. | sound | - |
| 25 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [integration] first two bullets | medium | - | refuted | duplicate of id=28. I re-read lexicon.md:299-302 ('The lexicon stops walking the corpus itself, and classifies the map's definitions') and layer-library.md:115-117 and :300-311. The claim is true: the absence table has map rows and lexicon rows, and no row for the lexicon installed without the map. But id=28 makes the same claim, adds the standing decisions and check_self_containment, and asks for the same absence row. | sound | - |
| 26 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[forced] items 1 and 3, [packs] JavaScript packs, and [integration] second bullet | medium | medium | confirmed | lexicon.py:117 maps js to ('js-regex','probe'). The js-regex set at :143-153 has only top-level function and arrow-const patterns plus a class-name pattern. It has no method pattern and no class context. .lexicon.conf:48-49 says a regex set 'is a `probe` and stays incomplete BY CONSTRUCTION', and LANGS declares js:js-regex:probe. The JS layer in map_extractors.py:369-370 uses enumerate_exports plus scan_js_definitions, not a lexicon tokenizer. So [integration]'s 'those tokenizers as its shell and JavaScript parsers' cannot supply the enclosing class or bases that [forced] item 1 requires for .js. The ts-tokens and tsx-tokens parsers exist only for ts and tsx. The effect is contained: React is second-wave and waits on a census. | sound | - |
| 27 | grounding | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[gaps-proposed] header and [Settled after L-1 to L-6] 'What changed elsewhere' | low | low | confirmed | The gap register at :165 holds gap-lex-08. architecture-v2.md:947 has dMindYourWords own 'the two lexicon drift signals as the lexicon's own leg pack' with gap-lex-08. layer-expansions.md:195-196 routes the signals to dMindYourWords. The lexicon record says only 'gap-lex-01 to gap-lex-07' at :317 and :435, and grep finds no leg pack or drift-signal mention and no revision note. | sound | - |
| 28 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [integration], first and second bullets | high | medium | confirmed | [integration] makes the lexicon classify the map's definitions, and L-4 at :382-383 says dTotalRecall 'supplies the map's extraction it classifies'. The tree contradicts this. DECISIONS.md:79 (TOOL-dClosedLexicon-12) says 'Coupling an opt-in kit to one that is not was REFUSED'. DECISIONS.md:184 (TOOL-aSurfacedLexicon-20) makes check_self_containment the compensating check. Its docstring at lexicon.py:2359-2367 says 'this kit must install without its neighbours'. tools/lexicon/kit.toml has no requires line, while codebase-map's kit.toml:7 has requires = ["memory-tree"]. grep over the dClosedLoop records finds no citation of self-containment or of either decision. Layer-library's absence table has no 'lexicon without map' row. The check would red at once rather than silently, so I grade the consequence medium. | sound | - |
| 29 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [drift], first bullet; [forks] L-3 | high | high | confirmed | canon.py:55-76 CLUSTERS lists load, read and parse as three separate representatives, and no 'acquire' family or any family layer exists. grep for acquire in canon.py and .lexicon.conf matches only an unrelated prose word at .lexicon.conf:321. The 57 figure comes from the ad-hoc ACQ set at research-lexicon-instruments.md:146. research-lexicon-population.md:147 counts only 6 same-cluster splits. 'create (build, make, new)' does match the build cluster, but the acquire example is false. TOOL-dScaffoldedMirror-12 (dScaffoldedMirror BACKLOG.md:16) records four disqualifying precision gaps for exactly this object-keyed instrument, and the record cites it 0 times. The false claim that the canon already groups verbs this way will mislead the builder. | unsound | - |
| 30 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [vocabulary], third bullet | high | medium | confirmed | [vocabulary] retires `ratified` without naming any consumer. I confirmed three. drift_report.py:1315-1333 signal_lexicon_ratified_stale returns not-asked when the stamp is absent. adopt-lexicon.sh:424-433 (S10) fails on an empty stamp. kit.toml:177-182 holds the lexicon-ratified hole with blocks_gate = true. layer-expansions.md:195-196 and v2:947 put this signal into the lexicon's leg pack. Built as written, that leg goes permanently not-asked and S10 refuses. The not-asked state is labelled, not green, so I grade medium rather than high. | sound | - |
| 31 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [forced], item 4; [gaps-proposed] item 6 | medium | medium | confirmed | [forced] item 4 at :223-225 names 'a site suppression with a reason', but gives no key and no relation to the existing waiver registry. The tree already has the matching design. spec-dScaffoldedMirror-4.md is DEFERRED, and its goal re-keys the registries to path::name with a mandatory reason. lexicon-verb-waivers.txt:5-6 records why the key is not <path>:<line>, and aRepatriatedFork BACKLOG.md:19 records the closed line-keyed registry, TOOL-aLoosenedCeiling-5. load_waivers sits at lexicon.py:2324. The record cites none of these. | sound | - |
| 32 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [enforcement], item 3 | medium | - | refuted | BY DESIGN: unit-level detail. --merge-losses exists (lexicon.py:4170-4190), and so do render_offender_keys and its --offenders key (:3480). But [enforcement] item 3 names a one-time measurement the chain build performs: replay the merges and count the reds from moved files. Which seam that measurement reuses is unit-spec detail, which this design-only build leaves to dMindYourWords' own specs. --merge-losses also answers a different question, definitions lost by a merge, not offender keys moved, so the claimed duplication is not established. | sound | - |
| 33 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [enforcement], item 2; [forks] L-2 | medium | medium | confirmed | [enforcement] item 2 at :261-263 says only 'At commit ... staged files'. .githooks/pre-commit runs staged legs ('bash "$g" --staged') and has no lexicon line. The later layer-runtime.md:754 lists 'the lexicon's commit check' as a hook pack. Its :531 defines a hook pack as a harness *.fragment.json. gap-test-07 (register :221) covers the hand-named pre-commit list. The lexicon record names no carrier and so leaves the git-hook versus harness-hook question open across records. The bar's by-name comparison backstops a commit the check misses, which contains the effect. | sound | - |
| 34 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [classes], first bullet; [enforcement], item 4; [fixes], fourth bullet | medium | low | confirmed | The kit carries VERB_OFFENDER_PIN and SUFFIX_OFFENDER_PIN (PIN_KEYS at lexicon.py:121) plus the per-cell PINS block. research-lexicon-kit.md:28 and :32 document both. The record speaks of one 'debt-only pin' (:199, :268) and never maps the three to it. The part about a decision being overturned does not hold. The shrink-only default came from the memory round's F4-8 (v2:609, lexicon.md:29), and [fixes] reconciling docs to it re-argues nothing. The remaining gap is a mapping a builder can derive, so its effect is minor. | sound | - |
| 35 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [forced], item 2; [integration], third bullet; [vocabulary], first bullet | medium | medium | confirmed | git grep for gov: markers in tools shows per-gate markers (kit 194, fixed-verifiers 50, bounded-fanout 40 ...), each read by its own gate, for example agent-cap.js FIXED_MARK. No contract-declaration marker or reader exists, and gov:note has no occurrence in tools. So 'the marker family's existing readers' (:303-304) and the stale arm (:218) need a new reader. [vocabulary] routes contract declarations through instructions.edit, but layer-instruction R-I (:548-553) makes that a command over units in kit manifests, not code comments beside a reader. The open ask TOOL-aKeyedAnnotation-5 (the vocabulary is unclosed) applies and goes uncited. | sound | - |
| 36 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[forks] 'Settled after L-1 to L-6' table, row L-1; [design] [forced] | medium | - | refuted | The cited section already says it. The record's own L-1 offer at :359-361 defines both alternative values: by name or verb tables, 'one list per kit, applied everywhere', measured as 53 sites for 1 forced, and by site annotation, 'the author marks each forced name, with a reason'. The settled table at :404 keeps them as allowed values of that offer. How the code routes each value is unit-level detail, which this design-only build leaves to the chain build's specs. | sound | policy-value-with-no-route |
| 37 | reuse | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[settled] (third bullet) and intro paragraph; [design] [packs] 'Selection'; [design] [enforcement] item 5; [gaps-proposed] | medium | medium | confirmed | The file hashes to blob 424d2a7. Line 32 still says '**dTotalRecall owns the lexicon's work**, with gap-mem-10', with no revision note, while line 411 says dMindYourWords takes them. [packs] Selection, lines 251-253, describes detection only ('Asked as L-5'), while the settled table at line 408 sets `detected-and-declared` and allows custom packs. Line 317 stops at gap-lex-07. v2:947's dMindYourWords row ends with 'the two lexicon drift signals as the lexicon's own leg pack, registered at Test's leg-pack point' and lists gap-lex-08. gap-register:165 and layer-expansions:196 both carry gap-lex-08. The record nowhere mentions the leg pack. | sound | amendment-leaves-its-other-half-standing |
| 38 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [vocabulary] ("`ratified` gives way to that path's record") | high | medium | confirmed | drift_report.py:1315 signal_lexicon_ratified_stale reads `ratified` and returns `_build_not_asked(... 'carries no ratified stamp; adopt-lexicon.sh --check owns that')` when the stamp is empty, and its dict carries 'gateable': True. kit.toml:177-183 has the `lexicon-ratified` hole with blocks_gate = true and discharge `adopt-lexicon.sh --check`. git grep -c ratified printed drift_report.py:17, lexicon/selftest.py:28, adopt-lexicon.sh:10 and scaffold_lexicon.py:6, among others. [vocabulary] says only '`ratified` gives way to that path's record' and names none of these consumers, nor what the signal is re-keyed to. layer-expansions:194-196 makes that signal part of the lexicon's leg pack. Graded medium rather than high: the retired stamp turns the signal into an explicit not-asked result, which is printed rather than a silent green, so the effect is contained. | sound | - |
| 39 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[current] Defects bullet 4, and [fixes] "Reconcile the Skill, the conf and the README" | medium | medium | confirmed | [current] line 116 says the README says 'shrink-only'. README.md:650's 'Shrink-only.' sits under the waivers text, while README.md:134 reads '**Every pin is a TWO-SIDED equality.**' (also 547 and 591). Two-sided pin text also appears in SKILL.template.md:53 and 58, lexicon.py:3274, 3326, 3343 and 4099, kit.toml:190 (the lexicon-pins hole), adopt-lexicon.sh:556, and selftest.py:2071 (AC10) and 4247-4248 (H2, asserting 'TWO-SIDED EQUALITY' in the template). Research G10 (research-lexicon-kit.md:191) scopes the README's word to waivers. The [fixes] line names only the Skill, the conf and the README. The fix is unsound because its own carrier list repeats the defect: it is incomplete. | unsound | - |
| 40 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [integration] ("The lexicon stops walking the corpus itself") and [current] | high | medium | confirmed | .githooks/pre-push:923-965 resolves the lexicon kit's lexicon.py (resolve_kit_dir ... lexicon lexicon.py) and runs `--merge-losses "$main_remote..$main_local"`, refusing as `merge-loss`. A grep for merge-loss over the dClosedLoop build records finds it only in the research return (research-lexicon-kit.md), never in the lexicon record or any layer record. [integration] says 'The lexicon stops walking the corpus itself' without giving this extractor-dependent lander check a home. Graded medium: the hook's failure modes print 'did NOT run' or DEAD PROBE and allow the push, so a broken check is loud, though a merge loss would then slip. | sound | - |
| 41 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [vocabulary] (`init` row "re-justified as vocabulary or removed") and [drift] (NOUNS table) | medium | low | confirmed | map_extractors.py:243 declares "lexicon-verbs": lambda: _read_lexicon_verbs(), which reads VERBS through lexicon_conf.load_conf and falls to [] on any exception (lines 247-273). The comment says a dossier still describing a verb VERBS no longer carries reds. memory/map/features/lexicon.md:36 lists "init". [integration] names only the tokenizer dependency (line 36 cites map_extractors.py:306). Graded low: the dossier ratchet is designed to red on removal and surfaces the change, an unparseable conf also surfaces through that ratchet rather than silently, and the effect is a missed touched-set entry and an incomplete dependency statement. | sound | - |
| 42 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [integration] ("Today's dependency inverts") | medium | medium | confirmed | grep for `requires` printed only tools/codebase-map/kit.toml:7 requires = ["memory-tree"]; the lexicon kit.toml declares none. gate-legs.json shows the 'codebase-map kit selftest' guard ['{prefix}/codebase-map/', '{prefix}/lib/', '{prefix}/lexicon/'] and the 'lexicon selftest' guard ['{prefix}/lexicon/']. layer-library's absence table (lines 299-311) covers the map absent and the lexicon absent separately, never a lexicon installed without the map. The lexicon record's [integration] makes the lexicon classify the map's definitions without stating that dependency or its absent behaviour. | sound | - |
| 43 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[gaps-proposed], [design] [enforcement] and [integration] | medium | - | refuted | duplicate of id=37. Its headline, that [gaps-proposed] stops at gap-lex-07 and no design section carries the lexicon's leg pack (gap-lex-08, layer-expansions:196, gap-register:165), is the same defect id=37 confirms. The residual about lexicon_marginal_offense_rate is accurate: drift_report.py:1434ff computes OFFENDER by the leading token outside the table. But it is a report-only reading that the record nowhere names as the Loop Review's debt source. | sound | - |
| 44 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[history] ("no chain build counts on them") against [classes] (out of scope, "found by a path selector (TOOL-aSurfacedLexicon-23)") | low | low | confirmed | Record line 62 says 'no chain build counts on them', while line 195 names TOOL-aSurfacedLexicon-23 as the out-of-scope class's path selector. memory/backlog/TOOL.md:322 shows TOOL-aSurfacedLexicon-23 OPEN, and no record outside dClosedLoop hands it to dMindYourWords. The result is two homes for one deliverable, and the effect is on record bookkeeping only. | sound | - |
| 45 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[forks] "What changed elsewhere" ("The chain gains dMindYourWords and becomes thirteen builds") | low | low | confirmed | Record line 432 reads 'The chain gains dMindYourWords and becomes thirteen builds'. architecture-v2.md:938 reads '## [chain] The chain: fifteen builds, final rosters'. A later record changed the count, and this record carries no note of it. | sound | - |
| 46 | blast-radius | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[classes] (records out of scope) and [fixes] ("Keep records out of the graded population with the path selector") | low | low | confirmed | gate-legs.json shows 'lexicon naming predicates' and 'lexicon wiring' each with doc_reads ['memory/builds/'], and the lexicon kit.toml mirrors doc_reads = ["{memory_root}/builds/"] on both legs (lines 170-176). [classes] and [fixes] take records out of the graded population, but name neither carrier. Graded low: the effect is extra leg runs in docs mode and a stale manifest claim. | sound | - |
| 47 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [forced] item 1 and item 5; [current] dispatch 29 'What passes' | high | medium | confirmed | research-lexicon-prior-art.md:74 shows 'LOCAL-inherited offenders: (none)     UNRESOLVED bases: Counter()'. Line 76 shows only 66 classes. K4 (around line 140) states 'Unresolved sites stay graded and are reported', calls the cross-node run 'the test the build must run', and says 'the build owes a fixture'. A grep for unresolv, fixture, transitiv and mro in the lexicon record matches only an unrelated 'fixture' in [classes]. [forced] item 1 says only 'resolves ... to the base' and does not address transitivity through in-corpus intermediates. The record also presents '5 of 5, exempt no free choice' without the research's 'thin evidence' caveat. Partly mitigated: [classes] makes everything else debt, so unresolved sites are graded, though not tallied. Graded medium, not high: the failure falls on adopter class hierarchies and refuses forced names (a visible red), not a silent pass. | sound | - |
| 48 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [vocabulary] bullet 1 against [forced] items 2 and 4 | high | high | confirmed | Record lines 283-285 say the contract declarations change only through the instruction write path (`instructions.edit`: owner commands, agents propose). Lines 216-218 put those declarations in the `gov:` marker family beside the reader in source. Lines 223-225 make a reasoned site suppression 'the owner's fallback'. layer-instruction.md:673-676 scopes instructions.edit to edits to an instruction's 'respective manifest'. A grep for suppression, contract declaration and marker family across layer-instruction, layer-runtime, v2 and layer-library found no guard on inline source markers. Built as written, an agent's own diff can add a declaration or a suppression and clear its debt past the at-commit refuse and the bar's by-name comparison. That is the self-applied stamp the record says it ends. | sound | - |
| 49 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [classes] bullet 1, [vocabulary] bullets 2-3, [packs] header | high | medium | confirmed | Read [vocabulary] at the pinned blob (hash-object printed 424d2a7…). It says 'The `init` verb row … is re-justified as vocabulary or removed'. It also says 'No session raises the pin', and [enforcement] item 3 has the bar 'red on any offender the branch adds'. No section says what happens to the debt count, or to the base set the bar compares against, when a vocabulary change or a pack range reclassifies existing definitions. Re-probed: git grep lists init_* shell definitions at .githooks/straggler-guard.sh:194, tools/unattended/unattended.sh:266 and :3127, plus many in *.test.sh files, and def init_repo at migrate_backlog.py:2731. .lexicon.conf:574 holds the init row. So removing the row would turn real definitions into debt. Graded medium, not high: the change goes through the owner's write path and its effect is a red bar, which is contained. | sound | - |
| 50 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [packs] 'Selection' and header bullet; [forks] L-5 settled | medium | medium | confirmed | [packs] gives each pack 'its version range' and says detection uses manifests 'where they exist'. It says nothing about a detected kit with no pack, a version outside every range, an unknown version, or several Python minors at once. [forced] item 4 offers only a manual site suppression 'for a host no pack covers'. The library round requires absence never to read as clean (layer-library.md, the [consult] three-state paragraph), and this record does not apply that to pack selection. | sound | - |
| 51 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [enforcement] item 2 (at commit) | medium | - | refuted | BY DESIGN: the build is design-only, and unit-level implementation detail is left to the chain build's own specs. Reading index blobs, partially staged files, parse-error reporting, rename detection, amend and rebase handling are all that kind of detail. The record already scopes the check to 'its staged files', which is the index. Runtime [extend] (layer-runtime.md:754) already requires every hook pack to declare its failure mode and budget when it registers, so dMindYourWords inherits that obligation. The claim that the build would grade the working tree is speculation the record does not support. | sound | - |
| 52 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [integration] bullets 1-2 | medium | medium | confirmed | [integration] says 'The lexicon stops walking the corpus itself, and classifies the map's definitions'. layer-memory.md:77 and v2 make the map and the lexicon separately optional components. The library's absent-component table (layer-library.md:300-312) has rows for an absent map and rows for an absent lexicon, but none for a lexicon installed without the map. Neither this record nor any sibling states the dependency or the fallback. A stale map index is also not addressed for the lexicon. | sound | - |
| 53 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[forks] 'Settled after L-1 to L-6' and 'What changed elsewhere' | medium | - | refuted | Premise false on re-probe. v2 states the class rule: architecture-v2.md:264 says 'policy.on-missing-expansion covers an absent optional component too', and :302 says 'a key an absent expansion owns is unread, so no preset is refused for it'. The catalogue row at :647 says the same, and P28 governs optional components as it governs expansions. So a lexicon-less adopter's preset carrying lexicon.at-commit is neither refused nor an unknown-key error. The library also says 'Each component's own legs install with it', and layer-expansions.md:196-197 says the drift leg pack gates 'only where the lexicon is installed'. The finder's impact does not follow. | sound | - |
| 54 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [drift] bullets 1-2; [forks] L-3 | medium | medium | confirmed | [drift] says 'A new definition over an object that already has an established verb in that family must use it', and L-3 sets the default to refuse-new. The record never defines 'object' or 'established verb'. Its own census (lexicon.md:146-149) finds 57 objects with two or more acquire-family verbs (conf: load 11, read 3, parse 2), for which no single established verb exists. Nothing says whether forced names count toward the drift rule or the noun canon. As written the rule cannot be tested. | sound | - |
| 55 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[design] [forced] item 1 ('A namespaced closed set applies by name'); [forks] L-5 settled, custom packs | medium | low | confirmed | [forced] item 1 says 'A namespaced closed set applies by name', but never says what makes a set namespaced. The custom-pack rule in [forks] ('a row applies only where the code resolves to its base or host') gives no way to resolve to a host namespace. The gap is real but contained: a custom pack changes only through the instruction write path, by the owner's command, so a generic closed set needs the owner's approval. Pack load validation is unit-level detail. Graded low. | sound | - |
| 56 | failure-envelope | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md:[gaps-proposed] header and [forks] 'What changed elsewhere' | low | low | confirmed | grep finds gap-lex-08 at gap-register.md:165, layer-expansions.md:196 and architecture-v2.md:307 and :947, and nowhere in the lexicon record. The record's [gaps-proposed] says 'gap-lex-01 to gap-lex-07', and 'What changed elsewhere' says the same. Neither carries a dated note about the drift-signal leg pack the expansion round assigned to dMindYourWords. v2's chain row does carry it, so the effect is mainly a stale record. | sound | - |
