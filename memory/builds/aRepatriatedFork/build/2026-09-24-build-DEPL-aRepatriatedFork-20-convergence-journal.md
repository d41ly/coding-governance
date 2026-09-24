# DEPL-aRepatriatedFork-20 — the inCMS convergence, first pass

**Serves:** journal DEPL-aRepatriatedFork-20

This is one unit pass under the aRepatriatedFork mandate. It wrote code only in an inCMS worktree
and wrote only records in gov. It ran no merge bar, no self-test suite, and no inCMS bar. The unit
ends BLOCKED. Two things are still open. The owner has to land it at inCMS. And the work listed
under "What remains" has to go onto the branch first.

## Where the work is

- **inCMS worktree:** `C:/projects/incms/main/.claude/worktrees/converge-arf20`.
- **Branch:** `converge/aRepatriatedFork-20`. It is not pushed and not merged.
- **Base:** inCMS `main` at `bc7e955894e15f34a086c1875f2f9af3cceb77bb`.
- **Tip:** `2b8d9a5cd04089c8416670fe87c9026c01ddb09d`.
- **Gov side:** the build branch at `55b82891` when the pass started.
- **Untouched:** inCMS's primary tree and its other worktrees. The branch's four commits are the
  only writes at inCMS.

| inCMS commit | What it carries |
|---|---|
| `a9745bc4b` | S1, first half. `gen_build_index.py`, `corpus_ids.py`, `gotchas.py`, `merge-rows.py` and `check-arms.py` now carry gov's a7c78ad2 blobs, and their five receipt rows are PINNED at that vintage. |
| `e75268199` | S6. `step02-migrate-memory.py`, committed and not run. The conf gains `DISCIPLINES`, `CHARTER`, `SPEC_FORMAT_CUTOFF` and a re-measured `ARMS_FLOORS`. |
| `1f29d2a01` | S2. step02 now lays each README out the way gov's slot contract reads it. |
| `2b8d9a5cd` | S3. `TOMBSTONE_ROOTS="docs"`, so gov's check 11 keeps inCMS's old check 11. |

### Why the five rows had to be pinned first (S1)

Before the pass, `govkit update --target <inCMS> --kits memory-tree` read the four programs and
`check-arms.py` as `unattributed`, with "no base to write against". So an update would never have
landed gov's bytes on them, and AC1 could not have passed.

- **Measured after step 01:** the same read-only update lists all five as `stale`, so they can land.
- **How the rows were made:** by govkit's own `adopt --re-adopt --staged`, with the 15 existing pins
  re-supplied and these five added.
- **What was taken from that run:** only those five rows and their sums lines, grafted by
  `step01-graft-receipt-rows.py`. The re-adopt re-measured all 209 rows, and it moved dozens that are
  outside this unit: roles, version strings, and `gov_source`, which it set to this worktree's path.
  So its receipt was not taken whole.
- **Check:** `check-receipt.sh --staged` passed on the five rows.

### Why step 02 is committed but not run

The installed hooks at `.git/incms-hooks` are copies, and they still call `check-docs-hygiene.sh
--staged` on any `memory/**` commit. That engine reds a migrated tree on its checks 22 and 31. The
engine that replaces it only lands with the S1 wiring, and that wiring is not on the branch yet. So
running the migration is a landing step. Here it was run only in a scratch clone.

## What the migration does to the tree

Measured in a `git clone --local` of the branch at `%TEMP%/arf20c`, with `step02 --apply`, then gov
HEAD's programs run from this worktree. The clone is scratch and was not committed.

- **Front matter:** 326 READMEs rewritten. That is 326, not 324: two builds opened since the census.
- **Statuses:** 194 READMEs have no gov-parseable spec header. Their records decide 44, and 150 are
  parked.
- **Rosters:** 70 are taken from the build's stream, because the build has no family-bearing id.
- **Ids dropped:** twelve READMEs carry `PKG-*` ids. `PKG` is not in inCMS's FAMILIES, so those ids
  leave `ids:`.
- **Gotchas:** 241 `metadata:` blocks stripped. Nine gates declared, and 63 records parked.
- **Registries:** 11 present-tense readers repointed to `memory/project/` for the two moved files.
- **With the 150 parked statuses answered:** they were stubbed in the clone ONLY, as a probe. Then
  `gen_build_index.py --write` wrote 971 artifacts, and `--check` came back clean over all 971.
- **`--check-format` before the layout fix:** 5532 findings across all 326 READMEs. After step02's
  layout fix, the only findings left are the 41 below.
- **Gov's `gotchas.py --check` on the migrated clone:** it refuses first on
  `recurring-bug-classes.md`, which has no front matter. With that file moved to `memory/guides/` as
  a probe, the result is: check 17, 1 finding (INDEX stale, which `--write` fixes); check 18, 59; and
  check 19, 1 (`stale-docker-container-owns-port.md` has no anchor).

### A gov finding the migration surfaced

`gen_build_index.py --check-format` treats every tracked `README.md` under `memory/builds/` as a
build README, at any depth (`gen_build_index.py:1734`). inCMS keeps 41 folder-shaped legacy records
whose index file is a `README.md`: 27 under `reviews/`, 13 under `spec/` and 1 under `build/`. Each of
the 41 reds "no generated region pair". Gov has no nested README, so its own bar cannot see this.

