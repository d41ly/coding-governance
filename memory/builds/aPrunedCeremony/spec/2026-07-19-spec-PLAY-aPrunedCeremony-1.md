# PLAY-aPrunedCeremony-1 — the full merge bar runs once, at the push boundary

**Status:** CLOSED · rev-2 · 2026-07-19 · node a · Tier-2 · base bf7f2c22 · reviewed wf_2f11fd07 · ratified 2026-07-19

## 1. Goal

Replace the playbook's "re-run the full gate suite after EVERY merge" rule with the gate-economy
principle proven in inCMS `ARCH-aTrimmedGauntlet-2`: the full merge bar runs ONCE, at the push
boundary; every earlier run (worktree DoD, post-merge) is diff-scoped where the project's runner
supports it. This removes the triple-run ritual (worktree → post-merge → pre-push) that spends the
full suite three times to certify one integration, while keeping the same protection — a red never
reaches shared `main`.

## 2. Scope (IN)

- S1 — Reword template §1 "Landing" line 48 (`Re-run the full gate suite after EVERY merge — a
  conflict-free merge is not a passing merge.`) IN PLACE to the new policy: a scoped gate after each
  merge where the runner supports it, and the full bar exactly once at the push boundary. Keep the
  "a conflict-free merge is not a passing merge" clause. This is a byte-neutral REWORD of an existing
  line, not an addition (see §4 Rollout — the ≤32 KiB budget forbids net growth).
- S2 — Reword template §7 line 126 (`Keep the automated suite green before any merge:
  {{GATE_COMMANDS}} …`), the SECOND authoritative "green before any merge" mandate the rev-1 spec
  missed — reconcile it to the same scoped-at-DoD/full-at-push model, in place.
- S3 — Reword template §14 line 185 (`… the full-repo gate at merge …`) → "at the push boundary",
  in place.
