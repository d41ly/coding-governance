**Serves:** research TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32

# dDeclaredLoop — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns for the re-ground brief [`2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground`](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md), extracted by script from each agent's transcript and not retyped. The cross-check record it folds is [`2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck`](2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck.md); each group's handoff sits beside the brief.

## Group A, led by spec 32 (specs 32 and 20)

I revised TOOL-dDeclaredLoop-32 and TOOL-dDeclaredLoop-20, both now at rev-4, and refused no row. I re-read both sides of every row against today's text. Neither file was changed by commit `740e19214` (the owner's fork picks), so no fork pick settled any of these rows.

**Checks:** `wc -c` is 35888 for dl32 and 32672 for dl20, both under 49152. Each Status line moves to `rev-4 · 2026-11-05` with every other field kept, and each §9 has one new rev-4 line naming the brief. I ran the memory hygiene gate with `--staged` over a copy of the index holding only these two specs, then deleted the copy. It names neither spec. Its only finding is check 9: `memory/builds/dDeclaredLoop/README.md` is stale until `gen_build_index.py --write` re-renders it. That belongs to the main loop, so I left it. The `dl30` file shown as modified in the tree is Group B's, not mine.

**TOOL-dDeclaredLoop-32**
- **Row 28, §4:** the predicate paragraph now says the second test (non-decrease) only runs when `no-fall` is unset, and that the first test reads the target, which defaults to the count. It also says that with arguments 4 to 6 unset the function behaves as dl21 leaves it. This replaces "byte-for-byte".
- **Row 29:** the asks sentence now reads "A closing-review loop's", and the Rollout says "every closing-review and fix-pass subject". I also changed two other places that make the same claim:
  - S4's "because a review loop's findings…" now says closing-review.
  - The target table's "review" rows now read "closing review".
- **Row 30, S6 and the §4 Check 2 paragraph:** the reading is now named as check 2's stalled-loop arm and its `flat` reading, instead of `:842` and `:822-870`. The code is at `check-unattended.sh:1008` and :1058-1059, and the name comes from :857. That reading now counts only build-slug rows (the awk's own `slug` variable) and `fix-pass` rows.
  - AC7 gains a plant: a spec subject that is flat and has no exit token stays green, while the same rows on the build slug go red.
  - The `check-unattended.test.sh` New arm line now names that plant too.
- **Row 31:** the edge to dl20 now says `review.trigger` refuses only a build-slug round past `flow.route-backs`, and that a spec subject's target is always ` · to units`.
- **Row 27:** I dropped "the `roundLimit` it passes" from the dl21 edge. A new non-goal says no dDeclaredLoop unit takes up the `roundLimit`/`roundState` edge in TOOL-dFairHearing-17 §3, and that the edge is reported to dFairHearing.

**TOOL-dDeclaredLoop-20**
- **(a)** In the dispose row, NON-CONVERGENT or CEILING now goes by budget only on built work. A spec subject's new mechanism is promoted by dl32's target, which is always units. The dl32 edge says the same.
- **(b)** S8, the fold row and AC1 now name BOUNDED or CEILING, the spec subject's end states, instead of NON-CONVERGENT. AC1 now also fails if the fold row keeps a NON-CONVERGENT route.
- **(c)** The trigger row and the dl32 edge now refuse a round past `flow.route-backs` on the build slug only.
- **(d)** The note under §3 and §4's table supports declaring the routes on the row, so I added them there as declared and not yet active: a plan revision goes to `plan.record`, and a landing record goes to its patch-build intakes. The targets come from the `review.dispose` row in flow-steps.md.

**Left unedited, for the main loop**
- dl20 S5 and "The unverified route" still count a `block` verification round against `flow.route-backs` for every subject. Saying what bounds it on a spec subject would change what the unit builds, and no item covers it.
- dl32 §4 "The target" still cites `check-unattended.sh:845-848` for the disposition-as-last-field read. It now sits at about :1028-1033. No item covers it.
- S6 extends check 2's stalled-loop arm to `fix-pass` rows, as row 30 directs. Today the awk matches only `review` rows (:984), so the builder will widen that match.

Files:
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-32.md
- C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-20.md

## Group B, led by spec 30 (specs 30, 31 and 21)

I revised all three Group B specs (dl30, dl31 and dl21). Every row in the brief was borne out by today's text, and none of the 2026-11-05 fork picks had already settled one, so I refused none. The memory hygiene gate names nothing of mine except the index render the main loop owns.

