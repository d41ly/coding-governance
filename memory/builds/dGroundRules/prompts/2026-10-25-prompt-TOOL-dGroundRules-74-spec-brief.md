**Serves:** research TOOL-dGroundRules-74

# Spec brief — TOOL-dGroundRules-74, the writer-split fallback arm the closed specs TOOL-dGroundRules-25, -30 and -34 claim

## The prompt

The closing diff review of this build, round 1 (`memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md`, verdict BLOCKED), confirmed the finding(s) below; each skeptic verdict and fix verdict is in that report and its appendix. Quoted from the report:

> ### H1. No arm reaches the writer-split fallback, while three closed specs say one does (id 9)
>
> - **Where:** `tools/workflows/check-protocol-parity.test.sh:593`. The fallback is `WRITER_SPLIT=0` at lines 482-497 and 579-600.
> - **What is wrong:** No suite stages an agent-cap hook that refuses the writer split and then runs `--render`. TOOL-dGroundRules-25 AC18, TOOL-dGroundRules-30 AC1/AC4 and TOOL-dGroundRules-34 AC6 all record an arm in this file covering it. The only arm that watched the outcome, the KIT_AGENT_CAP_VERSION arm, was removed by 93e4b4d31 and not replaced.
> - **Consequence:** An adopter whose installed hook predates `gov:fixed-writers` takes this path: three literal-span substitutions, the `_ub_why` reason extraction, the stderr notice and the exit-2 "denies the fallback too" branch. A regression in any of these ships with every gate green, because gov's own tree always takes `WRITER_SPLIT=1`. The closed specs claim coverage that does not exist, which will mislead the next change.
> - **Fix (skeptic judged SOUND):** Add the arm the specs name, for example in unattended-build.test.sh's build_layout section. (a) Copy the hook with WRITER_MARK changed to another string and run `--render`. Assert rc=0, stderr carrying `govkit update --kits agent-cap`, and a rendered unattended-build.js carrying `cap = 5)`, `const SPEC_WRITERS = 5` and `// gov:fixed-verifiers` on the split. (b) Replace the hook with one that exits 2 on every script. Assert rc=2, the "denies ... fallback too" line, and an unchanged harness file. Raise that suite's floor to match.
> - **Left-shift gate:** A spec-to-arm check at a unit's close. Every "New arm: <file> · covers ACn" line in a CLOSED spec must match an arm label in that file, and removing an arm that a closed spec cites goes red.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-74.md`, a Tier-1 micro-spec at order 26, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-71.md` follows, that repairs the finding(s) above. Author only: no product code, no commit, no gate beyond memory hygiene.

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
