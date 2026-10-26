**Serves:** research TOOL-dPlacedRequest-1

# dPlacedRequest — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns that revised the specs the cross-check record
[`2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck`](2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md)
names, each copied from its agent transcript. Group A revised specs 1, 2, 3, 4 and 5; B 6, 7, 9, 21 and 34, under the brief `../prompts/2026-10-26-prompt-TOOL-dPlacedRequest-1-parents-reground.md`.

## Group A

All five Group A specs are revised: 1, 2, 3, 4 and 5. The quoted parent text bore out every row, so none is refused. All five stay `DEFERRED`, each has a new §9 line citing the cross-check record and its row numbers, and each is under the 49152-byte cap.

The hygiene gate (`--staged`, over an index copy holding only these five specs) has one finding. It is check 9, a build-index render owed for `memory/LIVE.md` and `memory/builds/dPlacedRequest/README.md`. Only `gen_build_index.py --write` cures it, so it is yours to run. Its drift list also names two dWitnessedBar files, from that build's existing working-tree edits. I deleted the index copy and the `pr-wA` scratch folder; the real index has nothing staged. Group B's writer is editing specs 6, 7, 9 and 21 at the same time. I checked that spec 7 S8 still adds `probe` only to role rows whose outcomes are a list, which spec 3's F7 relies on.

**TOOL-dPlacedRequest-1** (row 2): rev-5, 40418 bytes.
- **Sections moved:** §2 S8, §4 "The witness under `progress`", §6 AC4, §8 F5 and F8.
- **Change:** the witness is now any recorded transition of the build, read from whichever channel `transitions.record` makes the source. That is the trailer when `trailer` is selected, and otherwise the `-transition-<n>.md` record the commit adds. With `micro-format` alone, nothing renews.
- **AC4:** gains a case with `transitions.record` planted to `["log"]`.
- **F5:** re-resolved, `RESOLVED (agent, 2026-10-26, delegated)`, rung 1, naming dl3 S4 and S7. Its earlier pick, the trailer alone, never renews under `["log"]`.
- **F8 (added):** `RESOLVED (agent, 2026-10-26, delegated)`, rung 3. The bash driver reads the selected channel itself with two `git` calls. The rejected option was asking dl3 for a `read` verb on `read_transitions`.

**TOOL-dPlacedRequest-2** (row 5): rev-5, 30789 bytes.
- **Sections moved:** §2 S8 and S12, §3 Edges, §4 Inventory and Files touched, §6 AC12 (new), §7.
- **Change:** the record serves as `card <anchor id>`. `card` joins `TYPED_RECORD_KINDS` and the HYGIENE kind list, and no `new card` door is claimed.
- **AC12:** `gen_build_index.py --print-bindings` prints an `S` row of kind `card` and no `A` row.
- **§7:** gains `memory hygiene`, `kit/dogfood doc parity`, `recall floor` and `recall floor arms`. Adding `memory/HYGIENE.md` to Files touched trips those legs' guards.
- **Forks:** none.

