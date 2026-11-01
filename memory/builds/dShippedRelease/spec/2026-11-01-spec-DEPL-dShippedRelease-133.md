# DEPL-dShippedRelease-133 — `dispose-landing` reduces the harness's absolute `report` path to its repo-relative form

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 15 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md) | research | DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-133-token-fix-brief.md](../build/2026-11-01-build-DEPL-dShippedRelease-133-token-fix-brief.md) | research | — |
| [2026-11-01-build-DEPL-dShippedRelease-133-token-fix-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-133-token-fix-return.md) | research | DEPL-dShippedRelease-128 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-138 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 23 of `reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md`, HIGH, item H5. Unit 114's table
passes the harness's `report` straight to `dispose-landing`. `tools/workflows/tier2-review.js` asks only for a
forward-slash path, and real records hold `C:/projects/...` values. Unit 14 S4 writes the value as given, and
unit 83 S1 requires it directly under `memory/builds/<slug>/reviews/`, so an honest review with findings prints
`forged · path` and the close holds. This unit reduces the path once, at the write.

## 2. Scope (IN)

- **S1** — The reduction. `derive_report_path(report, base_dir)` in `tools/loop/deploy_items.py` folds `\` to `/`,
  reads `C:/x`, `c:/x` and `/c/x` as one drive spelling, and for an absolute path strips `base_dir`, the drive
  letter compared without case. A relative path stands, and an absolute path outside `base_dir` raises.
  Observed by AC1, AC2, AC3.
- **S2** — The argument. `dispose-landing <sha> <report> [--root <dir>]` runs S1 first, `<dir>` the return's `root`
  key and by default the walk's own toplevel. It reads the file at the reduced path under the walk's root, and
  writes that reduced path into `disposed · <n> finding(s) · <report path>`. Observed by AC1.
- **S3** — The refusal. A path outside `<dir>`, and a reduced path absent from the walk's tree, each refuse, exit 2,
  printing `dispose — <sha8> · report outside <dir>` or `dispose — <sha8> · report not in this tree`, with `review`
  keeping its value. Observed by AC2.
- **S4** — The table. Unit 114's row 1 reads `dispose-landing <sha> <path> --root <the return's root>`. Observed by AC1.

## 3. Non-goals (OUT)

- The harness's prompt: `tools/workflows/tier2-review.js` keeps its wording, and the corpus already holds both forms.
- The term: unit 83 S1 stands, and now reads what this unit writes.
- A checklist item that a route consuming a harness field cites a real value: the audit's left-shift item.

### Edges

- **consumes-from** `DEPL-dShippedRelease-114` — §4's row 1 and the `review-harness-return` case, which this unit restates
- **consumes-from** `DEPL-dShippedRelease-83` — S1's path rule, which the written value must pass
- **consumes-from** `DEPL-dShippedRelease-14` — S4's `dispose-landing` and its field

## 4. Design

### Evidence

- `tools/workflows/tier2-review.js:1911` ends the synthesis prompt with `Return JSON {path, items, summary} with a FORWARD-SLASH path.`, and the success return carries `report: synth?.path || null` and `root: repo`.
- Report id 23 read `"path": "C:/projects/..."` in dRedressedBar's agent returns and `"report": "C:/projects/..."` in aMendedFleet-93-arm-a.json:23. PINNED at the audit.
- Unit 83 S1 fails anything not directly under `memory/builds/<slug>/reviews/` as `forged · path`.

### Supersedes

- Unit 14 S4's `<report path>`, which reads the reduced path.
- Unit 114 §4's row 1.
- Unit 114 §6's silence on a `report` that is a path: AC1 here plants it.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_report_path` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |
| `--root` | flag of `dispose-landing` | none |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `tools/loop/deploy_fixture.py`: the cases of §6
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`: the flag

### Alternatives rejected

- **A session step in unit 114's table.** It leaves a person to retype a path a function can reduce, and no fixture reaches it.
- **Keeping the suffix after the last `memory/`.** It accepts a path from any tree, so a report outside this repo's root would pass the reduction.

## 5. Production-readiness checklist

- security — S1 refuses a path outside `<dir>`, and unit 83 S1 still refuses a traversal, so the reduction opens no read outside the tree.
- perf / scale — N/A — one string fold per disposal.
- error / empty / loading states — S3 names the two refused states, and AC2 plants each.
- observability — each refusal prints the path it read.
- risks — a review run in another worktree returns that worktree's `root`, and its report must reach this tree by the records landing before disposal; S3's second line says so.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `tools/unattended/VERBS.template.md` states the flag.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-harness-return` drives a return whose `report` reads
  C:/.../memory/builds/fx/reviews/<file>.md, `read-landing` prints `review<TAB>disposed · <n> finding(s) · ...`
  ending in the repo-relative memory/builds/fx/reviews/<file>.md, and `--deploy close` passes `path`.
  Red when: an honest review with findings prints `forged · path`.
- **AC2** — When `python deploy_items.py dispose-landing <sha> <report> --root <other>` runs on a path outside
  `<other>`, and on a reduced path absent from the tree, each exits 2 and `review` keeps its value.
  Red when: a report from outside the repo is disposed, or a missing one reads as an empty report.
- **AC3** — When `python -c` calls `derive_report_path` on C:\x\memory\a.md, c:/x/memory/a.md and
  /c/x/memory/a.md with `base_dir` C:/x, each returns memory/a.md.
  Red when: a spelling this node's own shells write reads as outside the tree.

## 7. Gates

`recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 · an absolute `report` copied from a real harness record, its failing case the value written as given · none

## 8. Open questions

- **F1 — Which root strips the path?** Options: (a) a `--root` flag carrying the return's `root`, defaulting to the
  walk's toplevel; (b) the walk's toplevel alone. (b) refuses an honest return whose `repo` argument is spelled
  otherwise, the case the report's fix names. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the report's
  fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 23 (HIGH, item H5) of the round-4 spec audit.

## 10. Reuse audit

The seam extended is `dispose-landing` (unit 14 S4) and the `review-harness-return` case (unit 114 S2).
`python tools/codebase-map/reuse_lookup.py "reduce an absolute path to a repo relative path"`
ranked `repo_root`, `build_spec_path_re` and `resolveRepo`, none of which reduces a spelled path, so no
existing seam fits and S1 is new. The recall probe surfaced TOOL-dTotalRecall-87, TOOL-dFairHearing-8 and this
round's report, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what path spelling does a harness return carry" --terms "report path absolute forward-slash repo-relative root return drive-letter toplevel normalise dispose field"`
