**Serves:** research KICK-dKeptSession-1

# dKeptSession — the cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record
[`2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck`](2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md)
is assembled from, each copied from its agent transcript. Group A, citation, specs 1 to 16 read specs 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 and 16; Group B, citation, specs 17 to 64 read specs 17, 18, 20, 24, 25, 26, 27, 28, 35, 39, 41, 44 and 64; Group C, rule-wide read specs 2, 3, 22, 36, 45, 56, 57, 62, 63 and 65.

## Group A, citation, specs 1 to 16

I checked the 13 specs of Group A against the parents' specs at `c8d46e188`: 46 assumptions, of which 32 agree, 12 are mismatches and 2 can only be settled by a parent's build. The 12 mismatches fall in nine specs: 1, 5, 7, 8, 9, 10, 11, 12 and 13.

Most of them break R3. Six specs have code in one kit calling another kit's module in process: 1, 7, 8, 9, 10 and 11. Specs 7, 10 and 11 read policy keys through an in-process `resolve()`, where the parents now name `policy.py get` run as a subprocess. In spec 7, parent dl3 S4 (dl3:54-55) uses the same `resolve(...)` wording, so the parent text is ambiguous there too.

The other mismatches are specific:
- **Spec 5:** its transition step writes records before the parent's dirty-index refusal. It also still serves `mailbox-message` as `journal`.
- **Spec 7:** it reads a lease field that `--claims` never prints. It also takes the listing at a different commit from the one the dependent recomputes at.
- **Spec 12:** it reads a tree cell after the parent re-renders it for the current session.
- **Spec 13:** it rests on a "closed set of five" record kinds that the parents have since grown.

