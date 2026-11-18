**Serves:** journal TOOL-dDeclaredLoop-49

# Builder return — TOOL-dDeclaredLoop-49, dispatch 1: the budget row's figures and plant count moved under unit 48

## Why

DIVERGENCE: section 5 of memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-49.md (rev-3, grounded at c6e66bfc) makes two claims that unit 48 (d7d833cb5) has since changed.

(1) In the risks bullet "every held leg is budgeted, every budget row resolves", the spec says the `loop budget fixtures` row in tools/run-gates/selftest-budgets.txt has "315 PINNED proxy, 210 seconds of thirteen direct-CLI plant readings x1.5". It also says that after the re-price "its prose says fourteen plants". 48 re-priced that row. It now reads 328, from a 219 s reading over fifteen plants (trailer-only, patch-trailer-only and log-dropped took the place of no-log). If I followed the spec as written, the row would say "fourteen plants" and use the wrong base figure. Section 5 needs to say: the 328 PINNED proxy (219 s of fifteen direct-CLI plant readings x1.5) is re-priced with the parallel-append plant's direct-CLI reading added, x1.5, and its prose says sixteen plants.

(2) In the `loop budget fixtures` risks bullet, "the thirteen plants' rows are written by one history, so none disagrees" now has to say fifteen. 48's three plants also write their rows from one history and still pass under today's raise, so the conclusion holds and only the count is wrong.

The rest of the sweep against 48's shipped code still holds, so these two are the whole divergence:
- The raise is still at tools/loop/budget.py#read_budget_rows, inside the one row loop that now covers 48's trailer, suffixed RUN.md and run-state homes.
- Besides budget.py, the only caller of `read_budget_rows` and `record_draw` is still `tools/loop/loop_transition.py#write_transition`. 48 added one more `read_budget_rows` call, but it is inside that same function, and that function passes no `notes`.
- `main` still prints the draw verdict as its only line, and `tools/unattended/unattended.sh#run_budget_draw` still keeps the first line.
- `.gitattributes` still has no transition-record line, and the `merge=ours` block ends with the `.governance/instructions.lock` line.
- No transition record is tracked (count 0 at this base).
- VERB_OFFENDER_PIN is still 1215, and the REFUSAL_CEILINGS token for unattended.sh is still 329.
- The usage row `script:{prefix}/loop/budget.py` lists `--plant=`, and the three budget fingerprints sit on help/loop.md.
- The kickoff `watch:` line names none of the four files.
- The leg's ceiling in tools/gate-legs.json is still 300.

Nothing was written or staged, so no patch was saved.

## Summary

I stopped before writing anything, so nothing is committed and no product path changed. Base is b7ce52613d01e0c30b13fda1b0edbac472a40937.

**What I checked (read-only):**
- I read the spec, the brief, BUILD-METHOD.md and tools/loop/budget.py as 48 shipped it, then re-ran the spec's section 5 sweep against the tree.
- I diffed d7d833cb5 on tools/run-gates/selftest-budgets.txt. 48 moved that row from 315 / 210 s / thirteen plants to 328 / 219 s / fifteen plants.
- I ran AC1's probe at the base: `git check-attr merge -- 2026-11-16-build-TOOL-dDeclaredLoop-1-transition-1.md` in memory/builds/dDeclaredLoop/build/ answered `merge: unspecified`. That is AC1 failing as expected before the change, and it stands in for nothing at the gate.
- `python tools/govkit/docs_leg.py --fingerprints` showed the three budget.py anchors on help/loop.md.
- I checked the readers of `.gitattributes` (check-wiring.sh, asbuilt_view, and govkit's lf_pin, which only reads eol pins). None of them reads a `merge=union` line.

No gate, suite or bar ran.

**Still owed once the spec is revised:**
- AC2 is the parallel-append plant. Its new arm needs the main loop to see it fail first and then pass, at the close, on two staged breaks: the typed-figure refusal that is in the code today, and a tree where `git check-attr merge` answers `unspecified`.
- The close also owes the `loop budget fixtures` and `every held leg is budgeted, every budget row resolves` legs.

**Other things I noticed:**
- The orientation card still says unit 49 is Tier-2 at DEFERRED, but the spec header says INPROGRESS. The card is out of date.
- memory/builds/dDeclaredLoop/RUN.md has a brief row for unit 49 (line 282) but no `dispatch` row. The write set the task says was declared before I was spawned is not in the tracked RUN.md at this base, so the next dispatch should check that it actually recorded.

`gotchas.py --for-diff` was not run because there is no commit.
