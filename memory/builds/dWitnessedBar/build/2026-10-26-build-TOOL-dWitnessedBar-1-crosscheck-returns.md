**Serves:** research TOOL-dWitnessedBar-1

# dWitnessedBar — the cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record
[`2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck`](2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck.md)
is assembled from, each copied from its agent transcript. Group A read specs 1, 2, 11, 13, 14, 16, 17 and 18; B 19, 22, 24, 25, 28, 46, 51 and 84; C 3, 4, 6, 7, 8, 12, 15, 23, 30 and 56.

## Group A

I reviewed the eight Group A specs (1, 2, 11, 13, 14, 16, 17, 18) against dOrderedCharter at `462d20f35`. The two re-ground commits (`555e623a7`, `1e9b2dad5`) moved none of the parent text these specs rely on. All five mismatches below were already there at `ad002a024`.

1. Assumptions

| Spec | Assumption about the parent | Verdict | Evidence |
|---|---|---|---|
| 1 | The flake and gate-health records are read through oc7 S7's `build_records.py read` verb | AGREES | wb1:59-60, wb1:268 · oc7:88-95, oc7:219 ("`build_records.py` (verbs `new`, `read`)"); S7 is in neither revision's diff |
| 1 | `gate-health` can be added as a kind of S7's factory just by putting required fields into `build_records.py` | MISMATCH | wb1:69-73, wb1:96, wb1:138, wb1:173 · oc7:165, oc42:40-43 |
| 2 | `core.bypass`, whether a bypass may skip the core legs, is oc7 S10's | AGREES | wb2:74 · oc7:109-111 (rev-4 changed only how the key is read) |
| 11 | The `kind.gate-leg` row of `kinds.toml` exists, written pending by oc7 S4, owner dWitnessedBar, and S5 fills in `factory`, `gate` and `population` | AGREES (the tag's spelling: UNKNOWN) | wb11:51-53, wb11:170-181 · oc7:66-71, oc7:134 ("gate leg in dWitnessedBar") |
| 11 | The gate leg's `enforces` must hold every tag in the kind's `binds` (-7 S5) | AGREES | wb11:180-181, wb11:316 · oc7:72-75 |
| 11 | A leg with empty `enforces` is excused only by a `leg` row of `core-pending.txt`, and the meta-check prints each pending count | AGREES | wb11:54-56, wb11:160, wb11:320-322 · oc7:58-65, oc7:192 |
| 11 | Giving every leg a non-empty `enforces` is compatible with oc7's core checks | MISMATCH | wb11:28, wb11:54-56 · oc7:109-111, oc7:257-258 |
| 11 | The enforces rule's practice step reads `practices.toml` rows by `tag` and `line` (oc1) | AGREES | wb11:79, wb11:92, wb11:190-191 · oc1:54-59 (rev-4/5 moved only S4, S8 and F4) |
| 11 | The principle step uses v2 `[enforcement]` clauses, which oc7's registry carries as `clauses` | AGREES | wb11:187-189 · oc7:50-53 |
| 11 | The `pack` key is oc19 S12's | AGREES | wb11:76-77 · oc19:134-138 |
| 11 | The pass runs `owed_rows.py --base HEAD` before its commit | AGREES | wb11:218-220 · oc50:79-84 |
| 11 | `kind.policy-key` is a multi-word kind tag spelled in "PLAY-dOrderedCharter-7's family" (the precedent for F2) | MISMATCH | wb11:347-349 · oc7:133 |
| 13 | `compute_coverage` and `resolve_compare_base` are imported from oc19 S9's `coverage_join` module, canonical in `tools/lib/coverage_join.py` | AGREES | wb13:43-45, wb13:108-110, wb13:344-350 · oc19:113-117 |
| 13 | gate-lint can carry a third inline copy of S9's block under S9's own `coverage_join` parity row | AGREES (nested block: UNKNOWN) | wb13:57-58, wb13:210-211 · oc19:115-117, oc19:245-246, oc19:359 |
| 13 | Moving the functions is S9's job, and S9's move lands before this build run | AGREES | wb13:81, wb13:346-350 · oc19:113-124 (rev-5 changed only the hold on the `map_lib` re-export, which wb13 doesn't use) |
| 14 | `widen` joins oc7 S7's factory as a new kind with fields `Population`, `Keys`, `Reason`, `Caused-by`, by editing only `build_records.py` | MISMATCH | wb14:49-53, wb14:101, wb14:179 · oc7:165, oc42:40-43 |
| 14 | The pass runs `owed_rows.py --base HEAD` before its commit | AGREES | wb14:172-173 · oc50:79-84 |
| 16 | dOrderedCharter's keyed lists are left to unit 18 | AGREES | wb16:104 · oc19:131-133, oc20:90-93, oc26:112-113 |
| 16 | The S6 readers list (built by grepping for the two names) covers every reader of `memory/map/baseline.toml` | MISMATCH | wb16:55-64 · oc50:50 |
| 16 | oc50's probe still reads `spawn-idiom-sites.txt`, `testsuite-count-waivers.txt` and `unarmed-branches.txt` after they move to the ledger grammar | UNKNOWN UNTIL BUILT | wb16:145-153, wb16:168 · oc50:52, oc50:168 |
| 16 | The pass runs `owed_rows.py --base HEAD` before its commit | AGREES | wb16:212-213 · oc50:79-84 |
| 17 | The pass runs `owed_rows.py --base HEAD` before its commit | AGREES | wb17:156-158 · oc50:79-84 |
| 18 | The three lists are each kept "until dWitnessedBar's migration registers it" | AGREES | wb18:21-23 · oc19:131-133, oc26:112-113, oc20:90-91 |
| 18 | The homes are `tools/playbook/positional-refs.txt` and `tools/playbook/instructions-legacy.txt` | AGREES | wb18:34-35, wb18:78-79 · oc19:131, oc20:91 |
| 18 | `positional-refs` is keyed by citing path and ref, with file:line rows given as the reference as written | AGREES | wb18:78, wb18:91-94, wb18:192 · oc19:131-132, oc26:47-51 |
| 18 | The seed reads §n, Mn and `check n` through oc19's `--list-positional` and oc26's file:line rows | AGREES | wb18:42-44 · oc19:132, oc26:57-58, oc26:145-146 |
| 18 | The list's directions: oc26 S3 "`shrink` only ever shortens the list" and oc20 S8 "`instructions.legacy: shrink-only`" | AGREES | wb18:83-84 · oc26:59-62, oc20:93-94 |
| 18 | Re-pointed readers keep their policy keys `tags.positional` and `instructions.legacy` | AGREES | wb18:51, wb18:57-58 · oc26:65-69, oc20:95-98 (rev-4 moved both reads onto `read_policy_value`; the keys are unchanged) |
| 18 | The readers that must be re-pointed are `positional.py`'s check arm and `shrink`, `--check-render`'s legacy half, and `pinned-facts` with `--shrink` | MISMATCH | wb18:48-51, wb18:117-127, wb18:184 · oc26:52-53, oc26:82-84, oc26:92-97, oc26:216, oc20:287-292 |
| 18 | IW-1's legacy list is in oc20 S8 (F3) | AGREES | wb18:201-205 · oc20:90-91 (the list's line moved from `:87` to `:91`; F3 pins its observation at `19d6aae6`) |
| 18 | The pass runs `owed_rows.py --base HEAD` before its commit | AGREES | wb18:112-113 · oc50:79-84 |

2. Mismatches

- **wb1 and wb14, a new record kind joins the factory.** Parent side:
  - oc7:165: "the factory's kind list made the reader's (finding 31)".
  - oc42:40-43: "`build_records.py`, imports `TYPED_RECORD_KINDS` from `tree_lib` as its kind list, and its per-kind table … is refused at import, naming the kind, when its keys differ from that tuple. A kind added to the factory without the reader … fails on load."

  dWitnessedBar side:
  - wb1:69: "a record kind `gate-health` of S7's factory", with files touched (wb1:170-174) that list `build_records.py` and not `tools/memory-tree/tree_lib.py`.
  - wb14:49-50: "The record kind `widen` joins PLAY-dOrderedCharter-7 S7's factory `tools/memory-tree/build_records.py`", with files touched (wb14:177-185) that also omit `tree_lib.py`.
  - wb1:138 binds `**Serves:** gate-health <unit id>`, a token `RECORD_KIND_TOKENS` does not admit.

  Change: wb1 S4 and wb14 S5 each add their kind to `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py` and list that file. Each also states its record's Serves binding under oc42 S3's file-name join (oc42:44-49), which requires a typed kind's Serves kind to equal its file kind. That join conflicts with wb51 S7's `journal` binding, so whoever owns wb51 needs to reconcile it. One revision of each spec, observed with oc42 AC2's probe (`set(build_records.KINDS) == set(tree_lib.TYPED_RECORD_KINDS)`). Cause: pre-existing. oc7:165 already read so at `ad002a024` (rev-2), and oc42 has never been revised.

- **wb11, `enforces` on every leg against `core.bypass = never`.** Parent side:
  - oc7:257-258: "whether a leg is core is the fact `enforces` already states".
  - oc7:110-111: "`never` makes the meta-check red any leg whose `enforces` is non-empty and which carries a `guard`".

  dWitnessedBar side:
  - wb11:28: "every leg names in `enforces` the principles and practices it enforces".
  - wb11:54-56: every leg the rule reaches leaves the pending list.
  - No dWitnessedBar spec mentions `core.bypass` except wb2:74.

  Probe: `python -c "import json;L=json.load(open('tools/gate-legs.json',encoding='utf-8'));print(len(L),sum(1 for l in L if l.get('guard')))"` printed `142 71`. After wb11, an adopter who sets `never` turns up to 71 guarded legs red in the meta-check.

  Change: wb11 §5 risks and §6 state the interaction, and add an AC that runs oc7's `--plant bypass-never` over the generated manifest. Alternatively, it returns an ask to dOrderedCharter to narrow oc7's core-leg predicate. Cause: pre-existing.

- **wb11 F2, the precedent for the tag spelling.** Parent side: oc7:133 names the kind only as words ("command, policy key, preset … in dDeclaredLoop"). Probe: `git grep -n 'kind/.policy-key' -- memory/builds` found it only at `TOOL-dDeclaredLoop-6.md:226` and wb11:348, and found the same at `ad002a024`.

  dWitnessedBar side: wb11:348-349: "The only multi-word kind any spec spells is `kind.policy-key` (PLAY-dOrderedCharter-7's family)".

  Change: re-cite F2's rung-1 precedent to TOOL-dDeclaredLoop-6:226 as the spec that spells it, and keep oc7:133 as the source of the kind's name. Cause: pre-existing.

- **wb16 S6, renaming `baseline.toml`, misses the owed-rows probe.** Parent side: oc50:50, leg-removed population: "no row of `subject-pins.tsv`, `memory/map/baseline.toml` or `tools/run-gates/selftest-budgets.txt` naming it".

  dWitnessedBar side:
  - wb16:55-56: "The two map files take the ledger grammar at `memory/map/baseline.txt`".
  - wb16:58-62: readers "each found by a git grep for the two names". That grep cannot find `owed_rows.py`, which dOrderedCharter's build run creates.

  After wb16, the probe reads a file that is gone. It then either refuses or treats a removed leg's leftover baseline row as owing nothing.

  Change: wb16 S6's readers gain `tools/run-gates/owed_rows.py` (oc50 S2's leg-removed population and its `--selftest` plant). Files touched gains it too. An AC runs `owed_rows.py --selftest` after the rename. Cause: pre-existing; oc50 rev-2 changed only the size row.

