**Serves:** research DEPL-dShippedRelease-3 DEPL-dShippedRelease-6 DEPL-dShippedRelease-8 DEPL-dShippedRelease-15 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-26

# Reuse scout C — dShippedRelease

The scout's final return, extracted from its transcript by script, never retyped.

All paths are relative to `C:\projects\coding-governance\.claude\worktrees\unattended-dshipped-release-1a351d`, at HEAD `f4597719e`. I wrote nothing in the repository. Every lookup reported no unscanned layers, so no recall-dark caveat applies.

## (1) One row per unit

### DEPL-dShippedRelease-3: kit release notes (`cl-dClosedLoop-0414@d9d47e83`)
- **Decision:** `seam: govkit.py cmd_mint/derive_epoch_state — reuse for version deltas; extend via a sibling verb beside cmd_mint`.
- **Exists:**
  - `tools/govkit/govkit.py:13363` `derive_epoch_state`, `:13421` `cmd_epoch`, `:13497` `cmd_mint`, `:13294` `cmd_shipped`.
  - The lander's mint, `tools/push-main.sh:26-33`.
  - `units-at-landing`, written at `tools/unattended/unattended.sh:6582` and `:7031`. This is the nearest thing to a landing record.
  - `read_landing_commit` at `tools/unattended/lib-unattended.sh:1688`.
- **Missing:** a cut verb, a tag reader, a notes generator, a landing record. Only 3 `archive/*` tags exist.
- **Design:** `layer-expansions.md:457` (the item, every route), `:442` (kind and tag shape), `flow-steps.md:788-790`, `v2:1314`, `v2:1316`, `layer-memory.md:434`.
- **Owned nodes, proposed:** `item.kits.cut`, `item.kits.version`, `policy-key.kits.cadence`, `record-kind.kit-release`. Unit 7 keeps `policy-key.kits.host` and `policy-key.kits.watch-cadence`, since those are its clause's tokens; unit 3 reads them.
- **Policy rows:**
  - `kits.cadence`: yes, `catalogue.toml:1083`.
  - Reads `kits.host` (`:1089`) and `kits.watch-cadence` (`:1095`).
  - All three are unsummarised (`unsummarised-keys.txt:91-93`), so the owning unit drains them.
- **Touches:** `tools/govkit/govkit.py`, a new notes module, `tools/govkit/selftest.py`, `tools/runtime/points.toml` (a cadence row, once it exists), `help/`.

### DEPL-dShippedRelease-6: first engine adapter (`cl-dClosedLoop-0416@7154a42c`)
- **Decision:** `seam: [[adapter]] row of TOOL-dWellOiledMachine-20 at point.flow.release — reuse for registration; extend via the point's own graded fields`. Not built. No engine code exists at HEAD.
- **Exists:**
  - The adopter-name ban, `tools/govkit/govkit.py:3731` (arm 10), over `tools/govkit/adopters.toml`.
  - `check_value` at `tools/policy/policy.py:143`.
- **Design:** walk `:746-748` (WK-8, "fitted to what the first adopter runs"), walkthrough `:553` and `:567`, `layer-expansions.md:327`, `:390`.
- **Owned nodes:** none of the packet's list. The token arm cannot see this clause, so the carrier must be the `**Carries:**` line itself.
- **Policy keys:** no rows exist for the adopter's values. See disagreement 7.
- **Touches:** new adapter files under the new `tools/integrations/` kit, the kit's `kit.toml`, and `tools/runtime/points.toml` once built.

### DEPL-dShippedRelease-8: optional emitted CI (`cl-dClosedLoop-0418@0096c2c8`)
- **Decision:** `seam: [gate_runner.ci] — reuse for the "github-actions only" contract; extend by building the emitter it validates`, plus `.github/workflows/remote-ci.yml` as gov's own instance.
- **Exists:**
  - The validator only, `tools/govkit/govkit.py:6001-6005`.
  - The `ci` role, known at `:2733` and reported at `:8491`, whose comment says DEPL-dCarriedReceipt-6 owns emitting.
  - No `[gate_runner.ci]` row in any descriptor, and no emitter.
  - Pins live as literals at `remote-ci.yml:58`, `:118`, `:137`, `:330`, stated at `:27`.
  - `permissions: contents: read` at `:37-38`.
  - The generated-file mechanism, `tools/policy/kit.toml:49` and `:61` (`[[generated]]`, driven by `regen.py`).
  - `check_ci`-style parsing exists nowhere: `tools/memory-tree/routed_commits.py:248` is only a message. No `uses:` scanner exists.
