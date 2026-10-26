**Serves:** research TOOL-dGroundRules-80

# Spec brief — TOOL-dGroundRules-80, the policy fixtures pin the new case's bare remote HEAD and hold the remote refusal variant byte-equal

## The prompt

The closing diff review of this build, round 2 (`memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md`, verdict CLEAN WITH FIXES, exit CONVERGED), confirmed the finding(s) below; the terminal exit promotes every confirmed finding to a unit. Quoted from the report:

> ### M1. The new limit-hook-landed-unread fixture leaves its bare remote's HEAD unpinned, so the policy fixtures leg reds on any node whose init.defaultBranch is main (ids 3, 8)
>
> - **Where:** `tools/policy/check_policy.py:2989-2994`, in the limit-hook-landed-unread case added by TOOL-dGroundRules-73 S5. `run_fixture_git` is at line 4413.
> - **What is wrong:** The case runs `run_fixture_git(bare, "init", "-q", "--bare")` with no initial branch. It pushes only `master`, then runs `git remote set-head <remote> -a`. The bare's HEAD follows the node's init.defaultBranch. Where that is `main`, the bare's HEAD names an unborn `refs/heads/main`, and `set-head -a` fails with `error: Cannot determine remote HEAD` (rc=1). `run_fixture_git` uses `check=True` and passes only user.name, user.email and gpgsign, so no override is applied. Nothing in the policy fixtures isolates git config. `build_limit_repo` already pins its own branch with `symbolic-ref HEAD refs/heads/main` (line 2807), so this bare init is the only branch-sensitive step left unpinned.
> - **Consequence:** On such a node, a CalledProcessError reaches `run_limit_case`'s except. That records `the fixture · CalledProcessError: error: Cannot determine remote HEAD` as WRONG and reds the `policy fixtures` leg of the merge bar, with no product defect. The same happens under a git whose built-in default is `main`. Both skeptics reproduced it in a scratch repo. This node's default is `master`, which is why the close saw the case green. The effect is a false red, not a false green, so the grade is medium.
> - **Fix (skeptics judged SOUND for both findings):** Pin the bare's HEAD to the branch the fixture pushes, either with `run_fixture_git(bare, "init", "-q", "--bare", "--initial-branch=master")` or with `run_fixture_git(bare, "symbolic-ref", "HEAD", "refs/heads/master")` right after the init. To prove it, run `--fixture limit-hook-landed-unread` under `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=init.defaultBranch GIT_CONFIG_VALUE_0=main`, or with `GIT_CONFIG_GLOBAL` pointing at a file that sets it. The case should print WRONG before the fix and 0 wrong after.
> - **Left-shift gate:** The class is `memory/gotchas/fixture-inherits-ambient-machine-state.md`. Make `run_fixture_git` pass `-c init.defaultBranch=<a value no fixture uses>` on every call, or run the policy fixtures leg once under an injected `init.defaultBranch=main`. Either way, any future unpinned `init` reds on every node, not only on the nodes whose config differs.
>
> ### M2. Nothing holds the reader's and the shim's remote-variant refusal byte-equal (id 5)
>
> - **Where:** `tools/policy/check_policy.py:2247`, in `run_mirror_landed_parity` (lines 2227-2263). The two lines it should hold equal are `tools/policy/policy.py:491-494` (the reader's `if remote:` branch) and `tools/policy/policy-shim.sh:108-109`.
> - **What is wrong:** Unit 73 added both fallback refusal variants: no remote, and one remote with no remote HEAD and a default branch other than `main`. The parity arm's new fifth state compares only the no-remote variant by the whole line. In its "one remote" state `origin/main` is pushed and resolves, so the remote refusal is never reached. The remote variant is reached only by limit-hook-landed-unread (lines 2973-2995). That case runs through agent-cap.js, policy-mirror.js and the shim, and checks only two substrings. No fixture or test calls the Python reader's `if remote:` branch at all.
> - **Consequence:** This variant is round 1's H2 headline case, and spec 73 S2 promises the shim prints the reader's line byte for byte. Deleting the reader's `if remote:` branch (it would then print the no-remote remedy) leaves every gate green. So does rewording the shim's remote WHY anywhere outside the two substrings. Gate-side readers would then name a different remedy from the hook's. The two lines are identical today: a read-only probe printed the same `policy: refused · .governance/policy.toml:0 · refs/remotes/origin/main names no commit in this repository, and main is only the fallback: ...` line from both sides. Only spec 73's one-off AC2 diff holds that. The code is correct today and only the gate is missing, so the grade is medium.
> - **Fix (skeptic judged SOUND):** Add a sixth state to `run_mirror_landed_parity`: one remote, no remote HEAD, on master. Re-add FIXTURE_REMOTE after the rename, give it only `refs/remotes/<remote>/master`, and leave `refs/remotes/<remote>/HEAD` unset. Judge it by the same whole-line comparison (`e.strip() == line`). Prove it reds by staging `policy-shim.sh:108-109` back to the bare line.
> - **Left-shift gate:** The class is `memory/gotchas/rule-stated-with-no-check-that-fails.md`. The gate it asks for: every refusal variant that a spec declares byte-equal between the reader and the shim has a whole-line parity state. Adding a refusal branch to either side without a matching state should fail the parity arm's own count.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-80.md`, a Tier-1 micro-spec at order 28, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-79.md` follows, that repairs the finding(s) above. Its write set: tools/policy/check_policy.py (and, if the fix needs it, tools/policy/README.md). Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Re-verify each finding's premise at HEAD by reading the code it cites (and a probe where the report's reason ran one); a premise that no longer holds is said so in §4 and dropped from scope, never specced.
2. Spec the fix the report marks SOUND, or the skeptic's corrected fix where the finder's was judged UNSOUND. Both items edit tools/policy/check_policy.py, so they are one unit; spec them as two S-items.
3. Each acceptance criterion is a probe the pass may run (a direct call of the changed code, a scratch fixture, a single named `--fixture <case>`), never a whole suite or the bar, and carries `Red when:` with a staged break that reds it by name. A suite arm or fixture case the fix adds goes on a `New arm:` line; the close's main loop observes it red then green.
4. §6 names the legs the touched files owe through `derive_guarded_legs`, plus any unguarded leg that reads them; adjust a floor or a pinned count only where the change moves it, and say which. A change to `tools/policy/check_policy.py` grows the `policy fixtures` leg, now sized at budget 970 and ceiling 1290 from a 644s whole run: say whether the growth stays inside that ceiling.
5. §7 "Open questions" reads exactly `none`, with no bullet under it: a bullet outside an F-item there refuses the CLOSED flip at hygiene check 12. Any follow-up goes in the §8 revision log as prose. No line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet carries `Red when:`; keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no retirement word in §2; an untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Any other spec; the other findings of the report; the inherited reds the close recorded.

### Limitations
The report was written at `59f02fde9`; cite sites by symbol as well as line.

### Reuse
The code each finding cites, and the fix the report's skeptic checked.
