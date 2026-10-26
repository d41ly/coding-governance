**Serves:** research TOOL-dGroundRules-75

# Spec brief — TOOL-dGroundRules-75, a cap of 0 is unchecked in every enforcer, as the budgets switch says

## The prompt

The closing diff review of this build, round 1 (`memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md`, verdict BLOCKED), confirmed the finding(s) below; each skeptic verdict and fix verdict is in that report and its appendix. Quoted from the report:

> ### M1. A cap value of 0 means "unchecked" in the budgets switch, but most enforcers read it as a 0 ceiling or as the old constant (ids 2, 4, 5)
>
> - **Where:** The contract is in `tools/policy/budgets.py` (`check_cap` ~309-310 reads 0 as unchecked, and `check_budgets` ~349-350 accepts 0 as valid) and in `help/size-caps.md:77`. The enforcers that disagree:
>   - `tools/check-template-size.sh:254` compares `[ "$bytes" -gt "$MAX_BYTES" ]` itself (MAX_BYTES read at line 207). Its prose check (check 6, lines 236-244) treats 0 as a declaration (id 2).
>   - `tools/roles/handoff.py:518` (`cap = cap or ROSTER_LINE_MAX`), `tools/memory-recall/query.py:1288` (`a.value or EXPORT_CAP`) and `tools/playbook/render_playbook.py:688` (`a.value or ONE_LINE_MAX`) turn 0 back into the constant (id 4).
>   - `skills/session-kickoff/manifest-check.sh:1339-1341` assigns 0. Check 7 at 1359 does `-gt 0`, and check 8's awk at 1380 (`length(ln) > cap+0`) flags every non-empty line (ids 4, 5).
>   - `tools/memory-tree/check-memory-hygiene.sh:528`: `read_cap_modes` evals a policy-layer 0 straight into GUIDE_CAP_BYTES, ENTRY_CAP_CHARS and the other byte and char caps. The zero-refusal at lines 196-208 guards only the conf layer, so the check 6 and check 7 awks compare against 0 (id 5).
>   - Only gotchas.py's `if budget:` reads 0 as unchecked.
> - **Consequence:** `budgets.<cap> = 0` passes `policy.py check` but is never "unchecked" anywhere except gotchas. Roster-line, recall-export and one-line still enforce the old constant, and still refuse under `refuse`. Any manifest cap, any hygiene byte or char cap, or any template-size subject at 0 breaches on every file or line, and so refuses under `refuse` or warns on everything under `warn`. Template-size's failure quotes budgets' own "BUDGET OK ... unchecked" verdict inside it. The `budgets-zero-cap` fixture plants only `index-lines`, where the awk already guards `cl>0`. Every effect is a spurious refusal or a stale constant, never a false pass. Finding 5's finder graded it high. The skeptic graded it medium, and that grade binds.
> - **Fix (finding 2's fix was judged SOUND; findings 4 and 5 had their fixes judged UNSOUND, so the skeptics' corrected fixes are given here):**
>   - Treat 0 (and None) as unchecked in every enforcer, as `check_cap` does. In handoff, query and render_playbook, skip the comparison when the value is 0, or route the verdict through `budgets.check_cap`.
>   - In the hygiene awks, guard check 6 with `ob = cb>0 && sz>cb` for every class and check 7 with `cap>0 && length(line) > cap`.
>   - Skip manifest-check checks 7, 8 and 11 when the value is 0.
>   - In check-template-size, skip check 2 and the prose check (check 6) when MAX_BYTES is 0, and print the unchecked line. Its OK line at line 347 must print "unchecked" rather than divide by MAX_BYTES. Better, let the `budgets.py check` verdict's exit code and refuse flag decide the breach, so the shell keeps no comparison of its own.
>   - Add a CAP_CASES plant per cap: value 0 under `refuse`, an oversized subject, and an assertion of exit 0 with no awk error. Add `index-bytes`, `entry-chars` and a manifest cap to the `budgets-zero-cap` fixture. Add a template-size test arm with a 0 policy value under refuse mode that expects exit 0.
> - **Left-shift gate:** The per-cap zero plant above, derived from the census so a new cap cannot join without one. This is the C6 "two answers to one question" and C8 "check grades one layer of a layered config" classes. Where no gate fits, add an entry to the bug-class checklist: an enforcer must take the switch's verdict, not re-derive it.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-75.md`, a Tier-1 micro-spec at order 26, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-71.md` follows, that repairs the finding(s) above. Author only: no product code, no commit, no gate beyond memory hygiene.

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
