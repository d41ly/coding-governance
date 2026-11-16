# aPiecewiseGrade — asks

## Asks

- TOOL-aPiecewiseGrade-9 · filed 2026-11-16 · THE CARRIES JOIN STILL READS HISTORY ON EVERY RUN. The spec-token checker's carries join reads each chain spec's revision history on every whole-tree run, about 61 s of the run at `d9f84ee14` (PINNED d9f84ee14), and TOOL-aPiecewiseGrade-1 runs every join whole, so neither the per-spec cache nor the load-once fix of TOOL-aPiecewiseGrade-3 reaches it. TOOL-aPiecewiseGrade-1's F1 named it as the cost left over. · seen `tools/check-spec-tokens.py` matching `def read_carries_specs` run `python tools/check-spec-tokens.py` · accept a cache for that join keyed on its own inputs, its answer byte-identical to the plain run's on every tree, and a measured whole-tree run on node a, base against built

## Dispositions

- SEV · TOOL-aPiecewiseGrade-9 · MED · a cost, not a defect: every verdict is right, and the whole-tree run pays the history read each time
- KEEP · TOOL-aPiecewiseGrade-9 · out of this build by its own brief, which named the carries history read a follow-up at the wrap-up
