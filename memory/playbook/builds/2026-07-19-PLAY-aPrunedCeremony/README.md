# PLAY-aPrunedCeremony — gate-economy uplift for the playbook (specs)

**Master overview + owner decision menu for the playbook half of the gate-economy port.** Four
doc-only specs lifting the durable, project-agnostic lessons of inCMS `ARCH-aTrimmedGauntlet-2`
(the "gate-execution economy" build) into `parallel-coding-governance.template.md` and
`.domain-rules.md`. The tooling half (a manifest-driven runner, a pre-push enforcement hook) lives in
the sibling build `memory/tooling/builds/2026-07-19-TOOL-aPrunedCeremony/`.

These are **specs awaiting owner build-approval** — nothing here edits the template yet. Each was
adversarially reviewed (reviews land in `reviews/`); fold-ins bump the spec rev and are logged in §9.

**Review outcome (wf_2f11fd07, 16 confirmed → folded to rev-2).** The load-bearing finding: the
template has **86 bytes of headroom** under the hard `≤32 KiB` gate, so the rev-1 "add a bullet"
approach busted a mandatory merge-bar leg (3 HIGHs). rev-2 restructures accordingly — **new prose
lands in `parallel-coding-governance.domain-rules.md` (the uncapped overflow companion); template
edits are byte-neutral in-place rewords only**, and every spec's size-AC now MEASURES rather than
asserts. Other folds: PLAY-1 gained the missed edit sites (§7 L126, §14 L185, run-gates.sh L3) and
dropped a false "contradicts run-gates.sh" claim; PLAY-2 stopped banning the kit's own
`leg_if_changed` (discriminate on indirection, not map shape) and fixed a wrong §10 citation.

## The specs

| Spec | Item | Tier | Edit site | One-liner |
|------|------|------|-----------|-----------|
| [PLAY-aPrunedCeremony-1](spec/2026-07-19-spec-aPrunedCeremony-1.md) | full run at the push boundary | 2 | template §1 Landing line 48 + §7; AGENTS dogfood | The full merge bar runs ONCE at the push boundary; earlier runs are diff-scoped — replaces "re-run the full suite after EVERY merge". |
| [PLAY-aPrunedCeremony-2](spec/2026-07-19-spec-aPrunedCeremony-2.md) | fail-closed coarse scoping | 1 | template §7 | Diff-scoping is fail-closed and COARSE — an unclassified path runs the full bar; do not build precise per-path targeting (indirect reads make it unsafe). |
| [PLAY-aPrunedCeremony-3](spec/2026-07-19-spec-aPrunedCeremony-3.md) | vacuous-ratchet bug class | 1 | `.domain-rules.md` §10 | A ratchet whose matcher never matches its target is vacuous — prove a gate CATCHES an injected regression, never trust that it is green. |
| [PLAY-aPrunedCeremony-4](spec/2026-07-19-spec-aPrunedCeremony-4.md) | bookkeeping before push | 1 | template §1 Landing | Bookkeeping lands BEFORE the push; no trailing doc-only commit after a push. |

## Owner decision menu

The forks each spec raises, collected for one pass (detail + recommendation in each spec's §8):

1. **PLAY-1 — enforcement is capability-conditional.** The principle (full run at the boundary) is
   universal, but the *mechanism* (a pre-push hook) is a project capability. Ratify the conditional
   wording: where a project enforces a push boundary, the full run lives there; otherwise
   scoped-at-merge + a full run before push is the fallback. **Recommend: yes.**
2. **PLAY-1 — reconcile AGENTS.md dogfood prose too?** This repo's own `AGENTS.md` §"gate suite"
   says "all green before any merge". Update it in the same build for self-consistency, or leave the
   dogfood stricter than the playbook it ships. **Recommend: update it.**
3. **PLAY-2 — coarse two-tier, or keep it a principle only?** inCMS shipped a `gate-scope.json`
   surface; the template's `run-gates.sh` already scopes per-leg via `leg_if_changed`. Adopt the
   *guardrail wording* only (no new artifact), since the runner already fails-safe-to-run.
   **Recommend: wording only.**
4. **PLAY-4 — does dropping `pushed:<sha>` (a related inCMS Q4 change) ride this spec or stay out?**
   The ledger vocab at template §3 line 87 still carries `pushed:<sha>`; inCMS retired it as
   derivable. Out of scope here (it was not among the six), noted for a follow-up. **Recommend: defer.**