- **wb18 S5, re-pointed readers omit three of the parent's list readers and writers.** Parent side:
  - oc26:52-53: "`positional.py seed` writes the file:line rows once … and refuses when the list already holds one".
  - oc26:82-83: "`positional.py pin <file>` rewrites each unlisted file:line citation", which reads the list.
  - oc26:92-97 and oc26:216: the `tags positional selftest` leg runs every `positional-*` plant, `positional-seed` among them.
  - oc20:287-288: `instruction_units.py fixture --plant legacy` plants a file "neither rendered from units nor on `instructions-legacy.txt`". It writes the list in its two-field (bare-path) grammar.

  dWitnessedBar side:
  - wb18:48-51 re-points only "`positional.py`'s check arm and its `shrink` verb, `render_playbook.py --check-render`'s legacy half, and `writing_practice.py`'s `pinned-facts` arm".
  - Files touched (wb18:117-127) omits `gov_tag.py` and `instruction_units.py`.
  - The §7 gates (wb18:184) omit `tags positional selftest`.

  Once `read_rows` refuses a list with no header or the wrong arity, `seed`, `pin` and both fixtures write or read the old grammar, and `tags positional selftest` goes red.

  Change: wb18 S5 adds `positional.py seed` and `pin`, the `positional-*` fixture writer under `gov_tag.py --fixture`, and `instruction_units.py fixture --plant legacy` to its Readers. It lists both modules in files touched and puts `tags positional selftest` on its gate line. Cause: pre-existing; oc26 rev-4 moved only S3 and S9, and oc20 rev-4 only S8's key read.

