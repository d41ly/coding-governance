**Serves:** diff-review TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 TOOL-aFrugalTurnstile-11 DEPL-aFrugalTurnstile-1 PLAY-aFrugalTurnstile-1

# aFrugalTurnstile: Tier-2 closing diff review, round 1

*Node `a`, 2026-10-10. This was an adversarial pass over the build's whole cumulative diff. Five primed finder lenses ran, then a skeptic stage prompted to REFUTE each finding, then one synthesis. The build makes landing through gov's push boundary cheaper. It adds first-parent staleness, bar-green records with tree covers, scoped adoption, lineage reuse, a host-wide turnstile, a detached post-merge bar, and a `--decide` path for the unattended close.*

Reviewed range: d006cfc569f22e9f893ae9b57998b47a8bda6c1b...61e5103c8c2171d44fdc8a8044cfb0dde0a8f910 (origin/main d006cfc5, merged into the branch at 3f0059249, so the diff is exactly this build). ROUND: 1.

## Verdict: CLEAN WITH FIXES

There are no blockers. Five raw confirmed findings are high, grouped into four items. Each one is a path where a smaller run, or a cleared red, rests on evidence that does not cover the pushed tip. They are all narrow paths, but they are exactly the class this build's safety argument says it cannot have, so fix them before landing. Nine medium and three low findings follow. The checklist sweep did not run (see Run integrity), so this verdict does not say the project's recurring bug classes are absent from the diff.

## Review shape

Intensity full, raw 17, confirmed 17, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| seams | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| intent | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 0 blocker, 4 high, 5 medium, 3 low (12 items). Counted by raw confirmed finding: 0 blocker, 5 high (ids 1, 2, 6, 8, 15), 9 medium (ids 3, 4, 5, 7, 9, 12, 13, 16, 17), 3 low (ids 10, 11, 14), 17 in total.

## Run integrity

