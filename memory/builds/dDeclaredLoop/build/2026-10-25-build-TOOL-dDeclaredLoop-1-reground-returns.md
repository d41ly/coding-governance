**Serves:** research TOOL-dDeclaredLoop-1

# dDeclaredLoop — the re-ground writers' returns, verbatim

The `gov-spec-writer` returns that revised the specs the cross-check record
[`2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck`](2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md)
names, each copied from its agent transcript. Group A revised specs 1, 3, 6, 16, 17, 22, 46 and 56; B 24, 25, 26, 27, 28 and 33; C 2, 4, 5, 12, 18 and 34, under the brief `../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md`.

## Group A

All eight Group A specs are revised. The memory hygiene gate, run over an index copy holding only these eight specs, names none of them. It still fails check 9, but only because `memory/builds/dDeclaredLoop/README.md` is stale: that is the `gen_build_index.py --write` render, which is yours. I deleted the index copy; my two edit scripts and the gate's output are still in the scratch folder.

#### Per spec

| Spec | Rev | Bytes | Sections moved | Rows answered |
|---|---|---|---|---|
| 1 | rev-4 | 33626 | §2 S7 · §4 Files touched · §6 AC9, AC10 (new) · §7 · §9 | 3, 7 |
| 3 | rev-3 | 31425 | §2 S2, S8 · §4 The log record, Inventory, Files touched · §6 AC9, AC11 (new) · §8 F7 (new) · §9 · §10 | 16, 17, 18 |
| 6 | rev-3 | 26454 | §2 S1, S9, S11 · §4 Inventory · §6 AC8 · §9 | 32, 33, 36 |
| 16 | rev-3 | 20946 | §2 S4 · §3 · §4 Files touched · §5 · §6 AC6 (new) · §9 · §10 | 42, 43 |
| 17 | rev-3 | 26383 | §2 S1, S8 · §4 The acceptance record, Inventory, Files touched · §6 AC7, AC8 (new) · §9 · §10 | 45, 46, 47 |
| 22 | rev-3 | 26534 | §2 S1 · §3 · §4 The score, Inventory, Files touched · §6 AC10 (new) · §9 · §10 | 59, 60 |
| 46 | rev-3 | 15417 | §2 S1 · §4 Evidence · §6 AC1, AC3 · §9 | 123 |
| 56 | rev-4 | 48383 | §2 S4, S20 · §4 The owed leg rows, Files touched · §6 AC3, AC15 · §8 F5 (new) · §9 | 126, 127, and the `enforces` rows 7, 18, 23, 36, 47 |

Every Status line reads `DEFERRED · rev-N+1 · 2026-10-25`, and each §9 has one line naming the cross-check record and its rows. Every row's quoted sentence is gone. The one `grep` hit left is spec 56's `core-pending` line in Files touched, which is a corrected sentence.

#### How the revisions came out

- **The `enforces` tags are derived, not chosen.** v2's `[enforcement]` table, which unit 7 S1 copies into each principle's `clauses`, maps each unit's clause to a principle: spec 1 to `principle.p1`, spec 6 to `principle.p16`, spec 17 to `principle.p2`. Clause 0088 (spec 3) appears in no row, so spec 3 has a fork instead.
- **Stale pending rows.** Unit 7 AC3 reds a pending row for a principle a leg now enforces. So each leg-adding pass also deletes that principle's row from `core-pending.txt` where one exists, with a **Readers:** clause, which hygiene check 25 required.
- **Record kinds.** `transition`, `acceptance`, `disposition` and `recommendation` each join `TYPED_RECORD_KINDS` and the HYGIENE kind list in the same pass. Each spec states only the flags it passes and claims no `new <kind>` door (rows 17, 43 and 60 stay unknown until unit 7 builds).
- **Spec 6 S9:** `loop definition` now arrives from unit 1 already carrying `principle.p1`; S9 adds any `binds` tag it lacks.
- **Spec 56 beyond the brief:** S20 and AC15 tested `check_terminal_proof` on stdin. I moved both to stderr, per unit 15 F4, so spec 56 matches what Group C does to spec 2.
- **Spec 56's table** gained rows for units 3 and 17, and unit 27 now has its own row; unit 4 was already there.

