**Serves:** research TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-29

# Departures brief — thirty-five spec addresses revised past their first pass, recorded by nobody

The departures report, `deviations.py --report dCalibratedLens` on the prepared merge `15116b2b` (README rule 4), lists
64 members that no deviation record joins, each a spec changed after its first pass `59d3d8e57` or past its audited
revision. README rule 4 owes a record for each. A record joins a member by its **Departs from:** value
`<unit>@rev-N` and **Hand-off:** `spec-revised` (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py`,
its header's grammar), so one record per address covers every entry with that address, and thirty-five are owed.

The revising commits:

- `5e8c07f79`: the spec-token fix pass and the hands-off mirror pass, made before any audit: section-6 paths cited by
  basename, two suite observations moved to `New arm:` lines, hands-off edges mirrored, and units 8, 10 and 11
  re-pinned to the clause their own deviation record amends.
- `31588f5f0`: the round-1 spec audit's disposal folds (`memory/builds/dCalibratedLens/reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`).
- `530cadfbd`: the round-2 audit's disposal folds (`…/reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`).
- `2e6c6e34c`: the round-3 audit's disposal folds (`…/reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`).

| Address | Revised in | Against | Record to write |
|---|---|---|---|
| TOOL-dCalibratedLens-1@rev-1 | 31588f5f0, 530cadfbd, 5e8c07f79 | audited 31588f5f0, first-pass 59d3d8e57 | `deviation-12` |
| TOOL-dCalibratedLens-1@rev-2 | 530cadfbd | first-pass 59d3d8e57 | `deviation-13` |
| TOOL-dCalibratedLens-10@rev-1 | 2e6c6e34c, 31588f5f0, 530cadfbd, 5e8c07f79 | audited 31588f5f0, first-pass 59d3d8e57 | `deviation-102` |
| TOOL-dCalibratedLens-10@rev-2 | 530cadfbd | first-pass 59d3d8e57 | `deviation-103` |
| TOOL-dCalibratedLens-10@rev-3 | 2e6c6e34c | first-pass 59d3d8e57 | `deviation-104` |
| TOOL-dCalibratedLens-11@rev-1 | 31588f5f0, 5e8c07f79 | first-pass 59d3d8e57 | `deviation-112` |
| TOOL-dCalibratedLens-12@rev-1 | 31588f5f0 | first-pass 59d3d8e57 | `deviation-122` |
| TOOL-dCalibratedLens-13@rev-1 | 31588f5f0, 5e8c07f79 | first-pass 59d3d8e57 | `deviation-132` |
| TOOL-dCalibratedLens-14@rev-1 | 31588f5f0, 5e8c07f79 | first-pass 59d3d8e57 | `deviation-142` |
| TOOL-dCalibratedLens-15@rev-1 | 31588f5f0, 5e8c07f79 | first-pass 59d3d8e57 | `deviation-152` |
| TOOL-dCalibratedLens-16@rev-1 | 31588f5f0, 5e8c07f79 | first-pass 59d3d8e57 | `deviation-162` |
| TOOL-dCalibratedLens-17@rev-1 | 31588f5f0, 5e8c07f79 | first-pass 59d3d8e57 | `deviation-172` |
| TOOL-dCalibratedLens-2@rev-1 | 2e6c6e34c, 31588f5f0, 530cadfbd, 5e8c07f79 | audited 31588f5f0, first-pass 59d3d8e57 | `deviation-22` |
| TOOL-dCalibratedLens-2@rev-2 | 530cadfbd | first-pass 59d3d8e57 | `deviation-23` |
| TOOL-dCalibratedLens-2@rev-3 | 2e6c6e34c | first-pass 59d3d8e57 | `deviation-24` |
| TOOL-dCalibratedLens-21@rev-1 | 2e6c6e34c | audited 530cadfbd | `deviation-212` |
| TOOL-dCalibratedLens-23@rev-1 | 2e6c6e34c | audited 530cadfbd | `deviation-232` |
| TOOL-dCalibratedLens-25@rev-1 | 2e6c6e34c | audited 530cadfbd | `deviation-252` |
| TOOL-dCalibratedLens-29@rev-1 | 2e6c6e34c | audited 530cadfbd | `deviation-292` |
| TOOL-dCalibratedLens-3@rev-1 | 2e6c6e34c, 31588f5f0, 530cadfbd, 5e8c07f79 | audited 31588f5f0, first-pass 59d3d8e57 | `deviation-32` |
| TOOL-dCalibratedLens-3@rev-2 | 530cadfbd | first-pass 59d3d8e57 | `deviation-33` |
| TOOL-dCalibratedLens-3@rev-3 | 2e6c6e34c | first-pass 59d3d8e57 | `deviation-34` |
| TOOL-dCalibratedLens-4@rev-1 | 2e6c6e34c, 31588f5f0, 530cadfbd, 5e8c07f79 | audited 31588f5f0, first-pass 59d3d8e57 | `deviation-42` |
| TOOL-dCalibratedLens-4@rev-2 | 530cadfbd | first-pass 59d3d8e57 | `deviation-43` |
| TOOL-dCalibratedLens-4@rev-3 | 2e6c6e34c | first-pass 59d3d8e57 | `deviation-44` |
| TOOL-dCalibratedLens-5@rev-1 | 2e6c6e34c, 31588f5f0, 530cadfbd, 5e8c07f79 | audited 31588f5f0, first-pass 59d3d8e57 | `deviation-52` |
| TOOL-dCalibratedLens-5@rev-2 | 530cadfbd | first-pass 59d3d8e57 | `deviation-53` |
| TOOL-dCalibratedLens-5@rev-3 | 2e6c6e34c | first-pass 59d3d8e57 | `deviation-54` |
| TOOL-dCalibratedLens-6@rev-1 | 2e6c6e34c, 31588f5f0, 530cadfbd, 5e8c07f79 | audited 31588f5f0, first-pass 59d3d8e57 | `deviation-62` |
| TOOL-dCalibratedLens-6@rev-2 | 530cadfbd | first-pass 59d3d8e57 | `deviation-63` |
| TOOL-dCalibratedLens-6@rev-3 | 2e6c6e34c | first-pass 59d3d8e57 | `deviation-64` |
| TOOL-dCalibratedLens-7@rev-1 | 31588f5f0, 5e8c07f79 | first-pass 59d3d8e57 | `deviation-72` |
| TOOL-dCalibratedLens-8@rev-1 | 2e6c6e34c, 31588f5f0, 5e8c07f79 | audited 31588f5f0, first-pass 59d3d8e57 | `deviation-82` |
| TOOL-dCalibratedLens-8@rev-2 | 2e6c6e34c | first-pass 59d3d8e57 | `deviation-83` |
| TOOL-dCalibratedLens-9@rev-1 | 31588f5f0 | first-pass 59d3d8e57 | `deviation-92` |

For each address:

1. Read the spec's diff over each revising commit, `git diff <commit>~1 <commit> -- <spec path>`, to see what changed.
2. Write `memory/builds/dCalibratedLens/build/<date>-build-TOOL-dCalibratedLens-<n>-deviation-<k>.md`, `<k>` from the
   table's last column and `<date>` the revising commit's date (`2026-11-02` or `2026-11-03`), in the grammar of
   `memory/builds/dFairHearing/build/2026-10-23-build-TOOL-dFairHearing-1-deviation-19.md`:
   - **Departs from:** the address. **Hand-off:** `spec-revised`.
   - **Before** and **After:** what each revising commit changed, verbatim enough to check.
   - **Cause:** `review finding` for a disposal fold; for the `5e8c07f79` pass, the cause value that grammar
     names for a gate finding (read the reader's allowed set in `deviations.py` before choosing).
   - **Reason** and **Evidence:** the commits and, for a fold, the audit record and finding ids whose disposal made it.
   - **Risk:** `editorial` when only an edge, a path spelling, a pin or a §9 line moved and no criterion or design
     changed, else `additive`.
   - **Approver:** spec writer, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`), in the exemplar's
     wording. **Follow-through:** `usage spec-audit-fold` (the record reader rejects `none`). **Caused-by:**
     `PLAY-dClosedLoop-2`.

