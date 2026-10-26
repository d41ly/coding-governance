# dIndexedDesign — asks

## Asks

- TOOL-dIndexedDesign-17 · filed 2026-10-21 · build every roster unit of this build from its spec, filed by the opening so the spec run closes by carry-forward with each unit's spec header advancing this ask (README rule 1) · accept every unit of the README's `roster:units` pair is built from its spec and CLOSED, the last one's header carrying `closes` for this ask
- TOOL-dIndexedDesign-18 · filed 2026-10-23 · THE CARRIES INSTRUMENT READS NO AMENDMENT. `carries.py` (the bootstrap instrument, in service until this build's `design.coverage` lands) hashes each clause from v2 alone, while the product join in `tools/check-spec-tokens.py` reads the as-built view, where a deviation record's `amends` row replaces the clause's text. dFairHearing's deviations 11 and 171 amend `cl-dClosedLoop-0068` and `cl-dClosedLoop-0084`, so `TOOL-dFairHearing-1` and `TOOL-dFairHearing-17` pin the amended hashes `d09495d0` and `b793fdd5`: the product join is green, and `carries.py --build dFairHearing --exit` reports both as stale pins (the execution plan's [phase-1], line 837: an instrument-product disagreement is filed here) · accept this build's `design.coverage` reads a clause's text through the as-built view, so a spec pinned to its amended hash is carried, seen red on a planted pin to the baseline hash of an amended clause
- TOOL-dIndexedDesign-19 · filed 2026-10-26 · THE `repeat` ROUTE READS A PLAYBOOK BY PATH. dKeptSession carries cl-dClosedLoop-0156: a `repeat` request routes onto a playbook named by a repo-relative path, which TOOL-dPlacedRequest-4 resolves and the driver's recipe mode follows, until this build lands `record-kind.playbook` (KICK-dKeptSession-18 §8 F2) · accept TOOL-dPlacedRequest-4's `repeat` check resolves a `record-kind.playbook` record in the landing that adds the kind, its path stand-in pruned there, seen red on a planted `repeat` naming a path no playbook record holds

## Dispositions

- SEV · TOOL-dIndexedDesign-17 · MED · the build's units stay unbuilt and its owned gaps open
- SEV · TOOL-dIndexedDesign-18 · LOW · a chain spec that follows its own amendment reads as a stale pin to the in-service instrument, so a Design exit gated on carries.py cannot pass for it
- SEV · TOOL-dIndexedDesign-19 · LOW · a `repeat` keeps routing by a path no record kind validates
