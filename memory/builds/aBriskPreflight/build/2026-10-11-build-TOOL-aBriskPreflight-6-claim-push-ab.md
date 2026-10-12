# TOOL-aBriskPreflight-6 — the A/B: the pre-push hook on a claim-shaped push

**Serves:** research TOOL-aBriskPreflight-6

Node `a`, 2026-10-11, the build pass. Spec rev-2. The built hook is blob `50bb07520c29`, the
`.githooks/pre-push` the pass commit carries. The hook before this unit is blob `ecf1712e7567` at
`138b0c457`, written to the scratch dir by `git show`. `.githooks/straggler-guard.sh` is blob
`56c0452cb078` in both, since this unit does not edit it.

## The instrument

`2026-10-11-build-TOOL-aBriskPreflight-6-claim-push.sh`. Its `--setup` made one throwaway clone,
`%TEMP%/bp6`, of this worktree at the spec commit `2dfb826ca`, on a branch of its own. It recorded
`origin/HEAD` as `origin/main`, pointed `core.hooksPath` at the clone's own `.githooks`, and built the
claim the way `write_claim` does: `git mktree` over empty input, then `git commit-tree`. Each `--run`
copies one hook pair over the clone's `.githooks`, appends a host-state line, and feeds
`.githooks/pre-push origin <url>` the one line `refs/gov/runs/x <claim> refs/gov/runs/x <zeros>`.
That run is traced under `2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh` or timed bare.
`2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py` read each trace, given the hook and the
library of that run as the span source.

## The runs (AC1)

The A/B interleaved twice traced, then once untraced. The figure is forks plus execs times the
per-spawn cost from the run's own host-state line, `spawn5` divided by 5.

| Run | Hook | At (UTC) | spawn5 | Pool Paged | CPU | Wall | Forks | Execs | Figure |
|---|---|---|---|---|---|---|---|---|---|
| `before-1` | before | 07:36:48 | 1.09 s | 17855 MB | 43% | 24.2 s | 46 | 33 | 17.2 s |
| `after-1` | built | 07:37:22 | 1.49 s | 17858 MB | 48% | 6.3 s | 9 | 10 | 5.7 s |
| `before-2` | before | 07:37:55 | 1.41 s | 17860 MB | 47% | 17.9 s | 46 | 32 | 22.0 s |
| `after-2` | built | 07:38:21 | 1.47 s | 17863 MB | 57% | 4.7 s | 9 | 10 | 5.6 s |
| `before-u` | before | 07:38:34 | 0.92 s | 17863 MB | 57% | 28.1 s | — | — | — |
| `after-u` | built | 07:39:15 | 2.38 s | 17866 MB | 48% | 11.3 s | — | — | — |

The built hook's figure is 5.7 s and 5.6 s, and its untraced wall is 11.3 s, against the bound of
30 s. At the baseline's 0.75 s per spawn, the 19 spawns cost about 14 s and the 79 before them about
59 s. The baseline's figure at BASE was 45 forks and 31 execs, so main's merge added one fork and up
to two execs to this path before this unit. The host was lighter than at the baseline, so the walls
here are lower than its 53 s for both hooks; the counts do not depend on load.

## The decision is unchanged (AC2)

Every run exited 0 and printed nothing. The clone's push journal holds one END line per run, six
in all, each `rc=0 exit=clean decision=skip-nondefault`.

## The setup is gone (AC6)

`execs by program`, from the two traces of each hook:

| Program | before-1 | before-2 | after-1 | after-2 |
|---|---|---|---|---|
| `git` | 15 | 15 | 9 | 9 |
| `python3` | 4 | 4 | — | — |
| `awk` | 3 | 3 | — | — |
| `cat`, `dirname`, `grep` | 2 each | 2 each | — | — |
| `rm` | 1 | 1 | 1 | 1 |
| `mkdir`, `tr`, `head`, `tail` | 1 each | `tr`, `head`, `tail` 1 each | — | — |

`wall by function` for the hook before this unit names `init_straggler_guard`, `resolve_remote_sh`,
`read_blob_at`, `read_conf_value`, `check_has_delta` and `resolve_python` in both runs. The built
hook's names none of them. Its table still carries a `resolve_kit_dir` row of 0.7 s, which the
instrument charges by line span to the rows after the function's definition, since no python ran.

## The sliced arms (AC3, AC4, AC5, AC7, AC8)

Each slice was a temporary script cut from the suite that owns the arms, run alone, then deleted.

- **The straggler suite**, its prologue, F1, the pre-flip feature push and F3 with S4's two new arms,
  15 assertions, each hook pair copied in as the fixture's hooks. The built hook: PASS. The hook
  before this unit: PASS, so the two S4 arms are refused there too. With S2's predicate replaced by
  `true`: the pre-flip push prints no recipe, the F3 branch lands, both S4 arms land, and the
  did-NOT-run and DEAD PROBE arms see no layer. With the candidate list limited to `refs/heads/`:
  only the tag arm fails. With the shortcut taken when ANY candidate is an empty root: only the
  mixed arm fails.
- **The pre-push suite**, its prologue, the `mirror` fixture and the branch-bar block. With no runner
  placed, the hook before this unit prints `Sanctioned use: GOV_BRANCH_GATE_CMD='bash <the kit
  runner, once the kit root resolves>'`, so the suite now places `run-gates/run-gates.sh` at the
  fixture's root for that arm and asserts the line. Placed, both hooks print `Sanctioned use:
  GOV_BRANCH_GATE_CMD='bash run-gates/run-gates.sh'`, byte for byte. With S3's condition reduced to
  the default-branch test, the line falls back to the placeholder and the new assertion fails.
- **The unattended suite**, its prologue, the claim helpers and the `TOOL-aGraftedHelix-10` hooked
  claim block, with the built hook copied in by the block itself: PASS, 47 assertions, no SKIP.

## What this does not measure

A real `git push`, so git's own cost around the hook is not in the figure. The A/B at BASE's hook,
which the baseline record already holds. And a claim push on a host under the pool leak, where the
spawn cost the figure scales by was 0.75 s.
