**Serves:** research TOOL-dDeclaredLoop-1

# dDeclaredLoop — the cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record
[`2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck`](2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md)
is assembled from, each copied from its agent transcript. Group A read specs 1, 3, 6, 16, 17, 22 and 46; B 2, 24, 25, 26 and 28; C 4, 5, 27, 33 and 55; D 12, 18, 34 and 56.

## Group A

1. Assumption table

| Spec | Assumption about dOrderedCharter | Verdict | Evidence |
|---|---|---|---|
| 1 | oc6 S3's drive sort lives in `render()` of `render_playbook.py` and orders rows "by the workflow's `stage` integer" | AGREES | dl1:83-85 · oc6:53-56 (not moved at rev-4 or rev-5) |
| 1 | The drive-section reader exists only once oc6 lands, and is observed on the landed parent | AGREES | dl1:260, dl1:306-307 · oc6:3 (DEFERRED, order 19) |
| 1 | `instruction_units.py drive --check` exists and catches a change in the drive rows' order | MISMATCH | dl1:302-305 · oc6:62-66 |
| 1 | oc6's drive `stage` field names a workflow by name, so moving the `stage` integer out of `workflows.toml` leaves oc6 S1/S4's validation intact | AGREES | dl1:59-62 · oc6:42-43, oc6:62-64 |
| 1 | How oc6's renderer reads the integer (directly from TOML or through `roles_lib`), and what it does when the key is gone (sorts as 0, or raises) | UNKNOWN UNTIL BUILT | dl1:83-86, dl1:304-305 · oc6:54-56 (says nothing on this) |
| 1 | `handoff.py` reads no `stage` (S5/AC5), even after oc6 S5 adds drive lines to `render_handoff` | UNKNOWN UNTIL BUILT | dl1:70-72, dl1:193, dl1:286-288 · oc6:67-69 (order of the lines not stated) |
| 1 | The new leg `loop definition` can land with no `enforces` | MISMATCH | dl1:77-78, dl1:311 · oc7:58-63, oc7:228 |
| 3 | `build_records.py` is the factory, with name grammar `<date>-build-<unit id>-<kind>-<n>.md` and the `FIELD` regex | AGREES | dl3:39-42, dl3:119-120, dl3:330-331 · oc7:88-92 |
| 3 | A new kind is one kind row of required fields and closed sets | AGREES (but see the next row) | dl3:130-132, dl3:208 · oc7:91 |
| 3 | A `-transition-<n>.md` record binds as `**Serves:** journal <id>` | MISMATCH | dl3:123, dl3:133-134 · oc7:165 → oc42:40-49, oc42:158-161 |
| 3 | `build_records.py new transition --build --unit …` is a door shared by every kind | UNKNOWN UNTIL BUILT | dl3:119 · oc7:96-98 (states only `new exception`), oc7:219 |
| 3 | The new leg `loop transition record` owes only pins, ceiling evidence and dossier, with no `enforces` | MISMATCH | dl3:69, dl3:211-213 · oc7:58-63, oc7:228 |
| 6 | The register row is `tag`, `owner`, `binds`, `population`, `factory`, `gate`, and `population` may be a glob or a command | AGREES | dl6:121-124, dl6:138-153 · oc7:66-69 |
| 6 | `core.py new <kind> <name> …` runs the row's `factory` | AGREES | dl6:47-48, dl6:292-293 · oc7:76-77 |
| 6 | Contract: a row off the pending list names an existing factory and a gate leg whose `enforces` holds every `binds` tag | AGREES | dl6:79-82, dl6:121-124 · oc7:72-74 |
| 6 | Gate seen red on a planted instance, recorded as a `New arm:` line | AGREES | dl6:262 · oc7:74-75 |
| 6 | oc7 seeds `preset` under dDeclaredLoop, and dl6 re-owns it to dKeptSession through its deviation 61 | AGREES | dl6:30, dl6:83-85 · oc7:133-135 |
| 6 | The pending list's only reader is the meta-check, which reds the six `kind` rows as stale; oc7 is "DEFERRED at rev-3" | MISMATCH | dl6:40-46 · oc7:3, oc7:58-63, oc7:72-73 |
| 6 | Whether a `kind` pending row whose factory and gate have landed is red as stale | UNKNOWN UNTIL BUILT | dl6:43-44 · oc7:61-63 (stale rule stated for `principle`/`practice`/`leg`), oc7:192 |
| 6 | `binds = ["principle.p16"]` for `kind.role`, "as dOrderedCharter-7 seeded it" | UNKNOWN UNTIL BUILT | dl6:143 · oc7:66-69, oc7:181-188 (only `kind.skill`'s value is shown) |
| 6 | The register, the pending list, `new` and the contract are oc7 S4-S6's | AGREES | dl6:92-93, dl6:108 · oc7:66-87 |
| 6 | The new leg `loop factories fixtures` can land with no `enforces` | MISMATCH | dl6:86-88, dl6:172, dl6:248-250 · oc7:58-63, oc7:228 |
| 16 | Factory grammar and per-kind fields, with the kind `disposition` | AGREES | dl16:42-47 · oc7:88-92 |
| 16 | Adding a kind row to `build_records.py` is enough for `**Serves:** disposition` to bind | MISMATCH | dl16:42-47, dl16:102, Files touched (only `build_records.py`) · oc7:165 → oc42:35-44 |
| 16 | `build_records.py new disposition …` door | UNKNOWN UNTIL BUILT | dl16:46-47 · oc7:96-98, oc7:219 |
| 16 | A build-level record uses the build's first unit id, "the grammar as landed" | AGREES | dl16:217-220 · oc7:90 |
| 17 | Factory grammar, with the kind `acceptance` | AGREES | dl17:32-33, dl17:291 · oc7:88-92 |
| 17 | A `-acceptance-<n>.md` record binds as `**Serves:** journal <unit id>` | MISMATCH | dl17:34, dl17:92 · oc7:165 → oc42:40-49, oc42:158-161 |
| 17 | The new leg `loop computed witness` owes no `enforces` | MISMATCH | dl17:60, dl17:168, dl17:187-189 · oc7:58-63, oc7:228 |
| 22 | Factory grammar, with `recommendation` added as a new kind and never a second writer | AGREES | dl22:52-57, dl22:320-321 · oc7:88-95 |
| 22 | Adding a kind row is enough for `**Serves:** recommendation` to bind | MISMATCH | dl22:118, Files touched (only `build_records.py`) · oc7:165 → oc42:35-44 |
| 22 | `build_records.py new recommendation …` door | UNKNOWN UNTIL BUILT | dl22:56-57 · oc7:96-98, oc7:219 |
| 46 | oc7 S2 adds an `enforces` key to `gate-legs.json` rows, the pattern `stage` follows | AGREES | dl46:24 · oc7:55-57 |
| 46 | The canary's `KNOWN` holds `name argv guard impure reads chunk subject ceiling signature doc_reads` | MISMATCH | dl46:71-72 · oc7:167, oc50:37-39 |

2. MISMATCHES

- **dl1 AC9 cannot fail on the defect it names.**
  - dl1:302-305: "`python instruction_units.py drive --check` … exits 0 and the rendered drive rows keep their base order. Red when: the sort still reads `stage` … so every row sorts as 0."
  - oc6:64-66: "every line between the drive region's markers in the rendered charter is a selected kit's row; every selected kit's row is a line there." That is a membership check both ways. Only oc6 AC2 (oc6:227-229) checks order, and it checks the render.
  - So a collapsed sort re-renders the same rows in another order, and `drive --check` still exits 0.
  - Change: AC9 compares the ordered output of `drive --list` (or the rendered drive region) line for line with its base-order copy. Revision rev-4, §6 AC9.

- **The new legs carry no `enforces`, which the landed meta-check reds (dl1, dl3, dl6, dl17).**
  - dl1:77-78 (`loop definition`), dl3:69 and :211 (`loop transition record`), dl6:86-88 and :172 (`loop factories fixtures`), and dl17:60 and :187 (`loop computed witness`) each add a leg with no `enforces`. dl6:248-250 checks `enforces` on its five wrapped legs only.
  - oc7:61-63: "a leg carrying no `enforces` is red. Each red is excused only by a row of the shrink-only pending list". oc7:228: "The pending list is written once at the build pass and only shrinks after."
  - oc50's owed-rows probe never owes `enforces` (oc50:46-53), so the dl specs' "rows a new leg owes" leave it out.
  - dl56:87-91 (S4) does supply `enforces` for units 1 and 6, but only at order 36, so the bar's `core meta-check` leg is red from dl1's order-2 pass until then. Its fallback, "a `leg` row of `tools/playbook/core-pending.txt`", grows a list oc7:228 says only shrinks. Its table (dl56:283-295) has no row for unit 3 or unit 17. Probe: `grep -n -E '/| /`loop (transition record|computed witness)/`' dl56` printed nothing (exit 1).
  - Change: each leg-adding unit writes its leg's `enforces` in its own pass, and its AC checks it the way dl6 AC8 does. dl56 S4 drops the pending-row fallback and adds units 3 and 17. Revision rev-4 (dl1) and rev-3 (dl3, dl6, dl17), §2 and §6.

- **dl3 and dl17 bind typed records as `journal`.**
  - dl3:123 "`**Serves:** journal TOOL-dExample-1`" and dl3:133 "The `journal` binding kind is check 21's …"; dl17:34 "`**Serves:** journal <unit id>`".
  - oc7:165 hands oc42 "the three typed record kinds … joined to their file names, and the factory's kind list made the reader's".
  - oc42:45-49: "a file named `-<kind>-<n>.md` in a `build/` folder whose Serves kind is not `<kind>` is malformed". oc42:158-161 is this exact case: a `-change-1.md` file whose Serves line says `journal` reads `malformed`.
  - oc42:40-44: the factory's kinds must equal `TYPED_RECORD_KINDS`, or loading fails.
  - Change: the records serve as `transition <id>` and `acceptance <id>`. Each unit also adds its kind to `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py` and to the closed kind list in `tools/memory-tree/HYGIENE.template.md` (oc42 S5). The flood argument at dl3:133-134 is restated on that binding. Revision rev-3, §2 S2/S1 and §4.

- **dl16 and dl22 never add their kind to the reader's list.**
  - dl16:102 "`**Serves:** disposition TOOL-tFix-1`" and dl22:118 "`**Serves:** recommendation <first unit id>`". Each touches only `tools/memory-tree/build_records.py`.
  - oc42:40-44: "imports `TYPED_RECORD_KINDS` from `tree_lib` as its kind list … refused at import … when its keys differ from that tuple." oc42:94-95: a Serves token outside `RECORD_KIND_TOKENS` is malformed.
  - Change: add `tools/memory-tree/tree_lib.py` (`TYPED_RECORD_KINDS`) and `tools/memory-tree/HYGIENE.template.md` to Files touched, and add an AC that the record binds (`print-bindings` names it). Revision rev-3.

- **dl6 S1's Readers line.**
  - dl6:40-43: "minted by PLAY-dOrderedCharter-7, DEFERRED at rev-3 … its meta-check is the only reader, and it reds each of the six rows as stale".
  - oc7:3 is "rev-5". oc7:72-73: `core.py kinds` checks "a kind row out of the pending list". oc7:61-62 keys the meta-check's pending rows as "`principle`, `practice` or `leg`".
  - Change: cite rev-5, name `core.py kinds` as a reader of the `kind` rows, and state the stale arm as UNKNOWN until oc7 builds (§3 below). Revision rev-3, S1.

- **dl46's evidence pins `KNOWN` without `enforces`.**
  - dl46:71-72: "`KNOWN` holds `name argv guard impure reads chunk subject ceiling signature doc_reads` in both copies … PINNED 2026-10-24".
  - oc7:167: "`enforces` already in both canary key sets at order 10". oc50:37-39: both `KNOWN` copies "gain `enforces`, with a control pair".
  - Change: the evidence states the key set dOrderedCharter will have landed (`enforces` included), so S1's edit and AC1 are read against that set. Revision rev-3, §4 Evidence.

3. UNKNOWN UNTIL BUILT

- dl1, how the renderer reads the integer: oc6's build of S3 decides whether the sort reads `workflows.toml` directly, through `roles_lib`, or by subprocess, and how a missing key behaves. That fixes which call dl1 S9 re-points.
- dl1, `handoff.py`: oc6's build of S5 decides whether `render_handoff` orders a role's drive lines by `stage`. If it does, dl1 S5's "never reads `stage`" and AC5 no longer hold.
- dl3, dl16, dl22, the `new` door: oc7's build of S7/S8 decides whether `build_records.py new` is generic per kind, with each kind's own flags, or carries only an `exception` arm.
- dl6, the stale arm: oc7's build of S3/S4 decides whether a `kind` pending row whose factory and gate have landed is red as stale, and which verb reds it.
- dl6, the seeded `binds`: oc7's build-pass seed of `kinds.toml` from foundations C3 decides `kind.role`'s `binds`.

4. Per spec

- dl1: 3 AGREES · 2 MISMATCH · 2 UNKNOWN. oc6's rev-4/rev-5 moves (S6, S7, the new S9 `budgets.py home`, AC6-AC8, F4, F5) are not depended on.
- dl3: 2 AGREES · 2 MISMATCH · 1 UNKNOWN. oc7's rev-4/rev-5 moves (S9-S12, §4 "The policy reads", `read_policy_value`, `owner-only-expiring`) are not depended on.
- dl6: 6 AGREES · 2 MISMATCH · 2 UNKNOWN. oc7's rev-4/rev-5 moves (S9-S12, the policy reads) are not depended on.
- dl16: 2 AGREES · 1 MISMATCH · 1 UNKNOWN. oc7's rev-4/rev-5 moves are not depended on.
- dl17: 1 AGREES · 2 MISMATCH · 0 UNKNOWN. oc7's rev-4/rev-5 moves are not depended on.
- dl22: 1 AGREES · 1 MISMATCH · 1 UNKNOWN. oc7's rev-4/rev-5 moves are not depended on.
- dl46: 1 AGREES · 1 MISMATCH · 0 UNKNOWN. oc7's rev-4/rev-5 moves are not depended on.

Files cited:
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-{1,3,6,16,17,22,46,56}.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-6.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md
- memory/builds/dOrderedCharter/spec/ (the PLAY-dOrderedCharter-42, -50 and -30 specs)

## Group B

Group B (specs 2, 24, 25, 26, 28) checked against dOrderedCharter as it stands at `462d20f35`. Verdict totals: 29 AGREES, 9 MISMATCH and 4 UNKNOWN UNTIL BUILT. Every probe was a read.

**1. Assumptions**

| Spec | Assumption about dOrderedCharter | Verdict | Evidence |
|---|---|---|---|
| 2 | oc15 S4 refuses every instruction write until a core layer row declares `point.instructions.guard` | AGREES | dl2:88, dl2:160-161; oc15:72-74 |
| 2 | oc15 S5 refuses `signed`/`both` at load until `point.instructions.signed-proof` is declared | AGREES | dl2:161-162; oc15:81-82 |
| 2 | oc15's two load refusals (`flow-only`, `signed`/`both`) can be re-pointed to one function | AGREES | dl2:85-86, dl2:441-443; oc15:69-71, oc15:81-82 |
| 2 | F7: oc15 S4 accepts any core row | AGREES | dl2:446; oc15:73 |
| 2 | `instructions_edit.py`'s terminal check is stdin plus a typed `yes`, so it can become the shared `check_terminal_proof` block | MISMATCH | dl2:64-70, dl2:197, dl2:219-220; oc15:77-81, oc15:346-348, oc7:104-108 |
| 2 | The `change` record kind (S12/S13) exists for the same commit | AGREES | dl2:115, dl2:132; oc15:96-101 |
| 24 | `[[kind]]` row in `kinds.toml`, the `kind` namespace's declaring source | AGREES | dl24:32, dl24:209-210; oc7:66-71 |
| 24 | `core.py new <kind> <name>` runs the kind row's `factory` | AGREES | dl24:57-59; oc7:76-77 |
| 24 | The gate leg's `enforces` holds the kind's `binds` | AGREES | dl24:64-65; oc7:55-57, oc7:72-75 |
| 24 | The optional `schema` key on a kind row | AGREES | dl24:35-36; oc35:98-103 |
| 24 | `compose_rows`; a gov row changes only through a pinned `amends` | AGREES | dl24:43-46; oc35:53-56, oc35:75-78 |
| 24 | The landed revision is oc46 S1's (`HEAD`) | AGREES | dl24:44; oc46:42-47 |
| 24 | Schema fields declare `shape`, `ref`, and `fixed-by` or `widens` | AGREES | dl24:39; oc36:39-45 |
| 24 | A `floor=` source "reads unarmed" until the floor's tags register | MISMATCH | dl24:132-133; oc36:160-162 |
| 24 | Exclusions are refused naming the requirer, or naming `review.breakpoints` | AGREES | dl24:53-56; oc36:55-59, oc36:183-189; the dGroundRules catalogue at `df4912bd`:673 types `review.breakpoints` as a `set` |
| 24 | `check_rows(kind, schema, composition, exclude, policy)` | AGREES | dl24:156; oc36:69-71 |
| 24 | oc36 S5's three widening forms (`add`, `remove`, ordered list) | AGREES | dl24:297; oc36:61-65 |
| 24 | The overlay's one door carries the owner's proof | AGREES | dl24:218-219; oc15:65, oc15:77-81 |
| 24 | How the `exclude-breakpoint` plant's policy value reaches oc36's read at `--rev HEAD` | UNKNOWN UNTIL BUILT | dl24:257-260; oc36:186-189, oc36:69 |
| 25 | The splice schema follows oc36 S1, with `exit` "open, widening by `add`" | MISMATCH | dl25:35, dl25:124, dl25:143-144; oc36:153-156 |
| 25 | `[[splice]]` overlay tables read by `read_overlay_rows` and composed by `compose_rows` | AGREES | dl25:34-38; oc35:41-46, oc35:182-183 |
| 25 | `pin` is hashed by oc35 S6's normaliser | AGREES | dl25:49-50, dl25:123; oc35:75-77 |
| 25 | An exclusion of `step.test` is an "overlay exclusion", planted in a fixture with no policy file | MISMATCH | dl25:162-163, dl25:168; oc35:60-67, oc46:65-71 |
| 25 | oc36 leaves the flow's frame to the kind's build | AGREES | dl25:79-80; oc36:83-84 |
| 25 | `read_kind_schema` and the change records' `Successor` | AGREES | dl25:52-55, dl25:92; oc36:45, oc15:100 |
| 25 | The factory `instructions_edit.py add --manifest overlay` writes a `[[splice]]` row | UNKNOWN UNTIL BUILT | dl25:138; oc15:55-58, oc15:273-275, oc35:122-123 |
| 26 | The composition revision is dGroundRules' landed revision, and "at that commit" the overlay is oc46 S1's blob | MISMATCH | dl26:31-35; oc46:42-47, oc46:122-124 |
| 26 | Gov's packs are the "`population` files" of every kind row | MISMATCH | dl26:34-35, dl26:114-115; oc7:69 |
| 26 | `compose_at(root, rev)` composes at an older commit through oc46 S3 and `compose_rows` | MISMATCH | dl26:43-46, dl26:114-116; oc46:65-68, oc46:78, oc36:186-187, oc35:64-66, oc35:196 |
| 26 | Successor read through oc19's resolver over the index rows oc15 S9 writes | AGREES | dl26:53-55; oc19:75-90, oc15:114-117 |
| 26 | The redirect "between `old` and `new`" revisions | UNKNOWN UNTIL BUILT | dl26:123-125; oc19:64-74 |
| 26 | The tag-valued keys are those oc36 S4 reads | AGREES | dl26:65-66; oc36:183-184 |
| 26 | The mechanism belongs to oc35, -32 and -46; the update report and row states to oc34 | AGREES | dl26:82-83, dl26:90; oc35:95-96, oc34 S6 |
| 26 | The `Successor` field is oc15 S7's | AGREES | dl26:265; oc15:100 |
| 28 | The four acts are oc35's row operations | AGREES | dl28:35-38; oc35:41, oc35:53, oc35:57, oc35:60 |
| 28 | Proposed rows sit in the change record's `After` field as a TOML fence | MISMATCH | dl28:40-44; oc15:98-100 |
| 28 | "the change record already carries rows" | MISMATCH | dl28:169-170; oc35:80-81 |
| 28 | Additive vs loosening read from oc36 S5's classifier | AGREES | dl28:47-49; oc36:61-64, oc36:165-175 |
| 28 | A build's changes compose as the last layer, after the scenarios, through `compose_rows` | UNKNOWN UNTIL BUILT | dl28:60-62; oc35:182-194 |
| 28 | The overlay and its guarded write belong to oc15 and oc32 | AGREES | dl28:81; oc35:122-123 |

**2. Mismatches**

- **dl2 S5: the shared terminal proof.**
  - dl2:197: "`check_terminal_proof`: stdin a terminal and the typed confirmation `yes`".
  - dl2:69-70: "`instructions_edit.py`'s own terminal check is re-pointed to the inline block in the same unit".
  - oc15:77-81 (rev-5, the owner's pick): "`tty-cli` … is the owner's presence shown as standard error being an interactive terminal … the command tests `sys.stderr.isatty()` itself".
  - oc15:346-348: "one stream, stderr … RESOLVED (owner, 2026-10-25): (a). PLAY-dOrderedCharter-7's `core.exceptions: owner-only-expiring` proof is this check".
  - The text at the dl base (`96526383c`), oc15:71-72, said "standard input", so this moved with the re-ground. Re-pointing oc15's check would quietly switch the owner-settled proof, and with it oc7 S9's, to stdin. oc15 AC3 (oc15:261-264) would then fail.
  - Change: make `check_terminal_proof` test `sys.stderr.isatty()`, as oc15 S5 and dGroundRules' `[ -t 2 ]` do. If the typed `yes` stays, note it as a step only `policy_edit.py` adds, outside the parity block. Re-word dl2:197 and dl2:219-220 to match, change AC8's `</dev/null` to a stderr redirect, and cite oc15 F4 as the owner's settlement.
- **dl24 §4 The schema: a `floor=` source before its namespace registers.**
  - dl24:132-133: "A `floor=` source resolves once the floor's tags are registered (dOrderedCharter-36 S2), and reads unarmed until then."
  - oc36:160-162: "before it registers, the source is refused naming the namespace, so no kind claims a floor that does not exist."
  - This text predates the re-ground, but oc36 is a revised unit. As written, `item.test.verdict`'s `fixed-by = ["floor=floor.verdict-before-move"]` makes `read_kind_schema` refuse the schema, and the `loop item kind` leg goes red at landing.
  - Change: either name the unit that registers a `floor` namespace before unit 24 (dl2 makes the members policy-map values, not tags), or use a `principle=` or `parser=` source for `item.test.verdict` until it registers. Drop "reads unarmed".
- **dl25 §4 Data model: `exit` is a scalar declared as widening by `add`.**
  - dl25:124: `exit = "item.adopter.security-review.exit"`.
  - dl25:143-144: "`exit` is open, widening by `add`".
  - oc36:155-156: the reader refuses "a set field whose `widens` is not `add` or `remove`; a scalar whose `widens` is not a list of at least two distinct values".
  - Change: declare `exit` fixed, or give it an ordered-list `widens`. `add` is only legal on a set field.
- **dl25 §4 fixture `removes`: the exclusion's source.**
  - dl25:168: "`removes` | an overlay exclusion of `step.test`".
  - dl25:162-163: the fixture holds "gov's loop definition, an overlay and a change-record folder".
  - oc35:60-67 (rev-4): exclusion is `instructions.exclude`, "read with `policy_reader("instructions.exclude")` … passing `--rev HEAD`".
  - oc46:65-71: every composition read is at `--rev HEAD`, and with no commit the value is the default `[]`.
  - As written, the plant excludes nothing, so it cannot go red for the reason it names.
  - Change: have the plant commit `.governance/policy.toml` with `[instructions] exclude = ["step.test"]` as the fixture's `HEAD`, and say the exclusion is the policy key, not an overlay row.
- **dl26 S1: which revision the composition is.**
  - dl26:31-34: "the default branch's landed revision dGroundRules-2 S1's `derive_landed_revision` returns … At that commit the overlay is the blob `.governance/instructions.toml` (dOrderedCharter-46 S1)".
  - oc46:45-47 (rev-3): "It is the node's own last commit, not dGroundRules' landed revision, the remote ladder's ref (TOOL-dGroundRules-2 S1)".
  - Change: either define the composition revision as `HEAD`, as oc46 S1 does, or keep the remote-ladder ref and stop citing oc46 S1 for the overlay read at it. Either way, state which of the two the pin names.
- **dl26 S1 and §4: kind populations.**
  - dl26:34-35: "gov's packs are the `population` files of every `[[kind]]` row".
  - dl26:114-115: "the `population` blobs at `rev`".
  - oc7:69: "`population` (a tracked-path glob or a reader command)".
  - dl24 itself registers `population = "python {prefix}/loop/loop_items.py members"` (dl24:101), and dl25 does the same (dl25:137). A reader command has no blobs to read at a revision.
  - Change: say how a reader-command population is read at `rev`. For example, run the command in a worktree checked out at `rev`, or require each such reader to take a `--rev`.
- **dl26 S3: composing at an older revision.**
  - dl26:44-46: "`compose_at(root, rev)` composes every registered kind's rows from the blobs at that commit, passing the overlay through dOrderedCharter-46 S3's candidate read and composing through dOrderedCharter-35's `compose_rows`".
  - oc46:65-68 (rev-3 S6): "Every `policy.py get` the composition makes … passes `--rev HEAD`".
  - oc36:186-187: tag-valued keys are read "with `policy_reader(<key>)` at `--rev HEAD`", and oc35:64-66 reads `instructions.exclude` the same way.
  - oc46:78: "Reading a revision other than `HEAD` (a `--rev` option): no caller needs one."
  - At the pinned `rev`, the overlay and packs come from `rev` but `instructions.exclude` and the tag-valued keys come from `HEAD`. That is the split revision oc46 AC5 reds.
  - Change: either file an ask to dOrderedCharter for a `rev` parameter threaded through `compose_rows`, `check_rows` and oc46 S6, or have `compose_at` run in a worktree at `rev`. Note that dl26 is a caller that oc46:78 says does not exist.
- **dl28 S3 and §4 Alternatives: rows in the change record.**
  - dl28:40-41: "The proposed rows sit in a change record (I13, dOrderedCharter-15 S7) … its `After` field a TOML fence of overlay-grammar rows".
  - dl28:170: "the change record already carries rows (dOrderedCharter-35 S7)".
  - oc15:98-100: "`Action` (one of `WRITE_VERBS`), `Before` and `After` (each `<tag>@<hash8>` under S7's normaliser, or `none`)".
  - oc35:80-81: the record "takes a row tag of any registered kind as its subject", which is a subject, not row content.
  - `WRITE_VERBS` are `add`, `edit`, `remove`, `rename` and `split` (oc15:180), so `amend`, `exclude` and `supersede` are not legal `Action` values either.
  - Change: carry the rows somewhere the change kind admits, such as a field added by an ask to oc15 or a sibling file the record names. Map the four acts onto `WRITE_VERBS` or ask for new ones, and drop the "already carries rows" claim.

**3. Unknown until built**

- dl24 `exclude-breakpoint`: oc36 S7's `policy` argument (oc36:69) and S4's own read at `--rev HEAD` (oc36:186) could both supply the value. Which one a kind's fixture uses is decided when oc36 is built.
- dl25 factory: whether `instructions_edit.py add --manifest overlay` accepts a non-unit `[[splice]]` row. Its flags are unit-shaped (oc15:273-275), and oc15's build run decides it.
- dl26 S4: oc19's resolver serves a worktree's `HEAD` tree (oc19:64-74). Whether it can answer a redirect between two arbitrary commits is decided by oc19's build.
- dl28 S6: `compose_rows` takes one gov layer and one overlay layer (oc35:182). Whether further layers (scenarios, then a build's own changes) stack through repeated calls is decided by oc35's build. The pin dl28 reads also inherits dl26's revision mismatch.

**4. Per spec**

- **dl2:** 5 AGREES · 1 MISMATCH · 0 UNKNOWN. It cites one revised unit, oc15, and its assumptions depend on it.
- **dl24:** 11 AGREES · 1 MISMATCH · 1 UNKNOWN. Every revised unit it cites (7, 15, 35, 36, 46) carries at least one assumption.
- **dl25:** 6 AGREES · 2 MISMATCH · 1 UNKNOWN. It cites oc35 and oc36, and both carry assumptions. It also leans on oc15 (change records, the `instructions_edit.py` factory) without citing it by number.
- **dl26:** 5 AGREES · 3 MISMATCH · 1 UNKNOWN. Every revised unit it cites (7, 15, 19, 34, 35, 36, 46) carries an assumption. Its rev-1 still says these units were "read at base `ed497191`" (dl26:250), which is stale since `555e623a7`.
- **dl28:** 2 AGREES · 2 MISMATCH · 1 UNKNOWN. It cites oc15, oc35 and oc36, and all carry assumptions.

Files: `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-{2,24,25,26,28}.md`, and `memory/builds/dOrderedCharter/spec/` (`2026-10-23-spec-PLAY-dOrderedCharter-{7,15,19,34,35,36}.md` and `2026-10-24-spec-PLAY-dOrderedCharter-46.md`).

## Group C

| Spec | Assumption about dOrderedCharter | Verdict | Evidence |
|---|---|---|---|
| 4 | The gate-leg `stage` field copies the pattern of the `enforces` field from OC-7 S2 | AGREES | dl4:41-42 · oc7:55-57 is unchanged since `96526383c` (the `git diff` shows S2 untouched). OC-19 S12 (oc19:136) shows that a new leg key also has to join the canary's `KNOWN` set (`run-gates.test.sh:244,580`) |
| 4 | OC-19 S9 moves the coverage factory into `tools/lib/coverage_join.py` and ships it in `tools/memory-tree/coverage_join.py` | AGREES | dl4:71-73, dl4:86 · oc19:113-117. Rev-4 and rev-5 changed only S9's re-export hold (oc19:439-441) |
| 4 | The loop kit requires `memory-tree` and imports the join the same way codebase-map does | AGREES | dl4:65-66 · oc19:118-119 ("rewritten to import the four names from memory-tree's module") |
| 4 | `compute_coverage` sits at `map_lib.py:1404` today and is moved without a rewrite | AGREES | dl4:270-272 · oc19:114-115 · a grep of the code printed `1404:def compute_coverage(` |
| 4 | The new leg `loop stage coverage` can land as a plain row of `tools/gate-legs.json` | MISMATCH | dl4:58-61 · oc7:61 |
| 5 | `resolve_compare_base` is part of OC-19 S9's join factory | AGREES | dl5:111-112 · oc19:113-114 |
| 5 | `resolve_compare_base` is lifted from `map_lib.py:1502` | AGREES | dl5:254 · oc19:115 · the code grep printed `1502:def resolve_compare_base(root: Path)` |
| 5 | The function is read from `tools/lib/coverage_join.py` | MISMATCH | dl5:111-112 · oc19:115-119 |
| 27 | A `[[kind]]` row `kind.scenario` in `tools/playbook/kinds.toml`, in the OC-7 S4 shape | AGREES | dl27:33-34 · oc7:66-71 is unchanged |
| 27 | The factory arm is `core.py new scenario <name>` (OC-7 S6) | AGREES | dl27:35 · oc7:76-77 ("`core.py new <kind> <name>` … runs the kind row's `factory`") |
| 27 | The factory writes a repository row `scenario.adopter.trial` (AC7), and the unit adds no new write path | MISMATCH | dl27:245-246, dl27:206-207 · oc35:122-123, oc15:72-74 |
| 27 | The kind row's `schema` key names `scenario-schema.toml` (OC-36 S1) | AGREES | dl27:36 · oc36:39-40 points to OC-35's optional `schema` key (oc35:98-103) |
| 27 | The `[[namespace]]` row is OC-19 S4's | MISMATCH | dl27:38, dl27:302 · oc19:51 (S2 is the registry), oc19:64 (S4 is the index) |
| 27 | A repository tag `scenario.adopter.<name>` sits in the owner seat | AGREES | dl27:39 · oc35:47-52, oc35:98-101 (`owner-seat`) |
| 27 | `activates` uses OC-35's overlay row grammar | AGREES | dl27:42-43 · oc35:53-58, oc35:170-173 |
| 27 | `activatable` is a set field declared `widens = "add"` | AGREES | dl27:46-47 · oc36:61-62 |
| 27 | `compose_rows` composes, and every check reads the composed result | AGREES | dl27:62-64 · oc36:69-71 (`check_rows` is called by `compose_rows`) |
| 27 | The scenario list enters `compose_rows` after the overlay's rows and before the recorded changes | UNKNOWN UNTIL BUILT | dl27:132-133 · oc35:182-183 (`compose_rows(kind, gov_rows, overlay_rows, exclude, stale_mode, records)`, which has only two row layers) |
| 27 | A build's composition is read at the pin TOOL-dDeclaredLoop-26 records | MISMATCH | dl27:104 · oc35:64-66, oc35:196 (rev-4) |
| 27 | Overlay writes are guarded by OC-15 | AGREES | dl27:206-207 · oc15:72-76. Rev-5 only moved the proof to stderr, which dl27 does not depend on |
| 27 | OC-37 renders the scenario kind's reference page from the registry | MISMATCH | dl27:99, dl27:216-217 · oc37:50, oc37:118, oc37:82-96 (rev-4) |
| 27 | The `kind.scenario` row needs no `summary` or `usage` | UNKNOWN UNTIL BUILT | dl27:33-36 · oc7:66-69 lists no such field · oc37:55, oc37:142-148 require both fields of every kinds-page row |
| 27 | The OC-7 S5 conformance gate reads `kind.scenario` clean | MISMATCH | dl27:266, dl27:245-247 · oc7:72-74, oc7:61 |
| 27 | F2: later layers take precedence, read from OC-35's layering | AGREES | dl27:277-278 · oc35:185-194 (overlay over gov through edges) |
| 33 | `check` composes gov's composition with `compose_rows` over gov's packs and the overlay | AGREES | dl33:35-37 · oc35:182-196 |
| 33 | `check --build <slug>` composes "as TOOL-dDeclaredLoop-28 S6 composes a build", at that build's pin | MISMATCH | dl33:36-37 · oc35:64-66, oc35:196 (rev-4) |
| 33 | A loop-bound raise in the overlay appears in `derive_widenings`, and the update report names it | AGREES | dl33:67-68 · oc36:66-68 |
| 33 | A raise of a numeric loop bound (the budget, rounds, retries, a deadline) is classified `widens` | MISMATCH | dl33:58-59, dl33:67-69 · oc36:61-64 |
| 33 | The pending list follows the house pattern of OC-7 S3 | AGREES | dl33:298-299, dl33:325 · oc7:61-65 |
| 33 | The leg carries `enforces = ["principle.p39"]` | AGREES | dl33:76 · oc7:50-51 (`principle.p<n>`, P1 to P42), oc7:55-56 |
| 55 | The leg's inputs are what `compose_rows` composes, and the working-tree fingerprint covers them | AGREES | dl55:58-60, dl55:30-32 · oc35:196 (HEAD) · `tools/run-gates/gate-fingerprint.sh` hashes `HEAD^{tree}` plus a porcelain walk, so a read pinned to HEAD is inside the key |

**MISMATCH**

- **dl4:58.** dl4 says: "The leg `loop stage coverage` in `tools/gate-legs.json`, argv `python {prefix}/loop/stage_coverage.py`". Its S2 gives the leg a `stage` field but no `enforces` field, and no pending row. oc7:61 says: "a leg carrying no `enforces` is red". The red can be excused only by a `leg` row of `core-pending.txt` (oc7:61-63). **Change:** S5's row needs `enforces` with the principle tags the leg enforces, or a `leg` row on `tools/playbook/core-pending.txt` naming the build that arms it. dl4 has to say which.
- **dl5:111-112.** dl5 says: "`resolve_compare_base` (PLAY-dOrderedCharter-19 S9's `tools/lib/coverage_join.py` …)". oc19:115-119 says the factory is moved "to the canonical `tools/lib/coverage_join.py`, and shipped inline in `tools/memory-tree/coverage_join.py` … consumers … rewritten to import the four names from memory-tree's module". `tools/lib` is gov-internal. **Change:** name `tools/memory-tree/coverage_join.py` as what the unattended kit imports. That kit already requires `memory-tree` (`tools/unattended/kit.toml:12`).
- **dl27:245-246, dl27:206-207.** dl27 says: "`python core.py new scenario adopter.trial` … the row it writes", and "no new write path but the record field". oc35:122-123 says: "The write door: unit 15's `instructions.edit`, the only command that writes an overlay row". oc15:72-74 says every write is refused "while no core row … declares `point.instructions.guard`". An `adopter.` tag is legal only on an overlay row (oc35:50-51). **Change:** the factory writes gov-pack rows only, and AC7 plants a gov tag. For an adopter tag the factory either delegates to `instructions_edit.py`'s write verb or prints its proposal. The §5 claim follows from that.
- **dl27:38, dl27:302.** dl27 says: "A `[[namespace]]` row `scenario` in `tools/playbook/namespaces.toml` (dOrderedCharter-19 S4)". oc19:51 says: "**S2** — The registry, `tools/playbook/namespaces.toml`: one `[[namespace]]` row per namespace". oc19:64 is "**S4** — The index, `<git-common-dir>/gov/index.db`". The numbering was the same at `96526383c`, so the re-ground did not cause this. **Change:** cite OC-19 S2 at both lines, and fill the row's required fields (`ns`, `owner`, `layer`, `source`, `extractor`, `role`, `purpose-source`, `join-armed-by`).
- **dl27:104, and dl33:36-37 (one cause).** dl27 says the composition revision is "the pin … at which a build's composition is read". dl33 says it composes "as `TOOL-dDeclaredLoop-28` S6 composes a build". oc35:196 (rev-4) says: "The composer reads gov's packs and the overlay at the landed revision, `HEAD` (unit 46 S1)". oc35:64-66 says `instructions.exclude` is read "passing `--rev HEAD` as PLAY-dOrderedCharter-46 S6 rules for every read the composition makes". So a build pinned at an older revision gets HEAD's exclusions. **Change:** dl27 and dl33 should state that a pinned composition reads `instructions.exclude` at the pin and passes it to `compose_rows`'s `exclude` argument. That departs from OC-46 S6, so it needs an ask to dOrderedCharter, or a deviation recorded by TOOL-dDeclaredLoop-26 (Group B's spec), which owns `compose_at`.
- **dl27:99, dl27:216-217.** dl27 says: "No reference page of the kind's rows: dOrderedCharter-37 renders those from each registry". oc37:50 says: "A later registry joins by adding its row, which its own build lands". oc37:118 says: "Reference pages for registries a later build lands: each lands its own `[[reference]]` row". Rev-4 adds that each class is "registered there first" in `tools/govkit/surface-classes.toml`, with a reader and a plant (oc37:82-96). It also says a row with no `summary` or no `usage` refuses the render (oc37:55). Separately, the `kind` class now grades `kind:kind.scenario` on `help/reference/kinds.md`, which dl27 does not list among the files it touches (dl27:185-194). **Change:** dl27 should land a `[[reference]]` row, a `scenario` class row in `surface-classes.toml` and a `usage.toml` `[[class]]` row, and give scenario rows `summary` and `usage`. Or it should defer the page by name. Either way it should re-render `help/reference/kinds.md` in the commit that adds `kind.scenario`.
- **dl27:266, dl27:245-247, dl27:83-85.** dl27 says: "New arm: the kinds register's conformance gate dOrderedCharter-7 S5 runs … the register before the `kind.scenario` row", and AC7 expects "the kind's gate reads it clean". The row names no `binds` and no `gate`, and the leg `loop scenario fixtures` carries no `enforces`. oc7:72-74 says: "a kind row out of the pending list names a `factory` command that exists and a `gate` leg … whose `enforces` holds every tag of the kind's `binds`". oc7:61 says: "a leg carrying no `enforces` is red". **Change:** the `kind.scenario` row needs `binds` and `gate`, the gate leg needs `enforces` that holds them, and S10's leg needs `enforces`. The alternative is to file `kind` and `leg` rows on `core-pending.txt`.
- **dl33:67-69, dl33:58-59.** dl33 says: "a raise of a loop-bound field in the overlay appears in the composition's widening list … a raise the list lacks is a finding". The populations are "the budget (`route-back-count`), a round count, a retry count and a deadline". oc36:61-64 offers three directions: "`add` on a permission set, `remove` on a constraint set …, or an ordered list on a scalar whose later values are wider … an open field with no declared direction is refused". None of these orders an unbounded number. **Change:** dl33 (or the item kind's schema, TOOL-dDeclaredLoop-12 and -24) must state the direction each loop-bound field declares, for example an ordered list of its admitted values. Otherwise it files an ask to dOrderedCharter for a numeric direction.

**UNKNOWN UNTIL BUILT**

- **dl27, the third and fourth composition layers.** OC-35's build of `compose_rows` decides how a layer beyond `gov_rows` and `overlay_rows` enters. It also decides whether rows activated by gov's own scenarios, which carry gov tags with no `adopter` seat, may sit in the overlay position without the `owned` arm refusing them (oc35:50-52).
- **dl27, the field names on a `[[kind]]` row.** OC-37's build fixes the kinds reader that is "named at the build run" (oc37:143). That reader decides which `[[kind]]` keys supply the `summary` and `usage` its render requires, since OC-7 S4 declares neither.

**Per spec**

- **Spec 4:** 4 AGREES, 1 MISMATCH, 0 UNKNOWN. Cited units the re-ground revised but no assumption depends on: none (7 and 19 are both relied on).
- **Spec 5:** 2 AGREES, 1 MISMATCH, 0 UNKNOWN. None (19 is relied on). Spec 5 also cites PLAY-dOrderedCharter-16 §4, which the re-ground did not revise, so it gets no verdict.
- **Spec 27:** 9 AGREES, 5 MISMATCH, 2 UNKNOWN. None (7, 15, 19, 35, 36 and 37 are all relied on).
- **Spec 33:** 4 AGREES, 2 MISMATCH, 0 UNKNOWN. None (7, 35 and 36 are all relied on).
- **Spec 55:** 1 AGREES, 0 MISMATCH, 0 UNKNOWN. None (35 is relied on).

The specs read are in `memory/builds/dDeclaredLoop/spec/` (files `2026-10-24-spec-TOOL-dDeclaredLoop-{4,5,27,33,55}.md`) and `memory/builds/dOrderedCharter/spec/` (files `2026-10-23-spec-PLAY-dOrderedCharter-{7,15,19,35,36,37,46}.md`).

## Group D

1. Assumption table

| Spec | Assumption about dOrderedCharter | Verdict | Evidence |
|---|---|---|---|
| 12 | `derive_load_set(units, reader, item=<tag>)` takes an item argument | AGREES | dl12:40-41 · oc11:45 `derive_load_set(units, reader, item=None)`, unchanged since rev-1 |
| 12 | An item's scope is derived from the units' `scope` field and never typed | AGREES | dl12:182-183, dl12:40 · oc11:45-48; oc9:47's `scope` row was not touched by oc9's rev-4 |
| 12 | `loop_lib.py --check` calls oc11's Python function `derive_load_set` in-process | MISMATCH | dl12:40-42, dl12:270-271 · oc11:90-94 (rev-3), oc11:140-141, oc11:201 |
| 12 | Each item's scope prints `unarmed` while no instruction unit selects an item | UNKNOWN UNTIL BUILT | dl12:41-42, dl12:223-225 · oc11:48-50 ties `unarmed` to the namespace not being registered yet, and dl18 (order 1) registers it before dl12 (order 6) |
| 18 | The `[[namespace]]` row shape is `ns`, `owner`, `layer`, `source`, `extractor`, `role`, `purpose-source`, `join-armed-by` | AGREES | dl18:33-35 · oc19:51-53 |
| 18 | The index runs every extractor whose `source` matches a blob's path | AGREES | dl18:111-112 · oc19:212-213 |
| 18 | Plants run through `gov_tag.py --fixture --plant <case>` | AGREES | dl18:50 · oc19:139-140, oc19:237 |
| 18 | `TAG_RE` is compiled once in `tag_index.py` | AGREES | dl18:292 · oc19:47-48 |
| 18 | The `resolves` check holds no family resolver | AGREES | dl18:72-73 · oc19:84-85 |
| 18 | oc19's `tags` leg runs every registered extractor, so dl18 adds no leg | AGREES | dl18:170-171, dl18:240 · oc19:134-135 |
| 18 | The catalogue is `tools/policy/catalogue.toml`, made of `[[key]]` rows with a `name` | AGREES | dl18:39-40, dl18:102 · oc19:93-94, oc19:384 (AC15 reads `['key']` and `r['name']`) |
| 18 | The policy join imports `read_catalogue_row` in-process through `resolve_kit_dir("policy", "policy.py", here)` | MISMATCH | dl18:46-48, dl18:137-140 · oc19:99-102 (rev-4), oc19:457 |
| 18 | `step` and `item` are selectors that a unit's `scope` names | AGREES | dl18:105 · oc11:48-49 |
| 18 | `[[drive]]` is a descriptor table govkit does not read, and its `command` field is free text with no verb | AGREES | dl18:153-154, dl18:258-259 · oc6:41-45, oc6:333-335; oc6's rev-4 and rev-5 touched S6 and S9 only |
| 34 | `derive_change_mark` lives in `tools/playbook/pins.py` and returns `editorial` or `semantic` | AGREES | dl34:47-51 · oc33:47-53, unchanged by rev-3 and rev-4 |
| 34 | The classifier and its spelling map are oc33's, called and never re-specced | AGREES | dl34:75-76, dl34:235 · oc33:50, oc33:150 |
| 34 | `deviation_join.py` (memory-tree kit) calls `pins.py` (playbook kit) in-process "as an optional slot" | MISMATCH | dl34:51-52, with dl34:35 using "imported … as an optional slot" · oc33:90 (rev-3), oc33:349 (F4, rev-3) |
| 34 | The caller gets the first differing word to name in its refusal | UNKNOWN UNTIL BUILT | dl34:49-50 · oc33:47, oc33:52-54: the function returns a mark, and the word is named only by oc33's own red |
| 34 | `derive_change_mark` can be called on a deviation record's `Before` and `After` alone | UNKNOWN UNTIL BUILT | dl34:48-49 · oc33:47 signature `(before, after, spelling, ruling)`; oc33:151-153 defines a ruling as a change record's `**Ruling:**` field with a signed proof |
| 56 | `owed_rows.py` (in `tools/run-gates/`) prints a pass's owed rows | AGREES | dl56:89-90 · oc50:42-45, oc50:80 |
| 56 | The set `owed_rows.py` prints is the set S4 owes (`[[gate_leg]]` with `chunk` and `subject`, plus `enforces` or a `core-pending.txt` row) | MISMATCH | dl56:86-90 · oc50:49, oc50:50; `grep -n core-pending` on oc50 prints nothing |
| 56 | Whether "that parent has landed" by dl56's pass (order 36) | UNKNOWN UNTIL BUILT | dl56:90 · oc50:3 (order 10, DEFERRED) |

2. Mismatches

- **dl12, the load-set call.** dl12:40-42 says: "PLAY-dOrderedCharter-11 S1's `derive_load_set(units, reader, item=<tag>)`, printed by `loop_lib.py --check` per item". oc11's rev-3 at oc11:90-93 says: "finds `load_sets.py` through `resolve_kit_dir` and runs its `check` verb as a subprocess … since a kit may not import a sibling kit (TOOL-dGroundRules-1 §4 Evidence)". The verbs are listed at oc11:141 as "`derive`, `check` and `injected`", and the `derive` usage at oc11:201 takes only `--reader` and `--units`, with no item flag. The loop kit is a sibling kit: dl1:46 creates `tools/loop/` with its own `kit.toml`. dl12's text was written before rev-3 landed (`555e623a7` is not an ancestor of `96526383c`).
  - Change: re-point dl12 S4 to find `load_sets.py` through `resolve_kit_dir`, run `derive --reader … --units <fixture> --item <tag>` as a subprocess, and print `unarmed` when the playbook kit is absent, as oc11:93-94 does.
  - Revision needed: a dl12 rev-3. It also needs an edge asking oc11 for an item argument on `derive`, because oc11 does not name one.
- **dl18, the policy join.** dl18:137-140 says: "the join imports that matcher through `resolve_kit_dir("policy", "policy.py", here)`, the import PLAY-dOrderedCharter-10 S7 makes". oc19's rev-4 at oc19:101-102 says the playbook kit "carries its own inline `resolve_kit_dir` block, since a kit imports no sibling kit, and runs `policy.py get <key> --explain` as a subprocess". oc19:457 adds "never importing the sibling kit". The precedent dl18 cites is also not an import: oc10:68-69 reads the data file `namespaces.toml` through `resolve_kit_dir`.
  - Change: resolve a `policy.<prefix>.…` citation through a subprocess read of the policy kit, using oc19's `read_policy_value` in `tools/playbook/policy_value.py` or a `policy.py` verb, and treat an unknown key as undeclared. Re-state AC6's "Red when" against that call.
  - Revision needed: a dl18 rev-2 to S5, §4 "The catalogue in the `policy` namespace" and §10, adding a consumes-from edge on oc19's `policy_value.py`.
- **dl34, the classifier call.** dl34:51-52 says: "`tools/playbook/pins.py` is called as an optional slot: where it does not resolve, the typed risk stands". dl34:35 uses "imported … as an optional slot" for the same pattern. oc33's rev-3 at oc33:90 says "`run_unit_drift` … is `tools/playbook/pins.py`'s `drift` verb, since a kit never imports govkit (TOOL-dGroundRules-1 §4)". oc33:349 (F4) says "`pins.py` cannot import govkit (TOOL-dGroundRules-1 §4)". oc33 offers `derive_change_mark` only as a function: its only verbs are `drift` and `--fixture` (oc33:209-211). One caveat: the tree has a declared in-process sibling import, memory-tree's `requires_if` row for drift-audit (`tools/memory-tree/kit.toml:8`), so the rule has a precedent exception.
  - Change: either run `pins.py` as a subprocess, which needs a classifier verb that oc33 must be asked to add, or declare the import as a `requires_if` row on `tools/memory-tree/kit.toml` naming playbook and state why the dGroundRules-1 §4 rule admits it.
  - Revision needed: a dl34 rev-2 to S4, §3 Edges (today `none`) and §10.
- **dl56, the owed set.** dl56:86-90 says each row needs "its `enforces` list or a `leg` row of `tools/playbook/core-pending.txt` … each row the set PLAY-dOrderedCharter-50's `owed_rows.py` prints". oc50:49, for a leg added, owes only "a `tools/govkit/subject-pins.tsv` row; a descriptor `[[gate_leg]]` row or a `tools/govkit/registry.toml` `[[exempt_leg]]` row; a claim in a dossier". oc50:50's `key` population checks that keys are members of the `KNOWN` copies, not that a leg carries an `enforces` value, and oc50 never names `core-pending.txt`. This text predates the re-ground: oc50's rev-2 moved only the size population.
  - Change: S4 should take only the `[[gate_leg]]` part from `owed_rows.py`. It should keep its own list for the `enforces` and `core-pending` part, and reject an `[[exempt_leg]]` row as an answer.
  - Revision needed: a dl56 rev-4 to S4 and AC3.

3. Unknown until built

- **dl12, `unarmed`:** oc11's build decides what `derive_load_set` returns for an item once the item namespace is registered and no unit selects it: still `unarmed`, or an empty item part that dl12 must print as `unarmed` itself.
- **dl34, first differing word:** oc33's build decides whether `derive_change_mark`, or a sibling call, gives a caller the first differing word, or whether only oc33's own red computes it.
- **dl34, `spelling` and `ruling`:** oc33's build decides which `spelling` map and `ruling` a non-change-record caller passes. The parameters are fixed at oc33:47, and the ruling is defined only for change records at oc33:151-153.
- **dl56, landing order:** dOrderedCharter's build run decides whether `owed_rows.py` (order 10) has landed before dDeclaredLoop's order 36 pass. That picks which branch of dl56:90 applies.

4. Per spec

- **dl12:** 2 AGREES, 1 MISMATCH, 1 UNKNOWN. It cites only oc11, which its assumptions depend on. oc11's rev-3 and rev-4 changes to S2 (`instructions.checks` read), S3 (budgets, and `CODEX_MAX` read through `budgets.py home`), AC6 and §8 F2/F4 bear on none of them.
- **dl18:** 9 AGREES, 1 MISMATCH, 0 UNKNOWN. Every revised unit it cites (6, 11, 19) is depended on in part. The revised parts it does not depend on are oc6's rev-4 and rev-5 (S6, S9 `budgets.py home`), oc11's rev-3 and rev-4 (S2 to S4), and oc19's rev-5 (S9 hold settled).
- **dl34:** 2 AGREES, 1 MISMATCH, 2 UNKNOWN. oc33 is depended on through S1 only. Its rev-3 S3/S5/S7/S8 changes (the `drift` verb, the `instructions.stale` read, the usage row, the catalogue fill) and its rev-4 (`rev="HEAD"`) bear on nothing except the restated kit rule.
- **dl56:** 1 AGREES, 1 MISMATCH, 1 UNKNOWN. oc50 is depended on through S2's leg-added row. Its rev-2 size population (`budgets.*` caps through `budgets.py resolve`) bears on none of them.

Every probe only read files; nothing was written. The files are:
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-12.md
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-34.md
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-56.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-6.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-11.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-33.md
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-50.md