3. Unknown until built

- **wb11 S5 and AC6:** the tag oc7's build pass writes for foundations C3's "gate leg" (oc7:66-68 says only `kind.<name>`). oc7's pass decides it, and wb11 should read it from `kinds.toml`, not assume `kind.gate-leg`.
- **wb16 against oc50:52:** how `owed_rows.py` parses the three `memory/project/` files in its path-deleted population. oc50 names no grammar (oc50:168, "one parse of each registry"), so its build decides whether ledger-grammar rows still match.
- **wb13 S8:** whether a gate-lint copy of the `coverage_join` block also falls under the `remote_ladder_py` parity row the block carries inline (oc19:245-246). oc19's build decides how the nested block is marked.

4. Revised parent units cited but not depended on

- **wb1:** none. It depends on oc7 S7, which neither revision touched; rev-4 and rev-5 moved S9 to S12.
- **wb2:** none. It depends on oc7 S10 only as a pointer, and the key's meaning is unchanged.
- **wb11:** none at unit level. Its assumptions stay off what the revisions moved: oc1's S4, S8 and F4 (the `charter.practices` read), oc19's S8 and S9, and oc50's size population.
- **wb13:** none. It depends on oc19 S9's module, not on the re-export hold that rev-4 and rev-5 moved.
- **wb14:** none. It depends on oc7 S7 and oc50 S6, and neither moved.
- **wb16:** none. It depends on oc50 S2 and S6, and of those only the size row moved, which wb16 does not touch.
- **wb17:** none. It depends on oc50 S6, which did not move.
- **wb18:** none. It depends on oc19 S11, oc20 S8, oc26 S2, S3 and S5, and oc50 S6. Rev-4 moved only oc20's and oc26's policy-key reads, and wb18 keeps those keys unchanged.

