**Serves:** research TOOL-dGroundRules-77

# Spec brief — TOOL-dGroundRules-77, guard plants reach the text-shape, key-scope and not-a-count refusals

## The prompt

The closing diff review of this build, round 1 (`memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md`, verdict BLOCKED), confirmed the finding(s) below; each skeptic verdict and fix verdict is in that report and its appendix. Quoted from the report:

> ### M3. No guard fixture plant reaches the text-shape, key-scope or not-a-count refusals (id 10)
>
> - **Where:** `tools/policy/guard.py:172` (the text-shape condition, lines 166-174), the key-scope refusal at line 157 and the not-a-count refusal at lines 161-163. The plants are GUARD_PLANTS in `check_policy.py:2324-2352`.
> - **What is wrong:** None of these three refusals' reason strings appears in any plant. The plants that touch other lines also change a second key, so they return early at line 151.
> - **Consequence:** A probe with the text-shape condition disabled admitted a correctly argued raise beside a rewritten comment line, and every guard-* case stays green over that mutant. An agent commit could then rewrite any comment text in the owner-only policy file. The key-scope refusal holds only because the measured-file check behind it also refuses. The guard behaves correctly today, so this is a coverage gap.
> - **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Add three GUARD_PLANTS rows, each wanting exit 1:
>   1. `guard-other-line`: RAISED + ROW + an edit that adds a comment line not next to the cap, for example `# planted\n` appended after the class row. Needle: "another line of the policy file changed".
>   2. `guard-not-budgets`: first give GUARD_POLICY, and build_guard_repo's committed copy, a trailing `[runtime]\nagents-in-flight = 4\n` table. Then stage `# RAISED 4 -> 6\nagents-in-flight = 6\n` in its place, plus ROW. Needle: "only a cap under budgets.*".
>   3. `guard-not-a-count`: replace SMALL with `"small.md" = "60"\n`, plus ROW. Needle: "is not a count".
>
>   Each must go red against a guard copy with its condition removed.
> - **Left-shift gate:** A reason-string coverage check. Every refusal reason string in guard.py must appear as a needle in at least one GUARD_PLANTS row. A mutation pass that deletes each condition must turn at least one case red.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-77.md`, a Tier-1 micro-spec at order 26, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-71.md` follows, that repairs the finding(s) above. Author only: no product code, no commit, no gate beyond memory hygiene.

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
