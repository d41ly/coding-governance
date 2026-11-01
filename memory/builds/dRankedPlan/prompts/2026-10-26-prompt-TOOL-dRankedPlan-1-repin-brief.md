**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-9

# Re-pin brief — dRankedPlan, two stale pins and one interface spelling

The 16 specs under `memory/builds/dRankedPlan/spec/` are staged, uncommitted and `rev-1`. After the fix pass the
main loop re-rendered the as-built view and re-ran `tools/check-spec-tokens.py`: two hits, both stale pins, because
the deviation records 51 and 91 amend their clauses and the view now hashes the amended text. A spec carries a
clause an `amends` record changed at the view's hash, as `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-10.md`
line 5 does beside its deviation 101.

Fix exactly these, in place, changing no status header, clause token, §3 edge or §8 mark otherwise. Commit nothing,
and return each with what you changed.

1. `2026-10-26-spec-TOOL-dRankedPlan-5.md` · `[carries]` · `**Carries:** cl-dClosedLoop-0373@70fb5631 whole` → pin
   `@f1eb8c00`, the hash the as-built view gives the clause amended by deviation 51.
2. `2026-10-26-spec-TOOL-dRankedPlan-9.md` · `[carries]` · `**Carries:** cl-dClosedLoop-0377@fd363a7f whole` → pin
   `@a78b3ac9`, the hash the view gives the clause amended by deviation 91. Deviation 91's `Follow-through:` now reads
   `amends cl-dClosedLoop-0377@fd363a7f`, which the as-built join requires; leave that record as it is.
3. `2026-10-26-spec-TOOL-dRankedPlan-6.md` · interface (M2) · its §4 example and AC3 name the plan record
   `…-1-plan.md`, while TOOL-dRankedPlan-16 §8 F1, which owns I3, settled it as `<date>-build-<FAMILY>-<slug>-1-plan-1.md`
   and reads it through `find_plan_record`. Spell it as unit 16 does wherever unit 6 names it, and check that unit 6's
   fixtures and probes still hold with that name.

Afterwards run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` and confirm no finding names a
dRankedPlan file.
