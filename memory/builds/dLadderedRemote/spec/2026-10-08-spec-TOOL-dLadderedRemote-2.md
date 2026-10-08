# TOOL-dLadderedRemote-2 — every probe that read a literal origin carries the ladder inline and keeps its own fallback beneath it

**Status:** INPROGRESS · rev-3 · 2026-10-08 · node d · Tier-2 · base 40a8b8c3 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md](../build/2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md) | journal | TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 |
| [2026-10-08-build-TOOL-dLadderedRemote-2-1-site-probe.md](../build/2026-10-08-build-TOOL-dLadderedRemote-2-1-site-probe.md) | journal | — |
| [2026-10-08-review-TOOL-dLadderedRemote-2-closing-diff-round1.md](../reviews/2026-10-08-review-TOOL-dLadderedRemote-2-closing-diff-round1.md) | diff-review | TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 |

<!-- /gen:spec-records -->

## 1. Goal

Every kit site that asks for the default branch's remote-tracking ref takes the remote and the
branch from the ladder of `TOOL-dLadderedRemote-1`, inlined byte-identical. What each site did when
nothing resolved stays exactly as it was, so the only behaviour that moves is which remote is asked.

## 2. Scope (IN)

- **S1** — `tools/drift-audit/drift_report.py`, `resolve_base_ref`: rung 2 takes its name from the
  ladder's `branch`, rung 3 reads `refs/remotes/<remote>/<name>`, rung 4 applies only when the ladder
  answers no remote, rung 5 names `git fetch <remote> <name>`, and a ladder refusal raises
  `DriftError` carrying its text. The `--base-ref` help and the refusal text name no `origin`.
  Observed by AC1, AC2, AC3.
- **S2** — `tools/codebase-map/map_lib.py`, `resolve_compare_base`: the tip is
  `refs/remotes/<remote>/<branch or main>`, and a refusal or no remote returns `None` with the
  reason. The merge-base rule beneath is unchanged. Observed by AC4, AC2.
- **S3** — `tools/run-gates/run-gates.sh`: `DEFBR` and the tip come from the ladder, a refusal
  prints one stderr line naming it, and the fail-safe "run" beneath is unchanged. The evidence
  row `base_from` names the resolved remote. Observed by AC4, AC2.
- **S4** — `tools/unattended/unattended.sh`: `default_branch` keeps `AREF` and `GOV_DEFAULT_BRANCH`
  first, then reads the ladder's `observed` through `RR_GIT=GIT`; `derive_liveness` reads
  `refs/remotes/<remote>/<d>` before the local branch. Check 3's `fail` text is unchanged, so no
  armed signature strands; the ladder's refusal prints on stderr beside it. Observed by AC5.
- **S5** — `tools/playbook/render_playbook.py`, `derive_default_branch`: the ladder's `observed`
  first, never `GOV_DEFAULT_BRANCH`, because a render the bar byte-compares must not move with an
  operator's environment. Then the local `main`/`master` fallback, which is also what a refusal
  reaches, announced on stderr. Observed by AC5.
- **S6** — `tools/govkit/govkit.py`: `resolve_measurer_currency` probes the ladder's remote, and a
  refusal or no remote reads `unverified` with the reason; the epoch default base merge-bases
  `<remote>/<branch or main>` before the local branch, and a refusal is its failed exit 1 naming
  the refusal. Observed by AC5, AC2.
- **S7** — `tools/memory-tree/migrate_backlog.py`, `resolve_default_tip`: `observed` comes from the
  ladder, `GOV_DEFAULT_BRANCH` still only cross-checks it, a refusal is a `Refusal`, and the remedy
  names the resolved remote. Its embedded fixtures name their remote through a variable. Observed
  by AC5, AC2.
- **S8** — `tools/memory-tree/row_grammar.py`, `derive_relation_base`, and
  `tools/memory-tree/check-verdict-epoch.sh`: both merge-base `<remote>/<branch>` before the local
  branch, with `<branch>` from the ladder else `main`, and a refusal is their existing red naming
  the refusal. Row-grammar's embedded fixtures name their remote through a variable. Observed by
  AC5, AC2.
- **S9** — `tools/runlog/model.py`, `read_refs`: the default-branch symref is read from
  `refs/remotes/<remote>/HEAD` for the ladder's remote. The key keeps its name `origin_head`, since
  `resolve_default_ref` and the run log's model readers spell it. Observed by AC5.
- **S10** — `.githooks/pre-commit`'s branch-guard region and `.githooks/straggler-guard.sh`: both
  read `refs/remotes/<remote>/HEAD` for the ladder's remote. Pre-commit keeps `GOV_DEFAULT_BRANCH`
  first and `main` last. The straggler guard keeps the observed branch deciding, and a refusal
  takes its existing announced "NOTHING was checked" path with the refusal's text. Observed by AC5.