#### Forks

None re-resolved, none re-opened. Two new ones, both left open for the owner:
- **Spec 3 F7:** which principle `loop transition record` enforces, since no row names clause 0088. Options are `principle.p20`, `p2` or `p22`; I recommend `principle.p20`.
- **Spec 56 F5:** who writes `enforces` for legs whose own unit names none. I recommend re-grounding each such unit so its own pass writes the key. The alternatives are writing them all at spec 56's pass (order 36), which leaves the `core meta-check` leg red until then, or a pending-list row, which the shrink-only list refuses.

#### Refused rows

None.

#### For the main loop

**A gap in the cross-check's population.** Units 2, 7, 8, 11, 13, 14, 15, 21, 25, 26, 28, 29 and 30 all add legs with no `enforces`, at orders 9 to 28. The re-ground covers none of them, since Groups B and C were not told to add it to specs 2 and 25. The meta-check reds each one from its pass, and nothing can excuse it. Clauses 0087, 0100 and 0111 to 0114 appear in no `[enforcement]` row, so units 2, 15, 26, 27, 28 and 29 need a fork for their tags. Spec 56's table also leaves out the legs of units 11, 13 and 15. This is what F5 asks the owner to decide.

**dOrderedCharter specs that look wrong:**
- **Unit 7, S3 against S4:** S4 puts `kind` rows on the pending list, but S3's stale rule names only `principle`, `practice` and `leg` rows (oc7:61-63, :69-70). That is row 33's unknown.
- **Unit 50:** its owed-rows probe owes no `enforces` (oc50:49), yet unit 7 S3 reds a leg without one. Any later pass that trusts the probe misses it.
- **Unit 15 S5:** a bare `sys.stderr.isatty()` is likely true on win32 when stderr is redirected to `NUL`, so the owner proof may admit a non-terminal. Spec 56 S20 keeps its console-mode probe for this reason.

#### Files

Specs in `memory/builds/dDeclaredLoop/spec/`:
- 2026-10-24-spec-TOOL-dDeclaredLoop-1.md
- 2026-10-24-spec-TOOL-dDeclaredLoop-3.md
- 2026-10-24-spec-TOOL-dDeclaredLoop-6.md
- 2026-10-24-spec-TOOL-dDeclaredLoop-16.md
- 2026-10-24-spec-TOOL-dDeclaredLoop-17.md
- 2026-10-24-spec-TOOL-dDeclaredLoop-22.md
- 2026-10-24-spec-TOOL-dDeclaredLoop-46.md
- 2026-10-24-spec-TOOL-dDeclaredLoop-56.md

Left in scratch:
- <scratchpad>/wA/edit56.py
- <scratchpad>/wA/readers.py
- <scratchpad>/wA/hyg.out

## Group B

All six Group B specs are revised. Every record row the brief assigned to this group was borne out when I re-read both sides, so none is refused. Each spec stays DEFERRED, is under the 49152-byte cap, and is still LF. Each quoted `dlN:L` sentence now greps empty. The hygiene gate, run over an index copy with only these six specs staged, failed on one check alone: check 9, the build-index render. That is the main loop's `gen_build_index.py --write` (`memory/builds/dDeclaredLoop/README.md` is stale), so I left it. The copy is deleted. The one new function name, `extract_scenario`, passes the naming lexicon.

#### Per spec

**TOOL-dDeclaredLoop-24** — now rev-3, 26436 bytes.
- Moved: S3 and §4 The schema (row 68).
- `item.test.verdict` is now fixed by `principle=principle.p2`, not `floor=`. No unit registers a `floor` namespace: spec 2 makes the floor's members values of the policy key `floor`. Spec 2's `floor.py` also lands at order 15, after this unit's order 11, so a `parser=` source would not resolve either.
- S3 points at spec 26 §8 F5.
- No forks.

