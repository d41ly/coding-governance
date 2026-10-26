**Serves:** research TOOL-dTotalRecall-1

# dTotalRecall — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns for the re-ground brief
[`2026-10-26-prompt-TOOL-dTotalRecall-1-parents-reground`](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-parents-reground.md),
each copied from its agent transcript. The cross-check record they answer is
[`2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck`](2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck.md).

## Group A, record kinds and the factory (specs 1, 2, 4, 19, 25, 43)

I revised all six Group A specs: 1, 2, 4, 19, 25 and 43. Each one's Status line moved up one rev, stays `DEFERRED` and is dated 2026-10-26, and each gained a §9 line naming the sections moved and the cross-check rows. I refused no row. Two forks are left open for the owner (spec 2 F6, spec 19 F7). Specs 2 and 43 have edits beyond their listed rows, explained under each.

The memory hygiene gate, run over a copy of the index with only these six specs staged, fails only check 9: the build index is owed a render, which `gen_build_index.py --write` fixes. That one is yours, as the brief says. It also lists dBoundRoles/README.md and dKeptSession/README.md as stale. The check 25 "did not grade … READER NOT IN TREE" lines are informational and were already there. I deleted the index copy. Nothing is staged in the real index and nothing was committed.

**TOOL-dTotalRecall-1**, now rev-4, 37193 bytes, rows 2, 4, 5 and 6.
- Sections moved: §2 S2, S3, S9, S11; §3 the external edge; §4 the data model, the writer bullet, the rows table and the alternatives rejected; §6 AC1 and AC8; §8 F1.
- Factory writers: each kind's writer is now the command its owning spec names, or else the factory with `--build`, `--unit` and the kind's field flags. The build run re-grounds each one. The `new probe` example is gone.
- `deviation` now has one row, as a member of `TYPED_RECORD_KINDS`. Its source is now the factory, its writer the factory with its flags, and its hand-written row is gone.
- The `record-kinds` leg is declared through `leg_factory.py`. Its `enforces` holds the `kind.record-kind` row's `binds`, and AC1 checks that.
- F1 now cites TOOL-dPlacedRequest-1:145-146 and PLAY-dOrderedCharter-7:135. It stays RESOLVED, and its two asks are kept as preconditions of the build run's re-ground.

**TOOL-dTotalRecall-2**, now rev-6, 34849 bytes, rows 8 and 9.
- Sections moved: §2 S2 and S9; §3 the external edge; §4 "Minting"; §6 AC5 and AC9; §8 F6, which is new.
- The lease holder is no longer read through `--claims`, which prints five fields and no session. It is read through the verb F6 asks for.
- AC5 now plants the lease on the fixture's bare remote.
- F6 is open for the owner. It recommends (a): ask dPlacedRequest for a read-only holder verb over `read_claims`. The spec says the ask the build run would file.
- **Beyond rows 8 and 9:** S2, S9 and AC9 had to change to stay consistent with spec 1. Now that `deviation`'s writer names the factory, the door accepts that writer as its own, S9 no longer lists `deviation` among the hand-written rows, and AC9 says so.

**TOOL-dTotalRecall-4**, now rev-3, 30336 bytes, row 17.
- Sections moved: §3 the external edge; §4 "The routing region"; §6 AC5.
- The `deviations` row is replaced by one row per member of `TYPED_RECORD_KINDS`, read from the tuple. AC5 checks this against a scratch build holding one record of each typed kind.

**TOOL-dTotalRecall-19**, now rev-6, 35969 bytes, rows 38 and 39.
- Sections moved: §2 preconditions, S8 and S12; §6 AC6, which gains the plant `typed-causeless`; the §7 arm; §8 F7, which is new.
- F7 is open for the owner. It recommends (d): when a typed kind's factory fields hold no `Caused-by`, the cause is read from the record's Serves unit. It also names the asks to the parents the build run would file under (c). Until the owner picks, the unit builds as (d).
- S12 declares the leg with `enforces = ["principle.p35"]`, and AC6 prints it.

**TOOL-dTotalRecall-25**, now rev-3, 18069 bytes, row 45.
- Sections moved: §2 S6, which is new; §3 the external edge; §4 files touched; §6 AC6, which is new; §8 F3, which is new.
- F3 is resolved on rung 1, `RESOLVED (agent, 2026-10-26, delegated)`, citing PLAY-dOrderedCharter-42 S1, S2 and S5. `stream-plan` joins `TYPED_RECORD_KINDS`, the factory's table (with no required field) and the HYGIENE kind list.
- The fence can be a factory row only if it declares no required fields, so S3 alone grades the fence. Whether the landed factory accepts a kind with no required field is unknown until dOrderedCharter builds; if it does not, the build run falls back to (c), where `check_stream_plan` checks the file-name join itself.

