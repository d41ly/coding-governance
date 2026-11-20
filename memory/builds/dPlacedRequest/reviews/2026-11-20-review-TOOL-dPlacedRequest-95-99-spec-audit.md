**Serves:** spec-audit TOOL-dPlacedRequest-95@rev-1 TOOL-dPlacedRequest-96@rev-1 TOOL-dPlacedRequest-97@rev-1 TOOL-dPlacedRequest-98@rev-1 TOOL-dPlacedRequest-99@rev-1

# Tier-2 spec audit — TOOL-dPlacedRequest-95 to 99 (build dPlacedRequest)

Provenance: Tier-2 adversarial review, preset unit-spec, synthesised by gov-synthesizer from the skeptic-confirmed findings of the gov-spec-reviewer lenses and the gov-skeptic batches.

Reviewed: memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-95.md@eda59dbd4f847a6bf841163ca72a21621182e7c4, memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-96.md@5f3aaed0c11e52bb5d414140b49613bff37e5395, memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-97.md@c5f2b49a3b7f913e8a60946dd2f77f57e250a450, memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-98.md@9906c5d06b5b1bf9f9e0e438dc455487e5e025fc, memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md@5dad403c3e7739fe743742746b3b4426ab0a4d02

ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers. There are 27 items: 5 high, 15 medium and 7 low.
By raw confirmed finding the tally is 0 blocker, 5 high, 17 medium and 10 low, over 32 findings.
Five items merge two findings each, because each pair describes one defect: 2+16, 11+32, 13+19, 17+33 and 22+30.
Every finding keeps its binding grade.
Spec 99 carries most of the weight, with 18 of the 27 items.
Each fix is a spec amendment; none needs a redesign of the units' scope, so the verdict is CLEAN WITH FIXES rather than BLOCKED.

## Review shape

Intensity full, raw 33, confirmed 32, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.97.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| coherence | yes | 10 | 10 | 0 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 7 | 7 | 0 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 6 | 6 | 0 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 6 | 5 | 1 | 0 | 0 | 0 | 0.83 |

Adjudicated tally by item: 27 items (0 BLOCKER, 5 HIGH, 15 MEDIUM, 7 LOW).
Adjudicated tally by raw confirmed finding: 32 (0 blocker, 5 high, 17 medium, 10 low).

### Run integrity

- Lenses 5/5 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 27 judged sound, 2 judged UNSOUND (ids 13, 14), 3 judged INSTANCE-ONLY (ids 11, 19, 25), 0 none proposed, 0 NOT JUDGED.
- Severity: 0 UNGRADED by the skeptic, 3 RE-GRADED by the skeptic (ids 12, 13, 30).
- Unverified: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Preset unit-spec: coherence, grounding, reuse, blast-radius, failure-envelope.
- Intent: 1 spec document supplied as `specs`, as sibling context.
- Checklist: 71 items, each assigned to one lens: coherence 15, grounding 14, reuse 14, blast-radius 14, failure-envelope 14.
- By design: 2 invariants from the checklist's by-design block.
- Move check: no checked subject moved.
- Refuted findings shown: 1. Same-address pairs shown: 2.
- Dispositions: unclassed refuse; 63 class slugs handed; 202 leg names read from tools/gate-legs.json.

Every counter above is zero where it would mark the run incomplete, so this run is complete.

### Refuted finding and twins

