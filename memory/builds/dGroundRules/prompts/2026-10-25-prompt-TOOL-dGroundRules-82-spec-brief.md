**Serves:** research TOOL-dGroundRules-82

# Spec brief — TOOL-dGroundRules-82, a parity row holds policy-mirror.js's bash candidate order against the canonical resolve_bash

## The prompt

The closing diff review of this build, round 2 (`memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md`, verdict CLEAN WITH FIXES, exit CONVERGED), confirmed the finding(s) below; the terminal exit promotes every confirmed finding to a unit. Quoted from the report:

> ### L2. No check fails if the JS resolver and the checker's resolver drift apart again (id 6)
>
> - **Where:** `tools/policy/policy-mirror.js:66`. The claim is in `tools/policy/README.md:322` and the module comment.
> - **What is wrong:** Reverting line 66 to `...onPath` passes every gate. `resolveBash` and `onPath` appear only in policy-mirror.js. No suite, fixture or parity row in `tools/lib/resolve-python.test.sh` compares the JS resolver's candidate order with `resolve_bash`, and no fixture stages a PATH whose first bash cannot see the shim. Spec 78 §6 adds no arm. §8 lists the resolver-order gate only as an ask, and that ask is filed nowhere: not in memory/backlog, not in the build's BACKLOG.md, and not as a gotcha.
> - **Consequence:** The README and the comment claim parity with nothing holding it, so round 1's L2 drift can recur silently. The charter's left-shift rule requires a gate or a checklist entry for every confirmed finding, and this class has neither. Both resolvers run `test -f` on each candidate, so drift only changes which working bash is chosen. The effect is contained, so the grade is low.
> - **Fix (skeptic judged SOUND):** Add the resolver-parity row named in the spec's ask. Put it in `tools/lib/resolve-python.test.sh` or make it a policy fixture case. Stub `spawnSync` as spec 78's AC4 probe does, and assert that resolveBash tries GOV_BASH, then the first PATH bash, then the two Git for Windows paths, then `bash`. The row must red when a second PATH directory holding a bash is tried. If M3's widening fix is taken, assert the widened order instead, on both resolvers. Otherwise, record the class in the project's bug-class checklist.
> - **Left-shift gate:** The row above is the gate. The class is `memory/gotchas/rule-stated-with-no-check-that-fails.md`.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-82.md`, a Tier-1 micro-spec at order 29, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-79.md` follows, that repairs the finding(s) above. Its write set: tools/lib/resolve-python.test.sh, or a policy fixture case if the row cannot live there. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Re-verify each finding's premise at HEAD by reading the code it cites (and a probe where the report's reason ran one); a premise that no longer holds is said so in §4 and dropped from scope, never specced.
2. Spec the fix the report marks SOUND, or the skeptic's corrected fix where the finder's was judged UNSOUND. This unit builds after TOOL-dGroundRules-81, which restores the JS scan of every PATH bash and states the candidate order in its §4; assert that order (read spec 81 at your base) against the canonical resolver's, and red when a candidate is added, dropped or reordered on either side.
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
