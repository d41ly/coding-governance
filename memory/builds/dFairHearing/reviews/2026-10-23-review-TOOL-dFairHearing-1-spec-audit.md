**Serves:** spec-audit TOOL-dFairHearing-1@rev-2 TOOL-dFairHearing-2@rev-1 TOOL-dFairHearing-3@rev-1 TOOL-dFairHearing-4@rev-1 TOOL-dFairHearing-5@rev-1 TOOL-dFairHearing-6@rev-1 TOOL-dFairHearing-7@rev-1 TOOL-dFairHearing-8@rev-1 TOOL-dFairHearing-9@rev-1 TOOL-dFairHearing-10@rev-1 TOOL-dFairHearing-11@rev-1 TOOL-dFairHearing-12@rev-1 TOOL-dFairHearing-13@rev-1 TOOL-dFairHearing-14@rev-1 TOOL-dFairHearing-15@rev-1 TOOL-dFairHearing-16@rev-1 TOOL-dFairHearing-17@rev-2 TOOL-dFairHearing-18@rev-1

# Tier-2 spec audit — Build dFairHearing, the 18 committed specs

Provenance: tier2-review harness, kind spec-audit, round 1, five lenses (coherence, grounding, reuse, blast-radius, failure-envelope), skeptic-verified, synthesized 2026-10-23 on branch/unattended-dfairhearing-439b9e. The README and run mandate under memory/builds/dFairHearing/ state the build's purpose.

Reviewed: memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md@1f4598e2008bcdd2ccfc3d0fa5e7787d65252749, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-2.md@4c1cf90aa5bba2a1ecb47ae423f0f33a16e38c4f, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-3.md@4ffc96b9b6d7e911faf4a5ab31b43fc21e3a72ee, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-4.md@0d19057eb7bc3b6b3eee477dffee78b40a5bf0c8, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-5.md@d11cfa78b68dd6507cf503e0882f8e90d25dfd4f, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-6.md@b68f7cb06c5366b9e11827d78f90783838906661, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-7.md@af50412a16388b430ae1469542c8b67077406695, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-8.md@986fd47af5d50d29499a9aa6d73aaf61de7aaab9, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-9.md@3631b1c22924f31ef980b9d921c79fad6cd0c701, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-10.md@d339584bafc66bfede005589e60ab5132ad00697, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-11.md@3dfb4a0ca32cfd8a325b34b93283ff0712482716, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-12.md@47866408520d4b8b7d564dfe96d8d3eba6e94b34, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-13.md@ba8b99fa55783df5328552efcd455a620a09add2, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-14.md@3ba32ca2bbc4a4548b9eb4272c738efbde326fc7, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-15.md@26729e5d248ba4913bf9d1450d6d5fd4d384c8d6, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-16.md@7f19de46ec76d454abf655072a8ba304ac775f8b, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md@a4155dec21d8117cbb4bac941f40b248461f7316, memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md@29d31e1e47990d9f8cde652619433b33ea53cd28

Round: 1

## Verdict: CLEAN WITH FIXES

No blocker survived. Three high items and 28 medium items must be fixed in the specs before their units are built. Many medium items are acceptance criteria that cannot pass on a correct build, or cross-unit contracts that contradict each other.

Review shape: intensity full, raw 53, confirmed 52, refuted 1, unverified 0 (0 uncertain), precision 0.98. Adjudicated tally by item: 43 items (0 blocker, 3 high, 28 medium, 12 low). By raw confirmed finding: 52 (0 blocker, 3 high, 37 medium, 12 low).

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 12 | 12 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| reuse | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 12 | 12 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 17 | 17 | 0 | 0 | 0 | 1.00 |

### Run integrity

- Lenses 5/5 returned, 0 died. Skeptic batches 5/5 returned, 0 died.
- 0 contradictory verdicts demoted, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 46 judged sound, 6 judged unsound, 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 14 re-graded by the skeptic.
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 1 spec document supplied as `specs`, as sibling context.
- Checklist: none swept. A zero count here is not evidence that the project's recurring bug classes are absent.
- By design: none supplied, no caller byDesign and no block.
- Move check: no checked subject moved.
- The one refuted finding (id 17) was a duplicate of id 19 and is covered by item M1.

## High

### H1 — A walk-table gap reds only the prose, never the counts (id 37)

- **Where:** spec 18, section 4 The gaps; section 2 S4.
- **What:** A gap in the walk table makes the run red only through a synthesis-prompt instruction to write `## Verdict: BLOCKED`. Nothing feeds `walkGaps` into `blockers`, `highs` or spec 17's `roundState`.
- **Consequence:** A gapped walk with no blocker item returns `blockers: 0` and `roundState` CONVERGED beside a non-empty `walkGaps`. Every machine caller that routes on the counts reads it as clean, so the gap check certifies a red it never delivers.
- **Fix (skeptic: sound):** Put the red in the return. With `walkGaps` non-empty, null `blockers`/`highs` or force a non-zero blocker floor, and make `roundState` null or a non-converged value. Add an AC: a stub run with one planted empty cell and no findings returns no count that reads as CONVERGED.
- **Gate:** a harness self-test arm asserting that every BLOCKED condition the prompt names also moves a returned count.

### H2 — The held-out freeze check never compares the bytes it scores (id 39)

- **Where:** spec 14, section 2 S3; section 4 Output order.
- **What:** The freeze is checked only by `git log --format=%H -- <path>` listing one commit, but the cases scored are the working-tree file.
- **Consequence:** An uncommitted edit after the freeze, or a shallow clone, still prints `frozen at <sha>`. A held-out set tuned in the working tree is graded as frozen.
- **Fix (skeptic: sound):** Require `git hash-object <path>` to equal `git rev-parse <freeze>:<path>`, and refuse with exit 2 when `git rev-parse --is-shallow-repository` is true. Add an AC that plants an uncommitted edit in the scratch fixture repo and expects exit 2.
- **Gate:** bug-class checklist entry: "a provenance check must hash the bytes it certifies, not only the history".

### H3 — A partial `govkit update` drops the spec-audit opt-in (id 40)

- **Where:** spec 16, section 4 Rollout; section 5 risks.
- **What:** The spec prices only a whole `govkit update`. `govkit update --kits agent-cap` narrows to that kit, and agent-cap does not require the workflows kit.
- **Consequence:** The update lands a hook with no rule 0 and no pack, so the spec-audit opt-in fails open on a supported path. The section 5 claim that the pack is wired before the hook loses the rule holds only in this repository.
- **Fix (skeptic: sound):** Make rule 0's removal conditional: the hook keeps rule 0 unless the pack's fragment is wired, or the hooks kit declares the pack as a requirement. Alternatively, govkit refuses a partial update that lands agent-cap past this version without the workflows kit. Add the matching probe to section 6.
- **Gate:** a govkit self-test arm that runs `update --kits <k>` for each kit losing a rule to another kit and asserts that the rule is still enforced.

## Medium

### M1 — `extract_tag_ref` is minted twice with two return contracts (ids 1, 19, 34)

- **Where:** spec 18, section 2 S7, section 4 The grade and Inventory, AC7, section 7; against spec 12 S3, AC4 and F4.
- **What:** Spec 12 (order 13) builds `extract_tag_ref`, and AC4 pins `x.md:§2 S5` -> `('x.md', 2)`, an integer. Spec 18 (order 18) says the factory "gains" the function, and AC7 expects `('x.md', '§3')`, a string. Spec 18 §7 also claims a self-test leg that spec 12 never adds.
- **Consequence:** Both arms run in `replay_scorer`'s runner, so whichever contract the order-18 builder meets, the other arm goes red. A string section breaks `measure_recall`'s window subtraction, unit-spec replay scores pinned byte-identical by spec 12 AC3, and unit 1's known-set reader.
- **Fix (skeptic: sound):** In spec 18, consume `extract_tag_ref` from spec 12 instead of minting it: rewrite S7, the §4 "gains" bullet and the Inventory row, and add it to the consumes-from edge on unit 12. Restate AC7 to spec 12's contract (`x.md:§3 S2` -> `('x.md', 3)`), or amend spec 12 S3/AC4 and its `tag-section` arm to the string form so that one spec defines one contract. Reword §7 to name the factory runner inside `review-replay selftest`, not a new leg.
- **Gate:** a spec-set check that refuses two specs listing the same minted name in their Inventory.

### M2 — The review-replay manifest is undefined where units 1 and 15 rely on it (id 2)

- **Where:** spec 14, section 2 S2 and S5; section 4 The manifest (review-replay keys).
- **What:** Spec 14 makes a case a known item and `parsed` the cases holding a result row, and refuses unknown keys. Spec 15 treats records as cases (`dispatched 4`, `paired 4 of 4`). Spec 1 reads `parsed` as agent counts and needs a `--matched` list that no key admits.
- **Consequence:** A run matching 45 of 65 known items reads `parsed 45 of 65` and is void forever under spec 1's void rule. Units 1 and 15 cannot meet their acceptance through `check_experiment` as specified.
- **Fix (skeptic: sound):** In spec 14 §4, define the review-replay manifest fully: what a case is (a known item, or a record for a multi-record corpus), what `dispatched` and `parsed` count for a review run, and a `matched` key. Make spec 1 AC5 and its void rule, and spec 15 §4 The two arms and AC8, use the same terms.
- **Gate:** a `check_experiment` self-test arm per declared kind that feeds a manifest shaped like each consuming spec's AC.

### M3 — Spec 18's owned `review.design-audit.runs`/`.seed` nodes have no route (ids 3, 21)