The fix is a population predicate in a gov file this unit's write set does not hold. Until gov fixes
it, AC3 cannot pass at inCMS unless inCMS renames 41 grandfathered records. So it is recorded here
for the owner and the closing review, and it is not patched.

## Every inCMS check, and where it goes (S5, AC5's first half)

`check-docs-hygiene.sh` defines checks 1-8, 10-19 and 21-32. Its check 9 was retired before this
build.

| inCMS check | Property | Disposition |
|---|---|---|
| 1 | prompt placement | gov check 1 |
| 2 | link integrity | gov check 2 |
| 3 | structure lint | gov check 3 |
| 4 | build-folder naming and shape | gov check 4 |
| 5 | recording-file naming | gov check 5, with `legacy-files.txt` moved to `memory/project/` |
| 6 | index size caps | gov check 6, with `curation-debt.txt` moved to `memory/project/` |
| 7 | entry budget | gov check 7 |
| 8 | status vocabulary | gov check 8 |
| 10 | rotation note | gov check 10 |
| 11 | docs/ tombstone | gov check 11 via `TOMBSTONE_ROOTS="docs"` |
| 12 | spec-format ratchet | gov check 12 via `SPEC_FORMAT_CUTOFF="2026-07-15"` |
| 13 | spec-section canon freshness | inCMS project leg (F5), NOT YET BUILT |
| 14 | anchor-grammar coverage of rows | gov check 20 |
| 15 | id uniqueness inside one index file | gov check 20 |
| 16 | the recall fixture resolves into the corpus | inCMS project leg (F5), NOT YET BUILT |
| 17 | the orphan waiver describes the corpus | gov check 14 |
| 18 | the dead-path registry describes the corpus | gov check 15 |
| 19 | the summed read-path ceiling | inCMS project leg (F4), NOT YET BUILT |
| 21 | an added memory path is adopted | inCMS project leg (F5), NOT YET BUILT |
| 22 | a recording's session slug is rostered | retired by F3's delegated resolution; `roster:` now means families |
| 23 | build-index freshness | gov check 9 |
| 24 | gotchas INDEX freshness | gov check 17 |
| 25 | a new gotcha declares its gate | gov check 18, corpus-wide, per F2 |
| 26 | help/ and infra/ name no retired discipline dir | inCMS project leg (F5), NOT YET BUILT |
| 27 | a minted id owns a recorded row | retired by F3; gov backlog row owed at the landing |
| 28 | shipped ids are not SPECCED | retired by F3; gov backlog row owed at the landing |
| 29 | a new memory .md carries no NUL byte | inCMS project leg (F5), NOT YET BUILT |
| 30 | CLAUDE.md micro-formats parse under one grammar | inCMS project leg (F5), NOT YET BUILT |
| 31 | front-matter keys nothing reads | retired by F1, which it contradicts |
| 32 | no literal-credential fallback in memory scripts | inCMS project leg (F5), NOT YET BUILT |

## What remains before the owner can land this

Every item below goes on `converge/aRepatriatedFork-20`. It lands in one piece with the four commits
already there. None of it is done, and there is no gate this pass knows of that would pass without
it.

1. **The eight inCMS-only checks (S5).** The checks are 13, 16, 19, 21, 26, 29, 30 and 32. Extract
   them from `check-docs-hygiene.sh` into one inCMS project leg, with its ceiling and a
   testsuite-count row. Observe each one red on a staged violation (AC5).
   - Check 19 calls `corpus_ids.py --check readset`, which leaves with inCMS's `corpus_ids.py`.
     Its implementation has to move into an inCMS-owned module first: `check_readset`, the
     `READ_PATH_*` constants, and their helpers from the file's `bc7e95589` blob.
2. **The recall selftest (S4, AC4).** `scripts/recall/selftest.py` has 25 arms that import inCMS's
   `corpus_ids.py` directly. The 13 `check_s10_*` arms reach it through `_rs_import`.
   - The 13 `check_s10_*` arms test the readset, so they move with check 19 to the module in item 1.
   - The other 25 retire. They are the corpus-path classifier, the H1 rule, the waiver, backfill,
     sieve, id-uniqueness and S4/S7 path arms, and they test the implementation that retired.
   - Remove them from the registration list at `selftest.py:4044`.
   - Until this lands, the `recall-regression` leg on the branch is RED, because step 01 already
     swapped `corpus_ids.py`.
3. **The engine wiring (S1, AC2).**
   - `scripts/gate-legs.json`: the `memory-hygiene` argv becomes `scripts/check-memory-hygiene.sh`.
     The `docs-hygiene-test` leg and its ceiling note are deleted.
   - `.githooks/pre-commit`, `pre-merge-commit` and `pre-push`, and `.github/workflows/ci.yml:211`.
   - `.governance/kits.json:150-151,163-166`, and every `check-docs-hygiene.sh` row of
     `scripts/unarmed-branches.txt`.
   - The hook-test stubs: `push-main.test.sh:49`, `test-merge-guards.sh:46`,
     `test-pre-push-hook.sh:31`, `services/api/tests/test_workflow_guards.py:51,97` and
     `install-guards.ps1:121`.
   - `CLAUDE.md:183` and `.claude/SESSION-KICKOFF.md:236`.
   - Delete `check-docs-hygiene.sh`, its test and `hygiene-parity.test.sh`.
