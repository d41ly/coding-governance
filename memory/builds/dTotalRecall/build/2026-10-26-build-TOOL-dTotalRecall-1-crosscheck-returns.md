**Serves:** research TOOL-dTotalRecall-1

# dTotalRecall — the cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record
[`2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck`](2026-10-26-build-TOOL-dTotalRecall-1-parents-crosscheck.md)
is assembled from, each copied from its agent transcript. Group A, citation read specs 1, 2, 3, 4, 6, 11, 18, 19, 59, 62, 68, 76 and 88; Group B, rule-wide, legs read specs 7, 8, 9, 14, 15, 16, 22, 23, 26, 36, 43, 47, 48, 50, 53, 69, 75, 77 and 79; Group C, rule-wide, kinds and kits read specs 5, 20, 25, 40, 42, 51, 81, 87, 92, 93 and 94.

## Group A, citation

## dTotalRecall Group A cross-check, against the parents at `c8d46e188`

I checked all 13 specs of Group A (1, 2, 3, 4, 6, 11, 18, 19, 59, 62, 68, 76, 88). Of 37 rows, 15 are MISMATCH, 4 are UNKNOWN UNTIL BUILT and 18 agree.

### 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | The factory defines `probe` and `probe-trigger`, which the registry rows | cite | AGREES | tr1:59-64; pr7:91-103 |
| 1 | A factory kind's `writer` is `build_records.py new <kind>`, for example `new probe` | cite | MISMATCH | tr1:174-175, :197; pr7:104-106; pr2:115-116; wb1:76-89; wb14:63 |
| 1 | The legacy population is seeded once by `seed_population` | cite | AGREES | tr1:84-88; wb15:36-39 |
| 1 | F1: pr1 §3 is the non-goal giving the factory to dConvergedCharter, at line 137, and an ask re-points it | cite | MISMATCH | tr1:348-353; pr1:145-146 |
| 1 | The new leg `record-kinds` carries no `enforces`, and `kind.record-kind` leaves `core-pending.txt` | R1 | MISMATCH | tr1:66, :91-93, :98-101; oc7:61-63, :72-74 |
| 1 | "The five Serves kinds of `RECORD_KIND_TOKENS`", with `deviation` given its own row: writer `hand`, source `deviation_join.py:REQUIRED` | R2 | MISMATCH | tr1:59-60, :192; oc42:35-39, :40-44; oc7:93-96 |
| 1 | `schema.source = build_records.py:<its field tuple>`, a module-level literal per kind | R2 | UNKNOWN UNTIL BUILT | tr1:165-168, :197; oc42:40-44, :156 (`build_records.KINDS`) |
| 2 | Whether this session holds the build lease is read through `unattended.sh --claims` | cite | MISMATCH | tr2:183-185; pr1:90-92, :207-208, :396-397; `tools/unattended/unattended.sh:2204` (`cut -f1-5`) |
| 2 | AC5: a local-only lease ref in the clone is the authority the door reads | cite | MISMATCH | tr2:268-271; pr1:76-77; `unattended.sh:2088`, `:2136` |
| 2 | The door passes `leases.offline` to the claim verbs | cite | AGREES | tr2:188-190; pr1:113-120 |
| 2 | The factory has a stand-in verb `build_records.py new <kind>` generic per kind | R2 | UNKNOWN UNTIL BUILT | tr2:39-40; pr2:115-116; pr7:104-106; oc7:97-103 (only `new exception`) |
| 3 | Offline: `refuse` and `follow-leases` refuse an acquisition; `warn` queues; a lost flush prints `yield` and appends `lease-yielded` | cite | AGREES | tr3:53-58, :222-223; pr1:113-120 |
| 3 | The build lease grammar already carries `session:` | cite | AGREES | tr3:73-74; pr1:66-70, :184 |
| 3 | Other compare-and-swap mints apply `leases.offline` through the same queue functions | cite | AGREES | tr3:280-282 (cites `:139-140`); pr1:147-148 |
| 3 | `add_gov_queue` and `write_gov_queue` are the queue functions to reuse | cite | AGREES | tr3:55-58; pr1:268-272. The move into `gov_ref_sh` is tr3's own departure, recorded as deviations 31 and 32 |
| 4 | The card's ref is `refs/gov/builds/<slug>/card` | cite | AGREES | tr4:174; pr2:53 |
| 4 | The routing region reaches every build record through the kinds deviation, research and journal | cite | MISMATCH | tr4:164-176; pr2:105-107; wb51:67-69; wb1:78 |
| 4 | The legacy registration is seeded by `seed_population` at the pass SHA | cite | AGREES | tr4:153-158; wb15:36-39 |
| 6 | A local copy of the card ref, refreshed by the card's own fetch, can be matched | cite | AGREES | tr6:78-79, :140-142; pr2:81-84 |
| 6 | A local copy of the lease ref under `refs/gov/` exists and can be matched | cite | UNKNOWN UNTIL BUILT | tr6:140-142; pr1:76-77 names no cache namespace; today's cache is `refs/gov/remote/runs` (`unattended.sh:2088`) |
| 6 | The lease tip's `status:` key carries the terminal `withdrawn` | cite | AGREES | tr6:93, :136, :143; pr1:88-89, :186 |
| 11 | The new leg `shape-run records (each record equals its review line)` carries no `enforces` | R1 | MISMATCH | tr11:61-64, :171-173; oc7:61-63 |
| 11 | `shape-run` joins `TYPED_RECORD_KINDS` and the factory table, but not HYGIENE's closed kind list | R2 | MISMATCH | tr11:48-50, :177-196; oc42:57-59, :167-170 |
| 11 | The test suite reaches the parser by subprocess | R3 | AGREES | tr11:65-69 |
| 18 | `written by` reads the items whose `returns` is `record-kind.<name>` | cite | AGREES | tr18:50-52; dl12:113 |
| 18 | `read by` reads the items whose `inputs` name the kind | R4 | MISMATCH | tr18:48-49; dl12:43, :111, :127 |
| 18 | The rename keeps oc42's concatenation with `TYPED_RECORD_KINDS` | R2 | AGREES | tr18:67-70; oc42:35-39 |
| 18 | `record_kinds.py` derives its columns from the roles kit's `READ_KEYS` and `WRITE_FOLDERS` | R3 | MISMATCH | tr18:46-55, :290-291; dl12:47-51; `tools/memory-tree/kit.toml:8` |
| 19 | `Made-by` names `refs/gov/leases/<slug>/build` when the session mints under the lease | cite | AGREES | tr19:63-64; pr1:62 |
| 19 | Every tracked non-root record written after the seed carries `Caused-by` | cite | MISMATCH | tr19:85-87; pr2:107-108; pr7:93-96; wb1:78-79 |
| 19 | The new leg `record causes (…)` carries no `enforces` | R1 | MISMATCH | tr19:105-107; oc7:61-63 |
| 59 | A home absent at the base is a first seed, every row `seeded`, never `gained` | cite | AGREES | tr59:27-29, :36-38; wb51:148-151 |
| 62 | The same first-seed rule | cite | AGREES | tr62:23-24, :54; wb51:148-151 |
| 68 | wb16 derives the `memory/project/*.txt` population, keeps no old-grammar parser, and reds an unregistered home | cite | AGREES | tr68:25-28; wb16:37-41, :51-53, :335-339 |
| 76 | First seed; and a live ratchet leg with no base exits 1, printing `unresolved` | cite | AGREES | tr76:104-108; wb51:148-151, :157-158 |
| 76 | S16 reshapes the `record causes` leg row (adds `reads`) and names no `enforces` | R1 | MISMATCH | tr76:111-113; oc7:61-63 |
| 88 | wb14 S1 is the ratchet pack's verb set, `never gains` among them | cite | AGREES | tr88:92-93; wb14:36-39, :43, :125 |

