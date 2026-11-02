**Serves:** spec-audit TOOL-dSafePassage-99@rev-1 TOOL-dSafePassage-100@rev-1

# Tier-2 review: round-1 spec audit of TOOL-dSafePassage-99 and 100

The close's arm observation at 390033278 found two bar reds, and the run adopted both under UNATTENDED-PROTOCOL section 11. The two units have disjoint write sets and build concurrently.

- 99 fixes the govkit selftest leg. 87 AC6 loads a staged `upgrade_steps.py` copy in process, and the copy's `load_govkit()` rebinds `sys.modules['govkit']` to its own engine. `govkit_module()` then hands later callers that copy, and `check_upgrade_steps` crashes at [dSP-72] with an uncaught Refusal of another class. 99 makes `govkit_module()` hold the real engine at `GOVKIT` and rebind `sys.modules` on every call. It routes the suite's nine direct `import govkit` sites through that accessor and adds three [dSP-99] checks.
- 100 fixes the python resolver leg. `tools/push-main.test.sh:1409` carries `"${_py_arms:-python3}"`, a parameter-default launcher that the resolver suite's ban refuses. 100 drops the default, guards measure37's call site on `_py_arms`, and rewords its skip line.

Reviewed: memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-99.md@2c6c3a1e66d0dbd88a300c44f71b4ee5347fb406, memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-100.md@ccde7df9e75a863bf547d7478cb5a69e8fd732ca
ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers, highs or mediums. Three items are LOW, and they cover four raw confirmed findings, because findings 3 and 5 describe one defect. Every item is a wording or declaration defect in a spec. None of them changes what either build does. Both builds can go ahead once the three fixes are folded into the specs.

Review shape: intensity full, raw 5, confirmed 4, refuted 1, unverified 0 (0 uncertain), precision 0.80. Adjudicated tally by item: 0 blocker, 0 high, 0 medium, 3 low. By raw confirmed finding: 0 blocker, 0 high, 0 medium, 4 low.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| grounding | yes | 0 | 0 | 0 | 0 | 0 | - |
| reuse | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 0 | 0 | 0 | 0 | 0 | - |
| failure-envelope | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses: 5/5 returned, 0 died. Skeptic batches: 5/5 returned, 0 died. The finding set is complete, so the zero counts from grounding and blast-radius are evidence that those lenses found nothing.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 1 duplicate.
- Fixes on confirmed findings: 3 judged sound, 1 judged UNSOUND, 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 2 re-graded by the skeptic (3 and 4, both from medium to low).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: no spec was supplied. `context` was the caller's statement.
- Checklist: 21 items, each assigned to exactly one of 5 lenses: coherence 5, grounding 4, reuse 4, blast-radius 4, failure-envelope 4.
- By design: the caller's byDesign.
- Move check: no checked subject moved.

## Items

### LOW 1 — spec 99 S2 claims every engine reader routes through `govkit_module()`, but the by-path load at selftest.py:9764 does not (ids 3, 5)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-99.md`, in section 1, section 2 S2 and S3, section 4 "The held engine", "The arm" check 3, the "Inventory", and AC3.

**What is wrong:** Section 1 and S2 say "every other reader of the engine in the govkit selftest routes through `govkit_module()`". There is a tenth reader that the S2 inventory of nine import sites leaves out. At `tools/govkit/selftest.py:9764-9766` the suite loads the engine again by path, using `spec_from_file_location("govkit_mod", GOVKIT)` and then `exec_module`. That load only reads `LANDABLE_ROLES`, `ROLE_KINDS` and `KIND_MARKS`. Section 4 "The held engine" names this site and keeps it on purpose. Check 3 walks only `Import`/`ImportFrom` nodes, and AC3's grep matches only `import`/`from govkit` lines, so this site passes both. S3 still says check 3 "grades S2's class".