4. **The rest of S3.**
   - Fold the 18 `STATUS.md` files and the three root memory files. The root files are
     `backend-test-harness.md`, `browser-preview.md` and `review-workflow-protocol.md`.
   - Move `recurring-bug-classes.md` out of `gotchas/`. It has 17 present-tense readers outside
     `memory/`, including `scripts/recall/fixture.json`.
   - Convert the dead-path and orphan-id registries to gov's grammar.
   - Declare `ORPHAN_ID_PIN`, `DEAD_PATH_PIN`, `RECORD_UNBOUND_PIN` and the caps. These pins can only
     be measured once gov HEAD's `corpus_ids.py` runs at inCMS, which means after the update.
5. **F6.** Re-pin `VERB_OFFENDER_PIN` once, on gov HEAD's bytes after the update, and name the four
   swapped files as the cause.
6. **User docs.** Rewrite `CLAUDE.md:136-138`, which defines `ids:` as the authored minted list.
7. **The parked items below.** Each needs an answer from someone who knows the build or the record.
8. **The 41 nested READMEs.** Either gov fixes the `--check-format` population or inCMS renames them
   (see the gov finding above).

`[[own]]` rows: there are none to delete. inCMS last pulled at gov `a7c78ad2`, before
`DEPL-aRepatriatedFork-13` built them, so its receipt and `kits.json` carry none.

**inCMS legs the owner's landing will owe.** The landing needs inCMS's full bar (AC7), and within
it these legs:

- `memory-hygiene` on gov's engine (AC2)
- `recall-regression` and `lexicon` (AC4)
- `receipt-sync`, `encoding-posture` and `merge-rows-test`
- the project leg item 1 creates
- the arms meta-gate that `ARMS_FLOORS` feeds

The landing order is in the branch's `scripts/memory-reorg/converge/README.md`.

## Status decided by the builds' own records (44)

The rule is in step02's docstring. A spec's first status statement decides it. A STATUS.md that
opens with a completion banner decides the whole build. An undecided statement anywhere parks the
build.

- `aBrambleFinch` — CLOSED — spec statements CLOSED
- `aComposableLoom` — CLOSED — spec statements CLOSED
- `aFocusedLens` — CLOSED — spec statements CLOSED
- `aFoldingStrata` — CLOSED — STATUS.md opens with a completion banner
- `aFusedFoyer` — CLOSED — spec statements CLOSED
- `aMendedLedger` — CLOSED — spec statements CLOSED
- `aPlayfulScaffold` — CLOSED — spec statements CLOSED
- `aPliantCanvas` — CLOSED — spec statements CLOSED
- `aScalingSextant` — CLOSED — spec statements CLOSED
- `aStatelyNumeral` — CLOSED — STATUS.md opens with a completion banner
- `aSwiftHourglass` — CLOSED — spec statements CLOSED
- `aTemperedCanvas` — CLOSED — spec statements CLOSED
- `aThriftyHeron` — CLOSED — spec statements CLOSED
- `aUnifiedPlugboard` — CLOSED — spec statements CLOSED
- `aUnifyingLocksmith` — CLOSED — spec statements CLOSED
- `aVigilantWarden` — CLOSED — spec statements CLOSED
- `aWovenLantern` — CLOSED — spec statements CLOSED
- `bOrderlyAtlas-memory-reorg` — CLOSED — spec statements CLOSED
- `cFaithfulPrism` — CLOSED — spec statements CLOSED+WONTDO
- `ci` — CLOSED — spec statements CLOSED
- `conversion-delivery-operability` — CLOSED — spec statements CLOSED
- `dChiseledGrammar` — CLOSED — spec statements CLOSED
- `dGraftedAtelier` — CLOSED — spec statements CLOSED
- `dLayeredKeystone` — SPECCED — spec statements SPECCED
- `dSuppleLattice` — CLOSED — spec statements CLOSED
- `dUnbrandedCrate` — CLOSED — spec statements CLOSED
- `dWovenAtlas` — CLOSED — STATUS.md opens with a completion banner
- `eCandidSieve` — CLOSED — spec statements CLOSED
- `eTrifoldCharter` — CLOSED — spec statements CLOSED
- `eventing-webhooks` — CLOSED — spec statements CLOSED
- `extendability-hardening` — CLOSED — spec statements CLOSED
- `feature-flags` — CLOSED — spec statements CLOSED
- `font-upload` — CLOSED — spec statements CLOSED
- `forms-overhaul` — CLOSED — spec statements CLOSED
- `mcp-governance` — CLOSED — spec statements CLOSED
- `mcp-legacy-token-tls` — CLOSED — spec statements CLOSED
- `nicocares-editorial-illustration` — SPECCED — spec statements SPECCED
- `nicocares-integration` — CLOSED — spec statements CLOSED
- `palette-external-color-apis` — SPECCED — spec statements SPECCED
- `phase6-mcp-tokens` — CLOSED — spec statements CLOSED
- `plugin-phase1-tier0` — CLOSED — spec statements CLOSED
- `rest-api-credentials` — CLOSED — spec statements CLOSED
- `sitewide-spacing` — CLOSED — spec statements CLOSED
- `svg-support` — CLOSED — spec statements CLOSED

