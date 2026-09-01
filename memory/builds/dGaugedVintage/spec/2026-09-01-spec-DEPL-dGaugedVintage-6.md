# DEPL-dGaugedVintage-6 — an install block whose second line cannot run

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-1 · base d65da7ab · streams deployer · order 7

*Tier-1 light profile per `memory/TEMPLATE-SPEC.md`: the status header binds, the ten-section canon
does not. The sections below are the ones that carry decisions.*

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-3 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/drift-audit/README.md`'s Install block copies the kit to the ROOT prefix and then invokes it
at the `tools/` prefix. The two lines contradict each other, the second cannot run against what the
first produced, and every later step in the file agrees with the second spelling.

## 2. Scope (IN)

- **S1** — Repair the copy line so its destination matches the invocation that follows it and the
  rest of the document.
- **S2** — Check the sibling kit READMEs for the same shape, since a copy-paste install block is
  exactly the thing that propagates. Report what is found; repair only what is broken.

## 3. Non-goals (OUT)

- Rewriting the install instructions into a govkit invocation. `WIRE-INTO-PROJECT.md` owns the
  deployer path and the kit README's `cp -r` route is deliberate for adopters not using govkit.
- The root-prefix waiver rows in `tools/install-prefix-waivers.txt` that name this README. They
  excuse deliberate dual-spelling probes and are unrelated to a wrong destination.
- Any change to `adopt-drift-audit.sh` itself.

## 6. Acceptance criteria

- **AC1** — When a reader follows `tools/drift-audit/README.md`'s Install block literally in a
  scratch repo, the command on the third line resolves and runs.
- **AC2** — When `bash tools/check-install-prefix.sh` runs after the repair, it exits 0 and the
  carried-ledger row for that README is unchanged or lower, never higher.
- **AC3** — S2's sweep result is recorded under `memory/builds/dGaugedVintage/build/`, naming each
  sibling README checked and whether it carried the same shape, so a clean sweep is distinguishable
  from no sweep.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the install-prefix leg and `drift-audit wiring`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
