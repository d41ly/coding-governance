# Promotion brief — aSmoothedDispatch: reconcile with main at bdb633d94

**Serves:** research TOOL-aSmoothedDispatch-22

## The brief

### Goal
Local `main` and `origin/main` both sit at `bdb633d94`, where aShelvedLeg landed on top of aSwiftRefusal, aGuardedEffort and dPavedRoad. dPavedRoad's TOOL-dPavedRoad-1 shipped a `--spec` mode in `tools/check-spec-tokens.py`. This build's TOOL-aSmoothedDispatch-5 added its own `--spec` mode to the same checker. `git merge --no-ff main` into `branch/aSmoothedDispatch` conflicts in three files: `tools/check-spec-tokens.py`, `tools/check-spec-tokens.test.sh` and `memory/guides/SESSION-KICKOFF.md`. On 2026-11-11 the owner said "Keep main's --spec". This unit makes that merge commit. It keeps TOOL-dPavedRoad-1's checker, which grades several named specs of any status, and retires unit 5's one-path, live-only mode. Unit 5's scratch-guard allow, units 7 and 8's spec-writer overlay and every other part of this build are kept.

### Items
1. `tools/check-spec-tokens.py`: take main's side of every hunk. The merged file is byte-identical to `main`'s, because every change this branch made to it is unit 5's `--spec`. No line of unit 5's `scope` code or its usage paragraph remains.
2. `tools/check-spec-tokens.test.sh`: keep main's seven `PR1` arms and its fixture. Drop each `SD5` arm whose case a `PR1` arm already covers, or whose behaviour main's mode does not have. That covers the `scope ·` line, the live-only refusal and unit 5's refusal wording. An `SD5` arm whose case main's mode has and no `PR1` arm covers is kept, re-pointed at main's output. The two `SD8` overlay-parity arms are kept and read the overlay item 3 leaves. Recount `FLOOR_ASSERTIONS` off the merged arms, and keep both sides' comment lines plus one `MERGED` line naming this unit.
3. `tools/roles/house/gov-spec-writer.md`: main's kit prompt `tools/roles/agents/gov-spec-writer.agent.md` already tells the writer to run `check-spec-tokens.py --spec <path>` over each spec it wrote. The overlay keeps only what that line lacks:
   - the exit-1 row shape `spec-tokens: <spec path> [<kind>]`;
   - the `spec-tokens: <N> unwaived hit(s)` summary;
   - that a `spec-tokens: REFUSING` line, an exit 2 or an exit 1 with no summary is the checker refusing, not a hit.

   Each shape is checked against what main's checker prints. Re-render `.claude/agents/` with the roles kit's own renderer, never by hand.
4. `tools/hooks/scratch-guard.js`: unit 5's allow for `gov-spec-writer` running the checker with `--spec` stays as git merged it. Confirm it admits main's multi-operand form, several spec paths after `--spec`. If it does not, widen it to that form and add one scratch-guard arm for it, with no other change to the hook.
5. `memory/guides/SESSION-KICKOFF.md`: take main's `last-audit` stamp, then re-stamp it over the merge by the manifest's own rule.
6. The merge commit carries every other auto-merged file as git merged it. Re-render the generated outputs the merge stales with their generators: the build index, LIVE, symbols and the codebase map.

### Acceptance
- The merge commit has two parents: this branch's tip and `bdb633d94`.
- `git diff bdb633d94 -- tools/check-spec-tokens.py` over the merge prints nothing.
- `grep -c 'SD5 ' tools/check-spec-tokens.test.sh` counts only the kept arms. Each kept arm is named in the spec with the case it covers that no `PR1` arm does.
- The overlay holds no sentence the kit prompt already says.
- The memory hygiene, shell hygiene, install-prefix, docs and roles-render legs exit 0 over the merge.
- The main loop runs `tools/check-spec-tokens.test.sh` and `tools/hooks/scratch-guard.test.sh` at the close. Each prints no FAIL line, and any new arm is observed RED on its staged break first.

### Gates
`bash -n` on the touched shell files; the memory hygiene, shell hygiene, install-prefix, docs and roles-render legs (builder); the checker and scratch-guard suites (main loop); then the full bar once, through the lander.

### Non-goals
Any change to what main's `--spec` grades, refuses or prints. The unattended driver and its suite. Pushing, and the `--no-ff` merge into `main`, which are the main loop's.
