# TOOL-aSparedSpawn-34 — reconcile the build with local main, so it lands there conflict-free

**Status:** CLOSED · rev-1 · 2026-10-13 · node a · Tier-2 · base 249b4ab6 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-aSparedSpawn-34-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aSparedSpawn-34-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-aSparedSpawn-34-build-brief.md](../prompts/2026-10-13-prompt-TOOL-aSparedSpawn-34-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Merge LOCAL `main` into the run branch, so the completed build then merges onto local `main` with no
conflict. The owner asked on 2026-10-13 for the build to land on local `main` and stop there; the
gates run later, by the owner, on the fully reconciled tree. Local `main` was 6081d92e4 when this
spec was written, 200 commits past origin/main 6e8f8b1da, carrying aTrimmedHook, aBriskPreflight and
aOrientedCast merged locally and unpushed. This branch already holds origin/main 6e8f8b1da through
`TOOL-aSparedSpawn-32`, so 6e8f8b1da is the merge-base. A trial `git merge --no-commit main` into the
branch conflicted in 15 files.

## 2. Scope (IN)

The merge source is local `main` at the sha the pass reads when it starts, recorded in the ledger
and in the merge commit's subject. The conflict set below is the driver's trial merge against
6081d92e4; the builder re-takes it at the merge and records any difference in the ledger.

| File | Hunks | Kind |
|---|---|---|
| `tools/run-gates/run-gates.sh` | 8 | product |
| `memory/map/generated/symbols.json` | 8 | generated |
| `tools/unattended/unattended.sh` | 3 | product |
| `tools/unattended/unattended.test.sh` | 2 | suite |
| `tools/run-gates/run-gates.test.sh` | 2 | suite |
| `tools/run-gates/run-gates.runlog.test.sh` | 1 | suite |
| `tools/run-gates/gate-profiles.txt` | 1 | product |
| `tools/memory-tree/check-memory-hygiene.test.sh` | 1 | suite |
| `tools/memory-tree/check-memory-hygiene.sh` | 1 | product |
| `tools/drift-audit/selftest.py` | 1 | suite |
| `skills/session-kickoff/manifest-check.test.sh` | 1 | suite |
| `.githooks/pre-push.test.sh` | 1 | suite |
| `memory/map/generated/MAP.md`, `CARDS.md` | 1 each | generated |
| `memory/guides/SESSION-KICKOFF.md` | 1 | stamps |

What must survive, on each side:

- **This build's side.** Every unit of this build, and in particular the reuse composition
  `TOOL-aSparedSpawn-32` built (the three knobs read at one site, the one-mode precedence, the
  `reused_cache` stamp field and predicate 9's reading of it) and the digest view
  `TOOL-aSparedSpawn-33` built (the hook's restored environment, `GATE_REUSE_DIGEST_ENV`, read in
  the `push` mode only, and its `REUSE_SCHEMA`). Observed by AC2.
- **Local main's side.** Every unit local `main` carries past 6e8f8b1da. The runner changes among
  them, by `git log 6e8f8b1da..main -- tools/run-gates/run-gates.sh` at 6081d92e4, are aPairedSlots'
  turnstile slots (its units 1 to 7 and 15, and the `slots=<n>` key in `gate-profiles.txt`),
  aOrientedCast's four-field budget row (its unit 12), and the run-gates version aTrimmedHook minted
  (its unit 16). aTrimmedHook's hygiene, commit-msg and manifest-check changes (its units 1 to 7,
  and its kickoff unit 1) survive the same way. None of the three builds' folders exists on this
  branch before the merge, so each is cited here by build and unit number, and each spec is read on
  local `main` with `git show main:<path>` under `memory/builds/<slug>/spec/`. Observed by AC1.

- **S1** — Every conflict in a product or suite file is resolved by keeping BOTH sides' intent,
  never by picking a side. Each conflicted file's merge result is then diffed against BOTH parents,
  so that no hunk either side added is lost. This covers the "auto-took" class, a conflict-free hunk
  silently taken from one side, and the merge-drops-a-side's-hunks class `TOOL-dUnstuckLanding-26`
  names. Where both sides rewrote one function, the result carries both behaviours, and the ledger
  says how they compose. Observed by AC1 and AC2.
- **S2** — Generated files are re-rendered, never hand-merged. `memory/map/generated/symbols.json`,
  `MAP.md` and `CARDS.md` come from `python tools/codebase-map/gen_map.py --write`, and the build
  index and the backlog views from `python tools/memory-tree/gen_build_index.py --write`, each run
  after the hand-merged sources are resolved and staged. Observed by AC3.
- **S3** — The kickoff manifest's stamps, `last-audit` and `last-body-change` in
  `memory/guides/SESSION-KICKOFF.md`, take local `main`'s side at the merge. They are re-stamped in a
  follow-up commit after the merge commit, per the manifest's merge exception, because a commit
  cannot carry its own sha. Observed by AC4.
- **S4** — Kit versions: where both sides minted a kit's version, the merge takes the higher and the
  ledger records both; no new version is minted here. A version carrier outside the conflict set is
  grepped and `python tools/govkit/govkit.py selfcheck` confirms every carrier agrees. Observed by
  AC5.
- **S5** — The post-merge direct checks are green. A row this build owns in
  `memory/project/fork-ceilings.txt` or `memory/project/spawn-idiom-sites.txt` is re-measured when
  local `main`'s changes to the runner moved its count, and the ledger records both readings.
  Observed by AC6.
- **S6** — After the pass, the branch merges into local `main` with no conflict:
  `git merge-tree --write-tree main HEAD` reports a clean tree. Observed by AC7.

## 3. Non-goals (OUT)

- Merging the branch onto local `main`, pushing, or running any suite or the bar. The owner runs the
  gates on the reconciled tree afterwards, and the landing is the main loop's.
- A kit version mint. S4 reconciles the versions both sides minted and mints nothing.
- A contradiction between the two sides that keeping both cannot resolve is NOT decided here: the
  pass aborts the merge with `git merge --abort`, leaves the branch at its pre-merge tip, and returns
  the question, with both sides' intent and the hunk, for the owner.
- Re-deriving local `main`'s own records, decisions or backlog rows. They arrive as they were written.

### Edges

none

## 4. Design

The merge follows `TOOL-aSparedSpawn-32` and the build's earlier reconcile b9b24646f: a `--no-ff`
merge commit named `merge: local main <sha9> into aSparedSpawn`, carrying `Pass: none`, because a
merge's index holds every path local `main`'s 200 commits moved, shared records among them, and
`diff-tree` lists no paths for a merge commit. A pass commit after it, `Pass: TOOL-aSparedSpawn-34`,
carries this spec's CLOSED header and the acceptance ledger, then a stamps commit. The order inside
the merge is fixed so that generated output is rendered from the resolved sources:

1. Read local `main`'s sha and record it.
2. Resolve the product and suite conflicts by hand, both sides kept, and stage them.
3. Take local `main`'s side of the manifest stamps, and the higher of each kit version.
4. Run `gen_map.py --write` and `gen_build_index.py --write`, and stage what they change.
5. Run the two-parent diff over every conflicted file and record the result in the ledger.
6. Run the direct checks, then commit the merge.
7. Run S6's check against the merge commit.

The two-parent diff reads, per conflicted file F, every line `git diff 6e8f8b1da main -- F` adds and
every line `git diff 6e8f8b1da 249b4ab6 -- F` adds, and checks each is present in the result or is
justified by a ledger line. The justification is either a line the other side rewrote on purpose or
a line both sides moved.

The runner is the file to read twice. This build's reuse block and mode block sit beside
aPairedSlots' turnstile, which both sides edited for spawns and slots respectively; a slot beacon
written by builtins and a reuse read at the one knob site do not touch each other, so a hunk that
seems to need one or the other is the abort case in §3.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/gate-profiles.txt`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.runlog.test.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/drift-audit/selftest.py`
- `skills/session-kickoff/manifest-check.test.sh`
- `.githooks/pre-push.test.sh`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/map/generated/symbols.json`
- `memory/map/generated/MAP.md`
- `memory/map/generated/CARDS.md`
- `memory/project/fork-ceilings.txt`
- `memory/project/spawn-idiom-sites.txt`

### Alternatives rejected

- **Merge the branch onto local `main` and resolve there.** The primary tree would hold a half
  resolved merge while other sessions use it, and the owner asked for a conflict-free landing.
- **Rebase the run branch onto local `main`.** It rewrites the build's recorded shas, which its
  ledgers, its review record and `RUN.md` cite.
- **Take one side of the generated map files and re-render later.** The files would describe
  neither parent until then, and the map freshness leg grades every commit.

## 5. Production-readiness checklist

- security: the merged hook, runner and driver keep both sides' scrubs and refusals; S1's two-parent diff is what shows none was dropped.
- perf / scale: N/A — no new code path; a re-measured fork row records local main's cost, not a change of this unit's.
- error / empty / loading states: N/A — no behaviour change beyond reconciling.
- observability: the ledger records the merged sha, each conflicted file's resolution and its two-parent diff result.
- risks: a conflict resolved by picking a side drops a behaviour silently; S1's diff is the check, and a contradiction keeping both cannot resolve aborts the pass rather than being decided in it.
- testing: the direct checks in AC6 and S6's merge-tree check; the suites and the bar run later, by the owner.
- migration: N/A — no data or schema moves.
- user docs: N/A — no README conflicts; each side's docs arrive as written.

## 6. Acceptance criteria

- **AC1** — When, for each conflicted product or suite file F, every line
  `git diff 6e8f8b1da main -- F` adds is searched for in the merge result, each is present or
  carries a justification in the ledger. Red when: a line local main added is absent and
  unjustified.
- **AC2** — When the same search runs for every line `git diff 6e8f8b1da 249b4ab6 -- F` adds, each is
  present or justified. Red when: a line this build added is absent and unjustified, the reuse
  composition's and the digest view's lines included.
- **AC3** — When `python tools/codebase-map/gen_map.py --check` runs on the merge commit, it exits 0,
  and `python tools/memory-tree/gen_build_index.py --write` leaves no diff. Red when: either reports
  a generated file stale, or a hand-merged one differs from its render.
- **AC4** — When `grep -n 'last-audit\|last-body-change' memory/guides/SESSION-KICKOFF.md` runs
  after the stamps commit, the audit stamp names the merge commit's sha. Red when: it still carries
  either parent's stamp.
- **AC5** — When `python tools/govkit/govkit.py selfcheck` runs on the merge commit, it prints no
  version-carrier disagreement. Red when: a carrier holds a version the other carriers do not.
- **AC6** — When the merge commit is checked out, all of these exit 0:
  - `bash -n` on every conflicted shell file;
  - `python tools/memory-tree/check-arms.py --check`;
  - `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`;
  - `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only run-gates-1leg`, and
    the same with `--only run-gates-2leg`;
  - `python tools/codebase-map/gen_map.py --check`;
  - `python tools/check-spec-tokens.py`;
  - `bash tools/memory-tree/check-memory-hygiene.sh --staged`.

  Red when: any exits non-zero.
  figure: each fork count is DERIVED at observation; a row re-measured here records both readings.
- **AC7** — When `git merge-tree --write-tree main HEAD` runs after the pass commit, it exits 0 and
  lists no conflicted file. Red when: it exits 1 or names a conflict, which the trial merge against
  6081d92e4 does in 15 files.
  fixture: local `main` as the pass reads it; a commit landing on `main` after the pass can move it.

## 7. Gates

`run-gates evidence` · `run-gates canary` · `run-gates gov canary` · `run-gates turnstile` ·
`run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `pre-push self-test` ·
`pre-push bar self-test` · `pre-push run-log line` · `push-main self-test` · `branch-guard self-test` ·
`python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` ·
`transition-audit arms` · `straggler-guard arms` · `recall floor arms` · `recall floor` ·
`memory hygiene` · `codebase-map coverage + freshness` · `manifest-check self-test` ·
`shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` ·
`harness arms (fail branches armed or pinned)` · `govkit selfcheck` · `scratch-guard self-test` ·
`drift-audit selftest`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

No existing seam fits: a reconcile is a git operation, and `tools/codebase-map/reuse_lookup.py`
indexes code symbols, not procedures. The precedent is this build's own `TOOL-aSparedSpawn-32`,
which merged origin/main with the same commit shape, and the earlier reconcile b9b24646f. The
two-parent diff is the check the charter's reconcile rule names for the auto-took class.

Recall terms used: reconcile merge local main auto-took two parents generated re-render
last-audit stamps merge exception conflict merge-tree
