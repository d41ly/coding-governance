# Build journal — TOOL-dPolishedVitrine-14

**Serves:** journal TOOL-dPolishedVitrine-14

Tier-2 · node d · 2026-09-13 · spec base 09a22d2b · branch tip at start f1e58789 · worktree
`.claude/worktrees/derived-harness-paths`

## The leg and its sibling at the start, over this tree

`bash tools/unattended/check-brief-recorded.sh` at `f1e58789` exited 0 in 14 s. It graded 28 closed
units, skipped 101 builds by the 2026-09-06 cutoff, counted 2 builds with no pinned BASE and 18
units unbuilt-in-range. `bash tools/unattended/check-pass-order.sh` at the same commit exited 0 in
69 s, and its stdout was kept for the byte comparison below.

## The candidate predicate, run over the real tree before it was wired

An independent probe in the session scratchpad walked every build with a pinned BASE, with the
cutoff IGNORED, so its population was wider than the leg's. It found a build commit for 261 CLOSED
units and none for 108. At those build commits the run-state file read BUILDING for 198, ABORTED
for 20, REVIEWING for 14, FOLDING for 7, RUNNING for 6, LANDING for 5, LANDED for 5, VERIFYING for
4 and SPECCING for 2.

- **The hits.** 25 units were built under a terminal record, 20 ABORTED and 5 LANDED, across
  `aPacedTurnstile`, `cBriefedPilot`, `dClosedLexicon` and `dScriptedRepeat`. Every one sits in a
  build opened before the 2026-09-06 cutoff, so the leg's real population holds none of them.
- **The first corroboration was wrong.** Comparing the build commit's record BYTES with HEAD's bore
  out 8 of the 25. The other 17 records were edited after they finished, by `710f5a16`, the
  migration that added a halt code to six aborted records, and by `ef55c01b`, a merge fix that did
  the same to a seventh. Comparing the CLAIM, meaning base, phase and witness, bore out all 25. That
  is why the leg compares claims.
- **A history walk was tried and dropped.** A topological-order walk of each record's path flagged
  three terminal-to-live reopenings, in `aBoundedCeiling`, `aBranchedMandate` and
  `aPromptedMandate`. Each was two interleaved branches, not an ancestry edge. A parent-to-child
  edge scan found 19 real terminal-to-live edges, and every one carried a new retired record. So
  the driver's "a finished record leaves only by rotation" holds over the whole tree, and the claim
  comparison needs no topology.
- **The near-misses.** 5 units were built while their record read LANDING, the last live phase.
  All 5 stay graded, and the widened leg below redded each for its missing row.

## Every new arm, observed red before its fix

Each break was staged into a copy of the kit in the scratchpad, never into this tree, and run with
this unit's suite. The raw outputs are in the session scratchpad; the counts below are what matters.

1. **The leg at `f1e58789`, with this unit's suite.** 26 assertions failed. They were the two new
   liveness counts, all seven post-run asserts, the two post-abort asserts, the four terminal-set
   refusal asserts, the zero count in the live arm, both flip asserts, all three rotated asserts,
   both migrated asserts, and the announcement and count asserts in the reopened and copied arms.
   The live, landing and baseonly exits, and the reopened and copied exits, passed there as they
   must, because they assert the verdict this unit keeps. So did the staged-driver assert, which
   reds either way.
2. **The corroboration removed**, so any terminal phase is honoured. 8 failed: all five reopened
   asserts, both copied asserts, and the rotated arm's check that the retired record is the one
   still making the claim.
3. **The absence test removed.** Both copied asserts failed and nothing else did.
4. **The claim's terminating dot removed.** The baseonly arm failed, because the base was read as
   the phase and the leg announced GRADED ANYWAY.
5. **A byte comparison in place of the claim.** Both migrated asserts failed and nothing else did.

## A defect the staged runs found in the suite itself