**TOOL-dDeclaredLoop-25** — now rev-3, 25292 bytes.
- Moved: S1, S8, §4 Data model, §4 The fixture cases, and a new AC11 (rows 74, 77).
- `exit` is now fixed, by `principle.p2`.
- The `removes` plant commits `.governance/policy.toml` with `[instructions] exclude = ["step.test"]` at the fixture's `HEAD`, and the spec says the exclusion is the policy key.
- Beyond the record: the leg `loop splice check` had no `enforces`, although `kind.splice` binds `principle.p20`. The record's table missed this; the brief's leg fact covers it. The leg now carries `["principle.p20"]`, observed by AC11.
- No forks.

**TOOL-dDeclaredLoop-26** — now rev-3, 25937 bytes.
- Moved: S1, S3, S6, S7, S8, §3, §4, §5, AC5, AC6, a new AC8, §8, §9 and §10 (rows 81, 82, 83).
- The composition revision is `HEAD`. A reader-command population runs in the pin's worktree. The candidate read is dropped.
- **F4** (how a pin is composed) is marked `RESOLVED (agent, 2026-10-25, delegated): (a), rung 1`: compose in a scratch worktree detached at the pin. The cost is one worktree checkout per compose at an older pin.
- **F5** (new, OPEN for the owner): how the loop kit reaches `compose_rows`, a playbook-kit function. I recommend (a), an ask to dOrderedCharter for a `compose` verb on `tools/playbook/overlay_rows.py`. The alternative (b) is a declared import row in the shape of `tools/memory-tree/kit.toml:8`.
- Beyond the record, by the brief's facts:
  - `read_tag_policy` now runs `policy.py get --rev <pin>` as a subprocess, instead of calling dGroundRules' `resolve` in process at its default landed ref.
  - The leg carries `["principle.p8"]`, observed by AC8.
- I did not rewrite the rev-1 line of §9. I added "re-read at `462d20f35` for rev-3" to it, so the history stays true.

**TOOL-dDeclaredLoop-27** — now rev-3, 29502 bytes.
- Moved: S1, S2, S6, S10, §3, §4, §5, AC7, a new AC11, §7, §8 F5 and §10 (rows 91, 93, 99, 101, 103).
- The factory writes gov's pack only. For an `adopter.` name it writes nothing and prints a proposal.
- The namespace row now cites unit 19 S2 and fills every required field.
- The pin points at spec 26 F4.
- `kind.scenario` names `binds = ["principle.p8"]` and gate `loop scenario fixtures`, and that leg carries `enforces`.
- **F5** (new) is marked `RESOLVED (agent, 2026-10-25, delegated): (b), rung 3`: the scenario rows' own reference page is deferred by name. `help/reference/kinds.md` still re-renders in the commit that adds `kind.scenario`.
- Two changes follow from naming the factory and extractor explicitly:
  - The `factory` is now `scenario.py new`, and the Files touched line "`core.py`: the `new scenario` arm" is dropped.
  - The extractor moves to `tag_index.py`, following spec 18, since the index runs it and a kit imports no sibling kit.

**TOOL-dDeclaredLoop-28** — now rev-3, 25977 bytes.
- Moved: S2, S3, S6, S8, §4 Data model, the new §4 "The acts as write verbs", §4 Alternatives rejected, a new AC10 and §8 F5 (rows 106, 107).
- One change record per row: `Action` `add`, `Before` `none`, `After` `<tag>@<hash8>`, with the row in a TOML fence in the record's body.
- `add`, `amend` and `supersede` each map to the verb `add`.
- `exclude` writes no change record and rides the rescope row alone. A `remove` record would be read by unit 15 S9 as the gov tag ending for every build.
- "already carries rows" is gone.
- **F5** (new) is marked `RESOLVED (agent, 2026-10-25, delegated): (a), rung 1`. Today's reader admits a fenced body (`tools/memory-tree/deviation_join.py:218-220`). If `build_records.py` refuses it at the build run's first probe, the unit stops and files the ask.
- Beyond the record: the leg `loop adapt fixtures` carries `["principle.p8"]`, observed by AC10.

