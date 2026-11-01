**Serves:** research TOOL-dRankedPlan-82

# Revision brief — TOOL-dRankedPlan-82 rev-2, the reading is the main loop's

## The prompt

The builder dispatched on `TOOL-dRankedPlan-82` at `cc8880ae6` stopped without a commit. Two of the spec's steps are
ones its role may not take:

- §4 "The reading" and AC2 have the builder run `python tools/check-spec-tokens.py`, the argv of the
  `spec tokens (a spec's own names resolve)` leg. The role-gate arm of `tools/hooks/scratch-guard.js`
  (`checkRoleGate`, row G1) refuses every gate leg to `gov-builder` but those its allowlist in `.claude/roles.json`
  names, and it refused this one live.
- §5 AC1 has the builder run `python tools/run-gates/derive-ceilings.py --check`, the argv of the
  `leg ceilings clear their evidenced maximum` leg, refused the same way, so the builder can observe neither its red
  nor its green. `derive-ceilings.py --report` and `--write --observed … --how …`, and
  `manifest-check.sh --staged`, are admitted.

## The reading, taken

The main loop took R as §4 describes, on node a at `cc8880ae6`, the tree clean:

- `time python tools/check-spec-tokens.py` exited 0; `spec-tokens: packet join · 1 live chain run(s) · 1 packet(s)
  checked`; `real 6m50.960s`, so R is `411.0`.
- Census by `ps -ef`, before and after: no `run-gates.sh` but the idle orphan of `unattended-dgroundrules-0e6f4a`
  (pid 10907, from Oct 23); another worktree's `--dispatch` started its own `tools/check-spec-tokens.py` at
  23:44:14, overlapping the reading's last minute of 6m51s (23:38:24 to 23:45:15).
- C is therefore 10 × ⌈411.0 / 5⌉ = 830.

## The brief

### Goal
Revise `memory/builds/dRankedPlan/spec/2026-10-27-spec-TOOL-dRankedPlan-82.md` to rev-2, dated 2026-10-27, so the
builder can build it under its role. Author only: no product code, no commit.

### Items
1. §4 "The reading": R is the main loop's, taken as above, and stated in the spec with its census; the builder takes
   no reading. "The value" states C = 830 from R = 411.0.
2. §4 "The write": give the `--how` text with the values above, one line, no tab, recording the overlap honestly.
3. §5: AC2 and AC1 are the main loop's to observe, and say when — AC2 is the reading above; AC1's green after the
   pass commit. Give AC1's red a form the main loop can observe without writing under `tools/` (read
   `derive-ceilings.py` for what its `--check` reads), or state plainly that the red is observed only by the
   arithmetic and why. AC3 and AC4 stay the builder's, on its staged change.
4. Rollout: the main loop appends this unit's `## route` to the session card before the builder's dispatch; the
   builder sets DEFERRED to INPROGRESS before its first write. The header carries no `order` verb (removed at
   `63350171b`: the dispatch order gate reads the 79 DEFERRED units as non-terminal); the body's "order 28" sentences
   say so.
5. §8 gains a rev-2 entry naming this brief and the refusal. Keep §6, §7 (`none`) and every other section as they
   stand unless an item above moves them.

### Acceptance
`python tools/check-spec-tokens.py` names nothing in this spec (the main loop runs it); hygiene check 12 names
nothing in this spec. Run neither yourself: the main loop runs both on a quiet host.

### Gates
Memory hygiene only, scoped with `--only 2,12,25`.

### Non-goals
Any write outside this spec; any other unit's spec; the role gate and `.claude/roles.json`.
