# The acceptance ledger for the promoted unit

**Serves:** journal TOOL-aBoundedVerdict-22

Main's acceptance-ledger check landed in the merge with a cutoff of `2026-08-20`, and this branch had
exactly one post-cutoff closure. The grandfather list the merge imported names only main's own units,
because main had no way to know this branch had one — so the honest answer is to evidence the unit
rather than add it to a list of exemptions. An exemption is not coverage.

Every line is OBSERVED. Where a criterion was met by a measurement rather than a command, the line
names the measurement.

**Evidences:** TOOL-aBoundedVerdict-22
- AC1 — `bash tools/memory-tree/check-verdict-epoch.sh` — exit 0 once the 2.28 bump and the engine change shared a commit; it compares COMMITS, so an uncommitted bump reads as older than the change it dates.
- AC2 — `bash tools/memory-tree/check-memory-hygiene.sh` — exit 0 on the merged tree.
- AC3 — `is_published` — reproduced against this clone's live advertisement: three tips, one present and two absent. The presence-tracking form returned a definite "not published" from a third of the evidence; the absence-tracking form returns cannot-tell. Armed with a ghost commit built inside the bare origin, which the clone cannot have.
- AC4 — `plan_state` sliced from the shipped driver — `None of the forks below are resolved.` above an unmarked fork reads FORKED, `none - ...` above a marked fork reads READY, a bare `none.` reads READY, and a prose-only §8 reads FORKED. Measured over the corpus before landing: 12 older terminal specs would newly red and all 12 are already exempt by `FORK_MARK_CUTOFF`; zero at or after it.
- AC5 — `bash tools/memory-tree/marker-contract.test.sh` — PASS at 44 cases across 3 contracts, up from 38, the three added rows being denial, mixed-case none, and upper-case N/A.
- AC6 — PARTIAL, and stated rather than implied. The five suites pass on the integrated tree: driver 622, hygiene 251, shard one 205, shard two 430, marker-contract 44. `GATE_FULL=1` has NOT been run green on this tree — the integration review found four legs red and they are being folded now. This line is the one criterion of the six not yet fully met, and the unit stays open against it until the bar is green.
