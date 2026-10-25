**Serves:** research TOOL-dWitnessedBar-1

# dWitnessedBar — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns that revised the specs the cross-check record
[`2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck`](2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck.md)
names, each copied from its agent transcript. Group A revised specs 1, 8, 11, 14, 25 and 51; B 3, 6, 12, 15, 23 and 56; C 16, 18 and 28, under the brief `../prompts/2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md`.

## Group A

I revised all six Group A specs. None of them is refused, and no record row was refused. Each spec stays DEFERRED and is under the 49152-byte cap. Each now has its rev bumped, a §9 line naming the cross-check record and its rows, and every now-false sentence replaced where it stood.

I ran the memory hygiene gate (`--staged`) over an index copy with only these six specs staged. Check 12, the spec-shape check, passed for all six. The only failure is check 9: the build index is stale in `memory/LIVE.md` and `memory/builds/dWitnessedBar/README.md`. Only `gen_build_index.py --write` fixes that, so I left it for you. I deleted the index copy and my probe files, staged nothing in the real index, and committed nothing. I did not run the naming lexicon, because these revisions mint no new names.

| Spec | Rev | Bytes | Rows | Sections moved | Forks |
|---|---|---|---|---|---|
| 1 | rev-4 | 27181 | 2 | §2 S4 · §3 Edges · §4 Inventory, Files touched · §6 AC6 (new) · §7 · §10 | none |
| 8 | rev-3 | 27729 | 18 | §2 S3 · §3 Edges · §4 Inventory, Files touched · §6 AC8 (new) · §7 · §8 F2 · §10 | F2 re-resolved |
| 11 | rev-3 | 33892 | 24, 29 | §5 risks · §6 AC10 (new) · §8 F2, F5 (new) | F5 open for the owner |
| 14 | rev-5 | 29787 | 41 | §2 S5 · §3 Edges · §4 The widen route, Inventory, Files touched · §6 AC11 (new) | none |
| 25 | rev-3 | 25103 | 77 | §2 S5, S6 · §3 Edges · §4 Inventory, Files touched, Alternatives rejected · §6 AC10 (new) · §7 · §8 F1 · §10 | F1 re-resolved |
| 51 | rev-4 | 48905 | 100 | S7 · AC4, both replaced in place | none |

**Specs 1, 8, 14 and 25: the four record kinds**
- Each record now serves as its own kind: `gate-health`, `flake`, `widen` and `leg-tail`. Each spec adds its kind to `TYPED_RECORD_KINDS` and to the HYGIENE kind list, using dDeclaredLoop's rev-3 wording.
- Each lists `tools/memory-tree/tree_lib.py`, the HYGIENE template and its render `memory/HYGIENE.md` under Files touched.
- Each gains a criterion that runs `gen_build_index.py --print-bindings` and expects an `S` row of the kind and no `A` row.
- Each states the flags it passes the factory and claims no `new <kind>` door. In specs 1, 8 and 25 the writer lives in a different kit from the factory (drift-audit or run-gates against memory-tree), so it runs the factory as a subprocess. Spec 14's writer is in the same kit.
- The render `memory/HYGIENE.md` trips three non-broad guarded legs: `kit/dogfood doc parity`, `recall floor` and `recall floor arms`. I added them to the §7 leg lines of specs 1, 8 and 25; spec 14 already named them.
- Spec 8: the hand-off of a `journal` binding to unit 51 is gone. Spec 1's hand-off to unit 51 is reworded the same way.

**Spec 51**
- S7 now says the flake and gate-health records serve as their own kinds, which specs 8 and 1 join. AC4 checks for `S` rows of kind `flake` and `gate-health` and no `A` row.

**Spec 11**
- §5 risks states the interaction: once every leg carries `enforces`, `core.bypass = never` turns red every leg that also carries a `guard`. That is 71 of gov's 142 legs, a figure I measured myself.
- The new AC10 runs oc7's `bypass-never` plant, then `core.py meta-check` in a scratch clone with `never` committed. Its count is derived when it runs.
- F2's precedent is re-cited to `TOOL-dDeclaredLoop-6`, with oc7:133 kept as the source of the kind's name. Its mark is unchanged.

