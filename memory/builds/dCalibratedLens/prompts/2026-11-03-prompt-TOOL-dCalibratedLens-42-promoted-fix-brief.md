**Serves:** research TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48

# Promoted-fix brief — the round-3 promotions' token hits and their departure records

This brief covers ALL SEVEN units TOOL-dCalibratedLens-42 to -48, whatever unit the handoff marker names. The
round-3 spec audit (`memory/builds/dCalibratedLens/reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`)
promoted its findings into them. The `rescope · item add` rows in `memory/builds/dCalibratedLens/RUN.md` name each
unit's finding. The seven specs are uncommitted at `rev-1` and unaudited, so edit them in place with no rev bump and
no §9 line. Do not touch any other spec. Do not commit, do not stage, and do not run the build-index generator or
any gate.

1. **`[path]` hits in §6** (`check-spec-tokens.py` joins backticked path-shaped tokens in §6 against
   `git ls-files`). Unit 46 cites `runlog/extract.py`, `hooks/agent-cap.js`, `policy/policy-mirror.js`,
   `hooks/scratch-guard.js` and `tools/run-gates/leg_factory.py`; unit 47 cites `tools/run-gates/leg_factory.py`.
   For a file that is tracked under `tools/` (check with `git ls-files`), spell its full tracked path. For a file
   the build run will create, cite it by basename in §6 and keep the full path in §2 and §4.
2. **One departure record per added unit** (README rule 1), for each n in 42 to 48:
   `memory/builds/dCalibratedLens/build/2026-11-03-build-TOOL-dCalibratedLens-<n>-deviation-<n>1.md`. Copy the
   shape of `memory/builds/dCalibratedLens/build/2026-11-02-build-TOOL-dCalibratedLens-32-deviation-321.md`
   exactly, and keep its Follow-through and Approver wording, which `deviations.py` parses. Name the round-3
   record, the unit's finding id and item, the unit it repairs, and its rescope row. Write the minors-batch
   unit's record in the shape of `memory/builds/dCalibratedLens/build/2026-11-02-build-TOOL-dCalibratedLens-41-deviation-411.md`.

Return the files you changed and wrote.
