# TOOL-dDerivedDocket-37 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-37

**Evidences:** TOOL-dDerivedDocket-37
- AC7 — `grep -c '^arm "' tools/check-spec-tokens.test.sh` — prints 51 at the build commit, and
  `grep -m1 '^FLOOR_ASSERTIONS=' tools/check-spec-tokens.test.sh` prints `FLOOR_ASSERTIONS=55`.
  Both are the criterion's figures: 38 `arm` calls at `fb07ca25` plus the 13 this unit adds over
  §7's six rows in the distribution AC7 states — two each for the graded edge, the bullet shape and
  the counted silence, three each for the dated key and the edge-keyed waiver, one for the H1 join
  at any depth — and 42 plus those 13 for the pin. The four direct assertions outside `arm` are
  untouched, at `tools/check-spec-tokens.test.sh:275`, `:453`, `:455` and `:457` after this diff
  moved them down from the `:265`, `:443`, `:445` and `:447` AC7 read at `fb07ca25`, so 51 + 4 = 55 is
  the count AC10 will read from the suite's own print
- AC11 — `wc -c < memory/guides/SESSION-KICKOFF.md` — reads 20057 at this unit's commit and 20057
  at its parent, so the carrier is no larger; and `git diff --numstat` over that path between the
  same two commits reports `1	1`, one line added and one removed. The whole edit to that file is
  the `last-audit:` line at `memory/guides/SESSION-KICKOFF.md:5`, rewritten IN PLACE with this
  node's real local time and the merge-base sha, which is `fb07ca25048d6dea4ff93a69c565fce1289acec8`
  and did not move. No §B claim was edited: the manifest's `.memory-tree.conf`-derived claims name
  `STREAMS_CUTOFF` and the acceptance-ledger cutoff, and this unit moved neither. Both readings were
  taken in the pass against the staged tree, which is byte-identical to the commit; the criterion's
  own resolution is by sha rather than by `HEAD^ HEAD`, so a later fix-up in this pass would not
  disturb it

## What this ledger does NOT evidence, and why

AC1 to AC5, AC9 and AC10 are NOT observed here. Every one is a `tools/check-spec-tokens.test.sh`
invocation, and each carries a `permission:` line placing its run at the build's ONE post-build bar,
spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` — the `spec-tokens
self-test` leg is HELD, so a plain bar does not cover it. AC6 and AC8 are not observed here either:
each carries the build brief's owner rule that a unit pass runs no gate and no hand-run checker, so
AC6's `python tools/check-spec-tokens.py` over the tree is the orchestrator's run after this commit
and AC8's `kickoff-manifest ratchet` leg is the post-build bar's. The orchestrator writes those
nine lines after the runs that make them.

## What WAS checked directly in the pass

A pass with no observation at all is worth saying plainly about, so here is what ran, all of it the
sanctioned direct check: the checker this unit changes, over FIXTURE scratch repositories built
under this run's scratch root, never over the tree and never through the suite file.

**Six fixtures, thirteen states, every one of them the state an arm stages.** A scratch builder
reproducing the six repositories the new arms build — the same `write_handoff_spec` preamble, the
same `SPEC_HANDOFF_CUTOFF` in each repo's own `.memory-tree.conf`, the same filenames derived from
that key — was run against each state in turn and its stdout captured per state. The thirteen
`arm` lines' expected exit codes and substrings were then read out of the tracked suite AS DATA and
compared against those thirteen captured outputs: all thirteen agree, which is a transcription
check on the arms rather than a run of them. The graded states print
`1 bullet(s) graded in live spec(s) · 1 payload token(s)`, the silent states `1 silent` and
`2 silent`, the blank key `SPEC_HANDOFF_CUTOFF blank (arm off)`, and the malformed key
`REFUSING — SPEC_HANDOFF_CUTOFF 2026-9-14 is not an ISO date`.

**Every `Red when:` these criteria name was STAGED INTO A COPY of the checker and observed RED**,
before the arms were written, because a gate seen only to pass is an assertion about nothing. Seven
breaks, each against the fixture whose arm is meant to catch it, each producing the wrong verdict:
the join reading the SOURCE instead of the target (AC1 state 1 fell to rc 0); the bullet's first
line only (AC2 state 1 fell to rc 0, `0 payload token(s)`); a bullet shape narrower than check 12's
(AC2 state 2 fell to rc 0, `0 bullet(s) graded`); absence redding as disagreement (AC3 state 1 rose
to rc 1 with `0 silent`); the target joined by FILENAME rather than H1 (AC9 fell to rc 0, `1 silent`);
the key read through `read_conf_key` rather than `read_cutoff_key` (AC4 state 3 fell to rc 0, set
and grading nothing); and the waiver keyed on the BARE TOKEN, which took AC5 state 3 to rc 0 with no
key printed. That last break is why AC5's third arm asserts a printed key and a FORBIDDEN
`STALE WAIVER` rather than an exit code: the defect reaches rc 1 by the wrong route.

`bash -n` on the suite and an `ast.parse` on the checker were run in the pass as well.

## The key was RE-DERIVED at the build commit, and the spec moved with it

S3 orders the relation re-run at the build commit rather than carried. It was, on node `d` on
2026-09-21 before any file was written: (a) the newest spec filename date over every local and
remote ref and, at any depth, over every `git worktree list` worktree is 2026-09-20; (b)
`git log -1 --format=%cs` is 2026-09-21. The later is 2026-09-21, so the relation returns
2026-09-22, and rev-4's 2026-09-21 would have EQUALLED the setting commit's own day instead of
sitting past it. S3's three carriers moved together in this commit, per its own checklist, and
rev-5 logs it. Nothing else about the unit changed: the key still postdates every spec of this
build, so the day-one zero population S6 and AC6 describe is exactly as specced.
