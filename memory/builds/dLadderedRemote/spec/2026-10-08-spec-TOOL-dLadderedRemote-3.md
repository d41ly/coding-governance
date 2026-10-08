# TOOL-dLadderedRemote-3 — a ban leg reds a literal origin ref in kit code

**Status:** INPROGRESS · rev-3 · 2026-10-08 · node d · Tier-2 · base 40a8b8c3 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md](../build/2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md) | journal | TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-6 |
| [2026-10-08-review-TOOL-dLadderedRemote-2-closing-diff-round1.md](../reviews/2026-10-08-review-TOOL-dLadderedRemote-2-closing-diff-round1.md) | diff-review | TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-4 |

<!-- /gen:spec-records -->

## 1. Goal

The class, not the thirteen instances: a kit file that spells the remote `origin` as a ref, as a
default, or in a remedy reds the bar. Fixing the sites without this lets the next probe reintroduce
the defect, which is how one fixed lander and twelve unfixed probes came to coexist.

## 2. Scope (IN)

- **S1** — `tools/check-remote-literals.sh`, a pure ban with no waiver registry and no line marker.
  It greps the tracked population below for the predicate below and prints `<path>:<line>: <text>`
  per hit, exiting 1 on any hit, 0 on none, and 2 as a DEAD PROBE when the population is empty.
  Observed by AC1, AC2, AC3.
- **S2** — `tools/check-remote-literals.test.sh`, its red and green self-test over a scratch repo.
  Observed by AC2, AC3.
- **S3** — two legs in `tools/gate-legs.json`, the ban as a `repo`-subject leg in the `declarations`
  chunk and its self-test as a `kit`-subject leg, plus two `[[exempt]]` rows in
  `tools/govkit/registry.toml` declaring both files gov-internal. Every meta-gate the new legs trip
  is satisfied in this unit. Observed by AC4.

## 3. Non-goals (OUT)

- Draining the hits. Units 2 and 4 do that; this unit lands red against them and says so.
- Adopters. The checker greps gov's own kit source, so it is exempt from shipping, like
  `check-dead-paths.sh`.
- A bare quoted `origin` passed as a git argument. The predicate cannot tell an argv element from a
  dictionary key spelled the same, and `govkit.py` uses `"origin"` as a field name.

### Edges

- **consumes-from** `TOOL-dLadderedRemote-1` — the canonical blocks, whose own text must not trip
  the predicate it introduces
- **hands-off** `TOOL-dLadderedRemote-2` — the hits in kit sites, which that unit drains
- **hands-off** `TOOL-dLadderedRemote-4` — the hit in the review harness's default base
- **hands-off** `TOOL-dLadderedRemote-5` — the predicate and population gaps the closing review found

## 4. Design

### Population

Tracked `*.sh`, `*.py` and `*.js` files under `tools/` and `skills/`, and every tracked file under
`.githooks/`. Excluded by path: `*.test.sh`, `*selftest*.py`, `test_*.py`, and anything under a
`fixtures/` directory, because a fixture that creates `origin` on purpose is not a defect. Excluded
by line: a line whose first non-blank text is `#`, `//`, `/*` or `*`, because a comment that
records what a site used to read is history, not a read.

### Predicate, one extended regex per shape

| Shape | Pattern | Example it catches |
|---|---|---|
| tracking ref | `refs/remotes/origin([^A-Za-z0-9_.-]|$)` | `refs/remotes/origin/HEAD` |
| short ref | `(^|[^A-Za-z0-9_./-])origin/(HEAD|main|master|[$\{])` | `"origin/${DEFBR:-main}"`, `f"origin/{branch}"` |
| default | `(\bor|\|\||:-)[[:space:]]*["']?origin\b` | `_rn.stdout.strip() or "origin"` |
| remedy | `(set-head|fetch|get-url|ls-remote|set-url)[[:space:]]+origin\b` | `git remote set-head origin -a` |

