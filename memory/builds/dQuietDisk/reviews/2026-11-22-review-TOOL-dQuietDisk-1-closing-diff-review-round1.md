**Serves:** diff-review TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28

# dQuietDisk — Tier-2 CLOSING DIFF review, round 1

*Node `d`, 2026-11-22. This round reads the cumulative diff of build dQuietDisk (disk-churn fixes 1 to 3): the history verdict store and the incremental history legs, one guard diff per bar, the suite template cache, the owned swept scratch root, check-wiring's one listing, govkit update's batch handle and apply reuse, and kit attestation. The base is b3f5a2bc3, the merge that brought dWitnessedBar's land tip in. The tip is the last unit pass. The diff lands on main and ships kits to adopters through govkit update. Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. No spec was supplied: intent came from the caller's statement, read beside the range's commit messages. The checklist had 131 items, acquired by the harness from `--for-diff b3f5a2bc333dfbd4f9fe2b14dafb6fc21b852ca4..879413160dd03c1f0bd28c001007bd08b44e3a1d`, each assigned to exactly one lens: security 27, correctness 26, seams 26, verification 26, intent 26. By design: 3 invariants from the checklist's by-design block.*

**Range reviewed: `b3f5a2bc333dfbd4f9fe2b14dafb6fc21b852ca4...879413160dd03c1f0bd28c001007bd08b44e3a1d`**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER.
Two items are HIGH.
H1: the bash face of the template cache runs its git calls under the caller's environment, so an exported GIT_DIR commits a fixture tree onto the operator's real branch (finding 1).
H2: the new orphan rule of the dead-scratch sweep removes the turnstile suite's "foreign repository" fixture, so a held suite is red and the live-other-repository safety property is ungraded (finding 5).
Five items are MEDIUM, four are LOW.
Most of the MEDIUM and LOW items are verification gaps: new behaviour whose only evidence is an uncommitted probe or an arm that cannot fail.
I recommend folding both HIGH items before the landing, each with its arm seen red first.
The MEDIUM items should be folded or filed as units before the TOOL-dQuietDisk-15 reader of the attestations key is built.
The LOW items can be folded or filed.

## Review shape

Intensity full, raw 13, confirmed 11, refuted 2, merged 0, unverified 0 (0 uncertain), precision 0.85.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 2 | 0 | 2 | 0 | 0 | 0 | 0.00 |
| verification | yes | 7 | 7 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 11 items (0 blocker, 2 high, 5 medium, 4 low).
Adjudicated tally by raw confirmed finding: 11 (0 blocker, 2 high, 5 medium, 4 low).
The two tallies agree because no two confirmed findings describe one defect.
Every confirmed finding keeps its bracketed binding grade.
Finding 6's binding grade is the skeptic's MEDIUM, re-graded from the finder's HIGH.
The correctness lens returned no finding; the lens ran to completion, so this zero is a lens result, not a gap in the run.
The refuted finding 3 shares an address with finding 6 (`tools/govkit/govkit.py@69a24921:4118`), but it is a different defect (no reader of the key, against no arm grading the key), so no twin is flagged.
The refuted finding 4 (history-store aging by write time) matches no confirmed finding.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 0 duplicate refutations counted as merged confirmations.
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 9 judged sound, 0 judged UNSOUND, 2 judged INSTANCE-ONLY (findings 1 and 13), curing the cited instance and leaving its class standing, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic (finding 6, HIGH to MEDIUM).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 2. Same-address pairs shown: 0.
- Dispositions: unclassed is `refuse`; 131 class slugs handed; 226 leg names read from tools/gate-legs.json.

Every count above is zero where it would mark the run incomplete, so this run is complete.

## HIGH

### H1. The bash template cache runs git under the caller's GIT_DIR, so a fixture commit can land in the real repository (finding 1)

**Where:** `tools/lib/template-cache.sh@14b641eb:57` (`resolve_template`, lines 56-58) and `tools/lib/template-cache.sh@14b641eb:87` (`build_template_clone`, lines 87-88).
The same block is copied inline at `tools/lib/lib-selftest.sh@192087e2:111` (lines 111-143).

**What is wrong:** `resolve_template` runs `git -C <stage>/repo init`, `add -A`, `commit -m base` and `config --local`, and `build_template_clone` runs `clone` and `git -C <dest> remote remove origin`.
All of them run with the caller's environment unchanged.
An exported GIT_DIR overrides the repository discovery that `-C` relies on.
The Python face strips these variables: `tools/lib/template_cache.py@63ffe62b:130` drops every name in GIT_ENV_LEAKS for each `run_git`.
So the two faces of one protocol give different answers.
run-gates.sh unsets GIT_DIR only inside the subshells at :422 and :6262, and tools/lib/lib-selftest.test.sh@f019992e:10 only for its ROOT probe.

