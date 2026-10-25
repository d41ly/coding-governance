**Serves:** research TOOL-dGroundRules-81

# Spec brief — TOOL-dGroundRules-81, policy-mirror.js resolves every PATH bash that can see the shim again, and its comment and refusal say what it does

## The prompt

The closing diff review of this build, round 2 (`memory/builds/dGroundRules/reviews/2026-10-25-review-TOOL-dGroundRules-72-79-closing-diff-round2.md`, verdict CLEAN WITH FIXES, exit CONVERGED), confirmed the finding(s) below; the terminal exit promotes every confirmed finding to a unit. Quoted from the report:

> ### M3. The L2 fix narrows the JS bash resolver to the first PATH bash, so a host whose first bash is the WSL launcher now resolves none (id 9)
>
> - **Where:** `tools/policy/policy-mirror.js:66` (`onPath[0]`). The comment is at line 56 and the refusal text at line 80.
> - **What is wrong:** Round 1's L2 fix turned `...onPath` into `onPath[0]`, so only the first bash on PATH is tried. After it come only the two hardcoded `C:/Program Files/Git` paths and a bare `bash`. On Windows the bare `bash` resolves by PATH order to the same first bash.exe, so it adds nothing. The comment at line 56 still says candidates are tried "never by its place on PATH", but the code now picks one by its place on PATH. The refusal at line 80 still says "PATH's bash ... were each run".
> - **Consequence:** Take a host whose first PATH bash.exe is the System32 WSL launcher, which cannot open a `C:/` path, and whose Git bash comes later on PATH, outside Program Files. A per-user or scoop Git on the user PATH is one example. At fce5603f8 that host resolved Git's bash; at HEAD it resolves none. `runShim` throws `no bash can see <shim>`, every policy read through the helper refuses, and agent-cap rule 7 denies every Agent and Workflow call. A stubbed-spawnSync probe showed the base module running the shim under the second PATH bash and HEAD refusing. Spec 78 S3 chose the narrowing for parity with `resolve_bash` and never weighed this case. The path is narrow, since a hook running under Git Bash likely has Git's usr/bin first. The failure is a loud fail-closed denial, so the grade is medium. Refuted finding 2 argued this configuration cannot be reached from the hook, because Git Bash puts its own usr/bin first. The skeptic on this finding confirmed it as a narrow but real path.
> - **Fix (skeptic judged SOUND):** Get parity by widening rather than narrowing. Keep the JS scan of every PATH bash, and make the canonical `resolve_bash` scan every PATH entry the same way, keeping each candidate only if `test -f` passes. Failing that, at least make the line 56 comment and the line 80 refusal state the first-PATH rule and name `export GOV_BASH=<path>` as the remedy. Add the stubbed-spawnSync probe as an arm with a WSL-first PATH. This fix decides the resolver order that L1 and L2 below depend on.
> - **Left-shift gate:** The class is `memory/gotchas/a-view-fix-trades-one-blindness-for-another.md`. The arm above, a WSL-first PATH with a later Git bash that must resolve, is the gate. Share it with L2's parity row so that one fixture holds both the order and the lost case.
>
> ### L1. resolveBash still stats every PATH bash but reads only the first, and its comment overstates parity with `shutil.which` (id 4)
>
> - **Where:** `tools/policy/policy-mirror.js:63-66`, with the comment at lines 56-58.
> - **What is wrong:** `onPath` is still built by calling `fs.existsSync` on `bash.exe` and `bash` in every PATH directory, and line 66 reads only `onPath[0]`. At the base `...onPath` used every entry, so the wasted stats came in with the L2 fix. The comment says the order matches the checker's `resolve_bash` (check_policy.py:899), which asks `shutil.which("bash")` once. `existsSync` also accepts a directory or a non-executable file named bash, which `which` skips, so the parity holds only loosely. On this node both resolvers picked the same `C:\Program Files\Git\usr\bin\bash.exe`.
> - **Consequence:** Behaviour is unaffected, because every candidate is then run with `test -f`. Every rule-7 or mirror read in a fresh hook process stats each PATH directory twice for values nothing reads. The comment may lead the next edit to trust a parity that holds only on PATHs like this node's.
> - **Fix (skeptic judged the finder's fix UNSOUND; this is the skeptic's corrected fix):** Stop at the first hit, but keep `existsSync`'s swallow-all-errors behaviour: `const first = dirs.flatMap((d) => [path.join(d, "bash.exe"), path.join(d, "bash")]).find((p) => { try { return fs.statSync(p).isFile(); } catch { return false; } });`, then put `first` in `cands` in place of `onPath[0]`. Alternatively, keep the code and reword the comment so it no longer claims the same order as `shutil.which`. If M3's widening fix is taken, the full scan is used again and this item reduces to making the comment true.
> - **Left-shift gate:** L2's resolver-parity row covers it. Once that row compares the two resolvers' candidate order, a comment that claims parity has a check behind it.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-81.md`, a Tier-1 micro-spec at order 28, status `DEFERRED`, in the shape `2026-10-25-spec-TOOL-dGroundRules-79.md` follows, that repairs the finding(s) above. Its write set: tools/policy/policy-mirror.js (and the resolver sentence in tools/policy/README.md). Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Re-verify each finding's premise at HEAD by reading the code it cites (and a probe where the report's reason ran one); a premise that no longer holds is said so in §4 and dropped from scope, never specced.
2. Spec the fix the report marks SOUND, or the skeptic's corrected fix where the finder's was judged UNSOUND. Take the skeptic-SOUND fix for M3: keep the JS scan of every PATH bash (restore `...onPath`), and widen nothing in Python unless the parity requires it; make the comment and the refusal at the line the report names state the order truthfully and name `export GOV_BASH=<path>`. L1 then reduces to the comment. Add the stubbed-spawnSync WSL-first probe as a criterion. TOOL-dGroundRules-82 builds after this unit and asserts the order you settle, so state that order in §4 as one line it can copy.
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
