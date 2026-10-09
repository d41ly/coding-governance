# TOOL-aDistilledCharter-6 — the hook README's three bound phrases are compared with the hook again

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-7 DEPL-aDistilledCharter-2 |
| [2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round2.md](../reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round2.md) | diff-review | TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-7 DEPL-aDistilledCharter-2 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aDistilledCharter-3` retired three parity pairs because the charter stopped stating their
phrases, but the phrases still stand in `tools/hooks/README.md`, so the digits there can drift from
`agent-cap.js` with no gate noticing. This unit points those pairs at the README, where the values
are now stated.

## 2. Scope (IN)

- **S1** — `tools/check-playbook-parity.sh` S2 regains `lens-array bound`, `bounded-helper width`
  and `resolved-K ceiling`, each with the hooks README as its stated file and its old extraction.
  Observed by AC1 and AC2.
- **S2** — The self-test fixture carries a hooks README holding the three phrases, and the
  `MAX_LENSES` drift arm returns. Observed by AC2.

## 3. Non-goals (OUT)

- The hook matcher pair. `.claude/settings.json` is graded by `check-wiring.sh`, and no prose now
  states the matcher.
- Restating the phrases in the charter.

### Edges

- **consumes-from** `TOOL-aDistilledCharter-3` — the S2 stage it narrowed.
- **hands-off** `TOOL-aDistilledCharter-7` — the parity gate's S4 findings.

## 4. Design

The stated file is `${HK_DIR}/README.md`, resolved through the same sibling-kit resolver that finds
`agent-cap.js`, so an adopter whose hooks kit sits elsewhere is read where it is. An unresolvable
README is the existing "an extraction matched NOTHING" refusal.

### Files touched (estimate)

`tools/check-playbook-parity.sh` · `tools/check-playbook-parity.test.sh`

## 5. Production-readiness checklist

- security — N/A — a read-only gate.
- perf / scale — three more `sed` reads.
- error / empty / loading states — an extraction that matches nothing reds, as for every pair.
- observability — a disagreement names the pair and both values.
- risks — the README is another kit's file; the resolver already crosses that boundary for the hook.
- testing — the parity self-test.
- migration — none.
- user docs — the gate's header.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-playbook-parity.sh` runs on the tree, the three pairs are
  compared and agree. Red when: any extraction matches nothing.
- **AC2** — When the self-test sets `const MAX_LENSES = 6` in its fixture hook, the gate reds
  naming `lens-array bound`. Red when: the drift passes.

## 7. Gates

`playbook parity` · `playbook parity selftest` · `harness arms (fail branches armed or pinned)`

New arm: tools/check-playbook-parity.test.sh · covers AC2 · a fixture hook whose lens bound drifts from its README · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from the closing review round 1, G1 (HIGH).

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` is the set's probe; the seam
extended is the `PAIRS` list of `tools/check-playbook-parity.sh`, whose rows already resolve the
hook through `resolve_kit_dir`.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