- **Where:** spec 18, section 2 S1; section 3 policy-file non-goal; section 4 The argument and Files touched; section 8 F3.
- **What:** Spec 3 hands the per-run output for these keys to unit 18, but spec 18 never extends `tools/workflows/review_pin.py`, which is missing from its Files touched. Spec 18 also says `review.pin` "invokes the harness runs times", which contradicts spec 3's rule that `review_pin.py` runs nothing.
- **Consequence:** Two owned policy-key nodes ship with no stand-in, unlike `review.twin` (unit 11) and `review.unclassed` (unit 8), and the builder expects an invoker that does not exist.
- **Fix (skeptic: sound):** Add an S item, a Files-touched entry and a criterion: `review_pin.py` takes `--design-audit-runs` and `--design-audit-seed`, checked for shape only, and for a whole-design preset prints one JSON argument line per run (`walk.run` 1 to `runs`) carrying `runs` and `seed`. A run with `--design-audit-runs 3` prints three lines. Reword §4 and F3 to "the caller runs each printed argument set".
- **Gate:** a spec-set check that every owned `policy-key.*` node a spec carries names its stand-in file in Files touched.

### M4 — The render-freshness criterion fills only `{{FANOUT_CAP}}` (ids 4, 15, 16, 32)

- **Where:** spec 17 AC9; spec 18 AC10.
- **What:** Both criteria run `sed 's/{{FANOUT_CAP}}/5/g'` over a template and diff it against the render. `unattended-build.template.js` already carries `{{TOOL_ROOT}}`, `{{MEMORY_TREE_DIR}}` and `{{KIT_DIR}}` (the probe prints 36 diff lines at base). `tier2-review.template.js` gains `{{LENS_SLOTS}}` (spec 13, order 1) and `{{TOOL_ROOT}}` (specs 8 and 15) before either unit runs.
- **Consequence:** Both criteria are red on a correctly rendered tree, so they cannot tell a stale render from a fresh one, and the builder must waive or rewrite them.
- **Fix (skeptic: id 4 unsound, corrected; ids 15, 16, 32 sound):** Replace the sed/diff in spec 17 AC9 and spec 18 AC10 with the parity check in compare mode: `bash tools/workflows/check-protocol-parity.test.sh --check` (or with no `--render`) exits 0. That mode fills every placeholder and catalogue token and asserts that none survives. Keep "Red when" as a template edit with no re-render. Do not use `--render`: it rewrites the live copies in place.
- **Gate:** bug-class checklist entry: "a render-freshness criterion uses the kit's renderer, never a hand-rolled single-token sed".

### M5 — Specs 8 and 11 call `review_pin.py` without the `--subject` spec 3 requires (id 5)

- **Where:** spec 8 AC4; spec 11 AC5; against spec 3 AC7 and AC8.
- **What:** `review_pin.py --unclassed reason` and `review_pin.py --twin always` pass no `--subject`, and spec 3 AC8 requires that call to exit 2. Neither spec says whether the new key prints when its flag is absent.
- **Consequence:** Units 8 and 11 fail their own criteria on a correct build of unit 3. If the keys always print, spec 3 AC7's exact outputs go red.
- **Fix (skeptic: sound):** Add a `--subject` to both commands. State in specs 8 and 11 that `unclassed` and `twin` print only when their flag is given.
- **Gate:** when a spec adds a CLI refusal, a spec-set lint that greps later specs' ACs for calls to that CLI.

### M6 — Kit versions are hand-bumped on the branch, against the lander (ids 6, 31)

- **Where:** spec 11 S9/AC12, spec 8 S9/AC11, spec 16 S7/AC11, spec 10 S8/AC9; against push-main.sh:26-31 and specs 4, 5, 13, 17 and 18.
- **What:** Four specs move a kit version on the branch "if no earlier unit moved it", while the lander mints versions at `--prepare` and a branch owes no bump. The hand bumps touch only the constant's line and skip the other carriers (the `gov:kit roles@` markers in .claude/skills/build/SKILL.md, tools/roles/README.md and SKILL.template.md; `agent-cap@` in format-guard.js and scratch-guard.js).
- **Consequence:** `kit version markers` goes red, or the builder writes outside the dispatch set. The bump can collide with the mint. After unit 11 bumps tier2-review, the version halves of specs 8, 16 and 10 are green before those units are built.
- **Fix (skeptic: sound):** Use one rule for the whole set. Preferred: drop the hand bumps and their AC halves (spec 8 AC11, spec 10 AC9, spec 11 AC12, spec 16 AC11) and rely on `govkit.py mint` at `push-main.sh --prepare` plus the `kit epoch` leg. If a branch bump is kept, give each kit exactly one named bumping unit and list every carrier `write_version_carriers` would move.
- **Gate:** a spec lint that refuses any AC comparing a `KIT_*_VERSION` against base.

### M7 — Spec 3's `gov:lens-optins` marker is refused by spec 13's rule 11 (id 7)

- **Where:** spec 3, section 2 S6; section 4 The swap, in the template.
- **What:** Spec 3 puts `{{LENS_SLOTS}}` under `// gov:lens-optins` and says rule 11 "covers the new marker". Spec 13 defines a marker as a line ending `= [ // gov:lens-slots <literal>` and refuses any token without one, which AC7 pins.
- **Consequence:** Unit 13's renderer refuses unit 3's template with exit 2. The builder has to invent the amendment and decide how one token renders two row shapes.
- **Fix (skeptic: sound):** In spec 3 S6, state the amendment: rule 11 and the marker grammar admit `gov:lens-optins`, whose token renders opt-in rows, or give the opt-in body its own token. Add a criterion that the renderer accepts the opt-in marker and still refuses a truly orphaned token.
- **Gate:** a render_lenses self-test arm per marker form a later unit introduces.

### M8 — Spec 18 omits the whole-design literal, receiver branch and spec 2 arm rewrite (id 8)

- **Where:** spec 18, section 2 S1/S3; section 4 Files touched.
- **What:** Spec 18 adds `whole-design` to `PRESETS` and five rows, but has no S item for the `gov:lens-slots whole-design` literal or the receiver's fourth branch, which specs 2 and 13 assign to it. It never says spec 2 AC1's arm (asserting `preset: 'whole-design'` throws) is rewritten.
- **Consequence:** Spec 13 rule 8 refuses rows naming an undeclared literal, and an existing suite arm turns red with no line saying so.
- **Fix (skeptic: sound):** Add an S item and criterion: a `WHOLE_DESIGN_LENSES` literal marked `gov:lens-slots whole-design`, the receiver's extra branch, and the fan-out slot line counting four literals. State that spec 2's refusal arm is rewritten to refuse another unknown preset.
- **Gate:** a spec-set check that every hands-off a spec gives to unit N appears as an S item in unit N.

### M9 — Spec 16 AC8 greps for names the hook suite never contains (id 10)

- **Where:** spec 16, section 6 AC8.
- **What:** `grep -c "checkSpecAuditDeclared|scanJoinFindings|fanoutFindings" tools/hooks/agent-cap.test.sh` prints 0 at base. Those names live only in agent-cap.js.
- **Consequence:** The criterion cannot fail even if every moved arm stays in the hook's suite, so it certifies a move it never observes.
- **Fix (skeptic: sound):** Observe the arms themselves. Count the hook suite's checks whose payload carries a rule 0, 2 or 5 planted case (`verdictByRef`, a `gov:fixed-verifiers` receiver, `kind: "spec-audit"`) and expect only the new admit arms. Expect the moved arms' count in the three new suites.
- **Gate:** the build method's red-first probe: each AC is run at base and must be red there.

### M10 — The replay isolation recipe cannot clone (ids 13, 41)

- **Where:** spec 1, section 2 S5; section 4 The isolation and AC4; reused by spec 15 section 4 The two arms.
- **What:** `git clone --branch fh-base` cannot find a ref under `refs/replay/` (fatal, exit 128, reproduced), and nothing creates `$TEMP/fhb/` for the bundle. Dropping `--branch` gives an empty clone, on which AC4's first clause passes with nothing to check.
- **Consequence:** Replay 1 and all four replays of spec 15 fail at the first step. A hand workaround may create a real branch here and defeat the isolation AC4 is meant to pin.
- **Fix (skeptic: sound):** Spell a working recipe: `mkdir -p "$TEMP/fhb"`, bundle, then `git init "$TEMP/fh1"`, `git -C "$TEMP/fh1" fetch "$TEMP/fhb/h.bundle" refs/replay/fh-base:refs/heads/fh-base`, and `git -C "$TEMP/fh1" checkout fh-base`. A `clone --no-checkout` followed by the same fetch also works (verified). Parameterise the ref name and clone dir per replay. Add `git -C <clone> rev-list --count fh-base` > 0 to AC4.
- **Gate:** bug-class checklist entry: "a shell recipe in a spec is run once in scratch before the spec commits".

### M11 — The round-state parity arm requires an unreachable CEILING (ids 14, 38)

- **Where:** spec 17, section 4 The parity arm; AC6.
- **What:** The domain keeps round ≤ limit (1 to 4) with at most 3 prior counts. The harness returns CEILING only when round > limit, and the driver's `review_state` only when n+1 ≥ RUNAWAY_CEILING (8). AC6 requires all five tokens to appear.
- **Consequence:** AC6 can never pass, the builder weakens it without guidance, and CEILING parity is never checked.
- **Fix (skeptic: sound):** Over the parity domain, assert the four reachable tokens (CONVERGED, NON-CONVERGENT, BOUNDED, CONVERGING) and state in the arm's header that CEILING lies outside the domain on both sides. Leave CEILING to AC2's direct `deriveRoundState([4, 3, 2], 1, 3)` case. If parity at the ceiling is wanted, add a separate arm, either driving `review_state` with RUNAWAY_CEILING overridden to limit + 1, or asserting the harness's CEILING against the driver's refusal past the limit.
- **Gate:** red-first probe of each AC at its unit's starting commit.

### M12 — "Ungated" is read as "names no leg", not through the declaration grammar (id 23)