The first staged-break run printed `sed: can't read …/.brk/check-brief-recorded.sh` and failed the
truncated-cache arm with exit 127 in every variant. That arm copied `$LEG`, which is relative to
the invoking directory, so from the repository root it copied the repo's own leg and from anywhere
else it copied nothing. A suite run against a staged kit therefore graded the wrong leg in that one
arm. It now copies from `$KIT`, and every later staged run shows only the arms its break targets.

## The leg after the fix

- The suite passes all 88 arms in 43 s, from the repository root and from a scratch directory. At
  `f1e58789` the suite had 46 arms and took 24 s.
- The leg over this tree exits 0 in 16 s, with the four counts it printed at base and two new
  counts at zero.
- Over the widest population, in a scratch clone at `f1e58789` carrying this unit's leg with the
  cutoff lifted to 2026-01-01, the leg skipped 25 units and reported none unborne. The 25 ids equal
  the probe's, and none of them appears among that run's violations.
- `git diff f1e58789 HEAD` over `check-pass-order.sh` and `lib-unattended.sh` is empty.
- `bash tools/unattended/run-unattended-gates.sh --checks` passed all five legs. The kit gate took
  85 s, playbook validity 2 s, skill wiring 1 s, pass-order 64 s and brief-recorded 15 s.
- `bash tools/check-kit-versions.sh` exits 0 with every unattended carrier at 1.20.

## The full bar, first run: one red was this unit's

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at `8f22b419` ran from 15:21:49
to 15:33:25 UTC, while other sessions loaded the node. 103 of 106 legs were green and three were red.

- **`drift-audit records`, and it was this unit's.** Signal 2,
  `non_terminal_specs_cited_by_product_source`, went from 2 to 3 over a shrink-only pin, because
  the leg's header cited this unit's id while its spec is INPROGRESS. `e99df7d8` points the header
  at the ruling and the build instead, and leaves the id in the suite, which that signal does not
  read. That is where `TOOL-dPolishedVitrine-1` keeps its own id too. Spec rev-2 amends AC9 to
  match. The signal reads 2 again.
- **`python resolver (behaviour + inline parity + idiom ban)`.** Red at `24f8c712` too, as that
  unit's journal records, and not fixed here.
- **`process-monitor census selftest`, on this session and not on the code.** Its arm
  `test_live_scope_is_not_empty` found the shipped roots admitting no live process. Rerun alone, the
  sibling arm `test_shipped_conf_admits_this_repo` failed for the same reason. The arms admit a
  process only when its own command line carries a path under `PROCMON_ROOTS`, and this session's
  shells are rooted in a NicoCares worktree, so none does. Rerun from a command line carrying this
  repo's absolute path, the suite passed 66 of 66. Nothing under `tools/process-monitor/` or its conf
  has moved since `24f8c712`.

`pass-order history` printed stdout byte-identical to its run at `f1e58789` in that bar, 550 bytes
both, and `brief-recorded` printed this tree's counts with its two new counts at zero.

## The full bar, second run, at the fix

The same command at `e99df7d8` ran from 15:39:20 to 15:51:16 UTC. 104 of 106 legs were green, and
every chunk was green but `selftests` and `wiring`. The two reds are the two above that are not this
unit's. `process-monitor census selftest` failed `test_live_scope_is_not_empty` again, and passed
66 of 66 when rerun from a command line carrying this repo's absolute path. `python resolver`
failed on its unresolved-launcher arm, as it does at `24f8c712`. `drift-audit records` was green.
`pass-order history` printed stdout byte-identical to its run at `f1e58789` once more.

## The on-demand unattended suites, at `e99df7d8`

None of these is on any bar, so each was run by hand after the second bar finished.

- `check-brief-recorded.test.sh`, the suite this unit extends, passed 88 arms in 49 s.
- `check-pass-order.test.sh` passed 72 arms in 57 s, and nothing it tests has moved.
- `adopt-unattended.test.sh` passed 71 assertions in 18 s. It renders the protocol template this
  unit edited.
- `cross-component.test.sh` passed 19 assertions in 68 s. It copies the same template.

