---
slug: dQuietDisk
node: d
opened: 2026-11-20
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-20 TOOL-dQuietDisk-21 TOOL-dQuietDisk-22 TOOL-dQuietDisk-23 TOOL-dQuietDisk-24 TOOL-dQuietDisk-25 TOOL-dQuietDisk-26 TOOL-dQuietDisk-27 TOOL-dQuietDisk-28 TOOL-dQuietDisk-29 TOOL-dQuietDisk-30 TOOL-dQuietDisk-31 TOOL-dQuietDisk-32 TOOL-dQuietDisk-33 TOOL-dQuietDisk-34 TOOL-dQuietDisk-35 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 TOOL-dQuietDisk-38 TOOL-dQuietDisk-39 TOOL-dQuietDisk-40 TOOL-dQuietDisk-41
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

- Classification (M2): every roster unit MISSING at open, specced by the spec-writer role.
- Chain map (v2 `[chain]`): units 1 to 15, 19, 26, 28, 36 and 37 sit in dWitnessedBar's area (Test: gate health, held
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
| 20 | `TOOL-dQuietDisk-26` | `check-wiring.sh` lists the tree once per invocation, every check reading that one listing |
| 21 | `TOOL-dQuietDisk-28` | the history store resolves its policy switch once per process, not once per verb |
| 22 | `TOOL-dQuietDisk-36` | the closing review's round-1 fold: the bash template cache runs git with the inherited git environment scrubbed, and the turnstile suite grades both the spared live other repository and the swept orphan |
| 23 | `TOOL-dQuietDisk-37` | the closing review's MEDIUM and LOW findings, batched: the missing arms for the attestations, the owned scratch root, the one-diff rule, the template race and BlobBatch's fallbacks, the template key's builder arguments, the CR guard on batch names, and the run-selftests comment |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** DEFERRED · 23 unit(s) · node d · opened 2026-11-20 · streams tooling
ids TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16
ids TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-20 TOOL-dQuietDisk-21 TOOL-dQuietDisk-22 TOOL-dQuietDisk-23 TOOL-dQuietDisk-24 TOOL-dQuietDisk-25 TOOL-dQuietDisk-26 TOOL-dQuietDisk-27 TOOL-dQuietDisk-28 TOOL-dQuietDisk-29 TOOL-dQuietDisk-30 TOOL-dQuietDisk-31
ids TOOL-dQuietDisk-32 TOOL-dQuietDisk-33 TOOL-dQuietDisk-34 TOOL-dQuietDisk-35 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 TOOL-dQuietDisk-38 TOOL-dQuietDisk-39 TOOL-dQuietDisk-40 TOOL-dQuietDisk-41

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dQuietDisk-1 — one store of immutable history verdicts, keyed by the ids each one reads, with one `cat-file --batch` reader](spec/2026-11-20-spec-TOOL-dQuietDisk-1.md) | 1 | 2 | CLOSED | rev-4 | 2026-11-22 |
| [TOOL-dQuietDisk-14 — the kit attestation: gov's green held run of a kit's self-tests, recorded by content and carried in the adopter's receipt](spec/2026-11-20-spec-TOOL-dQuietDisk-14.md) | 1 | 2 | CLOSED | rev-3 | 2026-11-22 |
| [TOOL-dQuietDisk-2 — the pass-order leg grades only units whose key moved since its last graded tip](spec/2026-11-20-spec-TOOL-dQuietDisk-2.md) | 2 | 2 | CLOSED | rev-6 | 2026-11-22 |
| [TOOL-dQuietDisk-3 — the brief-recorded leg grades only units whose key moved since its last graded tip](spec/2026-11-20-spec-TOOL-dQuietDisk-3.md) | 2 | 2 | CLOSED | rev-5 | 2026-11-22 |
| [TOOL-dQuietDisk-4 — routed-commits reads only the commits its store does not already hold](spec/2026-11-20-spec-TOOL-dQuietDisk-4.md) | 2 | 2 | CLOSED | rev-4 | 2026-11-22 |
| [TOOL-dQuietDisk-5 — one `git diff --name-only BASE` decides every plain-guarded leg of a bar](spec/2026-11-20-spec-TOOL-dQuietDisk-5.md) | 2 | 2 | CLOSED | rev-3 | 2026-11-22 |
| [TOOL-dQuietDisk-7 — one suite template cache: each base repository built once, keyed by its inputs, and cloned per case](spec/2026-11-20-spec-TOOL-dQuietDisk-7.md) | 2 | 2 | CLOSED | rev-6 | 2026-11-22 |
| [TOOL-dQuietDisk-8 — the whole-tree readers clone without copying objects and check out only what they read](spec/2026-11-20-spec-TOOL-dQuietDisk-8.md) | 2 | 2 | CLOSED | rev-5 | 2026-11-22 |
| [TOOL-dQuietDisk-10 — `check-wiring.test.sh` builds its wired copies from one captured config, with no per-copy git](spec/2026-11-20-spec-TOOL-dQuietDisk-10.md) | 3 | 2 | CLOSED | rev-4 | 2026-11-22 |
| [TOOL-dQuietDisk-12 — `pre-push.test.sh` builds each repeated pushed-main fixture once and copies it per arm](spec/2026-11-20-spec-TOOL-dQuietDisk-12.md) | 3 | 2 | CLOSED | rev-3 | 2026-11-22 |
| [TOOL-dQuietDisk-13 — the run-gates suites build each repeated scratch repository once and clone it per arm, where a clone saves](spec/2026-11-20-spec-TOOL-dQuietDisk-13.md) | 3 | 2 | CLOSED | rev-4 | 2026-11-22 |
| [TOOL-dQuietDisk-18 — `govkit apply` reads both of its verdict maps through the target's reuse cache](spec/2026-11-20-spec-TOOL-dQuietDisk-18.md) | 3 | 2 | CLOSED | rev-4 | 2026-11-22 |
| [TOOL-dQuietDisk-28 — the history store's bash face resolves the switch and the git dirs once per calling shell](spec/2026-11-22-spec-TOOL-dQuietDisk-28.md) | 3 | 2 | CLOSED | rev-1 | 2026-11-22 |
| [TOOL-dQuietDisk-6 — the manifest check's pickaxe diffs only the commits whose stamp moved](spec/2026-11-20-spec-TOOL-dQuietDisk-6.md) | 3 | 2 | WONTDO | rev-5 | 2026-11-22 |
| [TOOL-dQuietDisk-11 — govkit's scratch targets come from the template cache, so `selftest.py` builds each distinct target once](spec/2026-11-20-spec-TOOL-dQuietDisk-11.md) | 4 | 2 | CLOSED | rev-4 | 2026-11-22 |
| [TOOL-dQuietDisk-15 — a kit self-test leg is held where gov's attestation matches the vendored bytes](spec/2026-11-20-spec-TOOL-dQuietDisk-15.md) | 4 | 2 | DEFERRED | rev-3 | 2026-11-22 |
| [TOOL-dQuietDisk-16 — `govkit update` reads every gov blob through one `cat-file --batch` handle](spec/2026-11-20-spec-TOOL-dQuietDisk-16.md) | 4 | 2 | CLOSED | rev-4 | 2026-11-22 |
| [TOOL-dQuietDisk-26 — `check-wiring.sh` lists the tree once per invocation](spec/2026-11-20-spec-TOOL-dQuietDisk-26.md) | 4 | 2 | CLOSED | rev-3 | 2026-11-22 |
| [TOOL-dQuietDisk-17 — `govkit update` skips a kit's verify check when nothing moved since its baseline](spec/2026-11-20-spec-TOOL-dQuietDisk-17.md) | 5 | 2 | WONTDO | rev-5 | 2026-11-22 |
| [TOOL-dQuietDisk-9 — every scratch path under one owned, swept root, and every tree removed by one chmod-and-retry helper](spec/2026-11-20-spec-TOOL-dQuietDisk-9.md) | 6 | 2 | CLOSED | rev-6 | 2026-11-22 |
| [TOOL-dQuietDisk-19 — the before and after measurements, with their instruments](spec/2026-11-20-spec-TOOL-dQuietDisk-19.md) | 7 | 1 | CLOSED | rev-5 | 2026-11-22 |
| [TOOL-dQuietDisk-36 — the bash template cache runs git without the inherited git environment, and the turnstile suite grades the spared live repository and the swept orphan](spec/2026-11-22-spec-TOOL-dQuietDisk-36.md) | 8 | 2 | CLOSED | rev-1 | 2026-11-22 |
| [TOOL-dQuietDisk-37 — the closing review's MEDIUM and LOW findings: the missing arms, the template key's builder arguments, the CR guard on batch names, and the serial runner's owned temp root](spec/2026-11-22-spec-TOOL-dQuietDisk-37.md) | 9 | 2 | CLOSED | rev-1 | 2026-11-22 |
<!-- /gen:build-units -->

Records: 141 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dQuietDisk-1 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-2 TOOL-dQuietDisk-26
TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37.

Ids whose spec moved past its audited revision: none — 0 of 23 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dQuietDisk-1`, `TOOL-dQuietDisk-14` | yes |
| 2 | `TOOL-dQuietDisk-2`, `TOOL-dQuietDisk-3`, `TOOL-dQuietDisk-4`, `TOOL-dQuietDisk-5`, `TOOL-dQuietDisk-7`, `TOOL-dQuietDisk-8` | no |
| 3 | `TOOL-dQuietDisk-10`, `TOOL-dQuietDisk-12`, `TOOL-dQuietDisk-13`, `TOOL-dQuietDisk-18`, `TOOL-dQuietDisk-28`, `TOOL-dQuietDisk-6` | no |
| 4 | `TOOL-dQuietDisk-11`, `TOOL-dQuietDisk-15`, `TOOL-dQuietDisk-16`, `TOOL-dQuietDisk-26` | no |
| 5 | `TOOL-dQuietDisk-17` | no |
| 6 | `TOOL-dQuietDisk-9` | no |
| 7 | `TOOL-dQuietDisk-19` | no |
| 8 | `TOOL-dQuietDisk-36` | no |
| 9 | `TOOL-dQuietDisk-37` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
