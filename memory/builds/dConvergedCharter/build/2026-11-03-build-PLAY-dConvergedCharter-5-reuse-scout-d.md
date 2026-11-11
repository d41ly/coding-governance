**Serves:** research PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-23

# Reuse scout D — dConvergedCharter

The scout's final return, extracted from its transcript by script, never retyped.

I'm returning findings only; nothing was written in the repository. I ran `reuse_lookup.py` once per behaviour, using `python3` directly because `resolve-python.sh` is a sourced function and returns empty when run as a script. Its shortlists named `tracked`, `surface_paths`, `read_steps`, `derive_pending_steps`, `render_scope_row` and the key readers. I then read the sources behind them. No layer was reported recall-dark.

## Clause table

| Unit | Seam to extend | What already exists | Design lines that decide it | Owned nodes | Product paths | Buildable? |
|---|---|---|---|---|---|---|
| **PLAY-dConvergedCharter-5** (cl-0479, adopters migrated onto the ranked charter and the loop) | **Build nothing new: drive the walk that already exists.** Extend through:<br>• `cmd_update` (`tools/govkit/govkit.py:9381`)<br>• `derive_pending_steps` (`tools/govkit/upgrade_steps.py:1886`) and `run_step_walk` (`:2036`)<br>• the `[[upgrade]]` grammar of `tools/govkit/steps.toml:1-10`<br>Read the adopters through DEPL-dShippedRelease-31 S2 (`read_adopter_rows`). Read "migrated" through DEPL-dShippedRelease-7 S7 (`adopter_reading.py read` returns `steps-pending` through `derive_pending_steps`). Push through DEPL-dShippedRelease-16 (`kits.offer`). | • At HEAD the update walk, the step reader, `[[retired]]` successions (`read_retired` `:890`, `resolve_claim` `:1002`) and the `upgrade-walk` leg (`tools/govkit/upgrade_walk.py`) are built: dSafePassage is CLOSED.<br>• `tools/govkit/adopters.toml:16-25` holds three rows with no `remote`, `branch` or `grant`, so under DEPL-31 S2 none is `registered`. The one at `:20` has no `key`.<br>• The migration content is each parent's own steps: PLAY-dOrderedCharter-31 S4 (adopter rules into `.governance/instructions.toml`), TOOL-dBoundRoles-19 (house files into the overlay), TOOL-dTotalRecall-20, and the loop kit's steps from dDeclaredLoop. | • adopter-instructions `[design]` 125-135, `[scenarios]` 192-208, `[chain]` 210-223<br>• research-adopter-design "Pick"<br>• research-adopter-today §5-6 | none (`policy-key.help.explanation` belongs to item 7, not here) | • `tools/govkit/adopters.toml` (the owner's `register` rows)<br>• no new engine code<br>• `help/kits.md`, `WIRE-INTO-PROJECT.md` (the migration's how-to) | **Waits** on DEPL-dShippedRelease-31 (register), -7 (`kits.adopters`), -16 (`kits.offer`) and -25 (schema 5); PLAY-dOrderedCharter-31; TOOL-dBoundRoles-19; and dDeclaredLoop's loop kit. It also needs the owner to register each adopter's remote. |
| **PLAY-dConvergedCharter-14** (cl-0488, fates join as the exit check) | **Extend selfcheck arm 8**, the registry's join of tracked files against declarations in both directions (`tools/govkit/govkit.py:3415-3453`), with:<br>• `tracked()` (`:344`, `git ls-files -z`)<br>• `surface_paths()` (`:361`)<br>• the `[[exempt]]` rule that reds an empty `why` or a stale path (`:3429-3441`)<br>For "vanished with no row": `step_gate.derive_vanished_members` (`tools/govkit/step_gate.py:219`) and `read_surface_population` (`:155`).<br>For the declined proposal: TOOL-dCalibratedLens-5 S8, the `keep` record keyed `(kind, id)` (`write_keep_record` / `read_keep_records`). | • Arm 8 already reds "tracked path … neither an entry member nor an exemption" and a stale claim. That is this join's exact shape, over a different population and table.<br>• The fates checks in `2026-10-17-…-map.py:240-753` (`FATE_KITS`, `FATE_ROWS`, the 12 fates plants) check the record's own consistency only. fates.md `[check]` 238-260 says the population derivation is "convergence's exit check". | • fates.md `[kits]` 28-43, `[table]` 66-213, `[check]` 238-260<br>• night-pass `[p8-fates]` 430-466 (last line: "dConvergedCharter runs the table's join as convergence's exit check")<br>• shape-reviews-compared 132 (`fates-population`, `declined-retirement`, B only) | none of its own; it reads TOOL-dCalibratedLens-5's `keep` kind | • New `tools/govkit/fates.toml` (proposed): the table as rows with path globs<br>• `fates_join.py` or a new selfcheck arm in `govkit.py`<br>• `tools/gate-legs.json` leg row<br>• `tools/govkit/selftest.py` plants | **The checker can be built now** on HEAD seams: unlisted-file and surviving-guide plants are both red today. **The declined-proposal arm waits** on TOOL-dCalibratedLens-5 S8. **The exit run** ("every part at its fate") waits on every other unit of this build. |
| **PLAY-dConvergedCharter-18** (cl-0492, the cycle walked by key) | **No seam fits at HEAD.**<br>• Probe: `reuse_lookup` for "walk a chain of hops each resolved by a key" returned only generic `key`, `walk`, `resolve*`. `corpus_ids.walk` is a file walker.<br>• `grep -rln "Gov-Act\|Gov-Unit:\|resolve_edge\|record find\|gov why\|caused-by" tools skills .githooks` gets 0 hits.<br>• `tools/runtime`, `tools/loop` and `tools/integrations` are absent, and `tools/playbook/edge_grammar.py` does not exist.<br>Seams to extend once they land:<br>• PLAY-dOrderedCharter-24 (S1 `tools/playbook/edges.toml`, S3 `parse_edge_lines`, S5 `derive_inverse_edges`)<br>• TOOL-dWellOiledMachine-34 S5 `gov why <key>` (`trace.py why`) as the per-hop resolver | Nothing at HEAD. | • memory-plan `[cycle]` 206-229 (14 hops, each with an edge type and a planted site)<br>• `[gates]` "cycle" 382-383<br>• `[chain]` 335<br>• shape-reviews-compared 66 and 267 (`cycle-walk`: "dConvergedCharter walks the cycle by key from a planted build's intake") | none | • New walker, e.g. `tools/memory-tree/cycle_walk.py`, plus its fixture<br>• a leg row in `tools/gate-legs.json` | **Waits** on every hop's build (per hop below). |
| **PLAY-dConvergedCharter-23** (cl-0502, the release asks' join) | **`render_scope_row`** (`tools/memory-tree/backlog.py:1528`) for the `seen` clause.<br>**`derive_content_key`** (`tools/memory-tree/row_grammar.py:1475`) as the intake's key.<br>**The 16-hex SHA-256 key hash** that is inline at `tools/drift-audit/drift_report.py:3777`, which TOOL-dTendedCadence-15 S2 reuses for `<reading>\t<offender key>`.<br>Each half's parent unit:<br>• DEPL-dShippedRelease-15 S10 (`run_release_route` files `release-verify-failed <sha> <E>` via `intake.py file --origin cadence --filer item.release.route`)<br>• TOOL-dTendedCadence-15 S2 (`write_breach_ask`, marker `maintain key <hash>`)<br>• TOOL-dTendedCadence-8 S6/S7 (`derive_event_key`, `write_patch_intake`)<br>• TOOL-dWellOiledMachine-27 S1 (`intake.py file`) | • At HEAD: `render_scope_row`, `derive_content_key`, and the inline hash only.<br>• Both halves are specced and DEFERRED. | • layer-expansions `[design-observability]` 700-713 (line 710)<br>• walk-return-b5 129-134 and 218 (B5-F14)<br>• fold-return-w5 27 and 103 | none | • A shared key function (proposed `tools/lib/filing_key.py`)<br>• its call sites in `tools/integrations/release.py` and `tools/drift-audit/maintain_file.py`<br>• a join fixture case (`release_fixture.py --case verify-join` or the drift-audit selftest) | **Waits** on DEPL-dShippedRelease-15, TOOL-dTendedCadence-15, TOOL-dTendedCadence-8, TOOL-dWellOiledMachine-27 and TOOL-dWellOiledMachine-4. The clause makes both parents build against stand-ins; this unit owns only the joined fixture. |

**Item 18, each hop and the unit that types it** (none is built):
- **Intake:** TOOL-dWellOiledMachine-4 and -27, with S5's `**Caused-by:** <content key>`.
- **Request key:** TOOL-dPlacedRequest-19 S1 (`derive_request_content_key`).
- **`instructs`:** PLAY-dOrderedCharter-24, plus dLinkedLibrary-20 (`feature.<name>` selector).
- **Work order:** TOOL-dBoundRoles-17 (the marker's `item=`, the return's `answers`).
- **Act and session:** TOOL-dWellOiledMachine-32 and -35.
- **Trailers:** TOOL-dWellOiledMachine-33 writes them; TOOL-dDeclaredLoop-23 is the one trailer reader.
- **Landing:** DEPL-dShippedRelease-1 (the landing record).
- **Verdict:** the dWitnessedBar verdict record.
- **`serves` and `caused-by`:** TOOL-dTotalRecall-19 (`read_header_edges`, `check_causes`).
- **Class `caused-by` and `decides`:** TOOL-dLinkedLibrary-22.
- **`part-of` and `implements`:** TOOL-dLinkedLibrary-17.
- **`promoted-from`:** PLAY-dOrderedCharter-14 and TOOL-dCalibratedLens-14 S8.

### Where a record and source disagree

1. **The brief says every earlier chain build is unbuilt.** dSafePassage has 98 specs CLOSED, and its code is at HEAD: `upgrade_steps.py`, `step_gate.py`, `steps.toml`, `upgrade_walk.py`. Item 5's walk and item 14's vanished-member diff are therefore real seams today.
2. **DEPL-dShippedRelease-31 S2** cites selfcheck arm 10 at `govkit.py:3731`. At HEAD it is `:3476-3519`, with the `adopters.toml` load at `:3487`.
   - S3 of the same spec cites `resolve_measurer_currency` at `:612`; HEAD has it at `:682`.
   - DEPL-dShippedRelease-7 S7 cites `resolve_entry_version_at` at `:696`; HEAD has it at `:766`.
3. **The fates record has no path-glob column**, but the clause needs "every path matched by a row's path glob". Its rows are keyed only (Kit, Function).
4. **The fate vocabularies differ.** The clause amends a row "to `kept`". `kept` belongs to the `[kits]` set (kept, optional, absorbed, retired). The `[table]` rows use STAYS, RESHAPED, MERGED and RETIRED. TOOL-dCalibratedLens-5 also uses `kept` as a ledger state.
5. **The `release-verify-failed` producer has no carrier.** TOOL-dTendedCadence-2 hands off "dShippedRelease registers `release-verify-failed`'s producer in `EVENT_PRODUCERS`". No dShippedRelease spec contains `EVENT_PRODUCERS`. TOOL-dTendedCadence-15's non-goal also leaves the stand-in to "whichever unit registers that reading", which is the same uncarried unit.
6. **The two halves spell their keys differently.**
   - DEPL-dShippedRelease-15 S10 keys its ask by the intake's content key of the text `release-verify-failed <sha> <E>`.
   - TOOL-dTendedCadence-15 S2 keys by `sha256("<reading>\t<offender key>")[:16]`, with the text `maintain key <hash> · …`.
   - As specced, one red verify reaches two different content keys, so two intakes are filed. That is exactly the clause's red case.
7. **memory-plan `[cycle]` has no intake hop.** It starts at "charter practice → feature-scoped units", while the clause starts the walk "from a planted build's intake". The intake → request → build hop has to come from TOOL-dWellOiledMachine-27 S5 and TOOL-dPlacedRequest-19, not from `[cycle]`.
8. **No callable `key_hash` exists.** TOOL-dTendedCadence-15 cites "`key_hash` hashes its keys (`drift_report.py:3761-3780`)". At HEAD that is a column name, and the hash is computed inline at `:3777`.

## Shared interfaces

1. **The filing-key hash.** Proposed spelling: `derive_key_hash(kind, key) -> str`, the first 16 hex of SHA-256 over `"<kind>\t<key>"`, in `tools/lib/key_hash.py`.
   - It already exists three times: inline at `drift_report.py:3777`, in TOOL-dTendedCadence-15 S2, and as TOOL-dCalibratedLens-5 S8's `derive_key_hash(kind, id)` factored out of `run_loop_file`.
   - Under the `[reuse]` rule a third instance means one factory. TOOL-dCalibratedLens-5 already spells the name, so keep it and move it to `tools/lib`.
   - Users: item 23 (the reading `release-verify-failed`, key `<sha> <E>`) and item 14 (the keep key of a declined part).
   - Other groups must agree: item 4 (PLAY-dConvergedCharter-4, ratified retirements) and both parent halves.
2. **The offender key of `release-verify-failed`.** Proposed: `<40-hex sha> <E>`, space-separated, as DEPL-dShippedRelease-15 S10's text already spells it. The rendered ask text is then `maintain key <hash> · release-verify-failed over its pin · <sha> <E>` (TOOL-dTendedCadence-15 S2's form). `release.route` should file that same text, not its own. This applies to item 23 and both parent halves.
3. **The fates table's product home and row grammar.** Proposed: `tools/govkit/fates.toml`, gov-internal under the registry's `<prefix>/govkit` exemption as `adopters.toml` is.
   - Rows are `[[part]]` with `id = "<kit>/<function-slug>"`, `kit`, `function`, `fate`, `where`, `decided`, and `paths = [...]`.
   - `paths` takes the globs `surface_paths` reads (`{prefix}/x/**`, plain `*`), resolved with `resolve_prefix_token` as `load_registry` does at `govkit.py:329-331`.
   - Fate set: the `[table]` four plus `KEPT`, as the clause requires.
   - Item 14 owns it. Items 4, 12, 16, 17 and 22 must agree, because each retires a part that has a row.
