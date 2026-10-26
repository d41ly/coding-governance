**Serves:** research TOOL-dGroundRules-72

# Spec brief — TOOL-dGroundRules-72, the pre-commit policy guard reads the index git hands the hook, so `git commit -a` and `git commit <path>` are graded

## The prompt

The closing diff review of this build, round 1 (`memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md`, verdict BLOCKED), confirmed the finding(s) below; each skeptic verdict and fix verdict is in that report and its appendix. Quoted from the report:

> ### B1. The pre-commit policy guard reads the real index, so `git commit -a` and `git commit <path>` bypass it (id 1)
>
> - **Where:** `.githooks/pre-commit:195`, with the second `git diff --cached` at line 211, and `tools/policy/guard.py:46-51` (`run_git`).
> - **What is wrong:** Line 8 of the hook unsets `GIT_INDEX_FILE`. The new policy-guard block (lines 192-220) runs after that. On `git commit -a` or `git commit <path>`, git hands the hook a temporary index (`index.lock` or `next-index-*.lock`). The block's `git diff --cached` calls and every `git diff --cached` and `:path` read in guard.py therefore read `.git/index` and see nothing staged.
> - **Consequence:** An agent shell (no TTY) that runs `git commit -am ...` or `git commit .governance/policy.toml` commits any change to policy.toml, policy.json, instructions.toml or deploy.toml past the owner-only guard, and the hook exits 0. A scratch-repo probe with the real hook confirmed it. A staged edit was refused (rc=1). The same edit committed with `git commit -qam a` exited 0 and landed. The guard header's "IT STOPS FORGETTING" list (guard.py:19-23) does not name this bypass, and the push bar does not re-check authorship. The class is already named in `memory/gotchas/inherited-git-dir-pins-the-work-tree-to-the-cwd.md`.
> - **Fix (skeptic judged SOUND):** Before line 8's unset, save the index git handed the hook, for example `hook_index=${GIT_INDEX_FILE:-}`, made absolute against the git dir if it is relative. Run the block's two `git diff --cached` calls (lines 195 and 211) and the `"$py" "$g" --staged` call with `GIT_INDEX_FILE="$hook_index"` when it is set, as `gen_build_index.read_staged_paths` already does. Add pre-commit.test.sh arms that edit the guarded path without staging it, run `git commit -am` and `git commit -- <path>` with stderr captured, and expect rc 1. Today's AC9 arms only exercise `git add` followed by `git commit`.
> - **Left-shift gate:** A hook-lint leg that fails any `.githooks/*` block running `git diff --cached` or `git show :path` after the `GIT_INDEX_FILE` unset without re-passing the saved index. Also make the `-a` and `<path>` commit arms mandatory for every staged-reading hook block in pre-commit.test.sh.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-72.md`, a Tier-1 micro-spec at order 26, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-71.md` follows, that repairs the finding(s) above. Author only: no product code, no commit, no gate beyond memory hygiene.

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
