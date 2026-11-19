**Serves:** diff-review TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4

# dTrackedAtlas — Tier-2 diff review of TOOL-dTrackedAtlas-1..4, round 1

*2026-11-19. Subjects: the build-state derivation `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py`, which the dClosedLoop schedule (`2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`) and the Closed Loop Atlas (`2026-10-16-build-PLAY-dClosedLoop-1-atlas.py` and its `.html` template) now both read; the Atlas's embedded generation stamp and its `--check --page` staleness check; and the build's specs, ledgers, red-fix records, prompts, asks and RUN.md. Units 1-3 are built and CLOSED. Unit 4 is DEFERRED against TOOL-dTrackedAtlas-7 and its code is not in this diff. Nothing under `tools/` changed. Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent came from 4 spec documents supplied as `specs`, beside the range's commit messages. By design: the caller's byDesign.*

**Range reviewed: `6547d032070ac45966116e412d91e84ceef963b1...5f2d3da6f8f440daee34140142b7bbdb56e19e3a`**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER. Three HIGH items stand, holding four confirmed findings. One MEDIUM item and two LOW items follow.

H1 (finding 1): a spec file name committed at the ref the derivation reads can run shell commands as the operator.

H2 (finding 2): on a run branch after the lander's prepare step, the derivation reads a held or unlanded build as landed and releases its children.

H3 (findings 3 and 5): `--check --page` certifies a page current at a landing merge while the page shows the wrong landed state.

M1 (finding 8): units 2 and 3 read CLOSED while two browser-pane acceptance checks are still owed.

No reviewer ran a gate. Every statement about behaviour comes from source or from the finders' and skeptics' read-only probes.

## Review shape

Intensity full, raw 9, confirmed 7, refuted 2, merged 0, unverified 0 (0 uncertain), precision 0.78.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 0 | 2 | 0 | 0 | 0 | 0.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 6 items (0 blocker, 3 high, 1 medium, 2 low).
Adjudicated tally by raw confirmed finding: 7 (0 blocker, 4 high, 1 medium, 2 low).
One synthesis merge accounts for the difference: findings 3 and 5 are one defect, the staleness digest that omits the merge history the landed predicate reads (H3).
Every finding keeps its binding grade. No grade was changed in synthesis.
Finding 5 was graded blocker by its finder and high by its skeptic. The skeptic's grade binds.
Refuted finding 6 is a twin of confirmed finding 8, noted at M1. The flag changes no verdict, grade, item or count.

## Run integrity

- Lenses: 5/5 returned, 0 died. Skeptic batches: 5/5 returned, 0 died.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 4 judged sound, 1 judged UNSOUND (finding 2), 2 judged INSTANCE-ONLY (findings 1 and 4), curing the cited instance and leaving its class standing, 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 1 re-graded by the skeptic (finding 5, blocker to high).
- Unverified findings: 0 answered uncertain by a skeptic, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Checklist: 29 items, each assigned to exactly one of 5 lenses: security 6, correctness 6, seams 6, verification 6, intent 5.
- Refuted findings shown to synthesis: 2. Same-address pairs shown: 0.
- Dispositions: unclassed refuse; 29 class slugs handed; 198 leg names read from `tools/gate-legs.json`.

## HIGH

### H1 — The fork scan sources tree-derived text as shell code (finding 1, high)

**Where:** `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@5f2d3da6:221`, and the sourcing line at `@5f2d3da6:225`.

**What is wrong:** `scan_forks` writes a bash script `grade.sh` line by line. Line 221 puts each spec's target path and the cutoff inside single quotes with no escaping: `printf '%s %s\n' {i} "$(plan_state '{target}' '{cutoff}')"`. The target ends in a spec basename taken from `git ls-tree` at `--ref`. The cutoff is `FORK_ITEM_CUTOFF` from `.memory-tree.conf` at that commit. Line 225 then sources the script through `breakpoints.run_sourced` (`bash -c`), and puts the temp-directory path inside single quotes the same way. Any spec whose status is not CLOSED or WONTDO reaches `scan_forks` under `detail=True`.