**TOOL-dDeclaredLoop-33** — now rev-4, 28837 bytes.
- Moved: S1, S8, §4 The rules and §8 F4 (rows 112, 114).
- `check --build` composes through spec 26's `compose_at` at the build's pin.
- **F4** (new, OPEN for the owner): which direction a loop-bound field declares. I recommend (b), an ask to dOrderedCharter for a numeric `widens` on unit 36 S1 and S5.
  - (a), an ordered list of values, cannot order a policy-tag deadline like `policy.flow.wait-ceiling`, which gov's own waits declare.
  - (c), leaving the fields fixed, would refuse the raise that clause 0118 says the update report must name as a widening.

#### Things that look wrong upstream, or in our specs

- **Unit 35** gives `compose_rows` no verb. Every loop-kit caller (specs 24, 25, 27, 28, 33 and 55) therefore needs either a verb or an import exception; spec 26 F5 holds that question.
- **Unit 46 §3** says no caller needs a revision other than `HEAD`. Spec 26 is such a caller; F4 works around it without a parent change.
- **Unit 36 S5** has no direction that orders numbers, yet clause 0118 needs loop-bound raises reported as widenings.
- **Unit 15 S7** gives the change kind no field for row content. Its S9 reads every `remove` repository-wide, so a build-scoped exclusion cannot use one.
- **v2's enforcement table** cites clauses 0111, 0112 and 0113 under no principle, though P8's text (v2:885-886) names all three. That is the basis for using `principle.p8` on the 26, 27 and 28 legs.
- **Our spec 27:** unit 7 S5 says a kind's gate reads the kind's whole population. `loop scenario fixtures` runs only fixture plants, so that may still fall short.

The pairs files and the checker I used are in `<scratchpad>/wB/`.

Files revised:
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-24.md`
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-25.md`
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-26.md`
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-27.md`
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-28.md`
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-33.md`

## Group C

I've revised all six Group C specs. Each record row I checked against both sides held, and none is refused. One detail of the brief for spec 5 was wrong, and I followed the spec text instead (see TOOL-dDeclaredLoop-5). Each spec has the new **Status:** rev and its §9 line. The quoted sentences are gone or read only as corrected. All six are under 49152 bytes. The hygiene gate, run over an index copy with only these six staged, names none of them. Its one failure is check 9, the stale `memory/builds/dDeclaredLoop/README.md`, which only `gen_build_index.py --write` fixes, so I've left that render to you. I deleted the index copy and my scratch files, and nothing is staged in the real index.

**TOOL-dDeclaredLoop-12** (row 39)
- Now rev-3, 25866 bytes.
- Sections moved: S4, §3 Edges, §4 Inventory, AC6, AC7 (new), §7, §8 F5, §10.
- S4 now finds `load_sets.py` through an inline `resolve_kit_dir` and runs `derive … --item <tag>` as a subprocess. With the playbook kit absent, every item's scope prints `unarmed`. AC7 observes that through a `scope-no-kit` plant and a grep showing no `load_sets` import.
- TOOL-dDeclaredLoop-41 (also order 6) inlines `resolve_kit_dir` into `loop_lib.py` too. S4 says there is one block, whichever unit's pass inlines it first.
- Fork added, F5, open for the owner. Recommendation (a), an ask: "PLAY-dOrderedCharter-11: `load_sets.py derive` takes `--item <tag>` and passes it to `derive_load_set`'s `item`". The cost is a wait: S4, AC6 and AC7 cannot pass until that lands. Option (b) is a `requires_if` import.

