**Serves:** research TOOL-dPlacedRequest-1

# dPlacedRequest — the cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record
[`2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck`](2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md)
is assembled from, each copied from its agent transcript. Group A read specs 1, 2, 3, 4, 5, 10 and 14; B 6, 7, 8, 9, 18, 21 and 34.

## Group A

1. Assumptions

| Spec | Assumption about the parent | Verdict | Evidence |
|---|---|---|---|
| 1 | Under `progress`, the witness is a commit whose `Gov-Transition` trailer names the build as `build=<slug>` | AGREES | pr1:93-95, :233-234, :347 · dl3:37-38 |
| 1 | Every recorded transition carries a `Gov-Transition` trailer, so a trailer-only witness read is enough | MISMATCH | pr1:94, :233-235, :408-409 · dl3:52-58, :346-348 |
| 2 | dl3's `write_transition` (S5) exists, so a last follow step can be added after its commit | AGREES | pr2:62-63, :144 · dl3:60-64 |
| 2 | The card record's anchor is the lowest unit id a spec H1 defines (dl3 §8 F2) | AGREES | pr2:104-105 · dl3:326-332 |
| 2 | A `card` kind row added to `build_records.py` and served as `**Serves:** journal <anchor>` binds, on the pattern dl3's transition record used | MISMATCH | pr2:101-105, :205, :228 · dl3:150-153, :45-49 · oc42:40-43, :45-49 |
| 2 | The policy-key factory is `core.py new policy-key <name> … --owner <build>` (dl6 S4) | AGREES | pr2:115-118 · dl6:65-68 |
| 2 | The record factory `tools/memory-tree/build_records.py` is oc7 S7's. The picks revised oc7 only at S9. | AGREES | pr2:101-102, :145 · oc7:88-95 |
| 3 | The `[[item]]` row shape: non-role rows declare `inputs`/`allowance`/`returns`, role rows inherit them | AGREES | pr3:43, :147-149 · dl12:105-130 |
| 3 | Entry items belong to dPlacedRequest and are never steps of the five | AGREES | pr3:239, :315 · dl12:80-81 |
| 3 | The actor convention is `command:<item name>` | AGREES | pr3:324 · dl12:109 |
| 3 | `step = "none"` is the value dl1 gives the `orient` workflow | AGREES | pr3:310-311 · dl1:149, :169 |
| 3 | `loop_lib.py --check` exits 0 on the built tree with the five rows (AC1, AC2, AC4) | UNKNOWN UNTIL BUILT | pr3:247-248 · dl12:46-56, :277-291 |
| 3 | A role row (`item.entry.place`) can take `outcomes = "dispositions"` and also the `probe` outcome every role row carries | MISMATCH | pr3:47-49, :176-178, :252-253 · dl12:39-40 |
| 3 | `outcomes = "dispositions"` and `read_outcome_set` give the nine words (dl16 S1, S5) | AGREES | pr3:48, :252-253 · dl16:32-35, :57-60 |
| 3 | The owner row's witness is written through dl16 S4's door `build_records.py new disposition --item …` | MISMATCH | pr3:145 · dl16:52-56, :249 |
| 3 | The factory composes `item.<step>.<name>` and routes `done` to the step's exit, so the rows cannot come from it | AGREES | pr3:236-237, :317-321 · dl24:61-63, :169-175 |
| 3 | A `returns` naming no record kind is prose and joins nothing | AGREES | pr3:151-153 · dl24:142-145 |
| 3 | The kind gate `loop_items.py check` passes over a composition that holds the five rows (AC3) | UNKNOWN UNTIL BUILT | pr3:250-253 · dl24:46-50 · dl26:280-291 |
| 3 | The schema field `outcomes`, shape `set`, accepts the string reference `"dispositions"` | UNKNOWN UNTIL BUILT | pr3:48 · dl24:122 · dl12:39-40 |
| 3 | `item.entry.intake` is dWellOiledMachine's to declare, so this build owes it nothing | MISMATCH | pr3:83-84 · dl24:136, :309-310 |
| 3 | `awaiting` declares `deadline`/`on-deadline` as the `wait` rule asks, with the deadline a policy tag | AGREES | pr3:186, :189 · dl33:57-63 |
| 3 | The `awaiting` self-route on `item.entry.claim`, which has no `draws`, passes the `counted` rule (AC6: no finding on `item.entry.*`) | MISMATCH | pr3:186, :280-281 · dl33:50-56 |
| 3 | `slug-taken` carries `draws`, so the `counted` rule reads that self-route as counted | AGREES | pr3:185, :190 · dl33:52-54 |
| 3 | A gov item's `deadline = "policy.flow.wait-ceiling"` stays admissible under the item schema | UNKNOWN UNTIL BUILT | pr3:186 · dl33:314-326 |
| 3 | A failed `placement.check`'s default self-route needs no route and no `draws` (dl14), and passes `counted` | UNKNOWN UNTIL BUILT | pr3:163-164 · dl33:50-56 |
| 3 | The parents' legs `loop definition`, item kind, tables and termination read the rows; no new arm is needed | AGREES | pr3:299-301 · dl1 S7 (rev-4) · dl24:68 · dl33:81-83 |
| 4 | `read_dispositions()` and `resolve_disposition(word)` in `loop_lib.py` are the one declaration | AGREES | pr4:35-38, :213 · dl16:32-39 |
| 4 | `attach` is an alias of `amend` | AGREES | pr4:235 · dl16:36-38 |
| 4 | The owner's placement is a dl16 S4 disposition record naming `item.entry.place-owner`, read by path | AGREES | pr4:44-46 · dl16:45-49 |
| 4 | `placement.py` sits beside dl27's `tools/loop/scenario.py` | AGREES | pr4:32 · dl27:64-65 |
| 4 | The new leg `loop placement fixtures` needs only its argv row, as its sibling leg did | MISMATCH | pr4:197 · dl27:92-97 · oc7:58-61 |
| 5 | The declaration is written through dl16 S4's door `build_records.py new disposition --build … --channel prompt` | MISMATCH | pr5:49-52, :109, :267 · dl16:52-56 |
| 5 | `prompt` is a legal `Channel`, and `breakpoint` is a member for `item.entry.place` | AGREES | pr5:52 · dl16:47-49, :57-60 |
| 5 | The disposition record kind is dl16's, not re-specced | AGREES | pr5:86 · dl16:45-46 |
| 10 | `select_scenarios(facts, composition)` in `tools/loop/scenario.py` returns admitted scenarios in declared order, else `flow.scenario-default` | AGREES | pr10:43-44, :50-51, :232 · dl27:64-70 |
| 10 | The `entry` values are `feature`, `amendment`, `patch` and `playbook-run` | AGREES | pr10:37-38 · dl27:58-61 |
| 10 | The composition passed is the repository's own (gov pack plus overlay, no build pin), held in memory | UNKNOWN UNTIL BUILT | pr10:44-45, §5 perf · dl27:71-75 · dl26:280-291 |
| 10 | The `scenario` field joins `TRANSITION_FIELDS` and is written via `write_transition --field`; the first record stands in for the claim | AGREES | pr10:56-59 · dl27:80-88 · dl3:60-61 |
| 10 | An unregistered default refuses (dl27 AC6); the risk line holds; Rollout activates nothing | AGREES | pr10:69, :136, :160 · dl27:293-295, :263-264, :228-229 |
| 14 | An owner's placement is an owner edge, never a repetition (dl33 S4) | AGREES | pr14:68-70 · dl33:54-55 |

