# Revision — aWitnessedCrash: TOOL-aWitnessedCrash-1 spec rev-2, the builder's divergence

**Serves:** research TOOL-aWitnessedCrash-1

## The prompt

> The memory-hygiene checker `tools/memory-tree/check-memory-hygiene.sh` prints `line 3611: ALFORM: unbound variable` during commit-hook runs, yet the hook still passes. Under `set -u` a variable that is empty or unset crashes that check, and the hook's overall verdict hides the crash. That means some check is silently not running. The defect was recorded as TOOL-aJoinedCanon-6.
> - Find where `ALFORM` is set and read at that line. Make it safe under `set -u`.
> - Find out why a crashed check does not red the hook, and close that hole for this class of failure (a crashed check must not read as a pass).
> - Go through this repository's flow: `/session-kickoff`, then a specced unit under `tools/`, built by the gov-builder role.


## The brief

### Goal
DIVERGENCE: spec section 5, AC5, cannot be observed as written, because the spec quotes its own grep strings. At the built tip, `git grep -l "memory-tree@2.158"` lists one file instead of none: memory/builds/aWitnessedCrash/spec/2026-11-13-spec-TOOL-aWitnessedCrash-1.md, whose S4 and AC5 prose spell the string. `git grep -l "memory-tree@2.159"` lists ten files instead of nine: the nine stamp carriers plus that same spec, which spells `memory-tree@2.159` in AC5. All nine real carriers moved. The only way to record AC5 as met would be an OBSERVED ledger line that the criterion's own text contradicts, and HYGIENE.md's "Acceptance ledger" sends that case to the AMENDED form, which needs a spec revision I may not write. The fix is for AC5, and S4 if wanted, to scope both greps away from build records, for example `git grep -l "memory-tree@2.158" -- ':!memory/builds'`. At the tip that lists nothing, and the 2.159 grep under the same pathspec lists exactly the nine files. Because of this I did not set the spec CLOSED and did not write the acceptance ledger. The code itself matches the spec as written, so I left the two pass commits on the branch (8e4f578c3 for S1-S3, ef4855a15 for the S4 bump) rather than reverting them. After the spec is revised, the next dispatch only needs to write the ledger and close the spec. No code move is owed, so the S4 bump stays valid.

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
