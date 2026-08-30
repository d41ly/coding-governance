# TOOL-aScouredKit-12 — two gate legs receive the path the descriptor already holds

**Status:** OPEN · rev-1 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling+deployer

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-6 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 |
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round2.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round2.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-6 TOOL-aScouredKit-11 TOOL-aScouredKit-13 TOOL-aScouredKit-15 |

<!-- /gen:spec-records -->

## 1. Goal

Pass the manifest path and the waiver-registry path into the two shipped gate legs whose engines
default them to a literal `tools/…`, so an adopter at any other prefix or memory root stops getting
a leg that exits non-zero forever with a remedy naming a path their tree does not have.

## 2. Scope (IN)

- S1. `tools/govkit/entries/kickoff-manifest.kit.toml` — the ratchet leg's argv gains
  `{manifest_path}`, the answer the descriptor already seeds the manifest to.
- S2. `tools/govkit/entries/check-agent-cap-restatement.kit.toml` — the restatement leg's argv gains
  `{prefix}/agent-cap-restatement-waivers.txt`, the destination its own `[[files]]` row declares.
- S3. Each edit carries, at the descriptor, the reason it exists — including which kit set the entry
  is in, because a default-set entry and a conditional one are different blast radii.

## 3. Non-goals (OUT)

- Making either ENGINE derive its own root. That is the durable fix and it is a wider change to two
  shipped scripts with their own arms; this unit takes the one the descriptor can already answer,
  and the durable form is named in §4 so it is not lost.
- `tools/check-testsuite-counts.sh` and `tools/check-install-prefix.sh`, which have the same shape
  and no argv the descriptor can fill. Both are already specced as `DEPL-dCarriedReceipt-15`.

## 4. Design

The class is one shape seen twice: the knob is parametric at the DESCRIPTOR layer, and the shipped
engine resolves the same thing from a literal. `manifest-check.sh` reads `MEMORY_ROOT` zero times
and resolves the manifest from a two-element list; `check-agent-cap-restatement.sh` defaults its
registry to `tools/agent-cap-restatement-waivers.txt` and swallows the miss with a `2>/dev/null`,
twenty lines from a `MEMORY_ROOT` read that is correct.

Both scripts already ACCEPT the path as `$1` and grade it correctly when given one — measured — so
the descriptor can close both today by passing what it already knows. The durable fix, kept here
because it is the one a later unit should take, is to have each engine derive its root the way
`tools/check-agent-cap-restatement.sh` does at its `MEMORY_ROOT` read and the way
`tools/run-gates/run-gates.sh` derives its own manifest from `$(dirname "$KITREL")`.

Severity is not symmetric between the two. `kickoff-manifest` is in the registry's DEFAULT selection
and its leg carries `guard = []`, so every adopter whose `manifest_path` answer is not gov's own gets
a permanently red bar; `check-agent-cap-restatement` is `selectable = "conditional"` and reaches
opt-in targets only.

## 5. Production-readiness checklist

- security — both added argv elements are descriptor-resolved tokens graded by the existing token
  resolver, not new target-supplied strings on a new path.
- perf / scale — N/A.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an unfilled `{manifest_path}` is already a declared hole and
  reports as one; passing it does not change that.
- observability — the legs stop printing a remedy naming a path that does not exist.
- risks — a target whose manifest genuinely sits at gov's default path now receives it explicitly
  rather than by coincidence, which is the same result by a checkable route.
- testing + left-shift gates — `python tools/govkit/selftest.py` and
  `python tools/govkit/govkit.py selfcheck`, which asserts every leg argv path against the shipped
  map.
- migration / rollback — an adopter re-running `apply` gets the corrected leg; nothing else moves.
- user docs — none needed; `WIRE-INTO-PROJECT.md` never documented the literal.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs, its `gate legs` note still reports
  `0 unshippable`, so both added argv paths resolve inside the shipped map.
- **AC2** — When the kickoff ratchet leg is read in
  `tools/govkit/entries/kickoff-manifest.kit.toml`, its argv carries `{manifest_path}`.
- **AC3** — When the restatement leg is read in
  `tools/govkit/entries/check-agent-cap-restatement.kit.toml`, its argv carries the
  `{prefix}`-rooted waiver registry.
- **AC4** — When `python tools/govkit/selftest.py` runs, it is green.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `kickoff-manifest ratchet` · `agent-cap restatement` · the
full bar at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.

## 10. Reuse audit

The seam is the descriptor token resolver, which already fills `{prefix}` and `{manifest_path}` in
every other argv in these same files — this unit adds two uses of an existing mechanism and writes
no code. `tools/run-gates/run-gates.sh` is the reference implementation named in §4 for the durable
form. The build's reuse probe is recorded in `TOOL-aScouredKit-1` §10 and is not re-composed.
