# TOOL-dQuietDisk-9 deviation 1 — the two waived rows carry their reason in a widen record, and the new leg is claimed by the gate-lint dossier

**Serves:** deviation TOOL-dQuietDisk-9

- **Departs from:** `TOOL-dQuietDisk-9@rev-6` [Files touched]
- **Hand-off:** spec-to-code
- **Before:** the spec's Files touched, an estimate, names `memory/project/cleanup-sites.txt` holding the two frozen step programs' sites "as waived rows with that reason", the leg's `[[exempt_leg]]` row and the rendered `tools/gate-legs.json`. It names no widen record and no dossier under `memory/map/` to claim the new leg.
- **After:** the pass ran `python tools/memory-tree/ratchet.py widen cleanup-sites` once, with both keys and one reason, which wrote `2026-11-22-build-TOOL-dQuietDisk-9-widen-14` and the two rows at HEAD's sha with `widened:2026-11-22-build-TOOL-dQuietDisk-9-widen-14`, count 1 each. It also appended `"cleanup posture (a tree removal that swallows its error)"` to the `gate-legs` claim of `memory/map/features/gate-lint.md`, beside the three `encoding posture` legs the same scanner runs, and regenerated the map. No other row or claim changed.
- **Cause:** builder discovery
- **Reason:** the ledger grammar `path TAB arm TAB count TAB sha TAB disposition` has no reason field: `tools/gate-lint/legacy_ledger.py#DISPOSITION_RE` admits only `seeded`, `carried:`, `deferred:`, `keep:` and `widened:`. A row's reason is its widen record's, which `ratchet (never gains)` grades as tracked, naming the key and holding a Reason. The first pass's patch also had the scanner's self-test write a `waived: ...` disposition, which `resolve_declaration` reads as malformed. That row now reads `widened:`, so the arm grades what it names. The map: `gen_map.py --write` printed the new leg as `UNCLAIMED`, and every gate leg is claimed by one dossier (PINNED, this pass's `memory/map/generated/MAP.md` before the claim).
- **Evidence:** `resolve_declaration("memory/project/cleanup-sites.txt", CLEANUP_ARMS)` returned both keys at count 1 with no malformed row, and the same call over a `waived:` row returned one malformed line. After the claim, `memory/map/generated/MAP.md` lists the leg against `gate-lint` and holds no `UNCLAIMED` row (PINNED, both run in this pass).
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value
- **Follow-through:** report
- **Caused-by:** TOOL-dQuietDisk-9