**Consequence:** A commit at the derived ref can hold a spec named, for example, `2026-11-19-spec-a'$(cmd)'.md`. `git ls-tree` passes `'`, `$`, `(` and `;` unquoted. Every build-state run, and every Atlas `--check` or `--out` with detail on, then runs `cmd` as the operator. `--ref` can name any branch, including one fetched from another machine, so the reader that is meant to be read-only executes code the tree chose. The finder's probe printed `INJECTED` before `0 OPEN`. A temp path containing `'`, such as a Windows profile named O'Brien, breaks the run. The path is narrow, because someone has to commit the hostile name, which makes this high rather than blocker.

**Fix (judged INSTANCE-ONLY by the skeptic; the class-level fix follows):** Put no data in shell text anywhere. Pass the script path, every target and the cutoff through env or positional arguments, or quote each with `shlex.quote`. That includes line 225's `. '<script>'`. Also refuse spec basenames that do not match `[A-Za-z0-9._-]+\.md` at the read boundary. The finder's proposal cures the cited instance alone: write the targets and cutoff to a data file read by `while IFS= read -r -d '' t; do plan_state "$t" "$CUTOFF"; done`, or `shlex.quote` each value, and refuse off-pattern basenames.

**Left-shift:** new class `tree-text-interpolated-into-shell-source`. Gate: a fixture ref that plants a spec named with `'$(touch <scratch>/pwned)'`, then a derive run, then an assertion that the marker file does not exist. A second arm runs with a temp directory containing `'`.

### H2 — A run branch's prepared landing merge reads as a landing (finding 2, high)

**Where:** `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@5f2d3da6:240` (`derive_landings`, lines 235-245).

**What is wrong:** `derive_landings` counts any first-parent merge of the ref that touches the build's RUN.md, and whose base matches, as a landing. The lander's prepared "land onto origin/main" merge has exactly that shape and sits on the run branch's own first-parent line before main takes it. Spec 1 says a build-kind RUN.md on a run branch that never merged has no landing and reads not-landed. The by-design list does not cover this.

**Consequence:** At `--ref 5125f93ea`, the dDeclaredLoop run-branch tip whose RUN.md reads phase HELD, the derivation reports dDeclaredLoop `landed-carrying`, landing `67f1ffb18`, next state `done`. `67f1ffb18` never reached origin/main's first-parent line; main's real landing is `c1f80c002`. dFairHearing reads the same way at `b55a6494a` (phase VERIFYING) through the prepared merge `7b42f2c47`. The schedule and the Atlas both default to `--ref HEAD`. So at any run-branch HEAD after the prepare step, the build is marked done and its children's waits are released before main has landed it.

**Fix (the finder's proposal was judged UNSOUND by the skeptic; the skeptic's corrected fix follows):** Measure landings against an explicit default-branch ref, given as an input that is recorded in the output and folded into the page's input digest. Count a merge only if it lies on the first-parent line of `git merge-base <ref> <default-ref>`. Fixtures and clones pass their own default ref. Probe: derive at `5125f93ea` reads dDeclaredLoop not-landed, and at `9e21ac760` it still reads six landed.

**Left-shift:** new class `prepared-landing-merge-read-as-landed`. Gate: a fixture arm that builds a run branch carrying a prepared `--no-ff` landing merge main never took, derives at its tip, and asserts not-landed. The same arm then lands it on the fixture's default branch and asserts landed.

### H3 — `--check --page` certifies a page current while its landed state is wrong (findings 3 and 5, high)

**Where:** `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@5f2d3da6:907` (`check_page`, lines 879-925), its digest at `@5f2d3da6:821` (`derive_input_digest`, lines 821-824), and the history read at `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@5f2d3da6:235`.

**What is wrong:** `check_page` reports `atlas: current` and exits 0 whenever the stamp's digest equals a sha256 of `git ls-tree -r -z <ref> -- <inputs>`. That digest covers tree content only. The landed state the page shows comes from `derive_landings`, which reads `git log --first-parent --merges <commit> -- <build>/RUN.md`, commit-graph history that no tree listing covers. A `--no-ff` landing merge typically leaves every stamped input byte-identical to the run-branch tip while it changes the derived landed state and landing sha. Neither the module docstring (lines 19-25) nor spec 3's "What it does not check" list names merge history. Spec 3's statement that the page reads stale "only when an input moved, never because the commit did" is what hides the case.

