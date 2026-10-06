# Acceptance ledger — TOOL-aGraftedHelix-32

**Serves:** journal TOOL-aGraftedHelix-32

Node `a`, 2026-10-05. The build commit is `525079d4`, over the pass's parent `a6de788a`, the spec's
rev-3 commit; rev-2 (`28f063c2`) corrected S12 and AC18 after the slice measured the holder call's
exit, and rev-3 added the parity scan's dead-probe refusal after the pass's bug-class checklist
selected `vacuous-selector-empty-population`. No merge bar and no self-test suite ran in this pass.
Each suite's new arms ran as a slice generated into the session scratchpad with the kit dir pinned:
the driver suite's prologue, the claim block's helpers and the new GH32 block (68 assertions, green);
the build-harness suite's prologue and its GH16 block (41, green) and its parity-leg layouts (82,
green); the card suite's prologue, card fixture and claims block (28, green); the recall self-test
module executed through `test_spine_nested_layout` (6 checks, all ok). Every staged break of the
driver was a copy beside it in the kit dir, removed after; each staged break of another file was
restored and confirmed byte-identical. The whole suites, and the bar, are the main loop's, at
VERIFYING.

**Evidences:** TOOL-aGraftedHelix-32
- AC1 — `git diff --cached --name-only` — the build-harness slice's GH32 run printed `rc=0`, `git show --name-only` named neither `notes.txt` nor `memory/builds/tB/RUN.md`, and the cached list read both; the same slice with the block's commit line cut back to the pathless `git commit -q` printed three FAIL lines, the commit holding both paths and the cached list empty.
- AC2 — `node tools/workflows/check-workflow-syntax.js` — exited 0 at the build bytes with `6 workflow script(s) parsed clean`; given a scratch copy of `unattended-build.js` with ` -- <spec paths> "${delta[@]}"` cut it exited 1 naming the copy at line 933; a copy of the check with its predicate inverted passed that cut copy.
- AC3 — `cd tools/workflows && python check_by_design_parity.py ../memory-tree` — exited 0 with one agreement line for `tier2-review.template.js`, one for `unattended-build.template.js` naming its pattern and its `BY_DESIGN_FORMAT` at count 0 and count 12, and `population — 3 file(s)` naming `gotchas.py`, `tier2-review.template.js` and `unattended-build.template.js`.
- AC4 — `BY_DESIGN_FORMAT` — scratch copies of the checker and both templates exited 0 over `tools/memory-tree`; the copy's format reworded to `by-design` exited 1 with two `DRIFT — the format` lines naming `unattended-build.template.js`; the declaration cut exited 2 with `REFUSING — the harness's format in unattended-build.template.js`.
- AC5 — `extra.py` — the same copies plus an `extra.py` carrying the tail exited 1 with a DRIFT line naming it; with it gone and the build template deleted the checker exited 2 with `REFUSING — the evaluated template unattended-build.template.js is absent`; `--selftest` printed `selftest: 18/18 arms`, and each of the five new arms printed FAIL under a scratch copy with its predicate disabled.
- AC6 — `push-main-active` — the driver slice's beat over a due claim printed one `beat —` line skipped naming the marker, the refusal file byte-identical and the claim ref unmoved; a driver copy without the guard redded the line, the file and the ref.
- AC7 — `retired the finished record` — green in the driver slice: check 9 at the README's markers with the line absent and the tree clean, and check 9 at a live record's generated close with the claim at its pre-call sha; the parent's driver redded both halves, archiving the record and moving the claim.
- AC8 — `preflight OK` — green in the driver slice: a session id carrying a CR, passed by redirect, refused at check 17 with the tree clean, the record at its HEAD blob and no archive, and the next clean call archived it; the parent's driver left the rename and a fresh record staged, and a copy with the restore cut did the same.
- AC9 — `the run-state file is unchanged` — green in the driver slice under a git shim failing only the record's add: check 9 `cannot stage the run-state file`, the line printed, the tree clean and no archive; a copy with the restore cut left the rename staged.
- AC10 — `claim marked aborted` — green in the driver slice: one line, and `--claims` read `aborted terminal`; a copy with the disposition cut printed no line and read `live live`.
- AC11 — `claim left` — green in the driver slice: one line naming `renew`, `--claims` read `live` and the record sat at its HEAD blob; a copy running the create row's write on a renew read `aborted`, and a copy with the restore cut left the record rewritten.
- AC12 — `write_preflight_record` — the slice's structural arm read `1:0`; a copy with one `return 1` added after the claim write read `1:1`; `python tools/memory-tree/check-arms.py --check` exited 0 silent once the check-9 stage row left `unarmed-branches.txt`, having named that row armed before.
- AC13 — `claims: off` — a clone under `%TEMP%` with `RUN_CLAIMS="off"` printed exactly `claims: off`, exit 0, its git shim logging no fetch among 2 calls; with `RUN_CLAIMS="on"` it printed `claims: none` with one fetch logged.
- AC14 — `claims — skipped: RUN_CLAIMS is off` — the card slice wrote that cell with no fetch logged and the shim's log non-empty, and the 25 existing claim assertions kept their verdicts; the card's awk with the off branch cut redded the cell, and the parent's driver redded the cell and the fetch count.
- AC15 — `UNATTENDED check 24 FAILED` — green in the driver slice: a second remote after preflight left `--dispatch` at exit 0 with one `claims not read` line naming check 24, none of that failure, and one dispatch row; a copy with the soft branch reverted exited 1 printing it.
- AC16 — `## Its gate` — `grep -n "location-probe-class-gate" memory/builds/aGraftedHelix/RUN.md` printed line 61, a decision row carrying ` · reason `, and the class record's grep printed a line inside that section.
- AC17 — `python tools/memory-tree/gotchas.py --check` — exited 0; `--for-paths tools/unattended/unattended.sh` listed `decision-re-derived-by-a-second-process`, `destructive-step-before-its-precondition` and `a-spelling-change-strands-its-readers`, and `--for-paths memory/builds/aGraftedHelix/RUN.md` listed `orchestrator-hand-off-owed-a-disposition`.
- AC18 — `git ls-remote` — green in the driver slice, the holder call exiting 0; a copy routing the unread claim into a CAS with an empty expected sha redded the push count and the exit while the ref assertion stayed green, as rev-2 states.
- AC19 — `EVIDENCE_BANNER` — the recall slice read all 6 checks ok; `query.py` printing the banner twice redded `test_empty_alias`; `extract.py` with its `superseded` print cut redded both spine arms; both restored, `git diff --quiet` held.
- AC20 — `python tools/memory-tree/row_grammar.py --selftest` — printed `PASS — row_grammar: all arms held`; with a sixth inline copy of the prefix the new arm printed `arm FAIL` reading `2 copy(ies)`; the file restored byte-identical.
- AC21 — `grep -cE "check 10[789]" memory/map/features/unattended-stops.md` — counted 3, and the check-89-or-90 grep printed nothing.
- AC22 — `bash tools/check-kit-versions.sh` — exited 0 at `525079d4`; `python tools/govkit/govkit.py epoch --base a6de788a2` read `clean` at unattended 1.79, review-harness 1.38, memory-tree 2.130, memory-recall 1.27 and kickoff-manifest 1.19; `bash tools/unattended/adopt-unattended.sh --check` printed `in sync`.
- AC23 — `python tools/codebase-map/test_codebase_map.py` — every line read `ok` once the new class record was claimed; `bash skills/session-kickoff/manifest-check.sh` exited 0 over the re-stamped manifest.