**Forks**
- **Spec 8 F2:** re-resolved on rung 1, naming oc42 S2, and marked `RESOLVED (agent, 2026-10-26, delegated)`. Option (a) is restated as the factory entry plus its `TYPED_RECORD_KINDS` and HYGIENE members, still with no `kinds.toml` row. The rev-2 "factory only" reading is ruled out by oc42 S2.
- **Spec 25 F1:** re-resolved on rung 1, naming oc42 S2, S3 and S5, and marked `RESOLVED (agent, 2026-10-26, delegated)`. The pick is still (a), now served as `leg-tail`; the `journal` binding is ruled out by oc42 S3.
- **Spec 11 F5 (new, open for the owner):** which legs count as core under `never` once every leg carries `enforces`. The options are:
  - (a) keep oc7's rule as it stands;
  - (b) ask dOrderedCharter to narrow it;
  - (c) give `enforces` only to unguarded legs, which oc7 S3 turns red.
  
  I recommend (b), because under (a) no repository that guards its legs can keep `never` green. The ask the build run would file in dOrderedCharter's `BACKLOG.md`: "narrow the core-leg predicate `core.bypass = never` reads (PLAY-dOrderedCharter-7 S10) to fewer than every leg carrying `enforces`". Until the owner picks, the unit builds as (a), and AC10 observes that.

**Parent specs and records that look wrong**
- **The cross-check record (row 29 evidence):** it cites `TOOL-dDeclaredLoop-6.md:226` for `kind.policy-key`. At `783f1ad3a` the spelling is at `:243`, which is the line spec 11 now cites.
- **oc7 (S3 against S10):** S3 turns red any leg with no `enforces`, so eventually every leg carries one. S10 treats every such leg as core under `never`. Together they turn red every guarded leg under `never`. This conflict is in the parent, and wb11 only reaches it; F5 holds it.
- **Spec 25's authority:** F1 had rejected option (b) because it edits a governance carrier the clause does not name. Option (a) now adds one member to HYGIENE's closed kind list. I treated that as oc42 S5's own path for every typed kind, as dDeclaredLoop's units do. If the owner reads it as a carrier edit needing the `may:` grant, F1 needs another look.
- **Spec 11 §10 (outside my rows, not edited):** it says the factory imports govkit's `read_descriptors` through `resolve_kit_dir`. That looks like a sibling-kit import from run-gates into govkit. wb45 S2 later restricts `leg_factory.py` to the standard library and `regen`.
- **Spec 51 §4 Evidence (not edited):** it cites `memory/HYGIENE.md:626-629` for the closed kind list. In the current render the list sits at about 628-630.

Files, all under `memory/builds/dWitnessedBar/spec/`:
- `2026-10-25-spec-TOOL-dWitnessedBar-1.md`
- `2026-10-25-spec-TOOL-dWitnessedBar-8.md`
- `2026-10-25-spec-TOOL-dWitnessedBar-11.md`
- `2026-10-25-spec-TOOL-dWitnessedBar-14.md`
- `2026-10-25-spec-TOOL-dWitnessedBar-25.md`
- `2026-10-25-spec-TOOL-dWitnessedBar-51.md`

## Group B

I've revised all six Group B specs (3, 6, 12, 15, 23, 56) against dOrderedCharter at `462d20f35` and dDeclaredLoop at `783f1ad3a`. Each design is unchanged apart from its assumptions about the two parents. All six stay `DEFERRED`, carry the date 2026-10-26, and have a new §9 line naming the cross-check record and its rows. I refused no rows: I re-read both sides of every row, and the parents bear each one out.

Nothing is staged in the real index and nothing is committed. The hygiene gate, run over an index copy holding only these six specs, fails only check 9: the build index needs a `gen_build_index.py --write` render. That is yours to run. The same run also lists `memory/LIVE.md`, `memory/builds/dWitnessedBar/README.md` and `memory/builds/dPlacedRequest/README.md` as stale. The index copy has been deleted. I did not run the naming lexicon, because these revisions mint no new code identifier.

#### Per spec

**TOOL-dWitnessedBar-3**: now rev-3, 32681 bytes, rows 4 and 6.
- **Sections moved:** §3, §3 Edges, §4 The routes, §5, AC5, §8 F6.
- **Owner exception (row 4):** narrowed to a core gate's red, matched by principle and part. A leg is core when its `enforces` is non-empty. Under `owner-only-expiring` no exception is admitted until PLAY-dOrderedCharter-15's check lands, and under `none` never.
- **Loop read (row 6):** `judge` reaches the loop kit by subprocess, through the inline `resolve_kit_dir` block that `tools/run-gates/measure_legs.py:116-153` already carries. AC5 adds a no-loop-kit case, a missing-verb case, and `git grep -nwE '(import|from) (loop_lib|policy)' -- tools/run-gates`, which prints nothing today.
- **Fork added:** F6, open for the owner, recommending (a): ask dDeclaredLoop for `loop_lib.py items --tag <tag>`.
- **Beyond the row:** rev-2 also had `judge` import dGroundRules' `resolve` in process. The brief's sibling-kit rule names policy modules, so I moved that read to a subprocess call of `policy.py get verdict.red-route`. The record has no row for this.