### 2. MISMATCH

- **tr1, factory writers.** tr1:174-175 gives "`build_records.py new probe`" as a writer, and tr1:197 fills the factory row as "`build_records.py new <kind>`". pr7:104-106 now says "this unit claims no `new probe` or `new probe-trigger` door, and the build run re-grounds the call on the landed factory". pr2:115-116 ("No `new card` door is claimed"), wb1 (no `new gate-health` door) and wb14:63 (no `new widen` door) say the same.
  - **Change:** each factory kind's `writer` names the parent's own command (`probe.py …`, `manifest-check.sh --card …`, `drift_report.py --gate-health --write`, `ratchet.py widen`), or whatever verb the landed factory offers, re-grounded at the pass. Drop the `new probe` example.
  - **Cause:** re-ground (2740f0a3d for pr2 and pr7, 443775a2f for wb1 and wb14).
- **tr1, F1 factory ownership.** tr1:348-353 says the factory belongs to "this registry", and that pr1 §3 "(line 137)" states otherwise. pr1:145-146: "No record-kind factory: the `record kind` kind's factory is dConvergedCharter's". The parent still resolves this fork the other way.
  - **Change:** re-cite pr1:145-146, and keep the two asks (to dPlacedRequest and dOrderedCharter) as preconditions in the build run's re-ground.
  - **Cause:** pre-existing in content. Only the line number moved, at the re-ground.
- **tr1, R1.** tr1:66 adds "the new leg `record-kinds`" and S11 lists its meta-gate rows with no `enforces`; S9 takes `kind.record-kind` off `core-pending.txt`. oc7:61-63: "a leg carrying no `enforces` is red… excused only by a row of the shrink-only pending list". oc7:72-74 requires a "`gate` leg… whose `enforces` holds every tag of the kind's `binds`".
  - **Change:** S3 and S11 give the `record-kinds` row an `enforces` holding the `binds` of the `kind.record-kind` row, and AC1 or AC10 observes it.
  - **Cause:** pre-existing.
