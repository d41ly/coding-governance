# TOOL-dPlacedRequest-11 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-11

The unit was built from its spec at rev-6 on base `9fdc501a`. Each criterion below was observed by a
probe of this unit's own code over a scratch clone and bare origin under the node's short temp path,
every hooked probe under `env -u GOV_REMOTE -u GOV_DEFAULT_BRANCH`. No gate, suite or bar ran in this
pass; the arms the spec's §7 declares and their RED-first observations are owed at the close.

**Evidences:** TOOL-dPlacedRequest-11
- AC1 — `tools/lib/gov-ref.sh` sourced, `GOVREF_RUNNER` a plain runner, `GOVREF_REMOTE=origin`: the
  create from an empty expected sha and the second write through `build_gov_commit <first tip>` both
  returned 0; `rev-parse refs/gov/runs/tFix^` on the origin printed the first tip, and
  `rev-list --parents -n1 <first tip>` printed one sha.
- AC2 — a third write from the first tip returned 1, `GOVREF_WHY` read
  `lost the race on the lease: [rejected] (stale info)`, and the origin still named the second tip.
- AC3 — an empty expected sha over an existing `refs/gov/runs/tNew` returned 1; an empty source with
  the current tip expected returned 2 `no source` and left the ref; `remove_gov_ref` with an empty
  expected sha returned 2 `no expected sha`; with the current tip it returned 0 and `show-ref` printed
  nothing.
- AC4 — with the repository's `pre-push` as the clone's hooks path, `push-main-active` and the three
  planted verdict files in its git dir, the renew returned 0, the three files hashed as before, and the
  new tip's parent was the first. Against the hook at base, the same probe found all three removed.
  Through the driver itself (sourced, `write_claim` called): the renew under the marker returned 0,
  the files were byte-identical, the tip was parented on `CW_SHA`, and no lock directory was made.
- AC5 — a `main` push with `GOV_GATE_CMD` naming a red stub was refused, `pre-push-refusal` read
  `gate-red`, and the planted `pre-push-allow` was gone.
- AC6 — with `origin/HEAD` unset, the hooked write returned 2 carrying `default-branch` and
  `git remote set-head origin -a`; with a refusal planted older than the call and a push the origin's
  `pre-receive` refused, `GOVREF_WHY` read `the push was refused: [remote rejected] (pre-receive hook
  declined)` and carried no token.
- AC7 — the spec's greps: no line in `unattended.sh`; only `marker="$gd/push-main-active"` in
  `push-main.sh`; nothing in `tools/loop/README.md` or `help/loop.md`; `parentless` in
  `STOPS.template.md` only in the sentence naming a create; `write_dir_lock()` and the take
  `write_dir_lock "$ST_LOCK"` still found.
- AC8 — `awk` cuts of the block from `gov-ref.sh`, `unattended.sh` and `post-merge.sh` compared equal
  by `cmp` (75 lines), and `grep -c '^gov_ref_sh|' resolve-python.test.sh` printed 1. The parity loop, (DERIVED)
  run alone over that row, passed, and failed naming `post-merge.sh` under a one-byte edit of its copy.
- AC10 — a `git` function failing only `commit-tree`: `build_gov_commit` returned 1 and printed
  nothing, `write_gov_ref` returned 2 `no source`, and the origin still named the second tip. The new
  lib-suite arm 2n, run alone, passed, and failed under a writer that pushes an empty source.
- AC9 — a runner stub writing `gate-red` into `$GOVREF_GITDIR/pre-push-refusal` and exiting 124:
  rc 2, `GOVREF_WHY` read `the push was killed by this kit's own bound · a pre-push refusal was
  recorded during this push: gate-red`, with no `the pre-push hook refused it` and no
  `git remote set-head`.

post-merge's adapters, extracted from the shipped file and driven from a scratch worktree:
`write_red_ref ""` created `refs/gov/bar-red`, an empty `PM_PUSH_SRC` returned 1 with `PM_WHY`
`no source` and left it, and `remove_red_ref <sha>` deleted it.

## Owed at the close

- The four `New arm:` lines of the spec's §7, each RED-first: `tools/lib/resolve-python.test.sh`
  (the `gov_ref_sh` parity row and arm 2n), `.githooks/pre-push.test.sh` (case 8b, staged by restoring
  the clear above the ref loop), `tools/unattended/unattended.test.sh` (the inverted GH32 AC6 arm,
  under README rule 8's waiver) and `tools/push-main.test.sh` (2d and 2e deleted, no staged break).
- The legs §7 names, run once by the main loop.
