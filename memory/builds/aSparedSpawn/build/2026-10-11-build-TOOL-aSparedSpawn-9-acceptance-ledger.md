# Acceptance ledger — TOOL-aSparedSpawn-9

**Serves:** journal TOOL-aSparedSpawn-9

Node `a`, 2026-10-12, git 2.54.0.windows.1, bash under MSYS, Python 3.14. The pass ran no bar, no
suite, no held leg and no slice of a suite. The observations below come from the instrument committed
beside this ledger, `2026-10-12-build-TOOL-aSparedSpawn-9-direct-checks.sh`, run over hand-built
repositories in a scratch root, and from reading the eighteen converted sources. `bash -n` passed on
the ten converted shell suites and the instrument, and an `ast.parse` of the eight converted Python
sources passed. Every criterion whose witness is a suite run is owed at VERIFYING and says so.

One fact the reading turned up that the spec did not state: node `a`'s `core.autocrlf=true` comes from
the SYSTEM file (`C:/Program Files/Git/etc/gitconfig`), not a global one. So every fixture that set no
`core.autocrlf` of its own used to run at `true` here, and now runs at `false`, the value Linux CI
already sees. That is the leak §4 names, now closed. The one combination no environment has run
before is a CRLF file written on Windows and then committed at `false`. The CRLF can come from a
Python text-mode write with no `newline=`, which occurs in the row-grammar, drift-audit and lexicon
selftests, or from a `cp` of this tree's CRLF working copy. Such a blob now keeps its CR. AC5's
inventory compare at VERIFYING is the observation that settles it.

**Evidences:** TOOL-aSparedSpawn-9
- AC1 — `direct-checks.sh` — under a scratch `HOME` whose `.gitconfig` sets `core.autocrlf = true`
  and the exported `GIT_CONFIG_COUNT` triple, a `git init --template=` repository read `false` from
  `git config --get core.autocrlf`, and `git config --local --get core.autocrlf` exited 1. The control
  read without the triple, on the same repository, printed `true`.
- AC2 — `direct-checks.sh` — `grep -nE 'config (user\.(email|name)|core\.autocrlf)'` and its Python
  spelling over the eighteen converted sources found no hit, so §4 keeps no site. The predicate was
  observed red on a staged break file carrying one shell and one Python write. A comment in
  `run-gates.test.sh` that named a `git config user.email` write which no longer exists was reworded.
- AC3 — `direct-checks.sh` — a `git init --template=` repository held 0 `*.sample` files where the
  default init held 14, and every fixture init in the converted sources spells `--template=`. Two
  inits are kept without it: the pre-push suite's arm 17 runs `git init` under an injected `GIT_DIR`
  on purpose, because that init is the subject the arm reproduces rather than a fixture. Three
  fixtures wrote into `hooks/` or `info/` that no template now creates, so each gained a
  `mkdir -p` first: push-main's `pre-receive`, and the pre-push suite's `b1` and `h49` excludes.
- AC4 — `direct-checks.sh`, the mechanism only — a seed built once and copied twice with `cp -a`
  gave both copies one HEAD, a commit in the first copy was absent from the second, the two `.git`
  directories were distinct, and the copy kept the pre-commit hook at mode `100755`. The criterion's
  own witness, two `newrepo` calls in one check-wiring run, is OWED at VERIFYING (one run of
  `tools/check-wiring.test.sh`).
- AC5 — not run — the arm labels and final assertion count of each converted suite at base
  `22efab65` and after the pass are OWED at VERIFYING, the owner's manual run of the merged tree. No
  arm was added, moved or removed in this pass. Two fixtures behave differently on node `a` by
  construction. The run-gates canary's ceiling scratch repository now has its `base` commit, because
  node `a` has no identity and that commit used to fail there. push-main's two racer clones now commit
  as the suite's identity rather than `r`, and no arm reads an author.
- AC6 — `direct-checks.sh`, and reading — no converted source runs `status`, `diff` or `add` through
  `git -C` or `cd` into `$ROOT`, `$REPO`, `$SRC` or `$ROOT_ABS`. The host-tree reads that remain are
  `rev-parse`, `ls-files`, `check-attr` and `show`, and none of them hashes a working-tree file. The
  evidence suite runs the runner over this tree only under a scratch bare `GIT_DIR`, so this
  repository's own index and config are never read under the exported value. The predicate was
  observed red on the staged break file.
- AC7 — not run — a `PS4='+ ' bash -x` count of traced `git` execs per converted suite before and
  after is OWED at VERIFYING, one traced run per suite per side. The Python selftests need a
  git-counting stub on `PATH` instead of a trace.