**TOOL-dDeclaredLoop-2** (row 12)
- Now rev-3, 38348 bytes.
- Sections moved: S5, §4 Evidence, The command, The factory, AC8, AC10.
- `check_terminal_proof()` now tests `sys.stderr.isatty()`, citing oc15 F4 as the owner's settlement. The typed `yes` belongs only to `policy_edit.py`, outside the parity block.
- AC8 now redirects stderr (`2>stderr.txt`). AC10 adds a grep that the block tests stderr and never mentions stdin.
- No fork added or re-resolved.

**TOOL-dDeclaredLoop-4** (row 23)
- Now rev-3, 22978 bytes.
- Sections moved: S5, §3 Edges, §4 Evidence, AC8 (new).
- The leg carries `"enforces": ["principle.p1"]`. This needed no fork: P1's enforcement row (v2:1823) names `cl-dClosedLoop-0089`, the clause this spec carries, and v2:851 reads "a coverage gate reds an unclaimed part".
- AC8 checks the leg the way spec 6's AC8 does.

**TOOL-dDeclaredLoop-5** (row 26)
- Now rev-3, 20564 bytes.
- Sections moved: §4 The checks, §10.
- The import now comes from `tools/memory-tree/coverage_join.py`.
- The brief said the unattended kit imports it. That is wrong: `check_actor_list` lives in `tools/loop/loop_lib.py` (dl5:108-111, :138), so the importer is the loop kit. TOOL-dDeclaredLoop-56 S17 (dl56:131-133) already says so and adds the loop kit's `requires memory-tree`. I wrote it that way.

**TOOL-dDeclaredLoop-18** (row 55)
- Now rev-2, 26915 bytes.
- Sections moved: S5, §3 Edges, §4 The catalogue in the `policy` namespace, AC6, §8 F5, §10.
- The family join now resolves a citation through oc19 S8's `read_policy_value(key, root, rev="HEAD")`, which runs `policy.py get` as a subprocess.
- An unknown key reads as undeclared: `get` exits 2 with `not a catalogue key`. Every `PolicyRefused` reads the same way. The `policy-family` plant carries copies of the playbook and policy kits, so `get` matches against the fixture's catalogue. AC6's "Red when" is restated against that call.
- Fork added, F5, open for the owner. oc7:209-210 says every `read_policy_value` call passes its key as a string literal, and a citation's key is not one. Recommendation (a): make the call and file the ask "PLAY-dOrderedCharter-7 §4: a caller that resolves a cited key's row, reading no value, may pass that key unquoted; the reader-coverage arm neither counts nor reds it".

**TOOL-dDeclaredLoop-34** (row 119)
- Now rev-2, 22707 bytes.
- Sections moved: S4, §3 Edges (was `none`), AC8 (new), §8 F6, §10.
- `pins.py` is now found with `backlog.resolve_kit_dir` (deviation_join.py:371) and run as a subprocess. A non-zero exit refuses the editorial claim.
- Fork added, F6, open for the owner. Recommendation (a), an ask: "PLAY-dOrderedCharter-33: a `pins.py mark --before <path> --after <path>` verb printing `derive_change_mark`'s mark under `spelling-map.toml` with no ruling, and for `semantic` the first differing word". That would also settle record rows 120 and 121. Option (b) is a `requires_if` import.

**Other things I found, not edited**
- **dl34 S1** (dl34:35) still imports the policy kit "as an optional slot". That is the same sibling-import pattern, but it is a dGroundRules surface outside row 119.
- **dl5 vs dl56:** spec 5 (order 5) imports from memory-tree, but the `requires memory-tree` that makes this legal lands with spec 56 S17 at order 36.
- **dl4 S7 vs dl56 S17:** both add `requires memory-tree` to the loop kit's descriptor.
- **Record, row 26:** its Change bullet (record:298) names the unattended kit as the importer, which is wrong (see TOOL-dDeclaredLoop-5 above).
- **dOrderedCharter:** no parent spec looks wrong. The literal-key sentence at oc7:209-210 does conflict with spec 18's resolver call, which is why F5 is there.

Files:
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-2.md
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-4.md
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-5.md
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-12.md
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-34.md
