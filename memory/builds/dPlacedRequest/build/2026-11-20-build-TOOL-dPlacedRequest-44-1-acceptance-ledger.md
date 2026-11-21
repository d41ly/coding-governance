# TOOL-dPlacedRequest-44 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-44

The unit was built from its spec at rev-9 on base `2dba1a194`. Its Files touched names no product
file: the oracle is the spec's section-4 block, spec 43 is CLOSED and untouched, and this pass's
work is the observations below. No gate, suite or bar ran in this pass. Every reading is the
section-4 block cut verbatim from the spec by `awk` into the session scratch and run by `bash`, over
a fixture repository built under the node's short temp path, or over this worktree, or a `grep` of
spec 43.

THE FIXTURE, the reading the lines below cite: a base commit holding
`KIT_UNATTENDED_VERSION=1.110` and `KIT_RUN_GATES_VERSION=2.10`, a run branch of two commits (the
first bumping `KIT_UNATTENDED_VERSION` to `1.111`), one main commit after the branch point,
`refs/remotes/origin/main` set to main, and a detached `--no-ff` merge of the branch onto main with
the subject `merge: dPlacedRequest — land onto origin/main at <R>`, the message
`tools/push-main.sh#cmd_prepare` writes.

**Evidences:** TOOL-dPlacedRequest-44
- AC1 — `KIT_` — the oracle on this branch tip at `2dba1a194` took the merge-base form, printed `version oracle: 9e21ac760dc0a43d6ed007396922722ccee98d57..HEAD · 237 commits` and no `KIT_` line, exit 1 from `grep`; the prepared-merge reading is owed to the close, see below. (DERIVED)
- AC2 — `HEAD^1..HEAD^2 · 2 commits` — the fixture's merge printed `version oracle: HEAD^1..HEAD^2 · 2 commits`, `-KIT_UNATTENDED_VERSION=1.110` and `+KIT_UNATTENDED_VERSION=1.111`; `git log --first-parent --no-merges --format=%s <base>..HEAD` listed `main: after the branch point` alone. (PINNED)
- AC3 — `walked no commit of the build` — on the fixture's main tip the oracle took the merge-base form, printed `· 0 commits` and `version oracle: walked no commit of the build`, and exited 1. (PINNED)
- AC4 — `TOOL-dPlacedRequest-44` — `grep -c 'first-parent'` over spec 43 printed `0`, and its AC24 paragraph, cut by the criterion's `awk` and squeezed by `tr -s '[:space:]' ' '`, names `TOOL-dPlacedRequest-44` on `1` line; spec 43's status reads CLOSED at rev-11. (PINNED)

## Readings beside the criteria

- On the fixture's run-branch tip the oracle took the merge-base form and printed `· 2 commits` and both version lines. (PINNED)
- With one commit planted on top of the fixture's merge it took the merge-base form and printed `· 3 commits` and both version lines. (PINNED)
- A second prepared merge, of a branch holding one clean commit, printed `version oracle: HEAD^1..HEAD^2 · 1 commits` and nothing after it, exit 1 from `grep`: the clean verdict the hand-bump reading departs from. (PINNED)
- The section-4 evidence's 235 commits at `c96319ad2` and this pass's 237 at `2dba1a194` differ by the two commits between them, `4941c2fec` and `2dba1a194`. (DERIVED)

## Items diverged

None.

## Owed at the close

- AC1 — the section-4 oracle on this build's prepared merge, after `--phase VERIFYING` and the last
  `push-main.sh --prepare`, printing `version oracle: HEAD^1..HEAD^2 · <n> commits`, `<n>` at least
  1, and no `KIT_` line; spec 43's AC24 is the same observation.
- The legs the spec's Gates section names, run once by the main loop. The spec names no `New arm:`,
  so no RED-first observation is owed.