- Lenses: 5 of 5 returned, 0 died. Skeptic batches: 5 of 5 returned, 0 died.
- No contradictory verdicts were demoted to unverified. No spurious verdicts were discarded, and there were no duplicates.
- Fixes on confirmed findings: 15 judged sound, 2 judged UNSOUND (ids 10 and 13; the skeptic's corrected fix is written below), 0 with no proposal, 0 not judged.
- Severity: 0 findings left ungraded by the skeptic, 1 re-graded by the skeptic (id 15, from blocker to high).
- Unverified findings: none. No skeptic answered UNCERTAIN, and none lacked a usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 2 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: NONE swept, because none exists. A zero count here is not evidence that the project's recurring bug classes are absent.
- By design: the caller's byDesign.
- Every lens and every skeptic batch returned, so in that sense the run is complete. The missing checklist sweep is the one gap in coverage.

## HIGH

### H1: the close's bar records a trusted green without scrubbing the bar's knobs (ids 1, 6)

- **Where:** `tools/unattended/unattended.sh:10656` (also 10654, the primary arm, and the writer at 10704).
- **Defect:** the gates-green arms inherit `GATE_LEGS`, `GATE_REUSE` and `GATE_DOCS_BASE` from the driver's environment. `write_bar_green` then records the rc-0 result as a `kind full` or `kind scoped` gate-bar-green. It stores neither the manifest nor the reuse mode. For a bar record, `check_cover_record` compares only the tree, the bar string and selftests, so a subset green covers a later push of that tree with no bar run. The hook scrubs these knobs for its own bar (`BAR_SCRUBBED_KNOBS`, `unset GATE_DOCS_BASE`), and so does post-merge.sh (`PM_SCRUB`). Only the driver's writer is missing the scrub.
- **Fix (skeptic judged it SOUND):** run every gates-green arm under `env -u GATE_LEGS -u GATE_REUSE -u GATE_DOCS_BASE -u GATE_SPAWN_CMD -u GATE_SPAWN_FLOOR -u GATE_VERDICT_FAULT`, which is the hook's scrub list plus the docs knob. The alternative is to have `write_bar_green` decline whenever any of those was set.
- **Left-shift gate:** a parity arm that extracts the hook's `BAR_SCRUBBED_KNOBS` and asserts that every bar-writing path in unattended.sh and post-merge.sh unsets the same set. Also add an arm that exports `GATE_LEGS=<subset>`, runs gates-green, and asserts that no gate-bar-green is written, or that the landing push still runs a bar.

### H2: the close acts on a `--decide` answer computed for a different bar (id 2)

- **Where:** `tools/unattended/unattended.sh:10628`.
- **Defect:** `--decide` decides for the hook's bar, `${GOV_GATE_CMD:-bash $GATE_RUNNER}`. The driver then skips the run (`covered`), or scopes it, for its own `$GATE_CMD` and never checks that the two are the same. Take an adopter with a wrapper `GATE_CMD` and no `GOV_GATE_CMD` (the design names nc). For them gates-green reports met on a tree where the declared bar never ran.
- **Fix (skeptic judged it SOUND):** honour a `--decide` answer only when the hook's vetted bar equals `$GATE_CMD` byte for byte. Either `--decide` prints the bar it decided for, or the driver compares against `bash <runner>` or the `GOV_GATE_CMD` read at R. Otherwise fall back to `GATE_FULL=1` and print one announcing line.
- **Left-shift gate:** an FT9-style arm with `GATE_CMD` set to a wrapper and `GOV_GATE_CMD` unset, under a declared `GATE_POST_MERGE`, on a tree that holds a runner stamp. Assert that the wrapper actually ran, or that the fallback line was printed.

### H3: lineage-qualified ledger rows are written by a run whose tree moved (id 8)

- **Where:** `tools/run-gates/run-gates.sh:3793`.
- **Defect:** the ledger block sets `lfull=1` from `GATE_FULL` and `TREE_CLEAN` only. `tree_moved` is not computed until 3962. A FULL run whose tree moved mid-bar therefore still writes `ok` rows with `full=1`, and their keys can describe content other than what the leg graded. A later `GATE_REUSE=lineage` run reuses them, and because `reuses == lineage_reuses` it stamps `gate-full-green` (4047).
- **Fix (skeptic judged it SOUND):** compute `FPRINT_END` and `tree_moved` before the ledger block and add `[ "$tree_moved" = no ]` to the `lfull` condition. The alternative is to blank `_full` on rows from a run whose verdict is not GREEN, or whose verdict is TREE_MOVED.
- **Left-shift gate:** a run-gates evidence arm in which a leg modifies a tracked file mid-bar under `GATE_FULL=1`. Assert that no ledger row carries `full=1`, and that a following `GATE_REUSE=lineage` run neither reuses those rows nor stamps gate-full-green.

### H4: a post-merge red is cleared by a scoped green (id 15)

- **Where:** `.githooks/pre-push:1922`.
- **Defect:** `check_post_merge_red` clears the red whenever `_pm_x` strictly descends from it. `_pm_x` is `rec_sha`, or `bg_sha` for a cover, and either can be a `kind scoped` record's own sha. Here is how that happens on an ordinary path. A scoped record written inside the post-merge window, before `refs/gov/bar-red` exists, descends from the red. The next push adopts that record and the red reads as cleared, so the full bar that went red never runs again. Design D8, AGENTS.md:112, the charter and WIRE-INTO-PROJECT.md:792 all say a FULL green must descend from the red.
- **Grade:** the finder graded this blocker and the skeptic re-graded it high. It is reachable only where an adopter declares `GATE_POST_MERGE`, and gov declares none. The binding grade is high.
- **Fix (skeptic judged it SOUND):** pass the full green the decision rests on, not the adopted sha. Use `_pm_x=$scoped_full` on the adopted path. For a cover, use the covering record's `base` when its kind is scoped, and its sha only when its kind is full. The alternative is to make `check_post_merge_red` refuse to clear on a kind-scoped record. Either way, add a revision line to the design record, because TOOL-7 S3 loosened D8 without one.
- **Left-shift gate:** a pre-push.test.sh arm that stages `refs/gov/bar-red` at X and a `kind scoped` record at a descendant of X whose base is older than X. Assert that the push goes FULL and that no "cleared" line is printed. Add the same arm for the cover path.

## MEDIUM

### M1: the same red-clearing defect, graded by the security lens (id 3)

- **Where:** `.githooks/pre-push:1922`.
- **Defect:** this is the same code path as H4. Any adopted or covering green that strictly descends from the red clears it, including a scoped one.
- **Grade:** the binding grade is medium. On the merits I would grade it high to match id 15, since the consequence is identical. The skeptic's medium rests on the next post-merge red re-binding, which limits the damage. It stays medium as bound, and fixing H4 closes it.
- **Fix (skeptic judged it SOUND):** clear only on a full descendant: a runner stamp, a `kind full` bar record, or the scoped record's own `scoped_full` when that strictly descends from the red. Otherwise force FULL. The alternative is to rewrite the D8 and WIRE text to the looser rule on purpose.
- **Left-shift gate:** the H4 arm.

### M2: the hook's and the driver's scoped-record writers disagree on `base` (ids 4, 7, 9, 12, 16)

- **Where:** `.githooks/pre-push:1964` (`--decide` prints `scoped $scoped_base`), `tools/unattended/unattended.sh:10635` and `:10636` (parsing), and `tools/unattended/unattended.sh:10704` (the write).
- **Defect:** when the decision adopts a `kind scoped` record M whose base is B, `--decide` prints M. The driver then writes `kind scoped base M`. The hook's own writer writes `scoped_full=B` (2162, TOOL-11 S6b). `check_bar_base` refuses a base that is not a full green, so the close's record can never be adopted. It also overwrites M's adoptable record in `gate-bar-green.scoped` and `.scoped.shared`. The landing push then falls back to an older full slot or to FULL. That is the FULL/scoped alternation TOOL-11 removed from the hook. Only cost is affected, never a verdict. Five findings across four lenses reported it. The AC8 parity arm compares only key names (`cut -f1`), so it reads as proof that the two writers agree when it is not.
- **Fix (skeptic judged it SOUND for all five):** have `--decide` print both shas, as `scoped <scoped_base> <scoped_full>`. The close exports `GATE_BASE` from the first and writes the record's `base` from the second. The alternative is for the driver to resolve the adopted record's full base before writing.
- **Left-shift gate:** extend the AC8 parity arm so both writers are called with kind scoped and a non-empty base, and compare whole records rather than `cut -f1`. Add an FT9 arm whose decision adopts a scoped record, and assert that the next push adopts the close's record.

### M3: post-merge.sh records a full green without checking that the worktree is clean (id 5)

- **Where:** `tools/run-gates/post-merge.sh:340` (the writer at 332-341, called at 388).
- **Defect:** after a GREEN verdict it writes `kind full` keyed on `$SHA^{tree}` into the common dir's `.shared` slot without a `git status` check. A wrapper bar is judged on rc and HEAD alone, so if it rewrites tracked files, a full green is still recorded for the pristine tree. The hook's writer and the driver's writer both refuse on a dirty tree.
- **Fix (skeptic judged it SOUND):** before writing, require `git -C "$WT" status --porcelain --ignore-submodules=untracked` to be empty. Otherwise print one line and write nothing.
- **Left-shift gate:** a post-merge arm with a wrapper bar that edits a tracked file and exits 0. Assert that no gate-bar-green.shared is written. Better still, a grep gate asserting that every `write_bar_green` definition carries the porcelain precondition.

### M4: no test reaches the cover pass's refusals of a runner stamp (id 13)

- **Where:** `.githooks/pre-push:1873`.
- **Defect:** no arm reaches the fingerprint-mismatch, foreign-manifest or manifest-blob-mismatch refusals. If the check were deleted, a gate-full-green earned on a wrapper's subset manifest would cover a push under the full runner bar, and every suite would stay green.
- **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** in the AC9 fixture, push with each altered stamp: a manifest naming another path, a different manifest_blob, and a different fingerprint. For each, assert that the marker grows by one and that no "covered on main push" line appears. To also assert the specific reason, first plant a gate-bar-green record that does not cover (for example bar `bash other-bar.sh`), so `_cov_bars` is set and the "not covered" line prints. Then grep that line for `graded tree fingerprint`, `leg manifest blob`, or the manifest reason. Keep the unaltered stamp as the control.
- **Left-shift gate:** the arms above. Each refusal message string should have a suite that greps for it.

### M5: the protocol row puts `GATE_POST_MERGE` in the wrong file (id 17)

- **Where:** `memory/guides/UNATTENDED-PROTOCOL.md:517`, and the same text in `tools/unattended/PROTOCOL.template.md:517`.
- **Defect:** the row says `GATE_POST_MERGE` is read from the file `GATE_POLICY_FILE` names. In fact `read_gate_policy`, push-main.sh and design D11 all read it from `.githooks/gate-env.sh` at R, and the protocol's own line 440 says so too. An adopter who follows the row silently loses the scoped landing and the post-merge bar. That fails safe, but it fails silently.
- **Fix (skeptic judged it SOUND):** change the row to say that `INHERITED_RED` and its age bound are read from this file, and that `GATE_POST_MERGE` is always read from the pre-push hook's `.githooks/gate-env.sh` at R. Make the same edit in the template.
- **Left-shift gate:** a doc-parity check that every key the protocol says is read from `GATE_POLICY_FILE` is actually read from the conf path by `read_gate_policy`.

## LOW

### L1: a scoped record over an inherited green can never be adopted (id 10)

- **Where:** `.githooks/pre-push:2162`.
- **Defect:** when an inherited green was adopted, `scoped_full=inh_sha`. `check_bar_base` never reads `gate-inherited-green`, so the record serves only as an exact-tree cover. The comment at 1747-1753 says the record names "the FULL green that base rests on", which this one does not.
- **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** have the hook writer decline the scoped record when `inh_sha` was adopted. Also make `--decide` show that the scoped base is an inherited green, for example by printing no full base, so the driver's write at unattended.sh:10704 declines too. The alternative is to keep these records as exact-tree covers and correct only the comment.
- **Left-shift gate:** an arm that pushes scoped from an inherited green and asserts no scoped record is written, or that the comment-pinned contract holds.

### L2: the driver rejects SHA-256 bases (id 11)

- **Where:** `tools/unattended/unattended.sh:10636`.
- **Defect:** the driver accepts only a 40-hex base, while the hook accepts 40 or 64. In a SHA-256 repository every scoped answer falls back to `GATE_FULL=1`. Only cost is affected.
- **Fix (skeptic judged it SOUND):** accept 40 or 64 hex digits, using the hook's `case "${#x}:$x"` shape.
- **Left-shift gate:** one shared sha-shape helper in both scripts, or a parity arm over both validators.

### L3: two post-merge.sh guards have no arm (id 14)

- **Where:** `tools/run-gates/post-merge.sh:313` (also 307).
- **Defect:** no arm reaches the guard that turns a default runner's exit 0 without a GREEN verdict into RED, or the guard that refuses when the worktree's HEAD moved.
- **Fix (skeptic judged it SOUND):** add a fixture runner that exits 0 and writes verdict RED, with `refs/gov/bar-red` staged at an ancestor. Assert exit 1, the ref kept, and no gate-bar-green.shared. Add a bar that moves the worktree's HEAD and assert exit 2 with REFUSED.
- **Left-shift gate:** those two arms.

review-shape kind=diff-review round=1 intensity=full at=synth raw=17 confirmed=17 refuted=0 unverified=0 blocker=0 high=5 medium=9 low=3 agents=11 out-tokens=23462

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/unattended/unattended.sh:10656 | high | high | confirmed | The driver's gates-green arms run `env -u GATE_WALL [GATE_FULL=1\|GATE_BASE=..] ... $GATE_CMD` and inherit the rest of the driver's environment. unattended.sh contains no scrub of GATE_LEGS or GATE_REUSE (grep finds no hit). The runner honours GATE_LEGS (run-gates.sh:227) and GATE_REUSE (2019). It honours GATE_DOCS_BASE only when GATE_FULL is unset, i.e. on the scoped arm. On rc 0, write_bar_green (10483-10516) records kind full or scoped and stores neither the manifest nor the reuse mode. check_cover_record for a bar record compares only tree, bar string and selftests, and check_bar_base accepts a kind-full bar record as a base. The hook's gate string defaults to `bash $GATE_RUNNER`, which can match the driver's GATE_CMD byte for byte, so a subset green covers the landing. The hook scrubs exactly these knobs for its own bar (BAR_SCRUBBED_KNOBS, unset GATE_DOCS_BASE), but its record writer does not reach the driver's. The trusted record is new in this diff. The path needs a knob exported in the driver's shell, which makes it narrow, hence high. | sound | - |
| 2 | security | tools/unattended/unattended.sh:10628 | high | high | confirmed | The hook decides for `gate=${GOV_GATE_CMD:-bash $GATE_RUNNER}` (pre-push:1603). The driver parses the --decide line and, on `covered`, sets _grc=0 without running $GATE_CMD (unattended.sh ~10655). Nothing compares the hook's bar with the driver's GATE_CMD. On `scoped` it hands $GATE_CMD a GATE_BASE that may be another bar's green. Design D9/D11 intend the close's bar and the landing decision to be one computation. The design names an adopter, nc, with GATE_CMD=`bash scripts/unattended-bar.sh`, so a wrapper close bar differing from the hook's bar is a real configuration. In that case gates-green reports met on a tree where the declared bar never ran. That is a check certifying what it did not check, on a narrow configuration (GATE_POST_MERGE declared plus a mismatched bar), hence high. | sound | - |
| 3 | security | .githooks/pre-push:1922 | medium | medium | confirmed | check_post_merge_red clears whenever the adopted sha _pm_x strictly descends from PM_RED. _pm_x is rec_sha, inh_sha or the covering bg_sha (pre-push ~1922), and rec_sha/bg_sha can be a kind-scoped bar record. Design D8 says 'the adopted full green's sha descends from it'. AGENTS.md:112, the charter template and WIRE-INTO-PROJECT.md:792 all promise 'until a full green descends from it'. A scoped record graded after R1 landed but before the post-merge red was published descends from R1 and clears it, while its full base does not, so a scoped run can skip the failing leg. The TOOL-7 unit spec uses the looser 'adopted green' wording, but the design and the shipped text say full. The next red re-binds, so the effect is contained: medium. | sound | - |
| 4 | security | .githooks/pre-push:1964 | medium | medium | confirmed | --decide prints `scoped $scoped_base` (pre-push:1964). When a kind-scoped record is adopted, resolve_scoped_base sets scoped_base=rec_sha (the scoped sha) and scoped_full=rec_base. The driver takes _gbase from that line and passes it to write_bar_green as base. The hook's own writer passes `_bg_base=$scoped_full` (~2162), with a comment that a scoped base is what check_bar_base refuses (the TOOL-11 bug). The driver's record therefore names a scoped sha as base, and check_bar_record/check_bar_base refuses it at the landing push, which falls back to an older candidate or FULL. The failure is only extra cost in the safe direction, and it is a real writer divergence: medium. | sound | - |
| 5 | security | tools/run-gates/post-merge.sh:340 | medium | medium | confirmed | Confirmed. post-merge.sh line 388 calls write_bar_green whenever PM_VERDICT is GREEN, and write_bar_green (332-341) writes `kind full`, keyed on $SHA^{tree}, into $CDIR/gate-bar-green.shared with no `git status` check. The hook's writer and the driver's writer both refuse on `git status --porcelain --ignore-submodules=untracked` being non-empty. For the default runner, a moved tree already turns the verdict into TREE MOVED, so it never reads GREEN. For a wrapper bar, run_bar judges on rc and HEAD alone, so if the bar edits tracked files in the scratch worktree, a full green is still recorded for the pristine tree. The cover pass then reads that record from the shared full slot. This needs a bar that rewrites tracked files, so the path is narrow and the effect contained. | sound | - |
| 6 | correctness | tools/unattended/unattended.sh:10704 | high | high | confirmed | Confirmed. unattended.sh never unsets GATE_LEGS, GATE_REUSE or GATE_DOCS_BASE (grep finds none). Its bar arms (10654/10656/10666) unset only GATE_WALL/GATE_FULL. run-gates.sh still honours GATE_LEGS (line 227, it outranks the manifest) and GATE_REUSE (2019). After rc 0, the driver's new write_bar_green (10704) records `kind full` or `kind scoped` under the bar string GATE_CMD. It does not check the run record's manifest or reuse count. The hook's cover check on a bar record compares only tree, bar string and selftests (plus kind and base). So a subset run under an inherited GATE_LEGS certifies the whole bar for that tree. The hook scrubs exactly these knobs before its own writer runs (BAR_SCRUBBED_KNOBS at 1717, GATE_DOCS_BASE at 1732). The driver wrote no such record at the base, so this diff makes the path reachable. It needs an inherited knob, so the path is narrow, but the result is a check certifying what it did not check. | sound | - |
| 7 | correctness | tools/unattended/unattended.sh:10635 | medium | medium | confirmed | Confirmed. --decide prints `scoped $scoped_base` (pre-push 1964). When a kind-scoped record is adopted, resolve_scoped_base sets scoped_base=rec_sha and scoped_full=rec_base, so the printed sha is the scoped record's own sha. The driver parses that sha into _gbase (10632-10634) and passes it to write_bar_green as the base. The hook's writer passes scoped_full instead (2162, S6b). check_bar_base refuses a scoped record whose base is not a full green, so the driver's record is unusable and overwrites the .scoped slot. That costs bar time, never a wrong verdict, so the effect is contained. | sound | - |
| 8 | seams | tools/run-gates/run-gates.sh:3793 | high | high | confirmed | Confirmed. The ledger block (around 3793) sets lfull=1 from GATE_FULL and TREE_CLEAN only. tree_moved is computed later, at 3962-3963. Each row's key is input_key computed when the leg finishes (2655). For unguarded legs that key is FPRINT_START, and for guarded legs it is `git ls-files -s` (the index at that moment) plus PORCELAIN_START. So in a run whose tree moved, a leg can grade moved content while its key names other content, and the row still carries full=1 with head=HEAD_SHA. The lineage predicate (2418-2443) checks full, blob, base, ancestry and key equality, but not the earning run's verdict. A later lineage run on a tree whose key matches then reuses that verdict, and since reuses==lineage_reuses it can stamp gate-full-green (4047). The full column and the lineage stamp are new in this diff. The path is narrow (a tree moving mid-bar, which i26 shows happens), and the consequence is a full-green stamp over a leg whose inputs moved. | sound | - |
| 9 | seams | tools/unattended/unattended.sh:10704 | medium | medium | confirmed | The adoption pass at pre-push:1655-1685 can adopt a `kind scoped` bar record. It then sets rec_sha=M and rec_base=B, and resolve_scoped_base (1753-1757) gives scoped_base=M and scoped_full=B. `--decide` prints `scoped $scoped_base` (1964), so the driver gets M. unattended.sh:10635 takes that as _gbase, and 10704 passes it as the record's base. write_bar_green puts that record in gate-bar-green.scoped (10490), overwriting M's own record. check_bar_base only accepts a runner stamp or a `kind full` record whose sha equals the base, so a record whose base is M is refused. The hook's own writer uses scoped_full (2162), so the two writers really do diverge. The only effect is cost (a FULL run or an older base), never a wrong verdict, so medium. | sound | - |
| 10 | seams | .githooks/pre-push:2162 | low | low | confirmed | resolve_scoped_base sets scoped_full=inh_sha when an inherited green was adopted (1755), and the hook writer records that as the base (2162). check_bar_base reads only green_candidates (gate-full-green, runner bar) and `kind full` bar records. It never reads gate-inherited-green. An inherited green is adopted only after the full green was refused, so a scoped record over it can never pass check_bar_base and is useful only as an exact-tree cover. The scoped records are new in this diff. The effect is a lost saving plus a misleading comment, so low. | unsound | - |
| 11 | seams | tools/unattended/unattended.sh:10636 | low | low | confirmed | unattended.sh:10636 requires `${#_gbase}` = 40. The hook's `--decide` argument check (pre-push:1307-1311) accepts 40 or 64 hex digits, and print_decision passes whatever sha git produced. In a SHA-256 repository every `scoped` answer is therefore treated as malformed, and the driver falls back to GATE_FULL=1. That is safe and costs only time, and SHA-256 repositories are rare, so low. | sound | - |
| 12 | verification | tools/unattended/unattended.sh:10704 | medium | medium | confirmed | This is the same defect as id 9, seen from the verification side, and the code bears it out. `--decide` prints scoped_base (pre-push:1964), the driver writes it as the base (unattended.sh:10704), and the hook writes scoped_full (2162). When the adopted record is `kind scoped`, the driver's record names a scoped sha, which check_bar_base refuses. The result is only extra work, never a wrong verdict, but the parity checks named in the finding do not catch it. Medium. | sound | - |
| 13 | verification | .githooks/pre-push:1873 | medium | medium | confirmed | The hook prints the 'pre-push: not covered — …' line only when `_cov_bars` is set, and only the bar-record loop sets it (pre-push ~1906-1913). The AC9 fixture has a runner stamp and no gate-bar-green, so a refused runner stamp prints no reason. The fix's assertion of 'not covered' with the specific why would fail against correct code. | unsound | - |
| 14 | verification | tools/run-gates/post-merge.sh:313 | low | low | confirmed | run_bar in post-merge.sh (lines 300-318) has two guards. One turns HEAD moving after the bar into REFUSED, which exits 2 through write_refusal. The other turns a default runner that exits 0 without verdict GREEN into RED. No post-merge arm in pre-push.test.sh, push-main.test.sh or run-gates.evidence.test.sh reaches either message. This is a test gap only, on a narrow path, so low. | sound | - |
| 15 | intent | .githooks/pre-push:1922 | blocker | high | confirmed | When a bar record is adopted, rec_sha becomes `_sel_sha=$bg_sha`, which is the scoped record's own sha (pre-push ~1658-1673). On a cover, `_pm_x=$bg_sha` (line 1922). check_post_merge_red clears the red whenever that sha strictly descends from it, and never asks whether the record is full. So a kind-scoped record written during the post-merge window (before refs/gov/bar-red existed) at a commit descending from the red clears it. That record's base can be a full green older than the red. The push then lands scoped (or covered), and no full green ever descends from the red. This contradicts design D8 ('the adopted full green's sha descends from it') and the AGENTS.md landing rule ('until a full green descends from it'). It is reachable only where an adopter declares GATE_POST_MERGE and a landing falls inside a post-merge bar's run. That window is ordinary but narrow in scope (gov declares none), so high rather than blocker. | sound | - |
| 16 | intent | tools/unattended/unattended.sh:10704 | medium | medium | confirmed | In unattended.sh, `_gbase=${_gdl#scoped }` is the --decide line's base, which is scoped_base (the adopted sha, possibly a scoped record's). write_bar_green then writes it as the base of gate-bar-green.scoped. The hook writes scoped_full (pre-push ~2162). check_bar_base (1467-1488) accepts only a full green as a base, so the driver's record can never be adopted, and it overwrites the scoped slot. The next push falls back to an older full green or to FULL. That costs bar time, not verdicts, so medium. | sound | - |
| 17 | intent | memory/guides/UNATTENDED-PROTOCOL.md:517 | medium | medium | confirmed | This diff changed the GATE_POLICY_FILE row at memory/guides/UNATTENDED-PROTOCOL.md:517 to add `GATE_POST_MERGE` to the keys read from the file GATE_POLICY_FILE names. tools/PROTOCOL.template.md:517 carries the same text. The code does not do that. read_gate_policy in tools/unattended/unattended.sh:8980 sets GP_POST_MERGE from `$r:.githooks/gate-env.sh` before it looks at the conf at all, and its own comment says 'whatever GATE_POLICY_FILE names' (TOOL-9 F3). push-main.sh:354-385 also reads it from the gate-env file at the landed tip, and design rev D11 says the same. The protocol's own landing paragraph at line 440 says 'declared at R in the pre-push hook's gate-env file', so the document contradicts itself. An adopter whose GATE_POLICY_FILE names another file and who follows the row declares the key where nothing reads it. They silently lose the scoped landing and the post-merge bar. That fails safe, since the full bar still runs, so the effect is contained: a misleading document, graded medium. | sound | - |
