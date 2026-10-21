# TOOL-dTrueNorth-2 deviation 3 — the product join takes the instrument's plant suite as its acceptance

**Serves:** deviation TOOL-dTrueNorth-2

- **Departs from:** `cl-dClosedLoop-0002@6acd9ea9` [acceptance]
- **Hand-off:** design-to-spec
- **Before:** the carries join, a further join of the spec tokens leg behind that cutoff as the handoff join is: a ghost id, an unbound spec, a stale pin, two specs carrying one clause whole, or pinning it to two hashes, and a revision that stops carrying a clause with no decision each red, a token of a clause missing from its carriers red, and a run that measured no spec never green, each seen on its planted case over a fixture spec set (the owner's FQ-2, P41)
- **After:** the carries join, a further join of the spec tokens leg behind that cutoff as the handoff join is: a ghost id, an unbound spec, a stale pin, two specs carrying one clause whole, or pinning it to two hashes, and a revision that stops carrying a clause with no decision each red, a token of a clause missing from its carriers red, and a run that measured no spec never green, each seen on its planted case over a fixture spec set (the owner's FQ-2, P41)
- **Cause:** review finding
- **Reason:** The product join takes the bootstrap instrument `carries.py`'s thirteen plants as its acceptance (D3), each with the verdict the instrument gives it, which is stricter than the clause's red cases: a `crossbuild` plant, a `moved` green control and a `moved-token` plant are among them, and the clause names none of the three. The clause's text stands, so the view cites this record on the clause's row and the clause's hash stays `6acd9ea9`, the pin both the instrument and the product join read.
- **Evidence:** the execution plan's `[deviations]`, "Carried, not asked, for the owner's walk" (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:1289-1294`); the instrument's plants (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py`, `PLANTS`); TOOL-dTrueNorth-2 §1 and §8 F3
- **Risk:** stricter
- **Approver:** spec writer, the gov-spec-writer role of dTrueNorth's whole run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); carried for the owner's walk unless it rules otherwise
- **Follow-through:** amends cl-dClosedLoop-0002@6acd9ea9
- **Caused-by:** PLAY-dClosedLoop-1
