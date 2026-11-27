# TOOL-dTotalRecall-119 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-119
**Caused-by:** TOOL-dTotalRecall-119

No merge bar, no self-test suite and no gate leg in this pass. The builder built spec rev-1 over base
`8c4aa9c784dbacd43938cb63d68a4fa5c6f184f3`, 2026-11-25 local, in one commit. The plant ran over the working tree's
`record_causes.py`. §7's legs and the `New arm:` RED-first observation of
`tools/memory-tree/check-memory-hygiene.test.sh`'s `claim-root` arm are owed to the close.

With today's reader put back in a probe over the same minted claim, the walk answered the empty set, one orphan and
RED; with the new one, no orphan and green (DERIVED 2026-11-25, the probe). A claim CLI with no usable bash made the
plant refuse at exit 2, its line carrying the CLI's (DERIVED 2026-11-25, the same probe).

**Evidences:** TOOL-dTotalRecall-119
- AC1 — `record_causes.read_claim_slugs` — answered `{'fClaim'}` over the minted claim, the same after the CLI's `ask` verb minted an id there, and the same with a local `refs/gov/claims/fOther` planted (DERIVED 2026-11-25, the probe).
- AC2 — `python record_causes.py --fixture --plant claim-root` — printed the line naming `refs/gov/remote/claims/fClaim`, `0 causeless · 0 orphan(s)` and `green`, exit 0, and the `update-ref` grep over the module listed no line (DERIVED 2026-11-25, that run and the grep).
- AC3 — `grep -n 'refs/gov/claims' tools/memory-tree/record_causes.py` — printed one line, the module docstring's prose naming the remote's ref (DERIVED 2026-11-25).
- AC4 — `python tools/memory-tree/gotchas.py --check` — named no finding of the new file, its advisory alone printed (DERIVED 2026-11-25); the relations half reads the commit, so the builder runs it after the commit and returns it.
- AC5 — `grep -n 'plant claim-root' tools/memory-tree/check-memory-hygiene.test.sh` — printed the arm, the line below it asserting the cache ref's line; `FLOOR_ASSERTIONS` went from 836 to 837 and the `shell-role` row from 3750 to 3751, the measured count, widened by `2026-11-25-build-TOOL-dTotalRecall-119-widen-30` (DERIVED 2026-11-25). The floor is counted by reading; the suite's own run is owed to the close.