**TOOL-dTotalRecall-43**, now rev-4, 49114 bytes, rows 49 and 50.
- Sections moved: §1, §2 S4, S9 and S29; §4 files touched and alternatives rejected; §5 security, observability and risks; §6 AC4, AC9 and AC29.
- I replaced text rather than appending, and cut other prose (the §1 id list, part of the second alternative, three §5 lines) to stay under the cap. That leaves only 38 bytes of headroom.
- S4 and AC4: the writer names the factory and its per-kind flags, not a `new <kind>` verb, and the build run re-grounds the call.
- S29 and AC29: each leg's declaration needs a non-empty `enforces`.
- **Beyond rows 49 and 50:** S9 and AC9 change to match spec 25, which makes `stream-plan` a typed kind. Row 51 had passed it as untyped.

**Things that look wrong or were left alone, in parent specs and in specs outside this group:**
- PLAY-dOrderedCharter-42 S4 refers to the factory's "record writer" for kinds that have no `new` verb. PLAY-dOrderedCharter-7 never names that writer or its flags, but specs 1 and 43 now point at it.
- TOOL-dTotalRecall-2 S1 (lines 39-40) still says the factory has a generic stand-in `build_records.py new <kind>`. That is row 11, marked UNKNOWN UNTIL BUILT and not on the re-ground list, so I left it.
- TOOL-dTotalRecall-1 S3 admits only `root` and `sections` as later columns. F7's recommendation is derived from data, so it needs no new column.

The edited files are in `C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dTotalRecall/spec/`:
- 2026-10-26-spec-TOOL-dTotalRecall-1.md
- 2026-10-26-spec-TOOL-dTotalRecall-2.md
- 2026-10-26-spec-TOOL-dTotalRecall-4.md
- 2026-10-26-spec-TOOL-dTotalRecall-19.md
- 2026-10-26-spec-TOOL-dTotalRecall-25.md
- 2026-10-26-spec-TOOL-dTotalRecall-43.md

## Group B, legs (specs 8, 9, 11, 15, 22, 26, 76)

I've revised all seven Group B specs (8, 9, 11, 15, 22, 26 and 76). No record row was refused, and no fork was added, re-resolved or re-opened.

Each leg is now declared once, as TOOL-dWitnessedBar-11 S1 requires. Each spec names its leg's `enforces` and has an acceptance criterion that reads it. To pick each `enforces` tag I applied TOOL-dWitnessedBar-11 §4 "The enforces rule":
- **Step 1:** a principle whose row in v2's `[enforcement]` table (`dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1813-1862`) names the unit's carried clause.
- **Step 2:** otherwise, the practice whose rule the leg's red reports broken. This is my judgement.
- **Self-test legs:** `practice.verify`, which TOOL-dWitnessedBar-51 S12 gives every self-test leg.

Every spec's Status line is DEFERRED and dated 2026-10-26, and §9 has one new line naming the sections moved, the cross-check record and its rows. In each spec I grepped for the sentence the record row quotes, and it no longer appears.

| Spec | Rev | Rows | Bytes | Sections moved | Leg and `enforces` |
|---|---|---|---|---|---|
| 8 | rev-3 | 25 | 33440 | §2 S13 · §3 Edges · §4 Files touched · §5 testing · §6 AC10 (new) · §9 | `code record` is a `[[gate_leg]]` in `tools/memory-tree/kit.toml`, `["principle.p32"]` (cl-0219 is in P32's row). AC10 reds a declaration with no `enforces`. |
| 9 | rev-3 | 27 | 32117 | §2 preconditions, S4 · §4 Files touched · §6 AC6 · §9 | The `recall floor` guard is edited in its `[[exempt_leg]]` declaration (`tools/govkit/registry.toml:380`), then `leg_factory.py --write` regenerates the manifest. AC6 adds a `leg_factory.py --check` probe. |
| 11 | rev-4 | 29, 30 | 27391 | §2 preconditions, S3, S6 · §4 The row, Inventory, Files touched · §5 testing · §6 AC9, AC10 (new) · §9 | `shape-run records (…)` is a `[[gate_leg]]` in memory-tree's `kit.toml`, `["practice.one-fact"]`. `shape-run` also joins the closed `<kind>` list in `HYGIENE.template.md` and its render in `memory/HYGIENE.md`. AC9 reads the leg and AC10 reads the kind list. |
| 15 | rev-2 | 32 | 21554 | §2 preconditions, S11 · §4 Files touched · §5 risks · §6 AC11 · §9 | The `map (the project map's checks)` leg gets `["practice.derive"]` and `map selftest` gets `["practice.verify"]`. §5 says both guarded legs go red under `core.bypass = never` until TOOL-dWitnessedBar-11 F5 is settled. |
| 22 | rev-4 | 43 | 24042 | §2 S6 · §3 Edges (external bullet) · §4 Files touched · §6 AC7 · §9 | `edge cardinality (…)` is declared in this unit's own pass with `leg_factory.py new --kit playbook … --enforces practice.one-fact`, as a `[[gate_leg]]` in `tools/playbook/kit.toml`. AC7 checks `enforces` and the file that declares the leg. |
| 26 | rev-3 | 46 | 36118 | §2 preconditions, S10 · §3 Edges (external bullet) · §4 Inventory, Files touched · §6 AC14 · §9 | `atlas selftest`'s `[[gate_leg]]` row carries `["principle.p42", "practice.verify"]` (cl-0237 is in P42's row). AC14 checks it. |
| 76 | rev-3 | 58 | 33382 | §2 S16 · §4 Inventory, Files touched · §6 AC10 · §9 | `reads` is written in the `record causes` declaration and rendered by `leg_factory.py --write`. S16 confirms the `enforces` that unit 19's S12 names (Group A's revision gives `principle.p35`) and adds it if absent. AC10 prints it beside `reads` and adds a `--check` probe. |