## Status no record decides — PARKED by name (150)

Left WITHOUT a `status:` key, so gov's generator refuses each one by name until it is answered. Ten of these were opened in August or September; the census named them as the ones needing a real answer each, and none of their records states a status.

- `aBraidedMains` — opened 2026-07-11 — no record states a status
- `aBranchingTrellis` — opened 2026-07-11 — no record states a status
- `aBridgingHeron` — opened 2026-06-28 — undecided statement(s): README.md: BUILD
- `aCandidLatch` — opened 2026-07-28 — no record states a status
- `aCandidPlacard` — opened 2026-07-11 — undecided statement(s): 2026-07-11-spec-aCandidPlacard-1.md: PROPOSED
- `aClearedRunway` — opened 2026-07-10 — no record states a status
- `aClearedUnderbrush` — opened 2026-07-10 — no record states a status
- `aCompactedBedrock` — opened 2026-07-05 — undecided statement(s): 2026-07-05-spec-aCompactedBedrock-1.md: SPEC
- `aCuriousLighthouse` — opened 2026-06-29 — no record states a status
- `aDeckledVignette` — opened 2026-07-04 — no record states a status
- `aDialectFold` — opened 2026-07-11 — no record states a status
- `aDutifulCourier` — opened 2026-06-30 — no record states a status
- `aEtchedColophon` — opened 2026-07-03 — no record states a status
- `aEvergreenBeacon` — opened 2026-06-29 — undecided statement(s): nicocares-classic-appearance-option.md: DRAFT
- `aFencedNamespace` — opened 2026-07-15 — no record states a status
- `aFerriedToolkit` — opened 2026-08-30 — no record states a status
- `aFoldedRampart` — opened 2026-07-13 — no record states a status
- `aGallantOtters` — opened 2026-06-27 — no record states a status
- `aGildedToggles` — opened 2026-06-27 — undecided statement(s): feature-flags-catalog-ui.md: RATIFIED
- `aGirdedFrame` — opened 2026-07-13 — undecided statement(s): 2026-07-13-spec-aGirdedFrame-1.md: SPEC
- `aKindledHearth` — opened 2026-07-01 — no record states a status
- `aKindledToggles` — opened 2026-07-11 — no record states a status
- `aKnittedSeam` — opened 2026-07-16 — no record states a status
- `aLaconicQuill` — opened 2026-07-03 — no record states a status
- `aLayeredParcel` — opened 2026-06-28 — undecided statement(s): site-packages.md: DESIGN
- `aLeanCharter` — opened 2026-07-03 — no record states a status
- `aLevelCornice` — opened 2026-07-21 — no record states a status
- `aLucidVitrine` — opened 2026-07-01 — undecided statement(s): SPEC.md: DOR
- `aMendedGlyph` — opened 2026-07-01 — undecided statement(s): 2026-07-01-settings-media-tracking.md: SPEC
- `aMendedMasthead` — opened 2026-07-10 — no record states a status
- `aMendingThicket` — opened 2026-06-29 — no record states a status
- `aPanningProspector` — opened 2026-07-01 — no record states a status
- `aProwlingComet` — opened 2026-06-27 — no record states a status
- `aQuietedKlaxon` — opened 2026-07-15 — no record states a status
- `aRealignedRace` — opened 2026-07-10 — no record states a status
- `aResurfacedRelics` — opened 2026-07-10 — undecided statement(s): 2026-07-10-spec-aResurfacedRelics-1.md: RATIFIED; 2026-07-10-spec-aResurfacedRelics-2.md: RATIFIED; 2026-07-10-spec-aResurfacedRelics-3.md: RATIFIED
- `aRoamingLantern` — opened 2026-06-28 — undecided statement(s): search-frontend-implementation.md: DERIVED; search-frontend-integration.md: APPROVED
- `aSealedConduit` — opened 2026-07-01 — no record states a status
- `aShardedLedger` — opened 2026-07-04 — undecided statement(s): 2026-07-04-spec-aShardedLedger-1.md: SPEC
- `aSiftedArchive` — opened 2026-07-10 — no record states a status
- `aSingularConduit` — opened 2026-06-29 — no record states a status
- `aSlackenedPortcullis` — opened 2026-08-13 — no record states a status
- `aSpannedKeystone` — opened 2026-07-28 — no record states a status
- `aSpeccedForge` — opened 2026-07-13 — undecided statement(s): 2026-07-13-spec-aSpeccedForge-1-b8-inbound-hooks.md: SPEC; 2026-07-13-spec-aSpeccedForge-10-e2-editor-fields.md: SPEC; 2026-07-13-spec-aSpeccedForge-11-d3-wasm-sandbox.md: SPEC; 2026-07-13-spec-aSpeccedForge-2-b1a-auth-datasource.md: SPEC; 2026-07-13-spec-aSpeccedForge-3-b5-settings-panel.md: SPEC; 2026-07-13-spec-aSpeccedForge-4-b3v2-field-conditions.md: SPEC; 2026-07-13-spec-aSpeccedForge-5-b9-package-mcp.md: SPEC; 2026-07-13-spec-aSpeccedForge-6-sigrevoke-rt.md: SPEC; 2026-07-13-spec-aSpeccedForge-7-a3-versioned-upgrade.md: SPEC; 2026-07-13-spec-aSpeccedForge-8-d2-client-islands.md: SPEC; 2026-07-13-spec-aSpeccedForge-9-e1-admin-surface.md: SPEC; 2026-07-14-spec-aSpeccedForge-12-flag-consolidation.md: SPEC
- `aStampedFolio` — opened 2026-07-10 — undecided statement(s): 2026-07-10-spec-aStampedFolio-1.md: RATIFIED
- `aSteadfastHarbor` — opened 2026-06-28 — undecided statement(s): end-user-auth-dashboard.md: RATIFIED
- `aSweptDockyard` — opened 2026-08-18 — no record states a status
- `aTetheredLantern` — opened 2026-07-01 — undecided statement(s): P1-model-migration.md: RATIFIED; P3-render.md: RATIFIED
- `aTetheredProvenance` — opened 2026-07-05 — undecided statement(s): 2026-07-05-spec-aTetheredProvenance-1.md: ROOT; 2026-07-05-spec-aTetheredProvenance-2.md: SPEC
- `aThriftyTollbooth` — opened 2026-08-04 — no record states a status
- `aThrivingHarbor` — opened 2026-07-02 — undecided statement(s): feature-a-faceted-filtering.md: SPEC; feature-b-dual-path-email.md: SPEC; about.md: SPEC; article-detail.md: SPEC; compare-vs-hims.md: SPEC; contact.md: SPEC; doctor-profile.md: SPEC; doctors.md: SPEC; faq.md: SPEC; for-families.md: SPEC; for-female-health.md: SPEC; for-men.md: SPEC; for-postpartum.md: SPEC; for-women-40-64.md: SPEC; home.md: SPEC; how-it-works.md: SPEC; journal.md: SPEC; legal-compliance.md: SPEC; legal-privacy.md: SPEC; legal-terms.md: SPEC; payments.md: SPEC; press.md: SPEC; pricing.md: SPEC; reviews.md: SPEC; safety.md: SPEC; splash.md: SPEC; start.md: SPEC; treatments-injectable.md: SPEC; treatments-sublingual.md: SPEC; treatments.md: SPEC; weight-care-states.md: SPEC; collectionfilter-pagination.md: BUILT; cost-estimator.md: BUILT; detail-jsonld.md: BUILT; disclaimer-pattern.md: BUILT; eligibility-teaser.md: BUILT; entry-byline.md: BUILT; entry-profile-header.md: BUILT; illustrated-portraits.md: BUILT; imagery-pipeline.md: SPEC; item-page-templates.md: BUILT; reviews-system.md: BUILT; seed-reauthor-wave.md: SPEC; sticky-cta.md: BUILT; video-background.md: DRAFT; phase-1-splash-waitlist.md: SPEC; phase-3-list-activation.md: SPEC; phase-5-optimization.md: SPEC; D-landers.md: SPEC; H-home.md: SPEC
- `aTidiedConfluence` — opened 2026-08-31 — no record states a status
- `aTracedBlueprint` — opened 2026-07-15 — no record states a status
- `aTracedBlueprint-fd35` — opened 2026-07-16 — no record states a status
- `aVerdantKeystone` — opened 2026-06-30 — no record states a status
- `aVernalForge` — opened 2026-07-06 — no record states a status
- `aWaltzingNarwhals` — opened 2026-06-18 — undecided statement(s): id-allocation-session-slugs.md: PROPOSED
- `aWardedLedger` — opened 2026-07-01 — no record states a status
- `aWardedScribe` — opened 2026-07-10 — undecided statement(s): 2026-07-10-spec-aWardedScribe-1.md: REV
- `aWaxedThimble` — opened 2026-08-03 — no record states a status
- `aWidenedSluice` — opened 2026-07-17 — no record states a status
- `aWinnowingFalcon` — opened 2026-06-30 — no record states a status
- `admin-band-discovery` — opened 2026-06-13 — no record states a status
- `admin-interaction-patterns` — opened 2026-06-22 — no record states a status
- `admin-mobile-audit` — opened 2026-06-14 — no record states a status
- `admin-shell-ia` — opened 2026-06-22 — undecided statement(s): admin-shell-ia.md: PROPOSED
- `admin-ux-remediation` — opened 2026-06-24 — undecided statement(s): admin-ux-remediation.md: PROPOSED
- `admin-ux-w6-preview-gallery` — opened 2026-06-26 — no record states a status
- `appearance-editor` — opened 2026-06-22 — undecided statement(s): appearance-editor.md: BUILT
- `autoupdate` — opened 2026-06-19 — undecided statement(s): autoupdate.md: ANALYSIS
- `bJauntyGirder` — opened 2026-07-19 — no record states a status
- `bLatchedWicket` — opened 2026-07-21 — no record states a status
- `bOrderlyAtlas` — opened 2026-07-03 — no record states a status
- `bPacedLantern` — opened 2026-08-01 — no record states a status
- `bWardedThreshold` — opened 2026-07-11 — undecided statement(s): 2026-07-11-spec-bWardedThreshold-1.md: SPEC
- `bWhittledTome` — opened 2026-07-15 — no record states a status
- `block-color-system` — opened 2026-06-20 — no record states a status
- `block-extensibility` — opened 2026-06-13 — undecided statement(s): block-extensibility.md: PROPOSED
- `block-style-controls` — opened 2026-06-22 — undecided statement(s): block-style-controls.md: RATIFIED
- `cBrimmingCellar` — opened 2026-07-03 — no record states a status
- `cBundledHarrier` — opened 2026-07-04 — no record states a status
- `cCandidLedger` — opened 2026-07-04 — no record states a status
- `cCraftedMissive` — opened 2026-07-04 — no record states a status
- `cDiligentMagpie` — opened 2026-07-04 — no record states a status
- `cDurableCourier` — opened 2026-07-03 — no record states a status
- `cGildedWorkshop` — opened 2026-07-05 — no record states a status
- `cGracefulThreshold` — opened 2026-07-05 — undecided statement(s): 2026-07-05-spec-cGracefulThreshold-1.md: RATIFIED
- `cMendedBinary` — opened 2026-07-04 — no record states a status
- `cMendingWayfarer` — opened 2026-07-03 — no record states a status
- `cMoltingPennant` — opened 2026-07-04 — undecided statement(s): 2026-07-04-spec-cMoltingPennant-1.md: RECOMMENDATIONS; 2026-07-04-spec-cMoltingPennant-2.md: BUILT
- `cOrderlyAtrium` — opened 2026-07-05 — no record states a status
- `cRosettaLedger` — opened 2026-07-04 — no record states a status
- `cSealedRampart` — opened 2026-07-03 — no record states a status
- `cShieldedConduit` — opened 2026-07-04 — no record states a status
- `cTolerantGatekeeper` — opened 2026-07-05 — no record states a status
- `cVernalForge` — opened 2026-07-06 — no record states a status
- `cVigilantBeacon` — opened 2026-07-03 — no record states a status
- `cWardedTurnstile` — opened 2026-07-04 — no record states a status
- `codebase-audit` — opened 2026-07-01 — no record states a status
- `content-block-defects` — opened 2026-06-23 — undecided statement(s): content-block-defects.md: RATIFIED
- `contrast-audit` — opened 2026-06-13 — no record states a status
- `conversion-payload-enrichment` — opened 2026-06-21 — undecided statement(s): conversion-payload-enrichment.md: ACCEPTED
- `dCanonicalSigil` — opened 2026-07-11 — no record states a status
- `dCombedArchive` — opened 2026-07-21 — no record states a status
- `dGildedFerry` — opened 2026-07-19 — no record states a status
- `dHushedEmbargo` — opened 2026-07-18 — no record states a status
- `dLucidThicket` — opened 2026-07-09 — undecided statement(s): 2026-07-09-spec-dVeiledLantern-1.md: SPEC
- `dLucidTollgate` — opened 2026-07-18 — no record states a status
- `dMarkedSentry` — opened 2026-07-19 — no record states a status
- `dMarshalledStorefront` — opened 2026-09-03 — no record states a status
- `dNimbleLantern` — opened 2026-06-28 — no record states a status
- `dOrderlyAbacus` — opened 2026-07-10 — no record states a status
- `dPolishedCrucible` — opened 2026-07-18 — no record states a status
- `dQuietedVellum` — opened 2026-07-19 — no record states a status
- `dQuiltedArmory` — opened 2026-07-18 — no record states a status
- `dSaltedCatalogue` — opened 2026-08-23 — no record states a status
- `dSteadfastPostbag` — opened 2026-07-20 — no record states a status
- `dSurveyedThicket` — opened 2026-08-07 — no record states a status
- `dTetheredPennant` — opened 2026-07-19 — no record states a status
- `dVeiledLantern` — opened 2026-07-09 — no record states a status
- `dVelvetMagpie` — opened 2026-06-28 — undecided statement(s): plugin-hardening-dVelvetMagpie.md: DRAFT
- `dWanderingKettle` — opened 2026-06-26 — undecided statement(s): rbac-granular-grants-d109.md: SCOPE
- `dWinnowedSigil` — opened 2026-07-22 — no record states a status
- `deployment-review` — opened 2026-06-13 — no record states a status
- `eBrokeredLattice` — opened 2026-07-11 — no record states a status
- `eFacetedPortico` — opened 2026-07-11 — no record states a status
- `eFaithfulReplica` — opened 2026-07-07 — undecided statement(s): 2026-07-07-spec-eFaithfulReplica-3-decisions-ratified.md: PROVISIONAL
- `eGildedConduit` — opened 2026-07-09 — no record states a status
- `eGuidingConcierge` — opened 2026-07-12 — no record states a status
- `eThriftyBellows` — opened 2026-07-15 — no record states a status
- `eUnbarredGateway` — opened 2026-07-08 — undecided statement(s): 2026-07-08-spec-eUnbarredGateway-1.md: BUILT
- `eVigilantCanary` — opened 2026-07-14 — no record states a status
- `external-catalog-genericization` — opened 2026-07-03 — undecided statement(s): README.md: DESIGN
- `frontend-analytics` — opened 2026-06-19 — undecided statement(s): frontend-analytics.md: DRAFT
- `header-menu-chrome` — opened 2026-06-22 — undecided statement(s): header-menu-chrome.md: RATIFIED
- `i18n` — opened 2026-06-13 — undecided statement(s): i18n.md: PROPOSED
- `initial-design-review` — opened 2026-06-13 — no record states a status
- `interaction-primitives` — opened 2026-07-01 — no record states a status
- `media-focal-point` — opened 2026-06-25 — undecided statement(s): media-focal-point.md: RATIFIED
- `menu-editor-preview-settings` — opened 2026-06-22 — undecided statement(s): menu-editor-preview-settings.md: PROPOSED
- `menus-overhaul` — opened 2026-06-16 — no record states a status
- `native-driver` — opened 2026-06-20 — no record states a status
- `node-doctor` — opened 2026-06-25 — undecided statement(s): node-doctor.md: REVISED
- `p7-unattended-fleet` — opened 2026-06-21 — undecided statement(s): p7-build-plan.md: BUILD
- `palette-editor` — opened 2026-06-21 — undecided statement(s): palette-editor-architecture-integration.md: DESIGN
- `plugin-platform` — opened 2026-06-26 — undecided statement(s): plugin-platform.md: RATIFIED
- `rawhtml-template-component-gate` — opened 2026-06-26 — undecided statement(s): 2026-06-26-rawhtml-template-component-gate.md: IMPLEMENTED
- `reference-template-fidelity` — opened 2026-06-25 — undecided statement(s): reference-template-fidelity.md: BUILT
- `search` — opened 2026-06-13 — undecided statement(s): search.md: PROPOSED
- `security-user-activity` — opened 2026-06-19 — undecided statement(s): security-user-activity-resolver-design.md: DESIGN; security-user-activity.md: DECISIONS

