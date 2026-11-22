**Serves:** diff-review TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97

# dWitnessedBar — Tier-2 CLOSING DIFF review, round 1

*Node `d`, 2026-11-21. dWitnessedBar is the Test build of the dClosedLoop chain, run unattended. This review is an adversarial pass over the whole landed diff of the 87 units built from their specs. TOOL-dWitnessedBar-28 is carried forward DEFERRED against asks TOOL-dWitnessedBar-101 to -103. Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent came from 1 spec document supplied as `specs`, read beside the range's commit messages. The checklist had 151 items, acquired by the harness from `--for-diff 9e21ac760dc0a43d6ed007396922722ccee98d57..HEAD`, each assigned to exactly one lens: security 31, correctness 30, seams 30, verification 30, intent 30. By design: the caller's byDesign, plus 3 invariants from the checklist's by-design block. Product code and gates were reviewed first; records only where a gate reads them.* (DERIVED from the builder's probe)

**Range reviewed: `9e21ac760dc0a43d6ed007396922722ccee98d57...0c8711aba1537d86e0de2ca470453927b79cd104`**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER.
Two are HIGH, and both are wrong results on narrow paths.
H1: a pushed tip that removes or edits the policy kit turns R's `hooks.bypass = refused` into `allowed`.
H2: `verify-peer` signs and publishes a stale per-tree slot that the current bar run did not write.
Each HIGH needs a fail-closed read plus one arm seen red first.
I recommend folding both HIGHs before the landing.
I also recommend folding the two MEDIUMs, since each is a small edit plus one fixture arm.
The two LOWs can be folded or filed.
Per M8, a fold earns a round 2 over the fold itself.

## Review shape

Intensity full, raw 7, confirmed 6, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.86.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 1 | 0 | 1 | 0 | 0 | 0 | 0.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 6 items (0 blocker, 2 high, 2 medium, 2 low).
Adjudicated tally by raw confirmed finding: 6 (0 blocker, 2 high, 2 medium, 2 low).
No merge was made, so the two tallies agree.
Every confirmed finding binds at its bracketed grade.
The one refuted finding (6, the `run-gates gov canary` budget row) is a different defect from every confirmed one, so no twin is flagged.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 0 duplicate refutations counted as merged confirmations.
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 4 judged sound (findings 3, 4, 5, 7), 0 judged UNSOUND, 2 judged INSTANCE-ONLY (findings 1 and 2), 0 none proposed, 0 NOT JUDGED.
- An INSTANCE-ONLY fix cures the cited instance and leaves its class standing, so each item below carries the skeptic's class-level fix.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 1. Same-address pairs shown: 0.
- Dispositions: unclassed is `refuse`; 151 class slugs handed; 219 leg names read from tools/gate-legs.json.

Every count above is zero where it would mark the run incomplete, so this run is complete.

## HIGH

### H1. `hooks.bypass = refused` at R fails open when the policy reader cannot answer (finding 1)

**Where:** `.githooks/pre-push@13e24816:1575`, in `read_policy_at` (lines 1546-1593).

**What is wrong:** `read_policy_at` sets `PP_BYPASS=allowed` before anything is read.
`hooks.bypass` is assigned only inside the loop, after `resolve_kit_dir` succeeds.
When no policy kit resolves, `dir` stays empty and the function returns at line 1587 with `PP_BYPASS=allowed` and `PP_BYPASS_WHY` empty, so not even the default line prints.
The same happens when no python resolves.
A reader that exits non-zero goes through `|| PP_BYPASS=""` at 1575 into the `*)` arm at 1579-1580, which also yields `allowed`.
The same function reads `verdict.blocks` the other way: a reader error there becomes `every-red`, the strictest value.

**Reachable path:** the policy kit is missing when the pushed tree removes or relocates `tools/policy/`.
Under the relative `.githooks` hooksPath, the fallback tree `${0%/*}/..` is that same pushed tree.
The reader and its `catalogue.toml` (`load_catalogue(KIT)` in tools/policy/policy.py) come from the pushed tree, not from R.
`check_reviewed_file` requires the reader to be tracked only at the pushed tip, not at R.
So a branch whose catalogue drops `refused` from the allowed values also turns R's `refused` into `allowed`.

