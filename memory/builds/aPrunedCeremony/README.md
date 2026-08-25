---
slug: aPrunedCeremony
node: a
opened: 2026-07-19
streams: playbook+tooling
roster: PLAY+TOOL
ids: PLAY-aPrunedCeremony-1 PLAY-aPrunedCeremony-2 PLAY-aPrunedCeremony-3 PLAY-aPrunedCeremony-4 PLAY-aPrunedCeremony-5 TOOL-aPrunedCeremony-1 TOOL-aPrunedCeremony-2
---

# aPrunedCeremony — gate-economy uplift (playbook + tooling)

**streams playbook+tooling.** One session, two id families, two halves of the same port of inCMS
`ARCH-aTrimmedGauntlet-2`. Before the flatten these were two build folders under two discipline
directories; the discipline is now a signal, not a path, so they are one build. Every recording
inside carries its FAMILY in the filename, which is what makes `PLAY-aPrunedCeremony-1` and
`TOOL-aPrunedCeremony-1` — different ids that shared a filename — coexist here.

The two sections below are the two original build-root overviews, unedited apart from the spec links
now pointing at the FAMILY-qualified filenames.

---

## PLAY half — gate-economy uplift for the playbook (specs)

**Master overview + owner decision menu for the playbook half of the gate-economy port.** Four
doc-only specs lifting the durable, project-agnostic lessons of inCMS `ARCH-aTrimmedGauntlet-2`
(the "gate-execution economy" build) into `parallel-coding-governance.template.md` and
`.domain-rules.md`. The tooling half (a manifest-driven runner, a pre-push enforcement hook) is the
TOOL section below.

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

### The specs

| Spec | Item | Tier | Edit site | One-liner |
|------|------|------|-----------|-----------|
| [PLAY-aPrunedCeremony-1](spec/2026-07-19-spec-PLAY-aPrunedCeremony-1.md) | full run at the push boundary | 2 | template §1 Landing line 48 + §7; AGENTS dogfood | The full merge bar runs ONCE at the push boundary; earlier runs are diff-scoped — replaces "re-run the full suite after EVERY merge". |
| [PLAY-aPrunedCeremony-2](spec/2026-07-19-spec-PLAY-aPrunedCeremony-2.md) | fail-closed coarse scoping | 1 | template §7 | Diff-scoping is fail-closed and COARSE — an unclassified path runs the full bar; do not build precise per-path targeting (indirect reads make it unsafe). |
| [PLAY-aPrunedCeremony-3](spec/2026-07-19-spec-PLAY-aPrunedCeremony-3.md) | vacuous-ratchet bug class | 1 | `.domain-rules.md` §10 | A ratchet whose matcher never matches its target is vacuous — prove a gate CATCHES an injected regression, never trust that it is green. |
| [PLAY-aPrunedCeremony-4](spec/2026-07-19-spec-PLAY-aPrunedCeremony-4.md) | bookkeeping before push | 1 | template §1 Landing | Bookkeeping lands BEFORE the push; no trailing doc-only commit after a push. |

### Owner decision menu

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

---

## TOOL half — gate-economy uplift for the tooling kits (specs)

**Master overview + owner decision menu for the tooling half of the gate-economy port.** Two specs
lifting the *mechanism* half of inCMS `ARCH-aTrimmedGauntlet-2` into `tools/run-gates.sh` and
`.githooks/`. The playbook (charter-wording) half is the PLAY section above.

Both carry a genuine "should we build this at all?" fork — the honest output of the design pass is
that neither is an obvious yes for THIS repo's shape (a single bash runner, hooks wired as a tracked
dir). Specs awaiting owner build-approval; reviews land in `reviews/`.