## Gotcha gates declared from the records' own words (9)

- a-for-update-on-an-entity-already-in-the-session-s-identity-map-re-rea.md -> services/api/tests/test_gateway_claim_race.py (the record: "stays green with the fix removed: ... is that shape")
- cms-page-can-squat-a-web-route.md -> services/api/tests/test_starter_packs.py (the record: "Gated for seed packs by `test_no_reserved_path_collisions`")
- hook-using-module-without-use-client-arch-dgildedsextant-1.md -> packages/blocks/src/serverSafeExports.test.ts (the record: "**Gated.**")
- incms-gate-ps1-stderr-abort.md -> services/api/tests/test_powershell_gate_static.py (the record: "**Left-shift:** ... reds if any script drains")
- incms-python-subprocess-bash-wsl-hijack.md -> services/api/tests/test_bash_env.py (the record: "`test_bash_env.py` is the regression gate")
- incms-squash-now-default-aDialectFold.md -> services/api/tests/test_migrate_cli.py (the record: "Left-shift `test_create_superuser_on_a_migration_built_sqlite_db`")
- missing-use-client-passes-every-gate.md -> packages/blocks/src/serverSafeExports.test.ts (the record: "gated since 2026-07-19 by")
- nicocares-repack-third-party.md -> services/api/scripts/check_no_brand.py (the record: "(the zero-hit gate)")
- page-schema-types-parity-gate.md -> apps/web/lib/schemaTypes.test.ts (the record: "Twin gates so neither language drifts")