**Consequence:** the refusal block at lines 2085-2103 is skipped, and unwitnessed pass commits land.
The comment at 2045 ("under `refused` refuses: deny by default") is false for this key.
The header at 1507 ("a branch that loosens its own policy file enables nothing") is false for this key.
The suite's bypass arms (.githooks/pre-push.test.sh 2965-3033) always ship a working policy kit, so no arm reaches the missing-kit or reader-failure branch.
The defect is new in this range: the base hook has no PP_BYPASS.
It is HIGH rather than BLOCKER because it needs a push that removes or tampers with the policy kit, which is a narrow path.

**Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** make every R-scoped policy read in `read_policy_at` fail closed against R's own committed bytes.
Read `.governance/policy.toml` at R with `git show R:...`.
When the kit is missing, python is missing, or the reader fails or answers outside the catalogue, take the strictest value R declares.
Refuse outright when R's raw file declares a non-default value the reader could not confirm.
Apply this to `hooks.bypass`, to `verdict.blocks` (whose no-kit branch currently reads own-only) and to `verdict.held`.
Add arms that delete the kit at the tip and assert the R value still holds.

The finder's proposal cures the cited instance alone: parse `hooks.bypass` from R's raw bytes, the way the hook already parses `INHERITED_RED_MAX_AGE`, and read any reader failure as `refused` when R's file holds `bypass = "refused"` under `[hooks]`.

**Left-shift gate:** add the missing-kit arm to the `pre-push self-test` leg: `build_bp_fixture` with `refused` at R, a tip that `git rm`s tools/policy/policy.py, and an assertion of `bypass-refused`. Run it against the current hook first and watch it go red. Add a `harness arms (fail branches armed or pinned)` requirement that every `read_policy_at` early return has an arm.

### H2. `verify-peer` signs and publishes a per-tree slot the current bar run did not write (finding 2)

**Where:** `tools/run-gates/verdict_backends.py@d75ea52b:656`, in `run_verify_peer` (lines 653-660).

**What is wrong:** after `subprocess.run`, `run_verify_peer` checks only that `common/gate-verdict/<tree>` is a file.
It then passes `read_tag_lines(slot.read_text(...))` straight to `write_peer_tag`.
It never checks that this run wrote the slot, by run_id or by mtime.
It ignores `p.returncode`.
It never checks `rec['tree']`.
It never applies `check_local_record` (the reuse pair and the selection), which `read_local_verdict` (lines 328-350) applies to the same slot.
This is a carried-forward row read as the current answer.

**Reachable path:** run-gates.sh writes no slot when the tree moved during the run, when the fingerprint cannot be read, or when the write fails (the `no per-tree verdict written` branches, tools/run-gates/run-gates.sh@04da8977:6251-6290).
In each case a GREEN slot left by an earlier full run on this clone for the same tree survives.
That slot may be one `check_local_record` would refuse, for example one carrying a non-zero `reused_cache` or a selection that held legs.

**Consequence:** verify-peer prints `published ... as node <n>` and pushes a signed GREEN tag.
`write_peer_tag` signs only the verdict, tree, run_id and node lines, and `read_peer_verdict` checks none of the reuse or selection keys.
So the peer reader cannot tell this tag from a witnessed one, and a peer-node GREEN certifies a bar run that did not produce it.
The defect is new in this range: `run_verify_peer` is absent from the base.
It is HIGH because the path needs a prior slot for the same tree on the verifying clone.

**Fix (judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):** snapshot the slot's run_id, or its absence, before the bar runs.
After the run, refuse to publish unless the run_id changed and `p.returncode` agrees with the verdict.
Then read the slot through `read_local_verdict(...)` itself, not `check_local_record` alone, so the tree-line match, the GREEN/RED line validity, `newline=""` and both record predicates all apply.
Publish only a GREEN that `read_local_verdict` returns as witnessed, or a fresh RED.

