**Serves:** spec-audit TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5

# Spec audit round 3 — the five-unit spec set of dBriefedPass at rev-3, after the round-2 fold

*Node d, 2026-09-01, round 3, unattended prompt-mode run under a standing mandate. Finder lenses primed on the ROUND-2 FOLD — spec 3's new S8 and its S3/S6 rewrite plus AC8 and AC9, spec 4's S2b and S5 rewrite plus AC8 and AC9, spec 1's AC8, spec 2's S5, AC5, AC8 and section-4 rewrite, spec 5's S7 withdrawal, and every rev-3 revision-log entry — then batched skeptics prompted to REFUTE each finding by re-deriving it against the source at the pinned blobs. Round 2's tuning note was carried forward as the priming rule and tightened: a finding survives here only when it joins a spec sentence to a MACHINE — a leg name resolvable in `tools/gate-legs.json`, a byte count, an awk program, a printf format, a line citation, a ratified decision id. Every citation below was re-checked against the tree by the author of this record before it was graded, and the merge decisions in the shape section are stated rather than performed silently.*

**Reviewed subjects, each pinned at the blob it was read at:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-1.md@cb9901eb246e` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md@ac7008c47443` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md@83431e656fb2` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md@2a1eac639824` · `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md@222a8cf4c02f`. **ROUND 3.**

## Verdict: BLOCKED

Three blockers stand after adjudication, against round 2's two. The loop does NOT re-arm under BUILD-METHOD M4, which required strictly fewer than two.

The count needs its arithmetic shown, because one of the three is an upward re-grade and hiding that would be the false-clean shape this corpus exists to refuse. **As filed by the lenses and skeptics, four findings arrived at BLOCKER severity: 1, 7, 8 and 26.** Three of those — 1, 7 and 26 — are one defect reached from three sides, and they collapse into B1 here along with findings 18, 28 and 20, which are the same scope item's remaining unclaimed carriers. That leaves two. **I then promoted finding 21 from HIGH to BLOCKER**, because its mechanism is identical to the one this build has twice already accepted as blocking: a declaration landing without its carrier on an UNGUARDED merge-bar leg, red from the commit that lands it through to landing. Round 1's B1 and round 2's B1 were both graded that way. Finding 21 reds `codebase-map coverage + freshness` — `chunk: declarations`, `subject: repo`, no guard — from the commit that creates `tools/workflows/unattended-build.js` through unit 5. Grading it lower to protect the count would be choosing the number over the standard.

The three blockers say one thing between them, and it is not the thing round 2's two said. **This build now knows how to write a carrier for a CONF KEY and does not know how to write one for a GATE LEG.** Round 2's B1 was a conf key with no protocol carrier; the rev-3 fold closed it properly, with S8, and S8 is a good scope item. In the same fold, spec 3 moved its check into a NEW script and created a NEW leg — and specified that leg as one row in one file. A row in `tools/gate-legs.json` is claimed by four other declarations, three of them on legs that carry no guard. Spec 4 creates a new workflow script and names two declaration files without saying what they declare. The class was left-shifted into one instance and not into the class, which is the exact wording §7 of the charter uses.

B2 is different in kind and worth reading on its own. The rev-3 fold fixed round 2's H1 and H2 by replacing an undeclared callback with a named line of a real file — and named the one return site in that file that structurally cannot carry the value. `tools/workflows/tier2-review.js:383` yields `blockers: null` under a comment that says "null, never 0". Through the channel S2b declares, a CLEAN audit round cannot reach the CONVERGED exit at all.

**Eighteen of the twenty-five confirmed findings were caused by the rev-3 fold**, which is 72% against round 2's 65% and round 1's fold at its own two blockers' worth. The fold rate is rising, not falling, and the reason is visible in H3: spec 3's rev-3 fold moved the check into a new script and updated §4, §6 and §7 while leaving S7 — the scope item that names the test suites — as unmodified rev-2 text. Three sections of one document now name three different test-file sets for one obligation. That is not a hard defect to find and it is not a hard one to prevent; it needs the fold to re-read the sections its own edits invalidated, which is the same prescription round 2 wrote and which was not applied.

## Review shape

- raw 39, confirmed 25, refuted 14, unverified 0, precision 0.64.
- confirmed by severity as ADJUDICATED in this report: **3 BLOCKER · 5 HIGH · 4 MEDIUM · 1 LOW**, over 13 reported items.
- confirmed blockers: 3.
- the 25 confirmed findings collapse into 13 items here. Round 2 reported its clusters as filed; this round MERGES them, and every merge is named in the item's own header so the two rounds stay reconcilable.
- confirmed findings caused by the round-2 fold: 18 of 25 (72%). Pre-existing and missed by rounds 1 and 2: 7.

Precision is measured over the whole raw population of 39 and is unaffected by the merging, which happens after grading. It rose from 0.49 to 0.64 under the tightened priming rule — the raw population fell from 41 to 39 while the confirmed count rose from 20 to 25. **Two rounds of tuning have now taken this corpus from 0.21 to 0.49 to 0.64 on the same subject, and the whole intervention is the priming sentence.** That is worth carrying out of this build: on a pre-code spec audit, priming the lens to join a spec sentence to an executable source is the single highest-value knob available, and it costs one paragraph of prompt.

One number deserves a caveat rather than a footnote. The confirmed count ROSE while the blocker count also rose, on a spec set that has now had two folds. That is not a converging loop, and the merge to 13 items should not be read as improvement — 25 findings survived a skeptic here against 20 last round.

## The two hunts round 2 named for this round

Round 2 closed by naming two specific things for round 3 to check. Both were run, and they came back with opposite answers.

