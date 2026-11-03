**Serves:** research TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41

# Promoted-fix brief — the round-2 promotions' gate hits and their departure records

The round-2 spec audit (`memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`)
promoted its findings into TOOL-dCalibratedLens-31 to -41. The `rescope · item add` rows in
`memory/builds/dCalibratedLens/RUN.md` name each unit's finding. Those eleven specs are uncommitted at `rev-1` and
unaudited, so edit them in place with no rev bump and no §9 line. Do not touch any other spec. Do not commit, do
not stage, and do not run the build-index generator or any gate.

1. **`[bar]`, unit 36:** §6 names the suite `format-guard.test.sh`. A suite is not an acceptance observation.
   Observe the checker on a staged break or a fixture instead, and declare the suite's arm on a `New arm:` line
   in §7.
2. **`[guards]`, units 37 and 41:** §4 Files touched names `tools/gate-legs.json`, and that path trips the guard of
   leg `run-gates canary`, which is absent from the §7 leg line. Add `run-gates canary` to each spec's §7 leg line.
3. **Hygiene check 12, unit 41:** scope items S8, S19, S22 and S23 name neither an acceptance criterion nor
   `NOT OBSERVED`. Give each one the criterion that observes it, or `NOT OBSERVED` with the reason, in the shape
   the spec's other scope items use.
4. **Hygiene check 25, units 31, 34 and 38:** a §2 scope item whose words retire, drop, remove or replace a
   backticked named thing owes a `**Readers:**` clause (`memory/HYGIENE.md` check 25). If the item truly retires
   something, write the clause. If it does not, reword the item off the retirement verb.
5. **One departure record per added unit** (README rule 1), for each n in 31 to 41:
   `memory/builds/dCalibratedLens/build/2026-11-02-build-TOOL-dCalibratedLens-<n>-deviation-<n>1.md`. Copy the
   shape of `memory/builds/dCalibratedLens/build/2026-11-02-build-TOOL-dCalibratedLens-20-deviation-201.md`
   exactly, and keep its Follow-through and Approver wording, which `deviations.py` parses. Name the round-2
   record, the unit's finding id and item, and the unit's rescope row.

Return the files you changed and wrote.