- S4 — Update `AGENTS.md` (this repo's dogfood, NOT byte-capped): the gate-suite header and its
  self-test list, plus `tools/run-gates.sh` line 3's header comment (`All green before any merge.`),
  to match — so the reference dogfood is not stricter than the playbook it ships (owner fork B).
- S5 — Reconcile the DoD (template §1 line 39, "Gates green") so it names the scoped run as the
  DoD-time gate, in place.
- S6 — Any enforcement DETAIL that will not fit as an in-place reword lands in
  `parallel-coding-governance.domain-rules.md` (the uncapped overflow companion), referenced from
  the reworded template line by a `§`-stub — never as net template bytes.

## 3. Non-goals (OUT)

- Not building the pre-push hook or a scope surface — those are TOOL-aPrunedCeremony-1/-2 and the
  adopting project's own runner. This spec is the playbook WORDING only.
- Not adding net bytes to the template (§4 Rollout). All template edits are in-place rewords or
  externalize to domain-rules.
- Not retiring the ledger `pushed:<sha>` vocabulary (template §3 line 87) — the related inCMS Q4
  change, deliberately out of the six (see PLAY-aPrunedCeremony-4 §8 for the coupled interaction).
- Not mandating diff-scoping for every project — the principle is "don't run the full bar more than
  once per integration", and the post-merge scoped step is conditional on the runner supporting it
  (S1).

## 4. Design

### Data model

N/A — prose-only change to `parallel-coding-governance.template.md`, `AGENTS.md`, `tools/run-gates.sh`.

### Inventory

Every template edit is an in-place REWORD of an existing line (net bytes ≈ 0); new prose goes to the
uncapped companion. This is the core rev-2 correction — the rev-1 spec added bullets and busted the
gate (review wf_2f11fd07 R-PLAY-1-HIGH).

| Edit site | Current text (verified live) | Change | Byte effect |
|-----------|------------------------------|--------|-------------|
| template §1 L48 | "Re-run the full gate suite after EVERY merge — a conflict-free merge is not a passing merge." | Reword: scoped-after-merge (if supported) + full once at push (S1). | ≈0 (reword) |
| template §7 L126 | "Keep the automated suite green before any merge: `{{GATE_COMMANDS}}` …" | Reword: green before the PUSH; earlier runs scoped (S2). | ≈0 |
| template §14 L185 | "… the full-repo gate at merge …" | "… the full-repo gate at the push boundary …" (S3). | ≈0 |
| template §1 L39 | "Gates green (§7); …" | Clarify the DoD gate is the scoped run over the unit diff (S5). | ≈0 |
| AGENTS.md gate-suite + L48 | "All green before any merge; each rides the runner:" | Full bar = the push boundary; earlier runs scoped (S4). | uncapped |
| run-gates.sh L3 | "# All green before any merge." | "# All green before any PUSH to main; earlier runs scoped." (S4). | uncapped |

### Migration

N/A — adopting projects inherit the wording on their next template sync.

### Rollout

Doc-only. **The ≤32 KiB template gate (`tools/check-template-size.sh`, live headroom 86 bytes) is a
hard merge-bar leg** — so every template edit here is an in-place reword with net bytes ≈ 0, and the
build MUST re-run `check-template-size.sh` after the edits and prove ≤ 32768 before landing (this
also bounds the shared budget across PLAY-2/-4, which now externalize their new content rather than
add it). The behavioral change (one boundary gate instead of three) is enabled by
TOOL-aPrunedCeremony-2, not by this wording.

### Files touched (estimate)

`parallel-coding-governance.template.md` (4 in-place rewords), `AGENTS.md` (2 sites),
`tools/run-gates.sh` (1 header line), optionally `.domain-rules.md` (S6). ~12 changed lines, net
template bytes ≈ 0.

### Alternatives rejected

- **Add new bullets to the template (rev-1's approach).** Rejected: the template has 86 bytes of
  headroom under a hard gate; two added bullets measured +409 and busted it (wf_2f11fd07). Reword in
  place, externalize the rest.
- **Mandate a pre-push hook unconditionally.** Rejected: the playbook is project-agnostic; a project
  may run gates only in CI. The principle is universal, the mechanism is not — hence the conditional
  in S1.
- **Keep the "contradicts run-gates.sh" motivation (rev-1).** Rejected as FALSE: run-gates.sh's own
  header (L3) reads "All green before any merge" — it AGREES with template L48. The runner scopes
  only 2 self-test legs via `leg_if_changed`; it is not a whole-run scoped runner. The real
  motivation stands alone: do not spend the full bar three times to certify one integration.

## 5. Production-readiness checklist

- security — N/A (prose).
- perf / scale — the point: removes 2 of 3 full-suite runs per integration; the boundary run is
  unchanged.
- a11y / i18n — N/A.
- error / empty / loading states — N/A.
- observability — a scoped run must print which legs it skipped and why (§16 L205 reporting rules),
  so a scoped green is never mistaken for a full green.
- risks — a scoped run green-by-absence lets a break reach the boundary; the boundary full run is the
  backstop and PLAY-aPrunedCeremony-2 keeps the scoping honest. Named here, mitigated there.
- testing + left-shift gates — none added by the wording; the ≤32 KiB gate is the one that must be
  re-verified post-edit (§4 Rollout). The enforcement test rides TOOL-aPrunedCeremony-2.
- migration / rollback — revert the edits; no state.
- user docs — N/A (this IS the operating doc).

## 6. Acceptance criteria

- AC1 — When template §1 Landing and §7 are read after this change, BOTH state the full bar runs once
  at the push boundary and earlier runs are scoped — and neither "after EVERY merge" (L48) nor
  "green before any merge" (L126) still mandates the full suite per merge.
- AC2 — When `bash tools/check-template-size.sh` runs after the edits, it exits 0 (≤ 32768 bytes) —
  proven by measurement, not asserted; the in-place rewords keep net bytes ≈ 0.
- AC3 — When `grep -rn "after EVERY merge\|full-repo gate at merge" parallel-coding-governance.template.md`
  runs, it returns nothing (both old mandates reworded).
- AC4 — When `AGENTS.md`, `tools/run-gates.sh` (L3), and the template are read together, they agree
  (no "green before any merge" prose contradicting the scoped-merge rule).

## 7. Gates

`tools/check-template-size.sh` (≤32 KiB — MUST be re-run and green after the edits; the load-bearing
gate for this spec), the memory-tree hygiene gate (this spec + README conform to check 4/5/12),
`check-kit-versions.sh` (unaffected). No new gate; enforcement is TOOL-aPrunedCeremony-2's.

## 8. Open questions

none — all forks below are RESOLVED (owner-ratified 2026-07-19); kept for the record.

- **Fork A — enforcement conditional wording (owner menu 1).** RESOLVED (2026-07-19): built as recommended — adopt S1's conditional —
  "where the project enforces a push boundary … otherwise scoped-at-merge + full before push". The
  post-merge scoped step is itself conditional on the runner supporting whole-run diff-scoping
  (which the kit's own `run-gates.sh` does NOT — it scopes only self-test legs), so the wording must
  not presume a mechanism the kit lacks (review R-PLAY-1-MED).
- **Fork B — reconcile AGENTS.md + run-gates.sh header in this build (owner menu 2).** RESOLVED (2026-07-19): built as recommended —
  yes (S4) — a reference dogfood that contradicts its own template is exactly the drift this kit
  exists to catch.
- **Fork C — keep or cut "a conflict-free merge is not a passing merge".** RESOLVED (2026-07-19): built as recommended — keep — it now
  motivates the scoped post-merge run.

## 9. Revision log

- rev-1 · 2026-07-19 · initial draft (node a, aPrunedCeremony).
- rev-2 · 2026-07-19 · folded review wf_2f11fd07: template ≤32 KiB budget (in-place rewords, not
  additions; AC2 now measures); added missed edit sites §7 L126 / §14 L185 / run-gates.sh L3;
  dropped the false "contradicts run-gates.sh" motivation; made the post-merge scoped run
  conditional on runner support; status → SPECCED.