**Consequence:** None in behaviour. `load_upgrade_steps` at `govkit.py:116-135` reuses `sys.modules['upgrade_steps']` only when its `__file__` is the real file next to the engine, so the 9764 load can never bind a staged copy's step module. The constants it reads are module-level literals or values derived from them. What is wrong is the wording: the arm certifies "no second engine reader" over a narrower population than S2 claims, and a future by-path or `import_module` reader would pass the gate. (Finding 3's finder graded this medium on an exposure the skeptic showed does not hold. The binding grade is low.)

**Fix:** The skeptic judged finding 3's fix SOUND, and it offers two options. The skeptic judged finding 5's finder fix UNSOUND and corrected it to the narrowing option only. Use that narrowing option, because it satisfies both verdicts:
- Narrow section 1 and S2 to "no import statement in the file names govkit".
- Name `selftest.py:9764-9766` in S2 or in "What it does not cover" as a by-path load left in place. After S1 it reuses the held `upgrade_steps` and reads only `LANDABLE_ROLES`, `ROLE_KINDS` and `KIND_MARKS`.
- Reword section 4's sentence to match, and narrow S3 so that check 3 grades import statements only.
- Leave check 3 and AC3 as written.

Finding 3's other sound option, which is the alternative and not the default, is to change 9764-9766 to `gk = govkit_module()` as a tenth inventory site and widen check 3 to report any `spec_from_file_location` call whose path argument is the name `GOVKIT` outside `govkit_module()`. Its red probe would put back a by-path `GOVKIT` load in a copy of the suite and confirm that check 3 reports its line.

**Left-shift:** Add a bug-class checklist entry: "a scope claim ('every X') must name the predicate the check actually reads, and every known exception in the same spec must be carved out of the claim."

### LOW 2 — spec 99 section 4 "What it does not cover" leaves out the real step module's own `load_govkit()` (id 4)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-99.md`, section 4 "What it does not cover", and section 4 "The arm".

**What is wrong:** The section says the only gap S1 leaves is a sibling module's own `import govkit` (step_gate, upgrade_walk) that runs after a staged load and before the next `govkit_module()` call. It misses a second path. `load_govkit()` at `upgrade_steps.py:2675-2692` reuses `sys.modules['govkit']` only when that module's file is the real `govkit.py`. Otherwise it loads a fresh engine by path. Eleven functions in `upgrade_steps.py` call `load_govkit()`: read_registry_at, read_registry_entries, check_frozen, derive_step_context, write_staging_line, read_staging_journal, write_attended_order, write_step_staged, write_reclaimed_lock, run_lock_fixture and run_rollback_fixture. If one of them is called through a `steps`/`us` binding inside that window, it builds a third engine with its own Refusal class, which the suite's catchers do not catch.

