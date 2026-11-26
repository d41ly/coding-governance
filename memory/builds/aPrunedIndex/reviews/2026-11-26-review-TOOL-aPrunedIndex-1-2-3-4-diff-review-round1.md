**Serves:** diff-review TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4

# aPrunedIndex — diff review of units 1 to 4, round 1

*2026-11-26. A Tier-2 adversarial pass over the build's landed code. Roles: finders gov-diff-reviewer,
skeptic batches gov-skeptic, synthesis gov-synthesizer.*

Reviewed: 3d6c1702afb6c2e86638785950d80657a187192c...d5288a92d559cedf8b867c683190b3d74b8467ba

Round: 1

## Verdict: CLEAN WITH FIXES

No blocker stands. By item: 0 blocker, 1 high, 0 medium, 4 low, 5 in all. By raw confirmed finding:
0 blocker, 1 high, 2 medium, 4 low, 7 in all. The high item merges ids 1, 4 and 7, so its two medium
findings count as medium raw and as part of one high item. No finding contests the verdicts or output
of `check`, the SQL indexes, the sweep's choice of rows or the gc skip. The high item is a closure
defect: unit 4 and the build are marked CLOSED while AC8 is still owed, so the `tags bundle selftest`
budget row is stale. The four low items are a README cost claim, a lambda-bound helper name the naming
leg cannot see, a refusal rule with no arm that fails, and a spec revision that was never audited.

The review shape is intensity full, raw 8, confirmed 7, refuted 1, merged 0, unverified 0
(0 uncertain), precision 0.88.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 0 | 1 | 0 | 0 | 0 | 0.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses: 5/5 returned, 0 died. Skeptic batches: 4/4 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to
  unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded,
  0 duplicates.
- Fixes on confirmed findings: 5 judged sound, 0 unsound, 2 instance-only, 0 none proposed, 0 not
  judged. An instance-only fix cures the cited instance and leaves its class standing. Where a fix is
  instance-only, the skeptic's class-level fix is the fix written below.
- Severity: 0 ungraded by the skeptic, 0 re-graded by the skeptic. Every binding grade is kept here.
- Unverified: 0 answered uncertain, 0 with no usable verdict.
- Refuted findings shown: 1. Same-address pairs shown: 0. Refuted id 2 (an orphan worktree's all-zero
  HEAD makes `--gc` refuse) shares tools/playbook/tag_index.py@4d1a9ef3:960 with confirmed id 6, but it is a different defect:
  id 2 claims the behaviour is wrong, and id 6 says the behaviour is right but no arm guards it. No twin
  is flagged.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intent: 4 spec documents supplied as `specs`, beside the range's commit messages. By design: the
  caller's byDesign.
- Checklist: 16 items, each assigned to exactly one of 5 lenses: security 4, correctness 3, seams 3,
  verification 3, intent 3.
- Dispositions: unclassed refuse, 16 class slugs handed, 226 leg names read from tools/gate-legs.json.
- Every lens and every skeptic batch returned, so this run is complete.

## HIGH

### H1 — unit 4 closed with AC8 owed, so the `tags bundle selftest` budget is stale (ids 1, 4 and 7)

**Grades:** id 7 HIGH, id 1 MEDIUM, id 4 MEDIUM. All are binding. Ids 1 and 4 describe the stale
budget row, whose effect is contained to the selftest cost verdict. Id 7 adds that the CLOSED status
claims a criterion nothing shows was met, which will mislead the next change.

- **Where:** `memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md@fa73c993:51` (S8;
  AC8 at line 267). `tools/run-gates/selftest-budgets.txt@4d739a1b:146`.
  `tools/playbook/tag_bundle.py@8a284c47:383` (the plants at lines 383-387).