**TOOL-dWitnessedBar-6**: now rev-4, 30282 bytes, row 13.
- **Sections moved:** S9, AC8.
- `--staged` reads no trailer. It refuses every agent-staged change to an `OWNER_ONLY_KEYS` key under every value of `policy-file.guard`, naming the key, before the value's rule. The trailer stays with `--push-range`.
- AC8's fixture sets `policy-file.guard = "agents-with-reason"` and stages the change record and the DECISIONS row, so only `OWNER_ONLY_KEYS` can refuse.
- No fork.

**TOOL-dWitnessedBar-12**: now rev-3, 26280 bytes, row 37.
- **Sections moved:** §3, §4 The tag rule, §8 F5.
- The rename or retirement path is named as unowned, and oc15 S9's `extract_change_records` is named only as the reader of retired rows.
- **Fork added:** F5, open for the owner, recommending (a): ask that oc15 S7's `new change` door accept a `leg.*` tag in `Unit`. Option (b) is the hand-off to unit 11's leg factory.

**TOOL-dWitnessedBar-15**: now rev-6, 26018 bytes, rows 44, 45 and 46.
- **Sections moved:** S6, §4 The item, AC8, §8 F4, §8 F5.
- **Step (row 44):** `step = "step.test"` is gone, and the row is declared as an adopt-program item outside the five steps.
- **Layer (row 45):** `inputs` now names `layer.flow`. It is a core row: oc16 S1 lands the optional `layer.flow.leg-packs`, and oc16 S3 says an optional row's `of` must name a core row.
- **Returns (row 46):** `returns = "none"`, pending F5.
- AC8 now runs `python loop_lib.py --check`, and records `NOT OBSERVED` while F4 or F5 has not landed.
- **Forks added:** F4, where adopt items are declared, open, recommending (a): ask dDeclaredLoop to admit `program = "adopt"` in place of `step`. F5, the `returns` value, open, recommending (a): ask dDeclaredLoop to admit `returns = "none"`.

**TOOL-dWitnessedBar-23**: now rev-3, 23568 bytes, row 69.
- **Sections moved:** S7, AC6.
- S7 re-keys `[item.routes]` in the same edit that changes the outcomes, each key keeping its old target.
- AC6 now also prints the sorted route keys and requires `python loop_lib.py --check` to exit 0. I ran the `python -c` part on a scratch fixture and it printed the expected line.
- No fork.

**TOOL-dWitnessedBar-56**: now rev-4, 28836 bytes, row 98.
- **Sections moved:** S18, AC16.
- AC16 now checks unit 6 S9's key-level refusal under `agents-with-reason`, not a trailer check. Its "red when" also covers a refusal that names only the path.
- No fork.

#### Problems for you to route

- **TOOL-dWitnessedBar-43, outside my group:** wb43:161-162 (AC3) still reads `--staged` "with no `Gov-Policy:` trailer". That is the same defect as rows 13 and 98, and the record has no row for it.
- **TOOL-dWitnessedBar-15, not edited:** `allowance = "the registered homes"` may fail dl9's check, which requires one word of `roles_lib.WRITES`. That constant does not exist in `tools/roles/roles_lib.py` today, so this stays unknown until built.
- **Parent spec that may be wrong:** dl12:80-81 says adopt items are owned by dLinkedLibrary, but flow-steps.md:713 names dWitnessedBar as `test.seed`'s owner. Spec 15's F4 takes flow-steps' owner.

#### Files

- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-3.md`
- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-6.md`
- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-12.md`
- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-15.md`
- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-23.md`
- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-56.md`

## Group C

All three Group C specs are revised. No record row was refused: I re-read both sides of rows 49, 59, 85, 86 and 87, and the parents' text backs each one. The hygiene gate, run over a scratch index with only these three specs staged, now flags only check 9. That is the build-index render (`memory/LIVE.md`, `memory/builds/dWitnessedBar/README.md`, and `memory/builds/dPlacedRequest/README.md`, which was already stale). That render is yours: `python tools/memory-tree/gen_build_index.py --write`. I deleted the index copy and my own scratch files, staged nothing into the real index, and committed nothing.

On its first run the gate also failed check 25, on spec 16's S6 by-name list: `owed_rows.py` is not in the tree yet, and I had listed the `baseline.txt` new name as a reader. I fixed it with the `READER NOT IN TREE` escape and a reason. Check 25 now prints only its "did not grade … READER NOT IN TREE covers it" note.