`check-unattended.test.sh` and `unattended.test.sh` were NOT run. Their declared budgets are 13600 s
and 3860 s, this unit changes neither file they exercise, and no arm in either greps the one
protocol row this unit edited. The kit gate those suites cover passed on both bars, with its
protocol parity check included.

## What moved and what did not

- No kickoff-manifest watch path moved, so `last-audit` is not re-stamped.
- The unattended kit stays at 1.20. `main` still holds 1.19, so this rides the unreleased version.
- `TOOL-dPolishedVitrine-15` files the one residual the corroboration leaves, a forged finished
  record that stays at HEAD, for the kit gate.

## What the round-3 review changed

The round-3 Tier-2 diff review of `d36549fb...c9bc0b2a` confirmed two defects in this unit. Its report
sits under `reviews/`, and `TOOL-dPolishedVitrine-1`'s journal carries the other eight.

- **R3-4, high: a wrongly picked build commit let a unit built during a live run skip grading.**
  `build_commit` returns the earliest commit that names the id and touches a path outside the record
  surface. A hand commit made between two runs qualifies, the record there still reads the first
  run's LANDED, and the second run's preflight retires that record afterwards, so the retired record
  at HEAD bore the claim out. The leg now walks the commits after the pick before it honours a skip.
  For each one whose cached subject names the id, it calls the library's own `build_commit` on that
  one commit, and the first one made while a run was live is where the unit is graded, announced
  with both commits and counted on the liveness line. `lib-unattended.sh` is unchanged, so
  `pass-order` keeps its pick, and `git diff c9bc0b2a` over both files is empty. The header states
  the rule and that it fails closed, and spec §4 has a subsection for it. The gate is the `misselect`
  arm, whose fixture is the review's reproduction. Observed red against the leg at `c9bc0b2a`: five
  of its assertions failed, and the leg exited 0 printing `NOT GRADED` for a unit built under the
  second run's BUILDING record. After the fix the suite passes 94 arms.
- **R3-10, low: the conf example dropped the claim-at-HEAD condition.** Its description now points at
  the protocol's `BRIEF_RECORDED_CUTOFF` row instead of restating which units are graded, and that
  row gains R3-4's later-commit condition, in the template and in this repo's installed copy
  together. The review asked for no new gate, because retiring the copy is the gate. The
  `two-answers-to-one-question` gotcha records it as a live instance.

The widest population was measured again. In a scratch clone at `c9bc0b2a` with the cutoff lifted to
2026-01-01, the fixed leg and the leg at `c9bc0b2a` each skipped 25 units, the same 25 ids, which are
the ids the probe found for AC14. The fixed leg graded 0 at a later commit, and its output differed
from the old leg's only by the new count on the liveness line. So the fold moves no verdict in this
repo's history, and its population is empty here, as this unit's own was when it landed. Over this
tree the leg exits 0 with all three post-run counts at zero.

The spec moves to rev-3, and its §9 line logs S6, S8, §4, §5, AC15, AC16 and §7.

The full bar at `728a59a4`, 18:19 to 18:31 UTC, was green on 105 of 106 legs, the one red the python
resolver line that is red at `24f8c712`. `brief-recorded` passed in 18 s, `pass-order history` in
82 s, and `unattended kit gate`, whose protocol parity check compares the edited row's two copies,
in 123 s. `pass-order history` printed 550 bytes of stdout, the size its run at `f1e58789`
printed; this time the bytes themselves were not compared. `TOOL-dPolishedVitrine-1`'s journal
records that bar and the one before it, whose reds were that unit's. `check-pass-order.test.sh` passed 72 arms, `adopt-unattended.test.sh` 71
assertions and `cross-component.test.sh` 19, each run by hand on the fold's tree.
`check-unattended.test.sh` and `unattended.test.sh` were NOT run, for the reason that journal gives.

## The merge of `main` at `9ce37fcc`

