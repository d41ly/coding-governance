# Brief — aWitnessedCrash: the hygiene engine reds on a bash runtime error it ran past

**Serves:** research TOOL-aWitnessedCrash-1

## The prompt

> The memory-hygiene checker `tools/memory-tree/check-memory-hygiene.sh` prints `line 3611: ALFORM: unbound variable` during commit-hook runs, yet the hook still passes. Under `set -u` a variable that is empty or unset crashes that check, and the hook's overall verdict hides the crash. That means some check is silently not running. The defect was recorded as TOOL-aJoinedCanon-6.
> - Find where `ALFORM` is set and read at that line. Make it safe under `set -u`.
> - Find out why a crashed check does not red the hook, and close that hole for this class of failure (a crashed check must not read as a pass).
> - Go through this repository's flow: `/session-kickoff`, then a specced unit under `tools/`, built by the gov-builder role.

## The brief

### Goal
Check 23 of `tools/memory-tree/check-memory-hygiene.sh` stops printing an unbound-variable error, and the engine reds whenever
bash reports a runtime error on its stderr, because some of those errors do not stop a `set -u` script.

### Items
1. Declare check 23's associative arrays with an empty value (`=()`), so `${#ALFORM[@]}` and every `${!…[@]}` walk read
   an empty set instead of an unset name. [planned TOOL-aWitnessedCrash-1]
2. A crash witness in the engine: its stderr is kept and replayed at exit, and a line in bash's runtime-error shape
   (`<file>: line <N>: <message>`) turns an exit 0 into exit 1 with a `HYGIENE FAILED` line naming it, plus an offender key
   under `--offenders`. [planned TOOL-aWitnessedCrash-1]
3. A self-test arm in `tools/memory-tree/check-memory-hygiene.test.sh` that injects a non-fatal runtime error into a copy
   of the engine and asserts the red, observed red against the engine as it stands at BASE. [planned TOOL-aWitnessedCrash-1]

### Acceptance
With a non-build memory file staged, `check-memory-hygiene.sh --staged` prints no `unbound variable` line and exits 0. The
suite's new arm reds against the BASE engine (exit 0 through an injected `${#X[@]}` on an unset array) and passes against
the built one. The bar's `memory hygiene` leg is green.

### Gates
`memory hygiene`, `memory-hygiene self-test` (run on demand for this unit's arms), `spec tokens (a spec's own names
resolve)`, and the full bar at the close.

### Non-goals
No other check's logic moves. No new gate leg, and no static lint for unset arrays across the tree.

### Limitations
Reproduced on node a: `bash 5.3.9`; `${#X[@]}` over `declare -A X` under `set -u` prints the error, fails the command and
continues, while `$Y` unset exits 1. The witness must keep every existing exit-0 channel, the `--offenders` fd-3 contract and
exit 2 for a refusal. A kit edit owes its version bump once, after the last move.

### Reuse
`reuse_lookup.py` named no seam that reads a script's own stderr for bash runtime errors. The witness rides the engine's
existing `--offenders` keys (`add_offender_keys`) and its final `exit "$status"`. Recall returned the fatal siblings
TOOL-aHoistedPass-37 and TOOL-aTracedSpawn-1; this is the non-fatal form.

## Drawn from the session

> `bash u2.sh` with `set -u; declare -A X; true; if [ "${#X[@]}" -gt 0 ]; then :; fi; echo after` printed
> `u2.sh: line 4: X: unbound variable`, then `after`, and exited 0.
— agent, 2026-11-13, reproducing the crash

> Staging `memory/HYGIENE.md` and running `check-memory-hygiene.sh --staged` printed `line 3611: ALFORM: unbound variable` and exited 0.
— agent, 2026-11-13, reproducing the hook's pass

## Owner confirmation

Asked: Go through this repository's flow: `/session-kickoff`, then a specced unit under `tools/`, built by the gov-builder role.
Answer: Done means: the unbound-variable message no longer prints on a commit; a check that crashes now reds the hygiene run, observed red-first in a fixture; the bar's memory hygiene leg is green.