The population and each pattern are written ONCE in the script. The script's header states what
it does not check: a remote name held in a variable, a bare quoted argument, a docstring line that
is prose rather than a read, and any file type outside the population.

### Liveness

An empty population is exit 2 with `DEAD PROBE`, never a clean 0. The self-test stages one hit per
shape, one hit per excluded path that must stay silent, and one comment that must stay silent.

### Files touched (estimate)

- `tools/check-remote-literals.sh`
- `tools/check-remote-literals.test.sh`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`

### Alternatives rejected

- A third check inside `tools/check-install-prefix.sh`. That gate is declared ONE predicate with
  zero tolerance about kit paths, and its `--offenders` signature keys on that one predicate.
- A section of `tools/lib/resolve-python.test.sh`. That leg is `kit`-subject and so HELD off every
  bar unless `GATE_SELFTESTS=1`, which no push boundary sets.

## 5. Production-readiness checklist

- security: N/A — read-only grep over tracked files.
- perf / scale: one `git grep` over the population; seconds.
- error / empty / loading states: an empty population is a DEAD PROBE exit 2.
- observability: every hit prints its path, line and text.
- risks: a docstring that QUOTES an old spelling reds; the remedy is to reword it, since a
  docstring that describes `origin` describes the defect.
- testing: the self-test's staged hits per shape and per exclusion.
- migration: none.
- user docs: N/A — gov-internal gate.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-remote-literals.sh` runs on the tree at 40a8b8c3, it exits 1 and
  its hits include `tools/drift-audit/drift_report.py`, `tools/codebase-map/map_lib.py`, the bar
  runner, `tools/unattended/unattended.sh`, `tools/playbook/render_playbook.py`,
  `tools/govkit/govkit.py`, `tools/memory-tree/migrate_backlog.py`, `tools/memory-tree/row_grammar.py`,
  `tools/memory-tree/check-verdict-epoch.sh`, `tools/runlog/model.py`, `.githooks/pre-commit`,
  `.githooks/straggler-guard.sh` and `tools/workflows/tier2-review.js`. Red when: any of those is absent from the hits.
- **AC2** — When the self-test plants one line per shape in a scratch repo, `check-remote-literals.sh`
  names each one. Red when: a staged break deleting one pattern leaves its planted line unnamed.
- **AC3** — When the self-test plants the same lines in a `*.test.sh` file, a `fixtures/` path and a
  `#` comment, `check-remote-literals.sh` exits 0, and over an empty population it exits 2 printing
  `DEAD PROBE`. Red when: any of those is named, or the empty population exits 0.
- **AC4** — When units 2 and 4 are built, `check-remote-literals.sh` exits 0 on the branch tip.
  Red when: a hit remains.

## 7. Gates

`remote literals (kit code names no remote)` · `remote literals self-test` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `codebase-map coverage + freshness` · `recall floor arms` · `run-gates canary` · `run-gates gov canary`

New arm: tools/check-remote-literals.test.sh · covers AC2 AC3 · one planted line per shape, per excluded path, and an empty population · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-08 · initial draft.
- rev-2 · 2026-10-08 · S3 · the ban leg sits in the `declarations` chunk, as built; closing review
  round 1 item 19, folded by `TOOL-dLadderedRemote-5`.
- rev-3 · 2026-10-08 · §3 · the hands-off edge to `TOOL-dLadderedRemote-5`, the batch unit the closing
  review promoted.

## 10. Reuse audit

The ban shape, its DEAD PROBE exit and its two-file exemption follow `tools/check-dead-paths.sh` and
its `[[exempt]]` rows in `tools/govkit/registry.toml`. `python tools/codebase-map/reuse_lookup.py "choose the remote and its default branch for a landed ref"`
found no ban over remote names, and the install-prefix gate was rejected in §4 as the wrong home.
Recall terms used: remote origin GOV_REMOTE GOV_DEFAULT_BRANCH set-head default branch ladder push-main resolve_base tracking ref stale local
