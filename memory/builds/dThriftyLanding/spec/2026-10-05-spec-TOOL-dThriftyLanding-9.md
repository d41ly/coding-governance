# TOOL-dThriftyLanding-9 — the hook's doc-only classification sees code touched on a merged side branch

**Status:** OPEN · rev-1 · 2026-10-05 · node d · Tier-2 · base f765eb8e · streams tooling · order 9

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The closing review's finding 22 (HIGH): `classify_docs` in `.githooks/pre-push` lists the files every
commit in `R..tip` touched with a path-limited `git log` that lacks `--full-history`. A `--no-ff` merge
whose side branch adds a code file and removes it again is pruned, so the push classifies doc-only and
predicate 5 is waived over a second parent that carried code. This unit makes the read see every commit.

## 2. Scope (IN)

- **S1** — `classify_docs`'s per-commit read carries `--full-history`. Observed by AC1.
- **S2** — Its comment states the read is full-history and why. Observed by AC1.

## 3. Non-goals (OUT)

- The runner's read: `TOOL-dThriftyLanding-8`.

### Edges

- **hands-off** `TOOL-dThriftyLanding-8` — the runner's read of the same range.

## 4. Design

### Evidence

Read at `f765eb8e`. Finding 22 reproduced it: a side branch adds `src/x.sh`, removes it and edits a doc,
then `merge --no-ff side`; the hook's exact command prints nothing, and with `--full-history` it lists
`src/x.sh`.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`

### Alternatives rejected

- **Refuse doc-only on any merge tip.** Every build lands as a merge here, so that would remove the
  saving for every records build, which is the commonest doc push.

## 5. Production-readiness checklist

- perf / scale — no new process on the common path.
- security — narrows nothing the push boundary decides; each change makes a skip rarer or a check wider.
- error / empty / loading states — unchanged.
- observability — each refusal or decision names its reason.
- testing — each arm observed RED against `f765eb8e` first.
- migration — none.
- user docs — the carriers unit 6 wrote, where this unit's change touches them.
- risks — none beyond the finding's own.

## 6. Acceptance criteria

- **AC1** — When a DOCS fixture's side branch adds and removes `src/` code and edits a doc, and is merged
  with `--no-ff` onto a doc commit past R, the decision line carries no `docs-only`.
  Red when: the hook at `f765eb8e` prints `docs-only` for that push.

## 7. Gates

`pre-push self-test` · `spec tokens (a spec's own names resolve)`

New arm: .githooks/pre-push.test.sh · a code touch only on a merged side branch, run against the f765eb8e hook · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · promoted from the closing diff review, round 1.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "scope the push-boundary bar to the legs a doc-only diff can affect"` was run for the build and cannot see `.sh`; no existing seam fits beyond the one named here. The seam is `classify_docs`, added by unit 3; only its git call changes. The review record names the
fix and judged it sound.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent
