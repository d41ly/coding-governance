# TOOL-dLadderedRemote-4 — the tier-2 review harness requires a diff review's base instead of defaulting to origin/main

**Status:** INPROGRESS · rev-1 · 2026-10-08 · node d · Tier-2 · base 40a8b8c3 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md](../build/2026-10-08-build-TOOL-dLadderedRemote-1-1-acceptance-ledger.md) | journal | TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-6 TOOL-dLadderedRemote-7 TOOL-dLadderedRemote-8 |
| [2026-10-08-review-TOOL-dLadderedRemote-2-closing-diff-round1.md](../reviews/2026-10-08-review-TOOL-dLadderedRemote-2-closing-diff-round1.md) | diff-review | TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 |

<!-- /gen:spec-records -->

## 1. Goal

A diff review called without `base` is refused before any agent spawns, instead of reviewing
`origin/main...HEAD`. The harness runs in the Workflow runtime with no git, so it cannot resolve a
remote itself, and its default named a ref that does not exist on a node whose remote is not
`origin`.

## 2. Scope (IN)

- **S1** — `tools/workflows/tier2-review.js` and `tools/workflows/tier2-review.template.js`: `base`
  carries no default. A diff-kind call with `base` absent or blank throws before the base-shape
  ladder, with a message naming `git rev-parse` as the way to pin one. A spec audit still ignores
  `base`. The moving-ref warning and its round-2 refusal stay, and their text no longer claims a
  default exists. Observed by AC1, AC2.
- **S2** — `tools/workflows/tier2-review.test.sh`: an arm for the absent base and one for the blank
  base on a diff review, and one for the absent base on a spec audit. Observed by AC1, AC2.
- **S3** — the usage comment at the top of both files and the HONEST LIMIT comment beside the range
  line state that `base` is required. NOT OBSERVED by a criterion: comment text, which the ban leg of
  `TOOL-dLadderedRemote-3` excludes by line.

## 3. Non-goals (OUT)

- Resolving a default branch inside the harness. The runtime has no shell and no filesystem.
- Other workflow scripts. `unattended-build.js` and `drift-audit-code.js` already require a sha.
- The base-shape rule itself: a ref still warns at round 1 and refuses above it.

### Edges

- **consumes-from** `TOOL-dLadderedRemote-3` — the ban leg, whose `tier2-review.js` hit this unit drains;
  without it nothing stops the default from coming back

## 4. Design

The refusal sits beside the existing `repo` refusal, so it runs before `baseLooksPinned`:

```js
const base = a.base
if (!isSpec && !String(base || '').trim()) {
  throw new Error('tier2-review: a diff review needs `base`, the immutable sha the diff starts from. ' +
    'It has no default: the harness cannot read which remote this repository lands on. ' +
    'Pin one with git rev-parse <the default branch>.')
}
```

`isSpec` is computed earlier than this line in the current file, which the build pass confirms
before moving the check; if it is not, the check moves to the first line after it.

### Files touched (estimate)

- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.test.sh`

### Alternatives rejected

- Keeping the default and waiving the ban hit. The owner chose to require `base` (2026-10-08).
- Defaulting to `HEAD~1`. That reviews one commit and reads as a review of the branch.

## 5. Production-readiness checklist

- security: N/A — argument validation only.
- perf / scale: N/A — one check before any agent.
- error / empty / loading states: absent and blank `base` are both refused, with a remedy.
- observability: the refusal names the missing argument and the command that pins it.
- risks: a caller that relied on the default now fails fast. M8 of `memory/guides/BUILD-METHOD.md`
  already spells `base` in its invocation, and `unattended-build.js` passes one.
- testing: three arms in the harness suite.
- migration: none.
- user docs: N/A — the harness's own usage comment is its documentation.

## 6. Acceptance criteria

- **AC1** — When the harness suite's new arm calls a diff review with no `base`, `tier2-review.js`
  throws a message naming `base` before any agent. Red when: the call proceeds or warns.
- **AC2** — When the same arm calls a spec audit with no `base`, it proceeds as before. Red when:
  the new check refuses a spec audit.
- **AC3** — When `bash tools/check-remote-literals.sh` runs after this unit, no hit names
  `tools/workflows/tier2-review.js` or its template. Red when: either still spells `origin/main`
  outside a comment.

## 7. Gates

`tier2-review self-test` · `review-protocol parity (kit vs dogfood)` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `remote literals (kit code names no remote)`

New arm: tools/workflows/tier2-review.test.sh · covers AC1 AC2 · a diff review and a spec audit each called with no base · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-08 · initial draft.

## 10. Reuse audit

The refusal reuses the harness's own `repo` refusal shape in `tools/workflows/tier2-review.js`,
which already throws before any agent for a missing root. `python tools/codebase-map/reuse_lookup.py "choose the remote and its default branch for a landed ref"`
found no resolver a Workflow script could call, since none has git access.
Recall terms used: remote origin GOV_REMOTE GOV_DEFAULT_BRANCH set-head default branch ladder push-main resolve_base tracking ref stale local