- **Wrong:** the diff adds five plants to `SELFTEST_ROWS`: dead-versions, named-probe, released-rows,
  released-cost and gc-predates. `run_selftest` runs each one in turn as its own `--fixture` scratch
  repository, inside the `tags bundle selftest` leg. Spec 4 S8 and AC8 require that leg's budget row and
  ceiling-evidence row to be rewritten from a timing taken with the five plants in place. No commit in
  the range touches `tools/run-gates/`. The budget row still reads `tags bundle selftest	60`, from a
  22 s reading at 51cd8b402, and `ceiling-evidence.txt` has no `tags bundle` row. The unit-4 ledger says
  `AC8 — owed at the close`, but spec line 3 and the build README both say CLOSED.
- **Consequence:** the ledgers time released-rows at 49 s and gc-predates at 46 s. With the old 22 s,
  the leg needs at least about 117 s against a 60 s budget. `run-selftests.sh --serial` grades each
  suite against its budget and goes RED on OVER BUDGET (lines 257 and 307). The next serial run will
  blame that breach on whatever change triggers it. The leg's 300 s ceiling has never been checked with
  the five plants in it. The bar's verdict on the code is not wrong.
- **Fix (sound):** time `python tools/playbook/tag_bundle.py --selftest` alone once on a quiet box at
  the tip. Write that worst reading x1.5, floored at 60, into `selftest-budgets.txt:146`, naming the
  reading and the sha. Run `derive-ceilings.py --write` so the evidence row and the `gate-legs.json`
  ceiling are re-graded. If the reading comes near 300 s, raise the ceiling or split the leg. Record
  the reading in the unit-4 ledger's AC8. Until then, set unit 4 and the build back from CLOSED to a
  status that shows AC8 is owed. The probe to pass: `bash tools/run-gates/run-selftests.sh --serial
  --kit tools/playbook` must not report OVER BUDGET for `tags bundle selftest`.
- **Left shift:** checklist class `budget-row-not-remeasured-after-added-arms`. Add a gate: a diff that
  adds a row to a selftest's arm table must also change that suite's budget row, or the leg reds.
  Separately, the build index should refuse CLOSED on a unit whose ledger still lists an AC as owed.

## LOW

### L1 — the README says the release sweep costs one seek per pair; it scans `dirty_path` (id 3, LOW)

- **Where:** `tools/playbook/README.md@72f63c58:340`; the code at
  `tools/playbook/tag_index.py@4d1a9ef3:879` (lines 879-884).
- **Wrong:** the README says a build clears released rows with "one seek per released pair".
  `dirty_path` is keyed on (worktree, path), per `SCHEMA` at tools/playbook/tag_index.py@4d1a9ef3:115. The two `EXISTS` clauses
  in `remove_released_rows` filter on `d.path`/`d.blob` and on `d.blob` with no worktree, so no index
  serves them. EXPLAIN QUERY PLAN prints `SCAN d` for both. Each pair that no tree holds therefore scans
  all of `dirty_path`. The code's own ponytail comment at lines 877-878 states this ceiling, so the code
  and the README disagree.
- **Consequence:** behaviour is unaffected. The tree `EXISTS` runs first and short-circuits for
  unchanged files, and `dirty_path` holds only uncommitted edits. On the node's shared index, where
  100+ worktrees write dirty rows, the documented cost is wrong, and the next change will rely on it.
  The released-cost plant pads only `path_row`, `blob_row` and `blob_parsed`, so it never sees this.
- **Fix (sound):** either reword the README to match the ponytail ceiling (one seek per pair against
  the trees, plus a scan of the dirty rows for each pair no tree holds), or add
  `CREATE INDEX IF NOT EXISTS dirty_path_blob ON dirty_path(blob)` to `SCHEMA` so both `EXISTS` seek. If
  you add the index, pad `dirty_path` in the released-cost plant with rows for other worktrees, assert
  the window's steps stay within 2x, and see that arm red with the index removed.
- **Left shift:** checklist class `observed-by-claim-no-arm-discharges`. A cost sentence in a README
  names the plant that measures it, or it is written as a ceiling.

