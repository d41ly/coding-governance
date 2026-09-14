---
slug: cWidenedNet
node: c
opened: 2026-09-13
streams: tooling
roster: TOOL
ids: TOOL-cWidenedNet-1
authorized-by: prompt
---

# cWidenedNet — the install-prefix gate stops being blind to its own class

## The problem this build exists to solve

`tools/check-install-prefix.sh` grades two prefixes over two populations, and both arms bound an
extension class of `sh|py|js|md|json|toml`. Every kit here keeps its declaration sidecars as `.txt`
or `.tsv` and ships a `.conf.example`, so a literal naming one was invisible to the gate that exists
to forbid it — including the two in the gate's own body that resolve its waiver registry and its ban
list. Measured at `c4f02308`: one live root spelling, 31 carried occurrences over nine files.

The second blindness is a population. Arm 1 excluded tests, selftests and example confs because they
build root-prefix installs on purpose; arm 2 covers the received set but grades only the shipping
spelling. That also excused their usage headers, and six shipped files name a path an adopter's tree
does not have.

`TOOL-aScouredKit-20` filed both and is OPEN. Its loose-file half landed as epoch 2.

## Expected improvements

- A literal naming a `.txt`, `.tsv`, `.conf` or `.conf.example` path is gradeable, in both arms.
- The gate resolves its own two sidecars rather than spelling them, so it stops breaking the rule it
  enforces and stops misreporting at any prefix but `tools/`.
- A root spelling in a received test or example conf is graded, with a principled per-line
  exemption rather than a blanket file exclusion.
- Six broken usage headers in shipped files are fixed rather than recorded.

## Detriments if this is not built

- The gate keeps certifying coverage it does not have, which is worse than a gap nobody claimed.
- Every new `.txt` sidecar reference lands green and the ban list never sees it.
- An adopter at any prefix but `tools/` keeps receiving selftest headers that name nothing, and the
  gate that would have caught them is the one carrying the same defect.

## Build-level rules

- **The 31 newly-visible carried literals are REBASELINED, not fixed.** A definitional widening is
  what `--rebaseline` and the predicate epoch exist for. Fixing them is a separate unit against
  `DEPL-dCarriedReceipt-15`, which already owns that class.
- **The new root-spelling class keys on an inline marker, never on `<path>:<line>`.** This corpus
  recorded the reason itself: positional keying unpinned `install-prefix-waivers.txt` on an edit
  ABOVE a waived line and redded a merge that touched nothing the waiver guarded
  (`TOOL-aSealedCaravan-1`). The marker moves with its line.
- **A deliberate root spelling is justified BY HAND, in the marker's reason column.** Same rule the
  carried ban already applies, for the same reason: a row a script wrote is an accident nobody
  reviewed.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-cWidenedNet-1` | 2 | the extension class widens, the gate derives its own sidecars, and the root spelling is graded over the received set |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node c · opened 2026-09-13 · streams tooling
ids TOOL-cWidenedNet-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-cWidenedNet-1 — the extension class widens, the gate derives its own sidecars, and the root spelling is graded over the received set](spec/2026-09-13-spec-TOOL-cWidenedNet-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-13 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-cWidenedNet-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-cWidenedNet-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
