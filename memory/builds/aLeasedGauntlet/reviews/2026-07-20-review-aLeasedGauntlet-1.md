# Closing adversarial review — TOOL-aLeasedGauntlet-1 (coding-governance port)

**Date:** 2026-07-20 · **Node:** a · **Base:** `d5ada669..HEAD` (branch `feature/leased-gauntlet-a`)
**Harness:** shared with the inCMS closing review (2 lenses over BOTH diffs → skeptic verify); 7
confirmed. Skeptics were told the lighter reconcile-before-gate design + block + no-lease are ratified.

All confirmed findings are diagnostic / robustness / doc; **no correctness or security break**. Folded
in commit `ba603ee` (manifest last-audit re-stamped: touched watched `tools/run-gates.sh`).

| # | Sev | Finding | Resolution |
|---|-----|---------|------------|
| F1 | MED | Lander classified a push failure on origin-movement, not on git's actual output (guard on the wrong signal). | `tools/push-main.sh` classifies on captured `git push` output (`tee` + `PIPESTATUS`), origin-movement as fallback; distinct `unreachable` outcome. |
| F2 | MED | The pre-push hook silently assumed `main` when `origin/HEAD` was unset AND `GOV_DEFAULT_BRANCH` unset → a push to a real `develop`/`master` default BYPASSES the gate (fail-OPEN in a generic drop-in kit); `push-main.sh` reinforced the trap by computing the same wrong def. | Hook and lander now fail CLOSED with a "set `GOV_DEFAULT_BRANCH` / `git remote set-head origin -a`" message when the default is unresolvable. New fixture cases: `pre-push.test.sh` case 6, `push-main.test.sh` case 8. |
| F3 | LOW | SIGKILL can leak the marker (unacknowledged). | One-line comment: soft advisory guard, self-heals, never admits red. |
| F4 | LOW | Dirty tree misreported as a "reconcile CONFLICT". | Clean-tree pre-check → "commit or stash"; new fixture case 7. |
| F5 | LOW | Bootstrap of a fresh remote needs `--no-verify`, undocumented. | Header documents the one-time seed. |
| F6 | LOW | `run-gates.sh` durable-summary guard was dead (always-suffixed path). | Guard on the raw gitdir var. |

**Fixtures set `GOV_DEFAULT_BRANCH=main`** — the scratch repos are `git init`+`remote add`
(origin/HEAD unset), so without the pin the new F2 fail-closed would refuse every gate case; the
fail-closed path itself is exercised by the new cases that unset it.

**Documented (no clean gate fits):** F1's `unreachable`/localized-git fallback; F3 (untrappable).

**Left-shift gates:** F2 → `pre-push.test.sh` case 6 + `push-main.test.sh` case 8. F4 → `push-main.test.sh`
case 7. F1 red/race → existing cases 4/5.

**Verification:** `push-main.test.sh` 8/8 · `pre-push.test.sh` 7/7 · `run-gates.sh` full suite 16/16 GREEN.