Refuted id 28 (a resolver that always returns null passes spec 95's arm) shares an address with confirmed ids 24 and 27.
It is not a twin of either: 24 is the missing codebase-map dossier and regeneration, and 27 is a stale doc comment.
No twin flag is raised, and id 28 is not counted.

## Items

### H1 — Spec 99 AC2 is green before S2 is built (id 1)

- **Where:** TOOL-dPlacedRequest-99, §6 AC2, against §2 S2.
- **What is wrong:** AC2 probes `resolve_node_tag` and `derive_node_tag` directly. TOOL-dPlacedRequest-43 S20 already fixed both, so the probes print `t` and the matched tag on today's tree. S2's real deliverable is two suite arms plus a kickoff floor rise, and no clause of AC2 observes them.
- **Consequence:** A build that adds neither the run-selftests.test.sh arm nor the manifest-check.test.sh arm passes AC2. The substring and case-fold rules then stay with no gate that reds on regression.
- **Fix (skeptic: SOUND):** Make AC2 observe the arms. Grep each suite at the tip for the new rows: the registry row at tag `s` above `t` in tools/run-gates/run-selftests.test.sh, and the upper-cased-USERNAME `--card` row in skills/session-kickoff/manifest-check.test.sh. Require the kickoff suite's FLOOR_ASSERTIONS above 379. Give a RED-first reading at 95c3103ad, where the greps print 0. Keep the staged-resolver run as a probe the build must run, showing each arm reds against the pre-S20 rules.
- **Left-shift gate:** extend `spec tokens` (or the spec-audit checklist) with a rule that each AC's Red-when must name a reading at the base that actually reds.
- **Grade:** id 1 high (binding).

**Specs:** TOOL-dPlacedRequest-99

### H2 — Spec 99 S4 freshness rule 1 serves a stale cache over a newer ref (ids 11, 32)

- **Where:** TOOL-dPlacedRequest-99, §4 "S4 — the freshness rule", rule 1, and §3 non-goal 2.
- **What is wrong:** Rule 1 picks the cache whenever `cref = local or cref != refc`. `write_card_cache` stores `local` or the commit this node's own publish produced. So a sha `cref` that differs from `refc` means the ref has since moved to another writer's newer publish. In that case rule 1 serves the older cache. `resolve_build_card` reads the ref for the same state, so the two readers disagree. Both S4 plants plant only `cref = local`, so the disagreeing case is never tested.
- **Consequence:** After another session or node publishes the slug's card (for example after a take-over), a follow re-renders and republishes the old route. That is the stale-card defect S4 exists to close, moved to a new path.
- **Fix (id 11 skeptic: INSTANCE-ONLY; the class-level fix is written here):** Restrict rule 1 to `cref = local`, and let a sha `cref` that differs from `refc` fall to the ref. When `cref = local` and `refc` also resolves, do not assume the local write is newer. Pick the newer of the two by the `published <at>` stamp in each card's header, which `render_build_card` writes. Then a foreign publish made after an offline local write still wins. Add two plants: a foreign publish after a cached sha, and a foreign publish after an offline local write. Each is followed by a follow that asserts the newer tail, and `resolve_build_card` must answer the same card.
- The finder's proposal (restrict rule 1 to `cache and cref = local`, plus one foreign-publish plant) cures the cited instance alone. It leaves a foreign publish after an offline local write losing to the older local cache.
- Id 32's fix (skeptic: SOUND) is subsumed by the class-level fix above.
- **Left-shift gate:** add a checklist entry under `decision-re-derived-by-a-second-process`: two readers of one card must share one freshness function, or a plant must assert they agree on every `cref`/`refc` combination.
- **Grades:** id 11 high (binding); id 32 medium (binding, since its finder graded the effect as confined to the orientation card).

**Specs:** TOOL-dPlacedRequest-99

### H3 — Spec 98's push-main floor is sized to gov's full install and reds every partial-kit adopter (ids 22, 30)

- **Where:** TOOL-dPlacedRequest-98, §4 "The branch and the count", and §2 S1.
- **What is wrong:** FLOOR_ASSERTIONS is pinned at "the count the suite prints on the build's node with every block running". push-main.test.sh ships to adopters as the `push-main self-test` gate leg, and the kit declares `requires = []`. The suite has about a dozen skip branches that fire when a sibling kit or python is absent (lines 575, 869, 908, 1050, 1201, 1229, 1304, 1341, 1433-1441, 1593, 1621, 1850). §2 S1 itself keeps the 42-54 skip for "no kit beside it or no python".
- **Consequence:** Every adopter whose install lacks one of the govkit deployer, runlog, lexicon, policy, regen.py, memory-tree or unattended kits runs fewer rows than the floor. Its leg reds on a healthy lander. In gov, the retained skip on a node with no python reds the same way. This is a false red, never a false green.
- **Fix (skeptic: SOUND):** Size the floor to the rows that run on every supported install, as scratch-guard's floor leaves out its Windows-only AC28 row. Alternatively, have each dependency skip add its row count to a `skipped` tally and compare `n + skipped` against the pin. State the rule in §4. Add a probe the build must run: copy the lander and its suite into a scratch tree with no unattended kit beside it, run the suite, and expect green with the skip line printed. Spec 99 S3 raises the same floor, so its raise must follow the same rule.
- **Left-shift gate:** extend `testsuite counts (every bar self-test prints one)` so that a shipped suite whose floor exceeds its kit-minimal count reds, using a kit-absent run of the suite.
- **Grades:** id 22 high (binding); id 30 medium (binding, re-graded by its skeptic).

**Specs:** TOOL-dPlacedRequest-98 TOOL-dPlacedRequest-99

### H4 — Spec 96 claims entry-claim's stale-lease routing is repaired, and nothing repairs or checks it (id 29)

- **Where:** TOOL-dPlacedRequest-96, §1 Goal, §2 S1 and §6 AC1.
- **What is wrong:** The Goal names three consumers of the lost stale row: take-over, the acquire hint and `--entry-claim`. The restored row keeps acquire at `CW_CAUSE=live-holder; CW_HINT=take-over; return 1`. `run_entry_claim` takes the first word after `lease refused — `, which is still `live-holder`, and claim.py routes `live-holder` to wait or stamp (`WAIT_CAUSES`, tools/loop/claim.py@95c3103ad:91).
- **Consequence:** A patch or repeat whose build lease is stale is still routed as a live holder: it waits, exits 4 until flow.wait-ceiling, then raises an owner item. The Goal says this is fixed, and no AC or arm looks at it. The misstatement will mislead the next change.
- **Fix (skeptic: SOUND):** Either scope the entry-claim path in, or scope it out. To scope it in: after a refusal that carries CW_HINT=take-over, `run_entry_claim` routes the stale lease to take-over, or claim.py gains a `stale` cause. Then add an AC clause that runs `--entry-claim` over a planted 25-hour-stale build lease and asserts it does not print `claim waiting`. To scope it out: state in §3 that entry-claim's routing of a stale lease is out of scope, and correct the Goal's sentence.
- **Left-shift gate:** add a checklist entry under `observed-by-claim-no-arm-discharges`: each consumer a Goal names as repaired has an AC or arm that runs it.
- **Grade:** id 29 high (binding).

**Specs:** TOOL-dPlacedRequest-96

### H5 — Spec 99 S5's plant-count check counts the PLANTS literal, not the plants the leg runs (id 31)

- **Where:** TOOL-dPlacedRequest-99, §2 S5 and §4 "S5 — the plant-count token".
- **What is wrong:** S5 counts the keys of a module-level `PLANTS` dict literal by `ast`. tools/loop/budget.py grows that dict after declaring it (`PLANTS.update(REQUEST_PLANTS)` at line 268), and its self-test runs `for c in PLANTS`. So the `loop budget fixtures` leg runs 41 plants while the check requires and accepts `plants=34`.
- **Consequence:** The check certifies a row priced over 34 plants as covering all of them, and leaves 7 request plants unpriced. That is the budget-row class S5 exists to close. Any module that later grows PLANTS by `.update`, a `**` splat or a subscript store is blind in the same way.
- **Fix (skeptic: SOUND):** Define the count as the runtime size. Import the module under `python -I` and take `len(PLANTS)`, or ask the module's own `--list`. Or have the `ast` reader refuse, reporting the module as ungradeable, any module where `PLANTS` is the target of `.update`, a subscript store or a dict literal with a `**` key. Add a check arm over a scratch module that declares 2 plants and updates in 1 more, and assert it requires `plants=3` or reports the module as ungradeable.
- **Left-shift gate:** the new check arm above, inside `run-selftests self-test`.
- **Grade:** id 31 high (binding).

**Specs:** TOOL-dPlacedRequest-99

### M1 — Spec 99 AC2's probes read the ambient GOV_NODE (ids 2, 16)

- **Where:** TOOL-dPlacedRequest-99, §6 AC2 (the probe's environment).
- **What is wrong:** Both resolvers answer GOV_NODE before they read the user (tools/run-gates/run-selftests.sh@95c3103ad:431, skills/session-kickoff/manifest-check.sh@95c3103ad:450 and 465), and AC2's probes never unset it. Both suites unset it for this reason (tools/run-gates/run-selftests.test.sh@95c3103ad:19, skills/session-kickoff/manifest-check.test.sh@95c3103ad:919).
- **Consequence:** On a node that exports GOV_NODE, a correct build fails AC2, or passes it for a reason unrelated to the substring and case rules. The effect is a false red, which is contained.
- **Fix (skeptic: SOUND, for both):** Run both AC2 probes under `env -u GOV_NODE`, as the two suites do.
- **Left-shift gate:** add a spec-audit checklist rule under `fixture-inherits-ambient-machine-state`: an AC probe of a GOV_NODE-reading function names `env -u GOV_NODE`.
- **Grades:** id 2 medium (binding); id 16 low (binding).

### M2 — Spec 99 AC3 never observes the derive_push_failure half of S3 (id 3)

- **Where:** TOOL-dPlacedRequest-99, §6 AC3, against §2 S3 and §4 S3.
- **What is wrong:** AC3 asserts only `read_fence_line`'s returns (4, 4 and 1). `derive_push_failure` (tools/push-main.sh@7a142cb6:323-335) tests only `rc = 3` for unreachable, so every other non-zero rc falls through to `fenced --code claim-lost`.
- **Consequence:** A build that adds return 4 but leaves the classifier alone passes AC3, while still printing `claim-lost` for every non-answer. That is the defect S3 exists to close.
- **Fix (skeptic: SOUND):** Extend AC3. With `derive_push_failure` cut by awk and a stub driver whose `--after` answer is an exit-2 `lease not written — x` line (and, as a second case, a bad-beat fence line), the probe prints `unreachable` and no `claim-lost` on stderr. Its RED-first reading at 95c3103ad prints `fenced`.
- **Left-shift gate:** checklist rule under `criterion-asserts-what-its-own-command-cannot-show`: each S-item's stated consequence is observed by some AC clause.
- **Grade:** id 3 medium (binding).

### M3 — Spec 99 S1 prices the manifest-check row over 30 plants, and S4 makes it 32 (id 4)

- **Where:** TOOL-dPlacedRequest-99, §4 S1 (the budget re-price), against §4 S4.
- **What is wrong:** S1 re-prices the row "from a reading over all 30" plants. S4 adds follow-offline-publish and follow-offline-publish-online, which join the loop through S1's `--list` read. S5's plants= check does not grade this row, because card-store.fixture.sh's PLANTS is a shell string.
- **Consequence:** The row is priced for fewer plants than the suite runs. The shortfall is about two plant runs inside a 1.5x margin.
- **Fix (skeptic: SOUND):** State that S1's reading is taken after S4's plants are in, over every name `--list` prints at that point (32). The row's note names that count, and AC1 observes it (the note's count equals `card-store.fixture.sh --list | wc -l`).
- **Left-shift gate:** the row-note plant count above, checked by AC1, under `budget-row-not-remeasured-after-added-arms`.
- **Grade:** id 4 medium (binding).

### M4 — Spec 99 S7's scratch-guard staged break cannot red on a Windows node (id 5)

- **Where:** TOOL-dPlacedRequest-99, §7 New arm (scratch-guard), against §2 S7 and §6 AC7.
- **What is wrong:** §7 says deleting the every-host AC28 row reds the raised floor. On a MINGW/MSYS/CYGWIN host, including node d where this build runs, the Windows-only AC28 row also runs (tools/hooks/scratch-guard.test.sh@95c3103ad:1759-1772). A floor raised by one keeps one row of slack, so the staged deletion stays green.
- **Consequence:** The arm's stated red reading cannot be observed on the build's own node. AC7 certifies a floor that does not catch the loss of the every-host row there.
- **Fix (skeptic: SOUND):** Stage the break on a non-Windows host, or on Windows by deleting both AC28 rows or forcing `sg_win` empty, and state in §7 which host observes the red. Alternatively, pin the floor per host.
- **Left-shift gate:** checklist rule under `portability-sweep`: a staged break against a host-conditional floor names the host it reds on.
- **Grade:** id 5 medium (binding).

### M5 — Spec 98 AC1 contradicts §4's placement of the GOV_NODE unset (id 6)

- **Where:** TOOL-dPlacedRequest-98, §6 AC1, against §4 "The fixture's own registry".
- **What is wrong:** §4 puts the GOV_NODE save and unset at block level, beside USERNAME and CLAUDE_CODE_SESSION_ID (tools/push-main.test.sh@95c3103ad:1664-1665). AC1 calls the bare `write_fence_fixture` with a GOV_NODE that names no tag and requires a return of 0. The function's acquire inherits that GOV_NODE, `resolve_fleet_tag` passes it as `--node`, `render_playbook` refuses it, and the function returns 1.
- **Consequence:** A build that follows §4 fails AC1. The builder must deviate from §4 or amend the spec mid-build.
- **Fix (skeptic: SOUND):** Choose one place for the unset. Either §4 makes `write_fence_fixture` itself run with GOV_NODE unset (for example the acquire under `env -u GOV_NODE`), or AC1 probes the block's save-and-unset rather than the bare function.
- **Left-shift gate:** checklist rule under `two-answers-to-one-question`: an AC that calls a function in isolation states the environment §4 gives that function.
- **Grade:** id 6 medium (binding).

### M6 — Spec 97's third row is refused by the session gate before it reaches the new row (id 7)

- **Where:** TOOL-dPlacedRequest-97, §4 The arm (the third row).
- **What is wrong:** An id-less `--lease acquire` goes through `run_lease_verb`'s session gate (tools/unattended/unattended.sh@95c3103ad:4122-4126). That gate prints `lease not written — no session` and returns 2 before `check_claim_writable` runs.
- **Consequence:** The row passes whatever the new keepalive `mine` row does, so it guards nothing about the non-goal that the `--lease` verbs gain no identity. It also asserts "still refuses" on an exit that is not a refusal.
- **Fix (skeptic: SOUND):** Run the third row under a present session that is not the record's (`CLAUDE_CODE_SESSION_ID=s2 --lease acquire build <slug>` over the `session: absent`, `keepalive: K` record of this node's tag). Assert `lease refused — live-holder`, exit 1. That reaches the column, where the new row's `c_sess absent` branch is live.
- **Left-shift gate:** checklist rule under `fixture-passes-by-finding-nothing`: a negative row states the earlier gate it must pass to reach the code under test.
- **Grade:** id 7 medium (binding).

