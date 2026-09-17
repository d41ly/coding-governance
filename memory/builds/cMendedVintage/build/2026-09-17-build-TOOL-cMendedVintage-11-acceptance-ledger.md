# cMendedVintage — the acceptance ledger for unit 11

**Serves:** journal TOOL-cMendedVintage-11

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh`
suite ran in this pass. The kit's own `python tools/process-monitor/selftest.py` did run, twice,
because the brief hands it over as the direct observation of every criterion here and it costs about
a minute. Every other observation below is a run of the arm itself in a standalone process.*

## The one thing worth reading twice

**The attribution held, and the product needed nothing.** The arm was run before anything was
touched and answered `(False, [], [])`, the tuple the read-only investigation measured at BASE and
at HEAD. Under a resolved launcher and with `census.py`, `scope.py` and `reap.py` untouched, the same
arm walks seven processes, kills seven and reports no survivor — which is the measurement the brief
predicted, reproduced here before a line of the fix was written.

**Resolution by lookup would have shipped the bug back.** `shutil.which("bash")` on this node
answers `C:\Program Files\Git\usr\bin\bash.EXE` — the RIGHT binary. Executing `bash` on the same
node answers `Linux`. The lookup and the execution disagree about the same name, which is the exact
shape this repo already recorded for its python launcher and is why the resolver RUNS every
candidate and reads `uname -s` rather than trusting the path a lookup handed back. Had the fix
resolved by `shutil.which` alone it would have accepted the WSL launcher under a longer spelling and
the arm would still be red.

**The count would have passed the AC2 run.** With one member prevented from starting the arm walked
FIVE processes. The assertion this unit deleted was `len(rep["walked"]) >= 4`, so that run would have
been green with the native python grandchild missing from the tree entirely. That is the
green-by-absence class caught in the act, and it is the argument for the member assertion being part
of the fix rather than a tidy-up.

**Evidences:** TOOL-cMendedVintage-11

- AC1 — `test_live_tree_dies_completely` — run standalone three times and inside the full kit suite
  twice, all after the change. Its own report line reads
  `walked 7 through C:\Program Files\Git\usr\bin\bash.EXE · members seen: the marked launcher, the nested shell, the native python grandchild, a staged sleep`
  and the suite closes `67 passed, 0 failed (67 assertions)` at exit 0. Before the change the same
  arm on the same tree answered `(False, [], [])`, recorded before anything was edited.
- AC2 — `the missing member was the native python grandchild` — observed on the REAL arm rather than
  a copy of it, by narrowing `PATH` to Git's own bin directories plus `system32` so that `python` no
  longer resolves inside the launched body while every other member still stages. The arm answered
  `(['the native python grandchild'], [], [])` and its report line named the three members it did
  see. Walked was 5, so the deleted `>= 4` count would have called that run green.
- AC3 — `SKIP test_live_tree_dies_completely` — observed with the resolver forced to answer that
  nothing resolved. The arm printed `SKIP test_live_tree_dies_completely (no candidate answered as a
  POSIX shell the census can see; RAN bash, C:/Program Files/Git/usr/bin/bash.exe)` and returned with
  `PASS` still empty, so the branch announces what it looked for and reports no pass. It is a
  distinct line from the pre-existing platform skip, which is what AC3's red condition names.
- AC4 — `the cleanup probe reported stray: none` — printed by every post-change run of the arm, as
  `cleanup probe through C:\Program Files\Git\usr\bin\bash.EXE` followed by the stray list. The probe
  now shells `ps -ef` and `kill -9` through the resolved launcher rather than a bare `bash`, and it
  states the launcher it used and every `stray` it found, so a clean report is readable rather than
  assumed.

## One thing observed that is NOT this unit's defect

On the FIRST post-change run the arm answered this tuple:
`([], [28548], [(28548, 1, 'kill: 1128596: Permission denied')])`
The member list was empty — all four members staged and walked — and the failure was the msys kill
binary refusing one signal. Five subsequent runs of the arm were clean. This is the
product's signalling path, which section 3 forbids this unit from touching, and it is one refusal in
six runs on a box carrying a sibling unit's build. It is recorded here rather than acted on, because
a one-line reproduction rate is not an attribution and inventing one inside a fixture repair is how
a second defect gets smuggled into a unit that had no business touching it.

## What ran, and what is owed

`python tools/process-monitor/selftest.py` ran twice, green both times, and stands in for section 7's
first gate `process-monitor census selftest`. `python tools/lexicon/lexicon.py --check` ran directly
because the new function is the standing ban's target: it reports `P1 verb graded=2287 offenders=987`,
equal to the declared pin, so the added `resolve_launcher` leads with a declared verb and moves
nothing. `python tools/codebase-map/gen_map.py --write` regenerated the map artifacts; only
`symbols.json` moved, by the single `resolve_launcher` row.

Section 7's second gate, `process-monitor adopter selftest`, is OWED to the bar this run closes with.
It is `adopt-process-monitor.test.sh`, a `*.test.sh` this pass may not run. Its `FLOOR_ASSERTIONS`
cannot have moved: this unit adds and removes no assertion in that file and does not edit it at all.

**A cross-unit entanglement this commit could not avoid, and the closing bar should know about it.**
`gen_map.py --write` derives from the WORKING tree, and the sibling unit `DEPL-cMendedVintage-25` is
building in the SAME worktree, so the regeneration also produced a `check_git_split_parses` row for
`tools/govkit/selftest.py` — a function this commit does not contain. That row was removed first, on
the principle that a generated artifact should describe its own commit's tree. The pre-commit
codebase-map gate then refused the commit as STALE, because it compares the artifact against a live
re-derivation over the working tree rather than against HEAD, and on this tree that function exists.

The row was therefore restored and this commit's `symbols.json` carries a symbol from a sibling
unit's uncommitted work. That is the honest description of what a shared worktree does to a
tree-derived artifact, and it is recorded rather than bypassed: the alternative was `--no-verify`,
which buys a tidier commit by disarming the leg that noticed. If `DEPL-cMendedVintage-25` lands, the
artifact is correct at the closing bar; if it is abandoned, that leg reds naming the phantom row and
a regeneration clears it.

## What the bug-class checklist changed

Run from `python tools/memory-tree/gotchas.py --for-paths tools/process-monitor/selftest.py` before
the commit, and again as `--for-diff HEAD~1..HEAD` after it.

`fixture-passes-by-finding-nothing` is the class this unit exists to close, and it was checked
against the fix rather than assumed by it. Every member predicate that the launcher's own row could
also satisfy excludes that row by marker, because the launcher's command line quotes the whole body
and therefore contains every string its members do — `time.sleep(613)` and `sleep 613` both appear in
it verbatim. Without that exclusion all four members would have been satisfied by one surviving row
and the repair would have rebuilt the defect in a new spelling.

`staged-break-substitutes-a-synthetic-value` is why AC2 narrows `PATH` instead of grading a copy of
the arm with a shortened body. The arm, its marker, its body and its predicates are the shipped ones;
only the environment the launched tree resolves `python` in was changed.

`fixture-inherits-ambient-machine-state` is unavoidable here and is answered by announcement rather
than by hermeticity. The resolver must read the machine's real PATH — that is its whole job — so the
arm prints the launcher it resolved on every green line and names every candidate it RAN on the skip.
A future node that resolves something unexpected says so in its own output instead of going quietly
green.

`two-answers-to-one-question` was checked against the one place the fix does NOT spell the resolved
launcher: the nested `bash -c` inside the staged body. That is deliberate — hard-coding the resolved
path there would change the command line under test — and the residual is covered rather than
ignored, because a nested shell that resolves to something the census cannot see makes `the nested
shell` missing and the arm reds naming it.

`empty-field-collapses-unless-it-is-last` touches the cleanup probe's `line.split()` over `ps -ef`.
It is untouched pre-existing parsing and the `isdigit()` guard already means a misparse skips rather
than signals, so nothing was changed on that line beyond the launcher it runs under.
