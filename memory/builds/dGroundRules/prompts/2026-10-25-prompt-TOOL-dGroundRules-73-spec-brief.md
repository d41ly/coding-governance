**Serves:** research TOOL-dGroundRules-73

# Spec brief — TOOL-dGroundRules-73, a missing default-branch ref refuses with its own remedy, never rule 7's settings remedy

## The prompt

The closing diff review of this build, round 1 (`memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md`, verdict BLOCKED), confirmed the finding(s) below; each skeptic verdict and fix verdict is in that report and its appendix. Quoted from the report:

> ### H2. With no `origin/HEAD` and a default branch other than `main`, every policy read refuses and rule 7 blocks every spawn with the wrong remedy (id 13)
>
> - **Where:** `tools/policy/policy-shim.sh:104` and `tools/policy/policy.py:480` (`branch = branch or "main"`). The denial is built in `tools/hooks/agent-cap.js` checkSettingsInForce (lines 1795-1800, remedy text at 1791).
> - **What is wrong:** The docs say the landed revision is the tip of the remote's default branch. When `refs/remotes/<remote>/HEAD` is unset and `GOV_DEFAULT_BRANCH` is not exported, the code reads `refs/remotes/<remote>/main`, or `refs/heads/main` with no remote. A repo on `master` with no origin/HEAD therefore names no commit. That is the normal result of `git init` locally and then pushing.
> - **Consequence:** Every policy read exits 2 and agent-cap rule 7 denies every Agent and Workflow call. The denial tells the user to run `python tools/policy/policy.py settings --write`, which has already succeeded and changes nothing. The probe confirmed this. `GOV_DEFAULT_BRANCH=master` or `git remote set-head origin -a` cleared it. help/policy.md:31 and help/agent-limit.md mention neither origin/HEAD nor GOV_DEFAULT_BRANCH. The hook fails closed and a clone sets origin/HEAD, so this is high rather than blocker.
> - **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Keep refusing rather than guessing a branch. Make the refusal from `derive_landed_revision` and from the shim's `landed` verb name the missing ref and the remedy: `git remote set-head <remote> -a`, or export `GOV_DEFAULT_BRANCH=<branch>`. With no remote, name the local default branch and GOV_DEFAULT_BRANCH. In agent-cap rule 7, give a PolicyRefusal its own denial text that prints the refusal's remedy, not `settings --write`. Document origin/HEAD and GOV_DEFAULT_BRANCH in help/policy.md and help/agent-limit.md. Add a policy fixture case for a master-default repo with no origin/HEAD that asserts the hook's denial names that remedy.
> - **Left-shift gate:** That fixture case, plus a rule that every hook denial path has a fixture asserting its remedy text for each distinct cause. A refusal must never share another cause's remedy.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-73.md`, a Tier-1 micro-spec at order 26, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-71.md` follows, that repairs the finding(s) above. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Re-verify each finding's premise at HEAD by reading the code it cites (and a probe where the report's reason ran one); a premise that no longer holds is said so in §4 and dropped from scope, never specced.
2. Spec the fix the report marks SOUND, or, where the finder's fix was judged UNSOUND, the skeptic's corrected fix the report gives. Keep each S-item to one mechanism and name every file it touches; name any reader of a changed value or spelling (grep, not memory).
3. Each acceptance criterion is a probe the pass may run (a direct call of the changed code, a scratch fixture, the module's own single-case runner), never a whole suite or the bar, and carries `Red when:` with a staged break that reds it by name. A suite arm the fix adds or moves goes on a `New arm:` line; the close's main loop observes it red then green.
4. §6 names the legs the touched files owe through `derive_guarded_legs` (not the first guard `--legs-for` prints), plus any unguarded leg that reads them; adjust a floor or a pinned count only where the change moves it, and say which.
5. The report's "Left-shift gate" line for each finding: spec it inside this unit only when it is one small arm of the same mechanism; otherwise name it in §7 as a follow-up the main loop files as an ask.
6. Keep every acceptance code span on one line and free of a `|` the spec-token checker's bar pattern reads as a pipe; no acceptance line starts at column 0 with `AC<n>`; every AC bullet carries `Red when:`; no retirement word in §2; an untracked path sits in a fenced block.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Any other spec; the other findings of the report; the inherited reds the close recorded (unattended shards 1, 3, 5, 7; the hygiene partition arm).

### Limitations
The report was written at `fce5603f8`; units 72 to 78 are specced together and build after, so a line number may move. Cite by symbol where a sibling unit touches the same file: units 73 and 76 both touch `tools/policy/policy.py`, units 75 and 77 both touch `tools/policy/check_policy.py`, units 73 and 78 both touch `tools/hooks/agent-cap.js`.

### Reuse
The code each finding cites, and the fix the report's skeptic checked.
