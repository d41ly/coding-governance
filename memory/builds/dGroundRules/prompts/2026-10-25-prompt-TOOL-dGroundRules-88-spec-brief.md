**Serves:** research TOOL-dGroundRules-88

# Spec brief — TOOL-dGroundRules-88, packet.py's --repin guard tells the owner from a chain run by its caller

## The prompt

The owner, after the main loop traced the cycle that blocked dGroundRules' close: "spec and build this in this build so it lands before any further units get built". "This" is the guard fix the main loop described:

> The cycle is in `packet.py`'s `--repin` guard (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py`, `scan_live_run` near line 540, refused in `cmd_repin` near line 659). The guard exists so a chain run never moves its own instrument pins, but it decides by tree state ("is any chain build's `RUN.md` non-terminal?") rather than by caller, so it refuses the owner exactly as it refuses an agent. The packet's pin arm grades the live run's tree against those pins, so while a chain run is open any instrument fix leaves a stale pin nobody may repin, and the run cannot close. The fix makes the guard key on the caller: still refuse an agent or an unattended session, admit an attended owner's repin and record it.

Context: `packet.py` is itself one of the pinned instruments (`SELF` in `INSTRUMENTS`), so this unit's edit leaves `packet.py`'s own pin stale until the owner repins it, which the new guard must admit while dGroundRules' run is live. The cost the cycle stranded is ask TOOL-dGroundRules-112 (`carries.py`'s per-revision `git show`). PLAY-dClosedLoop-26 (`106785b03`) is the last unit that changed this guard; its fixture plants `run-live`, `run-landed`, `run-pushed`, `run-unpushed` and `run-dirty` read the guard through `scan_live_run`.

## The brief

### Goal
Author `memory/builds/dGroundRules/spec/2026-10-25-spec-TOOL-dGroundRules-88.md`, a Tier-2 spec at order 34, status `DEFERRED`, in the shape `memory/TEMPLATE-SPEC.md` gives, that makes `--repin` (and only `--repin`: a first render stays refused inside a chain run) admit the owner while a chain run is live and refuse every agent and unattended caller. Author only: no product code, no commit, no gate beyond memory hygiene.

### Items
1. Reuse first: find how this repository already tells an owner's invocation from an agent's (the scratch-guard hook's `agent_type`, the unattended kit's owner-only verbs, `tools/check-template-size.sh`, `tools/run-gates/run-gates.sh`, any other seam a grep for owner/agent finds) and run `reuse_lookup.py` on the behaviour; spec the caller test on the seam that exists, or say with evidence why none fits. Deny by default: a caller the test cannot classify is refused.
2. Name what the guard records when it admits an owner repin inside a live chain run (where, in what shape, read by whom), so the repin is visible on the record rather than silent.
3. Keep every existing refusal and fixture plant meaning what it means today for an agent caller, and add the plant(s) that observe the owner path admitted and an agent or unattended caller refused with a live chain run; a `New arm:` line per added plant.
4. State the owner action this unit leaves: after its build commit, `packet.py --repin` of `packet.py` itself (and any other instrument this unit touches) by the owner, admitted by the new guard, before the close's bar; the close's spec tokens leg reds on the stale pin until then.
5. Each acceptance criterion is a command the pass may run (`packet.py --fixture --plant <case>`, a direct call of the guard), never the bar or a self-test suite, and carries `Red when:` with a staged break that reds it by name. §6 names the legs the touched file owes through `derive_guarded_legs`.
6. §7 "Open questions" reads exactly `none`, with no bullet under it, unless a fork genuinely needs the owner; any follow-up goes in the revision log as prose. No line anywhere in §5 starts at column 0 with `AC<n>` other than the bullets themselves; every AC bullet carries `Red when:`; keep every acceptance code span on one line and free of a `|` the bar pattern reads as a pipe; no retirement word in §2; an untracked path sits in a fenced block; never write a probe copy of a spec inside the spec folder.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); hygiene check 12 names nothing in this spec.

### Gates
Memory hygiene only.

### Non-goals
`carries.py` and its batching (ask TOOL-dGroundRules-112); the first-render refusal; the pin arm's grading; any other instrument.

### Reuse
`scan_live_run`, `cmd_repin` and the fixture's `run-*` plants in `packet.py`; whichever owner-versus-agent seam item 1 finds.