**Hunt 1 — did spec 5's S7 withdrawal leave a dangling reference, in that document or in spec 2? CLEAN. No finding.** Every occurrence of `S7` in spec 5 is inside the withdrawal itself or in the rev-3 log entry that records it, and spec 2's own `S7` is an unrelated scope item of its own (its test arms), referenced consistently in its §5 Testing bullet and its §7. Nothing in either document reads through to the withdrawn claim. The withdrawal is the cleanest edit in this fold and it is the one that closed five findings at once. Two adjacent numbers did survive the withdrawal and are NOT reported as findings, because neither joins to a machine: §5's "reverting is the seven files and the pin" and §10's "seven named carriers" both author a count beside the §4 table that §4's own M6 fold declared owns it. Both currently read TRUE against the table's seven files. They are noted here so the next fold sees them, not graded.

**Hunt 2 — is `check-pass-order.sh` fully specified as a NEW gate leg: row shape, ceiling, guard, and whether anything else must declare it? NO, on every one of the four.** This is B1, and it is the largest single item in this report. The spec declares one of the four (the ceiling). It does not declare the row's `chunk`, which `tools/run-gates/run-gates.gov.test.sh` requires unconditionally from a closed set of six; it does not declare the row's `subject`, which decides whether the bar runs the leg at all; it does not state a guard decision either way; and it names none of the four other files that must claim the leg in the same commit. Three of those four claims are enforced by legs that carry NO guard, so the omission is not a latent risk — it is a red bar from the commit that lands unit 3 through to landing. M4 adds the fifth thing nothing declares: the new script's own self-test is registered in no runner at all.

## B1 (findings 1, 7, 18, 26, 28 and 20) — a row in `tools/gate-legs.json` is not a declared leg, and four other declarations must land in the same commit

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` §2 S6 · §4 Files touched · §6 AC9.

Six confirmed findings, filed by four separate lenses, reaching one defect from the descriptor side, the registry side, the subject-pin side, the row-shape side and the codebase-map side. They are merged because the fix is one commit and one scope item; they are enumerated because a builder needs all five carriers, and closing four of them still reds the bar.

S6 says the check "is registered in `tools/gate-legs.json` as its OWN leg with its own declared ceiling, pointing at the new script", and §4 Files touched names `tools/gate-legs.json` and no other declaration file. AC9 asks for the row to be "present in `tools/gate-legs.json` with a numeric `ceiling`". That is the whole of the spec's account of how this leg comes into existence.

Here is what a manifest row actually obligates, each verified at the cited line:

| what else must claim the row | enforced at | on which leg | guarded? |
|---|---|---|---|
| a `[[gate_leg]]` block in `tools/unattended/kit.toml`, or an `[[exempt_leg]]` row with a non-empty `why` in `tools/govkit/registry.toml` | `tools/govkit/govkit.py:1390` | `govkit selfcheck` | **no** |
| that block's explicit `subject`, which must AGREE with the manifest's | `govkit.py:1317` and `:1345` | `govkit selfcheck` | **no** |
| a row in `tools/govkit/subject-pins.tsv`, regenerated by `selfcheck --write` | `govkit.py:1463` | `govkit selfcheck` | **no** |
| the leg NAME claimed in a map dossier — `memory/map/features/unattended.md` claims two legs and this is a third | `tools/codebase-map/test_codebase_map.py:79-90` | `codebase-map coverage + freshness` | **no** |
| the regenerated `memory/map/generated/MAP.md` and `inventories.json`, byte-compared | `test_codebase_map.py:126` | `codebase-map coverage + freshness` | **no** |
| a `chunk` from the closed six `records product wiring declarations selftests e2e` | `tools/run-gates/run-gates.gov.test.sh:337-346` | `run-gates gov canary` | held, see M3 |

The two failure strings are verbatim: `gate leg '<n>' is claimed by no descriptor and carried by no [[exempt_leg]] — a new leg must red until a declaration says whether an adopter receives it`, and `gate leg '<n>' has no row in tools/govkit/subject-pins.tsv — a NEW leg reds until its subject is on the record`. The map one is `UNCLAIMED (new key? claim it in a feature dossier ...)`.

The `govkit selfcheck` row is `{"name": "govkit selfcheck", "argv": ["python", "tools/govkit/govkit.py", "selfcheck"], "chunk": "declarations", "subject": "repo", "ceiling": 310}` with **no `guard` key**. `codebase-map coverage + freshness` is `{"chunk": "declarations", "subject": "repo", "ceiling": 300}`, also **unguarded**. `tools/run-gates/run-gates.sh:947` holds a leg only when `subject == kit || chunk == selftests`, and neither qualifies. Both run on every bar.

**Impact.** The commit that lands unit 3's manifest row reds two unguarded merge-bar legs on at least three assertions, and no later unit of this build claims the leg either — so the bar stays red through units 4 and 5 and into landing. This is the identical shape round 1's B1 and round 2's B1 both blocked on, third instance, same mechanism. The fold's own remedy for the last one, S8's "LANDS WITH ITS PROTOCOL CARRIER", was written for exactly this class and was applied to the conf key alone.

There is sibling evidence that this is an oversight rather than a decision: spec 4's §4 Files touched DOES list `tools/workflows/kit.toml` beside `tools/gate-legs.json` for its own new file. Spec 3 lists neither `tools/unattended/kit.toml` nor `tools/govkit/registry.toml` nor `tools/govkit/subject-pins.tsv`, and grep across all five specs finds zero occurrences of any descriptor or exempt-leg concept in spec 3.

**The row's own shape is the second half, and it is load-bearing.** S6 declares a ceiling and nothing else. `run-gates.gov.test.sh:337-346` reds UNCONDITIONALLY on any row whose `chunk` is absent or outside the closed six, with its own comment saying a new leg added without a key "would otherwise fall into `default` silently". All 86 current rows carry `chunk`, `subject` and `ceiling`; none is optional in practice. And `subject`/`chunk` are what decide whether the leg RUNS: a row declaring `subject: kit` or `chunk: selftests` is held off every default bar and off the push boundary, so the unit whose entire product is a merge-bar refusal would ship a refusal that never runs. No guard decision is stated either, on a check §5 itself prices at one `git log` per build over 84 build folders — the cost class `TOOL-aCollapsedScan-4` is open on, and the very reason §3 gives for this leg existing separately.

**Fix.** Rewrite S6 in the shape S8 already uses. State the full row: `name`, `argv`, `chunk` (`declarations` matches the sibling `unattended kit gate` row), `subject: "repo"` (matching this kit's three existing blocks), a numeric `ceiling`, and either `guard: []` with the reason it is unguarded or the guard pathspecs. State that the row lands in ONE COMMIT with: a `[[gate_leg]]` block in `tools/unattended/kit.toml` mirroring `:83-88` — which ships the leg to every adopter, a decision the spec must make and state — or, if the leg is deliberately gov-only, an `[[exempt_leg]]` row in `tools/govkit/registry.toml` with a non-empty reason; a `tools/govkit/subject-pins.tsv` row regenerated with `python tools/govkit/govkit.py selfcheck --write`; the new leg name added to `memory/map/features/unattended.md`'s `gate-legs` claim with its dossier prose refreshed; and the regenerated `memory/map/generated/` artifacts. Add all of those to §4 Files touched. Add `govkit selfcheck` and `codebase-map coverage + freshness` to §7, and extend AC8's shape with a criterion asserting `python tools/govkit/govkit.py selfcheck` and `python3 tools/codebase-map/test_codebase_map.py` both GREEN with the new leg declared.

**Left-shift.** This is the third instance of one class in three rounds, so the gate is owed rather than optional. Add an arm to `tools/run-gates/run-gates.gov.test.sh` — already the leg that closes over the manifest — asserting that every `tools/gate-legs.json` name is reachable from a kit descriptor's `[[gate_leg]]`, a `[[exempt_leg]]` row, a `subject-pins.tsv` row AND a map dossier claim, and print the four-way join as one message naming which of the four is missing. Today a builder discovers those four one red bar at a time, from four different scripts, which is why three rounds of a spec audit have each had to re-derive the same list. The cheaper half, available immediately: `tools/memory-tree/TEMPLATE-SPEC.md` gains a line requiring any spec whose §4 Files touched names `tools/gate-legs.json` to also name a descriptor or registry file, a subject-pins row, and a map dossier — a grep-shaped check over spec front matter that the memory hygiene gate can carry.

## B2 (finding 8) — S2b declares the one return site that yields `blockers: null` by design, so CONVERGED is unreachable

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md` §2 S2b, against §6 AC7 and §2 S5.