The finder's proposal cures the cited instance alone: require a changed run_id and an agreeing return code, run `check_local_record(rec, common, repo)` on a GREEN before `write_peer_tag`, and read the slot with `newline=""`.

**Left-shift gate:** add a verify-peer arm to the `run-gates gov canary` leg: plant a GREEN slot for the candidate's tree with `reused_cache 1`, stub the bar to exit 1 without writing, and assert verify-peer prints `not published`. See it red against today's code first.

## MEDIUM

### M1. `precommit.py` drops deletions from the guard trigger the runner counts (finding 3)

**Where:** `tools/run-gates/precommit.py@7bbc6ee6:185`, in `read_staged`.

**What is wrong:** `read_staged` lists staged paths with `git diff --cached --name-only --diff-filter=ACMR -z`, which drops deletions.
The runner trips a guard with `! git diff --quiet "$BASE" -- <guard>` (tools/run-gates/run-gates.sh@04da8977:599), which counts deleted paths.
The module docstring (lines 13-15) and `check_guard_trips` both claim the runner's semantics, so the two copies of one trigger rule disagree.
The hand-named hook this replaced (base .githooks/pre-commit:195) read `git diff --cached --name-status --no-renames` with no status filter, so a deletion tripped its triggers.

**Consequence:** today none.
All four `precommit` rows in tools/gate-legs.json have no guard, so each runs at every commit.
The first row that declares a guard will skip a commit that only deletes files under that guard, while the bar reds on the same change at push time.
That is the hand-named-list-green-while-the-bar-reds class the module was written to retire.

**Fix (judged SOUND by the skeptic):** use `--diff-filter=ACDMR`, or drop the filter, so a deletion trips a guard as it does in the runner.
Add a precommit.py fixture arm with a guarded row and a delete-only staged commit that asserts the row runs, and see that arm red against the current ACMR filter.

**Left-shift gate:** the fixture arm above, homed in the `leg-factory selftest` leg, keyed to the runner's `changed()` rule so any later divergence of the two copies reds.

### M2. The scaffolder still writes four ledger populations in their retired grammar (finding 4)

**Where:** `tools/memory-tree/adopt-memory-tree.sh@277edcb9:747` (the writes at 743-752 and 849-853).

**What is wrong:** this diff turns legacy-files, curation-debt, unarmed-branches and stale-header-waiver into ledger populations.
Each has a `[[ledger]]` row in tools/memory-tree/kit.toml (lines 739-828) and a `*-to-ledger` upgrade step (lines 905-957).
Gov's own homes now open with `# ledger · <population> · key ...`.
The scaffolder's readme-contract (line 800) and method-carriers (line 817) writes moved to the ledger header.
But `--scaffold` still writes the four homes with prose comments only and no `# ledger ·` header.
The unarmed-branches comment at line 748 still documents the retired grammar `gate<TAB>check<TAB>ordinal<TAB>signature`.

**Consequence:** `registry_to_ledger.py witness` over each header-less scaffolded home prints `... is in its legacy grammar: not applied` and exits 1, so a freshly scaffolded adopter reads as owing four conversions it never needed.
A row added as the scaffolded comment says, read through `legacy_ledger.read_rows(path, 3, verbatim=(1,2))` as check-arms.py `parse_pin` reads it, comes back malformed, so check-arms raises Problem and the arms leg reds.
Both failures are loud rather than a silent wrong verdict, so the effect is contained.

**Fix (judged SOUND by the skeptic):** scaffold all four homes the way readme-contract and method-carriers now are: a `render_header`-equal first line, `# ledger · <population> · key site <fields> · direction <dir> · drain hunk`, taken from the kit.toml registration rather than typed.
Rewrite the unarmed-branches comment to the ledger grammar `path<TAB>check<TAB>signature<TAB>count<TAB>sha<TAB>disposition`.
Add a memory-hygiene self-test arm that scaffolds a tree and runs every `[[upgrade]]` `*-to-ledger` witness over it, owing exit 0 for each, and see it red against today's scaffold first.