**TOOL-dDeclaredLoop-30: revised to rev-4** (29345 bytes)
- **Row 17, §3 non-goal:** dl32's strict-decrease routing now covers only closing-review follow-ups under `review.follow-up`'s `while-*` value and fix passes. A spec audit's stop and disposal are named as BUILD-METHOD M4's spec-audit rule's.
- **Row 18, S6:** the per-item early limit ends only follow-up, fix-pass and route-back items. A spec subject's `review-round` draws are counted but never end its loop (dl32 S2, S3).
- **Row 19, S4 and "The driver, in shell":** a spec subject's `review-round` draw is still made and spends the budget while any remains. An `exhausted` answer does not refuse its round: `verb_review` reads the exit 3 and records the round anyway. A spec subject means any subject other than the build slug (dl21 S3).
- **Row 19, AC7:** gains the plant `spent-spec-round`. With the budget spent, the spec subject's second round is recorded with no new `draw` row, and the build slug's second round is refused naming `flow.on-exhausted`. Its `Red when:` gains the case where the spec round is refused.

**TOOL-dDeclaredLoop-31: revised to rev-3** (30128 bytes)
- **Row 22, §3 non-goal:** follow-up and fix-pass loops are dl32's; a spec audit's end and disposal are M4's spec-audit rule's. The ` · to on-exhausted` sentence keeps its meaning. I changed its "Its" to "The routing's" because the new clause would otherwise make "Its" point at M4.
- **Beyond the row, for you to keep or drop:** S5, §4 "The lap refusal" and AC2 said every review round is refused once the budget is spent. That now contradicts dl30 S4 as revised under row 19. I added a spec-subject exception that points to dl30 S4, and AC2's `--review` round now names the build slug. What dl31 builds is unchanged, because the refusal is dl30's. The §9 line names all three edits.

**TOOL-dDeclaredLoop-21: revised to rev-4** (32652 bytes)
- **Row 5, S3:** the parity arm sets its ceiling variable to each row's limit. That puts the driver's ceiling one round past the limit, as dFairHearing-17 §4 "The rule" does for the harness, so the limit-4 row reads `BOUNDED` in both. I left the variable unnamed there: naming `MAX_ROUNDS` made hygiene check 25 red, since no tracked reader spells it.
- **Row 7, §3 non-goal and the dl32 edge line:** the `roundLimit` claim is dropped from both.
- **Row 10, §4 "The bounds":** the non-decrease reading applies to the closing review only. A spec audit passes `no-fall` (dl32 S3) and ends `CONVERGED`, `BOUNDED` or `CEILING`, never `NON-CONVERGENT`.
- **Row 11, §3 non-goal:** follow-ups and fix passes go to dl32. A spec audit's disposal is M4's spec-audit rule's, applied through dl20's `item.review.dispose` row; I checked that row's text in the current dl20.
- **Row 14, S4 and F4:** the readers list now has `BUILD-METHOD.template.md` :144 and :148, the latter being M4's chain paragraph. S4 rewords :148 from "so `REVIEW_ROUNDS` bounds no chain" to "so no round bound bounds a chain", which names no key and is shorter, so it should not strain the `build-method size` gate. F4's grant line says that paragraph names no key.

**Checks**
- Each Status line carries the new rev and `2026-11-05` with every other field kept, and each §9 has one new line ending `by the brief prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md`.
- `check-memory-hygiene.sh --staged` ran over a copied index with only these three specs staged; the copy is deleted. The only finding left is check 9: `memory/builds/dDeclaredLoop/README.md` is stale until `python tools/memory-tree/gen_build_index.py --write` runs. That is yours.
- I edited no file outside these three specs, staged nothing in the real index and made no commit. The dl20 and dl32 diffs in the working tree are Group A's.

**For the dl21 build pass:** template :144 still says "A SPEC subject takes `REVIEW_ROUNDS` rounds … and exits BOUNDED". When S4 rewords it to the policy keys, it should say a spec subject ends at its target or its bound, to agree with dl32 S3. I did not add this, because no brief item states it.

Files:
- C:/projects/coding-governance/.claude/worktrees/vigilant-einstein-2d0f7d/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-30.md
- C:/projects/coding-governance/.claude/worktrees/vigilant-einstein-2d0f7d/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-31.md
- C:/projects/coding-governance/.claude/worktrees/vigilant-einstein-2d0f7d/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-21.md