**Consequence:** when a `build_fixture --template` suite runs with GIT_DIR exported, the builder's tree is committed as `base` onto the current branch of the repository GIT_DIR names, which is the operator's real repository.
The probe, run in a scratch repo `real`: `resolve_template "$PWD/root" k1 b` left `real` with a new commit `642e4c9 base` adding f.txt, and `build_template_clone` then exited 128 fetching from real's origin.
The .githooks/ hooks scrub these variables, which narrows the path but does not close it.

**Fix (judged INSTANCE-ONLY by the skeptic; the class-level fix follows):** strip every name in GIT_ENV_LEAKS from the whole template path, not only from the cache's own git calls.
Run the builder subshell under the scrub too: `( unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES GIT_COMMON_DIR GIT_NAMESPACE GIT_PREFIX GIT_LITERAL_PATHSPECS GIT_GLOB_PATHSPECS GIT_NOGLOB_PATHSPECS GIT_ICASE_PATHSPECS; cd "$_tc_s/repo" && "$@" )`.
Wrap every git call in `resolve_template`, `build_template_clone` and `derive_template_key` the same way.
Propagate the change byte-identically to lib-selftest.sh.
Add the GIT_DIR-exported arm with a builder that commits its own tree.
The finder's proposal (scrub only the cache's own git calls with `env -u` or an `unset` subshell, plus an arm asserting a scratch repo's HEAD did not move) cures the cited instance alone: it leaves the builder subshell running under the leaked GIT_DIR.

**Left-shift gate:** an arm in the `python resolver (behaviour + inline parity + idiom ban)` family's style for shell: a check that every `git` call in a copy-installed bash face whose Python twin uses GIT_ENV_LEAKS runs under the same scrub, red on a bare `git -C`.

### H2. The orphan rule sweeps the turnstile suite's foreign-repository fixture, and the arm that proves it is spared goes red (finding 5)

**Where:** `tools/run-gates/run-gates.turnstile.test.sh@01d29320:1185` (the fixture) and `tools/run-gates/run-gates.turnstile.test.sh@01d29320:1233` (the arm), against `tools/run-gates/run-gates.sh@d35d666e:2446` (lines 2446-2454, the new `scan_dead_work` branch).

**What is wrong:** at the base, `scan_dead_work` skipped any owner whose common dir differed from `WORK_COMMON`.
TOOL-dQuietDisk-9 S9 changed that: it continues only for a relative common dir or one where `[ -d "$common" ]` holds.
The fixture, unchanged from the base, plants owner `999999\t/nowhere/else/.git\t0`.
That path is absolute and names no directory, and `ts_alive 999999` is false, so the new rule treats it as an orphan.
The sweep root is `$A22`, so the first bar removes `gate-work.foreign` and appends a `scratch-swept dead bar pid 999999` health line.

**Consequence:** the arm "a dead bar's scratch whose owner names ANOTHER repository survived" fails.
The health-line arm at :1227 sees two scratch-swept lines instead of one and fails too.
The held turnstile leg will be red at the close.
The suite was not re-run after S9; the unit 9 ledger marks AC5 OWED.
No fixture now reaches the "another LIVE repository is spared" property of a directory-deleting sweep.

**Fix (judged SOUND by the skeptic):** point the foreign owner's common dir at a directory that exists, for example `mkdir -p "$tmp/other/.git"`, so the arm keeps grading the live other-repository rule.
Add a separate orphan arm: a dead owner whose absolute common dir is missing must be swept, and one whose common dir is relative must be kept.
Re-run run-gates.turnstile.test.sh and record the red-then-green.

**Left-shift gate:** the `run-gates turnstile` leg already catches this once run; the gap is that a unit changing a swept-root predicate closed without running it.
Make a change under `scan_dead_work` name the turnstile suite as a must-run row in its unit's acceptance, so OWED cannot stand for it.

## MEDIUM

### M1. derive_kit_attestations writes a certification into every receipt, and no committed check grades it (finding 6)

**Where:** `tools/govkit/govkit.py@69a24921:4118`, called through `write_install_receipt` from apply (:8660), update (:12275, :13299, :13343, :13349) and adopt (:13984).

**What is wrong:** the function decides which kits are recorded as proven green and ships that record to adopters.
It does so through a row hash that must match run-gates' own (DECLARATIVE_LEG_KEYS loaded by path, with a whole-row fallback), a transitive `requires` closure, and blob identity at the record's sha against `to_commit`.
`grep -n attest tools/govkit/selftest.py` prints nothing, and no other suite covers it.
All 44 observations in the unit 14 ledger came from an uncommitted session-scratch script; the govkit selftest leg and AC4's "steps stays last" check are OWED.