### M7 — Spec 99 AC1 does not decide S1 (id 8)

- **Where:** TOOL-dPlacedRequest-99, §6 AC1, against §2 S1.
- **What is wrong:** AC1's plant-run half is green before the build, since the spec measured all 30 plants holding. Its grep half (`for cs_plant in publish publish-off` absent) passes for any loop that drops the literal list, including a deleted loop. "While the suite's loop reads --list" has no command behind it. Nothing observes S1's liveness row, floor rise, floor-comment fix or budget re-price.
- **Consequence:** A build that removes the hand list without wiring `--list`, or skips the liveness row and the re-price, satisfies AC1. The plants could stay ungated while the AC reads green.
- **Fix (skeptic: SOUND):** Make AC1 decide S1. Grep for `card-store.fixture.sh" --list` (or S1's assignment) feeding the loop, and for the liveness `check_eq` row. Require `^FLOOR_ASSERTIONS=` above 379, and require the manifest-check row of selftest-budgets.txt to differ from `3820` with a note naming the plant count. Give each part a RED-first reading at 95c3103ad.
- **Left-shift gate:** same checklist rule as H1, under `criterion-asserts-what-its-own-command-cannot-show`.
- **Grade:** id 8 medium (binding).

### M8 — Spec 96's static arm skips one reset line where the reset spans two (id 12)

- **Where:** TOOL-dPlacedRequest-96, §4, The arms, Static arm.
- **What is wrong:** The arm counts a CW_* name as assigned when it appears "beyond the reset line at its head". The reset in `check_claim_writable` (tools/unattended/unattended.sh@95c3103ad:2804 onward) spans two lines, and `CW_HINT=` appears only on the second.
- **Consequence:** Built literally, the arm counts CW_HINT as assigned at 95c3103ad, so it is green for the very instance it targets. The next row dropped beside a two-line reset passes silently. AC1's probe and the probe arm still guard this instance.
- **Fix (skeptic: SOUND):** Define the exclusion by content, not line count: drop every line of the head reset block (the contiguous bare `CW_X=""`/`CW_EPOCH=0` assignments after the `local` lines), or count assignments only inside the `case "$mode:$cls"` and class blocks. Stage the arm red against 95c3103ad and record that reading.
- **Left-shift gate:** the recorded RED-first staging of the arm, under `fixture-passes-by-finding-nothing`.
- **Grade:** id 12 medium (binding; the finder graded high, the skeptic medium).

### M9 — Spec 99 S1's re-price basis is ambiguous: plants alone or the whole suite (id 14)

- **Where:** TOOL-dPlacedRequest-99, §2 S1 and §4 S1, the budget re-price.
- **What is wrong:** tools/run-gates/selftest-budgets.txt@95c3103ad:98 prices the whole manifest-check suite (worst 2547s, x1.5 = 3820). S1 says the row is re-priced "from a reading over every plant", and §4 says "from a reading over all 30, worst of two". Read literally, that is the plants-only figure (781s, about 1170s at x1.5).
- **Consequence:** A literal build under-prices a suite of about 3100s, and every serial run breaches the row. (PINNED)
- **Fix (skeptic: UNSOUND; the skeptic's corrected fix is written here):** Say that the row is re-priced from a reading of the whole suite's argv with all 30 plants gated, worst of two at x1.5, and that its note names the plant count. Compare the manifest-check leg's ceiling (4370) with that reading, not with the budget. Raise the ceiling with `derive-ceilings.py --write --observed` evidence only where the reading leaves the leg too little headroom.
- **Left-shift gate:** extend `every held leg is budgeted, every budget row resolves` so a row's note names the population it was read over.
- **Grade:** id 14 medium (binding).

### M10 — Spec 99 S5's ceiling procedure names a command that never moves a ceiling (ids 13, 19)

- **Where:** TOOL-dPlacedRequest-99, §4 S5 "the plant-count token", Files touched, and §7.
- **What is wrong:** S5 says "the ceiling moves by `derive-ceilings.py --write`". That command writes only `ceiling-evidence.txt` (lines 362 and 628) and never writes tools/gate-legs.json. A direct-CLI reading enters the evidence only through `--write --observed '<leg>=<s>' --how` under GOV_NODE. TOOL-aClearedLedger-10 already decided the procedure. `ceiling-evidence.txt` is missing from Files touched, and `leg ceilings clear their evidenced maximum` is missing from §7. The wording is copied from memory/gotchas/budget-row-not-remeasured-after-added-arms.md, which says the same.
- **Consequence:** The builder runs plain `--write`, which records nothing for a direct-CLI reading and moves no ceiling. Either the step does nothing, or the builder hand-edits gate-legs.json with no evidence behind it, and the pass_leg fields can go stale.
- **Fix (id 19 skeptic: INSTANCE-ONLY; id 13 skeptic: UNSOUND; the class-level fix and the corrected fix are written here):**
  - In spec 99 S5, state the real path. Where a leg's reading, not its budget, approaches the leg's ceiling, edit the `ceiling` in tools/gate-legs.json and record the reading with `GOV_NODE=<tag> derive-ceilings.py --write --observed '<leg>=<s>' --how '<direct CLI, base, node>'`, so `--check` holds it. Assert no ceiling-at-least-budget relation, because the budgets file keeps the two figures apart by design.
  - Then run `pass_legs.py --apply`, and re-stamp `last-audit` in memory/guides/SESSION-KICKOFF.md when gate-legs.json changes. Add `tools/run-gates/ceiling-evidence.txt` to Files touched and `leg ceilings clear their evidenced maximum` to §7.
  - Class-level: correct the fix paragraph of memory/gotchas/budget-row-not-remeasured-after-added-arms.md (lines 30-31) to name `--write --observed '<leg>=<s>' --how` under GOV_NODE, the manifest ceiling move under `derive-ceilings --check`, `pass_legs.py --apply` and the last-audit re-stamp. The next spec would otherwise copy the wrong wording again.
  - The finder's proposal for id 19 (cite the decided procedure in spec 99 alone) cures the cited instance only. Id 13's finder proposal (an AC asserting each leg ceiling is at least its new budget) was rejected and is not the fix.
- **Left-shift gate:** the corrected class record, which `gotchas.py --for-paths tools/run-gates/` selects for the next spec touching ceilings.
- **Grades:** id 19 medium (binding); id 13 low (binding, re-graded by its skeptic: the consequence is a misstated procedure rather than a killed leg).

### M11 — Spec 95 writes a new class record for a class the catalogue already holds (id 18)

- **Where:** TOOL-dPlacedRequest-95, §2 S1 and §4 "The class record".
- **What is wrong:** The unit writes `hook-executes-code-resolved-from-its-target`. memory/gotchas/foreign-code-runs-on-the-ambient-credential.md already records that class: code another repository authored runs with this node's environment and credential. §10's reuse audit never names it.
- **Consequence:** The checklist would carry two records for one class, selected by disjoint anchors. A hook diff gets the new record, and a deployer or govkit diff gets the old one. Each review sees half the class history.
- **Fix (skeptic: SOUND):** Extend the existing record. Add an `## It bit again in the PreToolUse hook` section to foreign-code-runs-on-the-ambient-credential.md, citing `tools/hooks/scratch-guard.js` in backticks so `gotchas.py --for-paths tools/hooks/scratch-guard.js` selects it, the shape TOOL-dPlacedRequest-98 uses. Re-point AC1's second half to print `foreign-code-runs-on-the-ambient-credential`. If a separate record is kept on purpose, §4 must say why the existing class does not cover it, and §10 must name the rejected record.
- **Left-shift gate:** a spec-audit checklist rule that a new gotcha record's §10 names the nearest existing record from a catalogue search.
- **Grade:** id 18 medium (binding).

### M12 — Spec 99's §7 leg line omits `policy fixtures` (id 23)

- **Where:** TOOL-dPlacedRequest-99, §7 leg line, joined with §4 Files touched.
- **What is wrong:** `check-spec-tokens.py --legs-for` names `policy fixtures` as a non-broad guard of both skills/session-kickoff/manifest-check.sh and tools/gate-legs.json. Both are estimate paths, and the §7 line does not name the leg.
- **Consequence:** Once the unit goes INPROGRESS, the `spec tokens` leg's guard-legs join reds the spec. The builder's leg plan also never runs the one leg that reads manifest-check.sh as a policy-fixture subject against S4's rewrite.
- **Fix (skeptic: SOUND):** Add `policy fixtures` to the §7 leg line. The skeptic ran the probe over every estimate path of 95, 98 and 99 and found no other missing leg.
- **Left-shift gate:** `spec tokens (a spec's own names resolve)` already catches it at INPROGRESS; run `--legs-for` at spec-writing time too.
- **Grade:** id 23 medium (binding).

### M13 — Specs 95 and 99 add gotcha records without the codebase-map dossier and regeneration (id 24)

- **Where:** TOOL-dPlacedRequest-95, §4 Files touched; the same omission is in TOOL-dPlacedRequest-99, §4.
- **What is wrong:** Each new gotcha record becomes a key in the codebase map's `gotcha-classes` inventory (tools/codebase-map/map_extractors.py@95c3103ad:220-223). Each key must be claimed in a feature dossier under memory/map/features/, and memory/map/generated/ regenerated. 99's new `check_plant_tokens` also enters symbols.json. Neither spec names the dossier or the generated files.
- **Consequence:** The unguarded `codebase-map coverage + freshness` leg reds both units with UNCLAIMED keys and stale generated files. The build learns this only at the bar, and the write sets used to sequence sibling dispatch are incomplete.
- **Fix (skeptic: SOUND):** Add to each spec's Files touched the dossier that claims each new record (for example memory/map/features/agent-cap.md or a hooks dossier for 95; the session-kickoff, run-gates and unattended dossiers for 99), and memory/map/generated/* regenerated by `python tools/codebase-map/gen_map.py --write`.
- **Left-shift gate:** `codebase-map coverage + freshness` already catches it at the bar; add a spec-audit checklist line that a new gotcha record's Files touched names its dossier.
- **Grade:** id 24 medium (binding).

### M14 — Specs 98 and 99 raise the push-main floor without re-pricing its budget row (id 25)

- **Where:** TOOL-dPlacedRequest-98, §4 "The branch and the count" and Files touched; also TOOL-dPlacedRequest-99 S3 and its Rollout.
- **What is wrong:** The `push-main self-test` row (tools/run-gates/selftest-budgets.txt@95c3103ad:114, 1032) was priced on 2026-10-28, before arms 42-54 landed on 2026-11-19. Spec 98 pins a floor that forces those arms to run, and 99 S3 adds two more landing arms. Neither lists selftest-budgets.txt, and 99 §3 forbids re-pricing outside S5's rows. The same holds for the `scratch-guard self-test` row under 95 and 99 S7.
- **Consequence:** The block runs about 25 prepare and land calls at about 65s per landing by the row's own note, so the row silently loses its margin. A loaded node then cuts the suite as over budget. (PINNED)
- **Fix (skeptic: INSTANCE-ONLY; the class-level fix is written here):** Every unit in this set that adds rows or raises a FLOOR_ASSERTIONS pin re-prices that suite's budget row from a fresh reading, or states why not. That is `push-main self-test` for 98 and 99 S3, and `scratch-guard self-test` for 95 and 99 S7. Each such spec lists tools/run-gates/selftest-budgets.txt in Files touched and checks the leg's ceiling with derive-ceilings.py. The finder's proposal (re-price only the push-main row under 98 and 99) cures the cited instance alone.
- **Left-shift gate:** a check in `every held leg is budgeted, every budget row resolves` that reds when a suite's FLOOR_ASSERTIONS moved in a commit later than its budget row.
- **Grade:** id 25 medium (binding).

### M15 — Spec 99 §3 forbids the re-price S1 performs, and S1 never routes the ceiling (id 26)

- **Where:** TOOL-dPlacedRequest-99, §3 third bullet, against §2 S1; §4 S5's ceiling sentence.
- **What is wrong:** §3 says "No re-pricing of a budget row that is not a loop-kit row S5 names", while S1, Files touched and §5 re-price `manifest-check self-test`, which is not a loop-kit row. S5's ceiling sentence is scoped to S5's rows, so S1 says nothing about the 4370s ceiling. (PINNED)
- **Consequence:** A builder following §3 skips S1's re-price and leaves the added plants unpriced. A builder following S1 has no stated ceiling step.
- **Fix (skeptic: SOUND):** Narrow the §3 bullet to "no re-pricing of a budget row that neither S1 nor S5 names". Give S1 the same ceiling sentence S5 has, using the corrected procedure in M10. Name `leg ceilings clear their evidenced maximum` on the §7 line.
- **Left-shift gate:** checklist rule under `amendment-leaves-its-other-half-standing`: each non-goal is grepped against the scope items for a contradiction.
- **Grade:** id 26 medium (binding).

### L1 — Spec 99 S8's exit-3 spelling does not match the header it claims to mirror (id 9)

- **Where:** TOOL-dPlacedRequest-99, §2 S8 and §6 AC8.
- **What is wrong:** S8 lists exit 3 as `3 budget spent`, "as run_entry_claim's header does". The header (tools/unattended/unattended.sh@95c3103ad:4849) reads `3 spent`.
- **Consequence:** Two spellings of one exit list will drift. Behaviour is unaffected.
- **Fix (skeptic: SOUND):** Use one spelling. Either AC8's grep and S8 say `3 spent`, or S8 also amends the header to `3 budget spent` and AC8 greps both.
- **Left-shift gate:** the S8 arm compares the words of the usage line against the header, not only the codes.
- **Grade:** id 9 low (binding).

### L2 — Spec 95 AC1 does not observe the suite arm or the floor rise (id 10)

- **Where:** TOOL-dPlacedRequest-95, §6 AC1, against §2 S1.
- **What is wrong:** AC1 probes a hook copy with `node -e` and greps gotchas.py. S1 also promises a scratch-guard.test.sh arm over three fixtures and a FLOOR_ASSERTIONS rise (from 396), and no criterion observes them.
- **Consequence:** A build without the arm passes AC1, and the unit's promised regression gate is missing. The resolver fix itself is still observed.
- **Fix (skeptic: SOUND):** Add an AC1 clause: grep tools/hooks/scratch-guard.test.sh for the arm's rows naming TOOL-dPlacedRequest-95, and require `^FLOOR_ASSERTIONS=` above 396 with a comment naming this unit. The RED-first reading at 95c3103ad prints 0 and 396.
- **Left-shift gate:** same checklist rule as H1.
- **Grade:** id 10 low (binding).

### L3 — Spec 99 S8's arm misses run_entry_claim's pass-through returns (id 15)

- **Where:** TOOL-dPlacedRequest-99, §4 S8, the arm over run_entry_claim's returns.
- **What is wrong:** The arm collects literal `return <n>` codes by awk. run_entry_claim also has four `return "$rc"` exits that pass claim.py's code through (unattended.sh lines 4866, 4880, 4942, 4946).
- **Consequence:** A code claim.py produces outside 0-5 leaves through `--entry-claim` undocumented while the arm stays green.
- **Fix (skeptic: SOUND):** Have the arm also fail on any non-literal `return "$var"` in the body unless a comment pins the codes the variable can carry, or clamp the pass-throughs to a documented code (2) in the driver.
- **Left-shift gate:** the arm itself, as amended.
- **Grade:** id 15 low (binding).

### L4 — Spec 99 S1 says the suite's TMPDIR is always forward-slashed (ids 17, 33)

- **Where:** TOOL-dPlacedRequest-99, §4 "S1 — the plant loop", the TMPDIR paragraph.
- **What is wrong:** The spec calls a backslashed TMPDIR "a probe's trap and not the gate's". skills/session-kickoff/manifest-check.test.sh@95c3103ad:7 builds TMP from `${TMPDIR:-/tmp}`, MSYS `mktemp` keeps an inherited backslashed spelling, and run-gates derives TMPDIR from the ambient one.
- **Consequence:** A bar launched with a Windows-spelled TMPDIR reds every plant, and S1 widens that exposure from 8 plants to 30. On this node TMPDIR is forward-slashed, so behaviour matches the spec here.
- **Fix (skeptic: SOUND, for both):** Either normalise TMP in manifest-check.test.sh (for example `cygpath -m` where available) before handing it to the plants, or restate the claim as holding only where TMPDIR is forward-slashed.
- **Left-shift gate:** checklist entry under `portability-sweep` for a suite-made temp directory inheriting the ambient spelling.
- **Grades:** id 17 low (binding); id 33 low (binding).

### L5 — Spec 99 S5 re-derives the budget-row join that read_population already makes (id 20)

- **Where:** TOOL-dPlacedRequest-99, §4 S5, first paragraph.
- **What is wrong:** S5 joins each row to its held leg by name and reads the leg's argv. `read_population` in run-selftests.sh (line 665 onward, computed once as POP at line 954) already joins rows to argv, preferring the row's own argv and resolving `{prefix}`.
- **Consequence:** A row carrying its own argv would never be graded, and the two readers could disagree on which command a row prices. No current row carries its own loop argv, so this is latent.
- **Fix (skeptic: SOUND):** State that `check_plant_tokens` reads the `ok` lines of `read_population` (the `$POP` the run already computes) and matches the resolved argv against `<tool root>/loop/<module>.py`.
- **Left-shift gate:** checklist entry under `decision-re-derived-by-a-second-process`.
- **Grade:** id 20 low (binding).

### L6 — Spec 99 S1's liveness row counts an empty capture as one plant (id 21)

- **Where:** TOOL-dPlacedRequest-99, §4 S1, the plant-loop sketch.
- **What is wrong:** `wc -l <<<"$cs_list"` counts an empty capture as 1. The sketch also calls `--list` and the liveness row outside the existing `[ -f "$cs_fx" ]` skip, and the fixture ships to no adopter while the suite does.
- **Consequence:** At an adopter the liveness row reds 1 against 0 instead of taking the suite's skip. The bar itself is unaffected, since the suite is no adopter leg.
- **Fix (skeptic: SOUND):** Count with `printf '%s' "$cs_list" | grep -c .`. Guard the `--list` call and the liveness row with the existing `[ -f "$cs_fx" ]` test. Treat a non-zero exit of `--list` as a named FAIL rather than an empty list.
- **Left-shift gate:** extend `shell hygiene` with a pattern ban on `wc -l <<<` over a capture.
- **Grade:** id 21 low (binding).

### L7 — Spec 95 leaves resolveKickoffChecker's doc comment describing the removed rung (id 27)

- **Where:** TOOL-dPlacedRequest-95, §4 "The resolver after this unit" and Files touched.
- **What is wrong:** The comment above `resolveKickoffChecker` (tools/hooks/scratch-guard.js@95c3103ad:697-704) still describes the third rung, "then the one `cwd`'s repository tracks". The spec removes that rung and its parameter but does not list the comment.
- **Consequence:** The landed hook describes a walk it no longer takes, at a trust boundary. Behaviour is unaffected.
- **Fix (skeptic: SOUND):** Add to S1 and the Files touched entry: the header comment rewritten to name the two install-side rungs and to state that the target's tree is never a rung.
- **Left-shift gate:** checklist line: a removed branch or parameter lists the doc comment above its function as a carrier.
- **Grade:** id 27 low (binding).

review-shape kind=spec-audit round=1 intensity=full at=synth raw=33 confirmed=32 refuted=1 merged=0 unverified=0 blocker=0 high=5 medium=17 low=10 agents=11 out-tokens=232891 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=5 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 6 AC2, against section 2 S2 | high | high | confirmed | I checked that spec 99's blob is 5dad403c. In tools/run-gates/run-selftests.sh at lines 442-450, resolve_node_tag lower-cases the user and requires exact equality (`[ "$user" != "$tok" ]`). In skills/session-kickoff/manifest-check.sh at line 465, derive_node_tag compares `tolower(mt) == tolower(user)`. So both of AC2's direct probes already print `t` and the matched tag on today's tree. The AC's own Red-when admits that at 95c3103ad neither suite feeds either input. S2's real deliverable is the two suite arms plus a kickoff floor rise (the floor is FLOOR_ASSERTIONS=379 at line 2457), and no clause of AC2 observes either. A build that adds no arm passes AC2. | sound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 2 | coherence | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 6 AC2 (the probe's environment) | medium | medium | confirmed | AC2's text never unsets GOV_NODE. resolve_node_tag checks GOV_NODE first (tools/run-gates/run-selftests.sh@95c3103ad:431) and returns 2 when GOV_NODE is not a registered tag. derive_node_tag (skills/session-kickoff/manifest-check.sh@95c3103ad:450 and 465) compares against GOV_NODE when it is set, so the user comparison is never reached. Both suites unset GOV_NODE: tools/run-gates/run-selftests.test.sh@95c3103ad:19 does, with a comment about 46 arms going red, and skills/session-kickoff/manifest-check.test.sh@95c3103ad:919 does too. On this host GOV_NODE is unset, but on a node that exports it, a correct build fails AC2. The effect is a false red, which is contained. | sound | fixture-inherits-ambient-machine-state | class:fixture-inherits-ambient-machine-state |
| 3 | coherence | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 6 AC3, against section 2 S3 and section 4 S3 | medium | medium | confirmed | tools/push-main.sh@7a142cb6:323-335: derive_push_failure tests only `rc = 3` for unreachable. Every other non-zero rc falls through to `fenced` with `--code claim-lost`. AC3 asserts only read_fence_line's returns (4, 4 and 1). So a build that adds return 4 but leaves the classifier alone passes AC3 while still printing claim-lost for every non-answer, which is the outcome S3 exists to remove. The section 7 push-main arm would observe it, but no acceptance criterion does. | sound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 4 | coherence | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 4 S1 (the budget re-price), against section 4 S4 | medium | medium | confirmed | Spec 99, section 4 S1, says 'The budget row is re-priced from a reading over all 30'. S4 then adds follow-offline-publish and follow-offline-publish-online, which 'join the gate through S1's --list read'. Once both are in, the loop runs 32 plants against a row priced for 30. skills/session-kickoff/card-store.fixture.sh@95c3103ad:25-28 shows PLANTS is a shell string. S5's plants= check counts only top-level PLANTS dicts in tools/loop modules, so it does not grade this row. The shortfall is about two plant runs inside a 1.5x margin, so the effect is contained but real. | sound | - | class:budget-row-not-remeasured-after-added-arms |
| 5 | coherence | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 7 New arm (scratch-guard), against section 2 S7 and section 6 AC7 | medium | medium | confirmed | In tools/hooks/scratch-guard.test.sh, the every-host AC28 row is at line 1765, and the second AC28 row runs only when sg_win is set (MINGW/MSYS/CYGWIN, lines 1759-1772). The current floor of 396 counts neither row (see the comment chain ending at line 1841). `uname -s` printed MINGW64_NT-10.0-22621. On this node the suite runs both rows, so a floor of 397 keeps one row of slack, and deleting the every-host row leaves the count at the floor, which stays green. The section 7 arm's red reading therefore cannot be observed on the build's own node. | sound | - | class:portability-sweep |
| 6 | coherence | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-98.md:section 6 AC1, against section 4 'The fixture's own registry' | medium | medium | confirmed | Spec 98 blob 9906c5d0, section 4, puts the GOV_NODE save and unset at block level, beside USERNAME and CLAUDE_CODE_SESSION_ID. Today those two are saved and exported at tools/push-main.test.sh@95c3103ad:1664-1665, outside write_fence_fixture (lines 1639-1659). The function's acquire inherits the environment. resolve_fleet_tag (tools/unattended/lib-unattended.sh@95c3103ad:215) passes `--node "${GOV_NODE:-}"` and returns 1 when render_playbook refuses it. AC1 calls the bare function with a GOV_NODE exported that names no tag and requires a return of 0. A build that follows section 4 therefore fails AC1. | sound | - | class:two-answers-to-one-question |
| 7 | coherence | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-97.md:section 4 The arm (the third row) | medium | medium | confirmed | In tools/unattended/unattended.sh at lines 4122-4126, run_lease_verb sends acquire and every other unlisted act through a session gate. With CLAUDE_CODE_SESSION_ID unset, that gate prints `lease not written — no session` and returns 2 before any column check runs. So spec 97's third row, an id-less `--lease acquire`, passes whatever the new mine row does. It cannot guard the non-goal that the --lease verbs gain no identity, and its exit is 2 (not written), not a refusal. A present session that differs from the record's reaches check_claim_writable, where the c_sess-absent branch is live. | sound | fixture-passes-by-finding-nothing | class:fixture-passes-by-finding-nothing |
| 8 | coherence | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 6 AC1, against section 2 S1 | medium | medium | confirmed | Re-probed. `grep -n 'for cs_plant in'` prints line 2383, the hand list of 8, and FLOOR_ASSERTIONS reads 379 at line 2457. Spec 99 at line 120 says all 30 plants already hold, so AC1's plant-run half is green before the unit is built. Its grep half (`grep -c 'for cs_plant in publish publish-off'` prints 0) also passes if the loop is reordered or deleted. 'while the suite's loop reads --list' is prose with no command behind it. Nothing in AC1 observes S1's liveness row, its floor rise, the floor-comment fix or the budget re-price. The §7 arm row names the staged hand list but checks none of these. The consequence is contained: the plants could stay ungated while the AC reads green. | sound | - | class:criterion-asserts-what-its-own-command-cannot-show |
| 9 | coherence | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 2 S8 and section 6 AC8 | low | low | confirmed | tools/unattended/unattended.sh@95c3103ad:4849 is the run_entry_claim header, and it reads `3 spent`. Spec 99 S8 (lines 78-79) and AC8's grep spell it `3 budget spent`, 'as run_entry_claim's header does'. The mirroring claim is false and the two spellings will drift. The S8 arm compares return codes, not words, so behaviour is unaffected. | sound | two-answers-to-one-question | class:two-answers-to-one-question |
| 10 | coherence | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-95.md:section 6 AC1, against section 2 S1 | low | low | confirmed | Spec 95 AC1 (lines 136-144) observes only the node -e probes over a hook copy and `gotchas.py --for-paths`. S1 and §4 promise a scratch-guard.test.sh arm over three fixtures and a FLOOR_ASSERTIONS rise; the file reads `1842:FLOOR_ASSERTIONS=396`. No criterion observes that the arm or the floor rise landed. The §7 'New arm' row names the arm but no AC checks it, so a build without the arm passes AC1. The resolver fix itself is still observed, so the effect is a missing regression arm only. | sound | - | class:observed-by-claim-no-arm-discharges |
| 11 | grounding | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 4 S4, the freshness rule, rule 1 | high | high | confirmed | Read manifest-check.sh. write_card_cache (line 2037) writes `oid`, which is `local` or the ref's commit after a successful publish (lines 2015-2016 set oid=c only when the ref equals the published sha). So after this node's own publish, cref equals refc. A sha cref that differs from refc arises only when read_card_ref (line 1983, in write_build_card before read_card_stored at 1992) or a lookup moved the ref to another writer's newer publish. Rule 1 of spec 99 §4 (line 162) then serves the older cache. resolve_build_card (2151-2163) reads the ref for that same state, through derive_card_verdict, which is not `fresh`. So the two readers disagree, which §3 says the S4 plants exist to rule out. It is reachable whenever a second session or node publishes the same slug's card: a narrow path, but a stale card. | instance | - | class:decision-re-derived-by-a-second-process |
| 12 | grounding | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-96.md:section 4, The arms, Static arm | high | medium | confirmed | In unattended.sh, check_claim_writable starts at line 2804. Its reset spans two lines, body lines 5-6. `CW_HINT=` appears once in the body, on the second reset line (body line 6), and CW_EPOCH=0 is on that line too. Spec 96 §4 line 87 says 'beyond the reset line at its head', singular. Built literally, skipping one line counts CW_HINT as assigned at 95c3103ad, so the static arm is green for the very instance it targets. The harm is contained: AC1's direct probe and the probe arm still guard the instance, and §7 requires the arm staged against 95c3103ad, which would expose the green reading. | sound | - | class:fixture-passes-by-finding-nothing |
| 13 | grounding | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 4 S5, the plant-count token, 'the ceiling moves by `derive-ceilings.py --write`' | medium | low | confirmed | derive-ceilings.py docstring (lines 35-38) says `--write` distils readings into ceiling-evidence.txt and `--check` compares that file against gate-legs.json. The script writes only at lines 362 (run files) and 628 (EVIDENCE). So spec 99 §4 S5's 'the ceiling moves by derive-ceilings.py --write' is false. The finder's placement figure (about 122s budget against a 120s ceiling) compares a budget, not a run time, to the ceiling. The budgets header (lines 11-14) says the two figures are deliberately different, and line 90 already holds a 498s budget over a 300s ceiling. A real run of about 81s fits under 120. The consequence is a misstated procedure rather than a killed leg. | unsound | - | class:budget-row-not-remeasured-after-added-arms (PINNED) |
| 14 | grounding | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 2 S1 and section 4 S1, the budget re-price | medium | medium | confirmed | tools/run-gates/selftest-budgets.txt@95c3103ad:98 prices the whole suite: `manifest-check self-test 3820 worst of 9 readings 2547s, x1.5`. Spec 99 S1 says the row is re-priced 'from a reading over every plant', and §4 lines 127-128 say 'from a reading over all 30, worst of two'. Read literally, that is the plants-only figure (781s, about 1170s at x1.5), which would under-price a suite of about 3100s. §5's '22 plants ... so its budget row is re-priced' hints at the whole suite, but the text is ambiguous. The ceiling half is weaker: gate-legs.json has a 4370s ceiling, and a budget above it is allowed by design (budgets header lines 11-14). The real run of about 3121s would still sit below 4370. | unsound | - | class:budget-row-not-remeasured-after-added-arms (PINNED) |
| 15 | grounding | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 4 S8, the arm over run_entry_claim's returns | low | low | confirmed | Re-read tools/unattended/unattended.sh run_entry_claim (line 4849 onward). It has four `return "$rc"` exits that pass through claim.py's exit code: line 4866 after `claim.py body`, 4880 after `claim.py precheck`, 4942 after `scaffold` and 4946 after `record`. Spec 99 §4 S8 says the arm 'collects the `return <n>` codes ... by awk', so it never sees those exits. The claim 'names every code run_entry_claim's body returns' is therefore narrower than it reads. The effect is confined to a usage line and an arm. | sound | - | new:literal-return-scan-misses-pass-through-exits |
| 16 | grounding | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 6 AC2 | low | low | confirmed | tools/run-gates/run-selftests.sh@95c3103ad:430-440 resolve_node_tag returns early on a non-empty GOV_NODE, either printing GOV_NODE when it is a registered tag or returning 2. manifest-check.sh derive_node_tag's awk compares `tag == node` whenever node is set. Spec 99 AC2's probe text never scrubs GOV_NODE. Both suites do: tools/run-gates/run-selftests.test.sh@95c3103ad:19 runs `unset GOV_NODE`, and skills/session-kickoff/manifest-check.test.sh@95c3103ad:919 does the same. So the suites are safe, but the criterion probe as written reads ambient state. | sound | - | class:fixture-inherits-ambient-machine-state |
| 17 | grounding | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 4 S1, the TMPDIR paragraph | low | low | confirmed | skills/session-kickoff/manifest-check.test.sh@95c3103ad:7 sets `TMP=$(mktemp -d "${TMPDIR:-/tmp}/mfcheck.XXXXXX")` and passes it to each plant as TMPDIR (line 2385). I re-probed with `TMPDIR=<cygpath -w scratch> mktemp -d`, which printed `C:\Users\...\verify-skeptic/tmp.ZH6pTEhlVH`, so the backslashes survive. The spec's claim that the suite's directory is forward-slashed holds only when TMPDIR is POSIX-spelled. Usually it is under Git Bash, so the path is narrow. | sound | - | class:portability-sweep |
| 18 | reuse | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-95.md:section 2 S1 and section 4 "The class record" | medium | medium | confirmed | memory/gotchas/foreign-code-runs-on-the-ambient-credential.md records the class of code another repository authored running with this node's environment and credential. Its fix includes 'It refuses target-side execution' and a payload per kind of target-side code. Spec 95 §1/§4 describes the same root, a hook running 'that clone's tracked file with the agent's privileges', and creates a new record, hook-executes-code-resolved-from-its-target. Its §10 reuse audit names only reuse_lookup and the round records. `grep -rln "foreign-code-runs\\|ambient-credential" memory/builds/dPlacedRequest/` printed nothing, so the existing record was never weighed. gotchas.py derives anchors from backticked paths in the body (line 16), so the two records would be selected by disjoint anchors. | sound | - | new:class-record-duplicates-an-existing-class |
| 19 | reuse | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 4 S5 "the plant-count token", Files touched, section 7 | medium | medium | confirmed | The derive-ceilings.py docstring (lines 34-47) says --write distils run records into ceiling-evidence.txt, and that a reading taken outside the runner enters only through `--write --observed '<leg>=<s>' --how`. Its only writes are line 362 (a prune) and line 628 (EVIDENCE.write_text), and nothing writes gate-legs.json. Spec 99 S5 re-prices from direct-CLI readings and then says 'the ceiling moves by derive-ceilings.py --write', which neither moves a ceiling nor records those readings. Spec 99 contains no pass_legs, SESSION-KICKOFF or ceiling-evidence. §7 omits `leg ceilings clear their evidenced maximum`, which tools/gate-legs.json@95c3103ad:2841 holds. aClearedLedger-10 S2-S4 states the --observed / pass_legs --apply / last-audit procedure. | instance | - | class:budget-row-not-remeasured-after-added-arms |
| 20 | reuse | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 4 S5, first paragraph | low | low | confirmed | run-selftests.sh read_population (line 665 onward) already joins each budget row to its argv. It prefers the row's own argv, falls back to the held leg's, resolves {prefix}, and is computed once as POP at line 954, before the --check branch. Spec 99 S5 instead describes a second join ('joins each row to its held leg by name, reads the leg's argv'). That is a second reader of one decision, the C8 shape. No current budget row carries its own loop argv: my awk over selftest-budgets.txt printed nothing. So the divergence is latent today and contained. | sound | decision-re-derived-by-a-second-process | class:decision-re-derived-by-a-second-process |
| 21 | reuse | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 4 S1, the plant-loop sketch | low | low | confirmed | I reproduced the count: `x=$(bash /nonexistent/card-store.fixture.sh --list 2>/dev/null); wc -l <<<"$x"` printed 1, and `printf '%s' "$x" \| grep -c .` printed 0. Spec 99 §4 lines 107-109 call `--list` and the `wc -l <<<` liveness row outside any `[ -f "$cs_fx" ]` guard. The fixture is registry-exempt (tools/govkit/registry.toml@95c3103ad:380), while tools/govkit/entries/kickoff-manifest.kit.toml@95c3103ad:29 ships manifest-check.test.sh. At an adopter, then, the liveness row reds 1 against 0 instead of taking the existing skip at lines 2382-2384. | sound | line-count-reads-empty-capture-as-one | class:line-count-reads-empty-capture-as-one |
| 22 | blast-radius | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-98.md:section 4 'The branch and the count', and section 2 S1 | high | high | confirmed | tools/govkit/entries/push-main.kit.toml@c88a77f4:70-74 makes `push-main self-test` a [[gate_leg]] with argv `bash {prefix}/push-main.test.sh`, and lines 21-24 ship push-main.test.sh as an engine file. The kit declares `requires = []`, so an adopter can install the lander with no other kit. `grep -n skip tools/push-main.test.sh` printed the dependency skips the finder cites: 575, 869, 908, 1050, 1201, 1229, 1304, 1341, 1433/1439/1441, 1593, 1621 and 1850. Each fires when a sibling kit or python is absent. Spec 98 §4 pins FLOOR_ASSERTIONS at 'the count the suite prints on the build's node with every block running', and its own §2 S1 keeps the 42-54 skip for 'no kit beside it or no python'. On any such install the executed count falls below the gov-sized pin, so the shipped leg reds on a correct lander. tools/hooks/scratch-guard.test.sh@95c3103ad:1797-1843 has the same kind of executed-count pin, and spec 99 S7 already keeps a host-conditional row out of that floor, so the remedy pattern exists. | sound | - | new:executed-count-floor-sized-to-the-full-install |
| 23 | blast-radius | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 7 leg line, joined with section 4 'Files touched (estimate)' | medium | medium | confirmed | `python tools/check-spec-tokens.py --legs-for skills/session-kickoff/manifest-check.sh tools/gate-legs.json` printed, as non-broad guards, `policy fixtures <- skills/session-kickoff/manifest-check.sh [selftests/kit]` and `policy fixtures <- tools/gate-legs.json [selftests/kit]`. Both paths are in 99 §4 Files touched (lines 241 and 245). The §7 leg line (line 336) does not name `policy fixtures`. .memory-tree.conf:356 sets SPEC_GUARD_LEGS_CUTOFF="2026-09-22", and tools/check-spec-tokens.py@95c3103ad:2219-2230 turns a missing guarded leg into a hit. One caveat: the LIVE regex at line 615 leaves out DEFERRED, so the hit fires once the unit goes INPROGRESS, not today. I ran the same probe over every estimate path of 95, 98 and 99, and no other non-broad guarded leg is missing from any §7 line, so this fix covers the class. | sound | - | gate:spec tokens (a spec's own names resolve) |
| 24 | blast-radius | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-95.md:section 4 'Files touched (estimate)'; the same omission is in TOOL-dPlacedRequest-99 section 4 | medium | medium | confirmed | tools/codebase-map/map_extractors.py@302cdbd3:220-223 builds the `gotcha-classes` inventory from the files under memory/gotchas. `git grep fixture-inherits-ambient-machine-state -- memory/map` found the claim at memory/map/features/unattended.md:22 and in generated/MAP.md and inventories.json. Commit 9565d5680 added three gotchas and also touched memory/map/features/spec-tokens.md (and more). tools/codebase-map/test_codebase_map.py@95c3103ad:142-153 fails on UNCLAIMED keys, and :296 byte-compares the generated files. In tools/gate-legs.json@95c3103ad:924-935 the `codebase-map coverage + freshness` leg has no guard key, so it runs on every change. Spec 95 adds hook-executes-code-resolved-from-its-target.md and spec 99 adds global-set-and-never-read.md and usage-exit-list-lags-its-function.md. Neither spec's Files touched names a dossier or memory/map/generated. Specs 96 and 97 name no new gotcha, and 98 only adds a section to an existing record, so the fix covers every instance. | sound | - | gate:codebase-map coverage + freshness |
| 25 | blast-radius | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-98.md:section 4 'The branch and the count' and Files touched; also TOOL-dPlacedRequest-99 S3 and its Rollout | medium | medium | confirmed | tools/run-gates/selftest-budgets.txt@95c3103ad:114 prices `push-main self-test` at 1032, from readings dated 2026-10-28 (TOOL-dSafePassage-42). `git log -G` shows ff6a6ff79 (2026-10-28) as the row's newest commit. `git log -S write_fence_fixture` shows the block first landing in e20bb81e8 on 2026-11-19, so the row predates arms 42-54. `sed -n 1660,1860p \| grep -c` printed 25 prepare/land calls; the finder recorded 24. memory/gotchas/budget-row-not-remeasured-after-added-arms.md states the rule: 'A commit that raises a suite's FLOOR_ASSERTIONS re-measures that suite's budget row, or says why not.' Spec 98 pins a new floor and spec 99 S3 adds two landing arms and raises it. Neither lists selftest-budgets.txt for this row, and 99 §3 says the opposite: no re-pricing outside S5's loop rows. The fix is instance-level. Spec 95 adds three fixtures and raises the scratch-guard floor, and 99 S7 raises it again, yet neither re-prices the `scratch-guard self-test` row. That is the same class, left standing. | instance | - | class:budget-row-not-remeasured-after-added-arms |
| 26 | blast-radius | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 3 third bullet against section 2 S1; section 4 S5's ceiling sentence | medium | medium | confirmed | Spec 99 §3 line 90 reads 'No re-pricing of a budget row that is not a loop-kit row S5 names'. S1 (line 34), Files touched (line 244) and §5 all re-price `manifest-check self-test`, which is not a loop-kit row, so one non-goal contradicts the scope. `grep` shows budget row 98 at 3820 from a worst reading of 2547 s, and tools/gate-legs.json@95c3103ad:357 sets the ceiling at 4370. With the 574 s that §4 adds, (2547+574)x1.5 ≈ 4682 > 4370. S5's own sentence 'Where a new budget exceeds the leg's ceiling, the ceiling moves' is scoped to S5's rows, and S1 says nothing about the ceiling. One part of the impact is overstated: derive-ceilings.py#cmd_check (lines 668-691) grades the ceiling against ceiling-evidence.txt, where row 82 holds 1400.7 s from the runner, not against the budget. The leg `leg ceilings clear their evidenced maximum` exists at tools/gate-legs.json@95c3103ad:2841. The contradiction between the non-goal and S1 stands either way. | sound | - | class:amendment-leaves-its-other-half-standing |
| 27 | blast-radius | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-95.md:section 4 'The resolver after this unit' and Files touched | low | low | confirmed | `sed -n 697-704 tools/hooks/scratch-guard.js` shows the doc comment: '...the hook's own repository tracks, then the one `cwd`'s repository tracks — gov homes that kit under `skills/`...', directly above `function resolveKickoffChecker(cwd) {`. Spec 95 S1 and its Files touched entry ('the resolver's two rungs and its one call') remove the cwd rung and its parameter but never name the comment. The effect is a stale comment only, with no change in behaviour. | sound | - | new:doc-comment-outlives-the-branch-it-describes |
| 28 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-95.md:section 4 'The arm' and section 6 AC1 | high | - | refuted | The premise is false on re-probe. The claim that no existing arm runs resolveKickoffChecker without a stub does not hold. In tools/hooks/scratch-guard.test.sh, line 34 sets HOOK to the real $HERE/scratch-guard.js. The run_card rows at lines 674-703 feed checkOriented, which calls readCard(common, data.session_id) with no checker at tools/hooks/scratch-guard.js@95c3103ad:907, so the real resolver runs. In gov that resolver answers through rung 2 from __dirname: `git ls-files -- manifest-check.sh '*/manifest-check.sh'` printed only skills/session-kickoff/manifest-check.sh. Those rows need a resolved checker. The deny rows ('AC2 --write card holding the sentinel only -> deny' at exit 2, and 'AC3 card names A, payload from B -> deny'), the 'stderr EMPTY' allow rows, and the AC1 rows that expect the card path in the witness all need the checker's --card --path answer. Against a resolver that returns null, the card reads absent and gives an allow with a '(no card: ...)' witness. Every one of those rows would then red the `scratch-guard self-test` leg, which is on 95's §7 line. So an over-cut resolver is caught. | sound | - | - |
| 29 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-96.md:section 1 Goal, section 2 S1 and section 6 AC1 | high | high | confirmed | Read tools/unattended/unattended.sh#run_entry_claim. It runs `run_lease_verb acquire build "$slug"`. On rc 1 it sets `cause=${line#lease refused — }; cause=${cause%% *}` and calls `claim.py route --cause "$cause"`. tools/loop/claim.py@40976268:91 has `WAIT_CAUSES = ("live-holder", "offered")`, which routes to stamp, wait or expired. Spec 96 §4's restored row keeps acquire at `CW_CAUSE=live-holder; CW_HINT=take-over; return 1`, so the first word after `lease refused — ` is still `live-holder` and entry-claim still waits on a stale build lease. The round-1 record's H2 lists this as consequence bullet 3. Spec 96 §1 names it among the losses that 'This unit restores the row' cures. AC1 and the two arms test only the `--lease` verbs. So the Goal claims a repair the design does not deliver, and nothing checks it. The fault was also present under 71f85d59f's row, which shows the row alone never fixed it. The path is narrow, a dead holder plus a patch or repeat, but the misstatement will mislead the next change, so it is graded high. | sound | - | class:observed-by-claim-no-arm-discharges |
| 30 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-98.md:section 4 'The branch and the count' and section 2 S1 | high | medium | confirmed | tools/govkit/entries/push-main.kit.toml declares `requires = []`. It installs push-main.test.sh and declares the `push-main self-test` gate_leg with subject `kit`, run on demand in adopters. `grep -n skip tools/push-main.test.sh` printed kit-absence skips at lines 575, 869, 908, 1050, 1201, 1229, 1304, 1341, 1433, 1441, 1593, 1621 and 1850, among them no govkit deployer, no policy kit, no run-gates regen.py, no memory-tree kit and no unattended kit. Spec 98 §4 pins FLOOR_ASSERTIONS at 'the count the suite prints on the build's node with every block running'. Its S1 keeps the skip for a lander with no kit beside it, so the spec itself admits partial-kit runs. A partial-kit adopter therefore runs fewer `ok` rows than the gov-pinned floor, and its leg reds over a healthy lander. Nothing in §5 or §6 prices this. The effect is contained: a false red, never a false green, on an on-demand kit leg. Graded medium. | sound | - | new:executed-count-floor-sized-to-the-full-install |
| 31 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 2 S5 and section 4 'S5 — the plant-count token' | high | high | confirmed | Re-probed. An `ast` walk over tools/loop/budget.py printed `PLANTS 34` and `REQUEST_PLANTS 7`. Line 268 is `PLANTS.update(REQUEST_PLANTS)`, and line 1840 builds the self-test's cases from `for c in PLANTS`, so the leg runs 41 plants. tools/gate-legs.json's `loop budget fixtures` leg runs `{prefix}/loop/budget.py --selftest`, and tools/run-gates/selftest-budgets.txt@95c3103ad:90 is its row, so S5 grades it. Spec 99 §4 S5 counts 'a module-level PLANTS dict ... keys by ast'. The check would therefore require and accept plants=34 on a row whose leg runs 41: it certifies coverage it does not check, on exactly the class S5 exists to close. It touches one row today, so it is graded high rather than blocker. | sound | - | new:static-count-misses-a-runtime-grown-collection |
| 32 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 4 'S4 — the freshness rule', rule 1, and section 3 non-goal 2 | medium | medium | confirmed | Read skills/session-kickoff/manifest-check.sh. write_build_card calls read_card_ref, which moves refs/gov/remote/builds/<slug>/card to the fetched tip, before its stored-mode read_card_stored. write_card_cache stores `local` or the commit this node's own publish produced. So a cache whose card-ref is a sha that differs from the ref can only mean the ref moved later through a foreign publish: the ref is the newer one. Spec 99 §4 rule 1, `cache and (cref = local or cref != refc) -> the cache`, picks the stale cache in that case. resolve_build_card (lines 2143-2165) does the opposite: it trusts the cache only when derive_card_verdict calls it fresh, and otherwise reads the ref and rewrites the cache. The two readers disagree on exactly this case. The §3 non-goal names the two S4 plants as the agreement fixture, but per §2 S4 and AC4 both are offline-publish (`local`) plants, so the disagreeing case is never tested. The rule copies the round-2 M2 skeptic's fix verbatim, which does not make it correct. The effect stays within the orientation card, so it is graded medium. | sound | - | class:decision-re-derived-by-a-second-process |
| 33 | failure-envelope | memory/builds/dPlacedRequest/spec/2026-11-20-spec-TOOL-dPlacedRequest-99.md:section 4 'S1 — the plant loop', paragraph after the inventory | low | low | confirmed | Reproduced the probe. `mktemp -d "$W/mfcheck.XXXXXX"`, with W a `cygpath -w` path under my scratch directory, printed a path that kept its backslashes. skills/session-kickoff/manifest-check.test.sh@95c3103ad:7 is `TMP=$(mktemp -d "${TMPDIR:-/tmp}/mfcheck.XXXXXX")`, and line 2385 hands `TMPDIR="$TMP"` to each plant. tools/run-gates/run-gates.sh@95c3103ad:2357-2358 and 2423 derive TMPDIR from the ambient one. So the suite's directory inherits whatever spelling the ambient TMPDIR has. Spec 99 §4 lines 125-126 nonetheless say that directory 'is forward-slashed, so this is a probe's trap and not the gate's'. The ambient TMPDIR here is `/c/Users/...`, which is forward-slashed, so the gate behaves as the spec says on this node. The sentence overstates the immunity, though, and a backslashed ambient TMPDIR would red every plant. That is a wording defect with no behaviour change on the measured node, so it is graded low. | sound | portability-sweep | class:portability-sweep |
