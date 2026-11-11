# Brief — dFinishedRecord: check 24 stops grading a run whose landing is already on the remote

**Serves:** research TOOL-dFinishedRecord-1

## The prompt

> Fix check 24 first (Recommended)

The owner's answer to: "Nothing was pushed: the bar is red on check 24 of the unattended kit gate. Check 24 reads RUN.md's literal phase, LANDING, so it still grades this finished run and wants a rescope add row for unit 41. The --rescope verb derives the phase as LANDED and refuses (check 26). No record can satisfy both. How do you want to land?" The option read: "A Tier-2 kit unit: check 24 skips a derived-LANDED record, as checks 7 and 23 do, with an arm observed red. Then re-run the lander with both."

## The brief

### Goal
Check 24 of `tools/unattended/check-unattended.sh` excludes a run record whose landing commit is an ancestor of the advertised default-branch tip, so a finished in-place landing is not graded for roster amendments it can no longer record.

### Items
1. Check 24's roster loop (the `for f in $RUNS` loop holding the `fail 24` roster arms) asks `check_derived_landed` after its recorded-phase skip. On 0 it prints a `check 24 EXCLUDED` line and skips the record. On 2 it prints one `check 24 exclusion UNAVAILABLE` line and grades every record, as check 23 does. [planned TOOL-dFinishedRecord-1]
2. `tools/unattended/check-unattended.test.sh` gains arms for the exclusion, observed red before the fix. [planned TOOL-dFinishedRecord-1]

### Acceptance
1. A fixture LANDING record whose landing commit the advertised tip reaches, with a unit in its units region that no `rescope · item add` row names, passes check 24 and prints the EXCLUDED line. Before the fix the same arm reds with check 24.
2. The same fixture with the landing commit NOT on the advertised tip still reds check 24.
3. The existing check 24 arms stay green.
4. Over the merged tree (51912ffce), `bash tools/unattended/check-unattended.sh` prints `check 24 EXCLUDED memory/builds/dConvergedCharter/RUN.md` and no `check 24 FAILED`.

### Gates
unattended kit gate · unattended kit self-test (the arms) · lexicon naming predicates · kit epoch · kit version markers · memory hygiene · spec tokens; then the full bar at the landing.

### Non-goals
The driver's verbs and `refuse_if_terminal`; checks 7 and 23; `check_derived_landed` itself; dConvergedCharter's run-state file, which stays as landed; any other check's phase reads.

### Limitations
Kit versions move through the lander's `mint`, not by hand. Unit agents run no gate legs; the main loop runs them after the build.

### Reuse
`check_derived_landed` (check-unattended.sh, TOOL-aSightedSkeptic-13) is the one predicate, and check 23's exclusion block is the shape to copy, messages included. Recall returned TOOL-aSightedSkeptic-13 and TOOL-aPrimedKeepalive-4 (check 7's exclusion).

## Drawn from the session

> unattended: check 2 ... UNATTENDED check 24 FAILED — a unit is in the roster this run is executing and was not in the roster it entered BUILDING with, and no rescope row adds or supersedes into it, so the scope moved with nothing on the record saying so: PLAY-dConvergedCharter-41 in memory/builds/dConvergedCharter/RUN.md
— agent, the push-main.sh bar log of 2026-11-05

## Owner confirmation

Asked: "Should the new build dFinishedRecord declare `spec-audit:`? It is one Tier-2 unit with no open fork: check 24 asks `check_derived_landed`, as check 23 already does under TOOL-aSightedSkeptic-13."
Answer: "No audit (Recommended)"