**Consequence:** The digest of the stamped inputs is identical at a landing merge and its run-branch parent at 6 of 12 landings (`2511c1181d36`, `9760fb746c0f`, `0a760477e172`, `c1f80c00275e`, `9e21ac760dc0`, `1c5ef7c0a33c`). On each of them, a page generated on the run branch before landing passes `--check --page --ref <merge>` with exit 0, while its Chain view, landed count, "Landed since" column and next-run states are wrong. At `9760fb746c0f^2` the derivation reads dOrderedCharter not-landed, and at the merge it reads landed. At `5125f93ea` dDeclaredLoop's landing is `67f1ffb18`, and at `c1f80c002` it is `c1f80c002`. A caller that regenerates only on exit 1, which the deferred unit 4 hook is meant to be, never regenerates. Once H2's fix lands, the same gap keeps a just-landed build showing "not landed". Spec 3's AC6 cannot show the gap: its planted branch appends to RUN.md, which moves the digest on its own. Graded high, not blocker, by both skeptics: it needs a page generated on a run branch before landing and checked after it.

**Fix (judged SOUND by both skeptics):** Make the digest cover what the landed predicate reads, in both `build_stamp` and `check_page`. One option: hash, beside the ls-tree bytes, `git log --first-parent --merges --format=%H <commit> -- <each build>/RUN.md` for each chain build. The other: store the state document's per-build landing shas in the stamp and re-derive only the landings at `--ref`. With H2's fix, fold the default-branch ref into the same digest. Until fixed, add "the first-parent merge history the landed predicate reads" to the docstring's and spec 3's "does not check" sections.

**Left-shift:** new class `freshness-digest-omits-what-the-derivation-reads`. Gate: an AC that plants the merge-only case. Generate p0 at a branch tip whose RUN.md already carries the run's base, then `git merge --no-ff` that branch into a parent that touched no input, and expect `--check --page` at the merge to exit 1. The live probe: a page generated at `5125f93ea` and checked at `c1f80c002` exits 1. Both read red today.

## MEDIUM

### M1 — Units 2 and 3 read CLOSED with their browser-pane acceptance checks still owed (finding 8, medium)

**Where:** `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md@5f2d3da6:69` and `@5f2d3da6:78`; `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-3-ledger.md@5f2d3da6:75`; the status lines at `memory/builds/dTrackedAtlas/spec/2026-11-19-spec-TOOL-dTrackedAtlas-2.md@5f2d3da6:3` and spec 3's header.

**What is wrong:** The unit 2 ledger records spec 2's AC12 as "not observed in the browser pane ... owed to the close". It says the Build area's "Since the baseline" panel, which AC12 requires to name dTrueNorth and `2511c1181`, "was not observed". Ledger 3 owes AC8's pane look ("generated from <HEAD12>") and its red to the close. No later record, RUN.md entry or commit message in the range observes either check. The commits only flip the statuses, and specs 2 and 3 both read `**Status:** CLOSED`.

**Consequence:** The CLOSED status certifies AC12 and AC8 as passed when neither was observed, and AC12's red was not observed either. This goes against the brief's acceptance rule that each red case is observed red before green and recorded in the unit's ledger. The effect is contained: the headless dump-dom (ledger 2) and the grep with its red (ledger 3) observed most of each criterion. The gap is the click-gated Build panel and the pane render.

**Fix (judged SOUND by the skeptic):** Before the close, serve the page with `python -m http.server` from a temporary `.claude/launch.json` and open it in the browser pane. Observe AC12: 22 rows (PINNED) in the Chain view, six landed with AC1's merges, dPlacedRequest and dWitnessedBar reading "can start", and the Build area's "Since the baseline" panel naming dTrueNorth and `2511c1181`. Observe AC8's "generated from <HEAD12>". Observe each red on the `9e21ac760` page. Record both in the ledgers. Otherwise hold units 2 and 3 short of CLOSED until that is done.