**Consequence:** a drifted row hash, a dropped `requires` member or a source compared at the wrong commit would ship a wrong `attestations` list with every suite green.
The skeptic re-graded HIGH to MEDIUM: under spec S6 and the "No hold in any bar" non-goal, nothing in this diff reads the key, so a wrong list is an inert record until TOOL-dQuietDisk-15 reads it.

**Fix (judged SOUND by the skeptic):** add selftest arms that plant `gate-selftest-last/<key>` records in a fixture gov.
Cover: an attestation present with a matching row and sources; none with the record removed, with `row` set to forty zeros, or with a source moved after the record's sha; none when a required kit's source moved; and `[]` at a `to_commit` other than HEAD.
Add one arm that computes the row hash through run-gates.sh's own program and compares it with this function's hash.
Observe each arm red by reverting the clause it guards.

**Left-shift gate:** a unit ledger whose observations name a session-scratch script must cite a committed arm for each acceptance line before the unit closes; `govkit selftest` is the leg that then carries it.

### M2. The outer swept root, the TEMP/TMP export and the Python sweep faces have no committed check (finding 7)

**Where:** `tools/run-gates/run-gates.sh@d35d666e:2405` (GATE_OUTER_AMBIENT_TMP and the "names no directory" NOTE at 2410-2415, the TMPDIR/TEMP/TMP export at 2491), and the Python faces `scan_dead_scratch` and `init_owned_tempdir` in tools/lib/owned_scratch.py.