**Review outcome (wf_2f11fd07, folded to rev-2).** TOOL-1: the rev-1 "defer the manifest, keep the
canary" fallback was incoherent — the canary asserts the runner sources the manifest, so it cannot
exist without it; the real fork is now **build-both or defer-both** (recommend defer, no second
runner justifies it). Also corrected a false "Python is already a hard requirement" claim (it is
soft today; the manifest makes it hard → a startup probe is added). TOOL-2: the `.gitattributes`
change is **ADD, not verify** (extensionless hook files were unpinned), and the drift-signal is
**N/A only for this repo's direct-wire model** — the `WIRE-INTO-PROJECT.md` copy-install path DOES
reintroduce the staleness, so it is a scoped follow-up rather than universally moot.

### The specs

| Spec | Item | Tier | Target | One-liner |
|------|------|------|--------|-----------|
| [TOOL-aPrunedCeremony-1](spec/2026-07-19-spec-TOOL-aPrunedCeremony-1.md) | manifest-driven legs + no-hardcode canary | 2 | `tools/run-gates.sh` | Move the leg list into data + a canary forbidding inlined leg commands — pays off only with a SECOND runner (a PowerShell twin, a CI matrix). |
| [TOOL-aPrunedCeremony-2](spec/2026-07-19-spec-TOOL-aPrunedCeremony-2.md) | pre-push enforcement (+ drift-signal note) | 2 | `.githooks/pre-push` | A `pre-push` hook runs the full `run-gates.sh` on a push to `main`; the inCMS hook-staleness drift-signal is N/A here (tracked-dir hooksPath, not a copy). |

### Owner decision menu

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

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `PLAY-aPrunedCeremony-1` | 2 | the full merge bar runs once, at the push boundary |
| 2 | `PLAY-aPrunedCeremony-2` | 1 | diff-scoped gates are fail-closed and coarse |
| 3 | `PLAY-aPrunedCeremony-3` | 1 | recurring bug class: a ratchet that never exercises its target is vacuous |
| 4 | `PLAY-aPrunedCeremony-4` | 2 | bookkeeping lands before the push; retire the derivable `pushed:<sha>` |
| 5 | `TOOL-aPrunedCeremony-1` | 2 | manifest-driven gate legs + a no-hardcode canary |
| 6 | `TOOL-aPrunedCeremony-2` | 2 | pre-push full-gate enforcement (drift signal scoped, not dropped) |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 6 unit(s) · node a · opened 2026-07-19 · streams playbook+tooling
ids PLAY-aPrunedCeremony-1 PLAY-aPrunedCeremony-2 PLAY-aPrunedCeremony-3 PLAY-aPrunedCeremony-4 PLAY-aPrunedCeremony-5 TOOL-aPrunedCeremony-1 TOOL-aPrunedCeremony-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [PLAY-aPrunedCeremony-1 — the full merge bar runs once, at the push boundary](spec/2026-07-19-spec-PLAY-aPrunedCeremony-1.md) | — | 2 | CLOSED | rev-2 | 2026-07-19 |
| [PLAY-aPrunedCeremony-2 — diff-scoped gates are fail-closed and coarse](spec/2026-07-19-spec-PLAY-aPrunedCeremony-2.md) | — | 1 | CLOSED | rev-2 | 2026-07-19 |
| [PLAY-aPrunedCeremony-3 — recurring bug class: a ratchet that never exercises its target is vacuous](spec/2026-07-19-spec-PLAY-aPrunedCeremony-3.md) | — | 1 | CLOSED | rev-2 | 2026-07-19 |
| [PLAY-aPrunedCeremony-4 — bookkeeping lands before the push; retire the derivable `pushed:<sha>`](spec/2026-07-19-spec-PLAY-aPrunedCeremony-4.md) | — | 2 | CLOSED | rev-4 | 2026-07-19 |
| [TOOL-aPrunedCeremony-1 — manifest-driven gate legs + a no-hardcode canary](spec/2026-07-19-spec-TOOL-aPrunedCeremony-1.md) | — | 2 | CLOSED | rev-4 | 2026-07-19 |
| [TOOL-aPrunedCeremony-2 — pre-push full-gate enforcement (drift signal scoped, not dropped)](spec/2026-07-19-spec-TOOL-aPrunedCeremony-2.md) | — | 2 | CLOSED | rev-3 | 2026-07-19 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->