- **tr1, R2 kind list.** tr1:59-60 registers "the five Serves kinds of `RECORD_KIND_TOKENS` (`tree_lib.py:406`)", and tr1:192 gives `deviation` its own row: writer `hand`, source `deviation_join.py:REQUIRED`. oc42:35-39 makes the tuple four untyped kinds plus `TYPED_RECORD_KINDS`, `deviation` among the typed. oc7:93-96 moves each kind's required fields into `build_records.py`.
  - **Change:** register the four untyped tokens and join the factory side through `TYPED_RECORD_KINDS`, so `deviation` has one row: a factory kind, its source in the factory.
  - **Cause:** pre-existing.
- **tr2, lease holder.** tr2:183-185: "the lease … held by this session, read through `unattended.sh --claims`". pr1:207-208: "`print_claims` still prints fields 1 to 5". pr1:396-397: "rows of exactly five TAB fields", with no session field. pr1:90-92 tests `mine` by `fleet-tag` and `session`.
  - **Change:** read the holder through a surface that exposes `session` and `fleet-tag`, or file an ask for a `--claims` column or a holder verb. Through `--claims` the door cannot tell "this session" from another.
  - **Cause:** pre-existing.
- **tr2, AC5 local lease ref.** tr2:268-271: "a fixture clone holds a local lease ref `refs/gov/leases/xA/build`". pr1:76-77: `read_claims` "fetches `refs/gov/leases/*` … in one bounded fetch" from the remote, into the cache namespace (`unattended.sh:2136`). A ref that exists only locally is never read.
  - **Change:** AC5 plants the lease on the fixture's bare remote.
  - **Cause:** pre-existing.
- **tr4, routing region.** tr4:170-172 routes deviations, research and journals by kind only. pr2:107 now serves the snapshot as "`**Serves:** card <anchor id>`". wb51:67-69 serves flake and gate-health "as their own kinds". These records were `journal` at `fb872a37e`, so the region would have listed them. Now it lists none of them.
  - **Change:** add a purpose that lists every `TYPED_RECORD_KINDS` member's records (or one row per typed kind), so card snapshots, flake, gate-health, probe and widen records keep a route.
  - **Cause:** re-ground.
- **tr11, R1.** tr11:61-64 adds "the leg `shape-run records (…)` in `tools/gate-legs.json`" and names no `enforces`. oc7:61-63: "a leg carrying no `enforces` is red".
  - **Change:** S6 names the leg's `enforces` tag, and an AC reads it.
  - **Cause:** pre-existing.
- **tr11, R2.** tr11:48-50: "`shape-run` joins `TYPED_RECORD_KINDS`, and the factory's per-kind table gains its fields". Files touched (tr11:187-196) has no HYGIENE template. oc42:57-59 requires the closed kind list in `HYGIENE.template.md` to name every typed kind, and oc42 AC5 reds it otherwise.
  - **Change:** add `shape-run` to the closed `<kind>` list of `HYGIENE.template.md` and its render, and add an AC.
  - **Cause:** pre-existing.
- **tr18, R4.** tr18:48-49: "`read by` … the items whose `inputs` name the kind". dl12:111: `inputs = ["layer.memory:plan record"]  # <layer tag>:<what it reads>`. dl12:43: "every input names a layer tag". An input carries a layer tag and free text, not a record-kind tag.
  - **Change:** derive `read by` from something declared: a parent ask for a typed input reference, or the role read keys alone, with items dropped from `read by`.
  - **Cause:** pre-existing.