Files:
- `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-{1,2,11,13,14,16,17,18}.md`
- `memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-{1,7,19,20,26}.md`
- `memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-{42,50}.md`
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-6.md`

## Group B

1. Assumptions, one row each

| Spec | Assumption about the parent | Verdict | Evidence |
|---|---|---|---|
| 19 | A key-adding pass runs `owed_rows.py --base HEAD` before its commit and writes every row it names (oc50 S6) | AGREES | wb19:162-163 · oc50:79-84, unchanged. oc50's rev-2 (oc50:224) moved only the size population (oc50:53, 65-67). |
| 22 | `enforces` is oc7 S2's key: a list of `principle.*` or `practice.*` tags | AGREES | wb22:34-36, 108 · oc7:55-57, which rev-4 and rev-5 left alone (oc7:366-367) |
| 22 | The key's creation and its meta-check belong to oc7 S2 and S3 | AGREES | wb22:53 · oc7:58-65, unchanged |
| 22 | oc50 S1 may already have put `enforces` in the canary's key sets | AGREES | wb22:37-38 · oc50:37-41 |
| 22 | Edges resolve through oc19's resolver, and a namespace nobody has registered reads `unarmed` | AGREES | wb22:41-44 · oc19:75-80 (S6) and oc19:51-54 (S2). rev-4 and rev-5 moved only S8 and S9 (oc19:430-441). |
| 24 | oc30 pairs eight rules with legs. Three are pending on dWitnessedBar: line-endings, quoting, language-roles | AGREES | wb24:23-25, 75-77 · oc30:120-129, 148 ("three pending rows"). rev-4 moved only S5 and F4 (oc30:274-278). |
| 24 | The rule tags are `practice.portable.<rule>`, carried in `enforces` (oc30 S3) | AGREES | wb24:34-36 · oc30:41-45, 50-52 |
| 24 | `core.py meta-check` reds a pending row once a leg's `enforces` names its tag, so S14 drains the three rows | AGREES | wb24:78-80, 108 · oc7:61-63 ("a pending row whose item is now enforced is red as stale") · oc30:132-134 |
| 24 | Extra legs carrying `practice.portable.launch` and `interpreter-floor` sit beside oc30's `python resolver` pairing | AGREES | wb24:126-127, 62 · oc30:125, 127. The join counts a rule as enforced when any leg names it (oc30:53-56), so a second leg is admitted. |
| 24 | A pack is a row value, `pack` (oc19 S12) | AGREES | wb24:241, 339-340 · oc19:134-138, unchanged |
| 25 | The `leg-tail` kind joins oc7 S7's record factory `tools/memory-tree/build_records.py` | AGREES | wb25:53, 57, 82, 252 · oc7:88-95, unchanged by rev-4 and rev-5 · oc7:140 (other kinds join S7's factory) |
| 28 | Repository rows are `[[<kind>]]` tables in the overlay, read by `read_overlay_rows` | AGREES | wb28:59-60, 170 · oc35:41-46, unchanged |
| 28 | A patch is an `amends=<tag>@<hash8>` row that changes only the fields it names | AGREES | wb28:170-172 · oc35:53-56, unchanged |
| 28 | The leg schema is found through the `schema` key of the `kind.gate-leg` row, and the `[kind]` table carries `name` and `owner-seat` | AGREES | wb28:37-40 · oc35:98-103 |
| 28 | Schema grammar: `shape`/`widens`, `[[fixed-row]]` with `fixed-by = ["principle=principle.p16"]`, an undeclared field read as fixed | AGREES | wb28:38-42, 48-50 · oc36:39-50, 148-150, 158-159, unchanged |
| 28 | oc36's grammar admits a set direction or an ordered list for a scalar, so `changes` and `rises` must be added | AGREES | wb28:52-56, 326-333 · oc36:61-65, 155-156 |
| 28 | `instructions.exclude` naming a fixed row is refused (plant `exclude-fixed`) | AGREES | wb28 AC3 · oc36:51-54 |
| 28 | `instructions.exclude` is read "through dGroundRules' reader" and passed to the composer | MISMATCH | wb28:59-60 · oc35:64-67 · oc46:42-47, 65-71 |
| 28 | `compose_rows`, `check_rows` and `read_kind_schema` are called from run-gates and govkit code (`compose_target_legs` in `tools/run-gates/leg_factory.py`, under `write_gate_legs`) | MISMATCH | wb28:58-62, 55 · oc7:202-203 · oc33:89-92, 100-102 |
| 28 | A patch that is stale or orphaned is held and gov's row is written in its place; "no refusal withholds another leg" | MISMATCH | wb28:62-65 · oc35:84-85, 87-94, 182 · oc33:362 |
| 28 | The overlay is read "at the landed revision only" through oc35's reader | AGREES | wb28:248 · oc35:196 ("the landed revision, `HEAD` (unit 46 S1)") · oc46:42-47. The spec's wording is ambiguous next to oc46's "not dGroundRules' landed revision", which feeds the first MISMATCH. |
| 28 | A change record's `successor` re-points or orphans a leg patch, which is what S11's witness reads | AGREES | wb28:99 · oc35:80-86, unchanged |
| 28 | `help/overlay-rows.md` is oc35 S12's page | AGREES | wb28:103, 307 · oc35:110-112 |
| 28 | The `owned` arm keeps a repository row from claiming a gov tag; `leg.adopter.<name>` sits at the owner seat | AGREES | wb28:84-85, 248-249 · oc35:47-52, unchanged |
| 28 | A gov leg tag is an admissible `instructions.exclude` member | UNKNOWN UNTIL BUILT | wb28 AC3 · oc36:192-202 |
| 46 | The pass runs `owed_rows.py --base HEAD` before its commit (oc50 S6) | AGREES | wb46:114-115 · oc50:79-84 |
| 51 | The pass runs `owed_rows.py --base HEAD` before its commit (oc50 S6) | AGREES | wb51:301-302 · oc50:79-84 |
| 84 | oc3 is DEFERRED and names `memory/guides/MERGE-BAR.md` under Files touched, so S9's wider guard reaches it and it gets an ask row in dOrderedCharter's BACKLOG | AGREES | wb84:98-103, 210-211, 340-342 · oc3:3 (DEFERRED rev-4) · oc3:203. rev-4 (oc3:297-301) moved only S7 caps; at `ad002a024` the line was oc3:190. `memory/builds/dOrderedCharter/BACKLOG.md` exists. |
| 22 | oc24's `enforces` row admits `unit` or `practice` in `to`, so a `principle.*` target reds until that row is widened | UNKNOWN UNTIL BUILT | wb22:108-112, 206-214 · oc24:129. oc24 itself was not revised; the row is listed because the conflict is with oc7 S2. |
| 25 | A new kind is "a kind row" of `build_records.py`, in a form the factory holds | UNKNOWN UNTIL BUILT | wb25:57-60 · oc7:88-92 |

2. MISMATCH

- **wb28 S5, how `instructions.exclude` is read.** wb28:59-60: "reads the target's `[[gate-leg]]` rows through `read_overlay_rows` and `instructions.exclude` through dGroundRules' reader". oc35:64-67: "The key is read with `policy_reader("instructions.exclude")` … passing `--rev HEAD` as PLAY-dOrderedCharter-46 S6 rules for every read the composition makes … an exit 2 refuses the composition". oc46:46-47: the overlay revision "is the node's own last commit, not dGroundRules' landed revision". oc46:69-71: with an unborn HEAD "no read is made … `instructions.exclude` reads its catalogue default `[]`". As written, the exclusions are read at the landed ref while the overlay is read at HEAD.
  - Change (rev-3 of wb28): S5 reads `instructions.exclude` at `--rev HEAD` of the target. govkit is the caller, so that is govkit's `read_policy_value(key, root, rev)` (TOOL-dSafePassage-9, which oc33:362 confirms takes `rev`). An exit 2 refuses the composition and names the key. An unborn HEAD makes no read and passes `[]`. S5 also gains a plant: a policy committed at HEAD that differs from the landed ref. The §5 security line should say `HEAD`.
  - Cause: the re-ground (oc35 rev-4, oc35:383; oc46 rev-3, oc46:220; at `ad002a024` oc35 S5 read "through dGroundRules' one reader … with the catalogue default `none` until then").

- **wb28 S5 and S4, the composition called across kits.** wb28:60-62: "composes with `compose_rows("gate-leg", …)` and `check_rows` (PLAY-dOrderedCharter-35, -36), through `compose_target_legs` in `tools/run-gates/leg_factory.py`". wb28:55 also edits `read_kind_schema` in `tools/playbook/row_checks.py` as a reader the run-gates code uses. oc7:202-203: "A kit may not import a sibling kit (TOOL-dGroundRules-1, §4 Evidence)". oc33:89-92: the row pass is "`tools/playbook/pins.py`'s `drift` verb, since a kit never imports govkit … `cmd_update` … runs it as a subprocess". oc33:100-102: "The verb then runs the row pass for every row kind PLAY-dOrderedCharter-7's kinds register lists". dWitnessedBar's own wb45 S2 agrees: `leg_factory.py` "imports only the standard library and its sibling `regen`". So a run-gates or govkit module that imports `tools/playbook/overlay_rows.py` breaks the rule the parents now state. And once `kind.gate-leg` carries a `schema`, the drift verb composes gate-leg rows a second time.
  - Change (rev-3 of wb28): S5 reaches the composer only as a playbook-kit subprocess, found by `resolve_kit_dir`, and states which verb: either the drift verb's row pass, whose JSON `write_gate_legs` consumes, or a named `overlay_rows.py` compose verb. S5 also says which of the two compositions governs, so gate-leg rows are composed once. Add a fixture with no playbook kit present.
  - Cause: the re-ground for the import ban (oc7 rev-4, oc33 rev-3; `ad002a024` holds neither sentence, see probe 3). The double composition is pre-existing: at `ad002a024` oc33:78-80 already ran the row pass for every registered kind.

- **wb28 S5, stale and orphaned patches and the `refuse` mode.** wb28:62-65: "A row the checks refuse, or a patch held as orphaned or stale, is named on one line and recorded as a problem, and gov's row as shipped is written in its place; no refusal withholds another leg." oc35:89-91: "Under `order` the patch is applied over gov's new row and an order is filed; under `warn` it is applied over gov's new row … under `refuse` the update is held until `instructions.edit` re-pins the edge". oc35:84-85: an orphaned amendment "is held … each filing an order". oc35:182 shows `compose_rows(kind, gov_rows, overlay_rows, exclude, stale_mode, records)`. wb28 never names `stale_mode`, `records`, `instructions.stale` or an order. oc33:362 adds that `instructions.stale` is read "at the target's `HEAD`".
  - Change (rev-3 of wb28): S5 says the composition takes `stale_mode` from `instructions.stale` at `--rev HEAD`, and takes the change records. Under `order` and `warn` a stale patch is applied over gov's new row, not held. An order is filed through `write_row_order` for each held or orphaned patch. Under `refuse`, either the parent's update hold is kept, or the "no refusal withholds another leg" departure is recorded as a deviation and asked of dOrderedCharter.
  - Cause: pre-existing for the mode semantics and orders (oc35 S8 and S7 are not in the `ad002a024..HEAD` diff). The HEAD revision of the `instructions.stale` read is the re-ground (oc33 rev-4).

3. UNKNOWN UNTIL BUILT

- wb28 AC3 (`exclude-fixed`, a gov leg tag in `instructions.exclude`): oc36's build run decides it with its first probe, `policy.py check --rev HEAD` on a committed `exclude = ["<gov tag>"]` (oc36:192-202). If that exits 2, dGroundRules gets an ask and the plant cannot be built.
- wb22 F1: dOrderedCharter's build run decides whether oc24's `enforces` row lands with `principle` in `to` (wb22's ask). Either way wb22 handles it, by widening the row in `tools/playbook/edges.toml` at its own pass.
- wb25 S6: oc7's build run decides how a kind is declared inside `build_records.py` (oc7:90-92 names the required fields and closed sets per kind but no row format). oc42's "kind list made the reader's" (oc7:165) may move that home again.

4. Revised parent units cited that no assumption depends on

- 19: none (oc50 is relied on through S6).
- 22: none (oc7 S2/S3, oc19 S6 and oc50 S1 are relied on; rev-4 and rev-5 of oc7 and oc19 moved policy reads, S8 and S9 only).
- 24: none (oc7 S3, oc19 S12 and the oc30 pairing are relied on; oc30's rev-4 moved only S5 and F4).
- 25: none (oc7 S7 is relied on; the S9 to S12 policy-read changes do not touch it).
- 28: none (oc35 and oc36 are both relied on; oc17 is cited but was not revised).
- 46: none (oc50 S6).
- 51: none (oc50 S6).
- 84: none (oc3's Files touched line; its rev-4 moved only S7 caps).

Probes, all reads:
1. `git merge-base --is-ancestor` on `c63aabbb4`, `60d60e694` and `ad002a024` against HEAD `462d20f35` printed all three as ancestors.
2. `git diff ad002a024 HEAD -- <oc spec> | grep -E '^[-+][^-+]'` on oc24, oc28 and oc17 printed only one added spec-records table row each, so those units were not revised.
3. `git grep -n 'sibling kit' ad002a024 -- memory/builds/dOrderedCharter/spec/` printed nothing, and on HEAD it hits oc7:202, oc50:67, oc11:93, oc19:102, oc32:374 and oc37:154. `git show ad002a024:<oc33> | grep 'imports govkit'` also printed nothing.
4. The oc35 diff from `ad002a024` to HEAD shows S5's old text "read through dGroundRules' one reader … with the catalogue default `none`" replaced by the `policy_reader` call at `--rev HEAD`.

Files:
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-28.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md
- memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-46.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-33.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md

## Group C

I checked the 10 Group C specs (3, 4, 6, 7, 8, 12, 15, 23, 30, 56) against the dOrderedCharter specs at `462d20f35` and the dDeclaredLoop specs at this branch's re-ground commit `783f1ad3a`. The dOrderedCharter spec folder is the same at HEAD and `462d20f35` (`git diff --stat 462d20f35 HEAD -- memory/builds/dOrderedCharter/spec` printed nothing). Cause was settled with `git show ad002a024:<spec>` and with `git show 783f1ad3a -- <spec>` or `git diff ad002a024 462d20f35 -- <spec>`. Result: 8 MISMATCH (one caused by the re-ground, seven older), 6 UNKNOWN UNTIL BUILT, and the rest AGREES.

#### 1. Assumptions

| Spec | Assumption about the parent | Verdict | Evidence |
|---|---|---|---|
| 3 | An owner exception can excuse a blocking `DEAD PROBE` or `INHERITED` red on any bar leg, through oc7 S9's `core.exceptions` | MISMATCH | wb3:96-97, wb3:173-174; oc7:102-108 |
| 3 | `judge` reads `item.test.attribute`'s outcomes from `tools/loop/loop.toml` | AGREES | wb3:180-181; dl12:34-35 |
| 3 | `judge` calls dl12's `read_items` from inside the run-gates kit | MISMATCH | wb3:180-181; dl12:34-35, dl12:45-50, dl12:216-224 |
| 4 | `TRANSITION_FIELDS` is a tuple in `tools/loop/loop_transition.py` that later units may extend; `tree` can join it | AGREES | wb4:71-74; dl3:126-127 |
| 4 | dl3's writer `record` can carry `tree` and refuse at `item.test.exit` | AGREES | wb4:71-74, wb4:230-233; dl3:60-64, dl3:181-190 |
| 4 | dl12 writes the `item.test.merge`, `item.test.verdict` and `item.test.exit` rows | AGREES | wb4:92-93; dl12:36-38 |
| 6 | `[[drive]]` is the precedent of a descriptor table that govkit does not read | AGREES | wb6:159-161; oc6:41-45, oc6:334-335 |
| 6 | `[[command]]` is a descriptor table read by its own reader | AGREES | wb6:159-161; dl6:59-61; dl18:46-47 |
| 6 | `policy_edit.py set` is the owner's guarded command, with a terminal proof | AGREES | wb6:93-95; dl2:61-67, dl2:206, dl2:228 |
| 6 | `guard.py --staged` can refuse a staged change made "without the command's `Gov-Policy:` trailer" | MISMATCH | wb6:95-97, wb6:281-283; dl2:76-80, dl2:177-178, dl2:188-190 |
| 6 | `set` can write a table-valued key (`verdict.remote.pin`, path to blob) | UNKNOWN UNTIL BUILT | wb6:93-94; dl2:206 ("the leaf") |
| 7 | `core.py new command seen-red --kit memory-tree --run seen_red.py` appends a `[[command]]` row through dl6's factory | AGREES | wb7:66-68; dl6:54-56, dl6:59-61, dl6:195 |
| 7 | dl12's landed `item.test.seen-red` row gets its actor from a transcription that may need re-pointing | UNKNOWN UNTIL BUILT | wb7:68-70; dl12:36-38, dl12:109 |
| 7 | The route for a missing record is dl12's row | AGREES | wb7:85; dl12:36-41 |
| 8 | `flake` can be added as a kind of oc7's factory by editing only `build_records.py` | MISMATCH | wb8:44-49, wb8:98, wb8:192; oc7:88-92, oc7:165; oc42:35-49 |
| 8 | How `verdict_flow.py` writes the flake record through oc7's factory | UNKNOWN UNTIL BUILT | wb8:50-54, wb8:232-234; oc7:96-101; dl16:53-56 |
| 8 | A build-level Test record is named by the build's first unit id (dl16 F4) | AGREES | wb8:134-135; dl16:123-125, dl16:233-236 |
| 12 | Namespace row shape (`ns`, `owner`, `layer`, `source`, `extractor`, `role`, `purpose-source`, `join-armed-by`) | AGREES | wb12:35-36, wb12:110-118; oc19:51-54 |
| 12 | Tag grammar and `seg`, the 64-byte limit, extractors in `tag_index.py` | AGREES | wb12:93-99, wb12:37-40; oc19:47-50, oc19:201; dl18:39 |
| 12 | `pack` key from oc19 S12, and `pack.tags` | AGREES | wb12:59, wb12:124, wb12:140-141; oc19:134-138 |
| 12 | Plants on oc19 S13's `gov_tag.py --fixture --plant` | AGREES | wb12:52-53; oc19:139-140 |
| 12 | `enforces` in both `KNOWN` copies (oc50 S1); `owed_rows.py` reads "each `KNOWN` copy" (oc50 S2) | AGREES | wb12:140-143; oc50:37-45, oc50:51 |
| 12 | dl18's four namespace rows sit beside this unit's three | AGREES | wb12:109; dl18:36-38 |
| 12 | dl18 F2's declared-table precedent for `command` | AGREES | wb12:267-268; dl18:271-276 |
| 12 | A rename or retirement of a leg tag goes "through a change record: PLAY-dOrderedCharter-15's write path" | MISMATCH | wb12:68, wb12:102-103; oc15:55-57, oc15:96-99, oc15:180 |
| 15 | `tools/loop/loop.toml` is dl1's file, and `step.test` exists | AGREES | wb15:216, wb15:127; dl1:57-58, dl1:157 |
| 15 | `item.test.seed` is a `step.test` row of dl12's program | MISMATCH | wb15:53-54, wb15:127; dl12:36-38, dl12:80-81 |
| 15 | `inputs = ["layer.tooling:…"]` passes dl12's program check | MISMATCH | wb15:130, wb15:138-139, wb15:213-214; dl12:43, dl12:150 |
| 15 | `returns` may be prose ("the population files") | MISMATCH | wb15:132; dl12:113, dl12:128 |
| 15 | Route targets for `armed` and `unarmed` | UNKNOWN UNTIL BUILT | wb15:133, wb15:138; dl12:41-42, dl12:147-150 |
| 23 | dl12 seeds an `item.test.attribute` row whose `actor` and `outcomes` can be changed in place | AGREES | wb23:54-56; dl12:36-38, dl12:109-114 |
| 23 | Changing `outcomes` alone leaves the row passing dl12's check | MISMATCH | wb23:54-57, wb23:159, wb23:216-220; dl12:41, dl12:147-148 |
| 23 | Whether dl12's transcribed outcome words are `code-miss` and `spec-wrong` | UNKNOWN UNTIL BUILT | wb23:55-56; dl12:36-38 |
| 23 | The `item.test.reason` row and its reason record belong to dl51 and dl22 | AGREES | wb23:69-70, wb23:100-102; dl22:79-93; dl51:42, dl51:83 |
| 30 | `flow.wait-ceiling` is dl33's key, counted in hours (72 by default) | AGREES | wb30:55-56, wb30:85, wb30:103; dl33:7, dl33:59-63 |
| 30 | dl16's disposition record answers an owner item | AGREES | wb30:73-74; dl16:45-49 |
| 56 | dl2 creates `tools/loop/guard.py` | AGREES | wb56:111-113; dl2:44-49 |
| 56 | When `guard.py` exists, unit 43's AC3 (`--staged`, "no `Gov-Policy:` trailer") exits 1 naming `verdict.peer.signers` | MISMATCH (via wb6) | wb56:292-294; dl2:177-178, dl2:188-196 |

#### 2. MISMATCH details

- **wb3, owner exception (`core.exceptions`).**
  - wb3:96-97: "An owner exception excusing a blocking `DEAD PROBE` or `INHERITED` red: PLAY-dOrderedCharter-7 S9's `core.exceptions`, which the `probe-repair` and `fix-unit` routes name as the alternative."
  - oc7:102-103: "The exception register and `core.exceptions`, read by `core.py exceptions` and by every core gate: a red whose principle and part match an admitted record prints as `excepted`".
  - oc7:104-108 (rev-5): under `owner-only-expiring`, "while no pass has landed that check no record carries the proof, so the value admits none".
  - The register only excuses reds of core gates, matched by principle and part. Nothing in oc7 lets the hook or driver landing decision read it, and the default `any-session-recorded` is not owner-only.
  - **Change:** rev-3. Either narrow the alternative to a red on a leg whose `enforces` names a principle (the record naming that principle and part), with the reader that consults `core.py exceptions` named; or file an ask to dOrderedCharter for the bar's landing readers to read the register. Say that under `owner-only-expiring` no exception is admitted until oc15's check lands.
  - **Cause:** pre-existing. The "every core gate" scope was in S9 at `ad002a024`; rev-5 only narrowed `owner-only-expiring` further.

- **wb3, `read_items` across kits.**
  - wb3:180-181: "`judge` … reads `item.test.attribute`'s outcomes from `tools/loop/loop.toml` through TOOL-dDeclaredLoop-12's `read_items`; a missing loop kit refuses `judge` with exit 2".
  - dl12:49-50 (rev-3): "A kit may not import a sibling kit (TOOL-dGroundRules-1 §4 Evidence), and PLAY-dOrderedCharter-11 S4 runs the same module the same way".
  - `read_items` is a Python function (dl12:34-35). `loop_lib.py` offers only `--check` and `--fixture` (dl12:216-224), so `verdict_flow.py` in run-gates has no subprocess verb to call.
  - **Change:** rev-3. Reach the outcome set through a subprocess, the loop kit found by `resolve_kit_dir("loop", "loop_lib.py", here)`, and file an ask to dDeclaredLoop for a read verb (for example `loop_lib.py items --tag <tag>`). Until it lands, `judge` exits 2 naming the missing verb.
  - **Cause:** re-ground. `git show ad002a024:…-12.md` has no "sibling" or "subprocess" line; `783f1ad3a` added it to S4.

- **wb6, `--staged` and the `Gov-Policy:` trailer.**
  - wb6:95-97: "`tools/loop/guard.py --staged` refuses a staged change to that key without the command's `Gov-Policy:` trailer whatever `policy-file.guard` allows".
  - dl2:177-178: `--staged` is "Run by the pre-commit block only when a guarded path is staged and stderr is not a terminal, so every call is an agent's commit".
  - dl2:76-80: the trailer is checked by the push arm, `--push-range`.
  - At pre-commit no commit message exists, so `--staged` cannot read a trailer. Under the default `owner-only` (dl2:190), any agent write to the policy file is already refused. So AC8's "guard admits an agent's pin" cannot fail just because `OWNER_ONLY_KEYS` is missing.
  - **Change:** rev-4. In S9, `--staged` refuses every agent-staged change to an `OWNER_ONLY_KEYS` key under every value, as dl2's guard-self step does (dl2:182-185), naming the key. The trailer stays with `--push-range`. AC8's fixture sets `policy-file.guard = "agents-with-reason"`, so only `OWNER_ONLY_KEYS` can refuse.
  - **Cause:** pre-existing. `ad002a024` dl2:168 and dl2:71 already read so.

- **wb8, the `flake` factory kind.**
  - wb8:44-46: "a record kind `flake` of the typed build-folder record factory (PLAY-dOrderedCharter-7 S7…)". Its files touched (wb8:192) list `build_records.py` only.
  - oc7:165 hands the factory's kind list to oc42.
  - oc42:40-43: the factory's per-kind table "is refused at import, naming the kind, when its keys differ from that tuple" (`TYPED_RECORD_KINDS`).
  - oc42:45-49: a `-<kind>-<n>.md` file whose Serves kind is not `<kind>` is malformed.
  - The sibling re-ground already applies this (dl16:50-53).
  - **Change:** rev-3. S3 adds `flake` to `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py` and to the closed kind list of `HYGIENE.template.md`, Serves `flake`, and both files are added to Files touched. The hand-off at wb8:98 (id 2, a `journal` binding) cannot hold beside a `flake` factory row.
  - **Cause:** pre-existing. oc7:145 at `ad002a024` already carried the oc42 edge.

- **wb12, renaming a leg tag.**
  - wb12:68: "A rename or retirement of a leg tag through a change record: PLAY-dOrderedCharter-15's write path."
  - oc15:55-57: the write verbs each take "`--manifest <kit id>|overlay`" over instruction manifests.
  - oc15:180: `WRITE_VERBS = ("add", "edit", "remove", "rename", "split")`.
  - The change record's `Unit` field is an instruction unit's tag (oc15:96-99). No oc15 path writes `gate-legs.json`.
  - **Change:** rev-3. Name the path as unowned: either an ask to dOrderedCharter for the `new change` door to accept a `leg.*` tag, or a hand-off to TOOL-dWitnessedBar-11's leg factory, with oc15 S9's extractor named only as the reader of the retired rows.
  - **Cause:** pre-existing. oc15 S7 and S9 are unchanged since `ad002a024`; rev-4 and rev-5 moved S5, S10 and S11.

- **wb15, step membership.**
  - wb15:53-54 and wb15:127: `step = "step.test"`.
  - dl12:80-81: "The entry, adopt, lifecycle and probe items: owned by dPlacedRequest, dLinkedLibrary, dWellOiledMachine and dTotalRecall, never steps of the five."
  - `test.seed` sits in flow-steps' adopt-program table (flow-steps.md:713), not in the `[test]` table that dl12 transcribes.
  - **Change:** rev-6. Declare the row as an adopt-program item outside the five steps, or file an ask to dDeclaredLoop for where adopt items are declared. AC8 reads "no finding" only once that home exists.
  - **Cause:** pre-existing.

- **wb15, layer tag.**
  - wb15:130: `inputs = ["layer.tooling:the [[ledger]] registrations"]`. wb15:138-139: "the layer word in `inputs` is the one that unit's rows use for tooling."
  - dl12:43: "every input names a layer tag of `tools/playbook/layers.toml`". dl12:150 says the same against oc16's register.
  - `layer.tooling` is spelled nowhere in either parent (`grep -rn 'layer/.tooling' memory/builds/` matches only wb15:130), and dl12 has no "tooling" word. As written, AC8 hits the `input-no-layer` refusal.
  - **Change:** rev-6. Name a register row (oc16:40-41 lists the five core layers, the expansions and the optional rows), or derive the tag at the pass from `layers.toml`.
  - **Cause:** pre-existing.

- **wb15, `returns`.**
  - wb15:132: `returns = "the population files"`.
  - dl12:113: `returns = "record-kind.recommendation" # its return template: the record kind it writes`.
  - **Change:** rev-6. Use a `record-kind.*` tag, or state that the item writes no record kind and which value dl12 or dl9 admits for that.
  - **Cause:** pre-existing.