## Gotcha records no evidence gates — PARKED by name (63)

Left undeclared. Three cite a test that is NOT their gate: `mcp-stdio-handshake-flake.md` names the flaky test itself, `fastmcp-contextvar-does-not-reach-tool-body.md` names a test that bypasses the defect, and `api-suite-db-no-per-test-rollback.md` names only the fixture. `edit-escapes-crlf-shared-docs.md` names checks of the engine that retires. The rest cite no gate at all. Gov HEAD's check 18 reds 59 of these 63 on the migrated clone.

- `a-component-is-mounted-but-its-feature-is-not-wired-des-dpatientmason.md`
- `a-concurrent-gate-sh-and-next-build-corrupt-the-pnpm-symlink-farm.md`
- `a-default-off-deploy-flag-is-a-producer-an-operator-can-simply-omit.md`
- `a-deterministic-client-input-4xx-must-not-be-classified-as-a-transient.md`
- `a-dirty-cue-must-be-text-and-announced-not-a-colour-dot.md`
- `a-domain-409-routed-through-the-optimistic-concurrency-handler.md`
- `a-gate-predicate-copied-from-a-sibling-gate-des-dpatientmason-17-r11.md`
- `a-mutation-that-did-not-apply-and-a-test-that-was-never-collected-both.md`
- `a-self-test-fixture-whose-discriminating-property-is-not-among-the-val.md`
- `a-shared-primitive-built-specimened-and-adopted-by-nothing-des-dpatien.md`
- `a-specimen-only-exercises-the-happy-path-so-the-gaps-that-block-adopti.md`
- `a-tailwind-content-seam-has-no-artifact-at-all.md`
- `a-test-constant-that-encodes-a-platform-limit-where-that-limit-is-the.md`
- `a-test-that-exercises-a-failure-path-but-asserts-only-the-happy-path-i.md`
- `an-editor-only-client-reaching-a-per-block-public-loader-target-arch-d.md`
- `api-suite-db-no-per-test-rollback.md`
- `blocking-work-on-the-hot-path-event-loop.md`
- `check-then-mutate-racing-a-concurrent-bulk-update-lost-insert-pg-read.md`
- `client-as-you-type-autocomplete-robustness.md`
- `client-server-validation-divergence.md`
- `concurrent-session-shares-main-tree-at-push.md`
- `cross-language-catalog-coercion-drift.md`
- `dead-plumbing-through-layers.md`
- `dev-db-unstamped-create-all.md`
- `edit-escapes-crlf-shared-docs.md`
- `empty-string-as-invalid-on-a-native-input-conflated-with-deliberately.md`
- `fastmcp-contextvar-does-not-reach-tool-body.md`
- `feedback-max-4-concurrent-agents.md`
- `gate-vacuous-in-the-way-it-guards.md`
- `half-applied-merges.md`
- `headless-preview-pane-has-no-layout.md`
- `help-copy-that-documents-an-unreachable-capability-des-dpatientmason-1.md`
- `help-copy-written-from-the-spec-not-the-product.md`
- `incms-hero-form-embed-dPaintedCompass.md`
- `incms-msys-docker-bindmount-portability.md`
- `incms-stale-warning-misdiagnosis.md`
- `incms-xdist-worker-crash-is-a-timeout.md`
- `index-that-doesn-t-serve-its-query.md`
- `js-gate-harness-turbofan.md`
- `labelling-the-button-may-not-reach-the-operator.md`
- `login-lockout-gc-flake.md`
- `mcp-stdio-handshake-flake.md`
- `moving-a-field-to-a-second-storage-location-leaves-every-sweep-and-con.md`
- `node-c-js-execution-crash.md`
- `node-c-node-crash-0xc0000005.md`
- `platform-gating-written-as-an-early-return-reports-passed-not-skipped.md`
- `powershell51-cp1251-breaks-repo-ps1.md`
- `puck-custom-field-renders-no-label.md`
- `rawhtml-gate-document-guard.md`
- `sanctioned-html-prop-guard-on-the-page-path-but-not-a-sibling-puck-doc.md`
- `ssh-push-idle-reap-keepalives.md`
- `stale-docker-container-owns-port.md`
- `stale-module-caches.md`
- `superseded-gate-branches.md`
- `tailwind-utility-silently-no-ops.md`
- `the-reference-mount-reads-as-adoption.md`
- `twin-enforcement-points-that-state-the-same-predicate-twice-in-differe.md`
- `unification-is-often-impossible-not-merely-risky.md`
- `windows-worktree-remove-maxpath.md`
- `workflow-finding-id-collision.md`
- `workflow-verdict-join-false-negative.md`
- `workflow-verdict-ref-matching-bug.md`
- `zoom-to-fit-preview-overflow.md`