**What is wrong:** a grep over tools/*.test.sh, tools/lib/*.test.sh and .githooks/pre_push_bar_selftest.py finds GATE_OUTER_AMBIENT_TMP only in pre-push.test.sh's BAR_INERT_KNOBS list.
Nothing asserts the outer root is swept, nothing asserts the NOTE, and no leg's temp directory is checked to land under `gate-work.*/tmp`.
owned_scratch.py has no selftest; tools/lib/resolve-python.test.sh@4f356762:448-451 checks only that its copies are byte-identical.
Unit 9's acceptance ledger marks AC8-AC11 OWED; they were probed once outside the tree.

**Consequence:** `scan_dead_scratch` deletes directories, and 21 Python suites call `init_owned_tempdir`, which sweeps the real temp root on every run.
A widened sweep predicate (a dropped `py:` or common-dir test), an ignored outer root or a dropped TEMP/TMP export would all pass every committed arm.
The effect is contained to scratch directories and leaked temp files.

**Fix (judged SOUND by the skeptic):** add run-gates.test.sh fixture bars for three cases.
GATE_OUTER_AMBIENT_TMP=A: A is counted and swept, a planted dead root in A is removed, and a NOTE prints when A is missing.
TEMP/TMP: a leg running `node -e` (or `python -c`) on `os.tmpdir()` lands under `gate-work.*/tmp`, and fails with the export removed.
Python sweep: a self-test of owned_scratch.py planting live, dead-same-repo, dead-other-existing-repo, orphan and bash-owned roots.
Observe each case red.

**Left-shift gate:** the same as M1: an OWED acceptance line on a directory-deleting path blocks the unit's close until a committed arm discharges it.

### M3. The history-store arms cannot tell a store that serves hits from one that never hits (finding 8)

**Where:** `tools/unattended/check-pass-order.test.sh@936c6d11:1021` (lines 1021-1076) and `tools/unattended/check-brief-recorded.test.sh@c041094f:943` (lines 943-1010).

**What is wrong:** the store arms assert a red when a key moves, a non-empty items dir after the cold run, output that names the right units, and warm, torn and storeless output being equal.
A store that writes items but never serves a hit satisfies all of them.
The "announced from the store" arm checks `NOT GRADED — ARCH-tP-1`, which a cold run also prints.
tools/unattended/check-pass-order.sh@bc36c481:536-543 leaves PO_ON at 0 on any store failure and prints nothing about the store.
The lookup key (PO_Q, lines 690-712) and the write key (PO_W, lines 747-1050) are built separately.

**Consequence:** if the two key spellings diverge, or a later edit makes every lookup miss, both suites stay green while the incremental legs re-grade everything on every bar.
That silently loses the saving TOOL-dQuietDisk-2 and -3 exist for, and makes the stale-serve arms vacuous.
Verdicts stay correct.

**Fix (judged SOUND by the skeptic):** add a warm-run hit assertion to each suite.
Either count `cat-file`/`log` spawns under GIT_TRACE2_EVENT on a second run at an unmoved HEAD and require fewer than the cold run, or add a debug knob that prints the served-item count and require it to be greater than 0.
Observe the assertion red with the lookup key deliberately mangled.
routed_commits.py's arm, which spies `read_commits` and asserts a warm run logs `[]`, is the model.

**Left-shift gate:** add to the bug-class checklist: an arm for a cache must assert a hit on the warm run, not only that warm and cold outputs agree.

### M4. A template key that ignores builder arguments can serve the wrong base repository (finding 13)

**Where:** `tools/lib/lib-selftest.sh@192087e2:190` (`build_fixture --template`, lines 189-190), against `tools/lib/template-cache.sh@14b641eb:13` (the USAGE line) and `tools/lib/template-cache.sh@14b641eb:38` (`derive_template_key`, lines 38-46).

**What is wrong:** `build_fixture --template` keys the template by `derive_template_key "$1" <input files>`, which covers only the builder name, its `declare -f` and the input files' blob ids.
It then passes every argument to `resolve_template`, which runs the builder with them.
The canonical face documents `resolve_template <root> <key> <builder> [<arg>...]`, and its WHAT THIS DOES NOT CHECK line names builder helpers but not builder arguments.

**Consequence:** two batches in one cache root calling `build_fixture --template "" mkrepo a` and then `... mkrepo b` derive the same key.
The second reuses the template built from `a` and grades its arms against the wrong base repository, with no error.
The defect is latent: the only `build_fixture --template` caller (tools/lib/lib-selftest.test.sh@f019992e:180) passes no arguments, the turnstile suite passes the constant `.`, and the pre-push suite folds its arguments into an fx-args input file by hand.

**Fix (judged INSTANCE-ONLY by the skeptic; the class-level fix follows):** fold the builder arguments into the key inside `resolve_template` itself, so every caller is covered, both `build_fixture` and direct callers like tools/run-gates/run-gates.turnstile.test.sh@01d29320:365.
For example, when arguments are present, `resolve_template` hashes `$_tc_k` together with `printf '%q ' "${@:2}"` into the directory key.
Or give `derive_template_key` an explicit `--` separator for builder arguments and require every `resolve_template` caller to pass them through it.
Add the bash face's argument rule to the WHAT THIS DOES NOT CHECK line and to template_cache.py's protocol docstring.
The finder's proposal (hash the arguments in `derive_template_key`, or have `build_fixture --template` refuse more than one positional argument) cures the cited instance alone: direct `resolve_template` callers stay unkeyed.
Probe for the arm: two `build_fixture --template "" mk x` and `mk y` batches in one root, where `mk` writes `"$1"` to a file; the second clone must hold `y`, and holds `x` today.

**Left-shift gate:** add to the bug-class checklist: every value a cached builder reads is in its key, checked by an arm that varies each input alone and expects a new key.

### M5. Arm 3h1 never proves a plain-guarded leg was decided by the one moved list (finding 9)

**Where:** `tools/run-gates/run-gates.test.sh@aa765343:1489` (lines 1489-1532), against `tools/run-gates/run-gates.sh@d35d666e:3559` (lines 3559-3573) and `changed()` at :599.

**What is wrong:** a plain guard is answered from the slice of `base.moved`; any other guard falls back to `changed()`, which runs `git diff --quiet BASE -- <guards>`.
That fallback gives the same skip or run result for `ga/f` and `xga/f`.
So if `check_plain_guard` always returned 1, if `base.moved` were never consulted, or if `write_guard_slices` were dropped from the guard pass, arm 3h1 would still see "skip dir guard" on `xga/f` and "ok dir guard" on `ga/f`.
The trace checks assert only that the name-only diff ran once and that the held selection did not re-diff.
The `xga/f` near-miss catches a match-anywhere bug but not a dropped boundary (`gax/f` against `ga`).

**Consequence:** TOOL-dQuietDisk-5's core claim, one diff per bar, has no arm that can fail.
A regression back to a per-leg diff would ship green and restore the churn the unit removed.

**Fix (judged SOUND by the skeptic):** in the traced run, also assert that no ` diff --quiet [0-9a-f]{40} -- ga/` line appears, and that the glob guard's own diff does appear.
Add a `gax/f` boundary fixture against guard `ga/` (or `ga`).
Observe the arm red with `check_plain_guard` forced to return 1.

**Left-shift gate:** the M3 checklist entry covers it: an arm for a fast path must assert the slow path did not run, not only that both give the same answer.

## LOW

### L1. blob_at sends a name ending in CR to the batch handle, which answers with a different file (finding 2)

**Where:** `tools/govkit/upgrade_steps.py@36c4b740:2734`.

**What is wrong:** the guard is `batch is not None and not batch.dead and "\n" not in name`, with no CR test.
git strips a trailing CR from each `cat-file --batch` input line, so `<commit>:<path>\r` is answered with the blob of `<path>`.
The `git show` spawn path answers missing for the same name.
tools/lib/history_store.py@40eeb4d4:481 (`BatchReader.read_reply`) already guards both `\n` and `\r`.
This diff added BlobBatch and passes it from update (tools/govkit/govkit.py@69a24921:9819), which made the path reachable there.

**Consequence:** a receipt row whose `source` or a descriptor path ending in CR is read, classified and attested against the bytes of a different file when the handle is used, and reads as missing without it.
The skeptic's probe: `printf 'HEAD:a\r\n' | git cat-file --batch` answered with the content of `a`, while `git show "HEAD:a<CR>"` exited 128.
Reaching it needs a path with a trailing CR, so it is narrow and contained.

**Fix (judged SOUND by the skeptic):** change the guard to `"\n" not in name and "\r" not in name`, as `BatchReader.read_reply` does, so such a name falls through to the `git show` spawn.
Add a `blob_at` arm that asks for a path ending in CR with a batch handle and without one, and asserts both answers are None.

**Left-shift gate:** one shared `batch_safe_name` predicate in tools/lib/, inlined into every copy-installed batch reader and held byte-identical by the inline-parity check, so the two readers cannot answer differently.

### L2. The template race arm can pass without the two racers having raced (finding 10)

**Where:** `tools/lib/lib-selftest.test.sh@f019992e:216`.

**What is wrong:** the builder's `sleep 1` is the only thing overlapping the two background `resolve_template` calls.
`resolve_template` (tools/lib/lib-selftest.sh@192087e2:104) returns `reused` at once if `ready` already exists.
A second racer that forks more than about a second late never builds and never reaches the `mv -T` collision.
Both racers' stderr, where the `built`/`reused` lines go, is sent to /dev/null.

**Consequence:** under load the arm passes on "entries 1 nested 0" and "same template" without having raced.
Product behaviour is unaffected.

**Fix (judged SOUND by the skeptic):** have the builder append a line to a shared log, and require two lines (both racers built) before grading entries and nesting.
Alternatively, gate the builder on a go-file that both racers must reach before either proceeds, instead of a fixed sleep.

**Left-shift gate:** a `shell hygiene`-style scan in suites that reds on a `sleep` inside a function launched with `&` unless the arm also asserts the overlap happened.

### L3. BlobBatch's missing, ambiguous and dead-handle branches have no arm (finding 11)

**Where:** `tools/govkit/upgrade_steps.py@36c4b740:2734` (the batch branch of `blob_at`, lines 2733-2756).

**What is wrong:** `grep 'batch=|BlobBatch|build_blob_batch' tools/govkit/selftest.py` prints nothing.
The update arms reach the read path only through govkit.py, so they cover the happy path.
Nothing exercises the `missing`/`ambiguous` reply, the end-of-stream or bad-header fallback that sets `dead`, or the newline-name spawn.
The unit 16 ledger probes are not committed.

**Consequence:** a dead or short stream read as None would turn a gov blob into "absent" and a row into a withdrawal, with every suite green.
So would a desync that fails to mark the handle dead, or a non-blob object returned as a blob.
Nothing is wrong today.

**Fix (judged SOUND by the skeptic):** add selftest arms that call `upgrade_steps.blob_at` with a BlobBatch over a fixture repository.
Check that a missing path gives None and matches the spawn; that killing the batch process mid-run makes the next read return the right bytes through `git show` and sets `dead`; and that a name containing a newline takes the spawn path.

**Left-shift gate:** the `harness arms (fail branches armed or pinned)` leg's rule extended to govkit's upgrade_steps.py, so each fallback branch of a new reader is armed or pinned.

### L4. The owned-root comment says every row's TMPDIR sits under it, which holds only for pooled rows (finding 12)

**Where:** `tools/run-gates/run-selftests.sh@df2db125:1035` (lines 1035-1036).

**What is wrong:** the new header says "Every row's TMPDIR, TEMP and TMP sit under it, so a row's template cache finds this root's templates".
Only the `--pooled`/`--sweep` launch (line 1701) sets TMPDIR, TEMP and TMP, under `$RS_SCRATCH/s`.
The `--serial` loop (about line 2407) and the two `--attribute` evals (lines 2272 and 2323) run each row with the ambient TMPDIR.

**Consequence:** in `--serial` and `--attribute` runs, `resolve_template_root` (tools/lib/lib-selftest.sh@192087e2:79-90) does not find this runner's root, and native children's temp files land outside the swept root.
Behaviour stays safe, because rows fall back to the bar's root or SELFTEST_ROOT.
The next change that relies on the comment will be wrong for two of the three modes.

**Fix (judged SOUND by the skeptic):** either export TMPDIR, TEMP and TMP to a directory under `$RS_SCRATCH` before the `--serial` loop and the attribution evals, or narrow the comment to say only `--pooled` rows run under the root.
Probe: run `bash tools/run-gates/run-selftests.sh --serial --kit <one kit>` with a suite that prints `$TMPDIR`, and check the path is not under the run's `gate-work.*` root.

**Left-shift gate:** an arm in the `run-selftests self-test` leg that runs one row in each mode and asserts its TMPDIR is under the runner's root, which also makes the export the fix rather than the comment edit.

review-shape kind=diff-review round=1 intensity=full at=synth raw=13 confirmed=11 refuted=2 merged=0 unverified=0 blocker=0 high=2 medium=5 low=4 agents=11 out-tokens=149089 trigger=owed shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=2 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/lib/template-cache.sh@14b641eb:57 | high | high | confirmed | tools/lib/template-cache.sh does not exist at b3f5a2bc3, so this diff introduced the bash face. At 879413160, resolve_template runs `git -C "$_tc_s/repo" init/add -A/commit -m base/config --local` and build_template_clone runs `clone` and `git -C "$2" remote remove origin`, all with the caller's environment unchanged. The same block is copied inline into lib-selftest.sh at lines 111-143. An exported GIT_DIR overrides the repository discovery that -C relies on, so add and commit land in the repository GIT_DIR names. The Python face does strip these variables: tools/lib/template_cache.py@63ffe62b:130 builds `env = {k: v ... if k not in GIT_ENV_LEAKS}` for every run_git, so the two faces give different answers. run-gates.sh only unsets GIT_DIR inside the subshells at :422 and :6262, and tools/lib/lib-selftest.test.sh@f019992e:10 only for its ROOT probe. The path is narrow because it needs an exported GIT_DIR and the hooks scrub it. But the consequence on that path is a stray commit on the operator's real branch, which is high under the rubric. | instance | inherited-git-dir-pins-the-work-tree-to-the-cwd | class:inherited-git-dir-pins-the-work-tree-to-the-cwd |
| 2 | security | tools/govkit/upgrade_steps.py@36c4b740:2734 | low | low | confirmed | At tools/govkit/upgrade_steps.py@36c4b740:2734 the guard is `batch is not None and not batch.dead and "\n" not in name`, and nothing checks for CR. I re-ran the probe in a scratch repo. `printf 'HEAD:a\r\n' \| git cat-file --batch` answered `ce01362... blob 6` with the content of a. `git show "HEAD:a<CR>"` exited 128 with `path 'a?' does not exist`. tools/lib/history_store.py@40eeb4d4:481 (BatchReader.read_reply) does guard `"\n" in name or "\r" in name`. Base blob_at already had a batch branch, used by derive_introduced. This diff added BlobBatch and passes it from update (tools/govkit/govkit.py@69a24921:9819), which made the path reachable there. Reaching it needs a receipt or descriptor path that ends in CR, so it is narrow and contained. | sound | two-answers-to-one-question | class:two-answers-to-one-question |
| 3 | seams | tools/govkit/govkit.py@69a24921:4118 | medium | - | refuted | By design under the unit's ratified spec. memory/builds/dQuietDisk/spec/2026-11-20-spec-TOOL-dQuietDisk-14.md S5 requires that `apply`, `update --write` and `adopt --write` pass attest, so every receipt carries attestations. Its non-goals say outright: no hold in any bar, since reading the key is TOOL-dQuietDisk-15's job; no tracked attestation file, the evidence being gov's own held records; and 'No policy key'. Deferring the reader is a recorded decision in RUN.md:124 and BACKLOG TOOL-dQuietDisk-33 ('TOOL-dQuietDisk-14's receipt attestations are already carried'). That a gov clone's local held-tier records shape the key follows from the same chosen design, and WIRE-INTO-PROJECT.md:1108-1118 documents the key as inert. On the r.problems and ungraded paths the rows written are from to_commit. Each attestation carries its own gov_commit and a digest over to_commit's blobs, so its claim stays accurate whatever the receipt's stamp says. The finder graded this medium, and its substance is the spec's choice. | unsound | - | - |
| 4 | seams | tools/lib/history_store.py@749440b3:614 | low | - | refuted | The code does what the finding describes. At 879413160, HistoryStore.write returns early when read(fields)==body, read() never touches mtime, and remove_aged unlinks items with st_mtime < now-AGE_LIMIT. But this is what spec TOOL-dQuietDisk-1 S6 prescribes: 'remove_aged() unlinks each item file older than 30 days by mtime'. write's docstring states the warm-run rule on purpose: 'An item already holding it is left as it is, so a warm run writes nothing.' This is a disk-churn build, and a warm run writing nothing is the design. Aging by write time is the specified policy, not a defect. The finder's own account of the cost is one full regrade of a stable key per 30 days, never a wrong verdict. | unsound | - | - |
| 5 | verification | tools/run-gates/run-gates.turnstile.test.sh@01d29320:1185 | high | high | confirmed | At the base, scan_dead_work skipped any owner whose common dir differed: `[ "$common" = "$WORK_COMMON" ] \|\| continue`. At 879413160, tools/run-gates/run-gates.sh@d35d666e:2451-2453 continues only for a relative common dir or one where `[ -d "$common" ]` holds. The test at tools/run-gates/run-gates.turnstile.test.sh@01d29320:1185 (unchanged from base line 1159) plants owner `999999\t/nowhere/else/.git\t0`. That path is absolute and names no directory, and ts_alive 999999 is false, so the dir is now swept. The sweep root is RG_SWEPT_TMP=${TMPDIR}=$A22, per lines 2410-2416 and 2477, so the first bar removes gate-work.foreign and appends a 'dead bar pid 999999' health line. The arm at :1233 ('a dead bar's scratch whose owner names ANOTHER repository survived') then goes red. The arm at :1227 also sees two scratch-swept lines instead of the one it expects. The live-other-repository case no longer has a fixture that reaches it. This is a red held suite introduced by this diff, and it leaves a safety property of a directory-deleting sweep ungraded. | sound | - | gate:run-gates turnstile |
| 6 | verification | tools/govkit/govkit.py@69a24921:4118 | high | medium | confirmed | At 879413160, derive_kit_attestations (tools/govkit/govkit.py@69a24921:4118) is called by write_install_receipt with attest= from apply (8660), update (12275, 13299, 13343, 13349) and adopt (13984). `git grep -i attest` over tools/ finds no reference outside govkit.py except unrelated unattended --attest text. Neither selftest.py nor any suite covers it. The unit 14 ledger confirms that all 44 observations came from an uncommitted session-scratch script, and that the govkit selftest leg is OWED. So a regression in the row hash, the requires closure or the blob-at-sha comparison would ship a wrong attestations list with every suite green. I grade it medium, not high: spec S6 and the 'No hold in any bar' non-goal mean nothing in this diff consumes the key. A wrong list is an inert record in adopters' receipts until TOOL-dQuietDisk-15 reads it. | sound | - | class:observed-by-claim-no-arm-discharges |
| 7 | verification | tools/run-gates/run-gates.sh@d35d666e:2405 | medium | medium | confirmed | In run-gates.sh at 879413160, lines 2410-2415 read GATE_OUTER_AMBIENT_TMP, swap RG_SWEPT_TMP and print the 'names no directory' NOTE, and line 2491 exports TMPDIR, TEMP and TMP as $WORK/tmp. A git grep over tools/*.test.sh, tools/lib/*.test.sh and .githooks/pre_push_bar_selftest.py finds GATE_OUTER_AMBIENT_TMP only in the BAR_INERT_KNOBS list of pre-push.test.sh. Nothing asserts the outer root is swept, nothing asserts the NOTE, and no leg's temp directory is checked to land under gate-work.*/tmp. The only mentions of scan_dead_scratch and init_owned_tempdir are the definitions and calls themselves. tools/lib/owned_scratch.py has no selftest, and tools/lib/resolve-python.test.sh@4f356762:448-451 holds only the copies byte-identical to it. Unit 9's acceptance ledger (2026-11-22-build-TOOL-dQuietDisk-9-1-acceptance-ledger.md) says the pass ran no fixture bar or suite and marks those checks OWED. So a widened sweep predicate, an ignored outer root or a dropped TEMP export would all pass every committed arm. The impact is contained to scratch directories and leaked temp files. | sound | - | class:observed-by-claim-no-arm-discharges |
| 8 | verification | tools/unattended/check-pass-order.test.sh@936c6d11:1021 | medium | medium | confirmed | In check-pass-order.test.sh (lines 1021-1076) and check-brief-recorded.test.sh (lines 943-1010), the store arms assert four things: a red when a key moves, a non-empty items dir after the cold run, output that names the right units, and warm, torn and storeless output being equal. A store that writes items but never serves a hit satisfies every one of these. The 'announced from the store' arm checks 'NOT GRADED — ARCH-tP-1', which a cold run also prints. tools/unattended/check-pass-order.sh@bc36c481:536-543 says any store failure leaves PO_ON at 0, so every read misses and nothing about the store is printed. PO_Q (lines 690-712) and PO_W (lines 747-1050) are built separately, so if their keys diverged every lookup would silently miss, and no arm would go red. Correctness is unaffected, but the incremental saving the change exists for would be lost with nothing to flag it. The defect is contained. | sound | - | class:ab-arm-never-did-the-work |
| 9 | verification | tools/run-gates/run-gates.test.sh@aa765343:1489 | medium | medium | confirmed | In run-gates.sh at lines 3559-3573, a plain guard is answered from the slice of base.moved, and any other guard falls back to changed(). Per line 599, changed() runs git diff --quiet BASE -- guards, which gives the same skip or run result for ga/ and xga/f. So if check_plain_guard always returned 1, or base.moved were never consulted, arm 3h1 (tools/run-gates/run-gates.test.sh@aa765343:1489-1532) would still see 'skip dir guard' on xga/f and 'ok dir guard' on ga/f. The trace checks only assert that the name-only diff ran once and that the held selection did not re-diff. Neither asserts that the per-leg diff --quiet for ga/ is absent, and base.moved is written either way. write_guard_slices tests substr(p,1,len(g)+1)==g"/". The xga/f fixture catches only a match-anywhere bug, not a dropped boundary such as gax/f against ga. So the one-diff-per-bar claim has no arm that can fail. | sound | - | class:rule-stated-with-no-check-that-fails |
| 10 | verification | tools/lib/lib-selftest.test.sh@f019992e:216 | low | low | confirmed | The trace arm is new in this diff; the base copy of lib-selftest.test.sh has no 'racing' arm. In it, mkr's `sleep 1` is the only thing that makes the two background resolve_template calls overlap. resolve_template (tools/lib/lib-selftest.sh@192087e2:104) returns 'reused' at once if `$_tc_dir/ready` already exists. So a second racer that forks more than about 1s late never builds and never reaches the `mv -T` collision. Both racers' stderr, where the 'built'/'reused' lines go, is sent to /dev/null. The arm checks only 'entries 1 nested 0' and 'same template', and a run that never raced also meets both. That makes it a real but rare vacuous pass, with no effect on product behaviour, so low. | sound | fixed-sleep-does-not-place-a-signal | class:fixed-sleep-does-not-place-a-signal |
| 11 | verification | tools/govkit/upgrade_steps.py@36c4b740:2734 | low | low | confirmed | BlobBatch and the batch branch of blob_at (tools/govkit/upgrade_steps.py@36c4b740:2733-2756) are new in this diff. A grep for BlobBatch, blob_batch or `.dead` finds no reference in any test: the only caller is tools/govkit/govkit.py@69a24921:9819, and the other hits are unrelated 'dead-path' legs and a run-gates sleep loop. The update arms reach the read path through govkit.py, so they cover the happy path, but nothing deliberately exercises these branches: the missing/ambiguous reply, the end-of-stream or bad-header fallback that sets `dead`, or the newline-name spawn. A regression there (a dead stream read as None) would go unseen. This is a verification gap with no current wrong behaviour, so low. | sound | - | class:refusal-branch-with-no-arm |
| 12 | intent | tools/run-gates/run-selftests.sh@df2db125:1035 | low | low | confirmed | The owned-root header is new in this diff; it is absent from the base run-selftests.sh. At 879413160, the only place TMPDIR, TEMP and TMP are set for a row is line 1701, in the pooled launch. The --serial loop (`out=$(eval "$argv" 2>&1)`, about line 2407) and both attribution evals (`eval "$argv" > $ATTR_TMP/l.out` and `( cd "$ATTR_WT" && eval "$rargv" )`) inherit the ambient TMPDIR. As a result, resolve_template_root (tools/lib/lib-selftest.sh@192087e2:79-90) walks the ambient path and does not find this runner's gate-work root. The comment's claim that every row's TMPDIR sits under the root is false in two modes. Behaviour stays safe, because rows fall back to the bar's root or SELFTEST_ROOT, so the defect is a misleading comment: low. | sound | a-grep-for-a-word-is-a-presence-probe | class:invariant-held-on-one-admission-path |
| 13 | intent | tools/lib/lib-selftest.sh@192087e2:190 | medium | medium | confirmed | Checked at 879413160 and new in this diff: tools/lib/template-cache.sh does not exist at base b3f5a2bc3. In tools/lib/lib-selftest.sh@192087e2:189-190, build_fixture --template builds the key with `derive_template_key "$1" <inputs>`, which uses only the builder name, its `declare -f` and the input files' blob ids (template-cache.sh derive_template_key). It then calls `resolve_template "$_st_r" "$_st_k" "$@"`, and resolve_template runs `( cd stage/repo && "$@" )` with every builder argument. If a later batch in the same root calls the same builder with different arguments, resolve_template finds `ready` under the first batch's key and prints 'reused'. The arms are then graded against the wrong base repository, and nothing reports an error. The USAGE header documents `resolve_template ... <builder> [<arg>...]`, and the WHAT THIS DOES NOT CHECK line leaves builder arguments out. The defect is latent: the only build_fixture --template caller (tools/lib/lib-selftest.test.sh@f019992e:180) passes no arguments, and the turnstile suite always passes the constant '.'. So the effect is contained to future callers. | instance | - | new:cache-key-omits-an-input-the-builder-reads |
