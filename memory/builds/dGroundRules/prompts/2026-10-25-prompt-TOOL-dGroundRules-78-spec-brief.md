**Serves:** research TOOL-dGroundRules-78

# Spec brief — TOOL-dGroundRules-78, the close sweep of the review's M4 and lows: the policy fixtures leg's budget and ceiling, agent-cap.js's rule-7 header, policy-mirror.js's bash resolver order, and the stale "lands dark" waiver and help text

## The prompt

The closing diff review of this build, round 1 (`memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md`, verdict BLOCKED), confirmed the finding(s) below; each skeptic verdict and fix verdict is in that report and its appendix. Quoted from the report:

> ### M4. The policy-fixture leg's budget and ceiling are stale by about ten times (id 11)
>
> - **Where:** `tools/run-gates/selftest-budgets.txt:82` (60s, with evidence "measured 8s ... the fixture's 16 cases") and the leg's 300s ceiling at `tools/gate-legs.json:1843`.
> - **What is wrong:** `derive_cases` now yields 146 cases (136 CASES plus 10 schema-empty). `run_fixture` runs them one after another, each on a fresh git repo. The finder measured one serial `--fixture` run at 566s. The skeptic did not re-run the leg, but the TOOL-dGroundRules-9 ledger already records about 3s per case.
> - **Consequence:** The leg's guard is broad (gate-legs.json:1774-1839), so most builds trigger it. At this cost it overruns its 300s hang bound and is killed, a red that says nothing about the arms. `run-selftests --serial` also goes red on its 60s cost verdict. The effect is a false red, not a false green.
> - **Fix (skeptic judged SOUND):** Re-measure the whole fixture on the calibration node, then size both the selftest-budgets row and the gate-legs ceiling at that reading x1.5, with the evidence restated. Or split the leg, for example moving the budgets-cap and limit cases into their own guarded leg. Or run the independent outcome cases in a bounded pool, so a single leg fits a ceiling that can be evidenced.
> - **Left-shift gate:** Make each budget row's evidence carry its case count. A check compares that count with the leg's live `derive_cases` length and goes red when it drifts past 25%.
>
> ### L1. agent-cap.js's header says a `cwd` in no checkout adds no rule, but rule 7 refuses it (id 7)
>
> - **Where:** `tools/hooks/agent-cap.js:38-39`.
> - **What is wrong:** TOOL-dGroundRules-21 S38 changed this path to a refusal. `checkSettingsInForce` returns a BLOCKED message (around line 1785), and both its own comment (line 1776) and tools/hooks/README.md:213 describe the refusal. The header still describes the old fail-open behaviour.
> - **Consequence:** None at runtime. The next person to change rule 7 may "restore" the fail-open path the header describes.
> - **Fix (skeptic judged SOUND):** Change the header sentence to: "No policy kit beside this one adds no rule; a `cwd` in no checkout refuses, naming it (TOOL-dGroundRules-21 S38)."
> - **Left-shift gate:** Add a bug-class checklist entry for "amendment leaves its other half standing": a unit that changes a rule's behaviour greps the file header and the kit README for the old wording.
>
> ### L2. policy-mirror.js's bash resolver walks every PATH bash, while the checker's resolver it claims to match takes only the first (id 8)
>
> - **Where:** `tools/policy/policy-mirror.js:63` (`resolveBash`, lines 57-70, header claim at line 34) against `check_policy.py:930`, an inline copy of `tools/lib/resolve_bash.py`.
> - **What is wrong:** The JS tries every `bash`/`bash.exe` on PATH in order. The canonical resolver tries only `shutil.which("bash")`, then the two Git for Windows paths, then a bare `bash`.
> - **Consequence:** On a host where only a later PATH bash can see the shim, the hook reads policy but the checker's parity cases (check_policy.py:2271-2272, 3238) cannot. The checker fails loudly ("no bash can see the shim") rather than passing, so the effect is a contained false red.
> - **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Narrow the JS `resolveBash` to the canonical order in `resolve_bash.py`: GOV_BASH, the first `bash` PATH resolves, the two Git for Windows paths, then bare `bash`. Align its comments at lines 34 and 57-58 with that order. Leave `resolve_bash.py` unchanged.
> - **Left-shift gate:** Add a row for the JS resolver to the resolver parity table, so its candidate order is compared with `resolve_bash.py`.
>
> ### L3. The policy kit's playbook waiver and help page still say the kit "lands dark" (ids 12, 14)
>
> - **Where:** `tools/playbook-kit-waivers.txt:15` and `help/policy.md:12-14`.
> - **What is wrong:** The waiver's reason says no consumer reads the policy file until later dGroundRules units re-point one. In this same diff, agent-cap rule 7, budgets.py, check-template-size, check-line-length, the hygiene checks, manifest-check, gotchas, roles, query.py, gen_build_index and the workflow renderer all read it. help/policy.md still promises that "later dGroundRules units re-point each other consumer". Every dGroundRules unit is terminal, and the catalogue's owner column assigns the remaining keys to other builds (dWellOiledMachine, dShippedRelease, dDeclaredLoop and others).
> - **Consequence:** No behaviour changes, because the parity gate compares only the kit name. But the waiver still excuses the charter template from naming a kit that now refuses adopters' Agent and Workflow calls and switches their size caps, and its stated reason is false. The help page misleads adopters about where the remaining consumers come from.
> - **Fix (skeptic judged SOUND on both findings):** Either add the policy kit's `kit:` block to the charter template and delete the row, or rewrite the row's reason to the one that still holds: the kit's charter block belongs to a later build, named with that build's ask. In help/policy.md, replace "Later dGroundRules units" with the owning builds from the catalogue's owner column, or with "later builds".
> - **Left-shift gate:** Give each waiver row's reason a machine-checkable condition, here "no consumer reads X". Have the parity gate re-test it, for example by grepping for a consumer of the policy kit, and go red when the condition no longer holds.
>
> review-shape kind=diff-review round=1 intensity=full at=synth raw=14 confirmed=13 refuted=1 unverified=0 blocker=1 high=2 medium=6 low=4 agents=11 out-tokens=224873

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-78.md`, a Tier-1 micro-spec at order 26, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-71.md` follows, that repairs the finding(s) above. Author only: no product code, no commit, no gate beyond memory hygiene.

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
