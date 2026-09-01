# DEPL-dGaugedVintage-1 — a version constant an adopter never receives

**Status:** CLOSED · rev-3 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 4 · ratified 2026-09-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-build-DEPL-dGaugedVintage-1-acceptance-ledger.md](../build/2026-09-01-build-DEPL-dGaugedVintage-1-acceptance-ledger.md) | journal | — |
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

`selfcheck` check 5 asserts an entry's `version_from` file EXISTS in gov and that its pattern matches
exactly one line. Nothing asserts that file is inside the entry's own installed population, so a kit
could ship without the constant an adopter pins against and every gate would stay green.

## 2. Scope (IN)

- **S1** — An arm in `selfcheck` check 5 asserting the `version_from` file resolves into the entry's
  own resolved destination set, using the resolver `apply` uses rather than a re-implemented walk.
- **S2** — The refusal names the entry, the declared file, and the fact that it is not shipped —
  not merely that a check failed.
- **S3** — A fixture proving the arm fires: an entry whose `version_from` names a file its own
  `[[files]]` rules exclude.

## 3. Non-goals (OUT)

- The ten entries declaring `version_from.none`. They are exempt by declaration and S1 skips them.
- Whether a shipped constant is READABLE by a deployer once landed. That is
  `DEPL-dGaugedVintage-5`'s marker question, ordered beside this one.
- Changing any entry's `[[files]]` rules. This unit is an assertion; no current entry violates it.
- Check 5b's registry-versus-checker comparison, which stays report-only.

## 4. Design

### Inventory

Measured at `d65da7ab`: all fifteen entries with a `version_from` file resolve it into their own
landed set. NINE do so via an `include = "**"` rule. The other SIX name their files explicitly and
are the live risk surface, because a narrowing there is one edit away: `agent-cap`
(`tools/hooks/kit.toml`), `playbook-render` (`tools/playbook/kit.toml`), and `check-wiring`,
`kickoff-manifest`, `playbook` and `settings-merge` under `tools/govkit/entries/`. The entry id for
the first is `agent-cap`, not `hooks`, which is only its descriptor's directory.

So the arm lands GREEN and its value is forward-looking — a future narrowing of any of those six
would otherwise ship an unpinnable kit silently, and `check-wiring` is the AC4 fixture for that
reason.

This is stated plainly because it changes how the unit must be verified: a gate that has only ever
been seen pass is an assertion about nothing, so S3 is not optional here.

### Alternatives rejected

Asserting the file merely exists under the entry's `home` was rejected: a file can sit in a kit
directory and still be excluded from every `[[files]]` rule, which is exactly the state the arm
exists to catch.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one destination resolution per versioned entry, already computed by `selfcheck`.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an entry with no `version_from` file takes the declared-`none`
  path and is reported as exempt, never skipped silently.
- observability — the arm's pass prints nothing new; its failure names the entry and the file.
- risks — none live. The arm is green on today's tree by measurement, so it cannot block a landing.
- testing + left-shift gates — S3 is the failing case, and it is the reason this is Tier-2.
- migration / rollback — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs at `HEAD` after this unit, it exits 0
  and every versioned entry passes the new arm.
- **AC2** — When an entry's `version_from` file is excluded from its `[[files]]` rules on a fixture,
  `python tools/govkit/govkit.py selfcheck` exits non-zero and names that entry and that file.
- **AC3** — When an entry declares `version_from.none`, the new arm does not run for it, observed by
  confirming `python tools/govkit/govkit.py selfcheck` reports no arm result for those ten entries.
- **AC4** — The arm is observed RED before it lands: stage the S3 fixture into
  `tools/govkit/entries/check-wiring.kit.toml`, run `python tools/govkit/govkit.py selfcheck`, and
  confirm it exits non-zero where today it exits 0.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the `govkit selfcheck` leg. No new leg; this extends one.

## 8. Open questions

- **F1 — whether the arm should also cover the SENTINEL path** declared by the seven entries that
  use one. RESOLVED (agent, 2026-09-01, delegated): NOT in this unit, reversing rev-2's own
  recommendation. A sentinel answers "does this entry exist in the target", not "can its version be
  pinned", and the seven sentinel entries were never measured against a shipping test — so the arm
  would land with no observed failing case, which is the thing this unit exists to avoid. Filed as a
  follow-up rather than smuggled in on a shared resolution. `prior:` no prior ruling found.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded round-1 spec audit H4, which four lenses reported independently. The
  include split is nine glob to six explicit, not fourteen to one, and the six are now named because
  they are the risk surface the arm exists for. `hooks` corrected to the entry id `agent-cap`. The
  counts are re-derived, not copied: the audit reported ten-vs-five and that does not reproduce.

- rev-3 · 2026-09-01 · BUILT and CLOSED as an arm inside `selfcheck` check 5, resolved through
  `resolve_entry` — the resolver `apply` uses — rather than a second walk. F1 resolved the other
  way from rev-2's recommendation, with the reason.
  Acceptance ledger at `build/2026-09-01-build-DEPL-dGaugedVintage-1-acceptance-ledger.md`.
## 10. Reuse audit

- The seam is `resolve_dests` together with `resolve_rule_pool` in `tools/govkit/govkit.py`, the
  pair `apply` uses to turn `[[files]]` rules into destinations; check 5 currently resolves only
  `root / home / file` and never calls them. `python tools/codebase-map/reuse_lookup.py "assert every
  gov kit version marker site against its descriptor"` ranks `read_descriptors` first in the same
  file, which is the entry point this arm hangs off. No new seam.
- Recall terms used: `gov:kit marker population derive descriptor kit.toml check-kit-versions
  verdict-epoch remedy carriers bump sites`
