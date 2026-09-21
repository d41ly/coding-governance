# TOOL-dDerivedDocket-21 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-21

The drift report now measures against the remote-tracking default branch and prints the base ref and
its sha on every header; govkit's guard partition has a derived `root-conf` class; a new selfcheck
check reds a guarded bar leg whose argv names a declared root conf its guard lacks; and six manifest
rows, three of them also in their descriptors, name their confs. No merge bar, no gate leg and no
suite file ran in this pass. What ran instead, from a scratch root outside the tree:

- the new drift arm's function, lifted from its suite file and run alone over a scratch fixture
  repository with a bare origin, against the kit's report and then against the report at this
  unit's parent;
- the new govkit arm block, lifted verbatim from its suite file and run over scratch gov trees,
  against the unit's `govkit.py`, its parent's, and three staged breaks of the new code;
- `govkit.py selfcheck` over a scratch clone of this tree carrying this unit's edits, clean and then
  with each new guard entry reverted in turn;
- `git grep`, `git show` and `git diff` reads over the tree, the base and `origin/main`.

AC1's hand observation, over the fixture: with local main behind the landed pin raise, equal to
origin, and ahead by an unrelated commit, `--json --check` returned identical signal values and exit
0 with no weakened ratchet in all three. The control, `--base-ref refs/heads/main` in the behind
state, redded naming the weakened ratchet. The report at this unit's parent redded the behind state,
which is the criterion's red case. The suite run is owed to VERIFYING.

AC4's hand observation, over the scratch gov trees: a guard naming the kit's declared `.lexicon.conf`
fell into one class and the tree was green; `.nosuch.conf` beside it redded 7c naming only itself.
Staged breaks: the parent's `govkit.py` redded the first read, and a `root-conf` test admitting any
name without a `/` passed `.nosuch.conf`, which the arm caught. The suite run is owed to VERIFYING.

AC6's hand observation, over the scratch clone: selfcheck exited 0 printing
`guarded bar legs graded 8 · root-conf readers 5`. Reverting any one conf from the five reader
legs' guards, both of `straggler-guard arms`' two among them, redded naming that leg, its conf and
its argv file. Both halves were read again over a fresh clone of the build commit. The real-tree run
is owed to VERIFYING.

AC8's in-pass reads: at the build commit govkit reads 1.12, lexicon 1.6 and codebase-map 1.8. At
`fb07ca25` they read 1.11, 1.4 and 1.7, and at `origin/main` after this pass's fetch, `663a0dec`, they
read 1.11, 1.5 and 1.7, so each value is strictly greater than both. Every lexicon marker, in
`lexicon.py`, `canon.py`, `README.md`, `LEXICON.md` and the re-rendered Skill, reads 1.6. The
codebase-map marker and the regenerated map's generator string read 1.8, and the govkit marker reads
1.12. No drift-audit version line moved, no file under the review harness's directory changed, and
the memory-tree edit touches `kit.toml` alone, with no version line or marker. The version-marker leg
is owed to the post-build bar.

AC9's hand observation, over the scratch clone: the clean run printed no near-miss line naming
`recall floor`. With its `.memory-tree.conf` entry reverted, selfcheck stayed at exit 0 and printed
a near-miss line for `recall floor` naming `.memory-tree.conf` and, through the leg's own imports,
`tools/memory-recall/query.py` and `tools/memory-recall/recall_conf.py`. Both halves were read again
over a fresh clone of the build commit, with the same result. The real-tree run is owed to
VERIFYING.

AC1, AC4, AC6, AC8 and AC9 carry `permission:` lines and get no line here; the orchestrator writes
them after the post-build bar.

**Evidences:** TOOL-dDerivedDocket-21
- AC2 — `git fetch origin` — over the fixture with `origin` configured and its tracking ref deleted,
  the report exited 2 with empty stdout and a refusal naming `git fetch origin main`; with `origin`
  removed it printed `no origin remote, so the base is local main @` and eight hex digits on stderr
  and exited 0; its text headers read `(base refs/remotes/origin/main @ ` and eight hex digits while
  the tracking ref resolved, and `(base refs/heads/main @ ` and eight hex digits without a remote.
  The report at this unit's parent failed each of those reads.
- AC3 — `git grep` — the sweep command with its comment filter, re-run at the build tree, hits 10
  files and 50 lines. Each file is a row of the spec's inventory at rev-6 and each count equals the
  row's build count: two files landed after BASE and gained rows, `tools/push-main.sh` reads 5, and
  the converted report reads 4, which its CONVERT disposition names.
- AC5 — `python tools/govkit/govkit.py selfcheck` — over a scratch gov tree whose guarded,
  repo-subject leg's argv file names `.lexicon.conf` and whose guard lacks it, selfcheck exited 1
  naming `leg 'demo' reads root conf .lexicon.conf` and printed a graded count of 1. With the conf
  in the guard it exited 0, and with the leg moved to chunk `selftests` it graded only the other
  leg. A staged break in which the check read the guard alone, never the argv bytes, passed the
  first tree, and the arm caught it.
- AC7 — `tools/lexicon/kit.toml` — it and `tools/lexicon/adopt-lexicon.sh` now say the conf IS a
  guard pathspec under the `root-conf` class, in the past tense for the old ruling, and say that
  `lexicon wiring` still grades the declaration unguarded; that leg's empty guard and argv are
  unchanged. The same stale sentence in the kit README and a suite comment was rewritten too.
