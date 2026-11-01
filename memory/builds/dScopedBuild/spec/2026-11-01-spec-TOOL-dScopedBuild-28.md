# TOOL-dScopedBuild-28 — the pre-commit hook runs the hygiene leg on a deletion-only memory commit, so check 32's freeze reaches a deleted landed spec

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 4 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md) | research | TOOL-dScopedBuild-25 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-35 |
| [2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-30 TOOL-dScopedBuild-34 TOOL-dScopedBuild-27 TOOL-dScopedBuild-29 TOOL-dScopedBuild-31 TOOL-dScopedBuild-26 TOOL-dScopedBuild-25 TOOL-dScopedBuild-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
confirmed finding **id 14 at HIGH**, report item **H4**. `TOOL-dScopedBuild-14` S8 says
`.githooks/pre-commit` already runs `--staged` whenever `memory/**` is staged. The hook's trigger
reads `--diff-filter=ACMR` (`.githooks/pre-commit:227`), so a commit that only deletes a spec never
runs the hygiene leg. `TOOL-dScopedBuild-2` S2 counts a deletion as a revision and refuses one on a
landed unit, and its AC3 `frozen-delete` calls the verb directly, so the freeze is certified on a
path the hook never reaches.

This unit widens the hook's memory trigger to deletions and observes the freeze refusing a staged
`git rm` of a landed unit's spec through the hook itself. The defect's consequence lands on unit 2's
freeze, whose arm the observation needs, so it builds one step after unit 2 (order 4).

## 2. Scope (IN)

- **S1** — The trigger. The hook's memory-tree hygiene trigger reads
  `git diff --cached --name-only --diff-filter=ACMRD -- 'memory/**'`, so a staged deletion under
  `memory/` runs `check-memory-hygiene.sh --staged` as any other staged memory path does. The
  comment above it says a deletion triggers the leg and why. Observed by AC1.
- **S2** — The gate's own population is unchanged. `check-memory-hygiene.sh --staged` keeps its
  `--diff-filter=ACMR` read (`tools/memory-tree/check-memory-hygiene.sh:664`), so every check that
  grades staged names or bodies still grades nothing on a deletion, as its comment at `:646` states.
  A deletion reaches check 32 through the `deviation_join.py --staged` verb, whose own
  `git diff --cached --name-status -M` read lists it (unit 14 S7, unit 2 S2). Observed by AC1 and AC2.
- **S3** — Unit 14 S8's sentence "`.githooks/pre-commit` already runs `--staged` whenever
  `memory/**` is staged" holds after S1 and is answered in unit 14's acceptance ledger by a note naming
  `TOOL-dScopedBuild-28 S1`; unit 2's ledger answers its AC3 with the hook-level observation of AC2.
  Observed by AC2.

## 3. Non-goals (OUT)

- Grading deletions in the hygiene gate's other checks. S2 keeps their population.
- The deviation arm's own handling of a staged deletion or rename, id 37 of the same audit, a
  MEDIUM, which `TOOL-dScopedBuild-35` S19 takes.
- A push-time freeze over history, which unit 2 §3 excludes; a `--no-verify` commit is not refused.
- The left-shift hook-suite arm the report names beyond AC1's. AC1 is that arm.

### Edges

- **consumes-from** `TOOL-dScopedBuild-14` — S8's check 32 under `--staged`, the hook-reached host whose trigger S1 widens, and S7's `--staged` verb, whose name-status read lists the deletion (id 14)
- **consumes-from** `TOOL-dScopedBuild-2` — S2's frozen arm, which counts a deletion as a revision and refuses one on a landed unit, observed through the hook by AC2 (id 14)
- **hands-off** `TOOL-dScopedBuild-39` — S1's trigger in the adopter snippets, read as `--diff-filter=ACMRD`, §4's Evidence and §5's cost and docs lines, which that unit's S16, S17 and S23 to S26 complete (ids 23, 30, 10, 24, 32, 17)

## 4. Design

### Evidence

- `.githooks/pre-commit:226-233`: the "memory-tree hygiene, staged leg" runs only when
  `git diff --cached --name-only --diff-filter=ACMR -- 'memory/**'` lists a path.
- `tools/memory-tree/check-memory-hygiene.sh:640-664` builds `STAGED_SET` from an ACMR name-status
  read and says "A staged DELETION is graded by nothing here, as before"; with S1 a deletion-only
  commit runs the gate with an empty staged set, and its narrowed listing then grades the deleted
  path's own build folder only.
- `.githooks/pre-commit.test.sh:128-158` already drives the leg through a stand-in gate that prints
  `HYGIENE RAN from <dir> <args>`, run by the `branch-guard self-test` leg; AC1 adds one fixture to
  that shape.
- The hygiene leg costs about 20 s per commit on node a (TOOL-aTrimmedHook-8, filed 2026-10-11), so S1
  adds that cost to a deletion-only memory commit, which paid none before.

### Inventory

Minted: nothing in product code; one hook-suite fixture. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 4, one step after unit 2 (order 3), tied with unit 3. The hook change is live at
landing; a deletion-only memory commit then pays the hygiene leg.

### Files touched (estimate)

- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`

### Alternatives rejected

- **State the gap in both specs' "What it does not check".** It leaves a landed spec deletable at the
  commit with a green hook, which is the freeze unit 2 exists to hold.
- **Widen the gate's own staged read to D as well.** Every name and body check would then read a
  path with no index blob; the verb that needs the deletion already reads it.

## 5. Production-readiness checklist

- security — the change denies more: a deleted landed spec now meets the freeze at the commit.
- perf / scale — a deletion-only memory commit runs the hygiene leg, about 20 s on node a.
- error / empty / loading states — an empty staged set grades nothing and passes, as S2 states.
- observability — the gate's lines and check 32's `frozen` line print as on any memory commit.
- risks — a deletion-only commit of an unlanded spec now runs the gate; AC2 observes that it commits.
- testing — AC1 in the hook suite, AC2 in a scratch clone at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When a scratch repo whose hooks path holds the built hook, and whose root-install hygiene
  gate is a stand-in printing `HYGIENE RAN from <dir> <args>`, tracks one file under its memory
  folder, stages `git rm` of that file and runs `git commit`, the output holds
  `HYGIENE RAN from memory-tree --staged`.
  Red when: a deletion-only memory commit prints no `HYGIENE RAN`, the `ACMR` trigger.
  fixture: a repo built as `run_prefix_commit` builds one at the root rung, its memory file the
  fixture's own relative path, passed to `git rm` as an argument.
- **AC2** — When a scratch clone whose remote's `main` holds unit A's spec `CLOSED` stages
  `git rm` of that spec and runs `git commit` through the built hook, the commit is refused with a
  line naming `frozen` and A; the same deletion of an `OPEN` unit's spec commits.
  Red when: the landed spec's deletion commits, or an unlanded one is refused.
  fixture: a clone under `%TEMP%/<short-name>` with a bare remote, as unit 2 AC1 builds one.
  permission: the main loop's, at the close, after unit 2 is built.

## 7. Gates

`branch-guard self-test` · `memory hygiene` · `memory-hygiene self-test` · `spec tokens (a spec's own names resolve)`

New arm: .githooks/pre-commit.test.sh · covers AC1 · a deletion-only memory commit over the stand-in gate, staged by restoring `--diff-filter=ACMR` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1
  set. widens: none · relaxes: none
- **F2 — Which unit does this promotion repair, for its order?** Options: (a) unit 14, order 3; (b)
  unit 2, order 4. The finding's sentence is unit 14's, but AC2 observes unit 2's frozen arm, and at
  order 3 the unit would tie with unit 2 and could not read it. RESOLVED (agent, 2026-11-01,
  delegated): (b), rung 3, the survivor whose criterion can run. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15, id 14
  (HIGH, item H4).
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-39,
  the promotions of the round-1 spec audit of units 25 to 35 (ids 10, 17, 23, 24, 30, 32).

## 10. Reuse audit

The seam is the hook's own trigger line (`.githooks/pre-commit:227`) and the hook suite's stand-in
gate fixture (`.githooks/pre-commit.test.sh:128-158`), extended by one filter letter and one fixture.
`python tools/codebase-map/reuse_lookup.py "run the hygiene leg in the pre-commit hook when a memory
file is deleted"` ranked `run`, `pre`, `legs`, `leg` and `run_git`, name-token hits and none a hook
trigger, so no existing seam fits beyond the two named. The recall probe surfaced TOOL-aTrimmedHook-8,
whose measured hygiene-leg cost §4 cites.

Recall terms used: `python tools/memory-recall/query.py "does the pre-commit hook run hygiene on a deletion-only commit" --terms "pre-commit diff-filter ACMR deletion staged hygiene check frozen spec landed unit"`
