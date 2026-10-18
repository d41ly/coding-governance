# Brief — aScoutedSeam: a held-out case set, the system measurement, the T2 fixes, and the final workflow design set

**Serves:** research TOOL-aScoutedSeam-3 TOOL-aScoutedSeam-1

## The prompt

> can we add a set of cases that will not be specifically tuned for as an extra test group (the prompt case should still account for them), then go through your 1, 2, and 3 suggestions in the order. Once done, compile a final workflow design set that any other session would be able to use and adjust its processes to the best results discovered. Merge and push.

## The brief

### Goal
Measure the reuse workflow as a system on a fresh, untuned case set as well as the tuning corpus. Apply
the targeted fixes the misses point to, and compile the best measured design into one self-contained
workflow design set that another session can adopt. Land it on main and push.

### Items
1. **Held-out set.** Mine fresh reinvention cases from gov, inCMS and NicoCares commits made after the
   tuning corpus was cut, each with objective evidence and verified ground truth. Freeze them before any
   further tuning. No prompt or lister change may be made by reading their outcomes. Every prompt is
   still written for the general case, so it applies to them too.
2. **System measurement (step 1).** Run the shipped flow end to end on the tuning corpus and the
   held-out set: the pre-spec scout (M1c), then the diff check (T1) given the scout's `## reuse` output.
   Re-judge every arm in one judge pass, so the system figure is one measurement.
3. **Targeted fixes (step 2).** Each fix is general, never per case:
   - inject the dossier's declared seams into the diff prompt;
   - add a value-type field census;
   - read the same-module siblings;
   - add a reachability rule;
   - turn a spec diff's scope items into units;
   - add a convention census and a CSS-literal-to-token matcher.

   Re-measure on both sets.
4. **Held-out readout (step 3).** Report the held-out figures beside the tuning figures.
5. **Final workflow design set.** One self-contained document, plus the instruments it names, that any
   session can follow to run a reuse orientation and a diff check at the measured best settings, and to
   adjust its own processes to them.
6. **Land.** Merge to main and push, through the lander.

### Acceptance
- The held-out cases and their trees are frozen and committed before any further tuning.
- One judged table shows the arms and the system on both sets.
- The design set is committed and names its measured basis.
- `bash tools/push-main.sh` lands it, and the full bar runs at the push boundary.

### Gates
memory hygiene · spec tokens · build README slot contract · lexicon naming predicates · the full bar at the push boundary

### Non-goals
- No writes to the inCMS or NicoCares repositories, which stay read-only.
- No tuning against held-out outcomes.
- No product code under `tools/` in this pass. The design set documents the workflow, and the units that
  build it stay specced.

## Owner confirmation

Asked: "Should I start with 1?" (step 1, the system measurement), after the three next steps were listed.
Answer: "can we add a set of cases that will not be specifically tuned for as an extra test group (the
prompt case should still account for them), then go through your 1, 2, and 3 suggestions in the order. Once
done, compile a final workflow design set that any other session would be able to use and adjust its
processes to the best results discovered. Merge and push."