S2b declares the blocker count's channel as: "The blocker count it passes comes from the same `workflow()` return the AUDIT stage already receives — `tier2-review.js:383` yields `{confirmed, blockers, highs, ...}`."

Line 383 is the `allFindings.length === 0` return. Verbatim, with the comment immediately above it:

    // TOOL-dTieredTribunal-1 S3 - null, never 0: no synthesis ran on this path either.
    return { confirmed: [], report: null, root: repo, blockers: null, highs: null, ... }

It is one of three such sites. `:373` is the all-lenses-dead return, `:383` is the zero-findings return, `:476` is the every-finding-refuted return, and all three carry the same "null, never 0" comment. The ONLY path that yields an integer is `:608`, `blockers: synth ? synth.blockers : null`, on the adjudicated synthesis return — and `:603-607` explicitly refuses `synth?.blockers || 0` by name as "the false-clean class this file exists to refuse".

**Impact.** A CLEAN audit round — nothing found, or everything refuted — returns `blockers: null`, never 0. On the driver side, `unattended.sh:3768` prints CONVERGED only on a count of 0, and `:3821` refuses a non-integer outright: `fail 37 "--review requires --blockers as a plain integer, because the predicate compares this round's count against the previous one and cannot compare prose"`. So through the channel S2b DECLARES, the CONVERGED exit is structurally unreachable. A clean audit either refuses at the driver — and, by S5's required `verdict` field, refuses again at the harness for want of a verdict — leaving a loop with no clean exit and no round cap of its own by S2b's last sentence; or an implementer fabricates the 0 that the engine's own comment forbids and the harness reads convergence off a review whose every lens died. AC7's `CONVERGED` arm cannot be satisfied as written.

Round 2's H1 and H2 fix replaced an undeclared callback with a named line of a real file. That was the right move. It named the wrong line, and the defect moved rather than closed.

**Fix.** In S2b, name `tier2-review.js:585` as the adjudicated return site, whose `blockers` at `:608` is the only path yielding an integer. Then add the null case as a DECLARED STATE rather than an omission: a `blockers` of null means "no synthesis adjudicated a count"; the AUDIT stage must NOT pass it to `--review` as 0; and the harness treats it as a refusal in the same way S5 already treats an absent `verdict`. Add an AC arm asserting that an AUDIT return carrying `blockers: null` is refused rather than converted, alongside AC9's missing-verdict arm.

**Left-shift.** The class is "a spec cites a line of a real file as the source of a value that line does not carry". It is gateable cheaply and generally: a check over every `<path>:<line>` citation in a build's spec set that the cited file has that many lines and that the line is non-blank, which catches the stale-citation half; and, for the harder half, a `tools/workflows/unattended-build.test.sh` arm pinning the contract in the direction that matters — assert `tier2-review.js` returns a non-integer `blockers` on each of its three early-return paths, so that a future refactor making them integers is what reds, not silence. That arm belongs to unit 4 regardless of this fix.