**Left-shift gate:** the scaffold-then-witness arm above, in the `memory-hygiene self-test` leg; it covers every future `[[ledger]]` registration by enumeration, not by name.

## LOW

### L1. `run_quiet_leg` takes a `here` it never reads (finding 5)

**Where:** `tools/run-gates/verdict_flow.py@712fc604:551`.

**What is wrong:** `run_quiet_leg(run, row, n, top, here=HERE)` never reads `here`.
Its body takes the runner from `profile_bar.RUNNER` (:586).
Its only caller, `cmd_quiet_rerun` (:635), calls `(rerun or run_quiet_leg)(run, r, n, top)` and passes no `here`.
`cmd_quiet_rerun` does use its own `here`, for `read_wait_ceiling` (:624).

**Consequence:** no wrong verdict today.
A caller that sets `here` to point the quiet re-run at another kit dir would get its wait ceiling from that dir but its alone-run from the sibling profile_bar's kit.
The parameter implies a seam that does not exist, and a future fixture that relies on it would grade the wrong runner.

**Fix (judged SOUND by the skeptic):** drop the `here` parameter from `run_quiet_leg`, or thread it through: take the runner as `here / 'run-gates.sh'` in place of `profile_bar.RUNNER`, and pass `here` from `cmd_quiet_rerun` at :635.

**Left-shift gate:** extend the `python reads (a name never bound, an import outside its guard)` leg with the AST scan the finder ran: a parameter its function body never loads reds, unless pinned.

### L2. Agent-commit trailers drift from the charter's Level-0 rule (finding 7)

**Where:** `AGENTS.md@71a6071e:278`.