#### TOOL-dWitnessedBar-28 (leads Group C)
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-28.md`
- **Rev:** rev-3, 2026-10-26, DEFERRED. **Bytes:** 39884.
- **Sections moved:** §2 S4, S5, S8, S12; §3 Edges (the external line); §4 The plants (four new rows: `exclude-at-head`, `unborn-head`, `stale-modes`, `no-playbook-kit`) and Inventory; §5 security, risks, testing; AC2, AC3, AC4, and new AC13 to AC15; the §7 New arm `covers`; §8 F6 and F7; §9; §10.
- **What S5 now says:**
  - `instructions.exclude` is read at the target's `--rev HEAD` through oc35 S5's `policy_reader`. Exit 2 refuses the composition; an unborn `HEAD` makes no read and passes `[]`.
  - The composer is reached only by subprocess. The governing composition is unit 33's `pins.py drift` row pass, so the kind is composed once.
  - Stale and orphaned patches follow oc35 S7 and S8 and oc33 S3 under `order`, `warn` and `refuse`. Each held or orphaned patch files an order through `write_row_order`.
- **Forks added, both OPEN for the owner:**
  - **F6:** which composition governs, and which verb reaches it. Recommendation: (a), the drift verb governs. That needs one ask of dOrderedCharter covering three changes: the drift verb takes a kind's gov rows from its caller and prints the composed rows; `cmd_apply` runs it too; and `overlay_rows.py` gets a verb that prints rows, which S8 needs. The alternatives are a `compose` verb (the same ask as TOOL-dDeclaredLoop-26 F5) or a `requires_if` row.
  - **F7:** the departure "no refusal withholds another leg", now against oc36 S7. Recommendation: (a), ask that a row-level `check_rows` finding hold only that overlay row. AC3 and AC4 are written to (a), and state what (b) would observe instead.
- **Already-resolved forks:** none re-resolved. **Rows refused:** none.

#### TOOL-dWitnessedBar-16
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md`
- **Rev:** rev-4, 2026-10-26, DEFERRED. **Bytes:** 39542.
- **Sections moved:** §2 S6 (its Readers gain `tools/run-gates/owed_rows.py` through oc50 S2's leg-removed population and its `--selftest`); §4 Files touched; §5 testing; new AC11; §7, whose leg line gains `run-gates canary` (the leg that runs the probe's self-test, per oc50's New arm); §9.
- **AC11:** after the rename, `owed_rows.py --selftest` exits 0. A scratch-clone run of `--base HEAD` on a removed leg must print an `owed —` line naming `memory/map/baseline.txt`.
- **Forks:** none added or re-resolved. **Rows refused:** none.

#### TOOL-dWitnessedBar-18
`memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-18.md`
- **Rev:** rev-3, 2026-10-26, DEFERRED. **Bytes:** 21446.
- **Sections moved:**
  - §2 S5 gains `positional.py seed` and `pin`, the `positional-*` plants under `gov_tag.py --fixture`, and `instruction_units.py fixture --plant legacy`.
  - §4 Files touched lists `gov_tag.py` and `instruction_units.py`.
  - §5 testing.
  - New AC7: the plants exit as the parents' criteria state, each written list opens with its `# ledger · <population>` header, and the `tags positional selftest` argv exits 0.
  - §7 adds `tags positional selftest` to the leg line, with a note that oc26 S7 lands it.
  - §9.
- **Forks:** none. **Rows refused:** none.
- **Check for the main loop:** `tags positional selftest` is not in today's `tools/gate-legs.json`. `check-spec-tokens.py` counts a DEFERRED spec as terminal and does not grade it, so this should only matter once the spec goes live.

#### Parent specs that look wrong
- **oc33 S7** (with oc35 §4's "Orders return as data through unit 33's drift verb"): it never says where the row pass gets a kind's gov rows, or that its JSON carries the composed rows. Any consumer of a row kind outside the playbook kit needs both. For gate legs, only govkit knows the selected kits' legs.
- **oc36 S7:** "a finding refuses the composition" means one bad patch withholds every row of that kind. For legs, that brings back the withheld manifest of gap-test-21 (F7).
- **oc35:** neither `compose_rows` nor `read_overlay_rows` has a CLI verb, though every kind's consumer outside the playbook kit needs one. dDeclaredLoop-26 F5 makes the same ask.
- **oc26 S2 and AC1:** "the list is never held as a count" and "Red when: the seed writes a count" may clash with the ledger row's count field of `1` (wb18 S2) once the `positional-seed` plant asserts the row's shape. The parent's own build run should look at this.
- **Not a parent, outside Group C:** wb45 S2 has `leg_factory.py` load govkit in process (`load_govkit`). oc33 S7 says "a kit never imports govkit", so wb45 may be the next mismatch of the same kind.