- **Design:** research-deploy `:123-128`, research-integrations-b `:152` (`ci-emit:github-actions`), gap-deploy-03.
- **Owned nodes:** none. The tokens `permissions:` and `uses:` must appear in the carrier.
- **Policy keys:** none.
- **Touches:** a new pin declaration, templates, an emit/check tool, a `[[gate_leg]]` row, `tools/gate-legs.json`, `tools/govkit/govkit.py`, `.github/workflows/remote-ci.yml`.

### DEPL-dShippedRelease-15: promotion, `release/<E>`, compare-and-swap (`cl-dClosedLoop-0425@3b7313d6`)
- **Decision:** `seam: unattended.sh --lease (TOOL-dPlacedRequest-1 S5), not built — reuse for E's lease; extend by no change, called directly`, and `seam: read_held_reds — reuse for the dead-probe read shape`. Do not use `run_cadence_period` (disagreement 6).
- **Exists:**
  - Only the shapes: `CLAIM_NS="refs/gov/runs"` at `tools/unattended/unattended.sh:2087`, the push CAS at `:2423`, and `read_held_reds` at `:10113`.
  - There is no `--lease` verb at HEAD.
  - The catalogue rows exist; the `deploy.*` and `release.*` keys have no code readers.
- **Design:** `layer-expansions.md:375-393` (the seven items), `:180`, `:395-401`, `:417-423`; `flow-steps.md:498-503`, `:507`; FK-5-6 at whole-audit `:498`; B5-F4 at `layer-expansions.md:706`.
- **Owned nodes, proposed:** all seven `item.release.*`; `policy-key.deploy.runs`, `deploy.promotion`, `deploy.on-verify-fail`, `release.environments`; `record-kind.release`, `record-kind.release-exit`.
- **Policy rows:** yes, all four, at `catalogue.toml:1016`, `:1022`, `:1028`, `:1101`, each on the unsummarised list. The `routing` kind gains `release.route` as a writer (`layer-memory.md:429`).
- **Touches:** `tools/integrations/` (runner, header check), `tools/runtime/points.toml`, `tools/memory-tree/record-kinds.toml`, `tools/loop/loop.toml`, `tools/policy/check_policy.py` (cross-key rule), `tools/policy/catalogue.toml`.

### DEPL-dShippedRelease-19: CI jobs imported as legs (`cl-dClosedLoop-0429@78bd7623`)
- **Decision:** `seam: TOOL-dLinkedLibrary-8's ci-job census class and ruling kind, not built — reuse for job discovery and rulings; extend via an import reader and the ci-job refuse patterns`. Leg rows go through `leg_factory.py` (TOOL-dWitnessedBar-11, not built).
- **Exists at HEAD:** nothing for this. `tools/govkit/census.py` answers a different question (dLinkedLibrary-8 `:199`).
- **Design:** retrofit `:176-179`, `:350-355` (denied by default; the owner rules import, translate, keep alongside or retire); dLinkedLibrary-8 `:105-110`, `:177` (hands the import here), `:246`.
- **Owned nodes:** none.
- **Policy keys:** none.
- **Touches:** `tools/integrations/`, `tools/runtime/points.toml`, an adopter's rendered `gate-legs.json`, a registration check.

