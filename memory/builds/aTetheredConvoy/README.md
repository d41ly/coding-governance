---
slug: aTetheredConvoy
node: a
opened: 2026-08-16
streams: deployer+tooling
roster: DEPL
ids: DEPL-aTetheredConvoy-1
---

# aTetheredConvoy — the update verb, and the ratchet that keeps the kit converged

Node `a` · opened 2026-08-16 · streams deployer and tooling.

`govkit` lands an install and has no way to move one forward. Every repo that adopted it is an
upgrade orphan the moment gov commits again — which is the same sentence the deployer research
opened with about the era before govkit, one layer up. The `update` verb closes it.

Underneath that sits a second problem the owner named in the same breath, and it is the one that
decides whether `update` stays true: nothing forces a NEW moving part in this repo to ship
govkit-ready. The surface predicate forces a new `tools/` directory to be CLAIMED by a declaration.
It does not force that declaration to be complete, to name the kit's gate legs, to claim the kit's
version constant, to cover a file added inside the kit, or to actually deploy anything at all.

## Start here

**State.** Unit 1 is OPEN at rev-1 and has not been reviewed. Tier-2 by the manifest's tier rule —
it changes a kit's contract and is a cross-kit change.

**Read the grounding first, because it is measured rather than argued.** Every finding in §4 was
reproduced against the real tree at base `0f0a121d`, several by driving `govkit` end to end into a
throwaway repo. Three are blocker-class and two of them make the `update` verb unbuildable as the
code stands:

- `plan` does not promise the file set `apply` produces. Measured: `plan` promised eleven writes
  including the playbook's own destination; `apply` landed fifty-six files and six of the seven
  destinations `plan` named as `write` were never written and appear in no receipt. The two verbs
  count different things — `plan` counts RULES, `apply` counts FILES — and `plan` marks a role
  `apply` cannot land as `write`.
- The `playbook` entry, which is in the DEFAULT set, lands zero bytes. Both its file rules are
  `role = "project-owned"`, which the spec's own role table defines as "gov never supplies the
  bytes". Gov does supply them. The hole that grades its placeholders then probes a file nothing
  wrote.
- The receipt is not a stable inventory. Two identical applies with no gov change between them:
  fifty-seven rows, then fifty-six. `seed` rows are skipped when the destination exists and the
  receipt is rebuilt from the write log alone, so they fall out of the record. `update` and a later
  `remove` both need the receipt to be the complete statement of what gov put there.

**The convergence finding is the largest, and it is this unit's own defect class turned inward.**
The descriptors' `[[gate_leg]]` blocks and `tools/gate-legs.json` are two spellings of one fact with
nothing asserting they agree — which is the sentence the deployer spec uses to explain why govkit
exists. Measured at base: leg names declared in descriptors that exist in no manifest leg, and
manifest legs claimed by no descriptor including ones a target plainly must receive. The deployer
spec's own AC10 specified one direction of that cross-check. Neither direction was built.

**The mechanism the owner asked for is not more declarations.** Four of the five arms in §4 assert a
correspondence between populations that ALREADY exist, so they add no new thing to keep in sync. The
fifth executes the deployer against a fixture for every entry, because a descriptor that parses and
deploys nothing is indistinguishable from one that works — which is the sentence `govkit.py`'s own
module docstring opens with, and it is now true of `govkit` itself.

**Nothing here repairs the unbuilt halves of the deployer.** The gate-runner emitter, the
`.gitattributes` writer and the `merged` role stay unbuilt and stay REPORTED on every run. This unit
makes the parts that exist tell the truth and adds the verb the owner named; widening it to finish
the deployer would bury both.

The table below is GENERATED
from the status header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** OPEN · 1 unit(s) · node a · opened 2026-08-16 · streams deployer+tooling · ids DEPL-aTetheredConvoy-1

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [DEPL-aTetheredConvoy-1 — the update verb, and the ratchet that keeps the kit converged](spec/2026-08-16-spec-DEPL-aTetheredConvoy-1.md) | OPEN | rev-1 | 2026-08-16 |

Records live under `spec/`.
<!-- /gen:build-index -->
