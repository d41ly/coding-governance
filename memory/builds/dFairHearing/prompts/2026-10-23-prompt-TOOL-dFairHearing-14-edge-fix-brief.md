**Serves:** research TOOL-dFairHearing-14

# Edge-fix brief — TOOL-dFairHearing-14's false hands-off edge to TOOL-dFairHearing-18

Hygiene check 12 refuses an edge parity defect. `TOOL-dFairHearing-14`'s §3 Edges (line 79) declares **hands-off** `TOOL-dFairHearing-18` ("the whole-design walk's recall runs declare their manifest the same way"). Spec 18 declares no consumes-from back.

Spec 18's writer showed that spec 18 consumes nothing of spec 14:

- No `manifest`, `check_experiment` or `measure_union` appears in spec 18.
- Its grade takes `--key`, `--seed` and one review record per run.
- Spec 23's S43 routes the design grade through `measure_recall`.

So the false half of the pair is spec 14's edge. Under build method M2, a disagreement is a defect in exactly one document.

- Remove that one bullet from spec 14's §3 Edges.
- Bump the status header to the next rev.
- Add a §9 line naming §3, the removed edge, and why: spec 18's grade reads no experiment manifest.
- Change nothing else. If any other line of spec 14 depends on that edge (a §4 or §6 mention of spec 18 declaring a manifest), report it and do not edit it.
- Do not commit, do not stage, and do not run any gate. Report the old bullet and the new header and §9 line.
