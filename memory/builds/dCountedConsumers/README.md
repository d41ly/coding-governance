---
slug: dCountedConsumers
node: d
opened: 2026-11-02
streams: tooling
roster: TOOL
ids: TOOL-dCountedConsumers-1 TOOL-dCountedConsumers-2
---

# dCountedConsumers — help/policy.md names the policy keys that have consumers today

## The problem this build exists to solve

`help/policy.md` says that two families of keys have consumers so far, the agent limit and the size
caps, and that a value set for any other key changes no behaviour. That was already wrong for
`help.enforce`, which the docs leg reads. Since dFoldedAudit landed it is also wrong for the three
`review.spec-audit` keys, which the unattended driver reads. A reader trusting the page would think
those keys are inert. dFoldedAudit's unit 18 named the sentence as a follow-up (F1).

## Expected improvements

- The policy page names every key family a reader consumes today.
- Each named family links the page that documents it.

## Detriments if this is not built

- An owner reads that setting `review.spec-audit.disposal` changes nothing, and it does.
- The page keeps contradicting `help/spec-audit.md` and `help/docs-leg.md`.

## Build-level rules

- One Tier-1 unit, attended, with no spec audit (owner, 2026-11-02).
- BUILD-METHOD M6's dispatch sentence is out of scope: TOOL-dIndexedDesign-36 owns it (owner, 2026-11-02).
- HYGIENE's deviation paragraph stays as is (owner, 2026-11-02).

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dCountedConsumers-1` | help/policy.md's consumer paragraph names every consumed key family, with a link for each |
| 2 | `TOOL-dCountedConsumers-2` | the trace signal counts a help page as product, so a unit whose product is a help page has its commit |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node d · opened 2026-11-02 · streams tooling
ids TOOL-dCountedConsumers-1 TOOL-dCountedConsumers-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dCountedConsumers-1 — help/policy.md names every policy key family a reader consumes today](spec/2026-11-02-spec-TOOL-dCountedConsumers-1.md) | 10 | 1 | CLOSED | rev-1 | 2026-11-02 |
| [TOOL-dCountedConsumers-2 — the trace signal counts a commit that writes a help page as product](spec/2026-11-02-spec-TOOL-dCountedConsumers-2.md) | 20 | 1 | CLOSED | rev-1 | 2026-11-02 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dCountedConsumers-1 TOOL-dCountedConsumers-2.

Ids whose spec moved past its audited revision: none — 0 of 2 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 10 | `TOOL-dCountedConsumers-1` | no |
| 20 | `TOOL-dCountedConsumers-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