1. **Table**

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | `check_expansion_value(key, value)` in `tools/loop/guard.py` reads `[[selects]]` rows of `loop.toml` | cite | AGREES | ks1:73-75, :120; dl2:84-86, :252-260 |
| 1 | dl2 S8 refuses a value only when no core layer row declares its point, so `after-release-verifies` (a core point) is admitted; `needs = "attached"` is an open ask | cite | AGREES | ks1:323-335; dl2:86-91 (rev-3 did not move S8; grep finds no `attached"` in dl2) |
| 1 | `presets.py` (policy kit) passes each pair to the loop kit's `check_expansion_value` | R3 | MISMATCH | ks1:73-74, :81; dl2:272 (guard.py's only flags are `--staged`, `--push-range`, `--fixture`); dl12:47-49; oc7:202-205 |
| 1 | dl6 AC9 greps the `kind.preset` pending row; `core.py kinds` and `meta-check` read `core-pending.txt` | cite | AGREES | ks1:91-95; dl6:62-74, :262-264 |
| 1 | dl6 S2's factory contract: write, run the gate, restore on red | cite | AGREES | ks1:88-89, :120; dl6:89-93, :172-177 |
| 1 | dl6 S4 `new policy-key` writes only the catalogue row and its gate is the wrapped `policy check` | cite | AGREES | ks1:337-339; dl6:102-105 |
| 1 | the `policy check` leg's `enforces` gains the kind's `binds`; the leg carries no `guard` | R1 | AGREES | ks1:90, :221; dl6:113-117; tools/gate-legs.json `policy check` row has no `guard` (oc7:109-111) |
| 5 | `resolve_fleet_tag` (pr1 S11) | cite | AGREES | ks5:43-44; pr1:121-126 |
| 5 | the guard runs between dl3's writer steps 1 and 2; dl3 owns steps 4 to 7 | cite | AGREES | ks5:96, :218-225; dl3:181-190 |
| 5 | the disposal (step 3a) writes `mailbox-message` records "in the same commit", placed before dl3 step 4 | cite | MISMATCH | ks5:107, :224; dl3:185-189 |
| 5 | `read_transitions(build, repo)` (dl3 S7) | cite | AGREES | ks5:105; dl3:69-74 |
| 5 | an extension field registered in `TRANSITION_FIELDS`, with values matching `[A-Za-z0-9._:+@-]+` | cite | AGREES | ks5:106, :185-186; dl3:126-128, :149-150 |
| 5 | the anchor rule is dl3 §8 F2; the record serves `journal` | R2 | MISMATCH | ks5:116-118; dl3:42-49, :150-153 |
| 5 | `loop.toml`, `loop_lib.py`, `LoopError`, `help/loop.md`, leg `loop definition` (dl1) | cite | AGREES | ks5:52-57, :126, :339; dl1:55-66, :86-87, :225 |
| 5 | leg `loop transition record` (dl3 S8) | cite | AGREES | ks5:339; dl3:75-79 |
| 5 | `log` is a channel of `transitions.record` | R8 | AGREES | ks5:107; dl3:54-59, :172-177 |
| 5 | adds no leg | R1 | AGREES | ks5:375-377 |
| 6 | the policy read is I8's shell form, as pr1 S12's `read_lease_policy` reads | cite | AGREES | ks6:38, :190-191; pr1:127-130 |
| 7 | build lease ref `refs/gov/leases/<parent>/build`, mode `live`/`held` | cite | AGREES | ks7:39-41; pr1:62-63, :90-95 |
| 7 | the parent lease's `witness` field, read with no lease parsing, rows from `--claims` only | cite | MISMATCH | ks7:41-44, :58-60; pr1:206-208 (`print_claims` prints fields 1 to 5); tools/unattended/unattended.sh:2204 `cut -f1-5` |
| 7 | the listing posted at Design exit ("the move's witness") equals the one recomputed at the lease's `witness` | cite | MISMATCH | ks7:58-60, :70; dl3:37-40, :183-184; pr1:239-245, :252-253 |
| 7 | `write_transition` (dl3 S5) commits, then the unit posts | cite | AGREES | ks7:65-66; dl3:60-64, :188-190 |
| 7 | `resolve("deps.coordination")` in `position.py` | R3 | MISMATCH | ks7:77-78; dl18:85; dl12:47-49; oc7:202-205 |
| 8 | `new policy-key … --owner` flags (dl6 S4) | cite | AGREES | ks8:33-35; dl6:102-105 |
| 8 | an item's `inputs` are layer tags | cite | AGREES | ks8:107-108; dl12:43-44, :143 |
| 8 | `manifest-check.sh --card --path --build <slug>` is the one path reader | cite | AGREES | ks8:50-52; pr2:121-124 |
| 8 | the build card exists at the path `--card --path --build` prints | cite | UNKNOWN UNTIL BUILT | ks8:50-56, :84-85; pr2:58-61, :168 |
| 8 | `help/orientation-card.md` is pr9's page | cite | AGREES | ks8:79; pr9:206 |
| 8 | `scratch-guard.js` requires the policy kit's `policy-mirror.js` in process | R3 | MISMATCH | ks8:59-63; oc7:202-203; tools/hooks/kit.toml:9 (no `requires_if`) |
| 9 | step tags `step.plan`..`step.deploy` and `read_steps(kit_dir)` (dl1 S2, S3) | cite | AGREES | ks9:46-49; dl1:57-66, :152-157 |
| 9 | `read_transitions` returns no time field (F4 ask) | cite | AGREES | ks9:255-262; dl3:69-74 |
| 9 | runlog's `extract.py` calls `read_transitions`, `read_steps` and the policy kit's `check_cap` in process | R3 | MISMATCH | ks9:46-49, :67-69; pr1:444-452; dl12:47-49 |
| 10 | sibling kit reached by subprocess through `resolve_kit_dir` (dl12 S4) | cite | AGREES | ks10:43-46, :120-121; dl12:47-53 |
| 10 | `help/loop.md` is dl1's page | cite | AGREES | ks10:68; dl1:87 |
| 10 | `resolve("mailbox.reads")` in `position.py` | R3 | MISMATCH | ks10:49-51; dl18:85; oc7:202-205 |
| 11 | `write_transition` prints the `transition —` line where `micro-format` is selected; the progress line follows | cite | AGREES | ks11:49-51; dl3:50-53, :190 |
| 11 | `loop_transition.py --fixture --plant` and `check --selftest` | cite | AGREES | ks11:177-178, :201; dl3:75, :267 |
| 11 | dl6 S4 factory; dl1's `help/loop.md` | cite | AGREES | ks11:34-36, :61; dl6:102-105; dl1:87 |
| 11 | `resolve("notify.owner")` in `loop_transition.py` | R3 | MISMATCH | ks11:45; dl18:85; oc7:202-205 |
| 12 | `resume —`/`partial —` and the import-line override (pr2 S7); `card —`, `route —`, `resume —`, `partial —` order | cite | AGREES | ks12:28-30, :59-61; pr2:91-104 |
| 12 | the build card's `tree —` cell "as S6's lookup re-keys it" names the build's worktree | cite | MISMATCH | ks12:55-58; pr2:47-48, :87-89; manifest-check.sh:534 (`render_tree_cell` inside `render_card`) |
| 12 | `read_card_policy` (S11), `card-store.fixture.sh` (S12), pr9's help page | cite | AGREES | ks12:63-66, :82, :97; pr2:125-133; pr9:206 |
| 13 | `publish_build_card`, `follow_build_card`, `read_card_policy`, S10 checker resolution, S12 fixture | cite | AGREES | ks13:58-61, :76-78, :86-89, :119-120; pr2:66-75, :121-133, :212-213 |
| 13 | dl6 S4 factory, run only where the row is absent | cite | AGREES | ks13:63-67; dl6:102-105 |
| 13 | "the kinds are a closed set of five (`tree_lib.py:406`)", so `records —` stays bounded | R2 | MISMATCH | ks13:52-55, :296-299; oc42:35-39; dl3:42-49; pr2:105-117 |
| 14 | `read_card_policy` (pr2 S11), fixture (S12), pr2 §3's context-size non-goal | cite | AGREES | ks14 S2, S6, §3 last bullet; pr2:125-133, :147-148 |
| 14 | dl6 S4 factory | cite | AGREES | ks14 S2; dl6:102-105 |
| 15 | the route slug and payload capture of pr2 S7 | cite | AGREES | ks15 S1, S3; pr2:91-99 |
| 16 | the tag namespace `policy` and its `purpose-source` are dl18's and oc22's | cite | AGREES | ks16:85-87; dl18:36-38 |

2. **Mismatches**