- **S11** — every suite whose fixture set `refs/remotes/origin/*` WITHOUT configuring a remote gains
  `git remote add`, because the ladder reads configuration and a ref alone names no remote. Found by
  running each suite once, at the main loop, after the build is complete. NOT OBSERVED by its own
  criterion: it is fixture repair, and the suites going green is the observation.

## 3. Non-goals (OUT)

- inCMS's local scripts. The fix lands here and is re-pulled; a gov-owned file is never hand-edited
  in an adopter.
- Renaming any node's remote. Remote names are per-node variances on purpose.
- The unattended authorization anchor: `observe_remote`, check 24 and `resolve_claim_remote` keep
  their one-remote rule.
- The `.githooks/pre-push` remote resolution. Git hands it the remote's name as `$1`, and
  `TOOL-aGraftedHelix-10` already reads it.
- The review harness's default base. It is unit 4.

### Edges

- **consumes-from** `TOOL-dLadderedRemote-1` — the two canonical blocks every site inlines; without
  them there is nothing byte-identical to inline
- **consumes-from** `TOOL-dLadderedRemote-3` — the ban leg, which this unit turns from red to green
- **hands-off** `TOOL-dLadderedRemote-5` — the closing review's minors at these sites: the observed
  branch at run-gates and map_lib, liveness on a refusal, `base_from`, govkit's currency, and prose

## 4. Design

### The sites

| Site | Literal today | Fallback kept beneath | On a refusal |
|---|---|---|---|
| `drift_report.py` `resolve_base_ref` | `origin/HEAD`, `origin/<name>`, `remote get-url origin` | local `refs/heads/<name>`, announced, only with no remote | exit 2 naming `GOV_REMOTE` |
| `map_lib.py` `resolve_compare_base` | `origin/HEAD`, `origin/<branch>` | `main` when no branch; merge-base rule | `None`, UNGRADED with the reason |
| `run-gates.sh` base | `origin/HEAD`, `origin/${DEFBR}` | changed() fails safe to "run" | one stderr line, then the fail-safe |
| `unattended.sh` `default_branch` and `derive_liveness` | `origin/HEAD`, `origin/<d>` | `AREF`, `GOV_DEFAULT_BRANCH`, then local `refs/heads/<d>` | check 3 refuses with the ladder's text |
| `render_playbook.py` `derive_default_branch` | `origin/HEAD` | local `main`, then `master` | the same local fallback |
| `govkit.py` `resolve_measurer_currency` | `branch.main.remote` else `origin` | `unverified` | `unverified` with the reason |
| `govkit.py` epoch base | `origin/<dflt>` | local `<dflt>` | failed exit 1 naming it |
| `migrate_backlog.py` `resolve_default_tip` | `origin/HEAD`, `origin/<name>` | the env cross-check | `Refusal` with the text |
| `row_grammar.py` `derive_relation_base` | `origin/<branch>` | local `<branch>` | `Problem` naming it |
| `check-verdict-epoch.sh` base | `origin/$DEF` | local `$DEF` | its failed exit 1 naming it |
| `runlog/model.py` `read_refs` | `refs/remotes/origin/HEAD` | local `main`, then `master` | the same local fallback |
| `.githooks/pre-commit` branch guard | `origin/HEAD` | `main` | the same `main` |
| `.githooks/straggler-guard.sh` | `origin/HEAD` | local `GOV_DEFAULT_BRANCH` or `main` | announced, nothing checked |

A site whose fallback beneath was a LOCAL ref reaches it on a refusal only where it did so before
with no `origin`: render, runlog and the pre-commit guard. Every grader that measures what landed
refuses instead, because falling back to local is the defect drift-audit's rung 3 removed.

### Inventory

No new identifier beyond the two inlined blocks. Thirteen inline copies: seven Python, in
`drift_report.py`, `map_lib.py`, `render_playbook.py`, `govkit.py`, `migrate_backlog.py`,
`row_grammar.py` and `runlog/model.py`, and six shell, in `push-main.sh` from unit 1,
`run-gates.sh`, `unattended.sh`, `check-verdict-epoch.sh`, `.githooks/pre-commit` and
`.githooks/straggler-guard.sh`.

### Rollout

