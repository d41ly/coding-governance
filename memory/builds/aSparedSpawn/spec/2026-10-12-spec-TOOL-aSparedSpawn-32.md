# TOOL-aSparedSpawn-32 — reconcile the build with origin/main 37200355

**Status:** INPROGRESS · rev-2 · 2026-10-12 · node a · Tier-2 · base fce4b707 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-prompt-TOOL-aSparedSpawn-32-build-brief.md](../prompts/2026-10-12-prompt-TOOL-aSparedSpawn-32-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Merge origin/main at 37200355d into the run branch before the close's bar, so that the bar and the
lander grade the tree that will land. Origin is 183 commits past the merge-base 69e0ff0f5. Those
commits carry aDistilledCharter, aFrugalTurnstile, dHomedResolver, dRemeasuredRender, aHomedAnchor,
aSparedHolder, aSignalledHook and aBenchedProbe. A trial `git merge --no-commit origin/main` taken
by the driver conflicted in 16 files.

## 2. Scope (IN)

The conflict set is the driver's trial merge at this base; the builder re-takes it at the merge and
records any difference in the ledger. Conflicted files, with hunk counts:

| File | Hunks | Kind |
|---|---|---|
| `tools/run-gates/run-gates.sh` | 11 | product |
| `.githooks/pre-push` | 7 | product |
| `tools/run-gates/run-gates.evidence.test.sh` | 3 | suite |
| `tools/run-gates/README.md` | 3 | doc |
| `tools/run-gates/run-gates.turnstile.test.sh` | 1 | suite |
| `tools/push-main.test.sh` | 1 | suite |
| `tools/memory-tree/check-memory-hygiene.test.sh` | 1 | suite |
| `tools/hooks/agent-cap.test.sh` | 1 | suite |
| `.githooks/pre-push.test.sh` | 1 | suite |
| `.memory-tree.conf` | 1 | conf |
| `memory/guides/SESSION-KICKOFF.md` | 1 | stamps |
| `memory/backlog/TOOL.md` | 1 | generated |
| `memory/map/features/run-gates.md` | 1 | dossier |
| `memory/map/generated/symbols.json`, `MAP.md`, `CARDS.md` | 1 each | generated |

- **S1** — Every conflict in a product, suite or doc file is resolved by keeping BOTH sides' intent,
  never by picking a side. Each conflicted file's merge result is then diffed against BOTH parents,
  so that no hunk either side added is lost. This covers the "auto-took" class, a conflict-free hunk
  silently taken from one side, and the merge-drops-a-side's-hunks class `TOOL-dUnstuckLanding-26`
  names. Where both sides rewrote one function, the result carries both behaviours, and the ledger
  says how they compose. Observed by AC1 and AC2.
- **S2** — Generated files are re-rendered, never hand-merged. `memory/map/generated/symbols.json`,
  `MAP.md` and `CARDS.md` come from `python tools/codebase-map/gen_map.py --write`, and
  `memory/backlog/TOOL.md` and the build index from `python tools/memory-tree/gen_build_index.py --write`,
  each run after the hand-merged sources are resolved and staged. Observed by AC3.
- **S3** — The kickoff manifest's stamps, `last-audit` and `last-body-change` in
  `memory/guides/SESSION-KICKOFF.md`, take origin's side at the merge. They are re-stamped in a
  follow-up commit after the merge commit, per the manifest's merge exception, because a commit
  cannot carry its own sha. Observed by AC4.
- **S4** — The `.memory-tree.conf` conflict is resolved additively, keeping both sides' keys and
  their comment blocks. The run-gates dossier, `memory/map/features/run-gates.md`, is merged by hand
  keeping both sides' claims, and its claims must still name live inventory keys. Observed by AC5.
- **S5** — The post-merge direct checks are green. A row this build owns in
  `memory/project/fork-ceilings.txt` or `memory/project/spawn-idiom-sites.txt` is re-measured when
  origin's changes to the runner or the hook moved its count, and the ledger records both readings.
  Observed by AC6.

## 3. Non-goals (OUT)

- A kit version mint. The lander mints every carrier at `--prepare`.
- Running any suite or the bar inside the pass. The close's bar runs once, after this unit.
- Any behaviour change beyond reconciling the two sides. A defect found in either side's code is
  recorded as an ask, not fixed here.
- Re-deriving origin's own records, decisions or backlog rows. They arrive as origin wrote them.

### Edges

none

## 4. Design

The merge follows the build's earlier reconcile, b9b24646f, and aMeteredSweep's two, 345900823 and
2da5ad1d6: a `--no-ff` merge commit named `merge: origin/main 37200355 into aSparedSpawn`, then a
pass commit, then a stamps commit. The merge commit carries `Pass: none`, as those three did: the
commit-msg hook's `--check-commit` grades a trailered commit's whole index against the pass's
declaration, a merge's index holds every path origin's 183 commits moved, and two of them,
`memory/DECISIONS.md` and `memory/project/readme-contract.txt`, are shared records `--dispatch`
refuses to declare. A merge commit also lists no paths to `diff-tree`, so check 23 could not
attribute the pass to it. The pass commit after it, `Pass: TOOL-aSparedSpawn-32`, carries this
spec's CLOSED header and the acceptance ledger, which is a write check 23 can grade. The order
inside the merge is fixed so that generated output is rendered from the resolved sources:

1. Resolve the product, suite and doc conflicts by hand, both sides kept, and stage them.
2. Resolve `.memory-tree.conf` and the run-gates dossier additively, and stage them.
3. Take origin's side of the manifest stamps.
4. Run `gen_map.py --write` and `gen_build_index.py --write`, and stage what they change.
5. Run the two-parent diff over every conflicted file and record the result in the ledger.
6. Run the direct checks, then commit the merge.

The two-parent diff reads, per conflicted file F, every line `git diff 69e0ff0f5 37200355d -- F`
adds and every line `git diff 69e0ff0f5 fce4b707 -- F` adds, and checks each is present in the
result or is justified by a ledger line. The justification is either a line the other side rewrote
on purpose or a line both sides moved.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `.githooks/pre-push`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.turnstile.test.sh`
- `tools/push-main.test.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/hooks/agent-cap.test.sh`
- `.githooks/pre-push.test.sh`
- `.memory-tree.conf`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/backlog/TOOL.md`
- `memory/map/features/run-gates.md`
- `memory/map/generated/symbols.json`
- `memory/map/generated/MAP.md`
- `memory/map/generated/CARDS.md`
- `memory/project/fork-ceilings.txt`
- `memory/project/spawn-idiom-sites.txt`

### Alternatives rejected

- **Rebase the run branch onto origin.** It rewrites the build's recorded shas, which its ledgers,
  its review record and `RUN.md` cite.
- **Merge after the close's bar.** The bar would grade a tree that never lands, and the lander's
  own reconcile would meet these 16 conflicts with no unit to own them.
- **Take origin's side of the generated map files and re-render later.** The files would then
  describe neither parent until the re-render, and the map freshness leg grades every commit.

## 5. Production-readiness checklist

- security: the merged hook and runner keep both sides' scrubs and refusals; S1's two-parent diff is what shows none was dropped.
- perf / scale: N/A — no new code path; a re-measured fork row records origin's cost, not a change of this unit's.
- error / empty / loading states: N/A — no behaviour change beyond reconciling.
- observability: the ledger records each conflicted file's resolution and its two-parent diff result.
- risks: a conflict resolved by picking a side drops a behaviour silently; S1's diff is the check, and a hunk both sides rewrote is the case to read twice.
- testing: the direct checks in AC6 at the merge; the suites and the bar run at the close.
- migration: N/A — no data or schema moves.
- user docs: `tools/run-gates/README.md` keeps both sides' sections.

## 6. Acceptance criteria

- **AC1** — When, for each conflicted product, suite or doc file F, every line
  `git diff 69e0ff0f5 37200355d -- F` adds is searched for in the merge result, each is present or
  carries a justification in the ledger. Red when: a line origin added is absent and unjustified.
- **AC2** — When the same search runs for every line `git diff 69e0ff0f5 fce4b707 -- F` adds, each
  is present or justified. Red when: a line this build added is absent and unjustified.
- **AC3** — When `python tools/codebase-map/gen_map.py --check` runs on the merge commit, it exits 0,
  and `python tools/memory-tree/gen_build_index.py --write` leaves no diff. Red when: either reports
  a generated file stale, or a hand-merged one differs from its render.
- **AC4** — When `grep -n 'last-audit\|last-body-change' memory/guides/SESSION-KICKOFF.md` runs
  after the stamps commit, the audit stamp names the merge commit's sha. Red when: it still carries
  either parent's stamp.
- **AC5** — When `grep -c '^<<<<<<<\|^>>>>>>>' .memory-tree.conf memory/map/features/run-gates.md`
  runs, it counts 0 in each, and every key either parent's conf declares is declared in
  the result. Red when: a marker survives, or a key either side added is missing.
- **AC6** — When the merge commit is checked out, all of these exit 0:
  - `bash -n` on every conflicted shell file;
  - `python tools/govkit/govkit.py selfcheck`;
  - `python tools/memory-tree/check-arms.py --check`;
  - `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`;
  - `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only run-gates-1leg`, and
    the same with `--only run-gates-2leg`;
  - `python tools/codebase-map/gen_map.py --check`;
  - `python tools/check-spec-tokens.py`;
  - `bash tools/memory-tree/check-memory-hygiene.sh --staged`.

  Red when: any exits non-zero.
  figure: each fork count is DERIVED at observation; a row re-measured here records both readings.

## 7. Gates

`run-gates evidence` · `run-gates canary` · `run-gates gov canary` · `run-gates turnstile` ·
`run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `pre-push self-test` ·
`pre-push bar self-test` · `pre-push run-log line` · `push-main self-test` · `branch-guard self-test` ·
`python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` ·
`transition-audit arms` · `straggler-guard arms` · `recall floor arms` · `recall floor` ·
`memory hygiene` · `codebase-map coverage + freshness` · `agent-cap self-test` ·
`shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` ·
`harness arms (fail branches armed or pinned)` · `govkit selfcheck` · `manifest-check self-test` ·
`scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` ·
`hook destinations self-test` · `kit/dogfood doc parity`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft.
- rev-2 · 2026-10-12 · §4: the merge commit carries `Pass: none` and a pass commit after it carries the CLOSED header and the ledger, because `--check-commit` refused a trailered merge for staging `memory/DECISIONS.md`, a shared record no dispatch may declare, and `diff-tree` lists no paths for a merge commit.

## 10. Reuse audit

No existing seam fits: a reconcile is a git operation, and `tools/codebase-map/reuse_lookup.py`
indexes code symbols, not procedures. The precedent this unit follows is the build's own earlier
reconcile, b9b24646f (origin/main 69e0ff0f5 into aSparedSpawn), and aMeteredSweep's two,
345900823 and 2da5ad1d6, each a `--no-ff` merge with generated files re-rendered and stamps
re-taken after. The two-parent diff is the check the charter's §1 Landing rule names for the
auto-took class.

Recall terms used: reconcile merge origin/main auto-took two parents generated re-render
last-audit stamps merge exception conflict dossier additive
