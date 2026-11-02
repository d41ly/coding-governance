---
slug: dCountedConsumers
node: d
opened: 2026-11-02
streams: tooling
roster: TOOL
status: OPEN
ids: TOOL-dCountedConsumers-1
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

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-11-02 · streams tooling
ids TOOL-dCountedConsumers-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