Three things to check:
- **Spec 8 now puts its leg in a different file.** It used to put its leg row in `tools/govkit/registry.toml`. I moved the declaration to a `[[gate_leg]]` row in `tools/memory-tree/kit.toml`. TOOL-dWitnessedBar-11 S1 says a leg goes in its kit's file when an adopter receives the program, and nothing withholds `code_record.py`. This changes whether adopters get the leg, so please confirm it.
- **The step-2 tags are my judgement.** These are `practice.one-fact` for specs 11 and 22, and `practice.derive` for spec 15. Their clauses (cl-0222, cl-0233 and cl-0226) appear in no `[enforcement]` row. The closing review should check those tags against the clauses they cite.
- **No new internal edges.** I added no edge between dTotalRecall units, such as from 76 to 19, so no spec outside my group needs a matching edge. Specs 8, 22 and 26 only gained text in their existing external consumes-from bullets.

**Hygiene gate:** I ran `check-memory-hygiene.sh --staged` on a copy of the index with only these seven specs staged, then deleted the copy. The only failure is check 9: the build-index render is due for spec 11, and the dTotalRecall, dBoundRoles and dKeptSession READMEs differ from a fresh render. A `gen_build_index.py --write` run in the main loop clears that. Nothing else names these specs. I didn't run the naming lexicon because no new identifiers were added.

**Parent spec that looks wrong:** PLAY-dOrderedCharter-42 S5 and AC5 keep a hand-typed closed `<kind>` list at `tools/memory-tree/HYGIENE.template.md:628-630`. TOOL-dTotalRecall-1 S6 renders the kind list from the registry into a generated region of the same file. Every typed-kind spec, including 11, has to edit the hand-typed list too, which breaks the derive and one-fact rules. An ask for dOrderedCharter could make that bullet part of the generated region.

Files are in `C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dTotalRecall/spec/`:
- `2026-10-26-spec-TOOL-dTotalRecall-8.md`
- `2026-10-26-spec-TOOL-dTotalRecall-9.md`
- `2026-10-26-spec-TOOL-dTotalRecall-11.md`
- `2026-10-26-spec-TOOL-dTotalRecall-15.md`
- `2026-10-26-spec-TOOL-dTotalRecall-22.md`
- `2026-10-26-spec-TOOL-dTotalRecall-26.md`
- `2026-10-26-spec-TOOL-dTotalRecall-76.md`

## Group C, sibling kits (specs 18, 20)

I revised both Group C specs. Each now reads rev-3, has a new §9 line naming the cross-check record's rows, and is under the 49152-byte cap. I refused no record rows. Two of the three forks I left open go further than the brief asked (spec 20's F5 and F6, explained below).

The memory hygiene gate, run with only these two specs staged into an index copy, failed one check: check 9, "render owed under --staged". That needs a `gen_build_index.py --write` render, which is the main loop's job. The same render is also owed for the READMEs of dTotalRecall, dBoundRoles and dKeptSession; the last two were already out of date. Nothing else named either spec. I deleted the index copy and the probe files from `tr-wC/`. I ran no other gate, and the naming lexicon was not run.