## B3 (finding 21) — `tools/workflows/unattended-build.js` is a new inventory key against an EMPTY baseline, claimed by nothing

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md` §4 Files touched.

**Graded up from HIGH as filed.** The mechanism is identical to B1's map half and to round 1's and round 2's accepted blockers: an unclaimed key on an UNGUARDED merge-bar leg, red from the commit that creates the file through to landing. The standard is the build's own, applied twice; applying it a third time is what consistency costs.

`map_extractors.py` globs `tools/workflows/*.js` into the `workflow-scripts` inventory. `memory/map/baseline.toml:48-49` carries `workflow-scripts = [ ]` — an EMPTY list, so unlike `gate-legs` there is no baseline escape hatch at all and every script must be claimed by a dossier. `memory/map/features/review-harnesses.md:19-24` claims exactly four: `check-workflow-syntax.js`, `drift-audit-code.js`, `drift-audit-state.js`, `tier2-review.js`. Not `unattended-build.js`.

**Impact.** `codebase-map coverage + freshness` — `chunk: declarations`, `subject: repo`, **no guard** — reds with `UNCLAIMED` on the commit that creates the file and stays red through unit 5 and landing. The new file also adds JS symbols, so `memory/map/generated/symbols.json` and `MAP.md` go stale in the same commit and fail `test_generated_artifacts_are_fresh`, which byte-compares them. §4 Files touched lists four files and the map tree appears in no section of the document; §7 Gates names `workflow script syntax`, `verifier fan-out`, `harness arms` and `review-join ban`, and no map leg.

**Fix.** Add to §4 Files touched: `memory/map/features/review-harnesses.md`, claiming `unattended-build.js` under `workflow-scripts` with its dossier prose refreshed, and `memory/map/generated/` regenerated in the same commit. Add `codebase-map coverage + freshness` to §7. If H5 resolves toward a new leg for the arms test, the leg NAME is a second unclaimed key in the same commit and needs the same treatment plus B1's four declarations.

**Left-shift.** Same gate as B1's, one inventory over: the spec-shape check should require any spec creating a file under a globbed inventory root to name a dossier in §4. The mechanical version is cheaper than it sounds — `tools/codebase-map/map_extractors.py` already knows every glob root, so a check can read the roots from the extractor and grep the spec set's §4 sections for a `memory/map/features/` path whenever a new file lands under one. That is the derive-over-author shape, and it removes the need for any future spec author to know the inventory list.

## H1 (findings 2, 13, 19 and 30) — AC9's scheduling witness is an observation the runner cannot emit, so the criterion cannot fail

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` §6 AC9.

Four confirmed findings, four lenses, one defect. AC9 says the row is "present in `tools/gate-legs.json` with a numeric `ceiling`, and `bash tools/run-gates/run-gates.sh` SCHEDULES it — witnessed by the runner's unbounded-leg warning naming zero new legs".

The warning, at `tools/run-gates/run-gates.sh:961-968`, is one aggregate line:

    [ "$unbounded" -gt 0 ] && printf 'run-gates: %s of %s legs that will run declare no ceiling and run unbounded\n' "$unbounded" "$willrun" >&2

It prints COUNTS and no leg names, ever, and only when the count exceeds zero. AC9's other half already requires a numeric ceiling, so the new leg never contributes to `unbounded` in any case. `TOOL-aCollapsedScan-5` records — and this tree confirms — that all 86 current rows carry a ceiling, so the line never prints at all today.

**Impact.** The expected observation is NO LINE. That silence is produced identically by: a scheduled leg with a ceiling; a leg HELD as `ondemand` at `:947` because its `subject` is `kit` or its `chunk` is `selftests`, which never reaches the `willrun` increment at `:963-965`; a guard-skipped leg; and a leg absent from the manifest entirely. The criterion cannot distinguish any of these. The unit whose entire product is a merge-bar refusal can therefore land a refusal that never runs, with AC9 green — the green-by-absence class §7 of the charter names, one level up from where this spec set correctly cites it.

AC9 was added at rev-3 specifically to close round 2's H3, "the unit had no criterion reading its own manifest row". The fix reproduced the defect one level over: the unit now has a criterion reading its manifest row, and that criterion cannot fail on the half that matters.

**Fix.** Re-anchor AC9 on a positive artifact the run leaves behind, keeping the ceiling half as its own separate assertion over the row. Assert the leg's NAME appears with a verdict in a default `bash tools/run-gates/run-gates.sh` per-leg report, and specifically NOT as `GATE held  <name>  (self-test, set GATE_SELFTESTS=1 to run)`; or assert a row keyed on that name in `<git-dir>/gate-ledger.tsv` after the run. Both exist only if the leg actually ran. Then extend the row-shape half per B1 so `chunk` and `subject` are asserted too, since those are what decide scheduling.

**Left-shift.** The general class — "an acceptance criterion whose witness is the ABSENCE of output" — is the most reported shape across all three rounds of this audit and has now appeared in four specs. Gate it in the spec template rather than in a runner: add a `TEMPLATE-SPEC.md` rule that a criterion may not be satisfied by silence, and a memory-hygiene arm that flags any AC containing "naming zero", "no line", "does not appear", "warning ... zero" or "absent from" without a paired positive assertion. It will have false positives, and a spec author writing a genuine negative criterion (spec 5's AC5 is one, and it is correctly built on `git diff --name-only` output rather than on silence) can say so in one clause. The alternative is finding this by hand in round 4.

## H2 (findings 11, 36 and 15) — `check-wiring.sh --check` is named as the `unattended skill wiring` leg in two specs; that leg is a different script

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-2.md` §6 AC7 second half, and `...-5.md` §6 AC2 with its §4 inventory row for `.claude/skills/unattended/SKILL.md`.

Spec 2's AC7 says `bash tools/check-wiring.sh --check` "reports the installed Skill matching tracked, which is the `unattended skill wiring` leg over the RENDER half of S8's carriers". Spec 5's AC2 says the same command "reports the installed Skill matches tracked, so the render in `.claude/skills/unattended/` is not left behind", and its §4 inventory row grades that render with `check-wiring.sh`.

That leg's argv, in `tools/gate-legs.json` and identically in `tools/unattended/kit.toml`, is `["bash", "tools/unattended/adopt-unattended.sh", "--check"]`. A different script. `tools/check-wiring.sh` appears in no bar leg's argv except its own held self-test, `check-wiring self-test`, `chunk: selftests`. Its only skill arm is `check_skill_install()` at `:563-616`, hard-scoped to `${HOME}/.claude/skills/session-kickoff` against `skills/session-kickoff/`, returning early when that install is absent; grepping the whole file for `unattended` returns comments and an eol-attribute sweep over `.claude/skills/**.md`, which reads line endings and not render freshness. `.claude/skills/unattended/SKILL.md` is written and diffed by `adopt-unattended.sh:181-182`.

**Impact.** In spec 2, AC7 is the ONLY criterion covering S8's render half — the criterion added at rev-3 to close round 2's H5 — and it certifies a command with no arm over that render, so a stale render passes AC7 and the leg §7 names reds afterwards. In spec 5, the §4 inventory row and §7 name two DIFFERENT graders for one artifact, which is the two-answers-to-one-question shape this spec set invokes against itself elsewhere. Both specs' §7 sections name the leg correctly; only the criteria are wrong.

**Fix.** One substitution in both documents. Spec 2 AC7's second command becomes `bash tools/unattended/adopt-unattended.sh --check`, described as the `unattended skill wiring` leg; `tools/check-wiring.sh --check` may stay as an additional convenience clause but must not be described as that leg. Spec 5 AC2 takes the same command, and its §4 inventory row's `graded by` cell changes from `check-wiring.sh` to `unattended skill wiring`, matching its own §7.

**Left-shift.** Every spec in this set already claims "Every name resolves against `tools/gate-legs.json`" in §7, and three rounds have found that claim broken by name (round 2's M1, and the rev-3 logs of specs 3, 4 and 5 each record dropping a leg name that resolved to nothing). Extend that check one field further: a memory-hygiene arm that, for any spec sentence naming a leg AND a command in the same clause, asserts the command matches that leg's `argv` in `tools/gate-legs.json`. The manifest is JSON, the specs are greppable, and this is the second distinct defect class the pair has produced.

## H3 (finding 9) — three sections of spec 3 name three different test-file sets for one obligation

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` §2 S7, against §4 Files touched, §6 AC5/AC6 and §7.

- S7, lines 59-61: arms go in `tools/unattended/unattended.test.sh` and `tools/unattended/check-unattended.test.sh`.
- §4 Files touched, lines 115-118: lists `tools/unattended/check-pass-order.test.sh` (NEW) and `tools/unattended/unattended.test.sh`, and never `check-unattended.test.sh`.
- AC5 and AC6, lines 145 and 147: both say "in `tools/unattended/check-pass-order.test.sh`".
- §7, lines 166-168: the arms are witnessed by running `unattended.test.sh` and the new `check-pass-order.test.sh` directly.

**Impact.** S7 is unmodified rev-2 text from when the check lived inside `check-unattended.sh`; the rev-3 log at lines 183-188 records the move, and the fold updated §4, §6 and §7 without re-reading the scope item that names the suites. A builder following §2 writes the leg's negative arms into `check-unattended.test.sh` — a suite whose subject is a script that no longer carries the check, and a file this unit's declared surface does not include — so the arms AC5 and AC6 grade end up in neither place, or in both. Nothing in the unit legitimately belongs in `check-unattended.test.sh`: S1's and S2's refusals are in the driver, S3's are in the new script, and AC8 asks only that `check-unattended.sh` run green, not for a staged arm.

**Fix.** Rewrite S7 to name exactly the suites §4 and §6 name: `tools/unattended/unattended.test.sh` for S1's and S2's dispatch refusals, and the NEW `tools/unattended/check-pass-order.test.sh` for S3's history-join arms. Drop `check-unattended.test.sh`, or — if check 22's new-key arm is meant to live there — add it to §4 Files touched and say which acceptance criterion reads it.

**Left-shift.** This is the fold class in its purest form and it is the cheapest one to gate: a self-consistency check over a spec document asserting that every file path named in §2 also appears in §4 Files touched, and vice versa. Purely mechanical, no judgement, and it would have caught this instance, round 2's M2 and part of H5 below. It belongs beside the existing spec-header checks in the memory-tree kit, and it is the single highest-value gate this report recommends, because 18 of 25 findings this round trace to a fold editing one section and not its neighbours.

## H4 (finding 10) — spec 5's S6 asks `kit.toml` to record a version bump; that file carries no version and its named leg never reads it

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §2 S6 and the §4 inventory row for `tools/unattended/kit.toml`, against §7.

S6 says "`tools/unattended/kit.toml` records the version bump", and §4 grades that row with `kit version markers`. `tools/unattended/kit.toml` carries no version literal at all — it declares `version_from = { file = "unattended.sh", pattern = "^KIT_UNATTENDED_VERSION=" }`. The named leg, `tools/check-kit-versions.sh:144-171`, never opens `kit.toml`: it reads `KIT_UNATTENDED_VERSION=1.14` from `tools/unattended/unattended.sh:41`, requires the same constant PLUS a same-line `gov:kit unattended@1.14` marker in both `unattended.sh` and `check-unattended.sh:40`, and requires a matching marker in EVERY tracked `tools/unattended/*.template.md`. Today those are `PLAYBOOK-TEMPLATE.template.md`, `PROTOCOL.template.md` and `SKILL.template.md`, each at `@1.14`.

**Impact.** §4 Files touched delegates this unit's entire surface to the inventory table, so `unattended.sh`, `check-unattended.sh` and `PLAYBOOK-TEMPLATE.template.md` are all outside it — and `PLAYBOOK-TEMPLATE.template.md` is touched by no unit of this build at all. Following S6 literally is a no-op: editing `kit.toml` bumps nothing and S6 is silently unfulfilled. Doing the bump partially — `unattended.sh` alone, or the three files the table does name — reds `kit version markers`, an unguarded `subject: repo` leg that runs on every bar, on up to four separate assertions at once. §5's "reverting is the seven files and the pin" is wrong on the same count, and §6 carries no criterion over the bump at all.

**Fix.** Replace the `kit.toml` inventory row with the files the leg actually reads: `tools/unattended/unattended.sh:41` and `tools/unattended/check-unattended.sh:40`, each carrying the constant and its same-line `gov:kit unattended@` marker, plus the `gov:kit unattended@` marker in every tracked `tools/unattended/*.template.md` — noting explicitly that `PLAYBOOK-TEMPLATE.template.md` is in that derived population. Add a criterion asserting `bash tools/check-kit-versions.sh` GREEN after the bump. If unit 5 is not the unit that owns the bump, withdraw S6's version clause and name the unit that does.

**Left-shift.** The class is "a spec names a file as the site of an act that file cannot perform, and grades it with a checker blind to it". `check-kit-versions.sh` already knows the exact population it reads; make it say so. Add a `--explain` mode printing the files and markers it will compare for a named kit, so a spec author writing a version-bump scope item can paste the real list instead of guessing at `kit.toml`. That is derive-over-author applied to a spec's input, and it costs one function.

## H5 (findings 12 and 6) — spec 4's §4 names the exact file pair a new gate leg requires, and no section declares a leg

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md` §4 Files touched, against §2, §6 and §7.

§4 lists `tools/workflows/kit.toml` and `tools/gate-legs.json`. `tools/workflows/kit.toml:10-12` already declares `[[files]] include = "**"` with `role = "engine"`, so the two new files need no `[[files]]` entry — the only edit a `kit.toml` can carry here is a `[[gate_leg]]` block. Yet no scope item declares a leg: S7 names three pre-existing checks, S8 only names the new arms file. No §6 criterion observes a manifest row — AC1's citation `tools/workflows/kit.toml:59` is the `argv` line of the EXISTING `workflow script syntax` block, not a new row. §7 lists only pre-existing legs.

**Impact.** The spec is silent on whether `tools/workflows/unattended-build.test.sh` becomes a leg, and the dilemma is real in both directions. If it does, four further declarations bind that nothing here names: the `[[gate_leg]]` block with an explicit `subject` (`govkit.py:1317`), a `tools/govkit/subject-pins.tsv` row (`:1463`) — both on the unguarded `govkit selfcheck` leg — a `chunk` from the closed six (`run-gates.gov.test.sh:337-346`), and the assertion-count contract `tools/check-testsuite-counts.sh` enforces over every `*.test.sh` the manifest names. Worth stating: the sibling `tier2-review self-test` in that same descriptor is `subject = "kit"`, which holds it off the default bar, so an arms suite declared the same way would run nowhere by default. If it does not become a leg, then the two declaration files should not be in this unit's diff at all and S8's arms have no runner named. Round 2's H3 raised exactly this against spec 3; the fix landed in spec 3 alone and the identical shape survived one document over.

**Fix.** Decide it in §2. Either S8 states the arms test lands as a leg — naming its `subject`, `chunk`, `ceiling`, guard, its `[[gate_leg]]` block in `tools/workflows/kit.toml` and its `subject-pins.tsv` row, all in one commit — with a criterion asserting `python tools/govkit/govkit.py selfcheck` and `bash tools/check-testsuite-counts.sh` green; or the two declaration files leave §4 and S8 says the arms are witnessed by running the suite directly with the verdict owed in the landing report, which is the disposition §7 of specs 1, 2 and 3 already use for the same reason.

**Left-shift.** Covered by B1's four-way join gate, which would red on the ambiguous branch and stay silent on the clean one. The complementary half is the §2-to-§4 path-consistency check from H3: `tools/gate-legs.json` in §4 with no §2 sentence naming a leg is precisely the asymmetry that check reports.

## M1 (finding 5) — spec 5's S1 is the unit's headline product and no criterion of any kind reads it

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-5.md` §6 AC6, against §2 S1.

AC6 grades exactly one thing: that `memory/guides/UNATTENDED-PROTOCOL.md` states both limits from S2. S1's three protocol statements — the harness is the route for `prompt` and `slug` modes, a build pass owes a recorded brief, and a build pass is declared through `--dispatch` — have no criterion at all. AC1, AC2, AC3, AC4, AC5 and AC7 are the parity legs, the Skill render, the directive handle, the `DIRECTIVES_FLOOR` pin, the BUILD-METHOD negative and the check-26 join.

**Impact.** §4 states in the spec's own words that the parity legs compare the two COPIES to each other and that "a claim false in both is green", so no leg can reach S1's prose either. The section can land empty, wrong, or missing the `--dispatch` sentence — the sentence that makes `TOOL-dBriefedPass-3`'s refusal reachable on a SEQUENTIAL pass rather than only a concurrent one — with every criterion green. That is a cross-unit join, not a documentation nicety: spec 3's product is weaker without it and nothing in either spec would say so.

**Fix.** Widen AC6, or add an AC in its shape, naming S1's three statements alongside S2's two limits as what the closing review reads out of the protocol, quoting the handle or phrase each must contain. AC6 already gets this construction right — it names the closing review as the explicit reader "rather than pretending a leg reads prose" — so the fix is to extend the pattern, not to invent one.

**Left-shift.** Not gateable as prose, and it should not be faked. The documented check is a spec-template rule: every §2 scope item is named by at least one §6 criterion, and a spec whose §6 covers fewer scope items than it has must say which reader grades the remainder. A mechanical version is available and cheap — count `S<n>` handles in §2, grep §6 for each — and it would have caught round 2's M4, round 2's H4, this finding and part of H5.

## M2 (finding 24) — the harness declares `briefDir` and `briefPath` and no stage ever records a brief

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-4.md` §2 S4 and the §4 data model.

§4 declares `briefDir` ("where the SPEC stage writes each unit's brief") and a `briefPath` per unit, and S4 hands the BUILD agent "its brief path and its spec path and nothing else". **`--brief` appears nowhere in spec 4**, verified by exhaustive grep of the document.

**Impact.** `TOOL-dBriefedPass-5` S1 puts "a build pass owes a recorded BRIEF" into the protocol, and `TOOL-dBriefedPass-2` S1 makes the run-state row the only place that obligation is observable — spec 2's §1 says the brief is "written by a driver verb so it cannot be composed after the fact or LEFT OUT". Nothing makes that verb reachable on the harness route. The capability plainly exists and is simply unspent: S2b already establishes that a stage agent may shell out to a driver verb, and §3's non-goal list (orientation, preflight, owner turn, closing, landing, keepalive) does not exclude recording. So on the route this build ships, the obligation lands back on an agent's recollection, which is the defect this build's own README opens by naming. Compounding it, spec 2's S6 refuses an UNTRACKED `--path`, so the brief must be committed before it can be recorded — an ordering no stage in §2 carries.

**Fix.** Add to S4, or a new S4b, that the stage which writes a brief also COMMITS it and calls `bash tools/unattended/unattended.sh --brief <slug> --unit <id> --path <file>`, and state where that call sits relative to the BUILD agent's dispatch. Add an arm to `tools/workflows/unattended-build.test.sh` asserting the recorded-brief call is emitted once per unit.

**Left-shift.** The declared-and-unspent field is a gateable class inside this build's own product: `tools/unattended/check-pass-order.sh`, which B1 is about, is already walking CLOSED units and their build commits. A sibling term asserting that every unit with a build commit also carries a `brief` row in the run-state file would turn spec 5's protocol sentence into a machine refusal, which is the whole thesis of this build. Until then, the documented check is that the closing review reads the run-state file for one `brief` row per built unit.

## M3 (finding 29) — spec 3's §7 names two legs its own gate line cannot run

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` §7 Gates.

§7 leads with the bare `bash tools/run-gates/run-gates.sh` and then names `run-gates canary` and `run-gates gov canary` as "the legs that actually grade a manifest row". Both carry `chunk: selftests`. `run-gates.sh:947` marks any leg `ondemand` when `subject == kit || chunk == selftests` and `GATE_SELFTESTS` is empty, and the comment block immediately above records the owner's 2026-08-26 ruling that the CHUNK is held too — naming the two run-gates canaries explicitly among the six `subject: repo` legs it holds, and stating that `GATE_FULL=1` deliberately does NOT ask for them.

**Impact.** The bare invocation §7 leads with runs neither canary, so the unit whose entire product is a merge-bar refusal names two witnesses it will never produce. The concrete consequence is B1's missing-`chunk` half: it would go unobserved on every gate run this build makes. The spec demonstrably knows about the on-demand split — it applies it correctly to the driver suite in the very next sentence — and does not apply it to the canaries.

**Fix.** §7 spells `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` beside the two canaries and owes their verdict in the landing report, exactly the way the same section already handles the 2026-08-23 driver-suite ruling.

**Left-shift.** Standing prior art exists as a memory note ("kit self-tests are held — a DoD needs `GATE_FULL=1 GATE_SELFTESTS=1`"), and a note is not a gate. Make it mechanical in the spec-shape check: any §7 Gates section naming a leg whose manifest row is `chunk: selftests` or `subject: kit` must also name the invocation that runs it. The manifest is the single source and the lookup is exact, so this has no judgement in it.

## M4 (finding 32) — the new self-test is registered in no runner, and the kit's compensating check reds a suite that arrives without a budget

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-3.md` §2 S7 and §4 Files touched.

`tools/unattended/check-pass-order.test.sh` is created by §4 and registered nowhere. Not on the bar — correct, by the owner's 2026-08-23 ruling. And not in `tools/unattended/run-unattended-gates.sh`, whose suites are eight explicit `run_one` lines at `:170-178` against a hand-declared `BUDGET_*` block at `:46-53`. There is no ratchet enumerating tracked `*.test.sh`, and `:159-166` reds a suite arriving without a budget: "A MISSING BUDGET IS ITSELF A FAILURE. A suite added here without one would be exempt from the rule by the act of arriving, which is how every population in this repo has previously gone quiet."  Grep finds zero mentions of `run-unattended-gates.sh` in any of the five specs.

**Impact.** `tools/unattended/kit.toml:59-79` names that runner as the ENTIRE compensating check standing in for the removed legs, and says in its own words "There is no gate behind that sentence". A new checker in this kit whose self-test sits outside the runner is exercised exactly once — in this build's landing report — and never again. `TOOL-cSettledDocket-7` is the open row for precisely this class: a suite nobody runs is one nobody notices going quiet.

**Fix.** S7 adds a `run_one "pass order selftest" selftests` row for the new suite and a `run_one "pass order gate" checks` row for the checker itself, each with its measured `BUDGET_*` pin, and §4 lists `tools/unattended/run-unattended-gates.sh`. Or §3 records why not, citing `TOOL-cSettledDocket-7`. Note the ordering trap: the budget must be MEASURED, and `:159-166` reds the runner until it exists, so the pin lands in the same commit as the `run_one` row.

**Left-shift.** The registration itself is what needs deriving, not remembering. `run-unattended-gates.sh` should assert that every tracked `tools/unattended/*.test.sh` is named by exactly one `run_one` line — a liveness assertion over its own population, in the same spirit as its missing-budget refusal — so a suite that arrives unregistered reds the runner instead of being silently absent from it. That closes the class rather than this instance, and it is a few lines in a script that already reds on the adjacent omission.

## L1 (findings 14 and 38) — the `§` count in spec 1's AC8 and its rev-3 log is wrong, and read two incompatible ways

**Address:** `memory/builds/dBriefedPass/spec/2026-09-01-spec-TOOL-dBriefedPass-1.md` §6 AC8 and the §9 rev-3 entry.

AC8 scopes itself away from a whole-file assertion on the ground that the file has "27 other `§` references". The rev-3 log gives the same number differently: "a whole-file `§` count is 27 in both halves". Two incompatible readings of one measurement, and neither reproduces. Measured on the tracked blobs at HEAD on a clean tree: `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/BUILD-METHOD.template.md` each carry **30** occurrences of `§`. M2's two classification lines, 44 and 45, hold **4** of them (`§2`, `§6`, `§7` on the THIN line, `§8` on the FORKED line), leaving **26** others. No reading yields 27.

**Impact.** Confined to the rationale, which is why this is LOW rather than higher — one finder graded it MEDIUM and the reasoning that carried the day is that AC8's actual assertion is sound and stays falsifiable. What it costs is a builder who re-measures before asserting: they get 30 and 26, cannot tell whether the criterion describes this file or an earlier one, and must resolve that doubt by hand. AC8 exists precisely because round 2 found S6 with no criterion that could fail, so a false number in ITS justification is the wrong place for this class to appear. §7 of the charter states it outright: no count of a derived population is written in prose. This build's own M6 fold removed exactly this class from spec 5 in the same round it authored this one.

**Fix.** Drop the figure and keep the qualitative ground — "the file's other `§` references are unrelated, so a whole-file count cannot fail" — in both AC8 and the rev-3 entry. The criterion does not depend on the number. If a number is wanted, it is 30 whole-file and 26 outside M2's two lines, and it will be wrong again on the next edit to that file, which is the argument for dropping it.

**Left-shift.** Already a charter rule with no gate behind it, and it has now been broken in two specs in two rounds of one build. A memory-hygiene arm over spec and review documents flagging a bare integer within a few words of a filename or a `§`/`grep`/`count` token would be noisy, so scope it: flag an authored integer in a spec's §6 or §9 that sits in the same sentence as a tracked path. That is narrow enough to be quiet and would have caught both instances.

## Left-shift summary

Ranked by how much of this round they would have prevented, not by how easy they are.

1. **A §2-to-§4 path-consistency check over a spec document** — every file path named in a scope item appears in Files touched, and vice versa. Purely mechanical. Catches H3 outright and the ambiguous half of H5, and is the direct antidote to the fold class that produced 18 of this round's 25 findings. Home: the memory-tree kit, beside the existing spec-header checks.
2. **A four-way declaration join for a new gate leg**, printing which of descriptor/exempt, subject-pin, map dossier and `chunk` is missing, as one message. Home: `tools/run-gates/run-gates.gov.test.sh`, which already closes over the manifest. Catches B1 and B3 and the leg branch of H5 — three of this round's five worst items and the third consecutive round with a blocker of this shape.
3. **A spec-template rule that no acceptance criterion is satisfied by silence**, with a grep-shaped arm over the phrases that spell it. Catches H1, and it is the class this corpus has now reported in four specs across three rounds.
4. **A spec-template rule that every §2 scope item is named by at least one §6 criterion**, or the spec says which human reader grades the remainder. Catches M1 and would have caught two of round 2's findings.
5. **A leg-name-to-argv check over spec prose**: a sentence naming both a leg and a command asserts they agree with `tools/gate-legs.json`. Catches H2 in both documents.
6. **`run-unattended-gates.sh` asserts every tracked `tools/unattended/*.test.sh` is named by exactly one `run_one` line.** Catches M4 and closes `TOOL-cSettledDocket-7`'s class rather than this instance.
7. **`check-kit-versions.sh --explain <kit>`**, printing the files and markers it compares. Catches H4 and removes the guessing that produced it.
8. **A narrow authored-integer flag** in a spec's §6 or §9 sharing a sentence with a tracked path. Catches L1.

Items 1 through 4 are the ones worth building. They are all spec-shape checks over documents this repo already generates and lints, none needs new machinery, and between them they cover 11 of the 13 items in this report.

## What this round did not check

Stated so a green row here is never misread as a verified one.

- **No spec was read against its implementation, because there is none.** This is a pre-code audit at rev-3; every claim about behaviour is a claim about a document.
- **The build README, RUN.md and the prompts folder were not audited.** Round 2 corrected a README roster cell; whether that correction holds against rev-3 was not re-checked, and neither was the roster's agreement with the five specs' current scope.
- **Cross-round disposition of round 2's twenty findings was verified only where a round-3 finding touches the same text.** Fifteen of round 2's items were taken as folded on the strength of the rev-3 logs rather than re-derived. The rev-3 logs were read; they were not audited as claims.
- **No gate was actually RUN.** Every verdict about a leg's behaviour here is derived by reading its source at the cited lines and its row in `tools/gate-legs.json`, not by staging a break and observing red. The manifest rows, the hold predicate at `run-gates.sh:947`, the `govkit.py` failure strings, the map extractor and coverage test, `check-kit-versions.sh` and `run-unattended-gates.sh` were all read directly; none was exercised.
- **The `chunk` half of B1 is asserted from `run-gates.gov.test.sh` source and from the observation that all 86 current manifest rows carry the key.** A row with no `chunk` was not staged, so the failure was not observed.
- **`tools/check-testsuite-counts.sh`'s contract, cited in H5, was read at a distance** — the finding stands on the `[[gate_leg]]` and subject-pin halves, which were verified line by line, and the assertion-count half is reported as a consequence a builder should confirm rather than as a measured one.
- **Two authored counts in spec 5 were found and deliberately not graded** — §5's "the seven files and the pin" and §10's "seven named carriers" — because both currently read true against the §4 table and neither joins to a machine. They are recorded in the Hunt 1 paragraph so the next fold sees them.