**What is wrong:** the charter fact says every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
Over the range's 544 commits, 257 carry `Claude Opus 5` and 287 carry `Claude Opus 5.5`, the 5.5 form appearing from 5a7485743 onward.
The range's last commit, 0c8711aba, goes back to `Opus 5`.
Many commits (a2675ab88, 27a6568ef and 73fc3773b among them) also do not end with the trailer, because a `Commit-Checked: unattended@1.129` line follows it.
The value drift is older than this range: of the 300 commits before the base, 208 already carry `Opus 5.5`. (DERIVED from the builder's probe)
The position drift is new: the kit now writes `Commit-Checked` as a trailer (FLOOR_KEYS, `unchecked`) after Co-Authored-By, so "ends with" is untrue for every checked pass commit.

**Consequence:** commit metadata and charter wording only; no behaviour changes.
An audit that greps for the charter's trailer to find agent commits misses about half of this build's commits.
Nothing gates the trailer value or position (no `Co-Authored-By` hit in tools/unattended/, tools/lib/commit_trailers.py or .githooks), so the drift will recur.

**Fix (judged SOUND by the skeptic):** choose one form.
Either keep the charter's `Claude Opus 5` trailer, since AGENTS.md (Level 0) outranks a harness attribution reminder, or change AGENTS.md:278 through an owner-recorded change.
Decide whether a `Commit-Checked:` line may follow the trailer, and reword "ends with" to match.
Then add the trailer value and its position to the unattended kit's commit check (`commit_trailers.py` / `--check-commit`), so a mismatch reds.
Probe: `git log --format=%B 9e21ac760dc0..0c8711aba | grep -o 'Co-Authored-By: Claude Opus [0-9.]*' | sort | uniq -c` prints 257 `Opus 5` and 287 `Opus 5.5`.

**Left-shift gate:** the trailer-value-and-position check above, armed in the `unattended kit gate` leg, reading the expected value from AGENTS.md rather than a typed copy.

## Refuted, not counted

Finding 6 (verification, `tools/run-gates/selftest-budgets.txt:127`, the `run-gates gov canary` budget row) was refuted and is neither reinstated nor counted.
It is not a twin of any confirmed finding.

review-shape kind=diff-review round=1 intensity=full at=synth raw=7 confirmed=6 refuted=1 merged=0 unverified=0 blocker=0 high=2 medium=2 low=2 agents=10 out-tokens=98532 trigger=owed shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=2 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | .githooks/pre-push@13e24816:1575:1575 | high | high | confirmed | Checked at 0c8711aba in .githooks/pre-push, lines 1545-1593. `read_policy_at` starts PP_BYPASS at `allowed` and PP_BYPASS_WHY empty. hooks.bypass is assigned only inside the loop, after `resolve_kit_dir` succeeds. When no kit resolves under $top or `${0%/*}/..` (the same tree under the relative hooksPath), `dir` stays empty and the function returns at the `-z "$dir"` branch with PP_BYPASS=allowed. The same happens when no python resolves. A reader that fails or gives a stray answer goes through `\|\| PP_BYPASS=""` into the `*)` arm, which also yields `allowed`. The reader comes from the pushed tree: `check_reviewed_file` only requires it to be tracked at main_local, the pushed tip, not at R. So a tip that removes tools/policy/policy.py, or edits its catalogue, turns R's `refused` into `allowed`. The refusal block at about 2085 is then skipped. That contradicts the comment 'under `refused` refuses: deny by default' and the header at 1507 ('a branch that loosens its own policy file enables nothing'). Not pre-existing: the base hook has no PP_BYPASS. Graded high rather than blocker because it needs a push that removes or tampers with the policy kit, which is a narrow path. | instance | - | class:fallback-fabricates-the-passing-value |
| 2 | correctness | tools/run-gates/verdict_backends.py@d75ea52b:656 | high | high | confirmed | run_verify_peer was added in this range (it is absent from the base verdict_backends.py). At 0c8711aba lines 653-660, after `subprocess.run` it reads only whether `common/gate-verdict/<tree>` is a file. It then passes `read_tag_lines(slot.read_text(...))` straight to write_peer_tag. It never checks p.returncode, never checks that this run wrote the slot, never checks `rec['tree']`, and never calls check_local_record, which read_local_verdict (lines 328-350) applies to the same slot. run-gates.sh writes no slot when the tree moved, the fingerprint is unreadable, or the write fails (the `no per-tree verdict written` branches), so an earlier slot for that tree on this clone survives. write_peer_tag signs only the verdict, tree, run_id and node lines, so the peer reader cannot tell this tag from a witnessed one. The path is narrow (it needs a prior slot for the same tree on the verifying clone), but when hit it publishes a signed GREEN that the current bar run did not produce. | instance | - | class:carried-forward-row-read-as-current |
| 3 | correctness | tools/run-gates/precommit.py@7bbc6ee6:185 | medium | medium | confirmed | This diff adds tools/run-gates/precommit.py; the file does not exist at the base. Line 185 of read_staged runs `git diff --cached --name-only --diff-filter=ACMR -z`, so deleted paths are dropped. The runner's changed() at tools/run-gates/run-gates.sh@04da8977:599 is `! git diff --quiet "$BASE" -- "$@"`, and that does count deletions. The base .githooks/pre-commit:195 read `git diff --cached --name-status --no-renames` with no filter. The module docstring (lines 13-15) and check_guard_trips both claim the runner's semantics. I read tools/gate-legs.json: all four precommit rows (codebase-map coverage + freshness, kickoff-manifest ratchet, unattended skill wiring, template size <=48KiB) have guard None, so today every row runs on every commit. The defect is real and introduced by this diff, but it stays latent until a row declares a guard, and the bar still catches the change at push time. That makes its effect contained. | sound | - | class:two-guards-one-question-two-answers |
| 4 | seams | tools/memory-tree/adopt-memory-tree.sh@277edcb9:747 | medium | medium | confirmed | In the diff's kit.toml, curation-debt, legacy-files, stale-header-waiver and unarmed-branches are now [[ledger]] populations (lines 739-828), each with a `*-to-ledger` upgrade step (lines 905-957). At the base, kit.toml does not mention them. tools/memory-tree/adopt-memory-tree.sh@277edcb9:743-753 and :849-853 still write those four homes with only prose comments and no `# ledger ·` header, while readme-contract (line 800) and method-carriers (line 817) do get the header. The unarmed-branches comment at line 748 still says `Fields: gate<TAB>check<TAB>ordinal<TAB>signature`. Base check-arms parse_pin read that tab-split grammar; this diff's parse_pin reads `LL.read_rows(p, len(PIN_FIELDS), verbatim=PIN_VERBATIM)` with PIN_FIELDS=(path,check,signature), so the shipped comment now describes a grammar the reader rejects. I re-ran the probe in a scratch git directory with the header-less scaffolded unarmed-branches.txt and legacy-files.txt. `registry_to_ledger.py witness` printed `... is in its legacy grammar: not applied` and exited 1 for both. So a fresh adopter reads as owing conversions it never needed, and an adopter who follows the comment gets malformed rows. Both failures are loud rather than a silent wrong verdict, so the effect is contained. | sound | a-spelling-change-strands-its-readers | class:a-spelling-change-strands-its-readers |
| 5 | seams | tools/run-gates/verdict_flow.py@712fc604:551 | low | low | confirmed | verdict_flow.py is new in this range; it is absent at 9e21ac760. At :551 `run_quiet_leg(run, row, n, top, here=HERE)` never reads `here`: the body takes its runner from `profile_bar.RUNNER` at :586. Its caller at :635 calls `(rerun or run_quiet_leg)(run, r, n, top)` and passes no `here`, while `cmd_quiet_rerun` does use its own `here` for `read_wait_ceiling` at :624. The parameter is dead and implies a seam that does not exist. No caller relies on it today, so no verdict comes out wrong. | sound | - | new:parameter-never-read-implies-a-seam |
| 6 | verification | tools/run-gates/selftest-budgets.txt:127 | medium | - | refuted | The facts check out. The row at selftest-budgets.txt:127 is unchanged from the base (it was :125 there), the suite grew from 681 to 1295 lines, and FLOOR_ASSERTIONS went from 19 to 80. But the claimed consequence cannot be established, and part of it is contradicted by the code. Units run no gates, so no reading could be taken during the build. Rows this range added (leg-factory, ratchet, powershell hygiene) are PINNED estimates to be re-priced at the first measured run, which is the close. The file's header says a breach is read and then re-declared. tools/run-gates/run-selftests.sh@b2a29c65:2217/2225 prints OVER BUDGET and goes RED when the serial grading breaches, so a stale budget shows up loudly at the close and is not hidden. That contradicts 'nothing showed it'. Nothing shows the 80-assertion suite actually costs more than 60s: the old reading was 19s, and no new measurement exists. A medium finding that cannot be established is refuted. | unsound | budget-row-not-remeasured-after-added-arms | - |
| 7 | intent | AGENTS.md:278 | low | low | confirmed | I re-ran the probe over 9e21ac760..0c8711aba and it matches the finding: 544 commits, 257 with `Claude Opus 5` and 287 with `Claude Opus 5.5`. AGENTS.md:278 says every agent commit 'ends with' the `Opus 5` trailer. a2675ab88 ends with `Commit-Checked: unattended@1.129` after a 5.5 Co-Authored-By line, and 0c8711aba goes back to `Opus 5`. Two parts of the claim are older than this range. The value drift is: of the 300 commits before the base, 208 already carry `Opus 5.5` and 83 carry `Opus 5`. No trailer-value gate existed at the base either. The new part is position. `Commit-Checked` appears 0 times in the base's tools/lib/commit_trailers.py and in the 300 commits before the base. In this range the kit writes it as a trailer (FLOOR_KEYS, `unchecked`) after Co-Authored-By, so the charter's 'ends with' wording is now untrue for every checked pass commit. Only metadata and wording are affected, and no behaviour changes, so the grade is low. | sound | - | class:rule-stated-with-no-check-that-fails | (DERIVED from the builder's probe)
