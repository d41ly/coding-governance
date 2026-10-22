**Serves:** research TOOL-dTrueNorth-23 TOOL-dTrueNorth-24 TOOL-dTrueNorth-25

# Spec brief — dTrueNorth, the closing review's three promoted highs

## The prompt

> The closing diff review of dTrueNorth (round 1, CLEAN WITH FIXES, 0 blockers, 3 high, 19 minors, CONVERGED) promotes each high to a unit whose mechanism closes it (BUILD-METHOD M4, M8). The owner capped spec audits at two rounds, so these specs are built as written, unaudited.

## The brief

### Goal
Author three specs, one per promoted high, each a unit whose mechanism closes its finding and leaves a regression arm for its class: TOOL-dTrueNorth-23 closes item H1, TOOL-dTrueNorth-24 item H2, TOOL-dTrueNorth-25 item H3, all in `memory/builds/dTrueNorth/reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md`. Author only: no product code, no commit, no gate.

### Items
1. TOOL-dTrueNorth-23 — H1 (finding 2): `design_lib.read_spec_revisions` and `tree_lib.read_adding_commits` read zero revisions under an ambient `GIT_LITERAL_PATHSPECS`. Use the review's stated fix, the skeptic's where it corrects the finder's, and cover every `:(glob)` reader in the kit, not only the two named.
2. TOOL-dTrueNorth-24 — H2 (finding 4): `deviation_join.py` dates rescope rows of a rotated `RUN.<phase>.<blob8>.md` archive by the rotation commit, not the commit that wrote the row.
3. TOOL-dTrueNorth-25 — H3 (finding 11, and finding 20 which is M7, the same defect): the DELEGATES list in `tools/memory-tree/check-verdict-epoch.sh` leaves out `deviation_join.py`, so a change to it can move check 30's verdicts with no version bump; and AC34 of TOOL-dTrueNorth-20 cannot show its own red-when. Name in Scope that this unit discharges M7, so the minors batch need not.
4. Each spec: path `memory/builds/dTrueNorth/spec/2026-10-22-spec-TOOL-dTrueNorth-<n>.md`, H1 `# TOOL-dTrueNorth-<n> — <title>` with an em dash, status `OPEN`, Tier-2, `streams tooling`, `order 9`, a column-0 `**Derived:** PLAY-dClosedLoop-2` line, the review's ids in §1, §3 Edges naming the units whose code it amends, a `New arm:` line for its regression arm, §8 forks resolved by README rule 6's rungs, and §10's two probes run.
5. Write each unit's deviation record beside its spec, in the `deviation` kind's grammar (read any existing `memory/builds/dTrueNorth/build/*-deviation-*.md`): `2026-10-22-build-TOOL-dTrueNorth-<n>-deviation-<m>.md`, numbers 22, 23 and 24 in unit order; Departs from `dTrueNorth [roster]`, hand-off design-to-spec, cause review finding, risk additive, approver spec writer under author-recorded (`PLAY-dClosedLoop-4`), follow-through `new unit TOOL-dTrueNorth-<n>`, Caused-by `PLAY-dClosedLoop-2`.

### Acceptance
`python tools/check-spec-tokens.py` prints no hit on the three specs; every acceptance criterion is a probe a pass can run without a gate; each record reads with no malformed field under `python tools/memory-tree/deviation_join.py`.

### Gates
No gate runs in this pass; each spec's §7 lists what the close runs.

### Non-goals
The 19 minors (TOOL-dTrueNorth-26's); any other unit's spec; product code; inside §6, an untracked file named by full path inside a backticked token; a criterion naming a gate leg, a `*.test.sh` run or the bar.
