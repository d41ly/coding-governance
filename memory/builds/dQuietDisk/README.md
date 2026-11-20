---
slug: dQuietDisk
node: d
opened: 2026-11-20
streams: tooling
roster: TOOL
authorized-by: prompt
status: OPEN
ids: TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19
---

# dQuietDisk — gov's bars and suites stop churning the disk

## The problem this build exists to solve

C: on node d sits at 100% active time on NTFS metadata updates and process creation from gov's own
gates. The history legs re-grade all of history on every commit, one git process per question. Kit
suites rebuild a repository per case, and six suites each copy the whole tree. Adopters re-run gov's
kit self-tests on every bar. `govkit update` and `apply` redo work they already hold. The measured
analysis and the owner's prompt are recorded under `prompts/` and `build/`.

## Expected improvements

- History legs grade only what is new since their last graded tip.
- Suites build each base repository once and clone it per case.
- Adopters skip kit self-tests a gov attestation already covers.
- `govkit update` and `apply` stop repeating git reads, checks and whole bars.

## Detriments if this is not built

- Every bar on every node keeps paying tens of thousands of git processes.
- Interactive work on node d keeps stalling behind the same disk queue.
- Adopter bars keep re-proving kit bytes that did not change.

## Build-level rules

- Classification (M2): 19 units, MISSING at open, specced by the spec-writer role.
- Chain map (v2 `[chain]`): units 1 to 15 and 19 sit in dWitnessedBar's area (Test: gate health, held
  legs, budgets); 16 to 18 in dSafePassage's (Supersession: govkit update and apply); 2 to 6 also in
  dScopedBuild's (Build: the history-derived exit base). This build runs on its own track; a shared
  subject is reconciled at the merge, and no spec here contradicts theirs.
- Units writing a file dWitnessedBar's branch changes are built on its landed tip; the run holds
  until then.
- No spec audit: the prompt asks for none, and a run may not opt itself in.
- The unattended kit's own suites are never run (owner rule, 2026-08-23); a criterion they would
  observe is checked by a hermetic probe or an equivalence corpus, or handed over as one command.
- Kit changes reach adopters only through minted versions and `govkit update`.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dQuietDisk-1` | one store of immutable history verdicts, keyed by the commit and blob ids each read, with a `cat-file --batch` reader |
| 2 | `TOOL-dQuietDisk-2` | `check-pass-order.sh` grades only units new since its last graded tip |
| 3 | `TOOL-dQuietDisk-3` | `check-brief-recorded.sh` grades only units new since its last graded tip |
| 4 | `TOOL-dQuietDisk-4` | `routed_commits.py` grades only commits past its last graded tip |
| 5 | `TOOL-dQuietDisk-5` | the runner reads one `git diff --name-only BASE` for every guarded leg |
| 6 | `TOOL-dQuietDisk-6` | `manifest-check.sh`'s pickaxe scoped by path and range |
| 7 | `TOOL-dQuietDisk-7` | one suite template cache, keyed by kit tree hash, cloned per case |
| 8 | `TOOL-dQuietDisk-8` | one sparse no-checkout tree snapshot per bar, shared by six readers |
| 9 | `TOOL-dQuietDisk-9` | every scratch path under one owned, swept root, removed by chmod-and-retry |
| 10 | `TOOL-dQuietDisk-10` | `check-wiring.test.sh` on the template cache |
| 11 | `TOOL-dQuietDisk-11` | `govkit/selftest.py` on the template cache |
| 12 | `TOOL-dQuietDisk-12` | `.githooks/pre-push.test.sh` on the template cache |
| 13 | `TOOL-dQuietDisk-13` | the `run-gates*.test.sh` suites on the template cache |
| 14 | `TOOL-dQuietDisk-14` | the kit attestation: kit tree hash and its green self-tests, recorded by gov and shipped with the kit |
| 15 | `TOOL-dQuietDisk-15` | a kit self-test leg whose vendored tree hash is attested is held, and runs when unattested |
| 16 | `TOOL-dQuietDisk-16` | `govkit update` reads every receipt row through one batch handle |
| 17 | `TOOL-dQuietDisk-17` | `govkit update` runs each `adopt-*.sh --check` once |
| 18 | `TOOL-dQuietDisk-18` | `govkit apply` takes its baseline from the reuse cache and re-runs only the legs its writes reach |
| 19 | `TOOL-dQuietDisk-19` | the before and after measurements, with their instruments |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-11-20 · streams tooling
ids TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16
ids TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 3 bound to this build, across 2 record folder(s).

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
