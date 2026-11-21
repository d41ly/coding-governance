# TOOL-dPlacedRequest-11 — one compare-and-swap writer for every governance ref, each commit parented on the tip it read, and no lock the lander holds

**Status:** CLOSED · rev-6 · 2026-11-19 · node a · Tier-2 · base c63aabbb · streams tooling · order 1 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0129@30a0ceda whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-build-TOOL-dPlacedRequest-11-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dPlacedRequest-11-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dPlacedRequest-11-chain-rounds.md](../build/2026-11-19-build-TOOL-dPlacedRequest-11-chain-rounds.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-11-arm-breaks.md](../build/2026-11-21-build-TOOL-dPlacedRequest-11-arm-breaks.md) | journal | — |
| [2026-11-21-build-TOOL-dPlacedRequest-11-deviation-647.md](../build/2026-11-21-build-TOOL-dPlacedRequest-11-deviation-647.md) | deviation | — |
| [2026-11-21-build-TOOL-dPlacedRequest-11-deviation-648.md](../build/2026-11-21-build-TOOL-dPlacedRequest-11-deviation-648.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |
| [2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-63 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-52 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

Every lease and claim is written as a commit whose parent is its ref's previous tip, so the remote keeps
the history the design names as the witness (gap-conc-06), and no lease, claim or mail write waits on
or is refused by the lander (gap-conc-07). Today the run claim is a parentless commit
(`tools/unattended/unattended.sh:2419`), and `write_claim` refuses while push-main's marker exists
(`:2415`) and takes `claim-push.lock` (`:2402`), which push-main waits on (`tools/push-main.sh:304`).
Both exist only because the pre-push hook clears the lander's three verdict files on every push
(`.githooks/pre-push:494`), before its ref loop (`:609-617`) knows whether the push carries the
default branch. The two hand copies of the compare-and-swap push, `write_claim` (`unattended.sh:2396`)
and `write_red_ref` (`tools/run-gates/post-merge.sh:275`), become one shared writer first, since this
build adds five more callers of it.

## 2. Scope (IN)

- **S1** — The writer, `write_gov_ref <ref> <expected sha or empty> <src>` (I1), canonical in the new
  `tools/lib/gov-ref.sh` between `# >>> gov_ref_sh` and `# <<< gov_ref_sh`, with byte-identical inline
  copies in `tools/unattended/unattended.sh` and `tools/run-gates/post-merge.sh`. It pushes
  `--porcelain --force-with-lease=<ref>:<expected>` to `GOVREF_REMOTE` through the bounded runner
  named by `GOVREF_RUNNER`, and returns rc 0 written, 1 lost (`(stale info)` or `(fetch first)`), 2 not
  completed, the cause in `GOVREF_WHY`. An empty `<src>` returns 2 with `GOVREF_WHY` reading `no
  source` and pushes nothing, so a failed build captured as `c=$(build_gov_commit …)` is never a
  deletion. The one deletion form is `remove_gov_ref <ref> <expected sha>` in the same block, its
  expected sha non-empty, pushing the empty source through the writer's own push and porcelain read.
  Observed by AC1, AC2, AC3 and AC10.
- **S2** — The parented commit (I2), `build_gov_commit <tip read or empty> <message>` in the same
  block: `commit-tree -p <tip read>` over the empty tree under the fixed `gov-claim` identity, and a
  parentless commit only for a create, when the tip read is empty. When git cannot build it, it prints
  nothing and returns 1; a caller stops on that rc, and S1's `no source` refusal holds where one does
  not. Observed by AC1 and AC10.
- **S3** — The two hand copies become thin adapters. `write_claim` builds its message as today, builds
  the commit through `build_gov_commit "$CW_SHA"`, and writes through `write_gov_ref`, mapping
  `GOVREF_WHY` to `WC_WHY` and keeping its policy lines and its take-over health event.
  `write_red_ref` writes `refs/gov/bar-red` through `write_gov_ref` and `remove_red_ref` through
  `remove_gov_ref`, both keeping `PM_WHY` and their rc contract. Observed by AC1, AC5 and AC8.
- **S4** — The verdict-file clear in the pre-push hook (I3) moves from before the ref loop
  (`.githooks/pre-push:494`) to just after it, and runs only when the loop found the default branch
  (`main_local` non-empty), so a push of a `refs/gov/*` ref, or of any other non-default ref, leaves
  `pre-push-refusal`, `pre-push-bar` and `pre-push-allow` as it found them. A default-branch push
  still clears all three before anything writes one. Observed by AC4 and AC5.
- **S5** — `write_gov_ref` leaves `pre-push-refusal` in place and never names a token as this push's
  cause. The file is one per git dir, and with S6's lock gone another push from the same git dir can
  write it while this call runs, so a token newer than the scratch file the call created just before
  its push (`[ "$rf" -nt "$scratch" ]`) is advisory only: on rc 2 `GOVREF_WHY` appends
  ` · a pre-push refusal was recorded during this push: <token>`. The cause `GOVREF_WHY` names is this
  push's own porcelain reason. The `default-branch` hint, ` · default-branch · fix once: git remote
  set-head <remote> -a`, is added only from this call's own read: the push was declined and
  `git symbolic-ref -q refs/remotes/<remote>/HEAD` prints nothing. `GOVREF_GITDIR` names the git dir;
  empty, it reads no token. Observed by AC4, AC6 and AC9.
- **S6** — The lander lock leaves both kits. Deleted: `write_claim`'s take and release of
  `claim-push.lock` (`tools/unattended/unattended.sh#write_claim`, its `write_dir_lock … claim-push`
  and `remove_dir_lock` lines) with its `busy` branch, `write_claim`'s `push-main-active` test, the
  lander's wait (`tools/push-main.sh#check_claim_push_clear`, `CLAIM_WAIT_CEILING` and their two calls),
  and the arms that observe that take and that wait. Kept, and not deleted: the shared
  `write_dir_lock`, `check_dir_lock_stale`, `remove_dir_lock` and `write_dir_lock_pid`
  (`tools/unattended/unattended.sh#write_dir_lock`), which `init_spec_token_check` takes and releases
  for `spec-tokens.<slug>.lock` and `TOOL-dPlacedRequest-24` S1 moves into `gov_feed_sh`. Edited: only
  their header comment (`tools/unattended/unattended.sh@875eaadf:2646-2677`), which drops the
  `write_claim` sentence, the claim-push clause of the pid rule and the clause naming `until` the field
  the lander's wait reads, and keeps the spec-tokens caller.
  **Readers:** rebuilt from `git grep -n 'claim-push' -- ':!memory'` on 2026-11-19 at
  `unattended.sh` blob `875eaadf`, `unattended.test.sh` blob `72d9634c`, `push-main.sh` blob
  `cd8cf562` and `README.md` blob `1ab759b7`. by name: `tools/unattended/unattended.sh` spells `claim-push.lock`
  in `write_claim`'s take, its `busy` message, and the comments above `write_claim` and the shared
  factory; `tools/push-main.sh` spells it in `check_claim_push_clear` and its comment;
  `tools/push-main.test.sh` spells it in arms 2d and 2e, deleted; `tools/unattended/unattended.test.sh`
  spells it in the GH32 AC6 arm, inverted, the GH36 AC14 block, deleted, and the GH37 blocks and
  TOOL-aPiecewiseGrade-6's AC14 loop, which drive the shared factory with `claim-push` as a test stem
  and stay; `tools/unattended/README.md` spells `claim-push-lock-broken` and
  `claim-push-guard-cleared` in its health-event sentence, which S7 rewrites. by value: NO VALUE
  READERS — the factory composes `<stem>-lock-broken` and `<stem>-guard-cleared` and no file counts
  those two events, and `skills/session-kickoff/manifest-check.sh` counts health-log lines without
  reading an event name. The wait's value, grepped as `git grep -n 'CLAIM_WAIT_CEILING\|claim lock' --
  ':!memory'`: `tools/loop/README.md@76fa1eb8:755`, the waits table's `CLAIM_WAIT_CEILING` row, deleted,
  and `help/loop.md@7c0de7ed:1767`, whose sentence naming the lander's wait on a claim lock is
  rewritten to name no such wait. Observed by AC7.
- **S7** — The records name the parent: the claim block's header (`unattended.sh:2077` at the pinned
  base) and the stops guide's section 7 (`tools/unattended/STOPS.template.md:189`, rendered to
  `memory/guides/UNATTENDED-STOPS.md`) say each claim commit's parent is the ref's previous tip and a
  create is the one parentless commit, and `tools/unattended/README.md`'s health-event sentence drops
  the two `claim-push` events and keeps the `spec-tokens` pair. **Readers:** by name:
  `tools/unattended/README.md` spells `claim-push-lock-broken` and `claim-push-guard-cleared` in that
  sentence, and `tools/unattended/unattended.test.sh`'s GH37 blocks assert both as the factory's
  output under the test stem `claim-push`, which they keep. by value: NO VALUE READERS — no file other
  than the factory's event call writes those two events, and
  `skills/session-kickoff/manifest-check.sh` counts health-log lines without reading an event name.
  Observed by AC7.

## 3. Non-goals (OUT)

- No lease grammar, epoch or verb: `TOOL-dPlacedRequest-1`'s. This unit changes what a claim write
  does, never which ref it names or who may write it; `check_claim_writable`'s table is unchanged.
- No change feed: `TOOL-dPlacedRequest-13` hooks `write_gov_ref`'s one success exit.
- No fenced effect push: the lander's own pushes stay as they are (`TOOL-dPlacedRequest-15`).
- No mail writer: dKeptSession's mailbox ref writes through `write_gov_ref` when it lands.
- The `push-main-active` marker itself stays: the pre-push hook reads it to tell a lander from a raw
  push (`.githooks/pre-push:1222`) and in its run-log lines (`:424`, `:437`).
- A refusal the hook writes on a non-default push still writes `pre-push-refusal`: a declared branch
  bar's `gate-red` and `bar-refused` (`.githooks/pre-push:1147`, `:1161`) and the pre-loop
  `default-branch` refusals (`:575-594`) are read by feature pushes' tests and callers. Such a write
  can still overwrite a lander's refusal in the same git dir; it needs a declared branch bar or an
  unresolvable default branch, and this repository declares no branch bar.
- The claim fast path is not restored here. S2 parents every claim commit after a create, and the
  hook's fast path accepts only `tree 0` with `<sha>^ missing` (`.githooks/pre-push@2aa92a29:1002`), so
  a claim beat pushed alone takes the slow path until `TOOL-dPlacedRequest-34` S24 widens that
  predicate at order 22.

### Edges

- **hands-off** `TOOL-dPlacedRequest-13` — `write_gov_ref`, whose one success exit appends the change feed's event
- **hands-off** `TOOL-dPlacedRequest-1` — `write_gov_ref` and `build_gov_commit`, through which every lease is written parented on the tip it read
- **hands-off** `TOOL-dPlacedRequest-12` — `write_gov_ref`, whose empty expected sha makes each register create-only
- **hands-off** `TOOL-dPlacedRequest-15` — `write_gov_ref`'s porcelain reading and `build_gov_commit`'s parented beat, which the fenced push reuses
- **hands-off** `TOOL-dPlacedRequest-19` — `write_gov_ref`, which writes the request record's ref
- **hands-off** `TOOL-dPlacedRequest-2` — `write_gov_ref`, which writes the card ref per build
- **hands-off** `TOOL-dPlacedRequest-21` — `write_gov_ref`, which writes the claim ref `entry.claim` creates
- **hands-off** `TOOL-dPlacedRequest-14` — `write_gov_ref` and `build_gov_commit`, through which each pre-claim draw row is pushed parented on the tip read
- **hands-off** external — dKeptSession's mail writer calls `write_gov_ref`, so a mail write takes no lander lock either
- **hands-off** `TOOL-dPlacedRequest-33` — `write_gov_ref` and `build_gov_commit` in the driver, through which that unit's `--card-ref write` writes the card ref
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names
- **hands-off** `TOOL-dPlacedRequest-16` — `remove_gov_ref`, the one deletion form, through which `--lease prune` prunes a run's tombstone

## 4. Design

### The block

```
# >>> gov_ref_sh — canonical copy: gov-ref.sh in gov's lib dir (byte-identical; gated)
build_gov_commit() { # tip read or empty · message -> prints the commit; rc 1 when git cannot build it
write_gov_ref() {    # ref · expected sha or empty · src -> 0 written, 1 lost, 2 not completed; GOVREF_WHY
remove_gov_ref() {   # ref · expected sha -> as write_gov_ref, pushing the ref's deletion
# <<< gov_ref_sh
```

The caller sets three names before the call: `GOVREF_RUNNER`, a function taking `<outfile> <git
args…>` that runs git bounded and writes its stdout to the file (the driver's `observe_remote`,
`unattended.sh:480`, and post-merge's `run_remote` over its scratch worktree, `post-merge.sh:241`,
both already have this shape); `GOVREF_REMOTE`, the remote NAME the push names, so the hook observes
`<name>/HEAD` (`unattended.sh:2370-2379`); and `GOVREF_GITDIR`, the git dir whose `pre-push-refusal` a
hook writes. post-merge passes a one-line wrapper that prefixes `-C "$WT"`, since its push runs from
the scratch worktree. The writer:

1. Refuses an empty `<src>`, and `remove_gov_ref` an empty expected sha, with rc 2 and `GOVREF_WHY`
   `no source` or `no expected sha`. Creates its scratch output file, or returns 2.
2. Runs `"$GOVREF_RUNNER" "$f" push --porcelain "--force-with-lease=<ref>:<expected>" "$GOVREF_REMOTE"
   "<src>:<ref>"`, the source empty only when `remove_gov_ref` calls the push.
3. Reads the one porcelain line whose second TAB field ends in `:<ref>`, the pattern
   `?$'\t'*":<ref>"$'\t'*` both copies match today (`tools/unattended/unattended.sh@875eaadf:2796`),
   its trailing CR stripped, and decides as both copies decide: the bound
   firing (rc 124), no status line, or a `!` line without `(stale info)` or `(fetch first)` is 2; a `!`
   line with either is 1; any other flag is 0.
4. On 2, appends ` · a pre-push refusal was recorded during this push: <token>` when the refusal
   file is newer than the scratch file, an advisory only (S5), and the `default-branch` hint with
   `git remote set-head <name> -a` when `git symbolic-ref -q refs/remotes/<name>/HEAD` prints nothing.
5. Removes the scratch file. rc 0 leaves through one exit, the seam `TOOL-dPlacedRequest-13` hooks.

`build_gov_commit` runs `git mktree </dev/null`, then `commit-tree <tree> [-p <tip>] -m <message>`
under `GIT_AUTHOR_NAME=gov-claim`, `GIT_AUTHOR_EMAIL=gov-claim@invalid` and the same committer, the
identity `unattended.sh:2419` already fixes. It calls plain `git`, since post-merge has no `GIT`
wrapper; the driver's two pins (`lib-unattended.sh:61`) govern replace refs and graft advice, neither
of which a commit built from a named tree and parent reads.

### Why the clear can move

push-main clears the three files itself before each of its pushes (`tools/push-main.sh:971`, `:1121`)
and reads them only after that push returns (`check_push_allow`, `write_lander_marker`). The hook's own
clear exists for the attended default-branch push, "so a file an earlier push's hook wrote cannot be
read as this one's answer" (`push-main.sh:970`). Moved after the loop and guarded on `main_local`,
it still runs before every write a default-branch push makes: the writes of the three files all sit
after the loop (`.githooks/pre-push:1147` onward, `:2076`, `:2080`, `:2328`, `:2411`) except the
pre-loop `default-branch` refusals and the signal trap's (`:78`), which overwrite the refusal file
whole. A non-default push then clears nothing, so a claim beat landing mid-bar cannot erase a landing's
verdict, which is the whole reason for the marker test and the lock (NT-19's fold,
`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:672-675`).

### The history this buys

A renew, a take-over and a status write each parent on the tip `check_claim_writable` read (`CW_SHA`),
so `git log <ref>` on the remote lists every holder and beat in order, across take-overs. A lost race
leaves the remote's chain untouched, because the compare-and-swap refuses the push. The claim fetch
(`unattended.sh:2136`) now carries the chain; each commit is an empty-tree commit of under 400 bytes.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/lib/gov-ref.sh` | file | none declared for files |
| `gov_ref_sh` | parity block stem | none |
| `write_gov_ref` | shell function | `write`, OK |
| `remove_gov_ref` | shell function | `remove`, OK |
| `build_gov_commit` | shell function | `build`, OK |
| `GOVREF_RUNNER`, `GOVREF_REMOTE`, `GOVREF_GITDIR`, `GOVREF_WHY` | shell variables | none |

Every function deleted by S6 carries a declared verb (`write`, `check`, `remove`), so
`VERB_OFFENDER_PIN` (`.lexicon.conf:312`) does not move.

### Migration

None for data. A claim written before this unit is a parentless tip; the next write parents on it, so
its chain starts there.

### Rollout

Live on landing for the kits' own repository, where `RUN_CLAIMS` is `on` (`.unattended.conf:162`); dark
for an adopter whose switch is off, as today. The hook change ships to every push-main adopter.

### Files touched (estimate)

- `tools/lib/gov-ref.sh`: the canonical block, new
- `tools/lib/resolve-python.test.sh`: the `gov_ref_sh` parity row
- `tools/unattended/unattended.sh`: the inline block, `write_claim` as an adapter, its lock take and
  the marker test deleted, the shared `write_dir_lock` family kept with its header comment edited
  (S6), the header at `:2077`; the kit
  version is minted by the lander (TOOL-aMendedFleet-65; TOOL-dPlacedRequest-34 S59)
- `tools/unattended/unattended.test.sh`: the GH32 AC6 arm inverted, the GH36 AC14 block deleted, the
  GH37 blocks kept, `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` moved by the diff's count
- `tools/unattended/STOPS.template.md`: section 7's record sentence
- `memory/guides/UNATTENDED-STOPS.md`: its render
- `tools/unattended/README.md`: the health-event sentence
- `tools/run-gates/post-merge.sh`: the inline block, `write_red_ref` and `remove_red_ref` as adapters
- `tools/run-gates/post-merge.sh` is a shipped byte of the run-gates kit, whose version is minted by
  the lander (TOOL-aMendedFleet-65; TOOL-dPlacedRequest-34 S59)
- `tools/push-main.sh`: `check_claim_push_clear`, `CLAIM_WAIT_CEILING` and their two calls deleted
- `tools/push-main.test.sh`: arms 2d and 2e deleted
- `tools/loop/README.md`: the waits table's `CLAIM_WAIT_CEILING` row deleted
- `help/loop.md`: the sentence naming the lander's wait on a claim lock
- `.githooks/pre-push`: the clear moved
- `.githooks/pre-push.test.sh`: the non-default-push arm
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads,
  so `gen_map.py --check` exits 0 after the pass; `TOOL-dPlacedRequest-34` S38 is the final re-check
  only

### Alternatives rejected

- **Keep the lock, add only the parent.** The clause asks for both, and the lock costs a median 334 s
  of blocked claim writes per landing (gap-conc-07).
- **A per-push refusal path the hook takes from the environment.** It adds a public surface to a hook
  shipped verbatim, where the `-nt` test answers the stale-token question with no new input.
- **`build_gov_commit` in the driver only.** Registers, requests and the card ref are written by later
  units in other files, and the lib test is where a probe can source the builder whole.

## 5. Production-readiness checklist

- security — the writer pushes only the ref and source its caller names, under `--force-with-lease`,
  so a stale read can never overwrite; the commit identity stays fixed and publishes no address; the
  hook still gates every default-branch push exactly as before.
- perf / scale — the claim chain grows by one sub-400-byte commit per write and fetches incrementally;
  one `-nt` test replaces a lock directory, a wait loop and up to 120 s of lander delay.
- error / empty / loading states — rc 2 names the bound, the missing status line or git's reason;
  an empty `GOVREF_GITDIR` attributes nothing rather than guessing.
- observability — `GOVREF_WHY` carries git's porcelain reason and, when fresh, the hook's token.
- risks — a refusal a non-default push writes can still overwrite a lander's refusal file (§3).
- testing — the probes of §6 over scratch clones, and the suite arms of §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7, the unattended kit's user page, says the
  claim's history is its parent chain; `help/loop.md` anchors the driver's verbs beside its `--claims` paragraph, and this unit adds no verb.

## 6. Acceptance criteria

- **AC1** — When a scratch clone with a bare origin sources `gov-ref.sh`, sets `GOVREF_RUNNER` to a
  plain runner and `GOVREF_REMOTE=origin`, writes `refs/gov/runs/tFix` from an empty expected sha,
  then writes it again from the first tip through `build_gov_commit <first tip>`, both calls return 0,
  `git -C <origin> rev-parse refs/gov/runs/tFix^` prints the first tip and
  `git -C <origin> rev-list --parents -n1 <first tip>` prints one sha.
  Red when: `build_gov_commit` omits `-p`, so the second tip has no parent.
  fixture: a scratch clone and bare origin under the run's short temp path, built by the probe.
- **AC2** — When the same probe writes from the first tip again after the second write landed,
  `write_gov_ref` returns 1, `GOVREF_WHY` names `stale info`, and the origin's ref still names the
  second tip.
  Red when: the lease is dropped from the push and the stale write lands.
- **AC3** — When the probe writes `refs/gov/runs/tNew` with an empty expected sha while the origin
  already holds it, `write_gov_ref` returns 1; with an empty `<src>` and the current tip expected, it
  returns 2 naming `no source` and the ref is unchanged; `remove_gov_ref refs/gov/runs/tNew <current
  tip>` returns 0 and `git -C <origin> show-ref refs/gov/runs/tNew` prints nothing.
  Red when: an empty expected sha overwrites, or an empty source deletes.
- **AC4** — When the scratch clone's hooks path holds the repository's `pre-push`, its git dir holds
  `push-main-active` and planted `pre-push-refusal`, `pre-push-bar` and `pre-push-allow`, and
  `write_gov_ref` renews `refs/gov/runs/tFix`, the call returns 0 and `git hash-object` of each of the
  three files is unchanged. This is the clause's planted landing holding its lock while a lease renews.
  Red when: the hook clears the files on a non-default push, or `write_gov_ref` removes the refusal file.
  fixture: `git remote set-head origin -a` run once, so the hook resolves the default branch, and
  every probe of AC4, AC5, AC6 and AC9 runs under `env -u GOV_REMOTE -u GOV_DEFAULT_BRANCH`, as
  `tools/unattended/unattended.test.sh@72d9634c:2581` does, so no exported value moves the verdict.
- **AC5** — When the same clone pushes `main` with `GOV_GATE_CMD` naming a red stub, the push is
  refused, `pre-push-refusal` reads `gate-red`, and the planted `pre-push-allow` no longer exists.
  Red when: the moved clear no longer runs on a default-branch push.
- **AC6** — When `GOVREF_REMOTE` names a remote whose `HEAD` is unset, `write_gov_ref` returns 2 and
  `GOVREF_WHY` carries `default-branch` and `git remote set-head`; with a `pre-push-refusal` planted
  older than the call and a push the remote refuses by its own hook, `GOVREF_WHY` carries no token.
  Red when: a stale refusal token is attributed to this push.
- **AC7** — When `grep -n 'claim-push.lock\|check_claim_push_clear\|CLAIM_WAIT_CEILING\|push-main-active'`
  runs over `unattended.sh` and `push-main.sh`, it finds no line in `unattended.sh`, the factory's
  header comment included, and only the marker's own lines in `push-main.sh`;
  `grep -n 'CLAIM_WAIT_CEILING\|claim lock' tools/loop/README.md help/loop.md` prints nothing; and
  `grep -n 'parentless' STOPS.template.md` finds only the
  sentence naming a create as the one parentless commit. `grep -n 'write_dir_lock' tools/unattended/unattended.sh`
  still finds the line defining `write_dir_lock()` and the take `write_dir_lock "$ST_LOCK"`.
  Red when: a lock, a wait or the marker test survives, the guide still calls every claim parentless,
  or the shared factory or its spec-tokens take is deleted with the claim-push lock.
- **AC8** — When `awk` cuts each block from its `# >>> gov_ref_sh` line to its `# <<< gov_ref_sh` line
  in `gov-ref.sh`, `unattended.sh` and `post-merge.sh`, `cmp` finds the three cuts equal, and
  `grep -c '^gov_ref_sh|' resolve-python.test.sh` prints 1.
  Red when: the row is absent, so a drifted copy passes.
- **AC9** — When `GOVREF_RUNNER` names a stub that writes `gate-red` into
  `$GOVREF_GITDIR/pre-push-refusal` and exits 124, so the token lands after the call's scratch file
  exists, `write_gov_ref` returns 2 and `GOVREF_WHY` carries `a pre-push refusal was recorded during
  this push: gate-red`, no `the pre-push hook refused it`, and no `git remote set-head`.
  Red when: a token another push wrote during this call is reported as this push's refusal.
- **AC10** — When the AC1 probe exports a `git` function that returns 1 for `commit-tree` and passes
  every other call to `command git`, and runs `c=$(build_gov_commit <second tip> m); write_gov_ref
  refs/gov/runs/tFix <second tip> "$c"`, `build_gov_commit` returns 1, `write_gov_ref` returns 2
  with `GOVREF_WHY` reading `no source`, and `git -C <origin> rev-parse refs/gov/runs/tFix` still
  prints the second tip.
  Red when: a failed build is pushed as an empty source, so the lease-protected ref is deleted.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `branch-guard self-test` · `straggler-guard arms` · `transition-audit arms` · `push-main self-test` · `measure-legs selftest` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `unattended kit gate` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `scratch-guard self-test` · `tier2-review self-test` · `policy fixtures` · `codebase-map coverage + freshness`

New arm: tools/lib/resolve-python.test.sh · covers AC8 AC10 · the `gov_ref_sh` row's parity loop, staged by a one-byte edit of the post-merge copy, and a failing `commit-tree` stub, staged by a writer that pushes an empty source · none
New arm: .githooks/pre-push.test.sh · covers AC4 AC5 · a non-default push over planted verdict files under `env -u GOV_REMOTE -u GOV_DEFAULT_BRANCH`, staged by restoring the clear above the ref loop · none
New arm: tools/unattended/unattended.test.sh · covers AC1 AC4 · the GH32 AC6 arm inverted to a beat that renews while `push-main-active` exists and leaves `pre-push-refusal` byte-identical, staged by restoring the marker test in `write_claim` · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` fall by the deleted lock arms, counted off the diff · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14, and AC1 and AC4's probes are the observation at landing
New arm: tools/push-main.test.sh · covers none · arms 2d and 2e deleted with the wait they observed, no staged break · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation, 2026-10-25: the tuple holds
  `OPEN`, `SPECCED`, `INPROGRESS`, `BLOCKED`, `DEFERRED`, `CLOSED` and `WONTDO`, and not `DRAFT`.
  Liveness: the tuple would show `DRAFT` if the vocabulary held it. RESOLVED (agent, 2026-10-25,
  delegated): `OPEN`, rung 2.
- **F2 — Does the build's grant cover the pre-push hook and the lander?** Both are governance carriers
  outside `tools/unattended/`, and veto 2 holds them unless the grant lifts it. The clause names "lease,
  claim and mail writes taking no lock the lander holds", which is exactly the hook's clear and the
  lander's wait. RESOLVED (agent, 2026-10-25, delegated): covered, rung 3.
  grants: PLAY-dClosedLoop-3 the moved verdict-file clear in .githooks/pre-push and the deleted claim-push wait in tools/push-main.sh · widens: none · relaxes: none
- **F3 — How does the writer tell this push's refusal token from a stale one, once it no longer
  removes the file first?** (a) The `-nt` test against its own scratch file; (b) the hook writes a
  per-push file named by an environment variable; (c) no attribution at all. (b) adds a public input to
  a hook shipped verbatim, which veto 2 discards outside the grant's clause; (c) drops the
  `default-branch` hint today's callers print. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. A
  token the hook writes in the same filesystem tick as the scratch file reads as stale and is omitted,
  which loses a hint. A token another push from the same git dir writes during this call reads as
  fresh, which the `-nt` test cannot tell from this push's own, so rev-4 prints every fresh token as
  an advisory and never as this push's cause (S5). widens: none · relaxes: none
- **F4 — Where does `build_gov_commit` live?** (a) In the shared block; (b) in the driver beside
  `write_claim`. Units 12, 19, 21 and 2 build gov commits in files the scouts place outside the driver,
  and a probe sources the shared file whole. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3,
  post-merge carrying a function it does not call, which the parity row grades like the rest of the
  block. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 11, scout A row 2 and Shared interfaces
  2, 3 and 9, night-pass-two:276-278 and :672-675, gap-conc-06 and gap-conc-07.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: S1 and S5 reworded so no retirement verb sits
  beside a token they do not retire; S7 gains its **Readers:** clause for the two lock events; §3 gains the
  hands-off to TOOL-dPlacedRequest-14.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-33,
  hands-off TOOL-dPlacedRequest-34, each the mirror of that promoted unit's own edge.
- rev-4 · 2026-11-19 · §2 S5, S6, S7 · §4 The block, Files touched · §6 AC6, AC7, AC9 · §7 · §8 F3 · folds `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit`:
  findings 16 and 33 (H4), S6 deletes only `write_claim`'s take of `claim-push.lock`, its `busy`
  branch, the marker test and the lander's wait, keeps the shared `write_dir_lock` family the
  spec-tokens lock takes, rebuilds its Readers from `git grep`, and AC7 observes the factory kept;
  finding 24 (H6), the kit versions are the lander's to mint; finding 32 (M9), a fresh refusal token
  is advisory and never this push's cause, the set-head hint comes from this call's own read, and AC9
  plants a concurrent token; finding 4 (M3), the unattended.test.sh arm cites README rule 8. §7 also names `scratch-guard self-test`, `tier2-review self-test`, `policy fixtures`, the leg(s) the spec-token guard join names for this spec's Files touched.
- rev-5 · 2026-11-19 · §2 S1, S2, S3, S6 · §3 Non-goals, Edges · §4 The block, Files touched · §6 AC3,
  AC4, AC7, AC10 · §7 · folds `2026-11-19-review-TOOL-dPlacedRequest-13-spec-audit`: finding 28 (H4),
  the one deletion form is `remove_gov_ref`, an empty source to `write_gov_ref` returns 2 `no source`,
  and AC10 stubs a failing `commit-tree`, with the hands-off to TOOL-dPlacedRequest-16 for the prune;
  finding 8 (M3), AC4 to AC6 and AC9 run under `env -u GOV_REMOTE -u GOV_DEFAULT_BRANCH`; finding 20
  (M8), the wait's value readers `tools/loop/README.md` and `help/loop.md` join S6 and AC7; finding 21
  (M9), §7 names the four further legs guarding `.githooks/pre-push` and §3 states the claim fast path
  is lost until TOOL-dPlacedRequest-34 S24; finding 7 (L4), S6 edits the factory's header comment;
  finding 13 (L7), step 3 matches the status line's second field.
- rev-6 · 2026-11-19 · §4 Files touched · §5 · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 16 (M7), the user-docs line names
  `help/loop.md`, which anchors the driver's verbs; finding 17 (M8), this unit's own pass
  regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.

## 10. Reuse audit

The seam extended is the run claim's compare-and-swap push, merged from its two hand copies:
`write_claim` (`tools/unattended/unattended.sh:2396-2462`, push at `:2423`, porcelain parse at
`:2425-2437`) and `write_red_ref` (`tools/run-gates/post-merge.sh:275-300`, push at `:280`), whose own
header says "the porcelain line decides, as write_claim reads it". The copy discipline reuses the
`health_log_sh` precedent: a canonical in `tools/lib/` and the `PARITY_ROWS` loop in
`tools/lib/resolve-python.test.sh:168-233`. `python tools/codebase-map/reuse_lookup.py "compare-and-swap
push of a governance ref with a parent commit"` ranked `build_commit` (`lib-unattended.sh`, the pass
commit, a different commit kind) and `check_claim_push_lock_stale`, the lock this unit deletes; no
ranked symbol pushes a ref by lease, so the two hand copies above are the seam. Scout A's lines were
checked at base and hold, with two corrections: the pre-push clear is the `rm -f` at
`.githooks/pre-push:494`, not `:490`, which defines `PUSH_ALLOW`; and push-main's lock comment and
function span `tools/push-main.sh:294-317`. `python tools/memory-recall/query.py "why does a claim push
take a lock that the lander waits on"` returned TOOL-aGraftedHelix-37's spec and the
TOOL-aGraftedHelix-29 closing review's finding that motivated the lock; neither disagrees with source.

Recall terms used: claim-push.lock push-main-active write_claim pre-push verdict files lander clear parentless commit-tree force-with-lease
