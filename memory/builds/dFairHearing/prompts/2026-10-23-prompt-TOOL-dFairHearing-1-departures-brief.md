**Serves:** research TOOL-dFairHearing-1 TOOL-dFairHearing-3 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-30 TOOL-dFairHearing-32

# Departures brief — seven spec revisions past their audited revisions, recorded by nobody

The departures report, `deviations.py --report dFairHearing` on the prepared merge (README rule 4), lists 11 members that no deviation record joins. Each member is a spec changed past its audited revision. README rule 4 owes one record for each.

A record joins a member by its **Departs from:** value `<unit>@rev-N` and **Hand-off:** `spec-revised` (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py`, the header's grammar). One record per address covers every entry with that address, so seven records are owed:

| Address | Revised in | Audited at |
|---|---|---|
| `TOOL-dFairHearing-1@rev-2` | `32afb3770` | `c993af496` |
| `TOOL-dFairHearing-3@rev-1` | `92dd0f46a` | `c993af496` |
| `TOOL-dFairHearing-14@rev-3` | `96a0fb304` | `92dd0f46a` |
| `TOOL-dFairHearing-15@rev-1` | `32afb3770`, `92dd0f46a`, `96a0fb304` | `c993af496` |
| `TOOL-dFairHearing-16@rev-1` | `32afb3770`, `92dd0f46a`, `96a0fb304` | `c993af496` |
| `TOOL-dFairHearing-30@rev-1` | `c9fd32b9a` | `96a0fb304` |
| `TOOL-dFairHearing-32@rev-1` | `c9fd32b9a` | `96a0fb304` |

For each address:

1. Read the spec's diff over each revising commit, `git diff <commit>~1 <commit> -- <spec path>`, to see what changed.
   - Most are a later spec-audit round's disposal folding a hands-off edge to a unit it promoted, with a rev bump and a §9 line.
   - Unit 14's change at `96a0fb304` may also carry the round-4 fold. Its earlier edge removal is rev-3 itself (`32afb3770`).
2. Write `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-<n>-deviation-<n>9.md`: `-19`, `-39`, `-149`, `-159`, `-169`, `-309` or `-329`. Use the grammar of `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-24-deviation-38.md`:
   - **Departs from:** the address above.
   - **Hand-off:** `spec-revised`.
   - **Before** and **After:** what each revising commit changed, verbatim enough to check.
   - **Cause:** `review finding`, for a disposal fold.
   - **Reason:** why the audited spec moved.
   - **Evidence:** the commits and the audit record whose disposal made the fold.
   - **Risk:** `editorial` when only an edge or §9 line moved and no criterion or design changed, else `additive`.
   - **Approver:** spec writer, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`).
   - **Follow-through:** `none`.
   - **Caused-by:** `PLAY-dClosedLoop-2`.

Touch no spec. Do not commit, stage, or run the build-index generator or any gate. Report each record's path and its Before/After lines.

## The report's unjoined entries, verbatim

  - entry 13 · member · TOOL-dFairHearing-1@rev-2 · spec-revised · TOOL-dFairHearing-1's spec changed at 32afb3770, past its audited revision rev-2 (c993af496) · recorded by nobody
  - entry 14 · member · TOOL-dFairHearing-14@rev-3 · spec-revised · TOOL-dFairHearing-14's spec changed at 96a0fb304, past its audited revision rev-3 (92dd0f46a) · recorded by nobody
  - entry 15 · member · TOOL-dFairHearing-15@rev-1 · spec-revised · TOOL-dFairHearing-15's spec changed at 32afb3770, past its audited revision rev-1 (c993af496) · recorded by nobody
  - entry 16 · member · TOOL-dFairHearing-15@rev-1 · spec-revised · TOOL-dFairHearing-15's spec changed at 92dd0f46a, past its audited revision rev-1 (c993af496) · recorded by nobody
  - entry 17 · member · TOOL-dFairHearing-15@rev-1 · spec-revised · TOOL-dFairHearing-15's spec changed at 96a0fb304, past its audited revision rev-1 (c993af496) · recorded by nobody
  - entry 18 · member · TOOL-dFairHearing-16@rev-1 · spec-revised · TOOL-dFairHearing-16's spec changed at 32afb3770, past its audited revision rev-1 (c993af496) · recorded by nobody
  - entry 19 · member · TOOL-dFairHearing-16@rev-1 · spec-revised · TOOL-dFairHearing-16's spec changed at 92dd0f46a, past its audited revision rev-1 (c993af496) · recorded by nobody
  - entry 20 · member · TOOL-dFairHearing-16@rev-1 · spec-revised · TOOL-dFairHearing-16's spec changed at 96a0fb304, past its audited revision rev-1 (c993af496) · recorded by nobody
  - entry 21 · member · TOOL-dFairHearing-3@rev-1 · spec-revised · TOOL-dFairHearing-3's spec changed at 92dd0f46a, past its audited revision rev-1 (c993af496) · recorded by nobody
  - entry 22 · member · TOOL-dFairHearing-30@rev-1 · spec-revised · TOOL-dFairHearing-30's spec changed at c9fd32b9a, past its audited revision rev-1 (96a0fb304) · recorded by nobody
  - entry 23 · member · TOOL-dFairHearing-32@rev-1 · spec-revised · TOOL-dFairHearing-32's spec changed at c9fd32b9a, past its audited revision rev-1 (96a0fb304) · recorded by nobody