S7 rode an unattended 1.20 that `main` had not released. `main` then released its own 1.20 at
`7ade2b08`, a different kit, so the merge `9a5c0793` renumbered this lineage to 1.21 at every
carrier the version gate reads, and `tools/check-kit-versions.sh` exits 0 there. The leg merged
clean against `main`'s edits to the unattended kit. NicoCares took this change at `5cea0dfd` as
1.20, and so did inCMS core; their pull to 1.21 is `TOOL-dPolishedVitrine-16`. Spec section 9's
rev-4 line logs the move.

The full bar at `340d0679`, self-tests included, was green on 105 of 106 legs, `brief-recorded`
and the unattended kit gate among them. Its one red was the process-monitor census arm that counts
this node's processes by kind, which passed 66 of 66 run alone; `TOOL-dPolishedVitrine-1`'s journal
carries the detail.

## Acceptance ledger

**Evidences:** TOOL-dPolishedVitrine-14
- AC1 — `NOT GRADED` — the postrun fixture exits 0, names ARCH-tBrief-1, LANDED and the record still making the claim, and counts one unit built after its run finished.
- AC2 — `PHASES_TERMINAL` — the ABORTED fixture exits 0; with the fixture driver's set staged to LANDED alone the same history exits 1 with `NO brief row`.
- AC3 — `NO brief row` — the live and landing fixtures both exit 1 with the ordinary violation, and neither prints NOT GRADED.
- AC4 — `flip` — the fixture whose build commit writes LANDED exits 0 and prints NOT GRADED.
- AC5 — `rotated` — exits 0 and names the retired `RUN.ABORTED.` record as the one still making the claim.
- AC6 — `GRADED ANYWAY` — the reopened and copied fixtures both exit 1 and print it; each went green on a staged break of its own guard.
- AC7 — `migrated` — exits 0 with NOT GRADED after a halt code is added to the finished record; red on the staged byte comparison.
- AC8 — `DEAD PROBE` — a deleted or lowercase `PHASES_TERMINAL` line exits 2 with no liveness line.
- AC9 — amended rev-2 — the header points at the ruling in build `dPolishedVitrine` instead of citing this unit's id, which the suite carries; section 9's rev-2 line logs the drift red that forced it. Read at `e99df7d8`, `tools/unattended/check-brief-recorded.sh` names the predicate, the boundary, the corroboration, the rejected reachability predicate and both new non-checks.
- AC10 — `tools/unattended/check-brief-recorded.test.sh` — 88 arms, exit 0, run from the repository root and from a scratch directory; every staged kit copy showed only its targeted arms red. At rev-3 it passes 94 arms, `misselect` included.
- AC11 — `tools/unattended/check-unattended.sh` — the kit gate passed, check 10 included, over `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md`, which are byte-identical. It passed again on the bar at `728a59a4`, after rev-3 extended the row in both copies.
- AC12 — amended rev-4 — `tools/check-kit-versions.sh` exits 0 with every unattended carrier at 1.21, the merge's renumber; spec section 9's rev-4 line logs the move.
- AC13 — `tools/unattended/check-pass-order.sh` — stdout byte-identical to its run at `f1e58789` on both bars, and `tools/unattended/check-pass-order.test.sh` passed 72 arms; `git diff` over it and the library is empty.
- AC14 — `tools/unattended/check-brief-recorded.sh` — in the scratch clone with the cutoff lifted, 25 skipped, 0 unborne, the same 25 ids the probe found. Re-run at `c9bc0b2a` with rev-3's leg: the same 25 ids, and 0 graded at a later commit.
- AC15 — `GRADED AT A LATER COMMIT` — the `misselect` fixture exits 1 with `NO brief row`, names the unit and counts one; against the leg at `c9bc0b2a` it exited 0 printing `NOT GRADED`, and five assertions failed.
- AC16 — `tools/unattended/.unattended.conf.example` — its `BRIEF_RECORDED_CUTOFF` description points at the protocol row and states no population; the row carries the claim-at-HEAD and later-commit conditions in both copies.
