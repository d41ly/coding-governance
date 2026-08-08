# Adversarial review — TOOL-bConvergentLodestar-1 (rev-1)

**Reviewed:** 2026-07-22 · node b · 4 lenses (convergence-efficacy · portability · soundness ·
production-scope) + skeptic verify · `wf_69de6d2e-926`. 33 findings; skeptic verdicts: 5 blockers
CONFIRMED (+1 blocker design-judgment, accepted), ~15 majors CONFIRMED, 1 major REFUTED (stale), rest
minors/nits. Verdict: **needs-rework** — rev-1 adds recall + a dashboard but no new *force* on the
reinvention rate, and its metric is not falsifiable, so it does not meet the owner's "converges, not
ceremony" bar. All confirmed findings folded to **rev-2**.

## Blockers (all fixed in rev-2)

1. **Metric not falsifiable (#0/#8).** wire-through ratio = survivorship bias (only authors who ran the
   lookup); affordance-coverage% = documentation-theatre (S4 drives it to ~100% with zero dup reduction);
   dead-exports = confounded; new_clones = optional/foreign. Fix: re-derive S5 around a signal over ALL
   new code (the collision-without-fanin-edge proxy), make the clone signal required, demote the other two.
2. **No closing loop for the modal semantic class (#1).** S3 is the same advisory pass the diagnosis
   condemned + a dashboard; nothing catches *shipped* semantic reinvention. Fix: the collision signal,
   surfaced as a review WARN → reinvention backlog — a soft force, not a hard gate (which false-positives).
3. **Regex symbol tier cannot fail-closed (#9/#16).** `export (function|const|class)` silently misses
   `export default`, re-exports, `type`/`interface`/`enum`, decorated/abstract — green-by-absence the kit
   bans, and the freshness gate structurally cannot catch fail-open. Fix: real parser, or enumerate ALL
   export forms and raise `MapError` on an unmatched `export ` line; AC2 reframed to a fail-closed unit test.
4. **`fanin` in the freshness-gated `symbols.json` churns (#17/#12/#25).** A live reference count restales
   the artifact on nearly every commit — the exact mistake `render_inventories_json` (map_lib.py:421) was
   written to avoid. Fix: `symbols.json` = `{id,kind,file}` only; fan-in computed on demand in
   reuse-lookup/converge-report, never committed/gated.
5. **`## Reuse affordance` in `REQUIRED_HEADINGS` retro-reds every dossier (#22/#10).**
   `test_dossier_prose_headings_pinned` loops `REQUIRED_HEADINGS` over EVERY dossier with no exemption. Fix:
   a separate `AFFORDANCE_HEADING` + a graced check consulting an affordance-exempt list; do not touch
   `REQUIRED_HEADINGS`.

## Majors (fixed in rev-2)

- **Recall substrate mis-ranks the seams that matter (#2/#13/#19/#28).** Lexical rank was quantified 0%
  behavioural by the sibling diagnosis; the shortlist cutoff is the real recall gate; grep-fanin
  false-negs on registries/dynamic-dispatch (inCMS's most-reused seams are *registered*, not named) and
  false-positives on common-word ids (`get`/`render`). Fix: import/identifier-scoped fan-in; widen the
  shortlist to token-stem + structural neighbours (not hard top-K lexical); document the registry recall
  FLOOR; reconcile S3 explicitly as bThriftyCompass S1's portable re-implementation.
- **`dead_exports` invalid as a convergence signal (#3/#18).** A used duplicate isn't dead; feature-adds
  raise it; library/SDK repos keep it permanently high (breaks "any repo"). Fix: demote to a hygiene hint,
  off the convergence claim; re-anchor AC4 on the clone/collision signal.
- **Affordance-baseline has no seed path for already-adopted repos (#4/#14).** Fix: `gen_map.py
  --seed-affordance-baseline` (mirrors `--seed-baseline`), wired into the adopter; AC for a green re-adopt.
- **`converge-report` forks `map_diff` (#31).** `map_diff.py` already walks `<base>..<head>` and calls
  itself "the map's convergence-visibility metric." Fix: add the signals as a `map_diff` mode, not a
  second range-walker (a convergence tool must not reinvent the range-walker).
- **`reuse_decisions` not measurable + decision-log undefined (#23/#24).** The log records that a lookup
  RAN, not what the author shipped; location/format/commit/sharding all unspecified with a concurrency
  defect. Fix: drop `reuse_decisions` from the core signals (collision + clones are bypass-proof); promote
  the decision-log home to an explicit §8 fork.
- **recall-dark layer = silent false-negative (#27).** Fix: an explicit covered-layers list; reuse-lookup
  prints "recall partial: layers X have no symbol extractor" so "no seam fits" is never falsely confident.
- **AC2 tests the wrong invariant (#26).** Reframed to fail-closed `MapError`, per `t_extractor_helpers_fail_closed`.

## Minors / nits (folded)

S4a exemption-drop is socially-enforced not gate-detected — reword (#5/#32). AC3 rebased on a fixture, not
an inCMS path (#6/#11/#30). Micro-format: parse all leading `seam:` lines, accept `-`/`–`/`—` (#20). Perf:
measure on a fixture, state a budget, define fan-in as file-count (#7/#21). Files-touched: add the adopter,
fix the WIRE-INTO-PROJECT path (#7/#14).

## Refuted / stale

- **#29 (REFUTED):** claimed bThriftyCompass-1 is SPECCED-not-built so the grounding is false. It is now
  CLOSED + pushed to `origin/main`. rev-2 softens "re-adopted" to "re-adoption is the rollout" (the kit
  hasn't adopted it yet) but keeps the "shipped in inCMS" grounding, which is true.

## Resolution

rev-2 re-derives §1 (goal), §2 (S1/S2/S3/S5), §3, §4 (data model + migration + converge-report-as-map_diff),
§5, §6 (fixture ACs), and §8 (+decision-log fork), and logs it in §9. The load-bearing change is the
shipped-reinvention collision signal — the closing loop that turns "recall + dashboard" into a mechanism
that catches reinvention at review and routes it to consolidation.