- **wb23, outcomes without routes.**
  - wb23:54-56: the row "carries `actor = "role:gov-tester"` and `outcomes = ["code-miss", "spec-wrong"]`, amended in place where the seeded row spells either otherwise".
  - dl12:147-148: "`routes` holding exactly the outcomes as keys".
  - Changing the outcome words without re-keying `[item.routes]` makes `check_program` refuse the row.
  - **Change:** rev-3. S7 re-keys `[item.routes]` in the same edit (`code-miss` and `spec-wrong`, each to its existing target). AC6 also runs `python loop_lib.py --check` and requires exit 0.
  - **Cause:** pre-existing.

- **wb56, AC16 (inherits the wb6 mismatch).**
  - wb56:292-294: "a present file makes AC3 of unit 43 run and exit 1 naming `verdict.peer.signers`".
  - Unit 43's AC3 is `--staged` "with no `Gov-Policy:` trailer". As above, `--staged` reads no trailer (dl2:177-178). Its plain refusal prints `loop-guard: refused · <path> · <why>` (dl2:194), which names a path, not a key, unless `OWNER_ONLY_KEYS` adds the key.
  - **Change:** rev-4. AC16 checks the key-level refusal that wb6's corrected S9 defines, not a trailer check.
  - **Cause:** pre-existing.