### L2 — a lambda-bound helper escapes the naming leg (id 5, LOW)

- **Where:** `tools/playbook/gov_tag.py@c22d4773:1365`.
- **Wrong:** `commit_texts = lambda files: write_commit(...)` names a helper whose leading word
  `commit` is not in the `.lexicon.conf` VERBS table. `lexicon.py` `_python_defs` (lines 483-495)
  grades only `ast.FunctionDef` and `AsyncFunctionDef` names, so the lexicon leg never sees a name bound
  to a lambda. Commit 9750a135f renamed seven nested defs in these same plants and left this one.
- **Consequence:** behaviour is unaffected. A `def commit_texts` would be refused, while the same name
  bound to a lambda passes, so the naming gate certifies names it never read.
- **Fix (instance-only; the skeptic's class-level fix):** make `_python_defs` also grade `ast.Assign`
  targets whose value is an `ast.Lambda`, and `AnnAssign` likewise. Then drain or pin the offenders that
  surfaces. The finder's proposal, renaming it with a declared verb (for example `write_commit_texts`)
  or making it a `def`, plus a checklist note, cures this instance alone.
- **Left shift:** checklist class `naming-leg-grades-what-python-named`; the class-level fix above is
  its gate, in the `lexicon naming predicates` leg.

### L3 — no arm makes the HEAD probe's git call fail (id 6, LOW)

- **Where:** `tools/playbook/tag_index.py@4d1a9ef3:960` (the rule at lines 957-960); the plant
  `gc-predates` in `tools/playbook/gov_tag.py@c22d4773` (lines 1045-1132).
- **Wrong:** the comment says a git failure refuses and is never read as absence. `read_live_versions`
  refuses when `git ls-tree <head> -- <registry>` fails, and a second `read_git` probes the conf at
  HEAD. No step of `gc-predates` makes either `read_git` fail. Step 2 deletes a registry on disk but
  HEAD still holds it, so the refusal comes from `read_namespaces`. Steps 4, 5 and 6 reach a skip or a
  refusal through a HEAD that `ls-tree` reads cleanly.
- **Consequence:** a later edit that wraps that `read_git` in `except TagError: skip` keeps
  `gc-predates` green. `--gc` would then collect the rows of a live worktree it could not read. The loss
  is limited to rebuildable index rows.
- **Fix (instance-only; the skeptic's class-level fix):** add two staged steps with an unreadable HEAD
  object. Both assert that `--gc` refuses naming the worktree and that row counts do not change, and
  each is seen red under a staged `except TagError: skip`. In the first, the registry is absent on disk,
  so the registry probe's `read_git` fails. In the second, the registry is present and the conf is
  absent on disk, so the conf probe's `read_git` (the `not conf_path.is_file()` branch) fails. The
  finder's proposal, one step for the registry probe alone, cures the cited instance and leaves the conf
  probe unguarded.
- **Left shift:** checklist class `rule-stated-with-no-check-that-fails`. Every refusal branch a comment
  names gets an arm seen red under a staged swallow.

### L4 — spec 4 closed at rev-4 with its last audit at rev-1 (id 8, LOW)

- **Where:** `memory/builds/aPrunedIndex/README.md@9fd4bb67:82`.
- **Wrong:** the generated build index prints `Ids whose spec moved past its audited revision:
  TOOL-aPrunedIndex-4@rev-1`. Revisions 2 to 4 added the conf refusal (S2's conf cases, plant step 6,
  AC7) and AC9. The only audit after rev-1, `2026-11-26-review-TOOL-aPrunedIndex-1-2-3-spec-audit-round1`,
  leaves unit 4 out by name. The unit is still marked CLOSED.
- **Consequence:** the conf-refusal contract unit 4 built was never audited as written. The effect stays
  in the records and in how far the unit's statement of intent can be trusted.
- **Fix (sound):** run a spec audit that covers TOOL-aPrunedIndex-4 at rev-4, or record the owner's
  waiver, so the generated line clears before the unit stays CLOSED.
- **Left shift:** new class `closed-over-an-unaudited-spec-revision`. The build index refuses CLOSED on
  an id it lists as moved past its audited revision, unless a waiver is recorded.

review-shape kind=diff-review round=1 intensity=full at=synth raw=8 confirmed=7 refuted=1 merged=0 unverified=0 blocker=0 high=1 medium=2 low=4 agents=10 out-tokens=91232 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=1 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/playbook/tag_bundle.py@8a284c47:383 | medium | medium | confirmed | tools/playbook/tag_bundle.py@8a284c47:383-387 adds five plants (dead-versions, named-probe, released-rows, released-cost, gc-predates) to SELFTEST_ROWS. The budget row is unchanged: selftest-budgets.txt:146 still reads `tags bundle selftest	60`, measured at 51cd8b402 at 22 s. The TOOL-aPrunedIndex-4 ledger times gc-predates alone at 46 s (AC1), and its AC8 lists that timing, the budget row and `derive-ceilings.py --write` as owed at the close. The build README marks the build and all four units CLOSED, but no commit in the range updates the budget. In the diff, gate-legs.json changes only the leg's purpose string. run-selftests.sh documents --serial as grading each suite against its own budget and going RED on a breach. With 22 s for the old rows plus 46 s for one new plant, that run reds on cost. The effect is limited to the selftest budget grading. | sound | budget-row-not-remeasured-after-added-arms | class:budget-row-not-remeasured-after-added-arms |
| 2 | correctness | tools/playbook/tag_index.py@4d1a9ef3:960:960 | medium | - | refuted | The probe holds: an orphan worktree is listed as `HEAD 0000…0`, and `git ls-tree` on that sha exits 128 with `fatal: not a tree object`. I reproduced both on git 2.56.1. But this is the specified behaviour, not a deviation. Spec 4, in the passage after step 5, says: `git ls-tree` "fails on the all-zero sha of an unborn branch and on the empty string; both were run on 2026-11-25. A failure is a `TagError` inside the `try`, so it refuses as S2 says, and a git failure is never read as absence." S2 also lists "a HEAD git cannot read" among the cases that refuse. The finder's claim that spec 4 says to skip this worktree misreads the spec. The base refused this worktree too: read_namespaces on a missing registry raised TagError. So the diff made nothing newly reachable. | unsound | - | - |
| 3 | seams | tools/playbook/README.md:340 | low | low | confirmed | tools/playbook/README.md around line 340 says a build clears released rows with "one seek per released pair". The code does not do that. dirty_path's key is (worktree, path), per SCHEMA at tools/playbook/tag_index.py@4d1a9ef3:115. remove_released_rows' EXISTS at lines 880 and 884 filter on d.path/d.blob and on d.blob with no worktree, so no index serves them, and each one scans dirty_path for every pair no tree holds. The code's own ponytail comment at lines 877-878 states this ceiling, so the code and the README disagree. Both the README sentence and remove_released_rows are new in this diff. Behaviour is unaffected because the tree EXISTS short-circuits first, and dirty_path holds only uncommitted edits. The wrong claim is in prose, so the grade is low. | sound | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 4 | verification | tools/run-gates/selftest-budgets.txt:146 | medium | medium | confirmed | The diff adds five rows to SELFTEST_ROWS: dead-versions, named-probe, released-rows, released-cost and gc-predates. run_selftest runs each plant in its own subprocess, one after another, inside the `tags bundle selftest` leg (gate-legs.json, ceiling 300). The diff does not touch tools/run-gates/. selftest-budgets.txt:146 still budgets 60 s, from a 22 s reading at 51cd8b402. The ledgers pin released-rows at 49 s (unit 3 AC1) and gc-predates at 46 s (unit 4 AC1), so these two plants alone already exceed 60 s. Per run-selftests.sh lines 257 and 307, a serial run therefore grades the leg OVER BUDGET, RED. The unit 4-1 acceptance ledger line 18 still lists AC8 as 'owed at the close'. The contained effect is that the cost verdict goes red and the 300 s ceiling is unverified. The bar's result is not wrong. | sound | - | class:budget-row-not-remeasured-after-added-arms |
| 5 | verification | tools/playbook/gov_tag.py@c22d4773:1365 | low | low | confirmed | At tools/playbook/gov_tag.py@c22d4773:1365 the line is `commit_texts = lambda files: write_commit(...)`. It is new in this range: grep of the base file finds no commit_texts. The .lexicon.conf VERBS table (line 736 onward) lists build, load, read, write, ... add, remove, set, print, main, cmd, test. `commit` is not among them. lexicon.py _python_defs (lines 483-495) collects only ast.FunctionDef and AsyncFunctionDef names, so a lambda bound by assignment is never graded. Commit 9750a135f renamed seven nested defs in these same plants and left this name. Behaviour is unaffected, so the grade is low. | instance | naming-leg-grades-what-python-named | class:naming-leg-grades-what-python-named |
| 6 | verification | tools/playbook/tag_index.py@4d1a9ef3:960 | low | low | confirmed | tools/playbook/tag_index.py@4d1a9ef3:957-960 is new in unit 4. It refuses on a read_git failure of `ls-tree <head> -- <registry>`, and a second read_git probes the conf at HEAD. I read every step of the gc-predates plant (tools/playbook/gov_tag.py@c22d4773:1045-1132), and none makes read_git fail. Step 2 deletes wt4's registry on disk, but its HEAD still holds it: ls-tree succeeds and the refusal comes from read_namespaces. Step 4's skip reads a HEAD that ls-tree reads cleanly. Step 5 refuses on a missing kit, and step 6 on conf breaks whose HEAD ls-tree succeeds. So a wrapper that swallows a git failure as absence would stay green. The gap is real and contained to a regression guard over rebuildable rows, so the grade is low. | instance | - | class:rule-stated-with-no-check-that-fails |
| 7 | intent | memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-4.md:51 | high | high | confirmed | `git log 3d6c1702a..d5288a92d -- tools/run-gates/` prints nothing. selftest-budgets.txt:146 still reads `tags bundle selftest	60` from the 22 s reading at 51cd8b402, and ceiling-evidence.txt has no `tags bundle` row. Spec 4 S8 (lines 51-53) and AC8 (lines 267-271) require both rows to be rewritten from a timing taken with the five plants in place. Those plants are SELFTEST_ROWS 383-387 in tag_bundle.py. The unit-4 ledger (line 18) says `AC8 — owed at the close`, but spec line 3 and README line 65 say CLOSED. The build's own ledgers time released-rows at 49 s and gc-predates at 46 s, so the 60 s row is clearly stale. run-selftests.sh --serial is RED on a breach (usage text, and the OVER BUDGET lines 2380/2426), so the next serial run will blame whatever change triggers it. That misleads the next change, and the CLOSED status claims a criterion that nothing shows was met. | sound | criterion-asserts-what-its-own-command-cannot-show | class:budget-row-not-remeasured-after-added-arms |
| 8 | intent | memory/builds/aPrunedIndex/README.md:82 | low | low | confirmed | memory/builds/aPrunedIndex/README.md:74 prints `Ids whose spec moved past its audited revision: TOOL-aPrunedIndex-4@rev-1.` The reviews folder holds only `...-1-2-3-4-spec-audit-round1` (its findings were folded at rev-2) and `2026-11-26-...-1-2-3-spec-audit-round1`, whose name leaves out unit 4. So rev-2 to rev-4 of spec 4 were never audited, including the conf refusal and AC9. Spec line 3 and README line 65 still show the unit CLOSED. The effect stays in the records, so it is low. | sound | - | new:closed-over-an-unaudited-spec-revision |