## TOOL-dTotalRecall-18
`C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-18.md`
- **Rev:** rev-3. **Bytes:** 31368.
- **Sections moved:** §2 S2 and S3; §3 the external edge; §4 Files touched and Alternatives rejected; §5 error states and testing; §6 AC2 and the new AC8; §7 the `record_kinds.py` arm (new plants `item-inputs` and `roles-unresolved`); §8 F5 and F6; §9; §10.
- **Row 34, `read by`:** a parent already declares a typed input reference. TOOL-dDeclaredLoop-24 §4 "Records at a version" (dl24:144-145) writes record inputs as `<layer tag>:record-kind.<name>@<n>`, and TOOL-dDeclaredLoop-56 S15 applies that to the seeded rows. So `read by` now uses that reference, and a prose input joins nothing.
  - **F5 added:** `RESOLVED (agent, 2026-10-26, delegated)`, (a), rung 1. No ask is needed.
  - **Related fix:** `written by` now spells `returns` as `record-kind.<name>@<n>`.
- **Row 36, reading the roles kit — F6 added, open for the owner, recommendation (a):**
  - (a) A declared `requires_if` row naming `roles` (and one naming `loop`), with `roles_lib` read in process. A parent already does this for the same cycle: TOOL-dDeclaredLoop-9 F2. Memory-tree cannot plain-`require` roles, because roles requires memory-tree (`tools/roles/kit.toml:12`).
  - (b) `ast.literal_eval` plus a roles verb, which would be an ask to TOOL-dBoundRoles-14. A probe at `c8d46e188` showed `READ_KEYS` is not a literal, so `ast.literal_eval` refuses it until dBoundRoles-14 S4's `READ_FAMILIES` lands. `WRITE_FOLDERS` is a literal dict and reads fine. No roles verb prints these values today (`check_roles.py:418-420`, `handoff.py:942-962`).
  - (c) Memory-tree parses the role files itself, which would be a second parser.
  - AC8 is written to (a).
- **Cite update:** at `c8d46e188`, `WRITE_FOLDERS` is at `check_roles.py:101`, not `:99`.

## TOOL-dTotalRecall-20
`C:/projects/coding-governance/.claude/worktrees/silly-jang-ffa5af/memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-20.md`
- **Rev:** rev-3. **Bytes:** 28340.
- **Sections moved:** §2 preamble, S1, S4 and S5; §4 Inventory, Files touched and Alternatives rejected; §5 testing; §6 the new AC8; §7 the `selftest.py` arm; §8 F5 and F6; §9; §10.
- **Row 40, the policy read:** the retag step now reads its key with govkit's own `read_policy_value("memory.legacy-anchors", target)` (TOOL-dSafePassage-9 §4). It reaches it by importing `govkit`, the way `matrix.py:51-52` does, and no longer uses oc19 S8's playbook module.
- **Row 41, S1:** the journal step runs `gen_build_index.py --print-bindings` (`:690`, dispatched at `:8761`) as a subprocess in the target, and counts the `S` rows whose kind is `journal`.
- **Row 41, S4 — F5 added, open for the owner, recommendation (a):**
  - (a) Unit 20 adds a `--print-front-matter-findings` mode to `gen_build_index.py`, a file it already edits.
  - (b) An in-process `importlib` load, stated as an exception, with `govkit.py:3137-3155` as the only precedent.
  - (c) `ast.literal_eval` plus the step's own parse, which would be a second grader.
- **Beyond the record — F6 added, open for the owner, recommendation (a):** S5 calls `derive_anchor`, which lives in the playbook kit's `tag_index.py`. That is the same rule break as row 40, since TOOL-dWitnessedBar-28 S5 says a govkit module imports no playbook module, but the record never listed it.
  - (a) Ask TOOL-dTotalRecall-10 for a verb, `gov_tag.py anchors <path>`.
  - (b) A `requires_if` import, which TOOL-dWitnessedBar-28's own open fork recommends against.
  - (c) An inline copy of the anchor rule.
  - The reviewer may judge this outside the brief's rows. If so, dropping F6 and S5's added clause leaves the rest standing.
- AC8 checks with grep that no step program imports a memory-tree or playbook module, and that the policy read goes through govkit.

## Specs that look wrong
- **TOOL-dTotalRecall-43 S20** (tr43:110-112), Group A's spec: it says the front-matter step "calls" `check_front_matter`, which reads as an in-process call. The cross-check record flags this too. Spec 20's F5 (a) assumes the call goes through the new print mode instead.
- **dl12's example item** (TOOL-dDeclaredLoop-12) (dl12:111) still shows a prose input, `"layer.memory:plan record"`, and an unversioned `returns` (dl12:113). TOOL-dDeclaredLoop-24 F2 handed the `@<n>` form back to unit 12, and dl56 S15 applies it only to the seeded rows, so the example in dl12 itself has not caught up.