2. Mismatches

- **pr1, trailer-only witness.** pr1:233-234 says "`--witness <sha>` must name a commit the clone holds whose `Gov-Transition` trailer names this build … a sha that does not resolve or carries none exits 2". dl3:52-53 says "The channel set, read through dGroundRules-2's `resolve("transitions.record")`", and dl3:346-348 says "the log record [is the source when `trailer` is opted out]… since v2:1156 admits any non-empty subset". So a project that sets `transitions.record = ["log"]` never renews a lease under `progress`.
  Change: S8 and §4 "The witness under `progress`" read the witness through dl3 S7's `read_transitions(build, repo)`, or through the log record where `trailer` is unselected. Add an AC4 case with `transitions.record` planted to `log`.
  Cause: pre-existing.

- **pr2, the `card` record kind.** pr2:103 says "`<date>-build-<anchor id>-card-<n>.md`, `**Serves:** journal <anchor id>`", and pr2:228 adds only "`build_records.py`: the `card` kind row". dl3:150-152 now says "The record serves as `transition`, never `journal`: under PLAY-dOrderedCharter-42 S3 a `-transition-<n>.md` file whose Serves kind is not `transition` is malformed". oc42:41-43 says the factory's "per-kind table … is refused at import, naming the kind, when its keys differ from that tuple". As written, the `card` row makes `build_records.py` fail on load.
  Change: S8 serves the record as `**Serves:** card <anchor id>`. Files touched gains `card` in `TYPED_RECORD_KINDS` (`tools/memory-tree/tree_lib.py`) and in the HYGIENE kind list. Add an AC in dl3 AC11's form: `gen_build_index.py --print-bindings` prints an `S` row of kind `card` and no `A` row. Name no `new card` door, as dl3 and dl16 rev-3 name none.
  Cause: re-ground. dl3 rev-3 moved the pattern pr2 copied; the oc42 rule it applies already read so at `5352805c8`.