- **Where:** spec 15, section 2 S6; section 4 The two arms (`ungated`); section 8 F3.
- **What:** A class counts as ungated when its record names no `LEG_MANIFEST` leg. Records declare gates as paths and commands, and `gotchas.py`'s `declares()` is marked the one copy of that predicate.
- **Consequence:** About 57 gated classes (for example "Gated by `tools/hooks/agent-cap.test.sh`") join the ungated arm, which inflates it to about 130 items against 85 "no machine gate" records. The replay decides on the wrong population, and `--all-ungated` would ship it.
- **Fix (skeptic: sound):** A class is ungated when its body declares "no machine gate", or when no backticked token in its gate declaration resolves as a tracked path or a leg name, the resolution `check_invariant` already performs. Factor that into one function in `gotchas.py`, called by check 18, the replay instrument and `--all-ungated`. Add a criterion with a planted "Gated by `<tracked path>`" class that the flag omits.
- **Gate:** a gotchas self-test arm asserting the instrument's ungated set equals the shared predicate's.

### M13 — agent-cap rule 0 refuses replay 1's design-audit call (id 25)

- **Where:** spec 1, section 2 S5; section 4 The isolation.
- **What:** The clone's dClosedLoop README at 6cfd21619 carries `spec-audit:` under `authorized-by: prompt`, and run B's reviewDir places the call in that build. Rule 0 denies it. The spec never mentions the hook.
- **Consequence:** Both design-audit runs are refused at the first call, so AC4/AC5 and the S9 verdict have nothing to score. After unit 16 the same refusal lives in spec-audit-optin.js. Replays 3 and 4 face rule 6, which requires an Agent prompt to be exactly a rendered gov:handoff file.
- **Fix (skeptic: sound):** In The isolation, name how replay 1 passes the opt-in: an owner-dated opt-in valid for the clone (`SPEC_AUDIT_DEFAULT` cannot help, because the README carries the key), or a recorded departure. Add a criterion that a dry Workflow payload with run B's args and `repo` set to the clone is admitted by `node tools/hooks/agent-cap.js` (or spec-audit-optin.js). Name rule 0 and its moved home in section 7. State how replays 3 and 4 pass rule 6.
- **Gate:** a replay preflight that runs each planned payload through the hook dry before dispatch.

### M14 — Spec 13's whole-tree marker rule breaks existing fan-out fixtures (id 26)

- **Where:** spec 13, section 2 S5; section 4 The slot count.
- **What:** The spec says "every existing fixture arm passes explicit files". The mkfix arms AC2 and AC3, the anti-vacuity arm and the "non-workflow .js" arm run whole-tree over unmarked harnesses and expect exit 0.
- **Consequence:** `verifier fan-out self-test` goes red at the bar, and the builder was told it would not.
- **Fix (skeptic: sound):** Correct the claim in section 4. In S5, name the arms that change: mkfix's harness.js gains a marked five-slot literal, or those arms move to explicit files. Include the "non-workflow .js" arm. Add the edit to the suite's New arm line.
- **Gate:** a spec claim about existing fixtures cites the fixture lines it relies on.

### M15 — unattended-build layout fixtures lack the lens renderer (id 27)

- **Where:** spec 13, section 2 S4; section 4 Files touched.
- **What:** unattended-build.test.sh's build_layout (about :1995-2005) copies tier2-review.template.js and check-protocol-parity.test.sh, but not lenses.toml or render_lenses.py.
- **Consequence:** Once the template carries `{{LENS_SLOTS}}`, every layout's parity render fails, and every check_layout arm of `unattended-build self-test` goes red.
- **Fix (skeptic: sound):** Add tools/workflows/unattended-build.test.sh to Files touched, with build_layout copying lenses.toml and render_lenses.py beside the parity script. Add a red-first probe: one layout run fails before the copy and passes after it.
- **Gate:** bug-class checklist entry: "a new render dependency is copied by every fixture that copies the renderer".

### M16 — The pairing-site scan reaches tracked record code at the root prefix (id 28)

- **Where:** spec 12, section 2 S6; section 8 F2; section 7.
- **What:** The conformance arm scans every tracked *.py under the tool root. At the foreign-prefix leg's repository-root prefix that includes memory/builds/aScoutedSeam's bench.py, whose two sites the spec's own Evidence names.
- **Consequence:** `foreign-prefix parity` fails at the root prefix (`review-replay selftest` runs WHOLE there), and the remaining prefixes print `not run`. The same holds for an adopter installed at its repository root.
- **Fix (skeptic: sound):** Pin the population to the kit tree, the factory's parent directory and below, with `memory/` and every record folder excluded by rule. Add a probe running `scan_pairing_sites` with the tool root at the repository root that sees nothing. Name the foreign-prefix leg in section 7.
- **Gate:** the foreign-prefix leg already catches this. Add a checklist entry: "a whole-tree scan names its population relative to the kit, never to the tool root".

### M17 — Spec 16's new leg omits its registry and budget rows (id 29)

- **Where:** spec 16, section 2 S5; section 4 Files touched.
- **What:** The leg `spec-audit opt-in pack self-test` is added for a withheld suite, but neither tools/govkit/registry.toml nor tools/run-gates/selftest-budgets.txt is in Files touched.
- **Consequence:** govkit's descriptor check and `run-selftests.sh --check` both fail, on files outside the dispatch write set. The foreign-prefix leg also wants a WHOLE_RUN row or a FOREIGN_PREFIX_PROBE stop.
- **Fix (skeptic: sound):** Add to Files touched: an `[[exempt_leg]]` row in registry.toml worded like `verifier fan-out self-test`'s, a measured row in selftest-budgets.txt, and the suite's FOREIGN_PREFIX_PROBE stop or a WHOLE_RUN row in foreign-prefix.gov.test.sh. Name the govkit check leg and the `run-selftests` check in section 7.
- **Gate:** checklist entry (the a-new-leg-trips-meta-gates class): a spec adding a leg lists every file the meta-gates require for it.

### M18 — The fan-out gate gains a sibling .js the fixtures do not copy (id 30)

- **Where:** spec 16, section 2 S2; section 4 The three homes.
- **What:** check-verifier-fanout.sh comes to run `check-verifier-fanout.js` on every judged harness, but check-verifier-fanout.test.sh's fixtures (:199, :212, :231) copy only the .sh.
- **Consequence:** The judged fixtures exit non-zero on the missing file, and the foreign-prefix arms of `verifier fan-out self-test` go red.
- **Fix (skeptic: sound):** Name the fixture copies that must carry check-verifier-fanout.js beside the gate. Add an arm: a gate with its .js removed exits 2, naming the file, and never prints clean.
- **Gate:** same checklist entry as M15.

### M19 — Watched kickoff files change with no manifest re-stamp (id 33)

- **Where:** spec 15, section 2 S4, section 4 Files touched, section 7; also specs 16 and 17.
- **What:** Spec 15 edits coding-governance-agents.template.md, and specs 16 and 17 edit tools/gate-legs.json. Both are on SESSION-KICKOFF.md's `watch:` list, and none re-stamps it or names the `kickoff-manifest ratchet` leg.
- **Consequence:** manifest-check.sh C5 fails the unguarded ratchet leg on the build's tip, on a file outside every write set. SESSION-KICKOFF.md:99 still gives the instruction spec 15 retires.
- **Fix (skeptic: sound):** In specs 15, 16 and 17, add memory/guides/SESSION-KICKOFF.md (its `last-audit:` re-stamp after re-checking the derived claims) to Files touched and `kickoff-manifest ratchet` to section 7. In spec 15, also bring SESSION-KICKOFF.md:99 in line with S4.
- **Gate:** a spec lint that cross-checks Files touched against kickoff `watch:` lists.

### M20 — Spec 5's REVIEW_SHAPE bump breaks earlier units' key-pinning arms (id 35)

