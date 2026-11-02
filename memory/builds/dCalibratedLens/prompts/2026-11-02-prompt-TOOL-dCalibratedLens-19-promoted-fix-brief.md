**Serves:** research TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30

# Promoted-fix brief — the round-1 promotions' token hits, check 25, and their departure records

The round-1 spec audit (`memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`)
promoted its 11 HIGHs into TOOL-dCalibratedLens-19 to -29 and its 41 minors into TOOL-dCalibratedLens-30. The
`rescope · item add` rows in `memory/builds/dCalibratedLens/RUN.md` name each unit's finding. Those twelve specs are
uncommitted at `rev-1` and unaudited, so edit them in place with no rev bump and no §9 line. Do not touch specs 1 to
17. Do not commit, do not stage, and do not run the build-index generator or any gate.

1. **`[path]` hits in §6** (`check-spec-tokens.py` joins backticked path-shaped tokens in §6 against
   `git ls-files`). Cite each untracked file by BASENAME in §6 and keep the full path in §2 and §4:
   - unit 19: `tools/memory-tree/record-kinds.toml`
   - unit 20: `tools/loop/loop_review.py`
   - unit 21: `tomllib.load(open('tools/memory-tree/record-kinds.toml','rb'))['record-kind']`. Rewrite it so no
     backticked token is path-shaped, e.g. name `record-kinds.toml` by basename and describe the read.
   - unit 23: `tools/workflows/evals/check_evals.py` and `tools/workflows/replay_scorer.py`
   - unit 25: `json.load(open('tools/gate-legs.json'))['legs']`. Rewrite as for unit 21, naming `gate-legs.json`.
   - unit 30: `help/loop-review.md`
2. **Memory hygiene check 25** on units 19, 20 and 24: a §2 scope item whose words retire, drop, remove or
   replace a backticked named thing owes a `**Readers:**` clause (`by name:` the readers that spell the name,
   `by value:` the readers of its value, or `NO VALUE READERS` with a reason). If the item truly retires
   something, write the clause. If it does not, reword the item off the retirement verb. `memory/HYGIENE.md`
   check 25 states the grammar.
3. **One departure record per added unit** (README rule 1: a spec run records each unit it adds as a departure).
   Write `memory/builds/dCalibratedLens/build/2026-11-02-build-TOOL-dCalibratedLens-<n>-deviation-<n>1.md` for each
   n in 19 to 30 (deviation 191, 201, … 301), in the shape of
   `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-20-deviation-201.md`:
   - **Departs from:** `dCalibratedLens [roster]`; **Hand-off:** `design-to-spec`
   - **Before:** the roster's seventeen units and the build ask `TOOL-dCalibratedLens-18`
   - **After:** the roster also carries the unit, and what its mechanism closes
   - **Cause:** `review finding`; **Reason:** BUILD-METHOD M4's promotion, naming the finding id and item (H1–H11,
     or the minors batch for unit 30), and that this spec run defers the unit to the build run
   - **Evidence:** the audit record, the unit's rescope row in `RUN.md`, and the unit's spec
   - **Risk:** `additive`; **Approver:** `author-recorded`; **Follow-through:** carried forward to the build run;
     **Caused-by:** the unit id.

Return the files you changed and wrote.
