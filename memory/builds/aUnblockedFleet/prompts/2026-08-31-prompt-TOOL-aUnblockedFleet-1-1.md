# The owner's prompt — unattended builds must stop blocking each other out

**Serves:** research TOOL-aUnblockedFleet-1

Handed to `/unattended --prompt` on 2026-08-31, node `a`. The value carried whitespace and named no
readable file, so by the Skill's file-first test it is the prompt itself and is reproduced VERBATIM
below. The bytes travel rather than a reference: the build folder is the authorization, so it may not
point at a file that can be edited after the run starts.

## Verbatim

> The unattended kit requires modifications: --preflight refuses if a repo has unattended builds in
> non-terminal states (eg. `building` or `landing`). This doesnt make any sense - existing builds
> should not impair new builds starting up as they could be completely unrelated, and concurrent
> coding is the whole reason this repo exists. Understand the problem and build a solution to ensure
> that unattended builds do not block each other out.

## What the orientation found before the folder was written

The refusal the owner names is `check_single_live()` at `tools/unattended/unattended.sh:1224`, refusal
5, plus its mirror at `tools/unattended/check-unattended.sh:1112`, leg check 7. Both enforce **at most
one non-terminal run-state file in the whole tree**, and both carry the same stated justification:
otherwise "the run" is not well-defined, and anything keyed on it must either OR the phases together
or pick one arbitrarily.

**That justification names a consumer that does not exist.** Every one of the driver's fourteen verbs
takes a `<slug>` (`unattended.sh:4248-4261`); the leg's three global loops over `builds/*/RUN*.md`
(`:247`, `:332`, `:448`) each grade per file. Nothing in this repository resolves "the run" without
being told which build. The invariant's only consumers are the two checks that enforce it. That claim
is the load-bearing one and unit 1 tests it rather than asserting it.

## The prior art the recall probe surfaced

Three OPEN backlog rows describe this same defect from three angles, and none of them frames it the
way the owner does:

- `TOOL-aReapedTicket-5` — the registry has a liveness check for exactly ONE phase and none for the
  others. A run that dies in `BUILDING`, `REVIEWING`, `RESEARCHING` or `TESTING` leaves a record that
  is non-terminal forever and blocks every future run with no override. Its candidate fix is a second
  liveness signal (a recorded pid, a record-age bound). **That is the DEAD-run half only.**
- `TOOL-aFusedCharter-4` — the kit deadlocks when several builds land on one trunk. Measured
  2026-08-19 with three builds at `LANDING`; resolved only by falsely marking two of them `ABORTED`.
- `TOOL-aBoundedVerdict-24` — a run that CLOSES but cannot LAND reds every later run's bar forever.

The owner's framing is strictly stronger than all three: a genuinely **live** unrelated run should not
block a new one either. A liveness signal does not deliver that; scoping does.
