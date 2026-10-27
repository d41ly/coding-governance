# dRankedPlan - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id and the lease — the
session and pid holding the run — the pinned BASE with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
refreshed-at: 2bd5e10d4e861245d1a5adea5d53b45f90826489 · park · 0 touching
gate-backstop: 29400 (wall 21600 + queue 7200 + margin 600)
witness: 0689e7fa12b553c712dd853eeba9e0085abdf6ff
phase: RUNNING
spec-audit: 2026-10-21
may: PLAY-dClosedLoop-3
mode: slug
run-branch: refs/heads/branch/unattended-drankedplan-1fc3d7
anchor-kind: default-branch
cli-version: 2.1.308
lease-utc: 2026-10-26T18:31:05Z
pid-image: claude.exe
host: compeeto-agent
pid: 26296
session: 43fa2011-5bb6-422a-bd52-776c30d97bd4
keepalive: 08db21e2
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 0689e7fa12b553c712dd853eeba9e0085abdf6ff
anchor-ref: refs/heads/main
base: 0689e7fa12b553c712dd853eeba9e0085abdf6ff

## Parked

2026-10-26T21:39:58Z review · item dRankedPlan-spec-set-r1 · reason verdict BLOCKED · blockers 1 · BOUNDED · highs 9 · minors 39 · disposition promote

2026-10-26T21:50:41Z rescope · item add TOOL-dRankedPlan-19 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 1 BLOCKER item B1: plan.exit is said to need every reached item's witness and no unit builds that rule; repairs TOOL-dRankedPlan-12

2026-10-26T21:50:55Z rescope · item add TOOL-dRankedPlan-20 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 2 HIGH item H1: Scenario none on a patch or repeat plan record reads as a re-pick and its pin is undefined; repairs TOOL-dRankedPlan-14

2026-10-26T21:50:58Z rescope · item add TOOL-dRankedPlan-21 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 3 HIGH item H2 (shared with id 37): unit 2 judges a ratified plan row through the session-scoped predicate; repairs TOOL-dRankedPlan-2

2026-10-26T21:51:01Z rescope · item add TOOL-dRankedPlan-22 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 37 HIGH item H2 (shared with id 3): the commit-time order guard asks a session-scoped consent predicate; repairs TOOL-dRankedPlan-2

2026-10-26T21:51:03Z rescope · item add TOOL-dRankedPlan-23 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 4 HIGH item H3 (related id 38): show re-asks the predicate instead of reading how the gate released the re-entry; repairs TOOL-dRankedPlan-15

2026-10-26T21:51:07Z rescope · item add TOOL-dRankedPlan-24 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 21 HIGH item H4 (shared with ids 5 and 39): no one reader of a build's disposition records bounded to the current crossing; repairs TOOL-dRankedPlan-9

2026-10-26T21:51:10Z rescope · item add TOOL-dRankedPlan-25 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 5 HIGH item H4 (shared with ids 21 and 39): a disposition from an earlier crossing releases a later plan.exit; repairs TOOL-dRankedPlan-10

2026-10-26T21:51:13Z rescope · item add TOOL-dRankedPlan-26 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 39 HIGH item H4 (shared with ids 5 and 21): a disposition whose word is ask or none may release plan.exit; repairs TOOL-dRankedPlan-10

2026-10-26T21:51:15Z rescope · item add TOOL-dRankedPlan-27 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 27 HIGH item H5: gov-spec-writer gains plan: reads keys the closed roles vocabulary refuses; repairs TOOL-dRankedPlan-16

2026-10-26T21:51:18Z rescope · item add TOOL-dRankedPlan-28 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) id 28 HIGH item H6: the triage and dupes record kinds skip the binding reader, the factory table and the HYGIENE kind list; repairs TOOL-dRankedPlan-3

2026-10-26T21:51:20Z rescope · item add TOOL-dRankedPlan-29 · reason spec-audit round 1 (reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) the 39 MEDIUM and LOW findings batched into one unit: ids 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 22 23 24 25 26 29 30 31 32 33 34 35 36 38 40 41 42 43 44 45 46 47 48 49 (items M1 to M21 and L1 to L12)

