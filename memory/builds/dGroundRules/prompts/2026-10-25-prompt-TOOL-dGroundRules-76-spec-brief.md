**Serves:** research TOOL-dGroundRules-76

# Spec brief — TOOL-dGroundRules-76, `policy.py lists --check` grades the legacy-homes list by the gate arm's rule

## The prompt

The closing diff review of this build, round 1 (`memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md`, verdict BLOCKED), confirmed the finding(s) below; each skeptic verdict and fix verdict is in that report and its appendix. Quoted from the report:

> ### M2. `policy.py lists --check` goes red in every adopter install, and the remedy it prints cannot clear it (id 3)
>
> - **Where:** `tools/policy/policy.py:1365` (`held = argv == ["--check"] or (KIT / LEGACY_LIST).is_file()`), with `check_legacy_homes` at 1189-1201 and the withheld branch at 1397-1401. The disagreeing copy is `check_policy.arm_legacy_homes` (check_policy.py:399).
> - **What is wrong:** `--check` always grades the legacy-homes list, even when it is absent. kit.toml withholds `legacy-homes.txt` from installs, so it is absent in every adopter install. `lists --write` refuses to create it (LEGACY_WITHHELD). The gate arm uses the opposite rule and grades nothing when the list is absent or the tree is an adopter's.
> - **Consequence:** The documented `lists --check` (README.md:131, help/policy.md) exits 1 in every adopter install. It reports every key in `.*.conf` and `.githooks/gate-env.sh` as "stale list ..., re-run lists --write". Running `lists --write` prints "not written" and the check stays red, so the loop has no exit. A probe confirmed it. No gate leg runs `lists --check`, so the damage is limited to a manual command.
> - **Fix (skeptic judged SOUND):** Make `cmd_lists` use the arm's rule. Grade the legacy list only when `(KIT / LEGACY_LIST).is_file()` and `derive_census_tree` answers neither `adopter` nor `invalid`. Otherwise print the LEGACY_WITHHELD note and add no reports. Better, have both call one shared predicate. Add a fixture case that runs `lists --check` against a kit copy with no legacy list and asserts exit 0 with the withheld note.
> - **Left-shift gate:** That fixture case, plus a rule that every documented kit command gets an install-shape fixture: run it against a copy built from kit.toml's install set, so a withheld file is really absent.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-76.md`, a Tier-1 micro-spec at order 26, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-71.md` follows, that repairs the finding(s) above. Author only: no product code, no commit, no gate beyond memory hygiene.

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
