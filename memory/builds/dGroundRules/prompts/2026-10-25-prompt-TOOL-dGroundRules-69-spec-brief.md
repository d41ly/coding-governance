**Serves:** research TOOL-dGroundRules-69

# Spec brief — TOOL-dGroundRules-69, the strict case's source under the policy fixtures guard

## The prompt

> The close ran the `policy fixtures` leg with its own argv, `python tools/policy/check_policy.py --fixture --strict-from memory/builds/dClosedLoop/build/`, in a scratch clone of 3d86915cf. It printed `policy-fixture: 895 assertion(s) executed · 1 wrong`, the one wrong line `policy-fixture: guard-trace · WRONG memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md · not under the policy fixtures guard`. TOOL-dGroundRules-67 guarded the twelve paths a run WITHOUT `--strict-from` reported (that run printed `on-invalid-strict · NOT RUN`), so the strict case's source read was never traced until now. Every other case line of the run is green.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-69.md`, a Tier-1 micro-spec at order 23, status `DEFERRED`, in the shape `2026-10-24-spec-TOOL-dGroundRules-67.md` follows. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. S1: the `policy fixtures` row of `tools/gate-legs.json` gains one guard line naming the strict case's source. Decide between the file `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` and the directory `memory/builds/dClosedLoop/build/`, by reading how `check_policy.py`'s guard trace matches a read against a guard line and how the guard-census case (`TOOL-dGroundRules-37`, "names no file git tracks") grades a line; state the cost side (how often each would trigger the leg) in one sentence. Recommended: the file, since it is the one read traced.
2. S2: name every gate the insert can move: the install-prefix and spec-token waiver rows keyed by line or by first declared path (TOOL-dGroundRules-67 S4 had to re-key one), the kickoff manifest's audit stamp over `tools/gate-legs.json`, and the legs `python tools/check-spec-tokens.py --legs-for tools/gate-legs.json` prints. The builder runs those and re-keys or re-stamps what they demand, nothing else.
3. AC1: the guard trace of the strict case answers no WRONG line. The full leg is a bar leg the pass may not run; give the pass a probe it may run instead (the `on-invalid-strict` case run alone through the module's own case runner with `--strict-from memory/builds/dClosedLoop/build/`, reading its guard-trace lines). Red when: the line is removed again. The close's full run (main loop) observes the whole leg.
4. §7 names `policy fixtures` and the legs the touched file trips; declares no `New arm:`.
5. Keep every acceptance code span on one line; no acceptance line starts at column 0 with `AC<n>`; every AC bullet carries `Red when:`; no retirement word in §2; an untracked path sits in a fenced block.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
Any other spec; `check_policy.py`; the strict case's own judgement.

### Limitations
Measured by the main loop at 3d86915cf in a scratch clone; the log is in the run's scratchpad as `pf-full.log`.

### Reuse
TOOL-dGroundRules-67 S1, the same row's twelve-line insert.