**Consequence:** Nothing in the tree reaches this path today. In 87 AC6 (`selftest.py:3176-3185`), `us87.read_steps` is followed by the pure normaliser `steps.derive_contained_rel`, and then by `gk72 = govkit_module()` at 3197, which rebinds the table before any other step call. Built as written, behaviour is unchanged. The risk is that the next arm author reads the section, believes the gap is closed, and reaches the same crash by this route. (The finder graded this medium. The skeptic re-graded it low because the defect is confined to a prose section's completeness.)

**Fix (judged SOUND by the skeptic):** Name this path in "What it does not cover": any call into the held engine's step module that reaches `load_govkit()` between a staged copy's `load_govkit()` and the next `govkit_module()` call. List the in-process staged loads at f519c1934 that call a copy's `load_govkit()`, which are 87 AC6's `us87.read_steps` and the [dSP-99] arm, and say that no such call follows either of them before `govkit_module()` runs. Alternatively, add a fourth [dSP-99] check that calls `held99.upgrade_steps.load_govkit()` after `govkit_module()` has rebound the table and asserts the result `is held99`. A probe that calls it before the rebind prints False, so the comment at that point can state the window.

**Left-shift:** Prefer the fourth [dSP-99] check, because it turns the window into a graded property. If it is not added, add a checklist entry: "a 'does not cover' section enumerates every caller of the rebinding function, not only the import sites."

### LOW 3 — spec 100 leaves its acceptance ledger out of Files touched and `recall floor` out of its gate line (id 2)

**Where:** `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-100.md`, section 4 Files touched and section 7 Gates.

**What is wrong:** Spec 100 lists only `tools/push-main.test.sh` as touched, and its section-7 leg line names no recall leg. Every dSafePassage build writes `memory/builds/dSafePassage/build/<date>-build-TOOL-dSafePassage-<n>-ledger.md`: builds 92 to 98 each have one. Its sibling 99, built in the same order slot, lists its ledger and names `recall floor` and `recall floor arms` as tripped by the ledger's `memory/` path. `python tools/check-spec-tokens.py --legs-for` over 100's ledger path prints `recall floor <- memory/` and `recall floor arms <- memory/`.

**Consequence:** The two specs give two answers to what a build pass writes and which legs it trips, and 100 under-states its declared legs. Nothing ships wrong, because the bar runs those legs whatever the spec declares.

**Fix (judged SOUND by the skeptic):** Add `memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-100-ledger.md` to 100's Files touched. Add `recall floor` (and `recall floor arms`) to its section-7 line, as 99 does, or say why the ledger's `memory/` path is not counted. Then re-run `python tools/check-spec-tokens.py --legs-for` over the full write set.

**Left-shift:** Have the spec-tokens leg require that a build spec's Files touched includes its own `-ledger.md` path, and that the section-7 line covers every non-broad leg `--legs-for` prints for the declared write set.

## Refuted

- Finding 1 (coherence, spec 100 AC4) was refuted. The cited section already pins the shared fixture, and a green second run is only possible when `_mt_rc` is non-empty and the kit is present. The full reasoning is in the appendix.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=5 confirmed=4 refuted=1 unverified=0 blocker=0 high=0 medium=0 low=4 agents=11 out-tokens=96841

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-100.md:section 6 AC4 (and section 7 New arm line) | low | - | refuted | Refuted on case (2): the cited section already says it. I checked the spec blob (ccde7df9e) at lines 153-166. AC4 cuts the block once and runs it 'in a scratch bash twice, first with `_py_arms=""` and then with `_py_arms` set to the output of `resolve_python`'. It gives one fixture paragraph for that scratch bash: `HERE` is the tools directory, `_mt_rc` comes from the suite's own scan at line 1030, and `PREPARE_REFUSALS`, `tmp`, `ok` and `bad` are set the same way for both runs. So the only input that differs between the runs is `_py_arms`. The second run has to print two `ok — 37` lines, the first naming `refuses 6 way(s)`. In tools/push-main.test.sh:1423-1446 those lines can only come from inside `if [ -n "$_mt_rc" ] && [ -f "$HERE/$_mt_rc/check-arms.py" ]`, so a green second run already proves `_mt_rc` was non-empty and the kit was present. The finder's example (a wrong HERE, or no kit) would make the second run print the skip line instead of two ok lines, so AC4 goes red. AC4's red case points the same way: with the f519c1934 guard and an empty launcher, the run printed two `FAIL — 37` lines, which requires the kit branch to be live. The line-1030 scan (`_mt_rc=$(cd "$HERE" && for d in */; do [ -f "$d/routed_commits.py" ] ...`) is the one shared source the fixture names. Neither run can pass with an empty `_mt_rc` without the other run, or the red case, going red. An explicit `[ -n "$_mt_rc" ]` assertion would repeat what the second run already shows. | sound | fixture-passes-by-finding-nothing |
| 2 | coherence | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-100.md:section 4 Files touched and section 7 Gates | low | low | confirmed | Re-read spec-100: its Files touched (around line 105) lists only `tools/push-main.test.sh`, and its section-7 leg line names no recall leg. Spec-99 lists its acceptance ledger at lines 194-195 and says at lines 262-264 that `recall floor` and `recall floor arms` are tripped by the ledger's memory/ path. `ls memory/builds/dSafePassage/build/` shows ledgers for 94 to 98, and specs 92 to 98 each mention a ledger.md. Specs 93, 97 and 98 name `recall floor`, and 92 to 98 all name `recall floor arms`. I ran `python tools/check-spec-tokens.py --legs-for` over the 100 ledger path plus tools/push-main.test.sh. It printed `recall floor <- memory/` and `recall floor arms <- memory/` for the ledger. Every leg it printed for push-main.test.sh was broad. So 100's build will write a memory/ path that trips two non-broad legs its section 7 leaves out, and its account of the write set and legs is inconsistent with 99's. Graded low because the bar still runs those legs whatever the spec declares: the declared leg list is under-stated, and nothing ships wrong. | sound | two-answers-to-one-question |
| 3 | reuse | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-99.md:section 2 S2 and S3, section 4 "The held engine", "The arm" check 3 and "Inventory" | medium | low | confirmed | The wording mismatch is real. I read spec 99 at blob 2c6c3a1e. S2 says "every other reader of the engine in the govkit selftest routes through govkit_module()", but the inventory table lists nine sites and 9764 is not one of them. Section 4 "The held engine" names `govkit_mod` at selftest.py:9764-9766 and keeps it. Check 3 only walks Import and ImportFrom nodes. `grep -n spec_from_file_location tools/govkit/selftest.py` shows that 9764 is the only by-path load of GOVKIT. Lines 9764-9770 use `gk` only for LANDABLE_ROLES, ROLE_KINDS and KIND_MARKS. The claimed exposure does not hold. The finding says the fresh load is built against whatever sys.modules['upgrade_steps'] holds, but load_upgrade_steps at govkit.py:116-135 only reuses that entry when its __file__ resolves to the upgrade_steps.py beside the engine. Otherwise it loads the real file by path. So the 9764 load can never bind a staged copy's step module, and these constants are module-level literals or values derived from them. What remains is S2's broad sentence overclaiming against section 4's deliberate keep, and S3 saying check 3 grades a class wider than the one it reads. That changes no behaviour, so it is low. | sound | - |
| 4 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-99.md:section 4 "What it does not cover" (and section 4 "The arm") | medium | low | confirmed | The omission is real, but nothing reaches it today. In upgrade_steps.py:2675-2692, load_govkit() reuses sys.modules['govkit'] or '__main__' only when that module's file resolves to HERE/govkit.py. Otherwise it loads a fresh engine by path and puts it in the table. So once a staged copy has displaced sys.modules['govkit'], the real step module's load_govkit() builds a third engine with its own Refusal class instead of returning the held one. Spec-99's section 4 'What it does not cover' names only a sibling module's own `import govkit` (step_gate, upgrade_walk). It does not name this second path, so the claim is true of the spec. I found no path in the tree that reaches it. In the 87 AC6 block (selftest.py:3176-3185), us87.read_steps comes next, then steps.derive_contained_rel(...). That is a pure normaliser at upgrade_steps.py:1059, and it is not in the finder's load_govkit list. Then comes `gk72 = govkit_module()` at selftest.py:3197, which under S1 rebinds the table before steps.check_contained or the other step calls run. `steps` is bound to govkit_module().upgrade_steps (selftest.py:3093, 3569). Built as written, behaviour is unchanged, and the defect is confined to the completeness of a spec's prose section. That makes it low, not medium. | sound | - |
| 5 | failure-envelope | memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-99.md:section 2 S2 and section 4 "The arm" check 3 | low | low | confirmed | Re-probed. selftest.py:9764 does read `spec = importlib.util.spec_from_file_location("govkit_mod", GOVKIT)` and then exec_module, so it builds a second engine object that never goes through govkit_module(). Spec-99 S2 (blob line 32) and section 1 (line 22) still say 'every other reader of the engine ... routes through govkit_module()'. The S2 inventory table lists only the nine import sites. Check 3 (line 140) grades only Import and ImportFrom nodes, and AC3's grep matches only `import`/`from govkit` lines, so 9764 passes both. The spec knows this load exists: section 4 'The held engine' (lines 120-121) names it as a by-path load that will reuse the real step module. But it never carves it out of S2's 'every other reader' claim, so the scope wording overstates what the arm certifies. Nothing behaves differently: 9764 reads only LANDABLE_ROLES/ROLE_KINDS/KIND_MARKS, and after S1 it gets the held upgrade_steps. So this is a wording-only defect, graded low. | unsound | - |