- **Where:** spec 5, section 2 S5; section 4 The review key and Files touched.
- **What:** Moving REVIEW_SHAPE to `lenses5-r4` changes every review key. Spec 2 AC4, spec 3 AC5 and spec 9 AC7 (orders 2 to 4) pin the no-argument key to base 3708a705's harness, and spec 5 names only its shape-line arms as changing.
- **Consequence:** Those three arms go red at spec 5's pass, and the cause is not named.
- **Fix (skeptic: finder's fix unsound, corrected):** In spec 5 section 4, name the key-pinning arms of units 2, 3 and 9. Have each compare the no-argument key with the key derived by the harness at that pass's own starting commit, or with a run under REVIEW_SHAPE read from the current template. Never compare with a literal or with base 3708a705's harness.
- **Gate:** checklist entry: "an arm never pins a value to base when a later unit in the same build moves it".

### M21 — The grade tally throws on an item with no `grades` (id 42)

- **Where:** spec 6, section 4 The tally; AC3.
- **What:** `String(it.grades[String(id)])` throws a TypeError when `grades` is absent or null. Migration promises a fallback to the item's severity.
- **Consequence:** Suite stubs that assert the fallback, and replays of pre-unit syntheses, crash the tally.
- **Fix (skeptic: sound):** Read the grade only when `it.grades` is a non-null, non-array object, and otherwise default every id and name it. Add AC3 items with `grades` absent and `grades: null`, each placing ids at the item's severity with the WARNING.
- **Gate:** checklist entry: "every promised fallback has an AC that plants the absent case".

### M22 — Probe-returned leg names are trusted without checks (id 43)

- **Where:** spec 8, section 2 S4 and S7; section 4 Mechanism.
- **What:** The resume probe's `legs` list becomes the oracle for `gate:` dispositions, with no length, type, duplicate or empty check. Whether `[]` counts as no manifest read is unstated.
- **Consequence:** A truncated list refuses valid gates (the manifest has 142 legs), an invented name admits a gate that does not exist, and `[]` refuses every gate without the "no leg manifest" announcement.
- **Fix (skeptic: sound):** Have the probe also return the manifest's element count. Refuse, announced and treated as no `legs`, when the length differs, or when `legs` holds a non-string, a duplicate or an empty string, or is empty. Add AC5 cases for `legs: []` and a short list.
- **Gate:** checklist entry: "agent output used as an oracle carries a completeness count".

### M23 — Free-text disposition reasons reach the committed appendix unescaped (id 44)

- **Where:** spec 8, section 2 S8.
- **What:** The synthesis writes `none — <reason>` cells into the record's appendix with no line-folding or pipe-escaping, unlike `renderCell`'s other cells.
- **Consequence:** A `|` or newline cuts or forges a row of the table `review_replay.py` reads by header (AC10), so the scorer misreads the record.
- **Fix (skeptic: finder's fix unsound, corrected):** Tell the synthesis to write each reason on one line with `|` written as `\|`. At S7, refuse a reason containing `|` or a line break, and have the refusal note name the record's appendix as needing a re-render. Alternatively, have the harness write the appendix itself through `renderCell` in a step after the S7 check.
- **Gate:** a scorer self-test arm reading an appendix with a pipe and a newline planted in a reason.

### M24 — The factory's `<src>` cannot tell a drive-letter path from `<commit>:<path>` (id 45)

- **Where:** spec 12, section 2 S1; section 4 The factory.
- **What:** `<src>` is a path, `<commit>:<path>` or a 40-hex blob, with no rule for ordering them. `C:/...` matches the rev:path shape.
- **Consequence:** On this platform every scratch path the criteria pass (spec 8 AC10, spec 1, spec 14) is refused with exit 2.
- **Fix (skeptic: sound):** State the order: an existing working-tree path wins; a 40-hex string is a blob; otherwise `<rev>:<path>` only when the part before the first `:` is longer than one character or resolves with `git rev-parse --verify`. Add an AC reading a drive-lettered absolute scratch path.
- **Gate:** checklist entry: "every path parser has a drive-letter case".

### M25 — The slot walk tracks only square brackets (id 46)

- **Where:** spec 13, section 4 The slot count; AC5.
- **What:** The walk names "bracket depth" only. Spec 3 renders every slot as `deriveSlotLens('unit-spec', { key, brief })`, with commas inside parentheses and braces.
- **Consequence:** Every marked literal reads 10 or more slots and the leg goes red once unit 3 lands. check-verifier-fanout.sh is outside unit 3's Files touched.
- **Fix (skeptic: sound):** Track depth over `(`, `[` and `{` together. Add to AC5 a literal of five call expressions with object arguments, expected to read 5.
- **Gate:** an AC5 fixture shaped like the most complex slot any later unit renders.

### M26 — Two predicates for one `gov:lens-slots` marker (id 47)

- **Where:** spec 13, section 4 The slot count vs The render.
- **What:** The renderer anchors on a line ending `= [ // gov:lens-slots <literal>`, while the leg walks every line whose text carries `gov:lens-slots`, comments and strings included.
- **Consequence:** The comments S3 rewrites to describe the render can trigger a walk from a non-existent `[`, giving a false SLOTS red or a bogus count.
- **Fix (skeptic: sound):** Define one anchored predicate (the renderer's line-ending regex) once, and use it in both places. Add an AC where a comment containing `gov:lens-slots` sits above a valid literal and the leg still reads exactly the marked literals.
- **Gate:** checklist entry: "one marker, one predicate, defined once".

### M27 — A tail-truncated acquired checklist passes as complete (id 48)

- **Where:** spec 15, section 2 S1; section 4 The acquiring agent.
- **What:** The checklist is accepted on a `- ` line plus the by-design head count. The checker prints the by-design head last, and `extractByDesign` returns `entries: null` without refusing when the head is absent.
- **Consequence:** A return cut at its tail loses items and the head and still passes, so the `selected` arm is scored on a partial checklist.
- **Fix (skeptic: finder's fix unsound, corrected):** Refuse the acquired checklist (checklistError, announced) when it carries no `# by design —` head, or when its parsed `- ` items differ from n + u + k. Here k is the count on the `# invariants are read at <sha>; <k> that this subject adds, edits or takes out are listed as items` line. Add an AC3 case returning the real stdout cut inside its item list.
- **Gate:** checklist entry: "a relayed tool output is checked against its own trailer and totals".

### M28 — The `resume:checklist` agent has no stage, type or options constant (id 49)

- **Where:** spec 15, section 2 S1; section 3 Edges (consumes-from TOOL-dFairHearing-11).
- **What:** Spec 11's arm refuses any `agent(` call whose options are not `probeOpts`, `findOpts`, `verifyOpts` or `synthOpts`. Spec 15 names no stage, type or constant for the new agent, and spec 11 says it "joins" the stage table.
- **Consequence:** The fifth spawn either turns spec 11's arm red or silently reuses `probeOpts`, and neither specs says which.
- **Fix (skeptic: sound):** Either name the stage key (e.g. `checklist`, joining ROLE_KEYS), its default type and a `checklistOpts` constant, and add `checklistOpts` to spec 11's arm list, or state that the agent runs under `probeOpts`. Item L1's corrected fix chooses `probeOpts`, which agrees with spec 15's own edge.
- **Gate:** the spec 11 arm itself. Add a checklist entry: "a new agent spawn names its options constant".

## Low

### L1 — Spec 15 re-claims spec 8's `TOOL_ROOT` row and leaves the checklist agent's typing implicit (id 9)

- **Where:** spec 15, section 2 S1/S2; section 3 Edges; AC6.
- **What:** Spec 8 S9 (order 10) already adds `TOOL_ROOT` to tier2-review's `kit.toml` placeholders, and spec 15 S2 and the kit.toml half of AC6 (order 16) claim the same change. That half is green before unit 15 is built.
- **Consequence:** Two units claim one change, and one criterion half certifies nothing.
- **Fix (skeptic: finder's fix unsound, corrected):** In spec 15 S1, state that resume:checklist spawns with `probeOpts` (the resume probe's stage and type), so spec 11's four-constant arm stays as written. Replace S2's kit.toml claim with "reuses the TOOL_ROOT token TOOL-dFairHearing-8 declares", and drop the kit.toml half of AC6.
- **Gate:** the Inventory duplicate-mint check from M1.

### L2 — Spec 9 AC3 is green at base, and inert anchors are only advisory (id 11)

- **Where:** spec 9, section 6 AC3.
- **What:** `gotchas.py --check` exits 0 with 46 inert anchors today, yet AC3 lists "an anchor is inert" as red.
- **Consequence:** A new record with an inert anchor passes, and AC3 observes nothing of the unit's change.
- **Fix (skeptic: sound):** Drop "an anchor is inert" from the red list, or add an observation naming the three new records: none appears among `--report`'s inert anchors, and each `--for-paths` over an anchor selects its record.
- **Gate:** red-first probe of each AC at base.

### L3 — Spec 1 Rollout misplaces replay 1's flip (id 12)

- **Where:** spec 1, section 4 Rollout.
- **What:** Rollout says every hit flips a template constant of unit 2, 4, 7 or 8. S9 and F5 put replay 1's flip in `review.pin`'s mapping.
- **Consequence:** A builder could flip a template `preset` default that F5 rejects, and AC9's diff reads differently in the two sections.
- **Fix (skeptic: sound):** Reword Rollout: template defaults flip for replays 2 to 4 (units 4, 7 and 8), and replay 1's hit flips `DESIGN_RECORD_PRESET` in `review_pin.py` (spec 3 §4).
- **Gate:** none fits. This is wording, covered by self-review.

### L4 — Spec 18 AC7's Python literal does not parse (id 18)

- **Where:** spec 18, AC7 (the drive-letter case).
- **What:** `'C:\x.md:[a] then [b]'` is a truncated `\x` escape and a SyntaxError.
- **Consequence:** The probe never reaches `extract_tag_ref`, so the drive-letter fold goes unobserved.
- **Fix (skeptic: sound):** Write `r'C:\x.md:[a] then [b]'` or `'C:\\x.md:[a] then [b]'`.
- **Gate:** red-first probe: run each AC command once before committing the spec.

### L5 — Two slot counters and two homes for the number 5 (id 20)

- **Where:** spec 13, section 2 S5, section 4 The slot count and Alternatives rejected, section 10.
- **What:** Spec 13 mints a `measureSlots` lexer and `LENS_SLOTS=5`. Spec 16 moves `MAX_LENSES = 5` and agent-cap's `topLevelArgs` into the same leg, and decision TOOL-aBatchedTribunal-1d rules out a second implementation.
- **Consequence:** Maintenance drift: a change to one counter or constant leaves the other standing. Behaviour is the same today.
- **Fix (skeptic: sound):** Have the slot count call agent-cap's `topLevelArgs` over its literal-blanked view, both exported by spec 16 S1. Either order that export ahead of spec 13's arm, or put the count in `check-verifier-fanout.js` beside rule 2. Give 5 one home (`LENS_SLOTS` replaces `MAX_LENSES`, or rule 2 reads it). Rewrite §10 to name `topLevelArgs` as the seam extended.
- **Gate:** checklist entry citing TOOL-aBatchedTribunal-1d: one element counter per gate.

### L6 — `measure_design_recall` duplicates `measure_recall` (id 22)

- **Where:** spec 18, section 4 The grade; section 2 S7.
- **What:** A new file-and-tag matcher sits beside `measure_recall`, which already matches by equality at window 0. It uses address-only matching, which spec 1 F2 vetoed for the same factory.
- **Consequence:** Two known-set matchers can drift apart. §5 already declares recall an upper bound.
- **Fix (skeptic: sound):** Call `measure_recall(items, candidates, 0)` per run, with plants as items and confirmed rows as candidates, both read through `extract_tag_ref`. Keep only the union, bar and pin checks as new code. In §8, record why seeded plants escape spec 1 F2's veto, or route the grade through `--matched`. Name `measure_recall` in §10.
- **Gate:** the M1 Inventory check, extended to near-duplicate functions named in §10's lookup.

### L7 — `legManifest` renames the established `gateManifest` (id 24)

- **Where:** spec 8, section 2 S4, section 4 Evidence and Data model, section 10.
- **What:** Spec 8 cites drift-audit-state's `gateManifest` (same default) as precedent, then mints `legManifest`.
- **Consequence:** Naming drift only today: a forwarded `gateManifest` would be silently ignored.
- **Fix (skeptic: sound):** Name the argument `gateManifest`, or rename both and update the drift-audit template, its render and the README together. Record the name as reused in Data model and Inventory.
- **Gate:** checklist entry: "a spec citing a precedent reuses its argument names".

### L8 — Retired by-hand checklist instruction survives in three docs (id 36)

- **Where:** spec 15, section 2 S4 Readers.
- **What:** tools/memory-tree/HYGIENE.template.md:776-778 (and its render memory/HYGIENE.md:778), memory/guides/MERGE-BAR.md:95-97 and memory/guides/SESSION-KICKOFF.md:99 still say to run the lookup by hand before a review.
- **Consequence:** Doc drift only. The caller's checklist wins at run time.
- **Fix (skeptic: sound):** Name those files in S4's Readers. Reword each to say the harness acquires the checklist on the diff kind, or record them as deliberately left.
- **Gate:** a Readers line built from a `git grep` of the retired phrase, not from the exact sentence.

### L9 — `review_pin.py` misclassifies a backslashed spec path (id 50)

- **Where:** spec 3, section 2 S8; section 4 review.pin's stand-in.
- **What:** `SPEC_SUBJECT_PATH` matches only `/`, so `memory\builds\dX\spec\...` reads as a design record.
- **Consequence:** Only under `--design-record-preset design-audit` would a unit spec get the design lenses. The CLI has no caller in this build, and the harness classifies the same way.
- **Fix (skeptic: finder's fix unsound, corrected):** Refuse by name, with exit 2, any `--subject` containing `\`, as the harness's specsRule (:506) does. Add an AC7 case with a backslashed spec path that exits 2.
- **Gate:** the drive-letter/backslash checklist entry from M24.

### L10 — A falsy per-preset `lensNotes` entry silently becomes `{}` (id 51)

- **Where:** spec 9, section 4 The note derivation.
- **What:** `lensNotes[SLOT_LITERAL] || {}` turns `null`, `""`, `0` or `false` into `{}` before the D6 check, which refuses `null` by design.
- **Consequence:** The run uses generic briefs with only the existing "no lensNotes" warning.
- **Fix (skeptic: sound):** Refuse the run literal's entry unless it is absent or a plain object, applying today's flat check to it. Add AC6 cases `{ 'unit-spec': null }` and `{ 'unit-spec': 'x' }`, each throwing before the first agent.
- **Gate:** checklist entry: "no `|| {}` default ahead of a shape check".

### L11 — The address key does not fold repo-absolute paths or drive-letter case (id 52)

- **Where:** spec 4, section 4 The address key.
- **What:** `deriveAddressKey` folds `\` and one `./`, but `C:/.../memory/x.md` and `memory/x.md` get different keys.
- **Consequence:** Same-address findings miss batching (unit 4) and twin pairing (unit 7), which lowers a quality metric.
- **Fix (skeptic: sound):** Also strip a leading `repo + '/'` after folding both, and compare drive letters case-insensitively. Add an AC1 case keying `<repo>/src/a.js` to `src/a.js`.
- **Gate:** the M24 checklist entry.

### L12 — The walk grid has no size bound (id 53)

- **Where:** spec 18, section 4 The argument (walk fields); section 5 perf / scale.
- **What:** `walk.items` and `walk.scenarios` have no maximum count, and `name`/`walks` no maximum length. The audit measured 812 cells.
- **Consequence:** An oversized grid truncates walker returns into gaps, so the run is BLOCKED every time and no refusal names the cause.
- **Fix (skeptic: sound):** Refuse by name before the first agent: a maximum cell count per walker slice and a maximum length for `name`/`walks`. Alternatively, state the measured ceiling in section 5 and add an AC for the refusal.
- **Gate:** checklist entry: "every agent-sized input has a stated ceiling at the argument boundary".

review-shape kind=spec-audit round=1 intensity=full at=synth raw=53 confirmed=52 refuted=1 unverified=0 blocker=0 high=3 medium=37 low=12 agents=11 out-tokens=273809
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:section 2 S7, section 4 The grade, section 6 AC7, section 7 | high | medium | confirmed | Blob hashes match the pins. spec-12 S3 (:48-54) and AC4 (:260-262) give `x.md:§2 S5` -> ("x.md", 2), an integer section. spec-12 F4 (:317-323) says unit 18's builder finds extract_tag_ref already present, built 'under the name and contract TOOL-dFairHearing-18's spec spells'. But spec-18 S7 (:54-56) and the inventory (:277) mint the function, and AC7 (:383) expects `('x.md', '§3')`, a string. So the two specs give one function two return types, and both arms run in replay_scorer's runner. The leg part of the finding is weaker: spec-12 F3 (:309-315) already says spec 18's §7 'reads it that way'. The core conflict still stands. Gates would catch it during the build, so the effect is contained. | sound | - |
| 2 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-14.md:section 2 S2, S5; section 4 The manifest (review-replay keys) | high | medium | confirmed | spec-14 S2 (:34-37) defines a review-replay case as a known item. S5 (:45-48) defines parsed as 'the cases holding a parsed result row'. §4 (:115-117) refuses unknown keys, and review-replay takes only `known` and `candidates`. spec-1 consumes check_experiment's manifest (:96). Its void rule (:141-143) and AC5 (:245) need parsed to equal dispatched for agent runs, and it has a `--matched` list (:46-50) that no manifest key admits. spec-15 (:150, :247) uses `dispatched 4` and `paired 4 of 4`, which treats records as cases. The case unit and what parsed means for a review run are left undefined and contradictory. | sound | - |
| 3 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:section 2 S1; section 4 The argument; section 4 Files touched | high | medium | confirmed | spec-3's non-goal (:83-87) leaves `review.design-audit.runs` and `.seed` to their owning units. It says review_pin.py 'runs nothing' and that the multi-call output is 'the owning unit's to add'. spec-3's hands-off (:102) names unit 18. spec-18 carries both nodes (:7-9) and says they arrive through review.pin (:36, :79, :93). Its Files touched (:289-296) omits review_pin.py, no criterion observes it, and grep finds no review_pin mention in spec-18 at all. By contrast, specs 8 and 11 list the file and extend it. spec-18 :128 also says 'review.pin invokes the harness runs times', which contradicts spec-3. | sound | - |
| 4 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md:section 6 AC9 (and spec 18 section 6 AC10) | medium | medium | confirmed | I ran the criterion's own pipeline at base. Filling only FANOUT_CAP in unattended-build.template.js and diffing against unattended-build.js already prints 36 diff lines, for example `{{TOOL_ROOT}}unattended/unattended.sh` against `tools/unattended/unattended.sh` and `{{MEMORY_TREE_DIR}}/gotchas.py`. So spec-17 AC9 is red on a correct build. The same pipeline over tier2-review prints 0 at base. After spec-13 S3 (:35-37) replaces each literal body with `{{LENS_SLOTS}}`, and once spec 8 and spec 15 add `{{TOOL_ROOT}}`, that diff prints hunks too, which breaks spec-18 AC10. The fix is unsound because check-protocol-parity.test.sh `--render` (:6) rewrites the live copies in place and has no scratch output. Running it would write the tree and make the comparison vacuous. | unsound | - |
| 5 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-8.md:section 6 AC4 (and spec 11 section 6 AC5) | medium | medium | confirmed | spec-3 AC8 (:276-279) requires a review_pin.py run with no --subject to exit 2 naming --subject. spec-8 AC4 (:223-224) runs `review_pin.py --unclassed reason` and spec-11 AC5 (:247) runs `review_pin.py --twin always`, both with no --subject, and each expects a JSON line. On a correct build of unit 3 neither can pass. Neither spec 8 S3 nor spec 11 S4 says whether the new key is printed when its flag is absent, and spec-3 AC7 (:268-273) pins exact outputs such as {"preset": "unit-spec"}. | sound | - |
| 6 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-11.md:section 2 S9, section 6 AC12 (also spec 8 S9/AC11, spec 16 S7/AC11, spec 10 S8/AC9) | medium | medium | confirmed | push-main.sh :26-31 says 'KIT VERSIONS ARE MINTED HERE, NOT ON A BRANCH ... A branch therefore owes no bump'. Specs 4, 5, 13, 17 and 18 (e.g. spec-18 :84) say the lander mints versions. Yet spec-11 S9 (:68-70) and AC12 (:279-283), spec-8 (:71-73, :254-259), spec-16 (:73-75) and spec-10 (:66-68, :190-197) each move the tier2-review version on the branch 'if no earlier unit moved it', and each criterion compares against base 3708a705. The README build order puts 11 at 9, 8 at 10, 16 at 11 and 10 at 12. So once unit 11 bumps the version, the version halves of the later units are green before those units are built. | sound | - |
| 7 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-3.md:section 2 S6; section 4 The swap, in the template | medium | medium | confirmed | spec-3 S6 (:52-54) fills a token under `// gov:lens-optins` and says rule 11 of spec 13 'covers the new marker'. Its template sketch (:131-133) shows `const OPTIN_LENSES = [ // gov:lens-optins` followed by `{{LENS_SLOTS}}`. spec-13 defines a marker as a line ending `= [ // gov:lens-slots <literal>` (:167), and rule 11 (:155-156) refuses a token with no marker line above it. spec-13 AC7 (:302-307) pins the orphan-token refusal. Rule 11 as written does not cover the opt-in marker, and spec 3 never states the widening or how one token renders two row shapes. | sound | - |
| 8 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:section 2 S1/S3; section 4 Files touched | medium | medium | confirmed | spec-2 S2 (:33-35) defines the receiver over DIFF, DESIGN and SPEC only. Its hands-off (:73) gives unit 18 'the marked receiver its whole-design literal joins', and spec-13 (:64) gives unit 18 'the whole-design literal and its rows'. spec-2 AC1 (:175-177) is an arm (:215) asserting `preset: 'whole-design'` throws. spec-18 S1/S3 (:34-43) and §4 The walkers (:144-151) name only the preset-set entry, the five lenses.toml rows and WALK_RULES. Grep finds no WHOLE_DESIGN literal, no `gov:lens-slots whole-design` marker and no receiver change in spec-18, and nothing says spec 2's refusal arm is rewritten. | sound | - |
| 9 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-15.md:section 2 S1/S2; section 3 Edges (consumes-from TOOL-dFairHearing-11); section 6 AC6 | medium | low | confirmed | The TOOL_ROOT half holds. spec-8 S9 (:70-72) and AC11 (:253) add TOOL_ROOT to the tier2-review row of kit.toml at order 10, and the base kit.toml :79 reads placeholders = ["FANOUT_CAP"]. spec-15 S2 (:41-44) and the kit.toml half of AC6 (:238-240) claim the same change at order 16, so that half is green before unit 15 is built. The stage half is weaker. spec-15's edge (:85) says the resume:checklist agent takes its type and stage 'as the resume probe does', which reads as reusing probeOpts, a constant spec-11's arm (:37-40) already allows. Only the duplicate claim and the pre-green criterion half are established. The fix is unsound: adding a fifth options constant and widening spec 11's arm goes against spec 15's own edge and adds churn the defect does not need. | unsound | - |
| 10 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-16.md:section 6 AC8 | medium | medium | confirmed | spec-16 AC8 (:241-245) requires `grep -c "checkSpecAuditDeclared\\|scanJoinFindings\\|fanoutFindings" tools/hooks/agent-cap.test.sh` to print 0. I re-ran it and it prints 0 at base. Those names exist only in agent-cap.js (:789, :1767, :1894), never in the suite. So this half of AC8 cannot go red for its stated 'a moved arm is left in the hook's suite'. | sound | - |
| 11 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-9.md:section 6 AC3 | low | low | confirmed | spec-9 AC3 runs `gotchas.py --check` and expects exit 0 and 6 universal records, and its Red-when list includes 'an anchor is inert'. I re-ran `python tools/memory-tree/gotchas.py --check`. It printed 'HYGIENE advisory check 19: 46 of 559 anchor(s) in 26 class record(s) select no tracked path' and exited 0. So inert anchors are only advisory and AC3 is green at base. A new record with an inert anchor would pass it. | sound | - |
| 12 | coherence | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md:section 4 Rollout | low | low | confirmed | The two sections disagree. spec-1 Rollout (:194-195) says every template edit is a default flip of a constant that unit -2, -4, -7 or -8 named. S9 (:76-78) and F5 (:305-309) instead put replay 1's flip in review.pin's mapping, which TOOL-dFairHearing-3 owns. spec-3:186 names that mapping value as `DESIGN_RECORD_PRESET` in review_pin.py. Because F5 already resolves the question, the conflict is mostly wording, so it is graded low. | sound | - |
| 13 | grounding | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md:section 4 The isolation (and AC4); reused by TOOL-dFairHearing-15 section 4 The two arms | high | medium | confirmed | Reproduced in scratch. After `update-ref refs/replay/fh-base` and a bundle of that ref, `git clone --branch fh-base h.bundle c` printed `fatal: Remote branch fh-base not found in upstream origin` and exited 128. A plain `git clone h.bundle c2` warned about an empty repository, and `rev-list --all` counted 0 commits. spec-1:125-130 has no mkdir for $TEMP/fhb either. One correction to the finding: AC4's second clause, `rev-parse 6cfd21619:<record>`, would fail on an empty clone. So only the first clause passes vacuously, and the failure is loud rather than silent. That makes it medium, not high. | sound | - |
| 14 | grounding | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md:section 4 The parity arm; AC6 | medium | medium | confirmed | In unattended.sh:12610-12618, review_state returns CEILING only when n+1 >= RUNAWAY_CEILING. RUNAWAY_CEILING is 8 (:774), and the parity domain only reaches round 4. spec-17 :89 has the harness return CEILING only when round > roundLimit, and both §4 (:166-170) and AC6 (:284-288) limit the domain to round <= limit. So neither side can print CEILING inside the domain, yet AC6 requires all five tokens to appear. AC6 can never pass. | sound | - |
| 15 | grounding | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md:AC9 (the render-diff clause) | medium | medium | confirmed | `grep -o` on unattended-build.template.js finds {{KIT_DIR}} x4, {{MEMORY_TREE_DIR}} x4 and {{TOOL_ROOT}} x1 alongside {{FANOUT_CAP}}. A sed that fills only FANOUT_CAP therefore cannot match the render. The real render() in check-protocol-parity.test.sh:476-487 fills all four tokens. AC9 (spec-17:303) is red no matter whether the template was re-rendered. | sound | - |
| 16 | grounding | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:AC10 (the render-diff clause) | medium | medium | confirmed | Today tier2-review.template.js carries only {{FANOUT_CAP}}, 7 times. spec-13 S3 (:32-42), at build order 1, replaces the literal bodies with `{{LENS_SLOTS}}` and fills it at render time. AC10's single-token sed (spec-18:403) will therefore always differ from the render by unit 18's turn, order 18. That alone confirms the finding without the TOOL_ROOT point. | sound | - |
| 17 | grounding | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:section 4 The grade (extract_tag_ref) and AC7 | medium | - | refuted | duplicate of id=19. The integer-versus-'§3' contract conflict between spec-18 AC7 (:383) and spec-12 AC4 (:260-262) is the same defect id=19 reports. I also confirmed review_replay.py extract_section_ref returns int(m.group(1)). | sound | - |
| 18 | grounding | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:AC7 (the drive-letter case) | low | low | confirmed | spec-18:381 spells the literal 'C:\x.md:[a] then [b]' with a single backslash. In Python 3, `\x` followed by `.m` is a truncated \xXX escape and a SyntaxError. The probe as typed never reaches extract_tag_ref. | sound | - |
| 19 | reuse | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:section 2 S7, section 4 The grade, section 4 Inventory, section 6 AC7, section 7 | high | medium | confirmed | spec-12 S3 (:48-54) builds extract_tag_ref with a §<n> fallback to extract_section_ref's integer. Its AC4 (:260-262) pins `x.md:§2 S5` -> ("x.md", 2), and F4 (:318-323) says unit 18's builder will find the function already present. spec-18, however, says the factory 'gains' extract_tag_ref (S7 :54, §4 :232-235), lists it as minted in its Inventory (:277), and has AC7 expect ('x.md','§3') as a string (:383). Whichever contract the builder meets, one of the two ACs goes red. The conflict is loud, so it is graded medium rather than high. | sound | - |
| 20 | reuse | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-13.md:section 2 S5, section 4 The slot count, section 4 Alternatives rejected, section 10 | medium | low | confirmed | spec-13 §4 (:191-200) mints an inline string-aware `measureSlots` counter and a LENS_SLOTS=5 constant in the verifier fan-out leg. spec-16 S2 (:36-38) moves MAX_LENSES = 5 into the same leg, and that rule counts with agent-cap's topLevelArgs (agent-cap.js:497, :968, :1362). spec-16 F3 (:287-291) keeps those helpers exported from the hook for the rest of the build. The leg ends up with two element counters and two homes for 5, which is the drift risk TOOL-aBatchedTribunal-1d names (DECISIONS.2026-08-10.md:50). Mitigations: spec-13 §10 (:366-368) does name topLevelArgs and gives a reason for not calling it, and the two rules differ (an exact slot count versus a <= cap). So this is maintenance drift, graded low. | sound | - |
| 21 | reuse | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:section 3 (policy-file non-goal), section 4 The argument, section 4 Files touched, section 8 F3 | medium | medium | confirmed | spec-18's Files touched (:289-297) leaves out tools/workflows/review_pin.py, and no S item extends it. Its §4 (:128) and F3 (:433) say review.pin 'invokes the harness runs times'. spec-3 §3 (:85-87) says review_pin.py runs nothing and leaves the per-run argument output 'the owning unit's to add', and :102 hands review.design-audit.runs and .seed to unit 18. Units 11 and 8 both list review_pin.py in Files touched (spec-11:175, spec-8:163). As written, nothing routes the two keys. | sound | - |
| 22 | reuse | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:section 4 The grade (`measure_design_recall`), section 2 S7 | medium | low | confirmed | spec-18 :242-247 writes its own plant matcher, matching on the same file and the same key. It never names measure_recall (review_replay.py:263), which spec-12 S3 makes compare string keys by equality at window 0. The factory therefore ends up with two known-set matchers. Two mitigations reduce the matching concern: §4 alternatives (:309-311) records the address-only choice, and §5 (:327-328) states that recall is an upper bound. What remains is a duplicated matcher that could drift from the shared one, graded low. | sound | - |
| 23 | reuse | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-15.md:section 2 S6, section 4 The two arms (`ungated`), section 8 F3 | medium | medium | confirmed | Spec 15 S6 and F3(a) define 'ungated' as a class record that names no leg of LEG_MANIFEST, read through load_leg_names. Its Evidence (:97-98) counts 15 gated and about 130 ungated. gotchas.py:66-75 holds DECLARES_RE, marked 'THE ONE COPY OF THIS PREDICATE', and declares() is at :261. My own count over memory class records: 146 total, 85 say 'no machine gate', 64 match gated by/in/at, and 57 declare a gate without saying 'no machine gate'. Sample declarations name a gate as a path or a command ('Gated by `python tools/memory-tree/check-arms.py --check`'), not as a leg name, so the arm takes in gated classes. The non-goal names this reading a stand-in for dLinkedLibrary's status, but F3 never weighs the existing declaration grammar as an option. So the arm's population, and the flag's if it ships, is wrong where a better reading already exists. | sound | - |
| 24 | reuse | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-8.md:section 2 S4, section 4 Evidence and Data model, section 10 | low | low | confirmed | tools/workflows/drift-audit-state.template.js:78 and :226 use `gateManifest` with the default `{{TOOL_ROOT}}gate-legs.json`. Spec 8 :113 cites that harness as its precedent, yet :142 and :151 mint `legManifest` and list it among the names this unit mints. tier2-review.template.js has no unknown-key refusal: its Object.keys uses are canonical rendering, roles and efforts, not argument validation. The result is two spellings for one input. No caller forwards gateManifest to tier2-review today, so the effect is naming drift only. | sound | - |
| 25 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md:section 2 S5; section 4 The isolation | high | medium | confirmed | `git show 6cfd21619:memory/builds/dClosedLoop/README.md` shows `spec-audit: 2026-10-14` and `authorized-by: prompt`. There is no dClosedLoop RUN.md at 6cfd21619, so the live-run branch is skipped. agent-cap.js rule 0 (around :2001) then denies a README that carries the key under a mode other than slug. Run B's reviewDir is `memory/builds/dClosedLoop/reviews` (comparison record :33), which places the call in that build. .claude/settings.json:9 wires agent-cap.js. Spec 1's 'The isolation' (:123-138) uses kind spec-audit, repo the clone and run B's args verbatim, and never mentions the hook. So both design-audit runs are refused. I grade it medium, not high: the run is blocked visibly at the first call, and no wrong result ships. | sound | - |
| 26 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-13.md:section 2 S5; section 4 The slot count | medium | medium | confirmed | Spec 13 :206-207 says 'every existing fixture arm passes explicit files'. check-verifier-fanout.test.sh disproves it. mkfix (:226-231) writes a harness.js whose LENSES literal carries no gov:lens-slots marker. AC2 and AC3 (:247-258) run `bash scripts/$WFK/check-verifier-fanout.sh` with no file arguments, which is whole-tree mode, and expect rc 0. The 'non-workflow .js' arm (:203-205) also runs whole-tree over an unmarked bounded.js. S5's new rule, red when no marked literal exists in whole-tree mode, turns these arms red. The suite is in files touched, so the effect stays within the unit, but the spec's statement misleads the builder. | sound | - |
| 27 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-13.md:section 2 S4; section 4 Files touched | medium | medium | confirmed | unattended-build.test.sh build_layout (:1995-2005) copies tier2-review.template.js and check-protocol-parity.test.sh into each layout, but neither lenses.toml nor render_lenses.py. Spec 13 :184-187 has render() run render_lenses.py with the catalogue beside the script for any template that carries the token, and treat a non-zero exit as the 'render ... FAILED' branch. Once the template carries {{LENS_SLOTS}}, every layout's parity run fails. unattended-build.test.sh is not in spec 13's files touched (:223-235). | sound | - |
| 28 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-12.md:section 2 S6; section 8 F2; section 7 | medium | medium | confirmed | Spec 12 S6 (:70-71) scans every tracked *.py under the tool root the factory sits in. Its own Evidence (:119-120) names two positives in memory/builds/aScoutedSeam/build/...-bench.py, which `git ls-files` shows is tracked. The New arm line (:287) runs AC6 (no sites over the tool root) inside `review_replay.py --selftest`. foreign-prefix.gov.test.sh step 3 moves the tool root to the repository root, and :135 lists 'review-replay selftest' as WHOLE_RUN. At that prefix the scan reaches bench.py and the arm goes red. Section 7 (:289-290) names no foreign-prefix leg. | sound | - |
| 29 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-16.md:section 2 S5; section 4 Files touched | medium | medium | confirmed | Spec 16 S5 (:64-65) adds the leg `spec-audit opt-in pack self-test` and has kit.toml withhold its suite. Its files touched (:142-164) list neither tools/govkit/registry.toml nor tools/run-gates/selftest-budgets.txt. govkit.py :2944-2946 fails on any manifest leg that no descriptor claims and no [[exempt_leg]] carries, and registry.toml :644-649 shows the sibling withheld suites carrying such rows. run-selftests.sh --check (:826-840) fails on a held leg with no budget row, and the siblings have rows at selftest-budgets.txt:117 and :147. | sound | - |
| 30 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-16.md:section 2 S2; section 4 The three homes | medium | medium | confirmed | Spec 16 S2 and 'The three homes' (:131) have check-verifier-fanout.sh run the sibling check-verifier-fanout.js on every harness, and that .js exits 2 when it cannot load. In check-verifier-fanout.test.sh, mkfix (:231) copies only check-verifier-fanout.sh, and the empty and nohook fixtures (:199, :212) copy only the gate. AC2 and AC3 expect rc 0. A fixture that judges a harness would fail on the missing .js. The suite is in the unit's files touched, so the fix stays in its write set, but the spec names neither the fixture copies nor a missing-.js arm. | sound | - |
| 31 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-8.md:section 2 S9 and AC11; likewise spec 10 S8/AC9, spec 11 S9/AC12, spec 16 S7/AC11 | medium | medium | confirmed | push-main.sh:26-31 says kit versions are minted at landing and 'A branch therefore owes no bump'. Specs 4, 5, 17 and 18 carry the non-goal 'the lander mints them'. Specs 8 AC11 (:255-259), 10 AC9 (:192-196), 11 AC12 (:280-283) and 16 AC11 (:255-261) require hand bumps on the branch. Spec 10 touches roles_lib.py's version line only, yet `gov:kit roles@1.8` also sits in tools/roles/README.md:1, .claude/skills/build/SKILL.md:5 and tools/roles/SKILL.template.md:5, and check-kit-versions.sh:395 reds when the README marker differs from the constant. Spec 16's KIT_AGENT_CAP_VERSION bump leaves format-guard.js:7 and scratch-guard.js:144 stale, and check-kit-versions.sh:212-219 reds on that. | sound | - |
| 32 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md:section 6 AC9; likewise spec 18 section 6 AC10 | medium | medium | confirmed | I ran `sed 's/{{FANOUT_CAP}}/5/g' tools/workflows/unattended-build.template.js \| diff - tools/workflows/unattended-build.js` at HEAD. It printed hunks at 561 ({{TOOL_ROOT}}) and 565 ({{MEMORY_TREE_DIR}}), so spec 17 AC9 (:301-304) is already red on a correctly rendered tree. The same probe on tier2-review prints nothing today. Spec 18 AC10 (:399-407) uses that probe on tier2-review after spec 13 has made its literals {{LENS_SLOTS}}, and AC10 itself requires walk rows in lenses.toml. The probe would fail there too. | sound | - |
| 33 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-15.md:section 2 S4; section 4 Files touched; section 7 | medium | medium | confirmed | memory/guides/SESSION-KICKOFF.md:6 watch lists tools/gate-legs.json and coding-governance-agents.template.md. Spec 15 touches the charter template (:176), and specs 16 and 17 touch gate-legs.json. None names SESSION-KICKOFF.md or the `kickoff-manifest ratchet` leg, which is gate-legs.json's first entry and has no guard. manifest-check.sh C5 (:1453-1475) fails until a re-stamp follows the change. It allows that re-stamp as a follow-up, but no spec plans one, and push-main.sh:32 notes that a mint does not re-stamp. SESSION-KICKOFF.md:99 still says to run gotchas.py --for-diff 'before a review', the instruction spec 15 retires. | sound | - |
| 34 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:section 4 The grade; section 6 AC7 | medium | medium | confirmed | Spec 12 AC4 (line 260-262) expects extract_tag_ref('x.md:§2 S5') to return ("x.md", 2), and its S3 falls back to the section extract_section_ref gives. review_replay.py:100-115 returns int(m.group(1)), an integer. Spec 18 AC7 (line 383) expects extract_tag_ref('x.md:§3 S2') to return ('x.md', '§3'), a string. Spec 18 S7 (line 54) and section 4 (line 229) say the factory 'gains' extract_tag_ref, but spec 12 F4 says unit 18's builder finds it already present. The build order puts 12 at step 13 and 18 at step 18, so the two contradict each other. | sound | - |
| 35 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-5.md:section 2 S5; section 4 The review key; section 4 Files touched | medium | medium | confirmed | Spec 2 AC4 (line 192), spec 3 AC5 (line 262-263) and spec 9 AC7 (line 199) each pin the no-argument key to 'the key base's harness derives'. Their New arm lines cover those ACs (spec 2 line 215, spec 3 line 299, spec 9 line 214). The build order runs 2, 3 and 9 at steps 2-4 and spec 5 at step 6. Spec 5 S5 and The review key (line 137) set REVIEW_SHAPE to lenses5-r4. That shape is folded into inputPrint (template:985), so base's key moves. Spec 5 line 174 names only the shape-line arms and the duplicate-scan arm as changing. | unsound | - |
| 36 | blast-radius | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-15.md:section 2 S4 Readers | low | low | confirmed | The git grep reproduces. HYGIENE.template.md:776-778 ('Hand a reviewer the classes their diff can hit:'), MERGE-BAR.md:95 ('Before a review, run ...') and SESSION-KICKOFF.md:99 ('run before a review') still give the by-hand instruction. Spec 15 line 101-102 is literally true about the charter line's exact wording, but S4's Readers never addresses these restatements. Behaviour is unaffected because the caller's checklist wins, so this is doc drift only. | sound | - |
| 37 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:section 4 The gaps; section 2 S4 | high | high | confirmed | Spec 18 'The gaps' (lines 181-183) makes the red only a synthesis-prompt instruction to write BLOCKED. No line of spec 18 feeds walkGaps into blockers, highs or roundState. Spec 18 line 100 says whole-design rounds carry spec 17's roundState. Spec 17's deriveRoundState returns CONVERGED at count 0. A gapped walk with no blocker therefore returns roundState CONVERGED beside a non-empty walkGaps. Spec 17 directs callers to route on roundState. I found no unattended-build wiring of the whole-design preset in spec 18, so the path is narrower than the finder's evidence implies, but it is real. | sound | - |
| 38 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-17.md:section 4 The parity arm; section 6 AC6 | high | medium | confirmed | In spec 17, deriveRoundState gives CEILING only when round > roundLimit (line 89), and the parity domain keeps the round at or below the limit (line 170, AC6). review_state (unattended.sh:12614) gives CEILING only when n+1 >= RUNAWAY_CEILING (8), and n+1 <= 4 in this domain. Neither side can print CEILING, yet AC6 and line 171 require all five tokens to appear. The arm cannot pass as written. The failure shows up at once, so its effect is contained. | sound | - |
| 39 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-14.md:section 2 S3; section 4 Output order | high | high | confirmed | Spec 14 S3 (lines 38-41) checks only that `git log --format=%H -- <path>` lists one commit. Nothing in sections 2-6 compares the working-tree bytes it scores with the freeze blob, and AC2 plants only the two-commit and shared-id cases. An uncommitted edit after the freeze passes and prints 'frozen at <sha>'. Under a shallow clone, the boundary commit is the only one listed. Here `git rev-parse --is-shallow-repository` printed false, so the shallow path is narrow but the uncommitted-edit path is open. | sound | - |
| 40 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-16.md:section 4 Rollout; section 5 risks | high | high | confirmed | tools/hooks/kit.toml ships agent-cap.js and requires only settings-merge and kickoff-manifest. tools/workflows/kit.toml requires agent-cap, which is the reverse direction. govkit _cmd_update (lines 9286-9315) narrows a --kits scope to the kits named, widening it only through shared version markers. So `govkit update --kits agent-cap` lands a hook without rule 0 and no pack. Spec 16's Rollout (lines 168-170) and its section 5 risks price only a whole update and the review-without-hooks case. | sound | - |
| 41 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-1.md:section 4 The isolation; section 2 S5 | medium | medium | confirmed | Spec 1 lines 127-129 bundle refs/replay/fh-base and then run `git clone --branch fh-base`. I re-ran this in scratch (verify-b) and it printed 'fatal: Remote branch fh-base not found in upstream origin'. Spec 1 line 102 hands this procedure to spec 15. I also tried the fix's second form: clone --no-checkout, then fetch refs/replay/fh-base:refs/heads/fh-base, then checkout. It worked and showed the commit. | sound | - |
| 42 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-6.md:section 4 The tally; section 6 AC3 | medium | medium | confirmed | Spec 6 line 95 spells the expression as String(it.grades[String(id)]). That throws a TypeError when grades is undefined or null. Migration (lines 120-121) promises that items with no grades fall back to the item's severity. Line 136 says suite stubs 'keep none where an arm asserts the fallback', so those stubs reach the throwing expression. The schema's required key does not bind stubs or replays, and AC3 plants only grades objects that are present. | sound | - |
| 43 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-8.md:section 2 S4 and S7; section 4 Mechanism | medium | medium | confirmed | Spec 8 S4 (lines 49-50) and line 127 take the agent probe's legs as the oracle for gate: dispositions. The only fallback is for an absent legs ('a dead probe reads as no legs'). No length, type, duplicate or empty check is stated. gate-legs.json is a list of 142 objects (my python probe printed 'list 142'). A truncated list would refuse valid gates, and an invented name would admit a gate that does not exist. Effects stay within the disposition set. | sound | - |
| 44 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-8.md:section 2 S8 | medium | medium | confirmed | Spec 8 S8 (lines 65-69) has the synthesis agent write each disposition cell into the committed appendix itself, `none — <reason>` included. No folding or pipe-escaping is stated. In the template, renderCell (around line 1624) exists to fold line breaks and escape the pipe for every other cell. The fix does not work as written. Its first form cannot run, because the synthesis writes the record and returns dispositions in one call, so the harness has no accepted cell to hand over beforehand. Its second form refuses at S7 only after the record has already been written with the bad cell. | unsound | - |
| 45 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-12.md:section 2 S1; section 4 The factory | medium | medium | confirmed | Spec-12 S1 (lines 28-30) and section 4 line 136 say only that `<src>` is 'a working-tree path, or a `<commit>:<path>` or bare 40-hex blob'. Nothing in spec-12 gives an order for telling them apart (grep for drive/colon/rev-parse found only the F1 probe text). A drive-lettered path such as `C:/Users/...` matches the `<rev>:<path>` shape. Spec-8 AC10 passes `--known "$SCRATCH/k.md"`, and on this host that is a drive-lettered path. The reader refuses with exit 2, so the failure is loud and contained. | sound | - |
| 46 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-13.md:section 4 The slot count; section 6 AC5 | medium | medium | confirmed | Spec-13 section 4 (line 196) gives the walk 'bracket depth' and never names parentheses or braces. Spec-3 S2 and section 4 (lines 37, 149) render every slot as `deriveSlotLens('unit-spec', {...})`, which puts a comma inside parentheses. Spec-13 AC5 plants only punctuation inside strings and a trailing comma, so a counter that misses `(` passes every spec-13 AC. Spec-3 AC6 would then red the leg once the wrapper lands, and spec-3's Files touched list (lines 194-205) has no check-verifier-fanout.sh to fix it in. The effect is a red gate during the build, not a wrong result shipped. | sound | - |
| 47 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-13.md:section 4 The slot count vs The render | medium | medium | confirmed | Spec-13 states two different predicates for the one marker. The render (line 167) uses 'a line ending `= [ // gov:lens-slots <literal>`'. The slot count (line 194) uses 'every line whose raw text carries `gov:lens-slots`', which also matches a comment or string that names the marker. S3 rewrites the comments at :769-773, :806-809 and :838-841 to describe the render. A comment there naming the marker would be walked by the leg and give a false SLOTS red. No AC covers a comment line. | sound | - |
| 48 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-15.md:section 2 S1; section 4 The acquiring agent | medium | medium | confirmed | I re-ran `python tools/memory-tree/gotchas.py --for-diff 3708a705..HEAD` into my scratch directory. It printed the header `# 19 class(es) selected by an anchor + 6 universal` and 25 `- ` item lines, then `# by design — 0 invariant(s) this selection touches` as its LAST line (line 84). `extractByDesign` (template :561-580) returns `entries: null` with no refusal when the head is absent. A return truncated at its tail therefore loses the by-design head and some items and still passes. Spec-15 section 4 (lines 116-118) claims 'the by-design head-count refusal catches a truncated block', which holds only for a cut inside the by-design block itself. | unsound | - |
| 49 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-15.md:section 2 S1; section 3 Edges (consumes-from TOOL-dFairHearing-11) | medium | medium | confirmed | Spec-11 S3 (lines 39-40) refuses any `agent(` call whose options are not one of exactly four constants: probeOpts, findOpts, verifyOpts and synthOpts. Spec-15 never names a stage key, type or Opts constant for `resume:checklist`; grep for 'Opts' in spec-15 found nothing. Its edge says the agent takes its type 'as the resume probe does'. Spec-11 line 96 says the checklist agent 'joins' the stage table 'as the resume probe did', which reads as a new stage entry, and a new entry would red spec-11's arm. The two specs leave it open whether the agent reuses probeOpts or adds a fifth constant. | sound | - |
| 50 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-3.md:section 2 S8; section 4 review.pin's stand-in | medium | low | confirmed | The template's :317 `SPEC_SUBJECT_PATH = /(?:^\|\/)builds\/[^/]+\/spec\//` matches only `/`, and spec-3 S8 reuses it as typed, so a backslashed spec path reads as a design record. The consequence is narrow. The dark default maps both kinds to unit-spec, so the preset differs only under `--design-record-preset design-audit`. Spec-3 line 90 says review_pin.py has no caller in this build. The harness classifies the same path the same way (:428), so the two agree. | unsound | - |
| 51 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-9.md:section 4 The note derivation | medium | low | confirmed | Spec-9 section 4 (line 122) writes `lensNotes[SLOT_LITERAL] \|\| {}`, so an entry of null, "", 0 or false becomes `{}` before any check runs. S2 says only that 'the run literal's entry is checked' and that an absent entry is `{}`. The template's :856-858 comment says null is refused by design (the D6 class). AC6 has no null or non-object case. The fallback is announced by the existing no-lensNotes warning, so the run is degraded but not silent, which keeps the effect small. | sound | - |
| 52 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-4.md:section 4 The address key | medium | low | confirmed | Spec-4 section 4 (line 85) normalises `file` only by trimming it, folding `\` to `/` and dropping one leading `./`. A finder's `file` is a free string (schema :643, :749), and the spec-audit kind requires an absolute `repo`, so `C:/.../memory/x.md` and `memory/x.md` get different keys. The effect is lost batching and twin pairing, a quality metric, so it is contained. | sound | - |
| 53 | failure-envelope | memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-18.md:section 4 The argument (walk fields); section 5 perf / scale | medium | low | confirmed | Spec-18 section 4 (lines 114-115) sets no upper bound on the number of items or scenarios, nor on the length of `name` and `walks`. Section 5 (lines 318-320) records the audit's measured 812 cells, which is about 162 rows per walker. A grid too large for a walker to return shows up as gaps, and section 5 says 'a gap reds the record'. The failure is loud rather than a wrong result, but no refusal names the cause. | sound | - |