Touch no spec. Do not commit, stage, or run the build-index generator or any gate. Report each record's path.

## The report's unjoined entries, verbatim

  - entry 7 · member · TOOL-dCalibratedLens-1@rev-1 · spec-revised · TOOL-dCalibratedLens-1's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 8 · member · TOOL-dCalibratedLens-1@rev-1 · spec-revised · TOOL-dCalibratedLens-1's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 9 · member · TOOL-dCalibratedLens-1@rev-2 · spec-revised · TOOL-dCalibratedLens-1's spec changed at 530cadfbd, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 10 · member · TOOL-dCalibratedLens-1@rev-1 · spec-revised · TOOL-dCalibratedLens-1's spec changed at 530cadfbd, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 11 · member · TOOL-dCalibratedLens-10@rev-1 · spec-revised · TOOL-dCalibratedLens-10's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 12 · member · TOOL-dCalibratedLens-10@rev-1 · spec-revised · TOOL-dCalibratedLens-10's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 13 · member · TOOL-dCalibratedLens-10@rev-2 · spec-revised · TOOL-dCalibratedLens-10's spec changed at 530cadfbd, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 14 · member · TOOL-dCalibratedLens-10@rev-1 · spec-revised · TOOL-dCalibratedLens-10's spec changed at 530cadfbd, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 15 · member · TOOL-dCalibratedLens-10@rev-3 · spec-revised · TOOL-dCalibratedLens-10's spec changed at 2e6c6e34c, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 16 · member · TOOL-dCalibratedLens-10@rev-1 · spec-revised · TOOL-dCalibratedLens-10's spec changed at 2e6c6e34c, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 17 · member · TOOL-dCalibratedLens-11@rev-1 · spec-revised · TOOL-dCalibratedLens-11's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 18 · member · TOOL-dCalibratedLens-11@rev-1 · spec-revised · TOOL-dCalibratedLens-11's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 19 · member · TOOL-dCalibratedLens-12@rev-1 · spec-revised · TOOL-dCalibratedLens-12's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 20 · member · TOOL-dCalibratedLens-13@rev-1 · spec-revised · TOOL-dCalibratedLens-13's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 21 · member · TOOL-dCalibratedLens-13@rev-1 · spec-revised · TOOL-dCalibratedLens-13's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 22 · member · TOOL-dCalibratedLens-14@rev-1 · spec-revised · TOOL-dCalibratedLens-14's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 23 · member · TOOL-dCalibratedLens-14@rev-1 · spec-revised · TOOL-dCalibratedLens-14's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 24 · member · TOOL-dCalibratedLens-15@rev-1 · spec-revised · TOOL-dCalibratedLens-15's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 25 · member · TOOL-dCalibratedLens-15@rev-1 · spec-revised · TOOL-dCalibratedLens-15's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 26 · member · TOOL-dCalibratedLens-16@rev-1 · spec-revised · TOOL-dCalibratedLens-16's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 27 · member · TOOL-dCalibratedLens-16@rev-1 · spec-revised · TOOL-dCalibratedLens-16's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 28 · member · TOOL-dCalibratedLens-17@rev-1 · spec-revised · TOOL-dCalibratedLens-17's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 29 · member · TOOL-dCalibratedLens-17@rev-1 · spec-revised · TOOL-dCalibratedLens-17's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 30 · member · TOOL-dCalibratedLens-2@rev-1 · spec-revised · TOOL-dCalibratedLens-2's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 31 · member · TOOL-dCalibratedLens-2@rev-1 · spec-revised · TOOL-dCalibratedLens-2's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 32 · member · TOOL-dCalibratedLens-2@rev-2 · spec-revised · TOOL-dCalibratedLens-2's spec changed at 530cadfbd, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 33 · member · TOOL-dCalibratedLens-2@rev-1 · spec-revised · TOOL-dCalibratedLens-2's spec changed at 530cadfbd, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 34 · member · TOOL-dCalibratedLens-2@rev-3 · spec-revised · TOOL-dCalibratedLens-2's spec changed at 2e6c6e34c, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 35 · member · TOOL-dCalibratedLens-2@rev-1 · spec-revised · TOOL-dCalibratedLens-2's spec changed at 2e6c6e34c, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 36 · member · TOOL-dCalibratedLens-21@rev-1 · spec-revised · TOOL-dCalibratedLens-21's spec changed at 2e6c6e34c, past its audited revision rev-1 (530cadfbd) · recorded by nobody
  - entry 37 · member · TOOL-dCalibratedLens-23@rev-1 · spec-revised · TOOL-dCalibratedLens-23's spec changed at 2e6c6e34c, past its audited revision rev-1 (530cadfbd) · recorded by nobody
  - entry 38 · member · TOOL-dCalibratedLens-25@rev-1 · spec-revised · TOOL-dCalibratedLens-25's spec changed at 2e6c6e34c, past its audited revision rev-1 (530cadfbd) · recorded by nobody
  - entry 39 · member · TOOL-dCalibratedLens-29@rev-1 · spec-revised · TOOL-dCalibratedLens-29's spec changed at 2e6c6e34c, past its audited revision rev-1 (530cadfbd) · recorded by nobody
  - entry 40 · member · TOOL-dCalibratedLens-3@rev-1 · spec-revised · TOOL-dCalibratedLens-3's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 41 · member · TOOL-dCalibratedLens-3@rev-1 · spec-revised · TOOL-dCalibratedLens-3's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 42 · member · TOOL-dCalibratedLens-3@rev-2 · spec-revised · TOOL-dCalibratedLens-3's spec changed at 530cadfbd, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 43 · member · TOOL-dCalibratedLens-3@rev-1 · spec-revised · TOOL-dCalibratedLens-3's spec changed at 530cadfbd, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 44 · member · TOOL-dCalibratedLens-3@rev-3 · spec-revised · TOOL-dCalibratedLens-3's spec changed at 2e6c6e34c, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 45 · member · TOOL-dCalibratedLens-3@rev-1 · spec-revised · TOOL-dCalibratedLens-3's spec changed at 2e6c6e34c, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 46 · member · TOOL-dCalibratedLens-4@rev-1 · spec-revised · TOOL-dCalibratedLens-4's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 47 · member · TOOL-dCalibratedLens-4@rev-1 · spec-revised · TOOL-dCalibratedLens-4's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 48 · member · TOOL-dCalibratedLens-4@rev-2 · spec-revised · TOOL-dCalibratedLens-4's spec changed at 530cadfbd, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 49 · member · TOOL-dCalibratedLens-4@rev-1 · spec-revised · TOOL-dCalibratedLens-4's spec changed at 530cadfbd, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 50 · member · TOOL-dCalibratedLens-4@rev-3 · spec-revised · TOOL-dCalibratedLens-4's spec changed at 2e6c6e34c, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 51 · member · TOOL-dCalibratedLens-4@rev-1 · spec-revised · TOOL-dCalibratedLens-4's spec changed at 2e6c6e34c, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 52 · member · TOOL-dCalibratedLens-5@rev-1 · spec-revised · TOOL-dCalibratedLens-5's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 53 · member · TOOL-dCalibratedLens-5@rev-1 · spec-revised · TOOL-dCalibratedLens-5's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 54 · member · TOOL-dCalibratedLens-5@rev-2 · spec-revised · TOOL-dCalibratedLens-5's spec changed at 530cadfbd, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 55 · member · TOOL-dCalibratedLens-5@rev-1 · spec-revised · TOOL-dCalibratedLens-5's spec changed at 530cadfbd, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 56 · member · TOOL-dCalibratedLens-5@rev-3 · spec-revised · TOOL-dCalibratedLens-5's spec changed at 2e6c6e34c, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 57 · member · TOOL-dCalibratedLens-5@rev-1 · spec-revised · TOOL-dCalibratedLens-5's spec changed at 2e6c6e34c, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 58 · member · TOOL-dCalibratedLens-6@rev-1 · spec-revised · TOOL-dCalibratedLens-6's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 59 · member · TOOL-dCalibratedLens-6@rev-1 · spec-revised · TOOL-dCalibratedLens-6's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 60 · member · TOOL-dCalibratedLens-6@rev-2 · spec-revised · TOOL-dCalibratedLens-6's spec changed at 530cadfbd, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 61 · member · TOOL-dCalibratedLens-6@rev-1 · spec-revised · TOOL-dCalibratedLens-6's spec changed at 530cadfbd, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 62 · member · TOOL-dCalibratedLens-6@rev-3 · spec-revised · TOOL-dCalibratedLens-6's spec changed at 2e6c6e34c, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 63 · member · TOOL-dCalibratedLens-6@rev-1 · spec-revised · TOOL-dCalibratedLens-6's spec changed at 2e6c6e34c, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 64 · member · TOOL-dCalibratedLens-7@rev-1 · spec-revised · TOOL-dCalibratedLens-7's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 65 · member · TOOL-dCalibratedLens-7@rev-1 · spec-revised · TOOL-dCalibratedLens-7's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 66 · member · TOOL-dCalibratedLens-8@rev-1 · spec-revised · TOOL-dCalibratedLens-8's spec changed at 5e8c07f79, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 67 · member · TOOL-dCalibratedLens-8@rev-1 · spec-revised · TOOL-dCalibratedLens-8's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 68 · member · TOOL-dCalibratedLens-8@rev-2 · spec-revised · TOOL-dCalibratedLens-8's spec changed at 2e6c6e34c, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
  - entry 69 · member · TOOL-dCalibratedLens-8@rev-1 · spec-revised · TOOL-dCalibratedLens-8's spec changed at 2e6c6e34c, past its audited revision rev-1 (31588f5f0) · recorded by nobody
  - entry 70 · member · TOOL-dCalibratedLens-9@rev-1 · spec-revised · TOOL-dCalibratedLens-9's spec changed at 31588f5f0, not an ancestor of its first pass 59d3d8e57 · recorded by nobody
