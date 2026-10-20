# Return: the execution plan's writer, resumed to fold the owner's last answers

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 221's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-56-spec-writer.md`.

---

I've folded the owner's `[answers-3]` (ER:306-350) into the plan. The schedule script needed no change, and nothing is committed.

The plan is now 93 KB at `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md`. I swept it after the edits. Nothing still says a no-option fork is carried forward, or that only review-promoted units carry. No bare chain ids are left, and only a pasted script-output line runs long.

## What changed, section by section
- **Intro:** now cites `[answers-3]` alongside `[answers-2]`.
- **[answer]:**
  - Bad news 2 adds "Relax the weakest bound" (ER:328). The price is stated: a unit's own acceptance can be rewritten unreviewed until the owner reads the report.
  - Bad news 3: the extra unit now carries ANY unit a spec run adds ("Carry it too", ER:320).
  - The plan in brief now says nothing waits for the owner.
- **[constraints]:** the term-2 row now names adopted units as well as review-promoted ones.
- **[phase-0]:**
  - P0.2: the report lists `widens:` and `relaxes:` choices first, side by side. Two new red cases cover that ordering, and a third reds a `relaxes:` record that names no tier or reason.
  - P0.5 README rules: rule 1 covers every added unit (specced, audited, recorded as a departure, never deferred again); rule 6 adds the `relaxes:` mark.
  - P0.8 rows 1 and 5 now quote ER:320 and ER:328.
- **[phase-1], the extra unit:** it now admits review-promoted and adopted-discovery units from a spec run, once. A unit added by a run that closes a unit is refused as before. The other four carry-forward terms still apply, and the spec run audits its added units through the harness's scoped audit. Its red cases are now:
  1. a review-promoted unit in a spec run is carried;
  2. an adopted discovery's unit in a spec run is carried;
  3. deferring either one again is refused;
  4. a unit added and deferred by a run that closed a unit is refused, before and after.
- **[phase-2]:** the spec-run row now covers both kinds of added unit, and the build-run row now refuses re-deferring any of them. Rung 4 now carries a discovery's unit forward instead of filing an ask. Rung 6 is rewritten as relaxing the weakest bound, one bound at a time, so nothing parks.
  - **How "weakest" is judged:** the records rank bounds only by where they come from, in three tiers:
    - strongest: a bound the carried clause states, or a quoted owner ruling;
    - middle: a bound a v2 principle or policy key sets;
    - weakest: a bound the spec writer added on its own.
  - The run relaxes the lowest failing tier first. Within a tier the records give no ranking, so the run judges and writes its reason into the departure record.
  - The relaxed bound stays named in the spec so the coverage check still sees the clause's tokens.
  - The owner's spec-landing view lists widened surfaces and relaxed bounds first.
- **[schedule]:** one sentence added: the model is unaffected, and a re-run at HEAD `54c76bb24` prints the same output.
- **[deviations]:**
  - The rules now cover rungs 5 and 6, and record every unit a spec run adds as a departure.
  - The report ordering matches P0.2.
  - Two caveats added: relaxed bounds the run fails to mark won't be listed first, and nobody but the reader checks the run's tier judgement.
  - The approvals table now cites ER:320 for the extra unit. A new row says where each later ruling-made departure is recorded and when.
- **[owner]:** the two Tier-2 reviews come first (ER:343), then the walk and approval. Each build landing is now a read that nothing waits on.
- **[cannot]:** the spec-run-added-unit row and the residual-fork row now read as designed around by the owner's rulings.
- **[defaults]:** D9, D10, the record placement and wording (ER:336) and "Review twice" (ER:343) move to decided, each quoted. The "left open" subsection is gone.
- **[disagreements]:** the forks row now says nothing parks, and a new row records that the plan's file-an-ask route (D9) and carry-forward route (D10) are dropped.

## Schedule script
Unchanged: what a spec run carries and how a fork is settled don't touch the model's run counts, durations or precedences. Re-run as `python -B memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py` at HEAD `54c76bb24`, it exits 0 with output byte-identical to the block pasted in `[schedule]`: makespan 271, 43 runs at 37 distinct times, node b on spec runs only.

## Still open
- **Ranking within a tier.** Whether a relaxed bound was really the least important is checked only by the reader. The records give no ranking inside a tier, so it rests on the run's written reason. That is the owner's accepted price, but nothing gates it.
- **Detecting added units.** The extra unit's spec has to say how the driver recognises a spec run and the units it added (from the starting roster and the add/defer rows). I've stated that as an obligation on the spec, not designed it.
- **Not yet observed.** Whether the harness re-audits specs in a build run, and how the ask row holds the carry-forward ask open, are both first seen in dGroundRules' two runs.