- **pr3, `dispositions` plus `probe` on a role row.** pr3:176 says "The role rows also carry the `probe` outcome every role item takes", and `item.entry.place` declares `outcomes = "dispositions"` (pr3:47-49). dl12:39-40 says "every item's outcome set is non-empty and closed, a list or the reference `dispositions`". A reference cannot also hold `probe`, and AC3 expects exactly the nine words.
  Change: either type `item.entry.place`'s outcomes as the nine words plus `probe` (and AC3 then checks that list), or drop `probe` from the placing role row and state where its probe route lives.
  Cause: pre-existing.

- **pr3, the owner row's door.** pr3:145 names "TOOL-dDeclaredLoop-16 S4's door, `build_records.py new disposition --item item.entry.place-owner`". dl16:54-56 now says "Whether the factory's `new` verb is generic per kind is unknown until PLAY-dOrderedCharter-7 builds … so the build run re-grounds AC3's call". dl16:249 adds "no `new disposition` door is claimed".
  Change: the Body cell names "the record factory's writer, passed `--item item.entry.place-owner …` (dl16 S4)", with the verb re-grounded on the landed factory.
  Cause: re-ground.

- **pr3, who declares `entry.intake`.** pr3:83 says "No `entry.intake` row: dWellOiledMachine's hook item". dl24:136 says "`entry.intake` gains its fixed row when dPlacedRequest declares it as an item".
  Change: §3 states that dl24's `[[fixed-row]]` trigger names dPlacedRequest while dWellOiledMachine declares the item, and files the ask that dl24 (or dWellOiledMachine) owns the fixed row, so the floor item is not left unfixed.
  Cause: pre-existing.

- **pr3, the `awaiting` self-route.** pr3:186 routes `` `awaiting` | `item.entry.claim`, `deadline = …` `` with no `draws`, and AC6 (pr3:280) expects "no finding naming an `item.entry.*` item". dl33:50-52 says "with every counted edge and every owner edge set aside, the transition tables and the item routes are acyclic". A `command:` actor's self-route without `draws` is neither kind of edge, and dl33 exempts no wait edge.
  Change: give the `awaiting` route a `draws` cause, or ask dl33 to set aside an edge carrying `deadline`. Either way AC6 gains the matching case.
  Cause: pre-existing.

