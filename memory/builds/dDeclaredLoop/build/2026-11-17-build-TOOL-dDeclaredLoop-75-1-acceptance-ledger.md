# TOOL-dDeclaredLoop-75 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-75

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node `d`
(win32), at rev-10 of the spec, over the working tree: the plants each pass adds or edits, run alone by
`--fixture --plant`, standing in for the `loop budget fixtures`, `loop breakpoint fixtures`, `loop position
fixtures` and `loop guard fixtures` legs; `python -c` probes of the module docstrings, `check_terminal_proof`
and `demand_claimed_requires`, and `govkit.py update --write` over a scratch target, standing in for the
`govkit selftest` arms this pass adds; the docs leg's `--fingerprints` for the usage anchor; the map
generator's write, which left the map unchanged; and `grep` probes. The section 5 sweep re-run at this
pass's base held its design claims: `explain` and `name-only` absent from the two modules, the `ending`
usage row listing `--build=` alone, the protocol row at 68130 PINNED bytes, the lexicon offender pin at
1215 PINNED, the driver's refusal ceiling at 343 PINNED, `SHARED_RECORDS` naming the decision log and the
readme contract, neither written, and no edited path on the kickoff watch line. Its stale figures, and
the one staging step the plants table lacks, are deviation 753.

Owed to the close: every leg section 7 names; AC10 and AC22, each a leg run at another unit's pass commit
in a scratch worktree, which a pass may not run; and the re-price of the four loop legs' rows from the
close's timed readings. Owed RED-first, one per `New arm:` line: the `tools/loop/budget.py` arm
(`unset-driver-root`, `draw-id-rows`' explain step and `patch-claims-unread`), the `tools/loop/breakpoints.py`
arm (the held lines of `pre-placement`, `pre-placement-records-root` and `unattended-root`), the
`tools/loop/position.py` arm (`fetch-other-branch` and `clone-without-reflog`), the `tools/loop/guard.py` arm
(`push-merge-conflict-elsewhere` and `push-merge-tree-fatal`), and the `tools/govkit/selftest.py` arm (the
`[dDL-75] AC14` and `[dDL-75] AC26` checks).

**Evidences:** TOOL-dDeclaredLoop-75
- AC2 — `draw-id-rows` — `python budget.py --fixture --plant draw-id-rows` printed two lines `loop: budget · no draw id · draw · fix-pass · TOOL-tFix-1 · 1/4` after its two identical id-less rows, then `unfrozen 2/4 / unfrozen 3/4 / refused` and `loop: fixture · draw-id-rows · held`, exit 0.
- AC5 — `scaffold_runmd` — a `python -c` print of `budget.__doc__` tested true for `.unattended.conf`, `resolve_memory_root` and `scaffold_runmd`.
- AC6 — `unset-driver-root` — `--plant unset-driver-root` printed `loop: budget · refused · records root: .unattended.conf says memory, .memory-tree.conf says records — the driver writes under memory`, the run-state file's bytes checked unchanged, and `held`, exit 0; `--plant no-own-conf-read` printed `held`, exit 0, its two boundary functions the plant writers.
- AC7 — `ending --build tFix --explain` — the same run's second half printed `loop: budget · root records · from .unattended.conf`, then `loop: budget · read records/builds/tFix/RUN.md`, then the ending line.
- AC8 — `pre-placement-records-root` — that plant printed the `tWrong` held line ending `· root from .memory-tree.conf` and `held`; `--plant unattended-root` printed the `tWrong` held line ending `· root from .unattended.conf` and `held`; `--plant pre-placement` held with the `tNone` line ending `· root from .memory-tree.conf`.
- AC10 — `git worktree add --detach` — OWED to the close: the pass-commit probe runs a leg at each of units 41 to 52, 54 and 55's pass commits, which a pass may not run.
- AC12 — `fetch-other-branch` — `python position.py --fixture --plant fetch-other-branch` printed the ref's line ending `· from reflog`, then `read — FETCH_HEAD · skipped — no line for main of origin`, and `held`, exit 0.
- AC14 — `govkit: update would leave` — `govkit.py update --target <scratch> --write --to HEAD` over a committed receipt claiming `roles` without `loop` exited 2 with one such line, `git status --porcelain --untracked-files=all` printed nothing, `install.json` compared equal to `git show HEAD:.governance/install.json`, and `test -e` of the outbox lock exited 1.
- AC18 — `check_terminal_proof()` — a `python -c` probe on win32 that duplicated `os.devnull` onto fd 2 with `os.dup2` printed `check_terminal_proof() -> None on win32`.
- AC22 — `git worktree add --detach` — OWED to the close: the same probe at units 59 to 63 and 65's pass commits.
- AC24 — `TOOL-aSurfacedLexicon-17` — `grep -n` printed the comment in `tools/memory-tree/gen_build_index.py#derive_parallel_step` and the ask row TOOL-aSurfacedLexicon-26, which names TOOL-dDeclaredLoop-66; `grep -n "ties are the parallel group"` over the map feature printed nothing, exit 1.
- AC25 — `An adopter phase, a member of PHASES_EXTRA` — `grep -c` printed 1 PINNED over the template and 1 PINNED over its render, and the render measured 68288 PINNED bytes CR-stripped, the figure its size row now holds.
- AC26 — `demand_claimed_requires` — a `python -c` call with `unattended` claimed and its two requires unmet raised a refusal naming `'unattended' requires 'review-harness'` and `'unattended' requires 'settings-merge'`, its route `apply --kits unattended,review-harness,settings-merge`; the one-pair call still routes `apply --kits roles,loop`.
- AC27 — `push-merge-conflict-elsewhere` — `python guard.py --fixture --plant push-merge-conflict-elsewhere` held both scenarios, the trailered one exit 0 naming `0 finding(s)` and the untrailered one exit 1 naming the merge and `review.max-rounds`; `--plant push-merge-tree-fatal` held, exit 1, naming `the clean re-merge failed: 128 fatal: fx stand-in`; `push-merge-conflict-pick`, `push-merge-revert-to-unchanged-side`, `push-merge-unrelated-histories` and `push-merge-unparseable-c` still held.
- AC28 — `patch-claims-unread` — `python budget.py --fixture --plant patch-claims-unread` printed `draw · rc 2 · budget: patch draw refused — claims unread: fx: the remote did not answer` and `held`, the record unchanged and no draw counted; `patch-concurrent` still held.
- AC30 — `readme_of` — a `python -c` print of `breakpoints.__doc__` tested true for `README.md`, `$M`, `readme_of` and `.unattended.conf`.
- AC33 — `class-keyed` — `grep -n "class-keyed" README.md` in the loop kit printed one line naming `merge-rows.py` and `union`.
- AC34 — `clone-without-reflog` — that plant printed the ref's line ending `fetched never · core.logAllRefUpdates=false` and `held`; a `python -c` probe wrapping the plant's staging printed `GIT_CONFIG_GLOBAL` naming an empty file directly under the plant's scratch top, `GIT_CONFIG_SYSTEM` the same, and neither set after the plant; the six driver plants and the remote plants each held under the empty configs.