**Twin:** refuted finding 6 (verification lens, ledger 2:78) describes the same owed pane observations under CLOSED specs. Its claimed consequence, a silent drop, was refuted because "Owed to the close" lines are tracked and the close is still running. The flag changes nothing here.

**Left-shift:** new class `closed-while-acceptance-owed-to-the-close`. Gate: a memory-hygiene check that reds a spec whose status is CLOSED while its unit's ledger still carries an "Owed to the close" line that no later record discharges.

## LOW

### L1 — A valued option with no value raises IndexError outside `--page` mode (finding 4, low)

**Where:** `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@5f2d3da6:939` and line 940.

**What is wrong:** `main()` reads `argv[argv.index("--ref") + 1]` and the same for `--claims` with no bounds check. The `--page` branch (lines 930-937) bound-checks `--ref`, so the two copies of the argument rule disagree. This diff introduced both reads.

**Consequence:** `atlas.py --check --ref` prints `IndexError: list index out of range` instead of an `atlas:` refusal line. The run still stops non-zero, so only the message is wrong.

**Fix (judged INSTANCE-ONLY by the skeptic; the class-level fix follows):** Add one helper that reads the value of every valued option in `main`: `--ref`, `--claims`, `--plant` and `--out`. When the option is the last argument or its value starts with `-`, it exits with `atlas: <opt> takes a value`. Use it in both the `--page` branch and the derive branch. The finder's proposal cures the cited instance alone: copy the `index + 1 < len(argv)` check to `--ref`, `--claims` and `--plant` in the derive path.

**Left-shift:** class `two-answers-to-one-question`. Gate: a self-test arm that runs each valued option as the last argument and asserts one `atlas:` refusal line and no traceback.

### L2 — Ledger 1 still owes a lexicon pin raise the rev-3 rename made unnecessary (finding 9, low)

**Where:** `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-ledger.md@5f2d3da6:55` (lines 55-56).

**What is wrong:** The ledger's "Owed to the close" line asks for the lexicon's `VERB_OFFENDER_PIN` to gain `predecessors`, "the one verbless name the spec's interface fixes". Spec 1 rev-3 and commit `8d69e97b7` renamed the function to `derive_predecessors` in the spec (lines 107, 115, 238, revision log line 379) and in the code (`build-state.py` line 135). No record clears or supersedes the owed item.

**Consequence:** The closer is told to loosen the verb-offender pin by one for a name that no longer exists. Nothing executes the line, so behaviour is unchanged.

**Fix (judged SOUND by the skeptic):** Drop the `VERB_OFFENDER_PIN` item from the "Owed to the close" line, or say that the rev-3 rename to `derive_predecessors` cleared it.

**Left-shift:** class `amendment-leaves-its-other-half-standing`. Gate: a spec-tokens style check that reds a code-span name in a build's ledger "Owed" line when the name no longer resolves in the build's code or specs.

