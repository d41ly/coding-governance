# TOOL-dThriftyLanding-2 — a full green earned in any worktree serves every worktree's push

**Status:** CLOSED · rev-1 · 2026-10-05 · node d · Tier-2 · base c3ef6742 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-dThriftyLanding-1-runlog-58509c21.md](../build/2026-10-05-build-TOOL-dThriftyLanding-1-runlog-58509c21.md) | journal | TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6 TOOL-dThriftyLanding-8 TOOL-dThriftyLanding-9 TOOL-dThriftyLanding-10 TOOL-dThriftyLanding-11 TOOL-dThriftyLanding-12 |
| [2026-10-05-build-TOOL-dThriftyLanding-2-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-dThriftyLanding-2-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-dThriftyLanding-2-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-dThriftyLanding-2-1-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-dThriftyLanding-1-closing-diff-round1.md](../reviews/2026-10-05-review-TOOL-dThriftyLanding-1-closing-diff-round1.md) | diff-review | TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6 |

<!-- /gen:spec-records -->

## 1. Goal

The runner writes `gate-full-green` into `git rev-parse --git-dir`, which is per worktree, and the
pre-push hook reads it from the same place. A green earned in a run's worktree is therefore invisible
to the primary tree's push, which pays the full bar again: the records push after this clone's last
landing did exactly that. The stamp is self-validating — the hook checks that its sha is an ancestor
of the pushed tip, that its tree fingerprint reproduces at that sha, and that its manifest blob is the
current one — so where it was written does not change what it proves. This unit shares it.

## 2. Scope (IN)

- **S1** — When the run writes its own stamp from a LINKED worktree, so that
  `git rev-parse --git-common-dir` differs from its git dir, the runner also writes the same bytes to
  `gate-full-green.shared` in the common dir. It never writes the common dir's own
  `gate-full-green`, which is the primary tree's stamp. Observed by AC1.
- **S2** — The hook evaluates its candidates in order and adopts the first that passes predicate 1
  and `check_green_record` (predicates 2 to 8): its own git dir's `gate-full-green`, then the common
  dir's `gate-full-green`, then the common dir's `gate-full-green.shared`, each path once. Its
  decision line names the stamp it adopted when that is not its own. Observed by AC2 and AC3.
- **S3** — When no candidate passes, the FULL line's reason names the first candidate's refusal and
  each later candidate's, so no refusal is silent. Observed by AC3.

## 3. Non-goals (OUT)

- The inherited-green stamp: it binds to the remote sha the push reads, and is left per worktree.
- Which bar runs once the stamp is chosen: unchanged here; `TOOL-dThriftyLanding-3` adds the docs case.
- A clone that is not a linked worktree: the two directories are one, so nothing changes there.

### Edges

- **hands-off** `TOOL-dThriftyLanding-3` — the docs decision reads whichever stamp S2 chose.

## 4. Design

### Evidence

Read at base `c3ef6742`. `run-gates.sh` sets `GD` from `git rev-parse --git-dir` and writes the stamp
block under seven preconditions, among them zero skips, a clean tree at start, and a written GREEN
verdict. `.githooks/pre-push` reads `$gd/gate-full-green` into four fields, then runs predicate 1 and
`check_green_record` (predicates 2 to 8). This clone's `runlog/pushes.log` records a scoped push from
a run worktree at 22:15 on 2026-10-04 and, 21 minutes later, a FULL push of the records merge from the
primary tree.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `.githooks/pre-push`
- `tools/run-gates/run-gates.evidence.test.sh`
- `.githooks/pre-push.test.sh`

### Alternatives rejected

- **Write the stamp to the common dir's own `gate-full-green`.** In the primary tree that file IS the
  primary's stamp, so a branch's green that is no ancestor of main would replace main's valid one. A
  separate `.shared` file, read last, means sharing can only add a usable record, never remove one.
- **A directory of stamps keyed by sha.** It needs pruning and a selection rule, for one extra stamp
  that the own-then-common order already covers in the measured case.

## 5. Production-readiness checklist

- perf / scale — one `rev-parse` and at most one extra file read per push.
- security — no new trust: the shared stamp passes the same predicates as the own one.
- error / empty / loading states — an unreadable or absent common stamp leaves today's decision.
- observability — the decision line says which stamp it used.
- testing — the evidence harness and the hook suite, each arm RED against the base first.
- migration — none: the first full green after landing writes both.
- user docs — the hook's own header and the run-gates README, in `TOOL-dThriftyLanding-6`.
- risks — none beyond today's: the predicates are unchanged.

## 6. Acceptance criteria

- **AC1** — When a full green is earned in a linked worktree of a fixture clone, that worktree's
  `gate-full-green` and the common dir's `gate-full-green.shared` carry the same `sha` line, and the
  common dir's own `gate-full-green` is untouched.
  Red when: the base runner writes the worktree's copy only.
- **AC2** — When the primary tree of that clone pushes a tip one commit past the stamped sha, with no
  stamp of its own, the hook prints `scoped gate` and names `gate-full-green.shared`.
  Red when: the base hook prints `FULL gate` with `no recorded full green`.
- **AC3** — When the common stamp's sha is not an ancestor of the pushed tip, the hook prints
  `FULL gate`, and its reason names both the own stamp's refusal and the common one's.
  Red when: a failing shared stamp is adopted, or its refusal is not named.

## 7. Gates

`run-gates evidence` · `pre-push self-test` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: .githooks/pre-push.test.sh · a primary-tree push whose only stamp is in the common dir, run against the base hook · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the hook's stamp read and this clone's push log.

## 10. Reuse audit

The seam extended is `check_green_record`, which already serves two records, the full green and the
inherited green; a third caller reuses it unchanged. `python tools/codebase-map/reuse_lookup.py` was
run for the build and cannot see `.sh`. The recall query returned the specs that wrote the stamp's
preconditions, `TOOL-dUnstalledConvoy-27`'s coverage key among them; none places the stamp in the
common dir or rules it must stay per worktree.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent
