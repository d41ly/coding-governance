# Manifest ratchet — build report (unattended session, 2026-07-12)

The durable record of the unattended build that implemented `manifest-ratchet-spec.md`. Companion
to the spec (design history) and `reviews/2026-07-12-tier2-cumulative-main.md` (closing review).
Process per the owner's standing order: sub-spec each unit → adversarial review (≤4 concurrent
agents) before code → ratify decisions → build → commit per step → closing adversarial review →
merge + push only at the end.

## What shipped (BASE `dacade14` → this merge)

| Unit | Artifact | Substance |
|---|---|---|
| — | `manifest-ratchet-spec.md` | governing spec, committed as the design record (2 pre-build review rounds: 66 findings folded) |
| A | `skills/session-kickoff/manifest-check.sh` | the ratchet gate: C1 placeholders · C2 block parse+format · C3 anchor real+ancestor · C4 tracked anchors · C5 topological+structural drift · C5s staged leg · C6 watch liveness · version WARN · unmanaged NOTE |
| A | `skills/session-kickoff/manifest-check.test.sh` | 38-scenario suite, global-git-config-isolated, no-fatal + silent-green contracts pinned on every scenario |
| B | `skills/session-kickoff/MANIFEST-TEMPLATE.md` → v1.1 | manifest-audit block · ratchet contract · dated-corrections section (never-delete) · traps-accrete · standing gate-fence line · 23 normalized placeholders with full Customize parity |
| C | `skills/session-kickoff/SKILL.md` | Step 2b read-repair (run-don't-reimplement, trust-guarded `check-script:`, delta line + counter, commit vehicle) · scaffolding ratchet wiring · fallback template-skip fix · READY card carries the delta line |
| D | `parallel-coding-governance.template.md` → v2.2 | two §1 insertions: DoD manifest write-back (with the re-derivation accretion trigger) + `last-audit` reconcile exception; v2.1 snapshotted verbatim |
| E | `WIRE-INTO-PROJECT.md` + `README.md` | §4 ratchet wiring order (gitattributes → git add → check; `fetch-depth: 0` mandated) · durable 6-step retrofit recipe (body-first, marker-last) · §6 commit-first red/green probe · Maintenance stall review (≥10 watch commits or ≥3 months with zero body growth) |
| F | *(machine config)* | `~/.claude/skills/session-kickoff` stale inCMS copy → junction to the gov engine (backup in `%TEMP%\session-kickoff-stale-backup`; inCMS original untouched in its repo) |

## Review ledger (all adversarial, ≤4 concurrent agents per wave)

| Stage | Agents | Findings → folded |
|---|---|---|
| Spec round 1 (pre-session) | 18 | 39 confirmed + 5 gaps (precision 0.75) |
| Spec round 2 (pre-session) | 3 | 22 defects — incl. the two C5 semantics rewrites |
| Spec coherence pass | 1 | 4 fold slips |
| Unit A sub-spec review | 4 | 24 — incl. 3 demonstrated false-greens (rename laundering, decoy stamps, path-arg misresolution) |
| Units B–E doc review | 4 | 9 (1 per B/D, 3 C, 4 E — incl. the staged-chain probe false-green, demonstrated) |
| Closing tier2 (whole diff) | 8 | ship: 0 blockers, 0 highs, 3 lows — all fixed |

## Ratified decisions (the load-bearing ones; full rationale in the spec)

1. **C5 drift check is topological + structural** — newest watch-touching commit `W` must be an
   ancestor of the newest commit `S` that changed the audit block's `last-audit` VALUE; candidates
   from a pathspec-free `-G` scan (rename-proof), each validated block-stamp-vs-parent
   (decoy/reorder-proof). Two earlier textual designs were empirically broken by reviewers
   (same-commit sha paradox; true-merge laundering).
2. **Stamps are ISO datetimes with offset @ full 40-hex sha** — datetime so a frozen-anchor re-stamp
   is always committable; sha per the stamp rule: HEAD on the default branch, else merge-base
   against the (remote, else local) default — branch shas get orphaned by squash-merges.
3. **The staged leg narrows deliberately** to the bundle-into-this-commit form; stated at wiring
   time, one-directional consistency (C5s-green ⇒ C5-green) verified.
4. **The gate is wired by default** via the manifest's own gate-commands fence (enforcement floor:
   kickoff-only projects still enforce at every unit's merge bar); pre-commit/CI are offered
   hardening, CI mandates `fetch-depth: 0` (default shallow checkouts silently skip the drift check).
5. **Retrofit is body-deltas-first, marker-bump-LAST** — bumping first silences the version WARN
   while the freeze directive survives; step 5 re-pulls the v2.2 playbook lines (lever 2 for
   existing adopters).
6. **Unmanaged manifests (no marker) are skipped, never nagged** — the inCMS prototype stays as-is.
7. **`check-script:` is data, not an execution license** — the engine honors it only for a tracked
   in-repo `manifest-check.sh` (closing-review trust guard).
8. **Accretion ≠ repair**: the DoD trigger list includes "a fact this session had to re-derive";
   dated corrections get a never-deleted section with prune-when expiry; the stall review rides
   WIRE Maintenance with concrete thresholds, reading git-derivable body-growth (squash-proof), not
   chat ephemera.
9. Staged mode runs C1/C2/C4/C6 + C5s (committed-range scans C3/C5 belong to full mode) — the
   pre-commit fast-leg convention.
10. Six-step retrofit inlined verbatim in C2's fail message — a self-contained remedy beats a short
    form (house no-load-bearing-pointer rule); spec amended to match.

## Acceptance battery (§10) — all green

10.1 suite 38/38 · 10.2 fresh-scaffold probe (clean, placeholder-free, survives unwatched commits) ·
10.3 placeholder parity 23/23 both directions · 10.4 baseline `{{` grep: only deliberate deltas ·
10.5 agent-cap collateral 0 · 10.6 search order 1–4 verbatim + gov-repo fallback resolves to
no-manifest + inCMS prototype NOTE+0 · 10.7 playbook diff = header¶ + marker + two insertions,
nothing else · 10.8 lever-1 end-to-end (drift → red → repair+re-stamp → green, delta line with
counter in the commit message) · 10.9 stall review defined with named reader/cadence/thresholds ·
10.10 project memories updated.

## Build log (branch `feature/manifest-ratchet`)

- `a9e8744` spec committed (design record)
- `98d4448` Unit A — gate + suite (24 review findings folded; 38/38)
- `59f57ae` Unit B — template v1.1
- `310562b` Unit C — engine Step 2b + scaffolding
- `1f11e6c` Unit D — playbook v2.2 + v2.1 snapshot
- `04dc139` Unit E — wire docs + README
- `24c6572` closing review: 3 lows fixed + report committed
- *(this commit)* build report; then the `--no-ff` merge to `main` + push

## Known residuals (documented, accepted)

C5's decoy-predating-rename corner · tracked-but-dead verify-path stubs pass C4 · deliberate watch
narrowing (compensating control: manifest-diff review) · GNU-ish `realpath` preferred (textual
fallback covers git-bash/ubuntu; exotic busybox setups degrade to exit-2, never false-green).

## Follow-ups (not in this unit)

- Retrofit nicocares per WIRE §4's recipe (first real candidate; separate repo).
- inCMS convergence decision (its prototype now cleanly coexists as unmanaged).
- Restart Claude Code once so the skill list picks up the junction (already verified live in this
  session).