#### 3. UNKNOWN UNTIL BUILT

- **wb6, table-valued `set`:** dDeclaredLoop's build of dl2 decides whether `set` (dl2:206, "the leaf") writes a table-valued key such as `verdict.remote.pin`, and whether `--unit` is required.
- **wb7, `item.test.seen-red` actor:** dl12's transcription decides what actor the seeded row names; wb7 S7 already re-points it either way.
- **wb8, flake-record door:** oc7's build decides whether `build_records.py new` is generic per kind (oc7:96 states only `new exception`). That fixes how `verdict_flow.py` writes the flake record, as a subprocess, since run-gates cannot import memory-tree.
- **wb15, routes:** dl12's build, with dLinkedLibrary's adopt program, decides what item, `transition` or `stand-in:` target `armed` and `unarmed` route to.
- **wb23, outcome words:** dl12's transcription of the `test.attribute` Then column decides whether the row already says `code-miss` and `spec-wrong`.

#### 4. Revised parent units cited that no assumption depends on

- wb3: none. The oc7 assumption rests on S9, which rev-4 and rev-5 moved; the dl12 one rests on S4's new rule.
- wb4: none. It depends on dl3 and dl12, though not on the parts their re-grounds moved (dl3's log kind and leg `enforces`, dl12's S4 scope).
- wb6: none. oc6's rev-4 and rev-5 (S6, S7, S9) and dl6's rev-3 (S1, S9, S11) move nothing it relies on; dl2's rev-3 stderr proof is consistent with it.
- wb7: none. dl6's rev-3 and dl12's rev-3 parts are not relied on.
- wb8: none. oc7's rev-4 and rev-5 moved S9 to S12, not the S7 it relies on; dl16 is relied on through F4.
- wb12: none. oc19's rev-4 and rev-5 (S8, S9), oc50's rev-2 (the size row), oc15's rev-4 and rev-5 (S5, S10, S11) and dl18's rev-2 (S5) move nothing it relies on.
- wb15: none. dl1's rev-4 (S7, AC9, AC10) is not relied on.
- wb23: none. dl22's rev-3 (S1 record kind) is not relied on.
- wb30: none. dl33's rev-4 (S1, S8) and dl16's rev-3 (S4) are not relied on.
- wb56: none. dl2's rev-3 (S5) is not relied on.

Files:
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-{3,4,6,7,8,12,15,23,30,56}.md
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-{6,7,15,19}.md, 2026-10-24-spec-PLAY-dOrderedCharter-{42,50}.md
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-{1,2,3,6,12,16,18,22,33,51}.md
