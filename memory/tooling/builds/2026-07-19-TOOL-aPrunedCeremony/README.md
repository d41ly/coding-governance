# TOOL-aPrunedCeremony — gate-economy uplift for the tooling kits (specs)

**Master overview + owner decision menu for the tooling half of the gate-economy port.** Two specs
lifting the *mechanism* half of inCMS `ARCH-aTrimmedGauntlet-2` into `tools/run-gates.sh` and
`.githooks/`. The playbook (charter-wording) half lives in the sibling build
`memory/playbook/builds/2026-07-19-PLAY-aPrunedCeremony/`.

Both carry a genuine "should we build this at all?" fork — the honest output of the design pass is
that neither is an obvious yes for THIS repo's shape (a single bash runner, hooks wired as a tracked
dir). Specs awaiting owner build-approval; reviews land in `reviews/`.

## The specs

| Spec | Item | Tier | Target | One-liner |
|------|------|------|--------|-----------|
| [TOOL-aPrunedCeremony-1](spec/2026-07-19-spec-aPrunedCeremony-1.md) | manifest-driven legs + no-hardcode canary | 2 | `tools/run-gates.sh` | Move the leg list into data + a canary forbidding inlined leg commands — pays off only with a SECOND runner (a PowerShell twin, a CI matrix). |
| [TOOL-aPrunedCeremony-2](spec/2026-07-19-spec-aPrunedCeremony-2.md) | pre-push enforcement (+ drift-signal note) | 2 | `.githooks/pre-push` | A `pre-push` hook runs the full `run-gates.sh` on a push to `main`; the inCMS hook-staleness drift-signal is N/A here (tracked-dir hooksPath, not a copy). |

## Owner decision menu

1. **TOOL-1 — build the manifest runner now, or defer as YAGNI?** The byte-parity twin-runner
   machinery only earns its keep with a second consumer. coding-governance runs one bash runner.
   **Recommend: defer** — adopt only the cheap half (a no-hardcode canary over the existing runner)
   if desired, and build the manifest the day a PowerShell runner or CI matrix is added. Detail in
   TOOL-1 §8.
2. **TOOL-2 — add the pre-push enforcement hook?** This repo has `pre-commit` but no `pre-push`; the
   full bar is run manually. A `pre-push` hook makes the boundary machine-enforced (pairs with
   PLAY-aPrunedCeremony-1). **Recommend: yes, small and high-value.** Detail in TOOL-2 §8.
3. **TOOL-2 — drift signal: confirm N/A.** inCMS needed a staleness signal because it COPIES hooks
   to an out-of-tree dir; coding-governance points `core.hooksPath` at the tracked `.githooks/`
   directly and `check-wiring.sh` already auto-wires an unset path. **Recommend: record N/A**, do not
   port the signal. Detail in TOOL-2 §4/§8.
