# PLAY-aPrunedCeremony-1 — the full merge bar runs once, at the push boundary

**Status:** OPEN · rev-1 · 2026-07-19 · node a · Tier-2 · base bf7f2c22

## 1. Goal

Replace the playbook's "re-run the full gate suite after EVERY merge" rule with the gate-economy
principle proven in inCMS `ARCH-aTrimmedGauntlet-2`: the full merge bar runs ONCE, at the push
boundary; every earlier run (worktree DoD, post-merge) is diff-scoped. This removes the triple-run
ritual (worktree → post-merge → pre-push) that spends the full suite three times to certify one
integration, while keeping the same protection — a red never reaches shared `main`.

## 2. Scope (IN)

- S1 — Rewrite template §1 "Landing — merge protocol" line 48 (`Re-run the full gate suite after
  EVERY merge — a conflict-free merge is not a passing merge.`) to: a scoped gate after each merge
  (verifying the merge introduced no break in the changed surface), and the full bar exactly once,
  at the push boundary. Keep the "a conflict-free merge is not a passing merge" clause — it is still
  true, and now motivates the *scoped* post-merge run.
- S2 — Add the enforcement sentence, phrased conditionally on project capability: where the project
  enforces a push boundary (a `pre-push` hook running `{{GATE_RUNNER}}`), the full run lives there
  and is machine-enforced; where it does not, the fallback is scoped-at-merge plus one full run
  before the push, run by the lander.
- S3 — Reconcile the DoD (template §1 line 39, "Gates green") to name the scoped run as the
  DoD-time gate, so DoD and Landing agree on which run happens when.
- S4 — Update this repo's own dogfood prose in `AGENTS.md` ("The gate suite (the merge bar)",
  "All green before any merge") to match, so the reference dogfood is not stricter than the playbook
  it ships (owner fork 2, §8).
- S5 — Add a one-line cross-reference to the fail-closed-scoping discipline (PLAY-aPrunedCeremony-2)
  and the pre-push enforcement kit (TOOL-aPrunedCeremony-2) so the three land coherent.

## 3. Non-goals (OUT)

- Not building the pre-push hook or the scope surface — those are TOOL-aPrunedCeremony-1/-2 and this
  repo's own adoption. This spec is the *playbook wording* only.
- Not changing the leg SET or what "full bar" means.
- Not retiring the ledger `pushed:<sha>` vocabulary (template §3 line 87) — related inCMS Q4 change,
  deliberately out of the six; noted as a follow-up in the build README menu.
- Not mandating diff-scoping for projects whose suite is already sub-minute — the principle is
  "don't run the full bar more than once per integration", not "always scope".

## 4. Design

### Data model

N/A — prose-only change to `parallel-coding-governance.template.md` and `AGENTS.md`.

### Inventory

| Edit site | Current text (verified at base) | Change |
|-----------|--------------------------------|--------|
| template §1 L48 | "Re-run the full gate suite after EVERY merge — a conflict-free merge is not a passing merge." | Rewrite to scoped-after-merge + full-once-at-push (S1, S2). |
| template §1 L39 | "Gates green (§7); the change verified by a check that exercises it (§8), not asserted." | Clarify: the DoD gate is the scoped run over the unit's diff (S3). |
| AGENTS.md §"gate suite" L46-48 | "All green before any merge; each rides the runner:" | "The full bar is the push boundary; earlier runs are scoped." (S4) |

Proposed replacement for §1 L48 (two bullets):

```
- After each merge run a SCOPED gate over the merge's changed surface — a conflict-free merge is not
  a passing merge, but re-running the WHOLE bar per merge spends it N times to certify one push. The
  full bar runs exactly ONCE, at the push boundary.
- Enforce the boundary where the project can: a `pre-push` hook running {{GATE_RUNNER}} blocks a red
  push to shared `main` (machine-enforced, single authoritative run). Where no such hook exists, the
  lander runs the full bar once before pushing.
```

### Migration

N/A — no data or code; adopting projects inherit the wording on their next template sync.

### Rollout

Doc-only; lands with the template. No flag. The behavioral change (a project actually running one
boundary gate instead of three) is enabled by TOOL-aPrunedCeremony-2, not by this wording.

### Files touched (estimate)

`parallel-coding-governance.template.md` (2 sites), `AGENTS.md` (1 site). ~10 changed lines.

### Alternatives rejected

- **Leave line 48 as-is, add scoping as an option.** Rejected: line 48 as written *mandates* the
  full suite after every merge, which directly contradicts `run-gates.sh`'s own `leg_if_changed`
  scoping — the charter would stay stricter than the kit it ships. The contradiction is the bug.
- **Mandate a pre-push hook unconditionally.** Rejected: the playbook is project-agnostic; a project
  may run gates only in CI. The principle is universal, the mechanism is not — hence S2's conditional.

## 5. Production-readiness checklist

- security — N/A (prose).
- perf / scale — the whole point: removes 2 of 3 full-suite runs per integration; the boundary run
  is unchanged.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the boundary run is the one authoritative signal; a scoped run must print WHICH
  legs it skipped and why (covered by PLAY-aPrunedCeremony-2 and the §16 reporting rules), so a
  scoped green is never mistaken for a full green.
- risks — the load-bearing risk: a scoped run green-by-absence lets a break reach the boundary. The
  boundary full run is the backstop; PLAY-2's fail-closed rule keeps the scoping honest. Named here,
  mitigated there.
- testing + left-shift gates — none added by the wording; the enforcement test rides
  TOOL-aPrunedCeremony-2.
- migration / rollback — revert the template edit; no state.
- user docs — N/A (this IS the operating doc).

## 6. Acceptance criteria

- AC1 — When template §1 Landing is read after this change, it states the full bar runs once at the
  push boundary and the post-merge run is scoped — and the phrase "after EVERY merge" no longer
  demands the full suite.
- AC2 — When `grep -n "after EVERY merge" parallel-coding-governance.template.md` runs, it returns
  nothing (the old mandate is gone), and the template-size gate (`check-template-size.sh`, ≤32 KiB)
  stays green.
- AC3 — When `AGENTS.md` is read, its gate-suite section agrees with the template (no "green before
  any merge" mandate contradicting the scoped-merge rule).
- AC4 — When the DoD (§1 L39) and Landing (§1 L46-52) are read together, they name the same run at
  the same point (scoped at DoD/merge, full at push) with no contradiction.

## 7. Gates

`check-template-size.sh` (≤32 KiB — the edit must not push the template over budget), the
memory-tree hygiene gate (this spec + README conform to check 4/5/12), and `check-kit-versions.sh`
(unaffected). No new gate; the enforcement gate is TOOL-aPrunedCeremony-2's.

## 8. Open questions

- **Fork A — enforcement conditional wording (owner menu 1).** RECOMMEND: adopt S2's conditional —
  "where the project enforces a push boundary … otherwise the fallback is scoped-at-merge + full
  before push". Keeps the principle universal without mandating a hook every project can run.
- **Fork B — reconcile AGENTS.md dogfood in this build (owner menu 2).** RECOMMEND: yes (S4) — a
  reference dogfood that contradicts its own template is exactly the drift this kit exists to catch.
  The alternative (leave AGENTS.md, file a follow-up) risks the contradiction rotting.
- **Fork C — keep or cut "a conflict-free merge is not a passing merge".** RECOMMEND: keep it — it
  now correctly motivates the *scoped* post-merge run rather than the full one.

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
