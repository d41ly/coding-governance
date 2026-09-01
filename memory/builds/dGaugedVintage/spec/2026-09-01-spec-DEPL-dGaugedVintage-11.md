# DEPL-dGaugedVintage-11 — the relocate rung goes quiet exactly where a kit fans out

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`derive_carry_map` lifts one directory pair per row and then DROPS any gov directory that fans into
more than one target directory. Every kit that ships a rendered Skill beside its engine files fans
out by construction, so the `relocate` rung is silent for seven kits on a real adopter.

## 2. Scope (IN)

- **S1** — A needle map that admits a one-to-many gov directory instead of dropping it, keyed so a
  row resolves against the destination its OWN rule produced rather than against a single winner.
- **S2** — The dropped set is REPORTED whenever it is non-empty, naming each gov directory and its
  destinations, so a silent rung becomes a visible one even before S1 lands.
- **S3** — A fixture reproducing the fan-out: one kit whose engine files land under the prefix and
  whose rendered artifact lands under a skills path, asserting the rung fires for both.

## 3. Non-goals (OUT)

- Changing what the `relocate` rung MEANS or when it applies. `DEPL-dCarriedReceipt-9` ratified the
  rung and its re-proof-each-run discipline, and this unit does not reopen either.
- The other two rungs, `verbatim` and `eol`. They key differently and are unaffected.
- Making the map authored rather than derived. Derivation is the property `DEPL-dCarriedReceipt-9`
  bought and it stays.
- Fixing any adopter's receipt. This changes derivation; a re-run recomputes.

## 4. Design

### Data model

`derive_carry_map` at `tools/govkit/govkit.py:4779-4844` lifts one `dirname` pair per row at
`:4833-4839`, accumulating gov-dir to target-dir. At `:4840` it computes
`dropped = [(gd, sorted(ds)) for gd, ds in sorted(lifted.items()) if len(ds) > 1]` — every gov
directory with more than one destination is discarded rather than represented.

The lift is the problem, not the drop: a single pair per gov directory cannot express a fan-out, so
the drop is the only correct thing to do with the shape it produces. S1 changes the shape.

### Inventory

Seven kits fan out on the measured adopter — each ships a rendered `SKILL.md` or a `memory/guides`
document to a different tree than its engine files. That count is the ADOPTER's, measured on a
read-only run, and it is not a claim about this repo's own layout.

### Rollout

S2 is landable alone and is worth landing alone: it converts a silent gap into a reported one, which
is the property this repo asks of every signal. S1 follows.

### Alternatives rejected

Keeping the drop and documenting it was rejected — a rung nobody can see fire is indistinguishable
from a rung that does not work, which is the liveness rule this repo states about every signal.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the map is already built per run; admitting more keys does not change its order.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an empty dropped set must print as zero, not as nothing, or S2
  reports the same way whether it worked or was never reached.
- observability — S2 IS the observability half, and it lands first for that reason.
- risks — admitting fan-out could make a row resolve against the wrong destination if the key is
  chosen loosely. S1 keys on the rule that produced the destination, which is why the key is stated
  in scope rather than left to the implementation.
- testing + left-shift gates — S3, plus the existing `govkit acceptance matrix` arms for the rung.
- migration / rollback — none. The map is recomputed each run and never stored as a claim.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When a kit's rows land in two directories, `python tools/govkit/govkit.py update`
  reports the `relocate` rung for rows in BOTH, observed on the S3 fixture.
- **AC2** — Before S1, when the dropped set is non-empty, the run names each dropped gov directory
  and its destinations, observed by running `python tools/govkit/govkit.py update` read-only against
  a fan-out fixture.
- **AC3** — When no gov directory fans out, `python tools/govkit/govkit.py update` reports a dropped
  count of zero rather than omitting the line, observed on a single-destination fixture.
- **AC4** — A row whose destination came from one rule is never matched against another rule's
  destination, observed by asserting the pair `resolve_dests` returns on the S3 fixture.
- **AC5** — The `relocate` behaviour that `DEPL-dCarriedReceipt-9` established is unchanged for
  non-fanning kits: run `bash tools/run-gates/run-gates.sh` and confirm the `govkit acceptance
  matrix` leg stays green.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck` and `govkit acceptance matrix`.

## 8. Open questions

- **F1 — the key S1 uses.** Options: the `[[files]]` rule index that produced the destination, or the
  full source path's directory rather than the kit-root pair. Recommendation: the rule index, since
  `resolve_dests` already knows it and it cannot collide. Unresolved.
- **F2 — whether S2 ships as its own landing.** It is small, independently valuable, and makes S1's
  fixture easier to trust because the report shows the drop before and after. Recommendation: yes,
  two commits within this unit rather than two units. Unresolved.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.

## 10. Reuse audit

- The seam is `derive_carry_map` itself at `tools/govkit/govkit.py:4779`, with `derive_carry_rung`
  and `derive_carried_by_rung` beside it; `python tools/codebase-map/reuse_lookup.py "derive
  attribution for a receipt row against gov history"` ranks that whole `derive_*` family in one file
  at fan-in 1, so this unit modifies an existing private seam rather than adding one.
- Recall terms used: `check-install-prefix carried ratchet grep count literal carry map relocate
  needle rung prefix adopter`