- **ks1 R3.** ks1:73-74: "each pair passed to dDeclaredLoop's `check_expansion_value(key, value)`", with `presets.py` in the policy kit. dl2:272 has guard.py's CLI as `--staged`, `--push-range`, `--fixture` only. dl12:47-49: "A kit may not import a sibling kit (TOOL-dGroundRules-1 §4 Evidence)".
  Change: run the loop kit by subprocess through an inline `resolve_kit_dir`. Add a §8 fork with an ask to dDeclaredLoop for a guard.py verb that prints `check_expansion_value`'s verdict (target dl2 S8), or declare a `requires_if` row naming `loop` in `tools/policy/kit.toml`.
  Cause: re-ground (dl12:47-49 added at 783f1ad3a; the GR-1 rule and dl2's flag set already read so at e025029b8).
- **ks5 step order.** ks5:224: "3a. the disposal: `disposed=<id>+<id>` and the `mailbox-message` records", placed before "4 to 7". ks5:107: "in the same commit". dl3:185-186: "4. Refuse with exit 2 when the index holds staged changes"; dl3:188: "6. Commit the staged record". If 3a stages its records, step 4 refuses them. If it does not, step 6 commits only the transition record.
  Change: write the `mailbox-message` records at or after dl3 step 5, beside the transition record. Or ask dl3 for a hook that stages extra records after the step-4 check.
  Cause: pre-existing.
- **ks5 R2.** ks5:116: "`**Serves:** journal <anchor id>`", citing dl3's anchor rule. dl3:150-153: "The record serves as `transition`, never `journal`: under PLAY-dOrderedCharter-42 S3 a `-transition-<n>.md` file whose Serves kind is not `transition` is malformed". The fix is already promoted to ks39 (ks39:36-40), but ks5 S12 still contradicts it.
  Change: S12 serves `**Serves:** mailbox-message <anchor id>` and names the `TYPED_RECORD_KINDS` and HYGIENE template joins by reference to ks39.
  Cause: re-ground (dl3 served `journal` at e025029b8).
- **ks7 witness not on `--claims`.** ks7:41-44: "The rows are read by running `bash <kit>/unattended.sh --claims` … never by parsing a lease ref here". ks7:59: "the `witness` field of the parent's build lease row (TOOL-dPlacedRequest-1 S2)". pr1:207-208: "`print_claims` still prints fields 1 to 5 … so the `--claims` row shape … is unchanged". `witness` is field 15 of 18 (pr1:206).
  Change: name a reader that prints the `witness` field, either an ask to dPlacedRequest for a `--claims` field or verb, or a stated read of `CLAIM_ROWS` through the driver.
  Cause: pre-existing.
- **ks7 two witnesses.** ks7:70: the listing is "taken at the move's witness". dl3:40 says that is the `--witness` commit, "HEAD or its ancestor" (dl3:183). pr1:241-245 says the lease's `witness` is "a commit … that records a transition of this build": the transition commit itself, or the commit adding the `-transition-<n>.md` record. The dependent recomputes at the latter (ks7:58-59). The two commits differ whenever `--witness` is an older ancestor.
  Change: take S4's listing at the transition commit `write_transition` just made, the commit pr1 records as `witness`. Also state the `micro-format`-only case, where pr1:249 says no commit witnesses.
  Cause: re-ground (pr1:239-249 rewritten at 2740f0a3d).
- **ks7, ks10, ks11 R3, in-process `resolve()`.** ks7:77 "read through I8's Python form, `resolve("deps.coordination")`"; ks10:50 `resolve("mailbox.reads")`; ks11:45 `resolve("notify.owner")`. All three are in loop-kit modules. dl18:85: "the playbook kit's one subprocess caller of `policy.py get` … without it the join would import the policy kit". oc7:202-205: "finds `policy.py` with it, and runs `<sys.executable> <kit>/policy.py get <key>`".
  Change: each reads `python <prefix>/policy/policy.py get <key>` as a subprocess through the inline `resolve_kit_dir`, as ks6 S2 and ks9 S4 already do.
  Cause: re-ground (dl12:47-49 and dl18 rev-2 at 783f1ad3a). As noted above, dl3:54-55 itself still says `resolve(...)`.
- **ks8 R3.** ks8:59-61: "`readPolicy("actions.free", { repo })` … located by `resolvePolicyHelper()`: the policy kit's `policy-mirror.js`". That is a `require` across kits, its second instance after `agent-cap.js:465-469`. oc7:202-203: "A kit may not import a sibling kit". `tools/hooks/kit.toml:9` holds `requires` only, with no `requires_if` row.
  Change: declare a `requires_if` row naming `policy` in `tools/hooks/kit.toml` for both hooks, or read the value by subprocess.
  Cause: pre-existing.
- **ks9 R3.** ks9:46-49: the stage is "read through TOOL-dDeclaredLoop-3 S7's `read_transitions(build, repo)` and TOOL-dDeclaredLoop-1 S3's `read_steps(kit_dir)`" from `tools/runlog/extract.py`. ks9:69: "judged by its `check_cap`". pr1:444-450: "`read_transitions` is a Python function with no verb … (c) `python -c` importing `loop_transition`, a kit importing a sibling, which TOOL-dDeclaredLoop-12 S4 bars".
  Change: read the transition channel by `git` as pr1 F8 (a) does, or file a fork for a `loop_transition.py read` and `loop_lib.py --steps` verb run by subprocess. Reach `check_cap` through a `budgets.py` verb.
  Cause: re-ground (pr1 F8 added at 2740f0a3d; dl12:47-49 at 783f1ad3a).
- **ks12 worktree cell.** ks12:55-56: "`<tree>` the path of the build card's `tree —` cell (`render_tree_cell`, :742-746) as S6's lookup re-keys it". pr2:87-89: the lookup "re-keys the card into the session's file `<sid>.md` in the session's own tree: the session header, the startup cells re-rendered there". `render_tree_cell` is a startup cell (`manifest-check.sh:534`). After the re-key, the cell names the current session's tree, never the build's worktree.
  Change: read `tree —` from the stored build card before the re-key (the ref's or cache's text). Or ask dPlacedRequest to keep the publisher's tree in a tail field.
  Cause: pre-existing.
- **ks13 R2.** ks13:298-299: "the kinds are a closed set of five (`tree_lib.py:406`), so the line stays bounded and AC6 holds". oc42:37-38: `RECORD_KIND_TOKENS` "becomes `(…) + TYPED_RECORD_KINDS`". The parents now add `transition` (dl3:46-48), `card` (pr2:111-114) and more, and dKeptSession adds `mailbox-message`.
  Change: S3 and F3 read the extended token tuple. Re-derive the `records —` line's bound against `CARD_CAP_BYTES` for the grown set, or select a declared subset of kinds.
  Cause: re-ground (dl3 and pr2 joined their kinds at 783f1ad3a and 2740f0a3d).

3. **Unknown until built**

- **ks8 card store.** pr2's build of S2/S6 decides whether the cache file `--card --path --build` names is written when `card.store` omits `local-clone`. pr2:60 writes no unselected store, but pr2:168's "every lookup that re-derives" is unscoped. If it is not written, ks8 reads `unarmed` and fails open.
- **ks7 lease witness under other renewal values.** pr1's build decides whether the lease's `witness` field is written at all under `leases.renewal` `activity`, `fixed` or `none` (pr1:99-106 sets `renews` per value, not `witness`). That decides whether ks7 S3's listing can ever be derived under those values.

4. **Rule-wide hits not bound**

None: this is a citation group.

5. **Cited revised units no assumption depends on**

- ks1: none (dl2, dl6 both used)
- ks5: none (dl1, dl3, pr1)
- ks6: none (pr1)
- ks7: none (dl3, pr1)
- ks8: none (dl6, dl12, pr2, pr9)
- ks9: none (dl1, dl3)
- ks10: none (dl1, dl12)
- ks11: none (dl1, dl3, dl6)
- ks12: none (pr2, pr9)
- ks13: none (dl6, pr2)
- ks14: none (dl6, pr2)
- ks15: none (pr2)
- ks16: none (dl18)

Spec files: `C:\projects\coding-governance\.claude\worktrees\silly-jang-ffa5af\memory\builds\dKeptSession\spec\2026-10-26-spec-KICK-dKeptSession-{1,5,6,7,8,9,10,11,12,13,14,15,16}.md`

## Group B, citation, specs 17 to 64

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 17 | S1 writes the `attendance` row with `core.py new policy-key attendance --allowed … --owner dKeptSession`, which is dl6 S4's factory | cite | AGREES | ks17:38-39; dl6:55-56, :65-67. The rev-3 re-ground moved S1, S9 and S11, not S4. The row already stands in `tools/policy/catalogue.toml`, which ks41 handles; no parent causes that |
| 17 | The arm runs under `loop_lib.py --check` | cite | AGREES | ks17:48; dl1:62-66 |
| 17 | Each `[[step]]` row has an `exit` item, and `item.plan.exit` is Plan's exit | cite | AGREES | ks17:56, :184-185; dl1:57-59, :154 |
| 17 | `help/loop.md` is dl1's page | cite | AGREES | ks17:70; dl1:85-87 |
| 17 | The `loop definition` leg is dl1's, and this unit adds no leg row | R1 | AGREES | ks17:218-219; dl1:85-87 (`enforces = ["principle.p1"]`) |
| 17 | `[dispositions]` sits in `tools/loop/loop.toml` | cite | AGREES | ks17:249; dl16:32-34 |
| 17 | `attendance` is read through the policy reader, as `autonomy` is; nothing is imported in process | R3 | AGREES | ks17:53-55; dl19:43-45 (dl19 was not revised) |
| 18 | `repeat` is a member of `[dispositions]`, read by `read_dispositions` | cite | AGREES | ks18:25-26, :42-43; dl16:32-34 |
| 18 | The claim writes `mode: recipe` and `playbook: <path>` on a repeat | cite | AGREES | ks18:28-29; pr21:61-68 |
| 18 | pr4's `repeat` row resolves the `playbook:` path | cite | AGREES | ks18:28, :53-55; pr4:164 |
| 18 | `CLAIM_DISPOSITIONS` in `tools/loop/claim.py` is the tuple that pr21 S1's refusal reads | cite | UNKNOWN UNTIL BUILT | ks18:37-40; pr21:38-41, :149, :184-186 |
| 18 | `item.entry.claim` is a stand-in item with no `[[item]]` row | cite | MISMATCH | ks18:200-203; pr3:58-64 |
| 18 | `help/loop.md` is dl1's page | cite | AGREES | ks18:57; dl1:85-87 |
| 18 | `loop_table.py` reads `claim.py` inside the loop kit, not across kits | R3 | AGREES | ks18:116-117; pr21:207 |
| 20 | dl27 leaves the preset slot to this build | cite | AGREES | ks20:25-26; dl27:106-107 |
| 20 | The slot fields go in `tools/loop/scenario-schema.toml` and are inherited through `extends` | cite | AGREES | ks20:33-36; dl27:40-41, :140, :186 |
| 20 | Two disagreeing slots settle by dl27 S7's `flow.scenario-conflict` rule | cite | AGREES | ks20:57-59; dl27:76-79 |
| 20 | `derive_step_scenarios(build)` reads the transition record's `scenario=` field | cite | AGREES | ks20:49-53, :91; dl27:80-85, :201-204, :215 |
| 20 | An overlay scenario row is written only through the guarded edit path | cite | AGREES | ks20:148-149; dl27:41-45 |
| 20 | `read_scenario_value` in `tools/policy/policy.py` calls the loop kit's `derive_step_scenarios` in process | R3 | MISMATCH | ks20:49-53, :89-95, :119; dl27:158; dl26:70-71; dl12:49 |
| 20 | `check_scenario_policy` in `tools/loop/scenario.py` calls the policy kit's `check_value`, its `never` list and its pair rules in process | R3 | MISMATCH | ks20:38-42, :118; dl26:70-71; dl27:158 |
| 20 | A build's slot is read from its scenario rows; the spec names no composition read for them | R6 | UNKNOWN UNTIL BUILT | ks20:52-53; dl27:71-74; dl26:39, :280-290 |
| 20 | The new plants ride dl27's `loop scenario fixtures` leg | R1 | AGREES | ks20:202; dl27:94-97 |
| 24 | The `flow.wait-ceiling` catalogue default is 72 hours | cite | AGREES | ks24:33-34; dl33:62-63. Probe: `catalogue.toml` prints `flow.wait-ceiling 72 {'type': 'hours', 'min': 0}` |
| 24 | A wait declares `deadline` and `on-deadline` | cite | AGREES | ks24:92-93; dl33:57-59 |
| 24 | `policy.flow.wait-ceiling` is dl33 S5's grammar for a row's deadline | cite | AGREES | ks24:220-221; dl33:58-59 |
| 24 | `python loop_transition.py record` is the transition writer | cite | AGREES | ks24:187; dl3:60-61 |
| 25 | Today the lease renews on a transition alone (pr1 S8) | cite | AGREES | ks25:30; pr1:99-106 |
| 25 | pr1 S8 renews only on a commit carrying a `Gov-Transition` trailer | cite | MISMATCH | ks25:98-100; pr1:100-102, :241-248 |
| 25 | Before the ask lands, a beat that passes a question commit as `--witness` just reads S8's verdict | cite | MISMATCH | ks25:52-57, :153-154; pr1:249-250, :86-88 |
| 25 | `--beat` renews the build lease under pr1 S4 and S5 | cite | AGREES | ks25:53-54; pr1:76-77, :83-84, :250-254 |
| 25 | `step = "none"`, as pr3 F2 gives the entry items, which are never steps of the five | R4 | AGREES | ks25:36, :111, :236-240; pr3:333-339; dl12:80-81 |
| 25 | Each input names a layer tag | R4 | AGREES | ks25:114; dl12:43; oc16:35-41; dl1:54 |
| 25 | `returns = "an answer message"` | R4 | MISMATCH | ks25:116; dl12:113; dl24:144-145 |
| 25 | `routes` holds exactly the three outcomes, each `stand-in:<path>` | R4 | AGREES | ks25:117, :122-125; dl12:147-149 |
| 25 | `deadline = "policy.flow.wait-ceiling"` satisfies the `wait` rule | cite | AGREES | ks25:38-39, :118; dl33:57-63 |
| 25 | `on-deadline = "defaulted"`, an outcome | cite | MISMATCH | ks25:39, :119, :252-253; dl33:58-59 |
| 25 | `termination.py check` runs over a loop definition holding the row, or with its `deadline` cut | cite | UNKNOWN UNTIL BUILT | ks25:192-195; dl33:38-44; dl26:280-290 |
| 25 | The `awaiting` route draws nothing and is not a self-route, so `counted` does not read it | R8 | AGREES | ks25:122-125; dl33:50-56; pr3:204-209 |
| 25 | The five-step definition is dl1's | cite | AGREES | ks25:238-239; dl1:57-61 |
| 26 | `read_card_policy` reaches the policy kit as an optional sibling, a bounded call | cite | AGREES | ks26:33-34; pr2:125-126 |
| 27 | `take-over` is pr1 S5's verb | cite | AGREES | ks27:62-63; pr1:83-84, :93-95 |
| 27 | `read_claims` is the lease record's one parser and reads its tip | cite | AGREES | ks27:118-119; pr1:71-73 |
| 28 | `resolve_fleet_tag` matches this node, `read_fleet` is the one fleet reader, and pr1 adds `--fleet-tag` | cite | AGREES | ks28:62-63, :79-80, :115-116, :186-187; pr1:121-124 |
| 35 | `read_transitions(build, repo)` returns the build's recorded transitions | cite | AGREES | ks35:36-38, :71-72; dl3:69-71 |
| 39 | dl16 and dl17 add `disposition` and `acceptance` to the tuple, and dl17 reds a record served as `journal` | cite | AGREES | ks39:71-72; dl16:45-53; dl17:35-44, :278 |
| 39 | `mailbox-message` joins `TYPED_RECORD_KINDS`, is served as its own kind, and joins HYGIENE's closed list | R2 | AGREES | ks39:33-43; oc42:35-49, :57-59, :156 |
| 41 | dl6 S4's factory appends a `[[key]]` row; refusing a name that already stands is an ask | cite | AGREES | ks41:25-28, :57-58, :68; dl6:65-68, :177-179 |
| 44 | dl2 S8 admits `after-release-verifies`, since no `[[selects]]` row names it | cite | AGREES | ks44:41-43; dl2:84-91 |
| 44 | `tools/unattended/mail-notice.js` binds its build through `readCard` and `extractRouteUnits`, exported by `tools/hooks/scratch-guard.js` | R3 | MISMATCH | ks44:69-70; dl12:49 |
| 44 | `position.py` imports `resolve_bash` from `loop_lib.py`, inside the loop kit | R3 | AGREES | ks44:88-89 |
| 44 | ks20's pair rule is reached through `python <prefix>/policy/presets.py pairs` as a subprocess | R3 | AGREES | ks44:157-160 |
| 64 | pr2's card-ref writes go through `write_gov_ref` | cite | AGREES | ks64:123-125; pr2:53-57 |

2. MISMATCHES

- **ks18 §10, `item.entry.claim` has no row.** ks18:201-203: "`item.entry.claim` is a stand-in item with no `[[item]]` row, so its dispositions had no join". pr3:58-64: "**S3** — `item.entry.claim`: one row, actor `command:entry.claim` … **S4** — The stand-in row for `item.entry.claim` pruned from `tools/loop/loop.toml`'s `[[stand-in]]` list".
  - Change: restate §10. Once dPlacedRequest lands, the item is declared with outcomes `claimed`, `slug-taken`, `awaiting` and `refused`. dl13 S7's route join then covers `claimed → transition`, but not the `disposition` that rows B1 to B3 carry, so the S2 join is still owed.
  - Cause: pre-existing. The base text already held S4 at :55.
- **ks20 S4, a policy-kit step calls a loop-kit function in process.** ks20:49-53: "`read_scenario_value(...)` … reads the build's placed scenarios from TOOL-dDeclaredLoop-27 S8's `derive_step_scenarios(build)`", and its home is `tools/policy/policy.py` (ks20:119). dl27:158: "since the index runs it and a kit imports no sibling kit". dl26:70-71: "running `policy.py get <key> --rev <pin>` … as a subprocess, since a kit imports no sibling kit".
  - Change: read the build's placed scenarios and their slots through a `tools/loop/scenario.py` verb, run as a subprocess through an inline `resolve_kit_dir`. dl27 offers only `members`, `new` and `select` (dl27:212, :272), so add a §8 fork carrying an ask to dDeclaredLoop for a slots-per-build verb. The other route is a declared `requires_if` row on `tools/policy/kit.toml` naming `loop`.
  - Cause: re-ground. The parents' statements (dl12:49, dl26:70-71, dl27:158) entered at `783f1ad3a`; dl27 at `e025029b8` had none. The rule itself is TOOL-dGroundRules-1 §4.
- **ks20 S2, a loop-kit check calls policy-kit functions in process.** ks20:38-41: "`check_scenario_policy(row, table)` in `tools/loop/scenario.py` … each override key is a catalogue key on no `never` row and its value passes `check_value`; and the pair rules hold". The rule is the same as above: dl26:70-71, dl27:158.
  - Change: ks44 S41 (ks44:157-160) already moves the pair rule onto `presets.py pairs` by subprocess. S2 still needs `never` membership and `check_value` through a `policy.py` or `presets.py` verb by subprocess, or a `requires_if` row on `tools/loop/kit.toml` naming `policy`.
  - Cause: re-ground, as above.
- **ks25 §4 Evidence, the trailer-only witness.** ks25:98-100: "TOOL-dPlacedRequest-1 S8 renews only on a commit carrying a `Gov-Transition` trailer naming the build". pr1:100-102: "a commit that resolves, records a transition of this build on the channel `transitions.record` makes the source (TOOL-dDeclaredLoop-3 S4, S7 …)".
  - Change: reword the evidence to the channel source, either the trailer or the `-transition-<n>.md` log record. Reword the §8 F4 ask to "even when it records no transition of the build on the source channel".
  - Cause: re-ground. pr1 rev-5 changed it; the base at :94 read "carries a `Gov-Transition` trailer".
- **ks25 S4 and Rollout, the wait witness before the ask lands.** ks25:153-154: "before it, the beat passes the witness and the lease reads S8's verdict, so nothing renews early". pr1:249-250: "A sha that does not resolve or records no transition of the build exits 2". pr1:86-88: "`lease not written — <why>` with exit 2".
  - Consequence: until dPlacedRequest accepts F4, every beat during a wait is refused and writes no lease commit. `beat-utc` stops moving (pr1:250-252), so the lease goes stale sooner than it would without this unit.
  - Change: S4 passes the question commit only once the landed lease verb admits it, through a version gate or a capability probe. Otherwise it passes the transition witness pr1:252-254 names. Restate the Rollout and AC5 to match.
  - Cause: pre-existing. The base at :234-235 read "a sha that does not resolve or carries none exits 2".
- **ks25 §4 The row, `returns`.** ks25:116: `returns = "an answer message"`. dl12:113: `returns = "record-kind.recommendation" # its return template: the record kind it writes`. dl24:144-145: "`returns` is written `record-kind.<name>@<n>`; an input naming no record kind is prose and joins nothing".
  - Change: name the record-kind tag the answer writes, in the `record-kind.<name>@<n>` form. If an answer is a mail commit with no record kind, add a §8 fork with an ask to dDeclaredLoop to admit a prose `returns`. pr3:160-165 rests on the same reading, so the build run re-grounds both.
  - Cause: pre-existing. dl12:98 at `e025029b8` already read so.
- **ks25 S1 and the row, `on-deadline`.** ks25:119: `on-deadline = "defaulted"`. ks25:252-253: "the build pass re-grounds `on-deadline`'s value, an outcome here". dl33:58-59: "`on-deadline`, the route it takes past it".
  - Change: set `on-deadline` to a route target, the `defaulted` route's `stand-in:tools/unattended/unattended.sh`, and drop F3's deferral.
  - Cause: pre-existing. dl33:55 at the base read the same; rev-4 moved S1 and S8 only.
- **ks44 S9, a sibling kit's module required in process.** ks44:69-70: "`mail-notice.js` binds its build through `readCard` and `extractRouteUnits`, exported by `tools/hooks/scratch-guard.js:1615`". dl12:49: "A kit may not import a sibling kit (TOOL-dGroundRules-1 §4 Evidence)".
  - Probe: `tools/hooks/kit.toml:3` is `id = "agent-cap"`. `tools/unattended/kit.toml:12` is `requires = ["memory-tree", "review-harness", "settings-merge", "kickoff-manifest"]` and has no `requires_if`. A grep for `require(` of `scratch-guard` finds only hooks-kit files (`agent-cap.js`, `format-guard.js`).
  - Change: reach the card through `manifest-check.sh --card --path --session <sid>`, pr2 S10's one path reader and the call `readCard` itself makes, by spawn. The other route is a declared `requires_if` row on `tools/unattended/kit.toml` naming `agent-cap`, shaped like `tools/memory-tree/kit.toml:8`.
  - Cause: pre-existing. The rule stood at the base (dl12 F4 at `e025029b8`, :255).

3. UNKNOWN UNTIL BUILT

- **ks18 S1:** pr21 splits the act between the bash verb `run_entry_claim` and `claim.py` (pr21:184-186) and never says which half holds the "new|patch|repeat" refusal (pr21:149). dPlacedRequest's build decides whether a Python tuple can be "the tuple the refusal reads", and so whether AC4's single-spelling grep can pass.
- **ks20 R6:** dl26 §8 F5 is open on how a sibling reaches a build's composition at its pin (dl26:280-290). That pick, made at dDeclaredLoop's build, decides the read path S4 must use for an overlay scenario's slot.
- **ks25 AC1:** `termination.py check` composes through `compose_at` at `HEAD` (dl33:38-44), and the compose verb waits on dl26 F5. dDeclaredLoop's build decides whether a planted definition can be checked. In any case the plant must be committed at the scratch repository's `HEAD`.

4. Rule-wide hits the rule does not bind

- None. Group B is a citation group, and its specs carry no rule-wide hits.

5. Revised parent units cited that no assumption depends on

- 17 (dl1, dl6): none
- 18 (dl1, dl16, pr4, pr21): none
- 20 (dl27): none
- 24 (dl33): none
- 25 (dl1, dl12, dl33, pr1, pr3): none
- 26 (pr2): none
- 27 (pr1): none
- 28 (pr1): none
- 35 (dl3): none
- 39 (dl16): none
- 41 (dl6): none
- 44 (dl2): none
- 64 (pr2): none

## Group C, rule-wide

**Group C (rule-wide, led by spec 2)**

Two MISMATCHes, both on R3 (specs 36 and 56). Every other hit either agrees with today's parent text or is a hit the rule does not bind.

## 1. Assumptions

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 2 | The preset step calls `derive_preset_assignment` and `load_presets(KIT)` in process. They live in `tools/policy/presets.py`, the same kit as `policy.py`, so no sibling kit is imported. | R3 | AGREES | ks2:33-39, ks2:93; ks1:56-57 and ks1:197 put both functions in `tools/policy/presets.py`; oc7:202-203 bans only a *sibling* kit import |
| 3 | The `preset_section` probe in `render_playbook.py` runs the policy kit's verb as a subprocess found through `resolve_kit_dir('policy', 'policy.py', …)` and substitutes its stdout. | R3 | AGREES | ks3:42-46; oc7:202-206 (inline `resolve_kit_dir`, run `policy.py` as a subprocess); dl12:45-48 does the same; `tools/playbook/render_playbook.py:470-500` at HEAD (`derive_role_roster`) |
| 3 | The map's preset line (`instruction_units.py`, playbook kit) reads the `--line` output "through the same probe route", which is a subprocess and not an import. | R3 | AGREES | ks3:54-56; oc7:202-206 |
| 36 | Rejects importing govkit's resolver and carries `resolve_bash` inline in the loop kit. | R3 | AGREES | ks36:36-37, ks36:102-103; oc7:202-203 |
| 36 | The guard reaches the unattended kit's driver as `[resolve_bash(), <driver>, …]`. `<driver>` is "an absolute path", and "absent driver" is decided by `os.path.isfile(<driver>)`, not by the inline `resolve_kit_dir`. | R3 | MISMATCH | ks36:42-47 vs dl12:45-47, dl12:53-55 and dl52:43-44 |
| 56 | S3's one launcher `run_driver(argv)` runs `[resolve_bash(), <driver>, *argv]` and says nothing about how `<driver>` is found. | R3 | MISMATCH | ks56:51-54 vs dl12:45-47, dl12:53-55 and dl52:43-44 |
| 56 | S23: `mail-notice.js` carries `readCard`/`extractRouteUnits` inline and requires no file of the hooks kit. | R3 | AGREES | ks56:105-107; oc7:202-203 |
| 56 | S2: an inline copy of `extract_files_touched` under the parity marker, not an import. | R3 | AGREES | ks56:47-49; dl12:53-55 (inline block under `PARITY_ROWS`) |
| 56 | S40/AC30: `import tree_lib, build_records` is in process within `tools/memory-tree/`, not a sibling import. | R3 | AGREES | ks56:148-150, ks56:340-342; oc42:85-86 ("`build_records.py`, in the same kit as `tree_lib.py`") |
| 56 | S13/AC30: `mailbox-message` is a member of `TYPED_RECORD_KINDS` with a factory row. Unit 39 joins all three lists (tuple, factory, HYGIENE). 56 only observes two of them and adds no kind. | R2 | AGREES | ks56:78-79, ks56:340-342; oc42:35-43, oc42:57-59; ks39:34 and ks39:42 (the HYGIENE template half) |
| 56 | S40: cites oc42 S2's import refusal, `import build_records` exiting 0, as the tuple-and-table equality. | R2 | AGREES | ks56:148-150; oc42:40-43 ("refused at import, naming the kind, when its keys differ from that tuple") |
| 57 | S1/AC1: the tuple member in `tree_lib.py` and the factory row in `build_records.py`, observed together at this pass by `import build_records` exiting 0. The HYGIENE join is unit 39's. | R2 | AGREES | ks57:38-44, ks57:134-138; oc42:40-43; ks39:42 |
| 57 | AC1's `import build_records` is in-kit. | R3 | AGREES | ks57:136; oc42:85-86 |

## 2. MISMATCHes

- **ks36 S2/S3, the driver's locator.** ks36:42-43: "S9's step runs `[resolve_bash(), <driver>, "--mail", "read", <slug>, "--open"]`, `<driver>` an absolute path"; ks36:44-45: "The guard passes as 'an absent driver' only when `os.path.isfile(<driver>)` is false". The parent says otherwise. dl12:45-47: the loop kit "finds … `load_sets.py` through `resolve_kit_dir("playbook", "load_sets.py", here)` and runs [it] … as a subprocess". dl12:53-55: "The `resolve_kit_dir` block is carried inline … one block in `loop_lib.py`". dl52:43-44 reads the driver itself "through `resolve_kit_dir("unattended", "unattended.sh", here)` and printed `unarmed` where the driver does not resolve". At HEAD, `tools/lib/resolve_kit_dir.py:23,49` refuses with `LookupError` and never guesses a prefix.
  Change: S2 should name `<driver>` as `resolve_kit_dir("unattended", "unattended.sh", here) / "unattended.sh"`, taken from `loop_lib.py`'s inline block. S3's "absent driver" pass should be that `LookupError` (the NOTE naming the kit), with the `isfile` test applied only to the resolved path. AC4's "driver file removed" plant then removes the kit from all three places `resolve_kit_dir` searches.
  Cause: pre-existing. dl52:43 and oc7:202-203 already read so at `e025029b8`. dl12 S4's inline-`resolve_kit_dir` sentence was added by the re-ground `783f1ad3a`: grep for `resolve_kit_dir` in dl12 at `e025029b8` prints nothing.

- **ks56 S3, `run_driver`.** ks56:51-52: "One launcher, `run_driver(argv)` in `tools/loop/loop_lib.py`, runs `[resolve_bash(), <driver>, *argv]`". It names no locator for `<driver>`, while the four call sites it gathers (units 7/35, 42, 44) inherit spec 36's absolute path. The parent is the same text: dl12:45-47 and dl12:53-55, and dl52:43-44 "through `resolve_kit_dir("unattended", "unattended.sh", here)`".
  Change: S3 should state that `run_driver` finds `<driver>` once through `loop_lib.py`'s inline `resolve_kit_dir` and turns its `LookupError` into the callers' unarmed outcome. AC3's stub should also record `argv[1]` as the resolved path.
  Cause: pre-existing (dl52:43 and oc7:202-203 at `e025029b8`), restated by dl12's re-ground `783f1ad3a`.

## 3. UNKNOWN UNTIL BUILT

None.

## 4. Rule-wide hits the rule does not bind

- **ks2, "a composition read".** R6 binds the overlay composition's `policy.py get` reads: an adopter `when`, `instructions.exclude`, and the tag-valued keys (oc46:65-71). Spec 2 is the policy reader's own step and reads the table its caller's `read_revision` read (ks2:33-40, ks2:98-100). Its AC1 already passes `--rev HEAD` (ks2:157-160).
- **ks2, "an in-process sibling import".** The import is within `tools/policy/`, so it is the AGREES row above, not a cross-kit import.
- **ks3, "a composition read".** The `preset_section` probe resolves a derived placeholder (ks3:42-49). It is none of oc46 S6's three composition reads, so R6 does not bind it.
  - Owner's call: S2 passes no `--rev`, so the probe reads the reader's default revision. oc46:43-46 calls that "the remote ladder's ref", while the overlay in the same render is read at `HEAD`. AC4's local-commit red (ks3:168-171) depends on that choice.
- **ks22, "a loop item row".** `item.design.exit@1#0a1b2c3d` is only a field value in AC2's message-id probe (ks22:145). The spec adds no `tools/loop/loop.toml` row, and R4 (dl12 S1-S3) binds rows of the loop program.
- **ks45, "a loop item row".** The hits are audit report items ("report item H1", ks45:21-23). The unit touches only `tools/runlog/` (ks45:90-91) and adds no loop row.
- **ks36, "an in-process import".** The hit is the rejected alternative "Importing govkit's resolver" (ks36:102-103). R3 is applied in the rows above.
- **ks56, "a leg".** S25-S27 and S44 owe existing parent legs (`policy fixtures`, `loop selftest`, `loop definition fixtures`). Files touched (ks56:232-243) has no `tools/gate-legs.json`, so no row is added or reshaped and R1 does not bind.
- **ks57, "a leg".** §7 names the existing `build-index selftest` (ks57:152). Files touched (ks57:107-108) is `.governance/policy.json` and ledgers only. No leg row.
- **ks62, "a leg with no `enforces`".** S1 names the legs that run sibling arms in ledger lines (ks62:41-45). The spec never mentions `tools/gate-legs.json` (0 hits). No leg row.
- **ks63, "a leg with no `enforces`".** Its `tools/gate-legs.json` mentions (ks63:94, :118, :323, :343) only read the manifest, and S13 edits spec leg lines, not manifest rows. No leg row.
- **ks65, "a leg with no `enforces`".** Its AC5/AC6 legs sit in a scratch fixture manifest for `check-spec-tokens`' guards join (ks65:311-324), never the repository's `tools/gate-legs.json`, which is what oc7 S3's meta-check grades (oc7:58-63). §3 declines a new leg (ks65:160-161).

## 5. Revised parent units cited but not relied on

Not applicable: Group C is rule-wide and holds no citation spec.
