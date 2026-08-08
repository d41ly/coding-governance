# Closing adversarial review — full aPrunedCeremony build diff (wf_3c0f6fa3)

**Status:** closing review · 729a1ee3..HEAD · 2026-07-19 · 3 lenses (enforce/runner/integration) →
skeptic · 5 raw, 5 confirmed (0 HIGH, 3 MED, 2 LOW). The enforcement model held (no red-slip, no
code-as-non-main mis-classification, no manifest green-by-absence on the committed manifest). Folds:

- ENFORCE-MED · the canary validated `argv[0]` but not a non-empty `name` or `argv` length ≥ 2, so a
  malformed leg (empty name → dropped by run-gates.sh's drop-sentinel; launcher-only → `bash
  </dev/null` no-op) passed the canary AND reported GREEN. FIXED: canary check 1 now rejects empty
  names and `argv` len < 2. Verified: it reds on both bad shapes, passes the real manifest.
- INTEGRATION-MED · gate-legs.json (the new leg source) was outside the manifest `watch:` list, so a
  future leg-only change would not trip the C5 ratchet and §B/AGENTS could drift. FIXED: added
  `tools/gate-legs.json` to `watch:` + re-stamped.
- INTEGRATION-MED · the node-b ledger migration follow-up was claimed in the spec/build-log but not
  recorded in any backlog. FIXED: `PLAY-aPrunedCeremony-5` added to `memory/playbook/BACKLOG.md`.
- RUNNER-LOW · stale `<TAB>` separator comment in run-gates.sh contradicted the `\x1e` code. FIXED.
- ENFORCE-LOW · pre-push default-branch resolution falls back to literal `main` when origin/HEAD is
  unset and no `GOV_DEFAULT_BRANCH`. ACCEPTED by design: mirrors the existing `.githooks/pre-commit`
  branch-guard fallback exactly; coding-governance's default is `main` with origin/HEAD set.
  Diverging the two hooks for this edge would be worse than the narrow hole; a non-`main`-default
  adopter sets `GOV_DEFAULT_BRANCH` (documented on both hooks).