- **tr18, R3.** tr18:46-55 derives both columns from `READ_KEYS` (`tools/roles/roles_lib.py:36`) and `WRITE_FOLDERS` (`tools/roles/check_roles.py:99`), Python constants of the roles kit. memory-tree's `requires_if` (`kit.toml:8`) has no roles row, and dl12:47-51 restates "A kit may not import a sibling kit".
  - **Change:** name the channel: `ast.literal_eval` over the file text (tr1's own pattern), a roles verb run as a subprocess through `resolve_kit_dir`, or a declared `requires_if` row.
  - **Cause:** pre-existing.
- **tr19, causes check.** tr19:85-87: a non-root record with no legacy row is "red when it carries no `Caused-by`". The parents' kinds declare no `Caused-by`:
  - pr2:107-108, card: fields `Build`, `Step`, `Ref`.
  - pr7:93-96, probe-trigger: fields `Cause`, `Asker`, `Subject`, `At` and `Key`; probe: `Sha`, `Kind`, `Question`, `Losing`, `Asker`, `Trigger`, `Verdict`, `Writer`.
  - wb1:78-79, gate-health: `Measured`, `Verdicts`, `Legs`.

  These records are written by the parents' own commands, not by the door. So every one written after the seed reds `check_causes`.
  - **Change:** either make these kinds roots or exempt them by registry row, or file asks to the parents to add `Caused-by` to those kinds' factory fields. Reading the cause from the Serves unit, as for legacy records, is a third option.
  - **Cause:** pre-existing (the field sets are unchanged; the re-ground only retyped the kinds).
- **tr19, R1.** tr19:105-107: "The leg `record causes (…)` … with its meta-gate rows", with no `enforces`. oc7:61-63.
  - **Change:** S12 names the leg's `enforces`.
  - **Cause:** pre-existing.
- **tr76, R1.** tr76:111-113: "The `record causes` row of `tools/gate-legs.json` declares `"reads": …`", which reshapes the row and names no `enforces`. oc7:61-63.
  - **Change:** S16 also confirms or adds the row's `enforces`, and AC10 prints it beside `reads`.
  - **Cause:** pre-existing.

### 3. UNKNOWN UNTIL BUILT

- **tr1, `schema.source` per factory kind:** dOrderedCharter's build decides whether the factory keeps a module-level literal per kind or one `KINDS` table (oc42:156).
- **tr2, generic `build_records.py new <kind>`:** the PLAY-dOrderedCharter-7 build decides it. The parents now disclaim it (pr2:115-116, pr7:104-106).
- **tr6, the local name of the lease copy:** dPlacedRequest's build of pr1 S4 decides the cache namespace (`refs/gov/remote/runs` today), and tr6's match under `refs/gov/` must cover it.

### 4. Rule-wide hits the rule does not bind

None. Group A is a citation group; R1 to R8 were applied to its specs inside the table. No spec in the group touches R5 to R8.

### 5. Revised units cited but not depended on

- **tr1:** wb15 is depended on only through S1, which its re-ground did not move; pr1 only for the non-goal at :145-146.
- **tr2:** none.
- **tr3:** none. It depends on pr1 S10, which the re-ground did not move.
- **tr4:** none. wb15 is depended on through S1 only.
- **tr6:** none.
- **tr11:** wb1. Its only mention is an example record stem (tr11:142).
- **tr18:** none. dl12 is depended on for its data model and S3, not the re-grounded S4.
- **tr19:** none.
- **tr59:** none. wb51 is depended on through S30, not the re-grounded S7.
- **tr62:** none, as for tr59.
- **tr68:** none. wb16 is depended on through S1, S4 and AC1, not the re-grounded S6 or AC11.
- **tr76:** none. wb51 is depended on through S30 and S33.
- **tr88:** none. wb14 is depended on through S1, not the re-grounded S5 or AC11.

## Group B, rule-wide, legs

1. Assumptions table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 8 | The new leg `code record` can land with argv and meta-gate rows only, and no `enforces` | R1 | MISMATCH | tr8:96-100 (S13); oc7:61-63; oc7:227-228 |
| 9 | Adding a path to the `recall floor` guard needs no `enforces` from this unit | R1 | AGREES | tr9:93-96; oc7:221-223 (the pending seed holds every leg that exists at oc7's pass); wb11:57-62 (S6 gives each existing leg it reaches its `enforces`) |
| 9 | The guard is edited in `tools/gate-legs.json` itself | R1 | MISMATCH | tr9:93-96, tr9:244; wb11:36-47; `recall floor` is an `[[exempt_leg]]` at tools/govkit/registry.toml:380 |
| 9 | The `record` extractor takes the kind of the registry row whose `home` holds the path | R2 | AGREES | tr9:64-66, corrected inside dTotalRecall by tr42:52 and tr43:80-83 (the Serves kind decides, the home admits); oc42:45-49 |
| 15 | Two new legs, `map (the project map's checks)` and `map selftest`, each with a guard and no `enforces` | R1 | MISMATCH | tr15:68-74; oc7:61-63; oc7:109-111; wb11:384-396 (F5 still open) |
| 22 | The new leg `edge cardinality (per source and per target, over the merged tree)` can land with argv and `pack` only | R1 | MISMATCH | tr22:54-57, tr22:160, tr22:213-216; oc7:61-63; wb11:73-75 |
| 22 | The playbook kit's `edge_grammar.py` reaches memory-tree's `design_lib.py` in process | R3 | AGREES | tr22:121-122; tr43:210-212 (S49 declares a `requires_if` row for memory-tree); oc7:202-203 |
| 26 | The new leg `atlas selftest` lands as a kit `[[gate_leg]]` row and a manifest row, with no `enforces` | R1 | MISMATCH | tr26:104-108, tr26:201; oc7:61-63 |
| 43 | Each leg units 1, 8, 11, 19, 22 and 26 add is complete with four meta-gate rows, `enforces` not among them | R1 | MISMATCH | tr43:150-153 (S29), tr43:452-455 (AC29); oc7:61-63; oc7:227-228 |
| 43 | The factory-kinds row's writer is `gov_record.py new <kind>`, with `build_records.py new <kind>` as its alias for every factory kind | R5 | MISMATCH | tr43:49-54 (S4), tr43:359-362 (AC4); dl16:53-56, dl16:248-249; pr7:104-106; pr5:58 |
| 43 | `stream-plan` joins `RECORD_KIND_TOKENS` as an untyped kind | R2 | AGREES | tr43:67-70; oc42:35 (S1 keeps untyped tokens beside `TYPED_RECORD_KINDS`); HYGIENE's kind list is rendered from the registry (tr1:76-77) |
| 43 | memory-tree's reach into `tag_index.py` is declared as a `requires_if` row | R3 | AGREES | tr43:71-74; oc7:202-203 |

2. MISMATCHes

- **tr8 S13 (`code record`).** The spec says (tr8:96-97): "The leg `code record`, argv `python {prefix}/memory-tree/code_record.py --check`, and its meta-gate rows in `tools/govkit/registry.toml`…". It names no `enforces`. The parent says (oc7:61-63): "a leg carrying no `enforces` is red. Each red is excused only by a row of the shrink-only pending list". oc7:227-228 adds: "The pending list is written once at the build pass and only shrinks after." So `core meta-check` is red from this unit's pass onward.
  Change: S13 names the leg's `enforces` tags in its declaration. A criterion probes for them, red when the declaration carries no `enforces`, the way pr4:292-294 does. Cause: pre-existing (oc7:61 and :228 read the same at `fb872a37e`).

- **tr9 S4 (`recall floor` guard).** The spec says (tr9:93-95): "the `recall floor` leg's guard in `tools/gate-legs.json` gains `{prefix}/memory-tree/record_find.py`". The parent says (wb11:43-45): "`--write` renders `tools/gate-legs.json` from every declaration; `--check` exits 1 when the file differs". It also says (wb11:36-38) that an exempt leg's declaration "now carries the leg's whole row". `recall floor` is `[[exempt_leg]]` at registry.toml:380, so a guard edited only in the manifest reds `leg_factory.py --check`.
  Change: S4 and Files touched edit the guard in the leg's `[[exempt_leg]]` declaration and regenerate with `leg_factory.py --write`. Cause: pre-existing (wb11 S2 is at lines 40-44 of the `fb872a37e` text).

- **tr15 S11 (the `map` pack).** The spec says (tr15:68-72): "Two legs in `tools/gate-legs.json` carry `"pack": "map"` … a guard naming both modules". It names no `enforces`. The parent says (oc7:61-63): "a leg carrying no `enforces` is red". The parent also says (oc7:109-111): "`never` makes the meta-check red any leg whose `enforces` is non-empty and which carries a `guard`". wb11:384-396 leaves that conflict open (F5).
  Change: S11 gives both legs `enforces` in their `[[gate_leg]]` rows and adds a criterion for it. §5 risks names the guard as red under `core.bypass = never` until wb11 F5 is settled. Cause: pre-existing.

- **tr22 S6 (`edge cardinality`).** The spec says (tr22:54-56): "The leg `edge cardinality (…)` in `tools/gate-legs.json`, argv `python {prefix}/playbook/edge_grammar.py --cardinality`, `"pack": "tags"`". Its Files touched (tr22:160) lists no declaration, and AC7 (tr22:213-216) probes argv and `pack` only. The parent says (oc7:61-63) that a leg with no `enforces` is red. wb11:73-75 adds: "the factory refuses a manifest row no declaration produces". The declaration only arrives with tr43 S29, at order 27; this unit builds at order 10.
  Change: S6 declares the leg through `leg_factory.py new` with `--enforces`, in this unit's own pass. AC7 also checks `enforces`. Cause: pre-existing.

- **tr26 S10 (`atlas selftest`).** The spec says (tr26:106-108): "The leg `atlas selftest` … as a `[[gate_leg]]` row in `tools/memory-tree/kit.toml` and a row in `tools/gate-legs.json`". It names no `enforces`. The parent says (oc7:61-63) that a leg with no `enforces` is red, and no new pending row can excuse it (oc7:227-228).
  Change: S10 names the leg's `enforces` in its `[[gate_leg]]` row and checks it in AC14. Cause: pre-existing.

- **tr43 S29 (meta-gate rows).** The spec says (tr43:150-153): "Every leg units 1, 8, 11, 19, 22 and 26 added carries its meta-gate rows: a kit `[[gate_leg]]` or registry `[[exempt_leg]]` row, its … `subject-pins.tsv` row …, its … `ceiling-evidence.txt` line, and a `gate-legs` claim". AC29 (tr43:452-455) is red only "when a leg lacks a meta-gate row". The parent says (oc7:61-63) that a leg with no `enforces` is red. This is the batch that completes every new leg, and it leaves out the field the meta-check reds.
  Change: S29 adds "a non-empty `enforces`" to each leg's rows, and AC29 reds a leg without it. This matches the per-unit fixes above, and dl56 F5's recommendation that each unit's own pass writes its `enforces`. Cause: pre-existing.

- **tr43 S4 (the factory-kinds writer).** The spec says (tr43:49-51): "whose `writer` reads `gov_record.py new <kind>`; the door's writer refusal … admits `build_records.py new <kind>` as its alias". AC4 runs `gov_record.py new deviation` (tr43:360). The parents say (dl16:53-55): "Whether the factory's `new` verb is generic per kind is unknown until PLAY-dOrderedCharter-7 builds, since its S8 states only `new exception`". dl16:248-249 says "no `new disposition` door is claimed", pr7:105-106 says "claims no `new probe` or `new probe-trigger` door", and pr5:58 says "No `new disposition` door is claimed".
  Change: the factory-kinds row's writer names the factory and its per-kind flags, not a `new <kind>` verb. S4 and AC4 add that the build run re-grounds the call on the landed factory. Cause: re-ground. At `fb872a37e`, dl16:46 still claimed "its door, `build_records.py new disposition --build <slug> …`".

3. UNKNOWN UNTIL BUILT

- Whether `build_records.py new <kind>` is generic per kind, so that tr43 S4's alias and AC4's `new deviation` exist. Only PLAY-dOrderedCharter-7's build of the factory decides this (oc7 S8 states only `new exception`).

4. Rule-wide hits the rule does not bind

- **7 (R1):** adds no leg row. Its arms go into existing legs (tr7:245-248), and its `ask` registry row's `check` names the existing `memory hygiene` leg.
- **14 (R1, R2):** adds no leg; unit 15 wires the `map` pack (tr14:236). Its record-kind mention (tr14:54) reads a registry `purpose` and writes no typed record.
- **16 (R1, R2):** adds only an arm to the existing `record-kinds` leg (tr16:191). Its review record (tr16:57-58) is `-purpose-review.md` served as `log`. That is neither a `-<kind>-<n>.md` file nor a typed kind.
- **23 (R1):** changes what the legs' code reads ("leg rows", tr23:69-80), not any row of `tools/gate-legs.json`.
- **36 (R1):** adds no leg. Its census is an arm of `record_causes.py` (tr36:215).
- **47 (R1):** adds a verb and an arm to the `record causes` leg, which unit 19 lands (tr47:22, :124).
- **48 (R1, R2):** changes checker code under the unchanged `runlog record schema` row (tr48:25-26). Its run records are `*-runlog-*.md`, and `runlog` is no member of `TYPED_RECORD_KINDS`, so serving them as `journal` is not touched by oc42 S3.
- **50 (R1, R2):** adds no leg. The record it reads is served `journal` by a pinned dClosedLoop instrument (tr50:23-24), not by any parent's typed kind.
- **53 (R1):** batched arms only (tr53:342-345). Its Files touched holds no leg manifest or declaration.
- **69, 75, 77, 79 (R1):** each reads or re-stamps for the existing `kickoff-manifest ratchet` leg. None edits a leg row; their Files touched are `SESSION-KICKOFF.md` and build records (tr69:82, tr75:97, tr77:140, tr79:152-153).

5. Citation specs: none. Group B is rule-wide and has no citation specs.

## Group C, rule-wide, kinds and kits

Group C (specs 5, 20, 25, 40, 42, 51, 81, 87, 92, 93, 94) has two MISMATCHes: spec 20's govkit step programs reach into the playbook and memory-tree kits in process (R3), and spec 25's `stream-plan` kind is never joined to the typed-record list or the factory (R2). Every probe was a read, run at `c8d46e188`.

Two facts the verdicts rest on:
- `git diff --stat fb872a37e c8d46e188 -- memory/builds/dOrderedCharter/spec/` printed nothing. No dOrderedCharter spec moved during dTotalRecall's spec run, so any MISMATCH caused by an oc spec is pre-existing.
- None of `tools/memory-tree/build_records.py`, `id_grammar.py`, `tools/playbook/policy_value.py` or `core.py` exists yet. `tree_lib.py:406` still reads `RECORD_KIND_TOKENS = ("spec-audit", "diff-review", "journal", "research", "deviation")`, so every parent surface below is spec text only.

1. Table

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 5 | No plan record kind exists, so the owner passes the slug as an argument | R2 | AGREES | tr5:101-103 "no word list and no plan record kind exist, so the slug stays the owner's argument"; pr21:124-125 "`plan.dedupe`, the plan record kind and its writer `plan.record`: dRankedPlan's"; pr21:222-223 |
| 5 | Kits that require memory-tree (roles, unattended, memory-recall) import `id_grammar` in process through their own `resolve_kit_dir` copy | R3 | AGREES | tr5:204; oc18:46-49 is the precedent (memory-recall imports it under the declared `requires = ["memory-tree"]`); `tools/roles/kit.toml:12` and `tools/unattended/kit.toml:12` both declare `requires = [... "memory-tree" ...]` |
| 5 | Kits that do not require memory-tree (runlog, branch-reconcile, run-gates, workflows) reach it with a declared `requires_if` row and an inline legacy fallback; shell reaches it through `--print-slug-*` subprocesses | R3 | AGREES | tr5:76-82 and :206-207; R3's "unless a declared `requires_if` row admits it"; the row shape is `tools/memory-tree/kit.toml:8`, named as the rule's precedent exception at wb28:416-418 and dl12:282-285 |
| 20 | The retag step, a govkit program (`tools/govkit/steps/memory_retag.py`), reads `memory.legacy-anchors` through PLAY-dOrderedCharter-19 S8's `read_policy_value` | R3 | MISMATCH | tr20:33-34, :65-66 against oc19:99-101, oc7:211-212, wb28:63-64 (bullet below) |
| 20 | The journal and front-matter steps (govkit programs) run memory-tree's `read_bindings` and read `FRONT_MATTER_KEYS` from `gen_build_index.py` | R3 | MISMATCH | tr20:38, :57-58 against wb28:63-64 and oc7:202-203 (same bullet) |
| 20 | `journal` is still a valid Serves token, read as `log`; a file named for a typed kind but serving `journal` is reported as one that does not grade | R2 | AGREES | tr20:36-41; oc42:38 keeps `journal` among the free-form tokens; oc42:45-49 makes such a file malformed, which the step's "exits 1 naming any that does not grade" reports |
| 25 | `stream-plan` is a new kind whose files follow the typed name grammar `<date>-build-<unit id>-stream-plan-<n>.md` in `build/`, registered only in `record-kinds.toml` and the HYGIENE view (spec 43 S9 adds it to `RECORD_KIND_TOKENS` alone) | R2 | MISMATCH | tr25:31-36, :108-111; tr43:67-70; oc42:35-43, :45-49 (bullet below) |
| 40 | Routing compares `canonical_kind` against `deviation`, `research` and `log`; `journal` is read as `log` | R2 | AGREES | tr40:35-40, :75-79; oc42:38. The records the parents moved off `journal` (wb gate-health and flake, pr2 card) are read under no kind they no longer serve. They now route under no purpose row, which is spec 4's region and not a parent conflict |
| 42 | A record under a `fields` home whose Serves kind names another row is counted as a `home-kind mismatch` and never red in `record_kinds.py --check` | R2 | AGREES | tr42:98-107; oc42:45-49 puts the malformed red in `read_bindings`. The two verdicts sit in different checks, and tr42:129's file whose name carries `-shape-run-` but ends `-deviation-<n>.md` is legal under oc42 S3 |
| 51 | "Untyped" records take a prefixed header; the typed factory's `- **Key:**` form is unchanged | R2 | AGREES | tr51:33-35, :52; oc7:88-92 (factory `FIELD` regex), oc42:35-38 |
| 87 | memory-tree must not import `runlog_lib.resolve_memory_root`, so it mints its own resolver | R3 | AGREES | tr87:122-124, :153-154; oc7:202-203 "A kit may not import a sibling kit" |
| 92 | The tip scan reads deviation records through `deviation_join.read_record` (`malformed`, `n`, `address`, `before`, `after`, `supersedes`, `caused_by`) and `REQUIRED`, `RISKS`, `FOLLOW` | R2 | UNKNOWN UNTIL BUILT | tr92:198-209, :70-72; oc7:88-95 extracts `read_record`'s refusals and the name grammar into `build_records.py` and keeps only the deviation-only rules in `deviation_join.py` |
| 93 | `has_deviation` keys on `deviation_join._ID` and `deviation_join.read_record` over `*-deviation-*.md` | R2 | UNKNOWN UNTIL BUILT | tr93:93-102, :113; oc7:88-92; today `_ID` is at `deviation_join.py:155` and `read_record` at `:212` |
| 93 | A deviation record's unit is the one its `-deviation-<n>.md` stem names | R2 | AGREES | tr93:98-100; oc42:45-49 joins the deviation kind to that file name both ways; `tree_lib.py:566-576` already does |
| 93, 94 | "This unit's acceptance ledger", and 94's fixture `-94-ledger.md`, are served as `journal` | R2 | AGREES | tr94:117; the tree's 769 ledgers are named `-<n>-acceptance-ledger.md` and serve `journal` (e.g. `2026-09-13-build-TOOL-aBatchedArm-3-1-acceptance-ledger.md`); dl17:35-41's typed `acceptance` kind joins only `-acceptance-<n>.md` |

2. MISMATCHes

- **tr20, R3.** A govkit step program reads policy through the playbook kit's adapter and reaches memory-tree in process.
  - Spec side: tr20:33-34 "The policy read is PLAY-dOrderedCharter-19 S8's `read_policy_value` (shared interface I8)". tr20:65-66 "Each verb reads the target's `memory.legacy-anchors` through `read_policy_value`", said of `tools/govkit/steps/memory_retag.py`. tr20:38 "runs gov's own `read_bindings` over the target's records". tr20:57-58 "against unit 4's `FRONT_MATTER_KEYS`, read from gov's `gen_build_index.py`".
  - Parent side: oc19:99-100 "creates `tools/playbook/policy_value.py` with `read_policy_value(key, root, rev=None)`". oc7:211-212 "as govkit's `read_policy_value` is for `tools/govkit/` modules (TOOL-dSafePassage-9 §4); neither kit can import the other's." wb28:63-64 "A run-gates or govkit module imports no playbook module (TOOL-dGroundRules-1 §4; PLAY-dOrderedCharter-7 §4 "The policy reads")".
  - Spec 43 fixed the same class for `gen_atlas.py` and `gov_map.py` (tr43:75-77, S11-S12) but not here. Its S20 (tr43:111-113) adds another in-process call, to `check_front_matter`.
  - **Change:** spec 20 S5 should name govkit's own `read_policy_value` (TOOL-dSafePassage-9 §4), or a subprocess `policy.py get memory.legacy-anchors --explain`, in place of oc19 S8's module. S1 and S4 should reach memory-tree by subprocess: `gen_build_index.py --print-bindings` exists (`gen_build_index.py:8743`), and a print verb is needed for the front-matter keys or `check_front_matter`. Otherwise the spec must state the in-process load as an exception with its reason; `govkit.py:3137-3155` loading memory-tree's `check-arms.py` in process is the only precedent in the tree.
  - **Cause:** pre-existing. oc7:211-212 read so at `fb872a37e`; wb28:63-64's restatement came in the re-ground, since `git show fb872a37e:...dWitnessedBar-28.md | grep 'imports no playbook'` printed nothing.

- **tr25, R2.** A kind is added on the typed file grammar without joining the typed list or the factory.
  - Spec side: tr25:33-34 "home `memory/builds/*/build/*-stream-plan-*.md`, id-rule `<date>-build-<unit id>-stream-plan-<n>.md`". Its files touched (tr25:108-111) are `record-kinds.toml`, `record_kinds.py` and HYGIENE only; tr43:67-68 "`stream-plan` joins the record-kind vocabulary: `RECORD_KIND_TOKENS`".
  - Parent side: oc42:35-37 "`TYPED_RECORD_KINDS` … the kinds whose records the factory names `<date>-build-<unit id>-<kind>-<n>.md` in a build's `build/` folder". oc42:41-43 "A kind added to the factory without the reader, or to the reader without the factory, fails on load". oc42:46-48 "a file named `-<kind>-<n>.md` in a `build/` folder whose Serves kind is not `<kind>` is malformed".
  - Consequence: `stream-plan` takes the typed name but sits outside `TYPED_RECORD_KINDS` and `build_records.py`'s table. The name join of oc42 S3 never covers it, so a `-stream-plan-<n>.md` file serving `research` reads as bound.
  - Contrast spec 11, which joins `shape-run` to both (tr11:48-50).
  - **Change:** spec 25 (or 43 S9) should join `stream-plan` to `TYPED_RECORD_KINDS` and give it a row in the factory's per-kind table, or else drop the typed `-<n>.md` name. If the fence schema cannot be a factory field row, it should state that and have `check_stream_plan` apply oc42 S3's two-way name join itself.
  - **Cause:** pre-existing (oc42 is unchanged since `fb872a37e`).

3. UNKNOWN UNTIL BUILT

- tr92, tr93: whether `deviation_join.read_record` (with its `malformed`, `n` and `address` keys), `_ID`, `REQUIRED`, `RISKS` and `FOLLOW` stay in `deviation_join.py` or move to `build_records.py`. PLAY-dOrderedCharter-7's build of S7 decides it. tr81:168 (it cites `deviation_join.py:146` `REQUIRED`) rests on the same build.

4. Rule-wide hits the rule does not bind

- tr81 (R3): `read_at` and `pass_of` are probe heredocs run from the repository root. They source `lib-unattended.sh` and import `tree_lib` there; that code belongs to no kit, and tr81:183 says "spec text only".
- tr92 (R3): the tip scan, span script and sweep are root-run probes (tr92:198-229, :342-351). Its one kit edit, S23's docstring in `tree_lib.py`, names `runlog_lib` and imports nothing (tr92:374-376).
- R1 and R4-R8: none of the 11 specs adds or reshapes a `tools/gate-legs.json` row, writes a loop item, a disposition or an overlay read, or touches the guard or budget. A grep for `disposition|gate-legs.json|enforces|Gov-Policy|overlay|layers.toml|contention|budget` hit only tr5's two uses of "disposition", which mean a reader's handling, not R5's door.

5. Citation specs: none in Group C. All 11 specs are rule-wide hits.

The parent specs are under `C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\`: `dOrderedCharter\spec\2026-10-24-spec-PLAY-dOrderedCharter-42.md`, `dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-7.md`, `dOrderedCharter\spec\2026-10-23-spec-PLAY-dOrderedCharter-19.md` and `dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-28.md`. The dTotalRecall specs are `dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-{20,25,43}.md` in the same folder.
