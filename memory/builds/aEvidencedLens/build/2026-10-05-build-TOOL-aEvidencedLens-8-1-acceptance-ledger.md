# TOOL-aEvidencedLens-8 — acceptance ledger

**Serves:** journal TOOL-aEvidencedLens-8

The build harness promotes spec-audit minors, batched, and records the counts. The pass commits
`efad66acf` and `877ebb699` record no direct-check figures; the first says `FLOOR_ASSERTIONS` rose by
the 17 static sites added. The criteria are read from the main loop's VERIFYING run of the
unattended-build self-test in a frozen clone at `0c8dd1761`, whose `tools/` matches `5a1643c8d`
except the tier2-review rubric extractor: rc 0, `PASS (610 assertions)`, and every arm named below
printed `ok`. Where a criterion names text the arm label does not show, that is said. Greps were re-run
on the tree at `5a1643c8d` and over `git show efad66acf~1:tools/workflows/unattended-build.js`, the
pass-start render, saved to the scratch. AC11 is read from this build's `RUN.md`.

**Evidences:** TOOL-aEvidencedLens-8
- AC1 — `PROMOTE every MEDIUM and every LOW` — the seven `D8 the disposal prompt carries:` arms printed `ok`, for that phrase, `never one unit per minor`, `disjoint write sets`, and the four S1 markers, with `D8 ...and no longer orders a fold`. A static `grep -cF` of the four S1 markers counted 0 each over the pass-start render and 1 each at `5a1643c8d`; `FOLD every MEDIUM` counted 1 there and 0 at `5a1643c8d`. That reads the file, not a traced prompt over the base render.
- AC2 — `folded` — `D8 folded 1 over a reconciling sum: REFUSED by name` and `D8 ...with an empty roster` printed `ok`; the labels do not show the `disposal: NOT done` log text.
- AC3 — `promotedIds` — `D8 one unit for one high and two minors: REFUSED at the floor`, `D8 ...two units are ACCEPTED` and `D8 ...and the roster is handed out` printed `ok`.
- AC4 — `never one per minor` — `D8 five units for five minors: REFUSED at the ceiling` and `D8 ...two disjoint batches are ACCEPTED` printed `ok`; the labels do not quote the log text.
- AC5 — `--disposition` — `C zero blockers with a high: the record command carries the counts and --disposition promote`, `C zero blockers, nothing standing: the record carries zero counts`, `C ...and no disposition` and `C a clean zero-blocker record carries --highs 0 --minors 0` printed `ok`, as did `R2-B zero blockers, zero highs, a promoted UNVERIFIED finding: the record carries --disposition promote`.
- AC6 — `--blockers 2` — `C two blockers: the first command ends at --blockers 2`, `C ...and the retry appends --highs, --minors and --disposition` and `C ...triggered by a refusal naming any of the three` printed `ok`.
- AC7 — `--minors` — `D8 the DEGRADED note's hand-record command carries the counts` and `D8 ...and adds every promoted UNVERIFIED finding to --minors` printed `ok`.
- AC8 — `FOLD the confirmed findings` — no arm label reads the boundary sentence. At `5a1643c8d`, `grep -c` of that phrase over `tools/workflows/unattended-build.js` printed 1, and line 1292 of the render carries the sentence that this in-loop fold is not the exit's disposition. `CONVERGING: the caller is told what to do next` printed `ok` without naming the text.
- AC9 — `mustFold` — the criterion's `grep -niE` over `tools/workflows/unattended-build.template.js` printed nothing at `5a1643c8d`.
- AC10 — `unitCeiling` — at `5a1643c8d`, `grep -c 'unitCeiling'` printed 4 over the template and 4 over the render, and `node tools/workflows/check-workflow-syntax.js` printed `6 workflow script(s) parsed clean`.
- AC11 — `highs` — `RUN.md` carries the row `review · item aEvidencedLens-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · highs 0 · minors 6 · disposition promote` at 2026-10-05T03:27:29Z, the first spec-audit record after `TOOL-aEvidencedLens-7` landed at 01:40:32Z and this unit at 02:41:26Z; the row exists, so the real driver accepted it. The `spec-set-r2` row at 01:11:02Z predates this unit and carries neither count, and the `spec-set-r4` row carries `highs 1 · minors 14`.