### DEPL-dShippedRelease-22: one-way ask mirror (`cl-dClosedLoop-0432@e42728b4`)
- **Decision:** `seam: tools/memory-tree/backlog.py parse_file — reuse for reading asks; extend via a read-only exporter`. The design's seam, a journal reader, does not fit (disagreement 9).
- **Exists:** `parse_file` at `tools/memory-tree/backlog.py:555`, `render_ask_row`, and `read_journal` with `PRODUCER_FILES` at `tools/runlog/runlog_lib.py:40`.
- **Design:** `layer-expansions.md:321`, `:412`, `:99` of the agreement table, research-integrations-a `:149` (the owner's pick: argue away, mirror later), research-integrations-b `:239`, ownership-verify `:769`, `:913`.
- **Owned node, proposed:** `policy-key.integrations.tracker`.
- **Policy row:** yes, `catalogue.toml:1108`, on the unsummarised list at `:89`.
- **Touches:** `tools/integrations/`, `tools/runtime/points.toml`, a `[[selects]]` row in `tools/loop/loop.toml`.

### DEPL-dShippedRelease-26: platform matrix (`cl-dClosedLoop-0436@57841d5d`)
- **Decision:** `seam: run-held-wsl.sh with held_halves.py — reuse for the partition, the halves and the combine; extend by generalizing HOSTS`, and `seam: GATE_LEGS — extend by a fixture manifest, never a second seam` (`memory/map/features/run-gates.md:249-256`).
- **Exists:**
  - `tools/run-gates/run-held-wsl.sh:135` `run_half`, `:154` the half mode, `:157` the `/mnt` refusal, `:172-175` Windows-side only.
  - `tools/run-gates/held_halves.py:61` `HOSTS = ("windows", "wsl")`, `:427` the `--half` choices.
  - `tools/run-gates/windows-only-legs.txt`, withheld from adopters at `tools/run-gates/kit.toml:91-96`.
  - `held-green` is read by no boundary (`run-held-wsl.sh:31`, `held_halves.py:29`).
  - No floor declaration: `tools/lib` holds no floor file.
- **Design:** `v2:1401`, `v2:1402`, `v2:1717`, `v2:1058-1061` (P37), `[planned]` at `v2:1867-1880`, research-compatibility units table, dSafePassage-11 S1, S2, dSafePassage-12.
- **Owned nodes, proposed:** `policy-key.platforms.supported`, `policy-key.platforms.verify`. `platforms.provision` stays dSafePassage's.
- **Policy rows:** yes, `catalogue.toml:1615`, `:1622`, unsummarised at `:155-156`.
- **Touches:** `tools/run-gates/held_halves.py`, `tools/run-gates/run-held-wsl.sh`, `tools/run-gates/README.md`, `tools/run-gates/kit.toml`, the CI templates, the receipt writer in `tools/govkit/govkit.py`.

## (2) Where records and source disagree

1. **`read_held_reds` moved.** `layer-expansions.md:310` and `:503` say `unattended.sh:9972`. It is at `:10113`. TOOL-dWitnessedBar-6 S7 moves it again, to `tools/run-gates/remote_verdict.py`.
2. **`[gate_runner.ci]` moved.** research-deploy `:128` and research-integrations-b `:152` say `govkit.py:5746` and `:5745`. It is at `:6001-6005`, and it is a validator with no emitter.
3. **gap-deploy-11's count is stale.** It says 10 of 29 entries. HEAD has 30 registry entries, and 10 declare `version_from = { none … }`. research-distribution-b says 9 of 29. The "no release tag" half still holds.
4. **Superseded names.**
   - research-distribution-a `:111` has tag `release/<YYYY.MM.DD>`, and `:130` has `govkit release`. Both gave way to `gov/v<date>.<n>` and `kits.cut`; the old tag form would also read like the lease name.
   - research-integrations-a's `release.on-fail` and `release.close` gave way to `release.route` and `release.record`.
5. **`point.cadence-items` cannot carry `kits.cadence`.**
   - TOOL-dWellOiledMachine-59 S1 takes a static `period` of `daily` or `weekly` only.
   - `layer-expansions.md:457` needs `every-landing` (the `landed` event, keyed by SHA) and `owner-cut` (keyed by tip SHA). `kits.watch-cadence` adds `every-session`.
   - The row's `events` field is unread by the S3 tick, and event wakes are a non-goal there.
   - The period is also policy-chosen, while the row is static.
   - The default host `session-start` is left unregistered. TOOL-dWellOiledMachine-13 §3 and -59 §3 hand it to this build, and no clause of the 31 names it. At the default, the tick prints `not ready` and `kits.cut` never fires.
6. **`release/<E>` does not fit the cadence machinery as specced.**
   - The grammar gives `refs/gov/leases/run/release/<E>`, so `<E>` sits in the `<period>` slot.
   - `derive_period` cannot produce it, and TOOL-dWellOiledMachine-13 S6 reads a `landed` status as "already witnessed, run nothing". A second SHA into E would therefore run nothing.
   - So `release.pick` must call `--lease` directly and `release.record` must release with no `--as`, a hand-over. It cannot be a cadence-items row.
   - TOOL-dPlacedRequest-18's non-goals leave the `<period>` grammar to -1.
7. **Environments and engine values have no legal home.**
   - `layer-expansions.md:180` says each environment names an engine, a verify adapter and whether it is production. `release.environments` (`catalogue.toml:1101`) is a list of bare names.
   - `read_catalogue_row` (`tools/policy/policy.py:219-241`) refuses any key with no row, so "the adopter's values in its own policy file" is refused today.
   - The catalogue header says one row per row of the design's table, and v2 has none, so adding rows looks like a departure needing a record.
   - The item regex also admits names illegal as a ref segment (`a..b`, `x.lock`), which `<E>` must pass as a lease segment.
8. **The `integrations` kit has no carrier.**
   - `layer-expansions.md:327` names it: header factory, registry check, `verdict:remote-ci`, the release runner. `tools/integrations` appears in no spec, and no clause of the 31 names the kit.
   - TOOL-dWellOiledMachine-20's `[[adapter]]` row lacks the header's `kind`, witness source, probe and fallback (`layer-expansions.md:303-308`), and TOOL-dWellOiledMachine-17 S1 nests `secret` inside `grant`.
   - `point.flow.release` is spelled only in KICK-dKeptSession-1 `:175`, with no `[[point]]` row. PLAY-dOrderedCharter-16's text does not spell `layer.integrations` either, though TOOL-dBoundRoles-1 `:188` assumes it.
   - TOOL-dWitnessedBar-6 `:123` hands `GATE_POST_MERGE=ci` and `deploy.core`'s remote read to this build. No clause in my group carries them, so someone must place gap-deploy-02 and -10.
9. **The tracker cannot be a journal reader.** `layer-expansions.md:321` says it registers as one. The journal is `driver`, `gates` and `pushes` only (`runlog_lib.py:40`), and TOOL-dWellOiledMachine-16 S7 limits a reader to `read_journal`. Asks are not journal lines. research-integrations-a's "reader of the ask record kind" is the workable form. The owner was never shown a service name, and `mirror-out` names none.
10. **"Test jobs only" is not decidable from the census.** dLinkedLibrary-8 `:246` classes only `refused` jobs. A lint or build job can be ruled `import` and is not a test job. Retrofit `:354` also reds an imported leg with no grant row, a case the clause does not name.
11. **The floor has no receipt field.** cl-0436 says it is recorded in the receipt. cl-0435's schema 5 list has no floor field, and I found none in dSafePassage's receipt units. research-compatibility said per-kit floors; P37 and cl-0436 say one declaration, and that is the later word.
12. **Runner adapters are unowned in spec.**
    - TOOL-dWitnessedBar-24 `:99` assigns platform runner adapters to unit 9. Unit 9's `[[test_runner]]` (S3) is a test-level runner, and the spec has no platform content.
    - `v2:1873` and `:1879` put the macOS and pwsh adapters on dWitnessedBar, while cl-0436 puts adapters here.
    - cl-0436's "generalizing" also meets a script that refuses to start outside Windows.
13. **`platforms.verify: ci` has no gov Linux job.** The strict preset sets it (`v2:1717`). The clause adds Linux to emitted CI only, and `remote-ci.yml:19-21` argues against Linux for gov.
14. **`remote-ci.yml:15-16` goes stale.** It says no permanent gate grades the file's text. Unit 8's leg, if it covers gov's workflow, ends that. TOOL-dSafePassage-12 `:238` relies on it. Its AC2 also greps a literal `setup-python` pin in that file.
15. **flow-roles `:106`, `:119` is stale.** It places the release cut in Maintain step 6, with the deployer writing notes. `flow-steps.md:788-790` says it is not Maintain's, and cl-0414 says the notes are generated. Unit 23's "release notes for distribution" must be read against that.
16. **The packet's parents are stale.** It renders dTotalRecall, dBoundRoles, dWellOiledMachine, dLinkedLibrary and dFurnishedOrders as "specs done no" (`:155-159`), while their spec folders exist at HEAD. It also omits the surfaces this group needs from dPlacedRequest, dDeclaredLoop, dSafePassage and dOrderedCharter, which are transitive.
17. **Record kinds are named in no spec.** `kit-release` appears in none, and no spec names `record-kind.release` or `record-kind.release-exit`. `layer-memory.md:432-434` is the only home statement.

## (3) Shared interfaces, proposed names

| Interface | Proposed spelling | Between |
|---|---|---|
| Release point | `point.flow.release`, as `[[point]]` in `tools/runtime/points.toml` | 15, 6, 5, dKeptSession |
| Adapter header | `check_adapter_header(row)` in `tools/integrations/adapters.py`, adding `kind`, `witness-source`, `probe`, `fallback`, `cas` | 6, 15, 19, 22 |
| Engine verbs | `read-current <E>`; `promote <E> <sha> --expect <id>`; `rollback <E> <sha> --expect <id>`; `read-back <E> <sha>`; a distinct exit for CAS refused | 15, 6 |
| Lease calls | `unattended.sh --lease acquire run release <E>`, released with no `--as` | 15, dPlacedRequest |
| Exit record | `release-exit`, keyed by SHA, with outcome, E and release record id | 15, 5, 4 |
| Environment keys | `release.env.<E>.engine`, `.verify`, `.production` | 15, 6 |
| Engine values | `release.engine.<engine>.*` | 6, adopter policy |
| Tag reader | `read_release_tags()`, replacing TOOL-dSafePassage-6's stand-in | 3, 7, 25, 18 |
| Cut verb | `govkit.py cut`, with `derive_release_notes(prev, head)` and `check_release_notes` | 3, 18, 23 |
| Action pins | `tools/integrations/ci/action-pins.toml`, `[[action]]` name, sha, tag | 8, 26, dSafePassage-12 |
| Emitter | `ci_emit.py render` and `check`, with a floor token substituted at emission | 8, 26 |
| Floor in receipt | `python_floor`, in schema 5 | 26, 25, 10, 21 |
| Platform runners | `point.flow.platform-runners`, rows `windows-gitbash`, `linux` | 26, 8, 3 |
| Per-release verdict | a platform row on the `kit-release` notes | 26, 3 |
| Import reader | `read_job_ruling(census_record, job)` | 19, dLinkedLibrary |
| Landing record | whatever unit 1 mints; 3 reads it, and 15 reads its green SHA | 1, 3, 15, 13 |

## (4) Order constraints

**Within this build:**
- 1 before 3, since the notes need landing records.
- 15 before or with 6. The point, verbs and runner come first.
- 8 before 26, since the Linux job goes in the templates.
- 10 and 21 before 26, for the factory floor read.
- 25 and 26 agree the receipt field; 25 owns the schema.
- 15 before 5's `deploy.released` wake is real, and 13's `deploy.core` before `release.pick` has a green SHA.
- 3 before 7 and 18, which need tags.

**On parents, none built:**

| Unit | Needs |
|---|---|
| 3 | TOOL-dWellOiledMachine-59, -13, -20; `session-start` registration; TOOL-dSafePassage-6 stand-in |
| 6, 15 | TOOL-dPlacedRequest-1, -16, -18, -11; TOOL-dWellOiledMachine-20, -17, -63; PLAY-dOrderedCharter-16; TOOL-dDeclaredLoop-2 `[[selects]]` and -24; TOOL-dTotalRecall-1, -2; TOOL-dWitnessedBar-11 |
| 8 | TOOL-dSafePassage-11, -12; TOOL-dWitnessedBar-11, and -6 for the owner re-pin any workflow render forces |
| 19 | TOOL-dLinkedLibrary-8, -51; TOOL-dWitnessedBar-6, -11; TOOL-dWellOiledMachine-17 |
| 22 | TOOL-dWellOiledMachine-17, -20, -6; TOOL-dDeclaredLoop-2 |
| 26 | TOOL-dSafePassage-11, -12; TOOL-dWitnessedBar-11, -27; every node on 3.15 (dSafePassage-11 `:128`; this node runs 3.14.5) |

## (5) Forks

**Settled from source, as a recommendation:**
- `release/<E>` calls `--lease` directly and is no cadence row.
- The mirror reads asks through `backlog.py`, not the journal.
- Environment names are policy, not `points.toml`, because that file is overwritten on update and must not name an adopter.

**Not settled from source:**
1. How environment and engine values get catalogue rows, and whether that is a departure record.
2. Gov's workflow: rendered through `[[generated]]`, or a parity leg against the pin file. A render changes the blob `verdict.remote.pin` covers.
3. Who owns `tools/integrations/`, the header factory and `verdict:remote-ci`, given no clause names them.
4. What wakes `release.*` after a build closes under `at-landing`.
5. How `every-landing`, `owner-cut` and `every-session` run: extending TOOL-dWellOiledMachine-59 or a program of this build's own.
6. Whether an imported job's leg re-runs steps locally or reads the job's remote conclusion. A grant and secret reference suggest the second.
7. How "test job" is decided (disagreement 10).
8. Which tracker service, and whether any exists to mirror to.
9. The first tag's baseline, since no previous tag exists.
10. The engine's name, its CAS method and its signature tool. Sources give no tool. A compose and systemd host has no native CAS, so without an adapter-built swap the engine runs only under `deploy.runs: operator`, against the `landing-node` default, and that cross-key check is unowned.
11. Whether gov gains a Linux CI job for `platforms.verify: ci`.

**What I did not verify:**
- gap-tool-11's WSL failures: I did not run WSL.
- Whether `.githooks/pre-push` passes an annotated tag push: I read the refs loop only.
- Anything in adopter trees.
- I grepped the research records and most parent specs rather than reading them whole.