review-shape kind=diff-review round=1 intensity=full at=synth raw=9 confirmed=7 refuted=2 merged=0 unverified=0 blocker=0 high=4 medium=1 low=2 agents=11 out-tokens=105639 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=4 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@c860b053:221 | high | high | confirmed | build-state.py is new in this diff: it is absent at 6547d032 and was added by 390c2bc05. Line 221 is `lines.append(f"printf '%s %s\\n' {i} \"$(plan_state '{target.as_posix()}' '{cutoff}')\"")`. Both values go inside single quotes with no escaping. `target` ends in the spec basename taken from `git ls-tree` at the ref (lines 278-283), and `cutoff` is FORK_ITEM_CUTOFF from .memory-tree.conf at that commit (read_conf). Line 225 then sources the script with run_sourced. A spec reaches scan_forks whenever its status is not CLOSED or WONTDO (line 344, called at line 362 under detail=True). So a branch named by --ref, which can be fetched from another machine without being checked out, decides which shell code runs inside a reader that is supposed to be read-only. Line 225 also puts the temp-directory path inside single quotes without escaping, so a profile path that contains `'` breaks the run. The path is narrow because someone has to commit a hostile file name, which makes this high rather than blocker. | instance | - | new:tree-text-interpolated-into-shell-source |
| 2 | correctness | memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@c860b053:240 | high | high | confirmed | I ran the instrument with `--ref 5125f93ea` myself. It reports dDeclaredLoop build_run `landed-carrying`, landing 67f1ffb18 ('merge: dDeclaredLoop — land onto origin/main at 4e6ac5f7'), next.state `done`. 67f1ffb18 is 7th on 5125f93ea's first-parent line, and `git log --first-parent origin/main \| grep -c 67f1ffb` prints 0. RUN.md at 5125f93ea reads phase HELD, base 2ba17e9d6. At the same ref dFairHearing also reads landed and `done`. derive_landings (lines 236-246) takes any first-parent merge touching RUN.md whose base matches. A run branch's prepared landing merge has that shape, so on a held or unlanded run branch, the default --ref HEAD for both the schedule and the Atlas, the build reads landed and its children are released. That contradicts spec 1's 'A build-kind RUN.md on a run branch that never merged has none, so it reads not-landed'. It is not covered by the by-design list. | unsound | - | new:prepared-landing-merge-read-as-landed |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@924f579c:907 | high | high | confirmed | At 5f2d3da6f, check_page (atlas.py ~907) returns 0 'current' whenever derive_input_digest equals the stamp's digest. That digest is a sha256 of `git ls-tree -r -z <commit> -- <inputs>` (line 821-824), so it covers tree content only. The build-state module's derive_landings (memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@c860b053:235-240) reads `git log --first-parent --merges` on the commit, which is commit-graph state. I reproduced the gap. Over the dClosedLoop README/build/reviews, .memory-tree.conf and dDeclaredLoop/ inputs, the digest is identical (65df6d4a…) at c1f80c002 and at its branch parent 5125f93ea. The merge's 29 changed files are all outside the inputs. Yet `git log --first-parent --merges -- memory/builds/dDeclaredLoop/RUN.md` gives c1f80c002 as the latest landing at c1f80c002, and 67f1ffb18 at 5125f93ea. So a page generated on the run branch before landing is certified current at the landing merge while it shows the wrong landing. The docstring (lines 19-25) and spec 3's 'What it does not check' list name run claims, tools/ code and hand edits, but not merge history. Spec 3 says the page reads stale 'only when an input moved, never because the commit did', and that statement is exactly what hides this case. I graded it high rather than blocker because it needs a page generated before landing and checked after it, and the deferred after-landing hook (unit 4) is meant to cover that path. | sound | - | new:freshness-digest-omits-what-the-derivation-reads |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@924f579c:939 | low | low | confirmed | main() at line 939 runs `argv[argv.index("--ref") + 1]` and line 940 does the same for --claims, with no bounds check. So `--check --ref` with no value raises IndexError instead of an 'atlas:' refusal. The --page branch (lines 930-937) does bound-check --ref. The base's main (6547d032 line 700) had no --ref or --claims handling, so this diff introduced them. The run still stops non-zero, so the only effect is the message: low. | instance | - | class:two-answers-to-one-question |
| 5 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@924f579c:907 | blocker | high | confirmed | I checked the code. check_page (memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@924f579c:879-925) compares only derive_input_digest, which is sha256 of `git ls-tree -r -z <ref> -- <inputs>` (memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@924f579c:821-824). derive_landings (memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py@c860b053:235-245) works out landed state from `git log --first-parent --merges <commit> -- <build>/RUN.md`, and that is history, which no tree listing covers. I re-ran the precondition. `git diff --name-only <c>^2 <c> -- memory/builds/ .memory-tree.conf` printed nothing for 9760fb746c0f, 2511c1181d36 and 9e21ac760dc0. So every input the stamp lists is byte-identical at the landing merge and at the run-branch tip, the digests match, and a page stamped at the tip reports 'current' at the merge while its landed state is wrong. The docstring's 'does not see' list (memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@924f579c:24-25) names only claims, tools/ code and hand edits. This code is new in the diff: the base atlas.py has no check_page. I grade it high, not blocker: on this path the check certifies a wrong page, but only for a page generated on a run branch before its landing, and the intended regeneration happens after landing on main. | sound | - | new:freshness-digest-omits-what-the-derivation-reads |
| 6 | verification | memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md:78 | medium | - | refuted | The facts are true but the claimed consequence, a silent drop, is not shown. Ledger 2 says plainly that the Build-area panel 'was not observed' and ends with 'Owed to the close: ... AC12 in the browser pane'. Ledger 3 does the same for AC8. Ledger lines starting 'Owed to the close' are this repo's convention for tracking deferred observations, and the main loop later discharges them. The aClearedLedger ledgers are the precedent: TOOL-aClearedLedger-3-1 records 'Owed to the close, and since observed by the main loop'. RUN.md shows phase: REVIEWING, so the close (M8) is still running, and this review is part of it. Nothing yet shows the close dropping these items. The finder graded it medium and I could not establish the consequence, so it is refuted. | sound | orchestrator-hand-off-owed-a-disposition | - |
| 7 | verification | memory/builds/dTrackedAtlas/BACKLOG.md:6 | medium | - | refuted | The BACKLOG.md:5 row for TOOL-dTrackedAtlas-6 has the shape memory/guides/UNATTENDED-ASKS.md §5 requires of a filed ask: a `seen` and an `accept` clause, plus its SEV row (HIGH, BACKLOG.md:11). I found no rule in UNATTENDED-ASKS.md, UNATTENDED-PROTOCOL.md, HYGIENE.md or TEMPLATE-SPEC.md that makes an ask or a fork resolution list an owner-decline outcome. The only decline route the grammar defines is in HYGIENE.md:715, and it covers deviation-record approvals, not asks. The ask stays open until the owner acts, so the red is tracked rather than left with 'no exit'. Any decline would be the owner's own ruling, filed through the ordinary route. The state the finding describes (CP3/CP4/CP5 red under GATE_SELFTESTS=1, and the pin arm stopping packet checks) is the re-pin consequence that spec 1 §6/§7 F2 records and that the harness lists as by design. What remains is a wish for extra contingency prose, not a defect this diff introduced. | unsound | owner-item-without-its-reject-outcome | - |
| 8 | intent | memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md:69 | medium | medium | confirmed | Ledger 2:69 says AC12 was 'not observed in the browser pane ... owed to the close' and that 'The Build area's panel, which needs a click, was not observed'. Ledger 2:78 lists AC12 in the pane, with its red at 9e21ac760, as owed to the close. Ledger 3:75 owes AC8's pane look and its red. Spec 2 AC12 (line 308) requires the pane to show the Build area's panel naming dTrueNorth and 2511c1181, and spec 3 AC8 (line 288) requires the served page to show 'generated from <HEAD12>'. I grepped the build folder, RUN.md and every commit message in 6547d032..5f2d3da6f: no later record observes either check. The commits only flip the statuses ('unit 2 closes', 'unit 3 closes'), yet specs 2 and 3 both read Status: CLOSED. This conflicts with brief lines 83 and 114 ('Each red case observed red before green, recorded ... in the unit's acceptance ledger'). Graded medium: the headless dump-dom (ledger 2) and the grep plus its red (ledger 3) observed most of each criterion. The gap is the click-gated Build panel and the pane render, so the false certification is real but its effect is contained. | sound | - | new:closed-while-acceptance-owed-to-the-close |
| 9 | intent | memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-ledger.md:55 | low | low | confirmed | The ledger file is new in this diff: it does not exist at 6547d032. Lines 55-56 still say the close owes a change where the lexicon's `VERB_OFFENDER_PIN` gains `predecessors`. Commit 8d69e97b7 later renamed that function. Spec 1 now names `derive_predecessors` at lines 107, 115 and 238, its revision log records the rename at line 379, and build-state.py defines `derive_predecessors` at line 135. A grep of the dTrackedAtlas folder finds no other place where the pin item is cleared or superseded. So the owed item is stale and points the closer at an unneeded loosening of the verb-offender pin. Nothing executes it, though: it is a wording defect in a record and changes no behaviour, so it is low. | sound | - | class:amendment-leaves-its-other-half-standing |
