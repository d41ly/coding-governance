# TOOL-dDerivedDocket-13 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-13

The shards-to-builds straggler layer: the sourced library `.githooks/straggler-guard.sh` and its
three predicates, the pre-commit refusal and its two notices, the new `.githooks/pre-rebase`, the
per-ref block in `.githooks/pre-push`, the session step in `tools/check-wiring.sh`, the report-only
drift signal `backlog_stragglers`, the declarations the four new surfaces owe, the corrected
`core.hooksPath` premise in five carriers, and the drift-audit kit's one version move.

NO MERGE BAR, NO GATE LEG AND NO `*.test.sh` SUITE RAN IN THIS PASS. Every observation below was
made BY HAND against scratch fixture repositories under the run's scratch root: a git repository per
shape, the real hook files installed through `core.hooksPath`, the real kits copied in, and the real
hook or checker run inside it. The suite this unit adds encodes those same arms and runs at the one
bar the main loop makes when every unit is terminal.

TWO CRITERIA GET NO LINE HERE. AC9's observations are four gate legs over the real tree, and AC14's
`--topology` run invokes a file whose name ends `.test.sh`, which `tools/unattended/gate-guard.js`
denies before VERIFYING. Both are deferred to that run, and the orchestrator writes them after it.
The pass DID make AC9's three pure-git observations, and they hold: the `## The signals` row greps
back at 1, `grep -c 'githooks/pre-commit' tools/install-prefix-waivers.txt` prints 0, and the
`gate_at` probe line carries its `gov:root-fixture` marker with a reason.

THREE DEFECTS THE HAND RUNS FOUND, each fixed before this commit and each recorded in the spec's
rev-7 line: the library's `<rev>:<path>` blob reads were being rewritten by the POSIX-emulation
shell into `refs\remotes\origin\HEAD;.memory-tree.conf`, so every predicate read as dormant against
a fixture that had flipped; the session note's fixed prose carried the words `hooks own-tree`, which
would have made AC12's grep pass over a run where nothing was marked; and the extensionless
`pre-rebase` hook needed its own `.gitattributes` pin, since the `*.sh` rule above it misses one.

**Evidences:** TOOL-dDerivedDocket-13
- AC1 — `git commit --no-verify` — on a fixture whose default branch declares builds mode, a linked
  worktree on the pre-flip branch stages a shard edit and `git commit` exits 1 printing the whole
  relocation recipe, including the `--relocate --as <your-slug>` line rendered at the fixture's own
  derived prefix; the same commit with `--no-verify` exits 0.
- AC2 — `.githooks/pre-commit` — the same worktree commits a README edit at exit 0 with exactly one
  `pre-commit: note —` line, naming the relocation it still owes. The relocation merge is not
  refused: `git merge --no-ff --no-commit` leaves a builds-mode `MERGE_HEAD`, the restored view and
  the RELOCATED row are staged, and the concluding `git commit` exits 0 with no refusal.
- AC3 — `git rebase --no-verify` — `git rebase main` onto the builds-mode default is refused with
  the recipe, whose first step reads MERGE, never rebase or squash; `git pull --rebase origin main`,
  which passes the hook no branch argument at all, is refused the same way; `git rebase --no-verify`
  rebases. A branch whose only change under the archive is a decision-log rotation commits at exit 0
  with the merge-first notice and no recipe, and rebases with no refusal.
- AC4 — `.githooks/pre-push` — pushing a PRE-FLIP, HAS-DELTA feature branch to a local bare remote
  prints the recipe as a notice and the branch lands: `git ls-remote` on the bare repository lists
  it afterwards.
- AC5 — `--repair` — a feature branch carrying an unaccounted transition merge is refused at exit 1,
  and the refusal carries the audit's own lines naming the merge sha and `--repair <merge-sha>`.
  With the RELOCATED row committed the same push lands. With the audit module moved out of both
  trees the push lands and prints one line naming `refs/heads/feat` and saying the audit did NOT
  run. With the module's `read_mode` renamed so its conf reader raises, the push lands and prints
  the DEAD PROBE line naming the same ref.
- AC6 — `--session` — `tools/check-wiring.sh --session` over a shards-mode fixture prints no
  straggler note, only the skip line naming the mode; over the same fixture after the flip, with one
  local straggler, it prints exactly one `note     straggler` line naming `refs/heads/strag` and
  exits 0. Under `--check` the severity is still `note`, the line still names the branch, and the
  run exits 0 — nothing reading a non-zero exit as a refusal learns about a straggler that way.
- AC7 — `straggler-guard.sh` — on a fixture whose default branch is in shards mode the commit and
  the feature push both succeed and print nothing at all from the library. On a second fixture whose
  default branch IS in builds mode, carrying this unit's push hook with no library beside it, a
  feature push lands at exit 0, prints no `pre-push:` line, and the branch reaches the bare remote —
  the adopter that took the push-main kit and not the gov-only library.
- AC8 — `backlog_stragglers` — over a scratch repository holding the drift-audit kit alone the
  signal reports `not_asked` naming the missing memory-tree kit. With the kits installed, one local
  straggler and one that exists ONLY as a remote-tracking ref, it reads value 2 of 3 refs examined,
  `gateable` false, `live` true, and its detail names both `refs/heads/strag` and
  `refs/remotes/origin/elsewhere`. With every branch deleted and HEAD detached it reads value 0,
  `live` false, and carries the inventory's own DEAD PROBE sentence as its detail.
- AC10 — `migrate_backlog.py --recipe` — inside a fixture the engine's recipe and the library's
  `print_recipe` rendering are byte-identical after CR normalisation, both at the fixture's derived
  prefix. A copy of the library with one character changed in the merge-never-rebase line no longer
  compares equal, so the parity arm is falsifiable rather than decorative.
- AC11 — `git commit` — with a remote-tracking default branch in builds mode and the LOCAL default
  branch reset back to its shards-mode commit, a shard edit on a pre-flip branch is still refused
  with the recipe: the observed remote default is read first. In a repository with no remote-tracking
  default and no local branch the library can resolve, the commit succeeds and the library prints its
  named line saying this clone observes no default branch and that nothing was checked.
- AC12 — `core.hooksPath` — one fixture, one linked worktree built through the topology helper, two
  values. Under the relative `.githooks` the worktree runs its own pre-flip hook files and the shard
  edit commits at exit 0 with no refusal — the documented inert case — and `--session` in the primary
  tree names that branch with the `(hooks own-tree)` mark. Under an absolute value naming the primary
  tree's post-flip hooks the same worktree's next shard edit is refused with the recipe.
- AC13 — `repo-global` — `git grep -n -i` for that word over the push hook, the wiring checker, its
  suite and the gotcha tree prints nothing, and `git grep -c` for the pinned sentence's
  config.worktree phrase prints exactly one hit in each of the four carriers. The gotcha's
  description no longer states the retired premise and its index row was regenerated from it.
- AC15 — `KIT_DRIFT_AUDIT_VERSION` — the constant reads 1.12, strictly above the 1.10 every carrier
  holds at `fb07ca25` and above the 1.11 `git show origin/main:<carrier>` prints after this pass's
  fetch, for the constant, the README marker and both harnesses' `version:` fields. Every file the
  spec's S11 names carries `gov:kit drift-audit@1.12` at least once, and a repo-wide grep over the
  kit and the two harnesses prints no other value. The `kit version markers` leg itself runs at the
  one post-build bar, as this criterion's permission line states.