Every kit whose shipped bytes move takes a version bump, as `python tools/govkit/govkit.py epoch`
reports them. inCMS re-pulls with `govkit update`, then `--write`, and drops `GOV_DEFAULT_BRANCH`
from its lander once AC7 holds there.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/codebase-map/map_lib.py`
- `tools/codebase-map/test_codebase_map.py`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/unattended/unattended.sh`
- `tools/playbook/render_playbook.py`
- `tools/govkit/govkit.py`
- `tools/memory-tree/migrate_backlog.py`
- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/runlog/model.py`
- `.githooks/pre-commit`
- `.githooks/straggler-guard.sh`

### Alternatives rejected

- Refusing at every site, render and the run log included. Both are readers that fell back to a
  local branch before this build, and a renderer that refuses breaks a render the bar byte-compares.
- Falling back to the local branch at every grader on a refusal. That is the stale-local defect
  drift-audit's rung 3 exists to remove, and the handoff's AC2 requires a refusal.

## 5. Production-readiness checklist

- security: the unattended edits sit on `check_branch` and the liveness reader only, neither of
  which authorizes a run. `GOV_REMOTE` reaches no further than `GOV_DEFAULT_BRANCH` already does.
- perf / scale: one ladder resolution per process at each site, at most four git calls.
- error / empty / loading states: per the site table, refusal and no remote stay distinct.
- observability: every grader names the resolved ref or the refusal it hit.
- risks: a fixture that wrote `refs/remotes/origin/*` without a configured remote now reads no
  remote. S11 repairs those suites.
- testing: arms in the drift-audit, codebase-map and run-gates suites; a recorded cross-site probe
  for the rest; the unattended suites are not run, under the owner's standing instruction.
- migration: none.
- user docs: N/A — no `help/` surface; each refusal text names its remedy.

## 6. Acceptance criteria

- **AC1** — When `tools/drift-audit/drift_report.py` runs on a fixture whose only remote is `incms`,
  with `refs/remotes/incms/HEAD` naming `incms/main` and no environment set, its header reads
  `(base refs/remotes/incms/main @ <sha8>)`. Red when: it exits 2 or names `refs/heads/main`.
- **AC2** — When the same fixture gains a second remote and the branch has no upstream, with
  `GOV_REMOTE` unset, `drift_report.py` exits 2, `resolve_compare_base` returns `None`, and the
  bar runner prints the refusal on stderr, each naming `GOV_REMOTE`. Red when: any of them picks a remote.
- **AC3** — When `GOV_REMOTE=incms` is set beside an `origin` remote, `drift_report.py`'s header
  names `refs/remotes/incms/main`. Red when: it names `origin`.
- **AC4** — When `resolve_compare_base` runs on the AC1 fixture it returns a sha, and when the bar
  runner runs there its scope `BASE` is non-empty, so a guarded unchanged leg prints `GATE skip`.
  Red when: the first returns `None` or the second runs the leg.
- **AC5** — When the cross-site probe recorded in this unit's journal runs the remaining sites on the
  AC1 and AC2 fixtures and with `GOV_REMOTE=incms`, every row reads `incms`, its refusal or its
  declared fallback per the site table. Red when: a row reads `origin` or a local ref the table does
  not declare.
  permission: the `tools/unattended/` suites are not run; `unattended.sh` is probed by sourcing its
  two functions into a hermetic shell.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `memory hygiene` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `python resolver (behaviour + inline parity + idiom ban)` · `install-prefix (shipped surface)` · `encoding posture (text IO names its encoding)` · `pre-push run-log line` · `run-gates run-log line` · `runlog selftest` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `straggler-guard arms` · `verdict-epoch self-test` · `remote literals (kit code names no remote)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 · a fixture with no `origin` remote, staged against the 40a8b8c3 `resolve_base_ref` · none
New arm: tools/codebase-map/selftest.py · covers AC4 AC2 · the same fixture against the 40a8b8c3 `resolve_compare_base` · none
New arm: tools/run-gates/run-gates.test.sh · covers AC4 AC2 · the guarded canary with its remote named `incms` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-08 · initial draft.
- rev-2 · 2026-10-08 · S4 · S5 · §7 · what the build pass found: check 3's message stays put and the
  refusal prints beside it; the render reads the observed branch, not the environment; the
  codebase-map arm lives in the kit selftest, since the repo-subject coverage test runs on every bar.
- rev-3 · 2026-10-08 · §3 · the hands-off edge to `TOOL-dLadderedRemote-5`, the batch unit the closing
  review promoted.

## 10. Reuse audit

Every site extends the ladder `TOOL-dLadderedRemote-1` promotes from `tools/push-main.sh`; no site
gains a second resolver. `python tools/codebase-map/reuse_lookup.py "choose the remote and its default branch for a landed ref"`
returned no seam that fits, and the sites were enumerated instead by the ban predicate of
`TOOL-dLadderedRemote-3` run over the tree at 40a8b8c3.
Recall terms used: remote origin GOV_REMOTE GOV_DEFAULT_BRANCH set-head default branch ladder push-main resolve_base tracking ref stale local