**TOOL-dPlacedRequest-3** (rows 13, 15, 20, 22): rev-4, 32927 bytes.
- **Sections moved:** §2 S1, §3, §4 "The rows", "The placing route table" and "The claim's outcomes", §5, §6 AC3 and AC6, §8 F7 to F9, §10.
- **Row 13:** `probe` now sits on `item.entry.orient` only. `item.entry.place` keeps the `dispositions` reference, and its probe route lives in its body (unit 4 S6's `place`). AC3 checks orient's set.
- **Row 15:** the owner row's Body cell names the factory's flags, with the call re-grounded on the landed factory.
- **Row 20:** §3 now states the `[[fixed-row]]` trigger mismatch.
- **Row 22:** the `awaiting` self-route cannot take a `draws` cause, because it is contention and clause `cl-dClosedLoop-0115` says contention never draws on the budget. AC6 gains a cut-`deadline` case and states what the built tree prints until the ask lands.
- **F7 (added):** `RESOLVED (agent, 2026-10-26, delegated)`, rung 1: no `probe` on `item.entry.place`.
- **F8 (added):** OPEN for the owner. The recommended ask is on TOOL-dDeclaredLoop-24 §4 "The schema" and §8 F4: re-word the trigger to "when dWellOiledMachine declares it".
- **F9 (added):** OPEN for the owner. The recommended ask is on TOOL-dDeclaredLoop-33 S4 and §4 "Counted and owner edges": set aside an edge that carries `deadline` and `on-deadline`.
- **Grep note:** for rows 20 and 22, the grep still prints the quoted line. The `No entry.intake row` sentence stays true and the correction follows it. The `awaiting` table row stays as designed, because its fix is F9's ask.

**TOOL-dPlacedRequest-4** (row 31): rev-4, 30264 bytes.
- **Sections moved:** §2 S10 (new, with a `**Readers:**` line), §4 Files touched, §6 AC11 (new), §7.
- **Change:** the leg `loop placement fixtures` carries `enforces = ["principle.p22"]`. P22's v2 `[enforcement]` row names this unit's own clause `cl-dClosedLoop-0123` (architecture-v2.md:1844), so no fork was needed. Units 5 and 10 ride the same leg.
- **Pending list:** Files touched gains `tools/playbook/core-pending.txt` for a stale `principle.p22` row, where one exists. §7 gains `playbook render selftest` and `govkit acceptance matrix`, the legs that path's guard trips.
- **Forks:** none.

**TOOL-dPlacedRequest-5** (row 32): rev-4, 22932 bytes.
- **Sections moved:** §2 S4, §3, §4 "The flow", §6 AC4, §10.
- **Change:** S4 passes the factory dl16 S4's flags, the record serving as `disposition <first unit id>`, with no `new disposition` door. AC4 checks the binding and notes that its call is re-grounded on the landed factory.
- **Forks:** none.

**Parent specs that look wrong:**
- **dl16:185 (AC3)** still spells `python build_records.py new disposition …`, while S4 (dl16:52-56) and §9 (dl16:249) say no such door is claimed. S4 says the build run re-grounds AC3's call, but as written the AC reads like a claimed door.
- **dl24:136 and its §8 F4** wait for dPlacedRequest to declare `entry.intake`, which dWellOiledMachine declares. As written, that floor item's fixed row never arms (spec 3 F8).
- **dl33 S4 and §4 "Counted and owner edges"** give no exemption for a wait edge. Any non-owner contention self-route on `awaiting` reds `counted`, and the clause forbids drawing on the budget for one (spec 3 F9).
- **The cross-check record** (not a parent): its change text for row 31 cites "`cl-dClosedLoop-0120`'s sibling clause". The `[enforcement]` table names spec 4's own clause `0123` directly, under P22.

Files revised, in `memory/builds/dPlacedRequest/spec/`:
- `2026-10-25-spec-TOOL-dPlacedRequest-1.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-2.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-3.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-4.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-5.md`

## Group B

I revised all five group B specs (6, 7, 9, 21 and 34) against dDeclaredLoop at `783f1ad3a` and dOrderedCharter at `462d20f35`. I re-read both sides of every row before editing, and none needed refusing. The hygiene gate, run over an index copy holding only these five specs, names none of them. The one finding left is check 9: the build index needs a fresh `gen_build_index.py --write` render (`memory/LIVE.md`, the dPlacedRequest and dWitnessedBar READMEs), which is yours to run. I didn't run the naming lexicon, because the revisions mint no new names. The index copy is deleted, the real index has nothing staged, and nothing was committed.

For each answered row, the brief's grep for the quoted sentence prints nothing or only the corrected sentence. Every status stays `DEFERRED`, dated 2026-10-26, with one new §9 line.

| Spec | Rev | Bytes | Rows | Sections moved |
|---|---|---|---|---|
| 6 | rev-3 | 16402 | 39 | §2 S3 · §4 The check, in order · §5 · §6 AC4 · §8 F3 · §9 |
| 7 | rev-4 | 31916 | 45, 46, 48 | §2 S6, S9, S10 · §3 Edges · §4 The records, Inventory, Files touched · §6 AC7, AC10, new AC12 · §9 · §10 |
| 9 | rev-3 | 25014 | 58, 59 | §2 S3 · §4 Migration, Files touched · §6 AC1, AC3, AC5, AC7 · §9 |
| 21 | rev-5 | 30186 | 72, 73, 78 | §2 S6, S8 · §4 Inventory, Files touched · §6 AC1, new AC8 · §8 F6, F7 · §9 |
| 34 | rev-10 | 48777 | 78, 80 | §2 S31 · §6 AC31, AC34 · §9 (edited in place, nothing appended) |

What changed in each:
- **Spec 6:** with no namespace registry, the namespace check now prints `unarmed` and the run passes, following dl12 S4. AC4 now expects exit 0, and turning the registry back on still fails a misspelt unfold word.
- **Spec 7:**
  - `probe.points` is now a set row with `empty = "allowed"` and default `[]`, and AC10 reads that.
  - `probe` and `probe-trigger` serve as their own kinds and join `TYPED_RECORD_KINDS` and the HYGIENE kind list. The spec claims no factory door, and AC7 adds the `--print-bindings` check. Files touched gains `tree_lib.py`, the HYGIENE template and its render, and `core-pending.txt`.
  - The leg carries `enforces = ["principle.p31"]`, because P31's `[enforcement]` row (v2:1853) names this spec's clause `cl-dClosedLoop-0125`. AC12 checks it.
- **Spec 9:** S3 says `pockets` shows a unit only once its commit is `HEAD`, and the AC1, AC3 and AC5 plants commit `up`'s write first. Migration and Files touched now name `.governance/policy.json`: gov regenerates it in its own commit after the step's, and on an adopter the landing does. AC7 says the fixture holds no mirror.
- **Spec 21:** S6 names the ratification record, served as `disposition <unit id>` with id `<FAMILY>-<slug>-1`, which F6 recommends. It names the factory's flags and claims no door. AC1's plant writes `…-TOOL-dFixPatch-1-disposition-1.md`. The leg carries `enforces` with F7's tag, and AC8 checks it.
- **Spec 34:** S31 and AC31 now require `enforces` on both legs, pointing at unit 4 S10 and unit 21 S8. AC34's grep narrows to `resolve_kit_dir("memory-tree"` and expects one line, in `loop_lib.py`'s loader.
- **Specs 7 and 21:** the "delete the stale pending row" sentence made hygiene check 25 fail, so each gained the **Readers:** clause dl17 S8 uses.

**Forks:**
- **Spec 6 F3, added.** It is marked `RESOLVED (agent, 2026-10-26, delegated)`, (b), on rung 1 under dl12 S4 and AC7.
- **Spec 21 F6, added and open for the owner.** It asks what unit id the ratification record carries before the patch build has a spec. Recommendation: (a) `<FAMILY>-<slug>-1`. The other option the brief offered, ratifying after the first spec exists, is out, because clause 0501 is "seen red on a planted patch under `owner` reaching Design unratified" (v2:1770). The ask the build run would file is for dl16 S4 to state that id.
- **Spec 21 F7, added and open for the owner.** It asks which principle `loop claim fixtures` enforces, since no v2 `[enforcement]` row names `cl-dClosedLoop-0501`. Recommendation: (a) `principle.p39`.

**Parent specs that look wrong:**
- **dl6 S4.** The `new policy-key` flags (dl6:65-66) have no way to set `empty`, yet dGroundRules-1 requires it on every set-valued row (dGR-1:126, :162-163). So `probe.points`, or any set key, can't be written whole through the factory. Spec 7 S9 notes this and leaves it to the build run.
- **dl16 S4.** It names the record by `<unit id>` but gives no id for a record written before the build has a spec. dl3 gets around this for transition records by holding pre-spec moves as pending and back-filling them (dl3 F2, AC7). A ratification that gates Design can't wait like that, and hygiene check 21 fails any Serves id no spec defines. This is spec 21's F6.

**Two things to check:**
- **Spec 34's size.** It was already 48198 bytes before this pass, above the 48128 that unit 52 AC9 allows it, and is now 48777. That is still under the 49152 cap. Its edge to unit 59 says unit 59 cuts it if over 48128.
- **Spec 34 cites group A's work.** S31 points at unit 4 S10, which group A's writer added during this pass. Confirm it is still there once their work lands.

The revised specs are in `memory/builds/dPlacedRequest/spec/`:
- `2026-10-25-spec-TOOL-dPlacedRequest-6.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-7.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-9.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-21.md`
- `2026-10-25-spec-TOOL-dPlacedRequest-34.md`