2026-10-26T23:53:20Z rescope · item add TOOL-dRankedPlan-30 · reason spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) id 19 HIGH item H1: SESSION_PREDICATE_CALLERS spells two literal kit paths the install-prefix ban counts; repairs TOOL-dRankedPlan-22

2026-10-26T23:53:33Z rescope · item add TOOL-dRankedPlan-31 · reason spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) id 20 HIGH item H2: the tree-wide caller gate rides a guarded selftests leg that does not run for the files it polices; repairs TOOL-dRankedPlan-22

2026-10-26T23:53:35Z rescope · item add TOOL-dRankedPlan-32 · reason spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) id 30 HIGH item H7: the caller predicate misses the argv-list call form and false-flags the driver's resolver line; repairs TOOL-dRankedPlan-22

2026-10-26T23:53:38Z rescope · item add TOOL-dRankedPlan-33 · reason spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) id 21 HIGH item H3: unit 19's plan-record precondition reds every earlier admitted plan.exit arm of the shared fixture; repairs TOOL-dRankedPlan-19

2026-10-26T23:53:41Z rescope · item add TOOL-dRankedPlan-34 · reason spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) id 26 HIGH item H4: a disposition renamed after the newest transition counts as fresh; repairs TOOL-dRankedPlan-24

2026-10-26T23:53:44Z rescope · item add TOOL-dRankedPlan-35 · reason spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) id 28 HIGH item H5: the newest kept disposition is undefined for adds in one commit or on unrelated branches; repairs TOOL-dRankedPlan-26

2026-10-26T23:53:46Z rescope · item add TOOL-dRankedPlan-36 · reason spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) id 29 HIGH item H6: the build's first transition meets check_plan_scenario's exit 2 with no rule; repairs TOOL-dRankedPlan-20

2026-10-26T23:53:48Z rescope · item add TOOL-dRankedPlan-37 · reason spec-audit of TOOL-dRankedPlan-19 to -29 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) the 25 MEDIUM and LOW findings batched into one unit: ids 1 2 3 4 5 7 8 9 11 12 13 14 16 17 18 22 23 24 25 27 31 32 33 34 35 (items M1 to M12 and L1 to L6)

2026-10-27T00:14:02Z review · item dRankedPlan-spec-set-r2 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 7 · minors 25 · disposition promote

2026-10-27T01:42:10Z rescope · item add TOOL-dRankedPlan-38 · reason spec-audit of TOOL-dRankedPlan-30 to -37 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) id 1 HIGH item H1: unit 32 drops the textual caller rule for shell and hook files that units 22, 30 and 31 plant against; repairs TOOL-dRankedPlan-32

2026-10-27T01:42:12Z rescope · item add TOOL-dRankedPlan-39 · reason spec-audit of TOOL-dRankedPlan-30 to -37 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) id 2 HIGH item H2 (shared with id 34): a command led by a compound-command reserved word such as if or ! is never read as an invocation; repairs TOOL-dRankedPlan-32

2026-10-27T01:42:14Z rescope · item add TOOL-dRankedPlan-40 · reason spec-audit of TOOL-dRankedPlan-30 to -37 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) id 34 HIGH item H2 (shared with id 2): a command led by exec or another prefix command, or by a case-arm pattern, is never read as an invocation; repairs TOOL-dRankedPlan-32

2026-10-27T01:42:17Z rescope · item add TOOL-dRankedPlan-41 · reason spec-audit of TOOL-dRankedPlan-30 to -37 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) id 33 HIGH item H3: a shlex error on a split piece of a shell line has no rule; repairs TOOL-dRankedPlan-32

2026-10-27T01:42:19Z rescope · item add TOOL-dRankedPlan-42 · reason spec-audit of TOOL-dRankedPlan-30 to -37 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) id 10 HIGH item H4: AC19's CLI half exercises the drive-letter rule because the shell expands an unquoted tilde; repairs TOOL-dRankedPlan-37

2026-10-27T01:42:21Z rescope · item add TOOL-dRankedPlan-43 · reason spec-audit of TOOL-dRankedPlan-30 to -37 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) id 19 HIGH item H5: git log --follow dates a fresh near-copy disposition record to the older record's add; repairs TOOL-dRankedPlan-34

