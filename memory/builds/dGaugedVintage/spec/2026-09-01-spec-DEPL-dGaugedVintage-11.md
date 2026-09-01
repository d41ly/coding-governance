# DEPL-dGaugedVintage-11 — the relocate rung goes quiet exactly where a kit fans out

**Status:** OPEN · rev-2 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 |

<!-- /gen:spec-records -->

## 1. Goal

`derive_carry_map` lifts one directory pair per row and DROPS any gov directory that fans into more
than one target directory. Every kit that ships a rendered Skill beside its engine files fans out by
construction, so the `relocate` rung is silent for those kits on a real adopter.

## 2. Scope (IN)

- **S1** — A needle map that admits a one-to-many gov directory instead of dropping it, keyed so a
  row resolves against the destination its OWN receipt pair produced rather than a single winner.
  This is the unit.
- **S2** — The one reporting gap that is genuinely absent: an explicit ZERO-COUNT line when `dropped`
  is empty. The non-empty case is already reported — see §4 — so S2 is narrow by measurement.
- **S3** — A fixture reproducing the fan-out: one kit whose engine files land under the prefix and
  whose rendered artifact lands under a skills path, asserting the rung fires for both.

## 3. Non-goals (OUT)

- Changing what the `relocate` rung MEANS or when it applies. `DEPL-dCarriedReceipt-9` ratified the
  rung and its re-proof-each-run discipline. **S1 does reopen that unit's §8 F1**, which chose the
  single-winner map; this spec names that explicitly rather than implying the ratification is
  untouched.
- The other two rungs, `verbatim` and `eol`. They key differently and are unaffected.
- Making the map authored rather than derived. Derivation is what `DEPL-dCarriedReceipt-9` bought.
- Re-resolving descriptors inside `derive_carry_map`. Its docstring forbids it — see F1.
- Fixing any adopter's receipt. This changes derivation; a re-run recomputes.

## 4. Design

### Data model

`derive_carry_map` spans `tools/govkit/govkit.py:4779-4842`. It lifts one `dirname` pair per row at
`:4826-4834`, accumulating gov-dir to target-dir. At `:4835` it computes
`dropped = [(gd, sorted(ds)) for gd, ds in sorted(lifted.items()) if len(ds) > 1]`, and the sibling
comprehension at `:4836-4837` builds `pairs_out` from the `len(ds) == 1` keys only — so the fan-out
keys are discarded TWICE, and `pairs_out` is a second consumer S1 must change.

The lift is the problem, not the drop: a single pair per gov directory cannot express a fan-out, so
the drop is the only correct thing to do with the shape it produces. S1 changes the shape.

### The reporting that already exists

Rev-1 scoped a report that ships. `tools/govkit/govkit.py:5349-5353` prints the dropped directory by
name with its destinations in `update`, and `:6431-6434` does the same in `adopt`. That was resolved
by `DEPL-dCarriedReceipt-9` §8 F1. What does NOT exist is the zero-count line, which is S2.

### Inventory

Kits fanning out on the measured adopter each ship a rendered `SKILL.md` or a `memory/guides`
document to a different tree than their engine files. That count is the ADOPTER's, taken from a
read-only run by a review lens, and it is NOT re-derived here — treat it as attributed rather than
measured by this spec.

### Alternatives rejected

Keeping the drop and documenting it — a rung nobody can see fire is indistinguishable from a rung
that does not work.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the map is already built per run; admitting more keys does not change its order.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — S2 is exactly this line.
- observability — the non-empty report already exists; S2 completes it at zero.
- risks — admitting fan-out could resolve a row against the wrong destination if the key is chosen
  loosely. F1 states the key, and it is NOT a descriptor re-resolution.
- testing + left-shift gates — S3, plus the existing `govkit acceptance matrix` arms for the rung.
- migration / rollback — none. The map is recomputed each run and never stored as a claim.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When a kit's rows land in two directories, `python tools/govkit/govkit.py update`
  reports the `relocate` rung for rows in BOTH, observed on the S3 fixture.
- **AC2** — The existing non-empty dropped report survives S1: `python tools/govkit/govkit.py update`
  still names each dropped directory in the cases that dropped before, observed as a regression check
  against `:5349-5353`.
- **AC3** — When no gov directory fans out, `python tools/govkit/govkit.py update` prints a dropped
  count of zero rather than omitting the line, observed on a single-destination fixture. This is the
  arm that is RED at base.
- **AC4** — A row resolves against the destination its own receipt pair carries: assert over the
  `(source, path)` pairs the caller FEEDS `derive_carry_map`, never over a re-resolution.
- **AC5** — The `relocate` behaviour `DEPL-dCarriedReceipt-9` established is unchanged for
  non-fanning kits: run `bash tools/run-gates/run-gates.sh` and confirm `govkit acceptance matrix`
  stays green.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck` and `govkit acceptance matrix`.

## 8. Open questions

- **F1 — the key S1 uses.** NOT the `[[files]]` rule index via `resolve_dests`, which rev-1
  recommended: `derive_carry_map`'s docstring at `tools/govkit/govkit.py:4791-4797` forbids
  re-resolving descriptors inside it, as a decision rather than an oversight — the map must describe
  the target as INSTALLED, not as the descriptors read today. Recommendation: key off the receipt's
  own `(source, path)` pair, the sequence `derive_carry_map` already receives.
  `prior:` `DEPL-dCarriedReceipt-9` §8 F1 chose the single-winner map that S1 reopens. Unresolved.
- **F2 — whether S2 ships as its own commit.** It is small and independently valuable.
  Recommendation: yes, two commits within this unit rather than two units. `prior:` no prior ruling
  found. Unresolved.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded round-1 spec audit H2, H3, M1. S2 narrowed to the zero-count line: the
  non-empty dropped report already ships at `:5349-5353` and `:6431-6434`, so rev-1's AC2 was green
  at base and is now a regression check. F1 reversed — it recommended keying off `resolve_dests`,
  which `derive_carry_map`'s own docstring forbids. Every §4 line citation corrected: the function is
  `:4779-4842`, the lift `:4826-4834`, the drop `:4835`, and `pairs_out` at `:4836-4837` is a second
  consumer rev-1 missed. §3 now names the `DEPL-dCarriedReceipt-9` §8 F1 ratification S1 reopens.

## 10. Reuse audit

- The seam is `derive_carry_map` itself at `tools/govkit/govkit.py:4779-4842`, with
  `derive_carry_rung` and `derive_carried_by_rung` beside it; `python
  tools/codebase-map/reuse_lookup.py "derive attribution for a receipt row against gov history"`
  ranks that whole `derive_*` family in one file at fan-in 1. This unit modifies an existing private
  seam rather than adding one, and its docstring at `:4791-4797` is a constraint on HOW.
- Recall terms used: `check-install-prefix carried ratchet grep count literal carry map relocate
  needle rung prefix adopter`