## Rosters taken from the build's stream, because no id names a family

aBraidedMains aComposableLoom aKnittedSeam aMendedMasthead aRealignedRace aSiftedArchive aSweptDockyard aTracedBlueprint-fd35 aVernalForge aWidenedSluice admin-band-discovery admin-interaction-patterns admin-mobile-audit admin-shell-ia admin-ux-remediation admin-ux-w6-preview-gallery appearance-editor autoupdate bOrderlyAtlas-memory-reorg block-color-system block-extensibility block-style-controls cMendedBinary cOrderlyAtrium ci codebase-audit content-block-defects content-promotion contrast-audit conversion-delivery-operability conversion-payload-enrichment dCombedArchive dQuiltedArmory dSteadfastPostbag deployment-review eventing-webhooks extendability-hardening external-catalog-genericization feature-flags font-upload forms-overhaul frontend-analytics gap-closure header-menu-chrome i18n initial-design-review interaction-primitives mcp-governance mcp-legacy-token-tls media-focal-point menu-editor-preview-settings menus-overhaul native-driver nicocares-editorial-illustration nicocares-integration node-doctor p7-unattended-fleet palette-editor palette-external-color-apis phase6-mcp-tokens plugin-phase1-tier0 plugin-platform rawhtml-template-component-gate reference-template-fidelity rest-api-credentials scheduled-publishing search security-user-activity sitewide-spacing svg-support

## Ids dropped as outside inCMS's FAMILIES

aBraidedLintel: PKG-aBraidedLintel-1; aCandidLatch: PKG-aCandidLatch-1; aQuietedFurrow: PKG-aQuietedFurrow-1; aSpannedKeystone: PKG-aSpannedKeystone-2; aSurveyedCauseway: PKG-aSurveyedCauseway-35 PKG-aSurveyedCauseway-47 PKG-aSurveyedCauseway-6; bBurnishedSconce: PKG-bBurnishedSconce-1; bLucidCadence: PKG-bLucidCadence-51 PKG-bLucidCadence-67; bPacedLantern: PKG-bPacedLantern-1 PKG-bPacedLantern-3; bTemperedLattice: PKG-bTemperedLattice-1 PKG-bTemperedLattice-2 PKG-bTemperedLattice-3 PKG-bTemperedLattice-4 PKG-bTemperedLattice-5; dBraidedLantern: PKG-dBraidedLantern-1 PKG-dBraidedLantern-3; dReconciledIntake: PKG-dReconciledIntake-18 PKG-dReconciledIntake-4 PKG-dReconciledIntake-5 PKG-dReconciledIntake-6; dSiftedGranary: GOTCHA-dSiftedGranary-1