2026-10-27T01:42:22Z rescope · item add TOOL-dRankedPlan-44 · reason spec-audit of TOOL-dRankedPlan-30 to -37 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) id 22 HIGH item H6: dormancy's read_build_disposition picks the newest answer across items with no order and no conflict hold; repairs TOOL-dRankedPlan-4, whose read_build_disposition the finding on unit 35 lands in

2026-10-27T01:42:24Z rescope · item add TOOL-dRankedPlan-45 · reason spec-audit of TOOL-dRankedPlan-30 to -37 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) the 32 MEDIUM and LOW findings batched into one unit: ids 3 4 5 6 7 9 11 12 13 14 15 16 17 18 20 21 23 24 25 27 28 29 30 31 32 35 36 37 39 40 41 42 (items M1 to M18 and L1 to L9)

2026-10-27T02:00:02Z review · item dRankedPlan-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 7 · minors 32 · disposition promote

2026-10-27T02:17:14Z decision · item cap the dRankedPlan spec-audit promotion chain? · reason options: (a) keep promoting per M4 until a round's precision falls below the review protocol's floor — rounds 1-3 ran at 1.00, 0.91, 0.93 with 9, 7 and 7 highs, so no end is in sight; (b) stop at the first round confirming no BLOCKER and no HIGH, as the owner ruled for dPlacedRequest, dDeclaredLoop and dKeptSession; (c) another cap. Refused to choose: an owner cap on the chain is the owner's, and those rulings name their builds, not this one. The run keeps promoting under (a) meanwhile.

2026-10-27T03:26:38Z rescope · item add TOOL-dRankedPlan-46 · reason spec-audit of TOOL-dRankedPlan-38 to -45 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) id 1 HIGH item H1 (shared with id 30): S10's bash or sh body arm is stated through an interpreter class it contradicts, so a body fed to a shell has no reachable reader; repairs TOOL-dRankedPlan-45

2026-10-27T03:26:41Z rescope · item add TOOL-dRankedPlan-47 · reason spec-audit of TOOL-dRankedPlan-38 to -45 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) id 30 HIGH item H1 (shared with id 1): a heredoc body fed to a $ variable interpreter such as "$py" reaches only the textual rule, so its argv call to ratify.py passes; repairs TOOL-dRankedPlan-45

2026-10-27T03:26:44Z rescope · item add TOOL-dRankedPlan-48 · reason spec-audit of TOOL-dRankedPlan-38 to -45 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) id 8 HIGH item H2: S16 reads JavaScript argv elements from string texts scan_ts_tokens never emits; repairs TOOL-dRankedPlan-45

2026-10-27T03:26:46Z rescope · item add TOOL-dRankedPlan-49 · reason spec-audit of TOOL-dRankedPlan-38 to -45 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) id 33 HIGH item H3: a shell script path bound to a variable and invoked through it is read by no rule; repairs TOOL-dRankedPlan-45, whose S3 resolves bound names for Python only

2026-10-27T03:26:49Z rescope · item add TOOL-dRankedPlan-50 · reason spec-audit of TOOL-dRankedPlan-38 to -45 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) id 34 HIGH item H4: the prefix-command set rests on a false no-tracked-file premise, so timeout and same-file function wrappers pass the ban; repairs TOOL-dRankedPlan-40

2026-10-27T03:26:51Z rescope · item add TOOL-dRankedPlan-51 · reason spec-audit of TOOL-dRankedPlan-38 to -45 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) id 35 HIGH item H5: the op tokens ( ) { } have no reading, so brace groups, subshells and function bodies fail open; repairs TOOL-dRankedPlan-41

2026-10-27T03:26:52Z rescope · item add TOOL-dRankedPlan-52 · reason spec-audit of TOOL-dRankedPlan-38 to -45 round 1 (reviews/2026-10-27-review-TOOL-dRankedPlan-38-spec-audit.md) the 25 MEDIUM and LOW findings batched into one unit: ids 2 3 4 5 6 9 11 12 14 15 16 18 19 20 21 23 24 25 26 27 28 29 31 32 36 (items M1 to M12 and L1 to L11)

2026-10-27T03:48:14Z review · item dRankedPlan-spec-set-r4 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 6 · minors 25 · disposition promote