4. **The convergence population.** Proposed: `tracked(root)` (`govkit.py:344`) filtered to the roots `tools`, `skills`, `.githooks`, `.claude`, `.github`, `help`, `WIRE-INTO-PROJECT.md` and `coding-governance-agents.template.md`, plus every path a fates row names outside them.
   - Item 14 uses it. Item 20's widened exit check (every registered adopter with no step pending) must run beside it, not as a second population.
5. **The ratification and decline record of a part.** Proposed: TOOL-dCalibratedLens-5 S8's `keep` record, `python loop_review.py keep --kind part --id <fates id> …`. No new kind: TOOL-dCalibratedLens-14 F3 already refused one under shared interface S4.
   - Item 14 reads it. Item 4 (another group) writes the proposals it answers.
6. **The adopter row and its migration reading.** Proposed: `read_adopter_rows(root)` and its `registered` flag (DEPL-dShippedRelease-31 S2), plus `adopter_reading.py read --key <k>` with its `steps-pending` field (DEPL-dShippedRelease-7 S7).
   - Item 5 uses them, and item 20 (another group) must read the same field.
7. **The edge-type spellings for the cycle walk.** Proposed: the `type` column of `tools/playbook/edges.toml` (PLAY-dOrderedCharter-24 S1): `instructs`, `follows`, `runs-in`, `made-by`, `serves`, `carries`, `caused-by`, `answers`, `decides`, `promoted-from`, `part-of`, `implements`, as memory-plan `[cycle]` spells them. Hop rows should name these, never prose. This is item 18's interface with dOrderedCharter.

## Proposed build order

1. **Item 14's join engine and its plants first.** It needs only HEAD seams (`tracked`, `surface_paths`, arm 8's pattern, `derive_vanished_members`). Every retirement unit in this build then has a population check to land against.
2. **The `derive_key_hash` move to `tools/lib`.** It is the primitive item 23 and item 14's decline arm both call, and the third copy has to be absorbed before either is written.
3. **Item 23, once DEPL-dShippedRelease-15 and TOOL-dTendedCadence-15/-8 land.** The join fixture is meaningless until both real halves exist, and it is cheap once they do.
4. **Item 14's declined-proposal arm, once TOOL-dCalibratedLens-5 S8 lands.** It reads the `keep` record and nothing else new.
5. **Item 5, after every parent build has shipped its upgrade steps and the owner has registered the adopters.** Migration is just running the walk that exists, and its exit reading feeds item 20.
6. **Item 14's exit run.** "Every part at its fate" can only be green after every other retirement, fold and migration unit of this build.
7. **Item 18 last.** The clause makes it the acceptance "once every hop's build has landed", so it is the final proof over everything above.