- **pr4, the leg's `enforces`.** pr4:197 lists "`tools/gate-legs.json`: the leg `loop placement fixtures`, argv `python {prefix}/loop/placement.py --fixture`". dl27:94-96 now gives its sibling leg "`loop scenario fixtures` … carrying `enforces = ["principle.p8"]`". oc7:60-63 says "a leg carrying no `enforces` is red. Each red is excused only by a row of the shrink-only pending list".
  Change: the leg row carries a non-empty `enforces` (the principle whose v2 `[enforcement]` row names `cl-dClosedLoop-0120`'s sibling clause, or an owner-picked tag as dl3 F7 does). Add an AC: `python -m json.tool tools/gate-legs.json` shows it, and `core.py meta-check` names no such leg. Units 5 and 10 ride the same leg.
  Cause: pre-existing. oc7 S3 already read so at `5352805c8`; dl27 rev-3 is the re-ground that restates it.

- **pr5, the declaration's door.** pr5:49-52 says "through TOOL-dDeclaredLoop-16 S4's door, `python tools/memory-tree/build_records.py new disposition --build <slug> …`", and pr5:109 and :267 say the same. dl16:52-56 now says "A writer passes the factory `--build <slug> --unit <id> --item <tag> --disposition <word> --channel <channel>` … the build run re-grounds AC3's call on the landed factory".
  Change: S4, §4's flow and §10 name the factory's writer with those flags rather than a `new disposition` verb, and AC4 re-grounds on the landed factory.
  Cause: re-ground.

3. Unknown until built

- **pr3 AC1/AC2/AC4.** `loop_lib.py --check` refuses on a non-zero `derive` (dl12:51-53). It is decided by the owner's pick of dl12 §8 F5 (`--item` on `load_sets.py derive`) and that ask landing in dOrderedCharter's build.
- **pr3 AC3.** The kind gate composes through `compose_rows`, "reached as TOOL-dDeclaredLoop-26 §8 F5 settles" (dl24:46-47). It is decided by dl26 F5, open for the owner (a `compose` verb, or a declared import), and then dl26's build.
- **pr3, `outcomes` shape.** It is decided by how dl24's built `check_rows` reads a `set`-shaped field holding the scalar reference that dl12 and dl16 admit.
- **pr3, policy-tag `deadline`.** It is decided by the owner's pick of dl33 §8 F4: option (a) would refuse `policy.flow.wait-ceiling` off a typed list.
- **pr3, the default refusal self-route.** It is decided by whether dl33's built `counted` rule walks dl14's undeclared default refusal routes as edges.
- **pr10 S3, the composition argument.** It is decided by dl26 F5 (how the loop kit reaches `compose_rows`), and by whether `compose_at(root, HEAD)` returns an in-memory composition `select_scenarios` takes.

4. Revised parent units cited but not depended on

- pr1: none. dl3 S1 is depended on.
- pr2: none. dl3 S5 and §8 F2, dl6 S4 and oc7 S7 are depended on; oc7's rev-5 change (S9) touches none of them.
- pr3: none. dl1, dl12, dl16, dl24 and dl33 are each depended on.
- pr4: none. dl16 and dl27 are each depended on.
- pr5: none. dl16 is depended on.
- pr10: none. dl3 and dl27 are each depended on.
- pr14: none. dl33 S4 is depended on; its rev-4 changes (S1, S8, F4) do not touch it.

Files read:
- memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-{1,2,3,4,5,10,14}.md
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-{1,3,6,12,16,24,26,27,33}.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-42.md

## Group B

#### Group B (led by spec 7): parent cross-check, specs 6, 7, 8, 9, 18, 21 and 34

**Baselines I checked against:**
- dDeclaredLoop at `783f1ad3a`, the last commit to `memory/builds/dDeclaredLoop/spec`.
- dOrderedCharter at `462d20f35`. `git diff --stat 462d20f35 HEAD -- memory/builds/dOrderedCharter/spec` prints nothing, so HEAD holds the same text.
- `git merge-base --is-ancestor 60d60e694 HEAD` succeeds: the fork picks are in the tree.
- The parent diffs came from `git show --format= 783f1ad3a -- <dl spec>` and `git show --format= 1e9b2dad5 -- <oc spec>`.

**Result:** 35 assumptions: 21 AGREES, 9 MISMATCH and 5 UNKNOWN UNTIL BUILT. Five mismatches come from the re-grounds (two of them also rest on rules that were already there) and four were already present at `5352805c8`.

#### 1. Assumptions

| Spec | Assumption about the parent | Verdict | Evidence |
|---|---|---|---|
| 6 | Item rows of `tools/loop/loop.toml` in dl12's S2 shape carry an actor | AGREES | pr6:34-35 · dl12:36 (only S4 moved at rev-3) |
| 6 | The `policy` namespace row is dl18's | AGREES | pr6:41 · dl18:36, :108 (rev-2 moved S5's join only) |
| 6 | The registry `tools/playbook/namespaces.toml` has an `ns` column (oc19 S2) | AGREES | pr6:47-48 · oc19:51-54 (the picks moved only S9) |
| 6 | `loop_lib.py` reaches the registry through `resolve_kit_dir("playbook", …, here)` | AGREES | pr6:49-51 · dl12:45-56: rev-3 now puts the inline `resolve_kit_dir` block in `loop_lib.py` |
| 6 | When the playbook registry is absent, `loop_lib.py --check` is "not green" | MISMATCH | pr6:51-52, AC4 pr6:160-162 · dl12:50-52, AC7 dl12:243-246 |
| 7 | Eight item rows in dl12 S1's shape | AGREES | pr7:50 · dl12:34-35 |
| 7 | Policy-key factory `core.py new policy-key … --owner` | AGREES | pr7:107-109 · dl6:65-68 (rev-3 moved S1, S9 and S11 only) |
| 7 | `loop_witness.py rerun --sha --cmd --expect` answers confirmed/refuted/inconclusive, and dl17 §3 hands `probe.run` and `probe.judge` to this build | AGREES | pr7:75-80, :244-245 · dl17:52-56, :86 |
| 7 | The re-run is a detached worktree under a timeout (dl17 S2) | AGREES | pr7:253-254 · dl17:45 |
| 7 | `read_tag_policy(key, root, build)` reads `probe.points` | AGREES | pr7:110-111 · dl26:69-76 (same name and signature; it now runs `policy.py get --rev <pin>` as a subprocess) |
| 7 | `probe.points` (default `none`) is a tag-valued key that `read_tag_policy` handles | MISMATCH | pr7:110 · dl26:76 → oc36:183, :59 |
| 7 | The `probe` and `probe-trigger` kinds are rows of the record factory (oc7 S7), copying dl17 S1's `acceptance` row, and serve as `journal` | MISMATCH | pr7:85-89, :182, :192, Files touched pr7:233 · dl17:35-41, :110 · oc42:40-49 |
| 7 | The writer door for the two kinds exists in the landed factory | UNKNOWN UNTIL BUILT | pr7:61, :85 · dl17:43-44 |
| 7 | The new leg `loop probe fixtures` needs only its argv | MISMATCH | pr7:236 · oc7:58-64 |
| 8 | Schema file `tools/loop/item-schema.toml` (dl24 S2), each field with `shape` and `widens` | AGREES | pr8:34-38 · dl24:40-45 (rev-3 moved S3 and the fixed-row source only) |
| 8 | How the `[field.<name>]` table and its `values` key are spelled | UNKNOWN UNTIL BUILT | pr8:95-111 · dl24:42, :120-130 (no `values` key is named) |
| 8 | `python loop_items.py check` passes over the three new rows (AC1) | UNKNOWN UNTIL BUILT | pr8:196-198 · dl24:47-51 (composition reached "as TOOL-dDeclaredLoop-26 §8 F5 settles") · dl26:280-293 (F5 OPEN) |
| 8 | Item rows and `read_items` (dl12 S1, S2) | AGREES | pr8:40, :86 · dl12:34-36 |
| 8 | The `loop definition` leg's command is `loop_lib.py --check`, and the page is `help/loop.md` (dl1) | AGREES | pr8:44-45, :67 · dl1:85-87 (rev-4 adds `enforces`; the argv is unchanged) |
| 8 | A scalar's `widens` lists its values narrowest first (oc36 S5) | AGREES | pr8:112-113 · oc36:61-63 (the picks moved S4 only) |
| 9 | Overlay `.governance/instructions.toml` holds `[[unit]]` rows (oc32 S1) and admits level 2 (S3) | AGREES | pr9:35, :277 · oc32:47-49, :57-59 |
| 9 | `derive_unit_composition` (oc32 S4) | AGREES | pr9:46 · oc32:60-66 |
| 9 | `write_overlay_units` is the one writer, and the upgrade-step kind is one of its doors (oc32 S8) | AGREES | pr9:64, :209-210 · oc32:94-98 |
| 9 | Writing `[[unit]]` rows to the overlay touches nothing beyond the overlay and the manifest | MISMATCH | Files touched pr9:181-194 · oc32:84-90, :271-273, AC8 oc32:311-312 |
| 9 | `pockets` run after `up` sees the units `up` just wrote (AC3) | MISMATCH | pr9:234-236, :246-247 · oc32:49 |
| 9 | `instructions_edit.py propose --manifest overlay` (oc15 S2) | AGREES | pr9:72 · oc15:55-60 |
| 9 | The `[[upgrade]]` row copies `playbook/adopter-rules-to-overlay`'s shape (oc31 §4) | AGREES | pr9:120-132 · oc31:81-83, :170-176 |
| 9 | `OPEN` as dl3's F1 resolved it | AGREES | pr9:271 · dl3:322 |
| 18 | `seg := [a-z0-9][a-z0-9-]*`, at most 64 bytes, `parse_tag` in `tools/playbook/tag_index.py` (oc19 S1, AC1) | AGREES | pr18:28-30, :36-37, :74-76 · oc19:47-50 |
| 18 | oc19 registers the `unit` namespace | AGREES | pr18:104 · oc19:53-54 |
| 21 | `flow.wait-ceiling` default of 72 hours (dl33 S5) | AGREES | pr21:76-77 · dl33:57-62 |
| 21 | Owner's disposition record (dl16 S4) with `Item` and `Disposition` fields, read from the patch build's folder | AGREES | pr21:82-83 · dl16:45-53 (it now serves as `disposition <unit id>`, so AC1's plant must write it that way) |
| 21 | That record can exist in a just-claimed patch build's folder | MISMATCH | pr21:57-60, :82-83 · dl16:47, :50 · dl3:45-46 |
| 21 | How the owner writes that record (which factory verb) | UNKNOWN UNTIL BUILT | pr21:82 · dl16:53-55 |
| 21 | `write_transition` (dl3 S5) can be gated by `check_patch_ratified` | AGREES | pr21:83-85 · dl3:60, :109-112 |
| 21 | ` · scenario=<tags>` is dl27 S8's field | AGREES | pr21:88 · dl27:80-82 |
| 21 | oc7 S7's factory is not used (F2 picked (a)) | AGREES | pr21:268-271 · oc7:88-94 |
| 21 | The new leg `loop claim fixtures` needs only its argv | MISMATCH | pr21:94, :191 · oc7:58-64 |
| 34 | `tools/playbook/tag_index.py` is minted by oc19, which is DEFERRED | AGREES | pr34:217-218 · oc19:47-49 |
| 34 | Inside `tools/loop/`, only `loop_lib.py`'s loader spells `resolve_kit_dir` (AC34) | MISMATCH | pr34:148-151, :491-493 · dl12:45-56 |

#### 2. Mismatches

**pr6, registry absent: "not green" against dl12's "exits 0"**
- **Spec says:** pr6:51-52: "With no registry resolved, the namespace arm prints `unarmed — no namespace registry resolves` and the run is not green." AC4 (pr6:160-162): "exits non-zero."
- **Parent says:** dl12:50-52: "With the playbook kit absent, every item's scope prints `unarmed` naming the kit and the rest of the check runs." AC7 (dl12:243-246): "its `here` holding no playbook kit, every item's scope prints `unarmed` naming the playbook kit and the plant exits 0."
- **Conflict:** `namespaces.toml` lives in the playbook kit, so these two arms of the same `loop_lib.py --check` give opposite answers for the same absence. Once pr6 lands, dl12's `scope-no-kit` plant goes red.
- **Change:** pr6 S3 and AC4 state which rule wins when the kit is absent. Either the namespace arm reds only when some row declares `unfolds` (and dl12 AC7's plant holds none), or it follows dl12's unarmed-but-passing rule. The answer is named against dl12 AC7.
- **Cause:** re-ground. dl12 rev-3 added S4's absent-kit rule and AC7; at `5352805c8`, S4 named only `derive_load_set`.

**pr7, `probe.points` is not shaped as a tag-valued key**
- **Spec says:** pr7:110: "`probe.points` (default `none`), a set of item tags in `review.breakpoints`' grammar, read through TOOL-dDeclaredLoop-26 S6's `read_tag_policy`."
- **Parent says:** dl26:76: "The tag-valued keys are those dOrderedCharter-36 S4 reads as tag-valued." oc36:183: "key is tag-valued when its landed row's `allowed` is a table whose `type` is `set`, `list` or `name`." oc36:59 spells v2's `none` for a set key as "by default `[]`".
- **Change:** pr7 S9 gives `probe.points`' catalogue row `--allowed` as a `{ type = "set", … }` table with `--default []`, so `read_tag_policy` and the successor redirect cover it.
- **Cause:** pre-existing. oc36 rev-4 (§4:180 at `5352805c8`) already held the definition. The `[]` spelling of v2's `none` is the picks' (oc36 rev-5).

**pr7, the record kinds copy a row that has since moved**
- **Spec says:** pr7:86: "copying TOOL-dDeclaredLoop-17 S1's `acceptance` row". The examples at pr7:182 and pr7:192 read `**Serves:** journal TOOL-dExample-2`. Files touched (pr7:233) lists only `build_records.py`.
- **Parent says:** dl17:37-41: "`**Serves:** acceptance <unit id>` … `acceptance` is added to `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py`, which the factory's kind table must equal at import (PLAY-dOrderedCharter-42 S1, S2), and to the closed `<kind>` list of `tools/memory-tree/HYGIENE.template.md`". oc42:41-43: the factory "is refused at import … when its keys differ from that tuple". oc42:47-48: a `-<kind>-<n>.md` file "whose Serves kind is not `<kind>` is malformed".
- **Consequence:** adding two factory rows without the tuple stops `build_records.py` from loading, so AC7 cannot go green.
- **Change:** S6 adds `probe` and `probe-trigger` to `TYPED_RECORD_KINDS` and to the HYGIENE kind list. Both examples read `**Serves:** probe-trigger …` and `**Serves:** probe …`. Files touched gains `tools/memory-tree/tree_lib.py`, `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md`. AC7 adds a `--print-bindings` check, as dl17 AC8 does.
- **Cause:** re-ground. dl17 rev-3 moved the copied row from `journal`; oc42's rule was already there at `5352805c8`.

**pr7, the new leg has no `enforces`**
- **Spec says:** pr7:236: "`tools/gate-legs.json`: the leg `loop probe fixtures`, argv `python {prefix}/loop/probe.py --fixture`".
- **Parent says:** oc7:61-63: "a leg carrying no `enforces` is red. Each red is excused only by a row of the shrink-only pending list". dDeclaredLoop's re-ground made every new leg carry `enforces` for this reason (dl6:86-90 and S11, dl17 S8, dl1:85-95).
- **Change:** the leg row carries `enforces` with the principle whose v2 `[enforcement]` row names `cl-dClosedLoop-…` for this clause (P31's), any stale `principle` pending row is deleted, and an AC reads the row's `enforces`.
- **Cause:** pre-existing. The same sentence is at line 59 of oc7 at `5352805c8`; the dl re-ground only surfaced it.

**pr9, the step's overlay write stales the policy mirror**
- **Spec says:** Files touched (pr9:181-194) lists `.governance/instructions.toml` and nothing for the mirror.
- **Parent says:** oc32:271-273: "Any overlay edit, a `[[unit]]` row's included, stales the mirror, its key being the file's blob id; the landing regenerates it". oc32:88-90: "the guard's mirror shape also requires `.governance/instructions.toml`'s staged blob to equal HEAD's". AC8 (oc32:311-312): "`policy.py mirror --check` exits 1 until `mirror --write`".
- **Consequence:** the gov pass that runs `up` leaves the mirror stale, and the mirror cannot be staged in the same commit as the overlay.
- **Change:** Files touched and §4 Migration name `.governance/policy.json`, regenerated by `policy.py mirror --write` in its own commit after the step's commit, or state that the landing regenerates it per oc32 §5. The fixture's AC7 down/witness says whether it expects a stale mirror.
- **Cause:** re-ground (picks, oc32 rev-4, item 7).

**pr9, `pockets` reads the landed revision, not the working tree**
- **Spec says:** AC3 (pr9:234-236): "When `python instruction_units.py pockets --root <fixture>` runs after AC1's plant, it prints `## pockets` and three `- ` lines". AC6 (pr9:246-247) implies `up` leaves its writes uncommitted.
- **Parent says:** oc32:49: `read_overlay` reads "the file at the landed revision, never the working tree, as every composer does".
- **Change:** AC1's and AC3's plants commit `up`'s write before `pockets` runs, and S3 states that `pockets` shows units only once their commit is HEAD.
- **Cause:** pre-existing (oc32 S1 is unchanged by the picks).

**pr21, a just-claimed patch build has no unit id for the disposition record**
- **Spec says:** pr21:82-83: "the patch build's folder holds an owner's disposition record (TOOL-dDeclaredLoop-16 S4)". At that point the build holds only S4's README (pr21:57-60).
- **Parent says:** dl16:47: "`<date>-build-<unit id>-disposition-<n>.md`". dl16:50: "served as `**Serves:** disposition <unit id>`". dl3:45-46: "The anchor is the lowest unit id a spec H1 under the build defines."
- **Consequence:** before Design, the build defines no spec, so there is no id to name the record by.
- **Change:** S6 states the unit id the ratification record carries before the patch build has a spec, for example one minted with the derived plan record, or moves the ratification after the first spec exists.
- **Cause:** pre-existing (the `<unit id>` grammar is unchanged at dl16 rev-3, which added the typed `Serves`).

**pr21, the new leg has no `enforces`**
- **Spec says:** pr21:94: "the leg `loop claim fixtures` in `tools/gate-legs.json`, argv `python {prefix}/loop/claim.py --fixture`". pr21:191 says the same.
- **Parent says:** oc7:61-63, the same rule as for pr7's leg.
- **Change:** the leg row carries `enforces`. pr34 S31 (pr34:138-140), which amends this leg's subject, chunk and ceiling, also lists `enforces` for `loop placement fixtures` and `loop claim fixtures`.
- **Cause:** pre-existing.

**pr34, AC34's grep now hits more than the loader**
- **Spec says:** AC34 (pr34:491): "When `git grep -n resolve_kit_dir -- tools/loop/` runs, it prints only `loop_lib.py`'s loader".
- **Parent says:** dl12:45-47: "`loop_lib.py --check` finds PLAY-dOrderedCharter-11's `tools/playbook/load_sets.py` through `resolve_kit_dir("playbook", "load_sets.py", here)`". dl12:53-56: "The `resolve_kit_dir` block is carried inline between its markers … one block in `loop_lib.py`". pr6:49 adds a second call.
- **Consequence:** the grep prints the inline block and its calls, not just the loader, so AC34 is red as worded.
- **Change:** AC34 says S34's point: no `tools/loop/` module but `loop_lib.py` names `resolve_kit_dir` for a memory-tree module. Its grep is narrowed to `resolve_kit_dir("memory-tree"`, or it lists the expected hits.
- **Cause:** re-ground (dl12 rev-3 S4).

#### 3. Unknown until built

- **pr7, record writer door:** dOrderedCharter-7's build decides whether `build_records.py`'s `new` verb is generic per kind (dl17:43-44 claims no door), so the build decides how `probe.py return` and the trigger write their records.
- **pr8, field spelling:** dDeclaredLoop-24's build decides how a field is spelled in `item-schema.toml`, `values` included; pr8:111 defers to it.
- **pr8, AC1's `loop_items.py check`:** this check runs over the composition, reached as dl26 §8 F5 settles. F5 is open for the owner, so dDeclaredLoop-24 and -26's build decides whether `check` runs at all.
- **pr21, how the owner writes the record:** the same factory question as pr7, from dl16:53-55. It decides the verb the owner runs and the shape AC1's `patch-owner-ratified` plant must reproduce.
- **pr34 AC34, a possible third hit:** dl26 F5 is open (dl26:280-293). If it settles on a subprocess found through an inline `resolve_kit_dir` in `tools/loop/composition.py`, a hit outside `loop_lib.py` lands in AC34's grep. dDeclaredLoop-26's build decides it.

#### 4. Revised parent units cited that no assumption depends on

- **pr6:** none. dl18's revised S5 policy join and oc19's revised S9 window are not relied on.
- **pr7:** none. dl6's revised S1, S9 and S11, and oc7's revised S9 owner proof, are not relied on.
- **pr8:** none. dl1's `enforces` addition and oc36's revised S4 exclusion default are not relied on.
- **pr9:** dl3, cited only as precedent for F1. oc15's revised S5 proof and oc31's revised S3, S5, F6 and F7 are not relied on.
- **pr18:** none. oc19's revised S9 is not relied on.
- **pr21:** none. dl33's revised S1, S8 and F4 are not relied on.
- **pr34:** none. oc19's revised S9 is not relied on.

All paths are under `memory/builds/`: the seven `dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-{6,7,8,9,18,21,34}.md`, the `dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-{1,3,6,12,16,17,18,24,26,27,33}.md`, and the `dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-{7,15,19,31,32,36}.md` plus `dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-42.md`.
