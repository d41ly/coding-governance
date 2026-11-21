# TOOL-dPlacedRequest-55 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-55

The unit was built from its spec at rev-3 on base `3b663e72e`. It touches no product file: the
oracle is the block under the spec's "The oracle the close runs" heading, and this pass observes it
on scratch fixture repositories. No gate, suite or bar ran in this pass. The block was cut by `awk`
from the spec into a scratch file under the session scratch and run by `bash` with the fixture's base
as its one argument; spec 44's design-section block was cut the same way. Each fixture repository
sits under `%TEMP%`, is built by the probe and is not held in the tree: a base carrying
`KIT_UNATTENDED_VERSION=1.110` and `KIT_RUN_GATES_VERSION=1.50`, two branch commits (the first
bumping to 1.111, the second `b2`), one default-branch commit, and a merge made as
`tools/push-main.sh#cmd_prepare` makes it, detached at the default-branch tip and `git merge --no-ff`
of the branch with the lander's subject. The stub `git` exits 128 on a `log` carrying `-p` and runs
the real git otherwise, and enters `PATH` as a `/c/…` entry.

**Evidences:** TOOL-dPlacedRequest-55
- AC1 — `KIT_UNATTENDED_VERSION`: on the bump fixture's merge the block printed `version oracle: <t8>^1..<t8>^2 · 2 commits`, then `-KIT_UNATTENDED_VERSION=1.110` and `+KIT_UNATTENDED_VERSION=1.111`, and exited 1; the count is the fixture's two branch commits. (PINNED)
- AC1 — `· 2 commits`: on the same shape with the first branch commit touching another file the block printed the header alone, ending `· 2 commits`, and exited 0. (DERIVED)
- AC1 — `· 2 commits`: spec 44's block on that clean merge printed its header and exited 1, the clean build's non-zero exit the criterion's red names. (DERIVED)
- AC2 — `version oracle: the walk failed`: with the stub first on `PATH`, the block on the bump fixture's merge printed its header, the stub's `fatal:` line and `version oracle: the walk failed`, and exited 2. (DERIVED)
- AC2 — `PATH`: under the same stub the pipe form, the block's walk and grep replaced by `if git log … | grep …; then exit 1; fi; exit 0`, printed the `fatal:` line and exited 0, a dead walk over a bump read as clean, the red. (DERIVED)
- AC2 — `PATH`: under the same stub spec 44's block printed the `fatal:` line and exited 1. (DERIVED)
- AC2 — `PATH`: the pipe form with no stub printed both version lines and exited 1, so the stub's exit is what moved it; with the stub's directory entered as `C:/…` the block printed both version lines and exited 1, the stub never found, as the spec's Evidence says. (DERIVED)
- AC3 — `base does not resolve`: the block on the bump fixture's merge with a base of forty zeros printed `version oracle: base does not resolve` and exited 2. (DERIVED)
- AC3 — `no prepared merge on HEAD`: on the run branch's tip before the merge the block printed `version oracle: no prepared merge on HEAD` and exited 2. (DERIVED)
- AC3 — `no prepared merge on HEAD`: under a branch commit on top of a `merge: dOtherBuild — land onto …` landing made after the base, the block printed the refusal and exited 2; a scratch copy with the subject case cut walked that landing's one commit and exited 0, the red. (DERIVED)
- AC3 — `no prepared merge on HEAD`: on a merge of the default branch into the branch, subject `Merge branch 'main' into run`, the block printed the refusal and exited 2; the copy with the subject case cut walked one commit and exited 0, the red. (DERIVED)
- AC3 — `no prepared merge on HEAD`: under a branch commit whose first-parent line reaches this slug's earlier landing, with the base a default-branch commit after it, the block printed the refusal and exited 2; a scratch copy with the ancestor test cut walked the earlier landing's one commit and exited 0, the red. (DERIVED)
- AC4 — `walked no commit of the build`: on a merge built by `git commit-tree -p <tip> -p <base>` with the lander's subject, its second parent an ancestor of its first, the block printed the header ending `· 0 commits` and `version oracle: walked no commit of the build`, and exited 2. (DERIVED)
- AC4 — `walked no commit of the build`: spec 44's block on the same merge printed the same refusal and exited 1, the status it gives a clean walk, the red. (DERIVED)
- AC5 — `records: close`: with a single-parent `records: close` commit stacked on the bump fixture's merge, the block's header named the merge's `<t8>^1..<t8>^2`, not HEAD's, at `· 2 commits`, both version lines printed, and it exited 1. (DERIVED)
- AC5 — `records: close`: spec 44's block on that shape, with `origin/main` at the merge's first parent, keyed on HEAD's subject and fell to the merge-base form, walking 3 commits, the red. (DERIVED)

## Items diverged

None: each criterion was observed as written, and the block behaved as the spec's Evidence records on every shape.

## Owed at the close

- The legs the spec's Gates section names, run once by the main loop: memory hygiene, spec tokens, lexicon naming predicates, recall floor and recall floor arms. The spec declares no new arm.
- S1, the close's one run of this block on the prepared merge after `--phase VERIFYING` and the last `--prepare`, with the observing run's base.
