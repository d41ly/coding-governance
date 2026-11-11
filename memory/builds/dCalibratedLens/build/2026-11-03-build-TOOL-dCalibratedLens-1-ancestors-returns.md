**Serves:** research TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-1

# dCalibratedLens — the ancestors cross-check readers' returns, verbatim

The five `gov-spec-reviewer` returns the ancestors cross-check record [`2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck`](2026-11-03-build-TOOL-dCalibratedLens-1-ancestors-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck.md); each group's handoff sits beside it.

## Group A, led by spec 14 (specs 14, 13, 9, 10, 11 and 15)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-14-1-spec-reviewer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-14-1-spec-reviewer.md).

Group A has 31 assumptions over specs 14, 13, 9, 10, 11 and 15: 21 AGREES, 9 MISMATCH and 1 UNKNOWN UNTIL BUILT. All 9 MISMATCH rows are `pre-existing`. `git diff --name-only 22a8efac3 0d1c1dda4` over both builds' `spec/` names only tr1 and tr2, and no group A spec cites either.

Scope notes:
- cl13:354 cites dl25 in a continuation list ("TOOL-dDeclaredLoop-24 S7, -25"). The brief's cited list leaves dl25 out, so I read it and gave it a row.
- The brief names no name-only hits in group A. A scan for ancestor surface names in specs 9 to 15 found one more, cl9:158, which has a row.
- None of the four ask-check specs (cl1, cl3, cl6, cl7) is in group A. The ask rows below come from two other specs: cl13 relies on dl26 §8 F5's `compose` verb, and cl9 relies on wm32's `find --all` ask to dTotalRecall. Neither ask is in any BACKLOG.

**1. Table**

| Spec | Assumption about the ancestor | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 14 | `--trigger <slug> --subject <s> --cause <c>` is dl20 S2's verb in `unattended.sh`. It reads policy through `policy.py get` and passes `--opt-in` to `review_pin.py`. cl14 S2 widens it, and AC4's fixture is the one dl20 lands in `unattended.test.sh`. | cite | AGREES | cl14:43-45, :124, :306-312, :362; dl20:51-57, :139-144, :332 |
| 14 | AC4: with `review.opt-in` filling the slot, the `--trigger` JSON line carries the swap. | cite | UNKNOWN UNTIL BUILT | cl14:306-310; dl20:54-55, :142-143 pass `get`'s output as `--opt-in`; `policy.py:1347-1348` prints a list one member per line; catalogue.toml:417-422 makes the key a `set`; fh3:67-69 reads a JSON map |
| 14 | dl28's rows: `rescope · flow <act> <row tag> · change <stem>` and `flow-state <row tag> · applied`. A held or refused change is not carried. `After` is `<tag>@<hash8>` over the canonical form, so one row gives one `After`. | cite | AGREES | cl14:51-57, :143-145; dl28:37-43, :44-50, :58-67, :116-119 |
| 14 | A carrier's `scenario=` field gives "the scenario its build ran", one tag, and that tag fills the proposed row's `extends`. | cite | MISMATCH | cl14:55-56, :177; dl27:80-83, :50-51 |
| 14 | The activatable kinds are `kind.item` or `kind.splice`. | cite | MISMATCH | cl14:60-62, :178; dl27:54-56 |
| 14 | `derive_step_scenarios` (dl27 §4) runs at a transition into a step, and a scenario changes only at a step boundary (S8). cl14 S9 adds promoted scenarios at that point. | cite | AGREES | cl14:81-88, :148-150, :272-273; dl27:86-88, :201-204, :215, :240-241 |
| 14 | `compare_path` (dl28 S7) can find "no `skip` against [the promoted scenario] over the steps already walked". | cite | MISMATCH | cl14:84-86, :401-405; dl28:73-77, :154-157 |
| 14 | A row inherits `admits`, `entry` and `then` from its `extends` (dl27 §4). | cite | AGREES | cl14:181-183; dl27:186-187 |
| 14 | Gov's pack has one writer, `core.py new scenario`, which writes the pack only (dl27 S1). dl27 and dl28 both leave promotion to a later program. | cite | AGREES | cl14:111-113, :388-394; dl27:36-45, :108; dl28:93 |
| 14 | Re-picking a scenario between placement and close belongs to dl27's `then` edges and to dPlacedRequest. | cite | AGREES | cl14:114-115; dl27:86-88, :104-105 |
| 14 | The `loop scenario fixtures` leg (dl27 S10) and `scenario.py --fixture --plant <case>`. | cite | AGREES | cl14:337, :356-359, :365; dl27:92-97 |
| 14 | `help/loop.md` is dl1 S7's page. | cite | AGREES | cl14:92-94; dl1:85-87 |
| 14 | The owner's disposition record (dl16) lives in a build's folder under a unit id. | cite | AGREES | cl14:384-386; dl16:45-47 |
| 14 | Shared files `unattended.sh`, `unattended.test.sh`, `scenario.py`, `help/loop.md` and `tier2-review.test.sh` (dl20 S2/S3, dl27, dl28 S2, dl1 S7). cl14's at-base facts: the `flow.promote` row as at base, `review_pin.py` reading only its arguments, the harness reading no policy. | RB | AGREES | cl14:136-138, :163-165; catalogue.toml:826-830; dl20:258 ("`review_pin.py` still checks the opt-in's shape only"); dl20's `reviewPolicy` goes to the build harness (dl20:81, :201), not tier2-review; `grep -l flow.promote` over both builds' specs: no file |
| 13 | dl26 §8 F5's `compose` verb on `overlay_rows.py` is a specced precondition, and S3 reaches `compose_rows` through it. | cite / ask | MISMATCH | cl13:44-46, :66-70, :133; dl26:280-291 ("OPEN for the owner"; "The ask the build run would file is that verb"); `grep -rln overlay_rows */BACKLOG.md`: no hit |
| 13 | dl20 S2 reads `review.opt-in` one member per line. | cite | AGREES | cl13:337-338; dl20:54-55 reads through `policy.py get`; `policy.py:1347-1348` ("a list one member per line") |
| 13 | The item and stage kinds keep their step-gate class functions in their own kit's module (dl24 S7, dl25). | cite | AGREES | cl13:353-357; dl24:64-67, :184-187, :203-207 (`loop_items.py`); dl25:64-65, :193 (`splice.py`) |
| 13 | dl27 S1 and S2 are the template for the kind and namespace rows. | cite | AGREES | cl13:362, :378-380; dl27:36-49, :131-152 |
| 13 | Shared files `kinds.toml`, `namespaces.toml`, `tag_index.py`, `surface-classes.toml`, `gate-legs.json`, `subject-pins.tsv` and `kinds.md` (dl24, dl25, dl27). Every change there adds a row or an extractor. | RB | AGREES | cl13 Files touched; dl24:203-210; dl25:207; dl27:233-244 |
| 9 | The record door's `find` and `show` (tr9 S3, S5). `show <key>` gives the whole record, and `find` stops at 40 rows. | cite | AGREES | cl9:46-48, :54-55, :121, :189-191; tr9:89-96, :104-107 |
| 9 | `read_act_records` runs over "the uncapped `find --all`". | ask | MISMATCH | cl9:43-45, :199; tr9:89-96 has no `--all`; wm32:318-329; `grep -n -- '--all' dTotalRecall/BACKLOG.md`: no hit |
| 9 | `position.py <slug> --json` (dl7). | cite | AGREES | cl9:327-330; dl7:61-63 |
| 9 | tr11 lists `probe.run` among the shape-run writers, and a shape-run record holds "no token cost". | cite | MISMATCH | cl9:367-369; tr11:91-93, :175-179 (`"Out-tokens"` is a schema field) |
| 9 | The `compactions` line's item tags are `item.build.unit` and `item.review.synth` (by name). | cite | MISMATCH | cl9:158; neither tag is in any dDeclaredLoop spec (grep: the build's tags are `item.build.unit-pass`, and dl20's six `item.review.*`: trigger, pin, report, dispose, fold, cost) |
| 9 | Shared file `tools/loop/README.md` (dl7). cl9 states no at-base fact about it. | RB | AGREES | cl9 Files touched; dl7 Files touched |
| 10 | tr17 is a scorer instance, not an eval over instruction units. | cite | AGREES | cl10:463-465; tr17:34-35 |
| 10 | Shared files `replay_scorer.py` and `tools/workflows/README.md` (tr17 adds the `map-replay` row). cl10 states no instance count. | RB | AGREES | cl10 Files touched; tr17:34, :140-141 |
| 11 | "TOOL-dDeclaredLoop-32's bound counts both", and a fix pass's rounds reach `route-backs-per-build` "only where they are recorded as review rows". | cite | MISMATCH | cl11:231-232; dl32:63-71, :198-200 |
| 11 | `REVIEW_EXITS` (`tools/runlog/model.py:110`) ends a loop. dl32 edits `model.py`. | RB | AGREES | cl11:130; dl32:198-199 change only `PARK_KINDS` (`model.py:98`); `model.py:110` read |
| 15 | tr12 S9 hands the slice manifest to dWellOiledMachine, where it is unspecced. | cite | AGREES | cl15:367-369; tr12:83-86, :96, :108 |
| 15 | Shared files `runlog.py`, `selftest.py` and `README.md` (tr12 adds the `memory` verb). cl15's facts: the `extract --ready` walk, and `read_records` / `resolve_projects_root` unchanged. | RB | AGREES | cl15:57, :371-372; tr12:51-62 reuse `read_records` (:308) and `resolve_projects_root` (:185) unchanged |

**2. MISMATCH**

- **cl14, the `scenario=` field.**
  - cl14:55-56: "the scenario its build ran at the step it applied in, read from the `scenario=` field of the transition record into that step"
  - cl14:177: `extends = "<the scenario every carrier ran at that step>"`
  - dl27:81-83: "carries ` · scenario=<tag>+<tag>…`, the placed scenarios in declared order joined by `+`"
  - dl27:50: "`extends` (a scenario tag or `none`)"
  - Change: S4 has to read the field as the `+`-joined placed list. S4/S5 must then say what the candidate is keyed on, and which single tag fills `extends`, or refuse carriers placed under more than one scenario. AC6 needs a plant with two scenarios placed.
  - Cause: pre-existing.
- **cl14, the activatable kinds.**
  - cl14:61: "a row whose kind is not activatable (`kind.item` or `kind.splice`, TOOL-dDeclaredLoop-27 S3)"
  - cl14:178: `"<kind.item or kind.splice>"`
  - dl27:54-56: "the schema's `activatable` list … a set field declared `widens = \"add\"`, so each later build admits its own kind's rows by adding its kind"
  - Change: S5 and §4 "The proposed row" should read the schema's `activatable` list rather than name two kinds.
  - Cause: pre-existing.
- **cl14, `compare_path`.**
  - cl14:85-86: "`compare_path` (TOOL-dDeclaredLoop-28 S7) finding no `skip` against it over the steps already walked"
  - dl28:73-77: "At each transition out of a step, `compare_path(build, step)` sets the items the step's pinned composition declares against … Each files one order through `write_row_order` … kind `flow-deviation`"
  - The problem: dl28's function compares one step against the composition that step was pinned to, and files an order for every deviation it finds. It takes no other composition, and it cannot be called without filing.
  - Change: S9 must specify a comparison that takes the promoted composition and files nothing, either a widened `compare_path` in `tools/loop/adapt.py` (added to Files touched) or a function of its own. Otherwise S9 judges against the wrong composition and files spurious `flow-deviation` orders.
  - Cause: pre-existing.
- **cl13, the `compose` verb.**
  - cl13:44-45: "TOOL-dDeclaredLoop-26 §8 F5 (the playbook kit's `compose` verb on `overlay_rows.py`)", listed among the preconditions "each specced and unbuilt"
  - cl13:68: "reached as the playbook kit's `compose` verb run as a subprocess"
  - dl26:284-291: "(a) an ask to dOrderedCharter for a `compose` verb … The ask the build run would file is that verb. OPEN for the owner."
  - No BACKLOG holds the ask.
  - Change: §2 and §3 should say that F5 is OPEN and the verb is an unfiled ask on dOrderedCharter. The precondition becomes the owner's F5 pick plus the ask being filed, and S3 needs to say what it does under F5 (b), the declared import row.
  - Cause: pre-existing.
- **cl9, `find --all`.**
  - cl9:44: "over the uncapped `find --all` (TOOL-dWellOiledMachine-32 §8 F6, owner, 2026-10-29)"
  - cl9:199: "`read_act_records` over `gov_record.py find --all`"
  - tr9:89-96: `find [<question> --terms <words>] [--kind <k>] [--tag <t>] [--build <slug>] [--paths <glob>]` … "At most 40 rows"
  - wm32:327-329: "the build run files it in the owning build's `BACKLOG.md`". `dTotalRecall/BACKLOG.md` holds no such row.
  - Change: cl9 should say the ask is not yet filed with dTotalRecall and make its landing a build-run precondition. Until then it keeps wm32 F6's interim refusal at the total line, so no sum comes up short without notice.
  - Cause: pre-existing.
- **cl9, the shape-run's token field.**
  - cl9:368-369: "names `probe.run` among the shape-run writers, an experiment's review shape and no token cost"
  - tr11:179: the schema fields include `"Out-tokens"`
  - Change: §10 should read "output tokens only, no input-token field", which is still why the act record's `Tokens-In`/`Tokens-Out` price a probe.
  - Cause: pre-existing.
- **cl9, the example item tags.**
  - cl9:158: `compactions: item.build.unit 4, item.review.synth 1, unattributed 2`
  - dDeclaredLoop's item tags are `item.build.unit-pass` and dl20's six `item.review.*` tags (trigger, pin, report, dispose, fold, cost). Neither example tag exists.
  - Change: use real dl tags (for example `item.build.unit-pass`, `item.review.dispose`) so a fixture built from this example uses real tags.
  - Cause: pre-existing.
- **cl11, fix passes.**
  - cl11:231-232: "a fix-pass loop's rounds reach it only where they are recorded as review rows (TOOL-dDeclaredLoop-32's bound counts both)"
  - dl32:63-66: "records one fix pass … as a `fix-pass` row through `park()`, keyed by the unit, its state computed by the same `review_state` … and the same two bounds"
  - dl32:198-199: "`fix-pass` joins … `PARK_KINDS` in `tools/runlog/model.py:98`"
  - Change: §5 risks should name dl32 S5's `fix-pass` row, which is never a review row. Each loop is bounded by its own `review_state`; nothing counts the two together. The line should say `route-backs-per-build` excludes `fix-pass` rows, or reads them once runlog's `PARK_KINDS` carries them.
  - Cause: pre-existing.

**3. UNKNOWN UNTIL BUILT**

- cl14 AC4 (the swap via `--trigger`): this depends on which grammar `review.opt-in` ends up with. The catalogue spells a set, fh3 S9 spells a map, and dl20 S2 passes `get`'s output through unchanged. cl13 §8 F2's ask on dFairHearing settles it, but it is not yet filed (`grep opt-in dFairHearing/BACKLOG.md`: no hit). After that, dl20's build run decides.

**4. Ancestor text that looks wrong**

- dl20:143: `python review_pin.py <subject paths> --opt-in …` passes the subject positionally, but fh3:186 gives `--subject <path>`.
- dl20:55, :142-143: passes the `policy.py get` output of a `set` key (one name per line) as `--opt-in`, which fh3:67-69 parses as a JSON map.
- dl27:38-39 vs dl27:138: the factory is spelled two ways, `python tools/playbook/core.py new scenario <name>` and `factory = "python {prefix}/loop/scenario.py new"`.
- dl28:60, :161: `flow-state` rows are keyed by row tag alone, so two pending flow proposals on one tag cannot be told apart.
- dBoundRoles-20:62: "as TOOL-dDeclaredLoop-26 §8 F5 settles" reads F5 as settled, but dl26:291 says "OPEN for the owner".

Files read:
- /c/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-{14,13,9,10,11,15}.md
- /c/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-{1,7,16,20,24,25,26,27,28,32}.md
- /c/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-{9,11,12,17}.md
- /c/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dTotalRecall/BACKLOG.md
- /c/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dDeclaredLoop/BACKLOG.md
- /c/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/tools/policy/policy.py
- /c/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/tools/policy/catalogue.toml
- /c/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/tools/runlog/model.py

## Group B, led by spec 6 (specs 6, 5, 28, 48 and 8)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-6-1-spec-reviewer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-6-1-spec-reviewer.md).

The cross-read of Group B (specs 6, 5, 28, 48 and 8) is finished. It turned up 36 assumptions: 27 AGREES, 6 MISMATCH and 3 UNKNOWN UNTIL BUILT. All 6 mismatches are `pre-existing`, because none of the ancestor text they rest on moved in `66f7b8d32` or `58b395b6e`. Only tr1 moved in those commits (rev-5), and spec 5's keep row is unaffected: its writer is a command, not `hand`. `git diff 0d1c1dda4 HEAD` over both ancestor builds prints nothing, so line numbers hold at `0d1c1dda4`.

The serious ones:
- **cl6 §8 F4:** the per-role item-budget ask is filed nowhere. AC5 and S3's owner-wins rule depend on it.
- **cl5 AC9:** under TOOL-dTotalRecall-42 S2 it cannot exit 0 once a keep record is tracked, and the owner's first real keep would turn the `record-kinds` leg red.
- **cl5 S9:** its `item.loop.propose` row is missing three fields TOOL-dDeclaredLoop-12 requires and misses dl12's `returns` form. The `cadence.loop` step value it uses is one no dDeclaredLoop spec or BACKLOG row admits.

#### 1. Table

| Spec | Assumption about the ancestor | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 6 | tr9 S6 reads `measured` as 96,000 B for every role until 30 sliced work orders, names no reading after, and hands each role's p90 to the Loop Review; that is "tr9's reading today" (cl6:26-29, :104-106, :149-150) | cite | AGREES | tr9:110-111, :142, :359-361 (F4) |
| 6 | tr9 S8 has `render_handoff` write a `reads:` list, one key per line with its bytes, the only writer of a work order's slice bytes (cl6:38-40, :106, :320-323) | cite | AGREES | tr9:119-122 ("one key per line with its bytes and any mark") |
| 6 | The `reads:` list stays a block of its own whose lines S1 parses as `<key> <bytes>`, and a work order with no such block is unsliced (cl6:36-42) | cite | UNKNOWN UNTIL BUILT | tr9:121-122 gives no line grammar beyond "bytes and any mark"; dTotalRecall BACKLOG.md:22 (tr104, open) asks that the list be rendered as the body of the `### memory` slot through `render_slot` |
| 6 | "TOOL-dTotalRecall-9 §4 treats it as the work order" (cl6:107-109) | cite | MISMATCH | tr9 §4 (:167-262) says nothing about it; it is tr9 S8 :119 and §10 :398-399 |
| 6 | `check_read_set` lives in `record_find.py`, run as `gov_record.py budget --role`; over the cap under `report` it prints `memory over budget: <role> <bytes> B > <cap> B` (cl6:63-64, AC7 :291-295) | cite | AGREES | tr9:108-114 |
| 6 | "`record_find.py` and `gov_record.py` are TOOL-dTotalRecall-9's" (cl6:301) | cite | MISMATCH | tr9:151-152: `gov_record.py` is TOOL-dTotalRecall-2's door; tr9 adds only the `find`, `show` and `budget` verbs |
| 6 | dTotalRecall is the key's owner, and tr9 S6 already reads "a per-role value" (cl6:80, :337-343) | cite | AGREES | tr9:17 (`Carries: node:policy-key.memory.item-budget`), :111; catalogue.toml at `8bec4cef` :1457-1461 (`owner = "dTotalRecall"`) |
| 6 | Ask F4, THE ITEM BUDGET HAS NO PER-ROLE FORM, is filed in `memory/builds/dTotalRecall/BACKLOG.md` and lands before this unit's pass; S3, S5 and AC5 rely on it (cl6:51, :80, :87, :145, :286, :337-349) | ask | MISMATCH | The BACKLOG holds tr27-35 and tr101-106 and no such row; `git grep -n -i "per-role form\|item budget has no" 0d1c1dda4 -- memory` matches only cl6 itself. tr9 neither serves nor refuses it: S10 :130-133 adds only `summary` and `usage` |
| 6 | The slice manifest has no producer: tr12 S9 hands it to dWellOiledMachine's executor, ask tr35 is still open, and tr12 reads the channel `unarmed` until then (cl6:81-82, :317-319, :379) | cite | AGREES | tr12:54-55, :83-85, :108; dTotalRecall BACKLOG.md:13, :39-40 |
| 6 | The owner writes through `policy_edit.py set` at a terminal; `propose <key> <value>` writes nothing and prints the row diff and the command (cl6:57-62, :78-79, :93, :143) | cite | AGREES | dl2:61-68 (S4), :206-208 |
| 6 | Under the default guard, an agent's staged `memory.item-budget` change is refused (cl6:239-242, by name) | cite | AGREES | dl2:44-50 (S1), :190 (`owner-only`: "every other write refused") |
| 6 | RB `tools/roles/handoff.py`: `render_handoff` at `:312`, verbs `check` and `roster`, `MARKER_RE`; tr9 S8 changes `render_handoff` and its CLI, and cl6 names it | RB | AGREES | tr9:119-125 adds `--read` and the list only; at `8bec4cef` `handoff.py:942` `render`, `:955` `check`, `:956` `roster`; `roles_lib.py:79` |
| 6 | RB `tools/memory-tree/record_find.py`: S6 adds `read_measured_item_budget` beside tr9's `check_read_set`, and names tr9 S6 | RB | AGREES | tr9:108, :238 (new file); no at-base fact is stated |
| 5 | The registry `record-kinds.toml` and `record_kinds.py` are tr1's; the keep row's columns are tr1 S1's, and its writer is a door (cl5:48, :157, :246-260, :277, :468) | cite | AGREES | tr1:66-71 (S1), :78-89 (S3), :195-200 (writer bullet, rev-5: `hand` is legal on rows tr2 S9 does not move, and keep's writer is `loop_review.py keep`, not `hand`) |
| 5 | The keep row carries `unarmed = "no keep is tracked until the owner's first keep"`, and AC9 has `record_kinds.py --check` exit 0 in a scratch worktree holding one well-formed keep record (cl5:317-319, :463-466, by name) | cite | MISMATCH | tr42:40-46 (S2): the check "reds the row, naming the key, once its home matches a file, so the declaration cannot outlive its population" |
| 5 | The keep record is graded by its own row through its `**Serves:** keep` line, and the home is the id-rule's glob (cl5:286-290) | cite | AGREES | tr42:50-58 (S4 refuses a bare directory; S5 `derive_record_kind`) |
| 5 | `item.loop.propose` is "in TOOL-dDeclaredLoop-12's row form" with `step = "cadence.loop"`, `actor`, `needs`, `outcomes`, `routes`, `returns = "proposals"`, `owner` (cl5:121-125) | cite | MISMATCH | dl12:113 (`returns` is "the record kind it writes", `record-kind.<name>`), :127-130 (`inputs`, `allowance` and `returns` required for a non-role actor; `witness` required); dl50:44-48 admits only `step = "none"`, on `item.review.*` rows; dDeclaredLoop BACKLOG.md (26 lines) holds no cadence-step ask |
| 5 | "dDeclaredLoop's breakpoints call `keep` once they land" (cl5:147, by name) | cite | MISMATCH | dl19 S1-S7 (breakpoints) and dl20 hold no call to `loop_review.py keep`; an owner gate is released by "the owner's disposition record" (dl19 S6). `grep -n "loop_review\|keep record"` over the dDeclaredLoop specs: no hit |
| 5 | RB `record-kinds.toml`, `HYGIENE.template.md`, `tree_lib.py` `TYPED_RECORD_KINDS`: a row, the closed `<kind>` prose list and a tuple member are added; the registry view is regenerated by `record_kinds.py --write` | RB | AGREES | tr1:84-85 (S2), :92-96 (S6 adds a new `gen:record-kinds` section and leaves the `<kind>` prose list at HYGIENE.template.md:628 authored), :241-243 |
| 28 | tr9 S3 caps `gov_record.py find` at 40 rows and then prints `<total> rows match; narrow ...` (cl28:22-23, :66) | cite | AGREES | tr9:94-96, AC4 :294-297 |
| 28 | `find`'s order is not by commit time (cl28:25-26) | cite | AGREES | tr9:207 ("Rows sort by build, then key") |
| 28 | A record is read through `gov_record.py show` (cl28:36-37) | cite | AGREES | tr9:104-107 (S5) |
| 28 | `find`'s cap and order are tr9's to change (cl28:51) | cite | AGREES | tr9:89-96, §5 risks :272 |
| 48 | Spec 33's §4 is re-cited to tr42 S5 and §5, where the grader admits a path inside `derive_record_kind` (cl48:68-70) | cite | AGREES | tr42:53-58 (S5), :137 (§5 "one glob match and one dict lookup per record") |
| 8 | `review.dispose`'s module is `tools/loop/review_dispose.py`, and the DISPOSAL stage in `unattended-build.template.js` runs `review_dispose.py classes` (cl8:45-46, :82-85, :127, :327) | cite | AGREES | dl20:74-78 (S6), :190-195, :238 |
| 8 | `review_dispose.py classes` "reads `disposition` by name as well (TOOL-dDeclaredLoop-20 §4)" (cl8:141-142) | cite | UNKNOWN UNTIL BUILT | dl20:190 says only that it "reads every review record's disposition column"; it says neither by header name nor by position |
| 8 | The map and its renderer are tr14's (cl8:109) | cite | AGREES | tr14:46-50 (S2 `gov_map.py`), :37-44 (Goal) |
| 8 | The map's pre-build losing test is tr17, whose `lose` files the slice-manifest-only ask on dCalibratedLens (cl8:110) | cite | AGREES | tr17:65-70 (S7), :144-145 |
| 8 | On `lose`, S3 "already computes the cause without the map", so the tr17 ask is served (cl8:110-112) | cite | MISMATCH | tr17:68-69: the ask is "compute its not-in-view cause from the slice manifest alone"; cl8 S3 (:56-63) counts every `ORDER_SLOTS` slot's paths (`code`, `bug-classes` and others) |
| 8 | No spec writes a slice manifest: tr12 S9 hands it to dWellOiledMachine's executor, and tr9 §3 to dBoundRoles' renderer (cl8:131, :314-316) | cite | AGREES | tr12:83-85, :96-97; tr9:137-138 |
| 8 | A `cause` verb on `review_dispose.py` would need a second appendix parser, since the loop kit imports no sibling (cl8:327-330, F3) | cite | AGREES | dl20:77-78, :190 (`review_dispose.py` sits in the loop kit, `tools/loop/`, and reads the disposition column itself) |
| 8 | RB `unattended-build.template.js` and its render: dl20 §2 S4, S5, S7 and S8 change the DISPOSAL stage and the fold instruction; cl8 states no at-base fact about them and names dl20 S6 for the call it sits beside | RB | AGREES | dl20:64-73, :84-87, :238-239; cl8 S5 :82-86 |
| 8 | RB `tools/workflows/README.md`: dl20 and cl8 each add a name | RB | AGREES | dl20:240; cl8:233; no at-base fact is stated |
| 8 | RB `tools/roles/handoff.py`: `orders` sits beside `roster` (`:956`), markers are read through `MARKER_RE` (`roles_lib.py:79-80`); tr9 S8 (cited in F2) changes only `render` and its list | RB | AGREES | tr9:119-125; `8bec4cef` `handoff.py:956`, `roles_lib.py:79-80` |
| 8 | RB `tools/workflows/replay_scorer.py`: `parse_appendix_rows` keeps its confirmed-only filter; tr17 S1 adds a `map-replay` row to `INSTANCES` and touches no parser | RB | AGREES | tr17:33-40 |
| 6, 8 | Ask tr35 (the slice channel has no producer) is a BACKLOG row of dTotalRecall | cite | AGREES | dTotalRecall BACKLOG.md:13, :39-40 (DEFERRED until tr12) |

#### 2. MISMATCH

- **cl6:107-109 vs tr9 §4.** cl6 says: "its marker line carrying the role (`tools/roles/roles_lib.py:79`); TOOL-dTotalRecall-9 §4 treats it as the work order." tr9 §4 holds no such sentence. tr9:119 (S8) reads "The work order: `render_handoff` (`tools/roles/handoff.py:312`)", and tr9:398-399 (§10) reads "`render_handoff` renders the role handoff this unit treats as the work order."
  Change: re-cite the line to TOOL-dTotalRecall-9 S8 (and §10).
  Cause: pre-existing.

- **cl6:301 vs tr9:151-152.** cl6 says: "permission: `record_find.py` and `gov_record.py` are TOOL-dTotalRecall-9's, built before this pass." tr9 says: "**consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py`, the door CLI that gains the `find`, `show` and `budget` verbs."
  Change: AC7's permission line should read that `gov_record.py` is TOOL-dTotalRecall-2's door and its `budget` verb is TOOL-dTotalRecall-9 S6's. The precondition still holds through tr9's own edge, so nothing else moves.
  Cause: pre-existing.

- **cl6 §8 F4 (:341-349; relied on at :51, :80, :87, :145, :286) vs the dTotalRecall BACKLOG.** cl6 says: "RESOLVED (agent, 2026-11-02, delegated): (a), the main loop files it in `memory/builds/dTotalRecall/BACKLOG.md` · THE ITEM BUDGET HAS NO PER-ROLE FORM … Build-run precondition." The ancestor side is an absence: `memory/builds/dTotalRecall/BACKLOG.md` (47 lines) has no such row, and `git grep -n -i "per-role form\|item budget has no" 0d1c1dda4 -- memory` matches only cl6:342. tr9 S10 (:130-133) adds only `summary` and `usage` to the row, and the row at `8bec4cef` (`catalogue.toml:1457-1461`) still admits only `measured`, 96 and 128.
  Change: the main loop files the row in dTotalRecall's BACKLOG with cl6 F4's text, and cl6 F4 cites its filed id. Until it is filed and served, cl6 should mark S3's per-role member, S5's `memory.item-budget."<role>"` key path and AC5 as blocked on it. `policy_edit.py propose` (dl2:208) checks no member grammar of its own, so the ask is the only home for that key path.
  Cause: pre-existing.

- **cl5 AC9 (:463-466) and id 37 (:317-319) vs tr42 S2 (:40-46).** cl5 says: "The row carries `unarmed = "no keep is tracked until the owner's first keep"`" and "When `python record_kinds.py --check` runs in a scratch worktree holding one keep record that lacks `Words`, it exits 1 naming the record; with the field restored it exits 0." tr42 says: "`check_record_kinds` … passes that row while its home matches no tracked file … and it reds the row, naming the key, once its home matches a file, so the declaration cannot outlive its population."
  Change: AC9's "field restored" case should expect exit 1 naming `unarmed`, or plant the record against a scratch registry row with no `unarmed` key. S8 should also say who drops the `unarmed` key when the first real keep is committed; otherwise the owner's first `keep` turns the `record-kinds` leg red. Cite TOOL-dTotalRecall-42 S2 for the key. The `three-homes` plant that commits a keep (r2 id 1) meets the same rule.
  Cause: pre-existing.

- **cl5 S9 (:121-125) vs dl12 §4 (:108-130) and dl50 S3 (:44-48).** cl5 says: "The item row `item.loop.propose` in `tools/loop/loop.toml`, in TOOL-dDeclaredLoop-12's row form: `step = "cadence.loop"`, `actor = "command:loop.propose"`, `needs = [...]`, `outcomes = ["proposed"]`, `routes = {...}`, `returns = "proposals"`, `owner = "dCalibratedLens"`." dl12 says: "`returns = "record-kind.recommendation" # its return template: the record kind it writes`", "`inputs` | yes for a non-role actor", "`allowance`, `returns` | yes for a non-role actor", "`witness` | yes". dl50 says: "an `[[item]]` row may carry `step = "none"` when its tag's middle segment is `review` … `check_program` … admits `none` for those rows alone."
  Change: cl5 S9 should give the row `inputs`, `allowance` and `witness`, and spell `returns` as a `record-kind.<name>`. It should also name the cadence-step ask of TOOL-dCalibratedLens-3 §8 F5 ("THE LOOP KIT REFUSES A CADENCE STEP VALUE") as a build-run precondition of S9 and AC5. dDeclaredLoop's BACKLOG does not hold that ask yet.
  Cause: pre-existing.

- **cl5:147 vs dl19 S6 and dl20.** cl5 says: "Writing the keep at the owner's breakpoint: dDeclaredLoop's breakpoints call `keep` once they land; until then the owner runs it." No dDeclaredLoop text says this. dl19 S6 says "An owner gate holds as an `owner-decision` hold on a `decision` row naming the gate, released only by the owner's disposition record through `check_owner_disposition`." No dDeclaredLoop spec or BACKLOG row names `loop_review.py keep`.
  Change: either drop the forward claim and say the owner runs `keep`, or file an ask on dDeclaredLoop (TOOL-dDeclaredLoop-19's breakpoint disposition) and cite it.
  Cause: pre-existing.

- **cl8:110-112 vs tr17 S7 (:65-70).** cl8 says: "TOOL-dTotalRecall-17, whose `lose` files the slice-manifest-only ask here; S3 already computes the cause without the map, so on `lose` every cell reads `/no-map`." tr17 says: "dCalibratedLens is asked to compute its not-in-view cause from the slice manifest alone." cl8 S3 (:56-63) makes the view "every path it spells: the slice manifest, the map, the code slot and the other slots' bodies, the `bug-classes` slot's class paths among them".
  Change: cl8 §3 should say that, on `lose`, S3's view drops only the map slot and still counts the other slots. The ask as tr17 words it ("slice manifest alone") is therefore not met by S3 as written. Either S3 restricts the view to the slices when the verdict is `lose`, or the ask's disposal records the wider view as a departure.
  Cause: pre-existing.

#### 3. UNKNOWN UNTIL BUILT

- **cl6 S1, the `reads:` list's line grammar and block.** tr9 S8 does not fix the line grammar beyond "key, bytes and any mark", and the open ask tr104 (dTotalRecall BACKLOG.md:22) may move the list into the `### memory` slot's body. tr104's disposal and tr9's build run decide it.
- **cl8:141-142, `review_dispose.py classes` reading `disposition` by name.** TOOL-dDeclaredLoop-20's build run decides it. Both new columns are appended after `disposition`, so either reading survives them.
- **cl6 S5, the `policy_edit.py propose memory.item-budget."<role>"` key path.** It is decided only once the F4 ask is filed and dTotalRecall builds the per-role grammar (see the F4 mismatch). dl2 S4 checks only against the catalogue row.

#### 4. Ancestor text that looks wrong

- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-14.md:97` gives "the work order's `map` slot, its unfolds and `memory.project-map`" to dBoundRoles. The catalogue at `8bec4cef` (`tools/policy/catalogue.toml:1479`) has `owner = "dFurnishedOrders"`, and ask tr102 (BACKLOG.md:20) is still open on it.
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-9.md:137` gives "writing the slice manifest" to "dBoundRoles' renderer and the executor's". TOOL-dTotalRecall-12:83-85 and ask tr35 (BACKLOG.md:13) place it with dWellOiledMachine's executor alone.

Files read: `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dCalibratedLens\spec\2026-11-02-spec-TOOL-dCalibratedLens-{6,5,28,8}.md`, `...\2026-11-03-spec-TOOL-dCalibratedLens-48.md`, `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-{1,9,12,14,17,42}.md`, `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-{2,12,19,20,50}.md`, and `C:\projects\coding-governance\.claude\worktrees\musing-colden-d318c6\memory\builds\{dTotalRecall,dDeclaredLoop}\BACKLOG.md`.

## Group C, led by spec 7 (specs 7, 33, 34 and 32)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-7-1-spec-reviewer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-7-1-spec-reviewer.md).

#### TOOL-dCalibratedLens-7, Group C: cross-check against dTotalRecall and dDeclaredLoop at `0d1c1dda4`

I read all four specs (7, 33, 34, 32) whole, with their rev lines. The ancestor units read were dl20, tr11, tr42, tr53 and tr1, plus tr18 S7 where tr42 S5 cites it. Neither ancestor build's tree moved between `0d1c1dda4` and HEAD (`git diff --name-only 0d1c1dda4 HEAD -- memory/builds/dTotalRecall memory/builds/dDeclaredLoop` printed nothing). Of the two revision commits, only tr1 rev-5 touches a unit this group cites, and none of its changed lines is one these specs rely on.

The result is one MISMATCH and three UNKNOWN UNTIL BUILT; every other row agrees. The mismatch: cl7 says dDeclaredLoop-20's `review.cost` writes the review shape-run records, but no spec in either build calls the `--review` writer.

##### 1. Table

| Spec | Assumption about the ancestor | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 7 | tr11 registers the `shape-run` kind. Its record is `<date>-build-<unit id>-shape-run-<n>.md`, with `Kind` to `Out-tokens` and `Caused-by` required, and `Trigger`/`Shape`/`Efforts`/`Role-sha` present only when the line carries them. Its writer is `gov_record.py new shape-run --review`. | cite | AGREES | cl7:31-33, :88-90, :225; tr11:60-65, :155-162, :176 |
| 7 | S1 reads `builds/*/build/*-shape-run-*.md` and takes each record's date from the file name's `<date>` | cite | AGREES | cl7:39-41; tr42:36-38, :89; tr11:176 |
| 7 | `Kind` is `spec-audit` or `diff-review`. `Out-tokens` is a number or `unknown`. A count may read `-` and never means 0. | cite | AGREES | cl7:44-49, :50-53; tr11:121, :126, :130-131 |
| 7 | dl20 S3 appends `trigger=` `shape=` `efforts=` `role-sha=`, with `shape=` reading `-` until dBoundRoles lands its registry | cite | AGREES | cl7:34-35, :45-47, :86-87; dl20:59-62, and dl20 §4 "The record line" |
| 7 | **`review.cost` (dl20 S3) writes the shape-run records for review acts and is one of the kind's "two writers"** | cite | **MISMATCH** | cl7:25-26, :60-61, :66-67, :166; dl20:59-62, :130; tr11:60, :91-93; tr42:45, :91 |
| 7 | tr11 S1 makes `shape_run.py` the line's one parser. `check_shape_runs` compares each record with its line. The CLI parses lines, not records. | cite | AGREES | cl7:141-144, :232-234; tr11:46-52, :66-69 |
| 7 | The act form (`--act`, `Kind` `act`, `Workflow` `Shape` `Shape-match` `Agents` `Efforts` `Out-tokens` `Caused-by`) is an ask filed on dTotalRecall. Note: the ask is named at cl7:93 (§4 Evidence, as wm19 §8 F2), not at cl7 §8 F2, which is about catches. | ask | AGREES (the row exists and says it; tr11 neither serves nor refuses it) | cl7:35, :91-93; dTotalRecall/BACKLOG.md:15 (TOOL-dTotalRecall-105, required `Workflow`, `Shape`, `Shape-match`, `Agents`, `Out-tokens`, `Caused-by`, optional `Efforts`...), :43; tr11:60 (`--review` only), :121 (closed `kind` set) |
| 7 | RB: cl7 states facts about `renderShapeLine`, the `-` rule and output-only tokens (`tier2-review.template.js:74-86`). dl20 §2 S3 changes that function, and cl7 names dl20 S3 at :86. tr11 S7 changes `tier2-review.test.sh` and `README.md`, which cl7 states nothing about. | RB | AGREES | cl7:84-87, :163-164; dl20:59-62; tr11:79-85; `git show 8bec4cef:tools/workflows/tier2-review.template.js` :74-86 matches cl7's account |
| 33 | `record_kinds.py --check` grades by Serves kind and stays green whether homes overlap or not. tr42 rejected refusing overlapping homes, saying "deciding by the Serves kind needs no disjoint homes". | cite | AGREES | cl33:24-25, :52-54, :76-77; tr42:53-58, :106-108, :126-128 |
| 33 | tr42 S5 and its §5 "one glob match and one dict lookup per record" moved past tr1 §5's "one `git ls-files` per home glob" | cite | AGREES (tr1's line is now :303, not :297, after rev-5; drift only) | cl33:68-72; tr42:137; tr1:303 (was :297 at `22a8efac3`) |
| 33 | `derive_record_kind(path, <kind>, rows)` takes a kind as its second argument (tr53 S21). Passing a row's name with `[row]` returns that row exactly when its home admits the path. A tr42-form function reads the argument as text and admits nothing. | cite | AGREES | cl33:37-41, :73-75, :105-107; tr53:94-96; tr42:53-56; tr18:168 (`canonical_kind` is identity on a non-alias) |
| 33 | tr42 S1 makes the shape-run home name its own kind (narrowed to its id-rule glob) | cite | AGREES | cl33:94-96; tr42:29-32, :36-38 |
| 33 | RB: Files touched is `tools/loop/loop_review.py`, which no cited unit's §2 changes. The registry facts are build-run preconditions, and the one ancestor change to them (tr53 S21) is named. | RB | AGREES | cl33:85-87; tr42:36-58; tr53:94-96 |
| 34 | tr1 S4 grades every tracked record under a home against that row's fields | cite | AGREES (rev-5 changed only the §4 writer bullet and the note under the rows) | cl34:23-24, :76-77; tr1:87-89; `git diff 22a8efac3 0d1c1dda4 -- …dTotalRecall-1.md` |
| 34 | tr42 S4 and S5 at their revision moved grading to the Serves kind ("deciding by the Serves kind needs no disjoint homes") | cite | AGREES (tr42 is at rev-2, unmoved) | cl34:24-25, :35-37, :40-41, :78-79; tr42:51-58, :127-128, :191 |
| 34 | RB: Files touched is `memory/gotchas/*`, `INDEX.md` and `memory/map/generated/`. No cited unit's §2 touches them. | RB | AGREES | cl34:100-102; tr42:36-58; tr1:87-89 |
| 32 | tr42 S4: `check_record_kinds` reds a home that ends in `/` or names a directory, naming the row (H1 by name, and §1, §3, §4, §10) | cite | AGREES | cl32:1, :27-28, :52-53, :63-65, :143-144; tr42:51-52, :160-162 |
| 32 | tr42 S5 and its table: a record under two homes is graded once by its kind, and a mismatch is counted only when the Serves kind names another row, never red | cite | AGREES | cl32:25-27, :66-67, :85-87; tr42:53-58, :101-103, :106-108 |
| 32 | The registry `tools/memory-tree/record-kinds.toml` and `record_kinds.py` are tr1's and tr42's | cite | AGREES | cl32:38, :70-71; tr42:36, :41, :118-119; tr1:152 |
| 32 | AC2: the unmutated registry check exits 0 in the plant's scratch worktree | cite | UNKNOWN UNTIL BUILT | cl32:110-111; tr42:40-46, :151-152; tr53:101-103 (the S23 homeless arm) |
| 32 | RB: Files touched is `tools/loop/loop_review.py`, which no cited unit's §2 changes | RB | AGREES | cl32:79-81; tr42:36-58 |

##### 2. MISMATCH

- **cl7: review-act shape-run records written by `review.cost`.**
  - cl7:25-26 says "the shape-run records `review.cost` writes for review acts (TOOL-dDeclaredLoop-20 S3, recorded by TOOL-dTotalRecall-11)". cl7:66-67 lists the kind's writers as "TOOL-dTotalRecall-11, TOOL-dDeclaredLoop-20 S3 and TOOL-dWellOiledMachine-19 S6", and S6 (:60-61) documents "its two writers".
  - The ancestor says otherwise. dl20:59-62 has S3 only adding fields to the line ("`renderShapeLine` … appends `trigger=`, `shape=`, `efforts=` and `role-sha=`"). Its item row, dl20:130, has the witness "the `review-shape` line's cost fields". tr42:45 sets `unarmed = "no writer calls gov_record.py new shape-run yet"`.
  - Probes:
    - `git grep -c -E 'shape-run|shape_run' 0d1c1dda4 -- memory/builds/dDeclaredLoop/` matched nothing (exit 1).
    - `git grep -E 'shape-run.{0,20}--review|new shape-run' 0d1c1dda4 -- 'memory/builds/*/spec/*' 'memory/builds/*/BACKLOG.md'` found the `--review` form only in tr11 and in cl7 itself.
    - Neither build's `BACKLOG.md` holds an ask for the writer.
  - Consequence: AC1 to AC4 still pass, because they plant their records, but on the live tree no review exit writes a record. Every `spec-audit/…` and `diff-review/…` row prices nothing and the summary reads `0 review`. That is the outcome cl7:149-150 rejects for unshaped records.
  - Change: re-cite dl20 S3 as the source of the line's four fields only. State that tr11 S4's `--review` verb has no caller in any ancestor spec (tr42:45). Then either file an ask, in dDeclaredLoop's or dTotalRecall's `BACKLOG.md`, for a writer calling `gov_record.py new shape-run --review` at each review exit and list it as a build-run precondition in §2, or have §5 and AC3 state that review rows stay empty until that writer lands. Revise S6's "two writers" to match.
  - Cause: `pre-existing` (dl20 and tr11 are not in `git diff --name-only 22a8efac3 0d1c1dda4`).

##### 3. UNKNOWN UNTIL BUILT

- **cl7, act form:** dTotalRecall's disposal of TOOL-dTotalRecall-105 decides whether tr11 gains `--act` and `Kind` `act`. Today's grammar (tr11:121) admits only `diff-review|spec-audit`, and tr11:68 requires `Caused-by` to name a review record. cl7's §2 preconditions (:35) credit the `--act` form to wm19 S6 rather than naming TOOL-dTotalRecall-105.
- **cl33, glob dialect of `derive_record_kind`'s home match:** tr42/tr53's build run decides it. tr42:137 says only "one glob match"; cl33:73-75 already defers to the shipped module.
- **cl32 AC2, unmutated check exits 0 in the scratch worktree:** the shipped `check_record_kinds` decides it, including the `unarmed` rows of tr42 S2 and the homeless arm of tr53 S23, as built over the real tree at dCalibratedLens's build time.

##### 4. Ancestor text that looks wrong

- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-11.md:91-92` names "`review.cost`'s review act row (TOOL-dDeclaredLoop-20)" as a writer that calls `gov_record.py new shape-run`. dl20 S3 (`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-20.md:59-62`, :130) writes no record and names no door.
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-53.md:94-96`: S21 restates `derive_record_kind`'s signature but does not say whether `canonical_kind` still applies to `written_kind`, which tr42:54-55 makes the match rule.

## Group D, led by spec 16 (specs 16, 2, 19 and 4)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-16-1-spec-reviewer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-16-1-spec-reviewer.md).

#### Group D cross-check: specs 16, 2, 19 and 4 against dTotalRecall and dDeclaredLoop at `0d1c1dda4`

Every probe was a read. I checked that `git diff --name-only 0d1c1dda4 HEAD` names no dTotalRecall or dDeclaredLoop spec, so these ancestor texts are the same as on origin/main. The dCalibratedLens specs were read as they stand now. Of the two revising commits, only tr1 rev-5 (`58b395b6e`) touches a cited unit, and it changes nothing these four specs rely on. All 11 MISMATCHes are therefore `pre-existing`. Paths: `memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-{16,2,19,4}.md`, and under `memory/builds/{dDeclaredLoop,dTotalRecall}/spec/`.

##### 1. Table

| Spec | Assumption about the ancestor | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 16 | An instance key is `<item tag>@<round\|pass>#<inputs>`, so the item is the text before `@` (dl7 S3) | cite | AGREES | cl16:64-65, AC3 :281-282 · dl7:45-49 |
| 16 | `read_transitions` exists and reads a build's transition records newest first (dl3 S7) | cite | AGREES | cl16:67, :122, :392 · dl3:69-73 |
| 16 | Each transition record gives a time and a commit, so S4 can take "the newest … at or before the line's `t`" and S8 can run `policy.py get --rev <the commit of its newest transition record>` | cite | UNKNOWN UNTIL BUILT | cl16:66-67, :88-91 · dl3:69-73 (return shape not stated); dl3:42-46 (fields `Build`, `From`, `To`, `Item`, `Sha`; `Sha` is the witness commit) |
| 16 | The `scenario` field of a transition record is one scenario tag, used as the tuple's scenario (`scenario.feature`) | cite | MISMATCH | cl16:65-67, AC3 :284-286, AC12 :320-321 · dl27:80-83 |
| 16 | Draw and freeze row grammar; `record_draw` returns `exhausted`; `budget_state` reads those rows (dl30 S2, S3) | cite | AGREES | cl16:139-141, :149, :348 · dl30:39, :43-51, :131, :135 |
| 16 | `flow.rework-budget` takes the form `<base>+<per-unit>` and both flow keys are `raise-loosens` | cite | AGREES | cl16:109-110, :149, :166 · dl30:32-36 |
| 16 | `flow.rework-budget` evidence is `max(0, spent - per_unit*units)` per build; AC7 plants spends of 3 to 32 under `4+2` with one unit | cite | MISMATCH | cl16:149, AC7 :298-304 · dl30:37-41, :49-50 |
| 16 | `flow.route-backs` evidence is "the most `route-back` draws one item took" | cite | MISMATCH | cl16:150 · dl30:62-63 |
| 16 | A build "ran under" `flow.rework-budget` when the value at its newest transition's commit equals HEAD's | cite | MISMATCH | cl16:88-91 · dl30:37-42 |
| 16 | A closed build's draw rows are fixed at close, so the first record after close keeps them and no later record re-reads them (S7, id 54) | cite | MISMATCH | cl16:81-87, :228-231 · dl30:67-71 |
| 16 | `policy_edit.py propose <key> <value>` writes nothing and prints the row diff and an apply command (dl2) | cite | AGREES | cl16:115, :165-166, :254-255 · dl2:61-63, :208 |
| 16, 4 | The proposal's `accept` is "the `policy_edit.py set` command propose printed", applied by the owner, for keys such as `flow.rework-budget` and `budgets."AGENTS.md"` | cite | UNKNOWN UNTIL BUILT | cl16:206-207; cl4:220, :172-173 · dl2:206 (`set … --unit <id>`, typed `yes`), :207 (`raise`), :208 (propose: "the command that would apply it") |
| 16 | `gov_record.py find --kind --build` and `show <id>`; `find` caps output at 40 rows, which id 50 avoids by not calling `find` (tr9 S3, S5) | cite | AGREES | cl16:69, :115, :122, :215 · tr9:89-96, :104-107 |
| 16 | `help/loop.md` "gains a section" (S9) | RB | AGREES | cl16:95, :239 · dl1:85-87 creates the page; dl3, dl27 S11 and dl30 S10 add sections only |
| 16 | `measure.py`, `loop_review.py`, `tools/runtime/journal.py` and its README | RB | AGREES | cl16:235-238 · no cited dl or tr §2 names these files |
| 2 | dl1 gives the loop kit `tools/loop/`, its `kit.toml` and `loop.toml` | cite | AGREES | cl2:47-48, :156 · dl1:54-61 |
| 2 | The `item.loop.price` row is "in the row form of TOOL-dDeclaredLoop-12 §4 'Data model'" with keys `step`, `actor`, `needs`, `outcomes`, `routes`, `returns`, `owner` | cite | MISMATCH | cl2:112-118 · dl12:105-130; dl9:29-34 |
| 2 | `check_program` grades the routes, and the `stand-in:<path>` route word is legal; `loop_lib.py --check` runs it | cite | AGREES | cl2:115, :266, AC8 :435-438 · dl12:39-44, :145-153 |
| 2 | AC8 passing depends on "the ask F5 states" (cl3 §8 F5, filed on dDeclaredLoop) | ask | MISMATCH | cl2:323-325; cl3:529-534 · `grep -n 'CADENCE' memory/builds/dDeclaredLoop/BACKLOG.md` prints nothing (0 of 26 lines); `grep -rn 'CADENCE STEP VALUE'` hits only cl3:530 |
| 2, 4 | The leg is claimed by a new dossier `memory/map/features/loop-review.md` "(new when no dossier claims `tools/loop/`)" | RB | MISMATCH | cl2:318-322, :362; cl4:244-246, :263 · dl1:85, :260, :318; dl3:237 |
| 2 | dl1 provides `record-kinds.toml` and its `record-kinds` leg; `check = "record-kinds"` names that leg | cite | AGREES | cl2:50, :156, :241 · tr1:66-70, :78-86 |
| 2 | `value-ledger` joins `TYPED_RECORD_KINDS`, its snapshot at `memory/loop-review/<date>-value-ledger-<key>.md` | cite | MISMATCH | cl2:279-283, :359, :97 · tr1:71-77, :222-224; dOC42:35-49 |
| 2 | `record_kinds.py --write` renders the `gen:record-kinds` region, then `--render` copies it (tr1 S6) | cite | AGREES | cl2:309-312 · tr1:92-95, :230-236 |
| 2 | Writer cell `loop_review.py price; loop_review.py record` (tr1 rev-5, the `hand` rule) | cite | AGREES | cl2:303-304 · tr1:195-200, :414-417 (applies to `hand` rows only) |
| 2 | Home `memory/loop-review/*-value-ledger-*.md`, spelled as tr42 S1 spells the shape-run home | cite | AGREES | cl2:275-277 · tr42:36-39 |
| 2 | The row carries `unarmed` "until `loop_review.py record` lands the first period" | cite | MISMATCH | cl2:305-308 · tr42:40-46 |
| 2 | tr42 S5 grades the snapshot by its own row | cite | AGREES | cl2:282-283 · tr42:53-59 |
| 2 | `record-kinds.toml`, `HYGIENE.template.md`, `loop.toml`, `kit.toml`: rows or regions are added and no at-base fact is relied on | RB | AGREES | cl2:349-355 · tr1:66, :92-95 and dl12:34-37 are additive |
| 19 | tr42 S4 refuses a home that ends in `/` or names a directory, naming the row | cite | AGREES | cl19:27-28, :58-59 · tr42:51-52 |
| 19 | tr42 S5 grades a record once, by its Serves kind, so overlapping homes give no red; tr1 S4's reading is replaced; tr42 rejected a disjoint-homes refusal | cite | AGREES | cl19:28-31, :52, :67-69, :117-118 · tr42:53-59, :126-128; tr1:87-89 |
| 19 | The precedent: tr42 S1 narrows a home to its id-rule's glob | cite | AGREES | cl19:41, :93-94, :183 · tr42:36-39 |
| 19 | `record_kinds.py --check` is tr1's and absent at base | cite | AGREES | cl19:49-50, :151 · tr1:78-80 |
| 19 | The `three-homes` plant (a scratch worktree, one snapshot and one record committed) gets exit 0 from `record_kinds.py --check` | cite | MISMATCH | cl19:47-51, AC2 :147-151 · tr42:40-46; cl2:305-307, cl3:326-327 |
| 19 | (by name, cl19:122) a rejected ask on dTotalRecall to scope S4 by `id-rule`; the owner is tr42 S4, and no ask is relied on | cite | AGREES | cl19:122-123 · tr42:51-52 |
| 19 | `tools/loop/loop_review.py`, the only file touched | RB | AGREES | cl19:113 · no cited dl or tr §2 names it |
| 4 | `python tools/loop/policy_edit.py propose <key> <value>` writes nothing and prints the row diff and the command (dl2 S4) | cite | AGREES | cl4:45-51, :107-110, :119, :198, :408 · dl2:61-63, :208 |
| 4 | `raise` condition 1 is the working tree's file over the old value (dl2 §4) | cite | AGREES | cl4:267-270, :366-371 · dl2:209-215 |
| 4 | "The command's own guard (TOOL-dDeclaredLoop-2 S1) is untouched" | cite | AGREES | cl4:279-280 · dl2:44-50 |
| 4 | `tools/loop/kit.toml` and `gate-legs.json` get rows; the at-base facts about `tools/policy/guard.py:141` and `check_raise_shape` | RB | AGREES | cl4:97, :257-258, :415-417 · dl2:102 and Files touched (dl2:310-329) add rows, and dl2 wraps `tools/policy/guard.py` without editing it |

##### 2. The MISMATCHes

- **cl16: scenario taken as a single tag.** cl16:65-67 says "The scenario is the `scenario` field of the newest transition record", and AC3 expects `scenario.feature`. dl27:80-83 says "every transition record into a step carries ` · scenario=<tag>+<tag>…`, the placed scenarios in declared order joined by `+`". `Change:` S4 has to say whether a joined value is one tuple key or counts once per member, and AC3 and AC12 need a plant with two placed scenarios. `Cause:` pre-existing.
- **cl16: rework-budget residual and AC7.** cl16:149 says "`max(0, spent - per_unit * units)`", and AC7 (:298-299) says "30 closed builds of one unit each under `flow.rework-budget = "4+2"`, their spent draws 3 to 32". dl30:49-50 says "Once spent equals total the budget is spent, and the next draw writes nothing and returns `exhausted`". The total is the base plus the per-unit share (dl30:39-41), so one unit under `4+2` caps spent at 6. AC7's rows cannot occur, and real residuals never exceed the base, so the p90 can never propose a raise. `Change:` count the `exhausted` refusals as evidence too (dl31's ending or the cl16 F1 `budget-spent` line), or say the estimate is censored at the current base. AC7 then needs planted rows within the total. `Cause:` pre-existing.
- **cl16: route-backs evidence counts the wrong draws.** cl16:150 says "the most `route-back` draws one item took". dl30:62-63 says "`count_returns(build, item)` counts the draws naming the item; past `flow.route-backs` that item's loop ends `non-converging`". That covers every cause, not only `route-back`. `Change:` the evidence row is the most draws of any cause naming one item, which is what `count_returns` reads. `Cause:` pre-existing.
- **cl16: "ran under the value" read at the wrong commit.** cl16:88-91 keeps a build "only when `policy.py get <key> --rev <the commit of its newest transition record>` equals the key's value at `HEAD`". dl30:37-41 says "At the transition `designing` to `building`, `freeze_budget(build)` appends the row `budget · frozen · <units> unit(s) · <total>` … once". The budget a build ran under is fixed at the freeze. `Change:` for `flow.rework-budget`, read `--rev` at the commit that wrote the freeze row, or compare the frozen total with the value at HEAD. `Cause:` pre-existing.
- **cl16: evidence frozen at close, but patch draws arrive later.** cl16:229-231 says "The kept population is every CLOSED build that no earlier `loop-review` record's `bound-evidence` lines name". dl30:67-71 says "the row is appended to the originating build's transition record even when that build is terminal". A patch draw after close never reaches the kept row. `Change:` the committed keys (`flow.*`) are re-read from transition records at derivation time and only node-local keys are kept in the record; otherwise S7 must name dl30 S7 and say why late draws are dropped. `Cause:` pre-existing.
- **cl2: the item row is missing required keys.** cl2:112-118 gives the row only `step`, `actor = "command:loop.price"`, `needs`, `outcomes`, `routes`, `returns` and `owner`. dl12:127-130 says "`inputs` | yes for a non-role actor", "`allowance`, `returns` | yes for a non-role actor", "`witness` | yes". dl9:31-34 adds "`inputs`, `allowance` and `returns` present after defaults; `witness` present". dl9 is order 7, so it lands before this build. `Change:` S9's row needs `inputs`, `allowance` and `witness` (and cl3's re-point keeps them), or AC8's "refuses no row" reds. `Cause:` pre-existing.
- **cl2: the ask it relies on is filed nowhere.** cl2:324-325 says "AC8's `loop_lib.py --check` passing them is a build-run precondition on the ask F5 states". That ask is cl3:530, "a new ask the main loop files · dDeclaredLoop · THE LOOP KIT REFUSES A CADENCE STEP VALUE". `memory/builds/dDeclaredLoop/BACKLOG.md` holds no such row (grep for `CADENCE`: 0 hits). `Change:` file the dDeclaredLoop BACKLOG row before cl2's build run, or mark AC8 as blocked on an unfiled ask. `Cause:` pre-existing.
- **cl2, cl4: the leg is claimed in a new dossier.** cl2:319-320 says "claimed … by the feature dossier `memory/map/features/loop-review.md` (new when no dossier claims `tools/loop/`)", and cl4:244-245 inherits it. dl1:85 says "The kit's dossier `memory/map/features/loop.md`, claiming kit `loop` and its leg", and dl3:237 says "`memory/map/features/loop.md`: the module's claim and the leg in its `gate-legs` list". dl1 is a precondition, so the condition is never true, yet Files touched still names `loop-review.md`. `Change:` claim `loop-review selftest` and `loop measure fixtures` in dl1 S7's `loop.md`, as every dl unit does, or name dl1 S7 and say why a second dossier is wanted. `Cause:` pre-existing.
- **cl2: `value-ledger` cannot join `TYPED_RECORD_KINDS` as written.** cl2:280-281 says "`value-ledger` joins `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py`", with the snapshot at `memory/loop-review/<date>-value-ledger-<key>.md`. tr1:75-76 calls that tuple "the factory's kind list (PLAY-dOrderedCharter-42 S2)", and tr1:223 says "a `-<kind>-<n>.md` record is graded once, by its factory row". dOC42:40-44 says the factory's table "is refused at import … when its keys differ from that tuple", and dOC42:46-49 says "a record whose Serves kind is a typed kind and whose file is not so named is malformed". `Change:` either add a `build_records.py` kind row and move the snapshot into the `build/<…>-value-ledger-<n>.md` form, or bind the Serves kind some other way that names tr1 S2 and dOC-42 S2-S3. The same applies to cl3 and cl5 (`loop-review`, `keep`). `Cause:` pre-existing.
- **cl2: no unit removes `unarmed`.** cl2:306 says "`unarmed = "no snapshot is tracked until loop_review.py record lands the first period"`". tr42:43-45 says the check "reds the row, naming the key, once its home matches a file". No dCalibratedLens spec removes the key (grep for removing or dropping `unarmed`: no hit), so the first landed snapshot reds `record-kinds`. `Change:` the commit that lands the first snapshot (cl3's record step) drops `unarmed` from the row in the same commit, and an AC checks it. `Cause:` pre-existing.
- **cl19: the plant cannot exit 0.** cl19:48-51 says the plant "commits them, and runs … `record_kinds.py --check` … The check exits 0". tr42:43-45 says it "reds the row, naming the key, once its home matches a file". At order 3 the real rows carry `unarmed` (cl2:306, cl3:327), so the scratch worktree's check reds both rows. `Change:` the plant removes `unarmed` from the scratch rows before committing, naming tr42 S2, or AC2 expects the two `unarmed` reds and asserts only the per-record grading. `Cause:` pre-existing.

##### 3. UNKNOWN UNTIL BUILT

- **cl16 S4 and S8, transition time and commit:** dl3 S7 does not say whether `read_transitions` returns the transition commit or its time; it only promises records newest first with the `Sha` field set to the witness commit. dDeclaredLoop-3's build run decides.
- **cl16 and cl4, the proposal's apply command:** dl2 says `propose` prints "the command that would apply it", but not whether that is `set … --unit <id>` or `raise`, nor how a `budgets."AGENTS.md"` key is spelled. dDeclaredLoop-2's build run decides.

##### 4. Ancestor text that looks wrong

- dl3:69-71 names TOOL-dDeclaredLoop-30 as a `read_transitions` reader, but dl30:46-47 reads its rows "through the record factory's reader (`tools/memory-tree/build_records.py`)".
- dl1:85-87 and dl2:102 put their legs straight "in `tools/gate-legs.json`". tr1:78-82 and tr9:97-102 instead render the manifest through `leg_factory.py --write`, where a manifest-only edit reds `--check`.

## Group E, led by spec 1 (specs 1, 35, 3, 20 and 42)

Handoff: [`2026-11-03-prompt-TOOL-dCalibratedLens-1-4-spec-reviewer`](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-4-spec-reviewer.md).

Group E (specs 1, 35, 3, 20, 42), read against dTotalRecall and dDeclaredLoop as they stand at `0d1c1dda4`. I wrote nothing: every probe was a read, `git diff`, `git show` or `grep`.

Tally: 15 MISMATCH rows (11 bullets in 2, because rows that share one fact share one bullet), 3 UNKNOWN UNTIL BUILT, and the rest AGREES. Every MISMATCH is `pre-existing`. The two commits that moved ancestor text (`66f7b8d32` for tr2, `58b395b6e` for tr2 and tr1 rev-5) touch no assumption these five specs make. tr1 rev-5 only changes the `hand` writer, and the one registry row here (cl3:255) uses a command as its writer.

One correction to the brief. cl3 §8 F2's ask is filed on dWellOiledMachine (cl3:499-509), not on either of these builds. cl3's ask on dDeclaredLoop is §8 F5 (cl3:521-534), and the ask rows check F5.

#### 1. Assumptions

| Spec | Assumption about the ancestor | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | `--trigger` is dl20 S2's verb in `unattended.sh`: `--trigger <slug> --subject <s> --cause <c>`, takes no `--stage`, passes opt-in and unclassed to `review_pin.py`, prints that line with `trigger` and `blocks` added. cl1 adds `--stage` and `efforts` | cite | AGREES | cl1:83-86, :206-208, :410 · dl20:51-57, :137-144 |
| 1 | The key set the `--trigger` line prints is `{"preset","optIn","trigger","blocks","efforts"}` | cite | MISMATCH | cl1:209 · dl20:281 |
| 1 | dl19 S6 has a "firing site" that passes the step segment of the breakpoint's `position` tag, written `item.<step>.<name>`, as `--stage` | cite | MISMATCH | cl1:87-88, :205 · dl19:64-65, :100-101, :140-146 |
| 1 | A Maintain review runs where `review.breakpoints` (dl19 S4) places a breakpoint at an `item.maintain.*` boundary; "dDeclaredLoop places a review breakpoint for each stage" | cite | MISMATCH | cl1:40, :104-106, :434-435 · dl19:54-57 · dl1:57 · `grep -rn "item\.maintain" memory/builds/dDeclaredLoop/spec/` printed nothing · tc1:58-60 |
| 1 | `derive_breakpoints` reads `review.<stage>` for five stages and never `review.maintain` | cite | AGREES | cl1:107, :433-434, :442-443 · dl19:43-45, :126 |
| 1 | `review.<stage>` defaults to `opt-in`, so no stage lens fires until the stage opts in or is owed | cite | AGREES | cl1:113-114 · dl19:44-45, :148-150 |
| 1 | §8 F4's ask "DERIVE_BREAKPOINTS READS NO REVIEW.MAINTAIN" is to be served by dDeclaredLoop | ask | MISMATCH | cl1:128, :440-445 · `memory/builds/dDeclaredLoop/BACKLOG.md:5-13` holds asks 35 and 101-108; `grep -n -i maintain` there printed nothing. dl19 neither serves nor refuses it |
| 1 | AC9's fixture is "the `--trigger` fixture TOOL-dDeclaredLoop-20 lands in the unattended kit's suite" | cite | UNKNOWN UNTIL BUILT | cl1:390-391 · dl20:332-335 |
| 1 | Files touched vs dl19/dl20 §2. Shared files: `unattended.sh`, `unattended.test.sh`, `VERBS.template.md`, `tier2-review.template.js`, `tier2-review.test.sh`, `tools/workflows/README.md`. cl1's facts about the template at base are line regions (`:260-277`, `:356-360`, `:781-849`); dl20 S3 edits only `renderShapeLine` (`:78-83`) and adds arguments | RB | AGREES | cl1:141-142, :340 · dl20:58-61 · dl19:209-218 |
| 3 | dl12 supplies the `[[item]]` rows, `check_program`, `order_by_needs` with its inline `needs_graph_py` block, and `read_items(kit_dir, step=…)` | cite | AGREES | cl3:54, :319, :563 · dl12:36-37, :40-46, :48-53 |
| 3 | The four `item.loop.*` rows are "in TOOL-dDeclaredLoop-12's data model" as §4 "The items" lists them: actor, needs, outcomes and routes, witness | cite | MISMATCH | cl3:59-60, :209-217 · dl12:127-128 · dl50:35-36 |
| 3 | dl50 S3 admits only `step = "none"`, and only on `item.review.*` rows | cite | AGREES | cl3:524-525 · dl50 S3 (`check_program` admits `none` for those rows alone) |
| 3 | §8 F5's ask "THE LOOP KIT REFUSES A CADENCE STEP VALUE" is to be served by dDeclaredLoop (named again at :325) | ask | MISMATCH | cl3:325, :530-534 · `memory/builds/dDeclaredLoop/BACKLOG.md:5-13`; `grep -n -i cadence` printed nothing. dl12:108 and dl50 S3 refuse the value today |
| 3 | `item.loop.record` routes `recorded → transition` | cite | UNKNOWN UNTIL BUILT | cl3:217 · dl12:42 |
| 3 | tr1's registry: column order, `tag = record.<name>`, `writer` is a door command, `check` names the `record-kinds` leg. tr1 rev-5's `hand` change does not reach this row | cite | AGREES | cl3:55, :247-258, :567 · tr1 S1, S3, §4 writer bullet |
| 3 | id 1: `home` is the id-rule's glob "as TOOL-dTotalRecall-42 S1 spells the shape-run home" | cite | AGREES | cl3:285-287 · tr42:41-43 |
| 3 | id 37: the row carries `unarmed = "no record is tracked until the first period's record lands"`, and the record lands later through a patch build (S8) | cite | MISMATCH | cl3:327, S8 · tr42:40-44 |
| 3 | id 36: `loop-review` joins `TYPED_RECORD_KINDS` and HYGIENE's closed `<kind>` list | cite | MISMATCH | cl3:288-290 · tr11:53-57 · `PLAY-dOrderedCharter-42:40-44` |
| 3 | Files touched vs dl12, tr1, tr42 §2 (`loop.toml`, `record-kinds.toml`, `HYGIENE.template.md`, `memory/HYGIENE.md`): no fact about these files at base is stated that those units' scopes change | RB | AGREES | cl3 Files touched · dl12, tr1, tr42 Files touched |
| 20 | `derive_record_kind` reads the kind from the record's own Serves line and returns None when there is none; the edge reads "the kind read from a record's Serves line" | cite | MISMATCH | cl20:23-25, :48, :74, :86, :113 · tr53:94-96 · `tools/memory-tree/tree_lib.py:421-425` |
| 20 | The hands-off ask "THE RECORD-KIND CHECK READS NO SERVES LINE OUTSIDE THE BUILD FOLDERS" is filed only if AC2 goes red at the build run | ask | MISMATCH | cl20:75 · `memory/builds/dTotalRecall/BACKLOG.md:5-19` has no such row · tr53:94-96 already decides the case |
| 20 | Each kind joins `TYPED_RECORD_KINDS` and HYGIENE's list "as TOOL-dTotalRecall-11 S3 joins `shape-run`" | cite | MISMATCH | cl20:36-41, :175-176 · tr11:53-57 · `PLAY-dOrderedCharter-42:40-44` |
| 20 | `TYPED_RECORD_KINDS` is the concatenation of PLAY-dOrderedCharter-42 S1 and tr18 S7; `canonical_kind` returns a row name unchanged | cite | AGREES | cl20:84-85, :94 · tr18:76-81 |
| 20 | A gap that "TOOL-dTotalRecall-42 §4 'The kind decides'" names | cite | MISMATCH | cl20:58 · tr42:53, :84, :97 |
| 20 | AC2: `record_kinds.py --check` in a scratch worktree holding committed records exits 0 over the whole records | cite | MISMATCH | cl20:140 · tr42:40-44 · cl3:327 · cl2:306 |
| 20 | AC2's fixture: `record_kinds.py` comes from tr1 and tr42 | cite | AGREES | cl20:143 · tr1 Inventory · tr42 Inventory |
| 20 | Facts about `tree_lib.py` at base (`record_paths`, `read_bindings` and its population) vs tr18 S7, which changes `read_bindings`. cl20 names tr18 S7, and S7 only adds alias acceptance, so the population fact holds | RB | AGREES | cl20:80-85 · tr18:76-82 |
| 35 | `derive_record_kind(path, written_kind, rows)`, citing tr42 S5 `:53-58` and tr53 S21 `:94-96` | cite | AGREES | cl35:37-41, :61, :71-76 · tr42:53-58 · tr53:94-96 |
| 35 | tr42's check prints only the unarmed kinds and the mismatch count | cite | AGREES | cl35:95-96 · tr42:140 |
| 42 | The S21 signature is `(path, written_kind, rows)` with no Serves line parsed inside | cite | AGREES | cl42:1, :23-24, :66, :72-80 · tr53:94-96, AC21 |
| 42 | S2 reads the written kind through `BIND_RE` itself rather than through `read_bindings`, and calls this "the form TOOL-dTotalRecall-53 S21 gives it" | cite | MISMATCH | cl42:1, :39-46 · tr53:94-96 |
| 42 | Facts about `tree_lib.py` at base (`BIND_RE :401`, `BIND_HEAD_LINES :410`, `unfenced :515-532`, `record_paths :421-425`) vs tr53 §2, which edits `tree_lib.py` only for `read_header_edges` (S17) | RB | AGREES | cl42:40-44 · tr53 Files touched, S17 |

#### 2. MISMATCH

- **cl1:209 vs dl20:281.** cl1: "prints {"preset", "optIn", "trigger", "blocks", "efforts"}". dl20 AC2: "one JSON line carrying `preset`, `optIn`, `unclassed`, `"trigger": "owed"` and `"blocks": "yes"`".
  Change: add `unclassed` to the key set in §4 "The stage path", so a builder keeps the field dl20 prints.
  Cause: pre-existing.

- **cl1:87-88, :205 vs dl19:100-101, :140-146.** cl1: "TOOL-dDeclaredLoop-19 S6's firing site passes the step segment of the breakpoint's `position` tag (`item.<step>.<name>`) as `--stage`". dl19: "this unit lists and holds; a placed review breakpoint fires through `--trigger`". dl19's positions are relational ("before `item.plan.exit`", "after `item.design.reason`, before `item.design.ready`"), and dl19 builds no call site for `--trigger`.
  Change: name the unit or caller that actually calls `--trigger` at a placed breakpoint (for example the main loop reading `--plan`'s `breakpoint:` lines), and add that caller to Files touched. Take the stage from the position's step segment, whatever relational form `derive_breakpoints` gives it.
  Cause: pre-existing.

- **cl1:40, :104-106 vs dl19:56-57, dl1:57.** cl1: "A Maintain review runs where `review.breakpoints` places one at an `item.maintain.*` boundary (TOOL-dDeclaredLoop-19 S4)". dl19 S4: "a tag the loop definition does not declare is refused naming `review.breakpoints` and the tag". dl1 S2: "five `[[step]]` rows, `step.plan` … `step.deploy`". No dDeclaredLoop spec declares an `item.maintain.*` row; tc1:58-60 does (`item.maintain.lease` … `item.maintain.record`).
  Change: name TOOL-dTendedCadence-1 S1's `item.maintain.*` rows as the boundary, add it to the build-run preconditions and to "Waits on", and soften §1's "for each stage" to the five stages dl19 reads.
  Cause: pre-existing.

- **cl1 §8 F4 (:440-445), cl3 §8 F5 (:530-534): ask not filed.** Each says "The main loop files the ask in `memory/builds/dDeclaredLoop/BACKLOG.md`" (cl1) or "a new ask the main loop files · dDeclaredLoop" (cl3). That BACKLOG holds only TOOL-dDeclaredLoop-35 and -101 to -108, and none names `review.maintain` or `cadence.loop`. dl12:108 (`step = "step.plan"`) and dl50 S3 (`none` "for those rows alone") refuse cl3's value today.
  Change: file both rows before either spec is built, or mark each as a build-run precondition that names the missing ask. cl3's ask gates unit 2's AC8 and cl3 S2.
  Cause: pre-existing.

- **cl3:59-60, :209-217 vs dl12:127-128, dl50:35-36.** cl3: rows "in TOOL-dDeclaredLoop-12's data model", with actors such as `command:loop.gather`, and the table gives only actor, needs, outcomes and routes, and witness. dl12: "`inputs` | yes for a non-role actor", "`allowance`, `returns` | yes for a non-role actor". dl50 likewise: "with `inputs`, `allowance` and `returns` a non-role actor requires".
  Change: give each `item.loop.*` row its `inputs` (layer tag and what it reads), `allowance` and `returns` in §4 "The items", or state which role actor supplies them.
  Cause: pre-existing.

- **cl3:327 (id 37) and cl20:140 (AC2) vs tr42:40-44.** cl3: `unarmed = "no record is tracked until the first period's record lands"`. cl20 AC2: "the check exits 0 over the whole records" in a scratch worktree where the plant commits a record. tr42 S2: `unarmed = "<reason naming the writer that will arm it>"`, and the check "reds the row, naming the key, once its home matches a file". So cl20's exit-0 run goes red on the `unarmed` key on a correct build. The patch build that lands cl3's first record also reds `record-kinds`, and no unit removes the key.
  Change: cl3's reason should name `loop_review.py record`, and S8's patch build should drop the key in the commit that lands the first record. cl20 S2 should strip `unarmed` from the scratch registry, or expect that red and name it.
  Cause: pre-existing.

- **cl3:288-290 (id 36) and cl20:36-41 vs tr11:53-57, PLAY-dOrderedCharter-42:40-44.** cl20: "each kind joins `TYPED_RECORD_KINDS` … and the closed `<kind>` list …, as TOOL-dTotalRecall-11 S3 joins `shape-run`". tr11 S3: "`shape-run` joins `TYPED_RECORD_KINDS`, the factory's per-kind table gains its fields … the three lists PLAY-dOrderedCharter-42 S2 and S5 keep one, all joined in this pass". dOC-42 S2: the factory's "per-kind table … is refused at import, naming the kind, when its keys differ from that tuple".
  Change: either add each kind to `build_records.py`'s per-kind table (and to Files touched), accepting dOC-42 S3/S4's typed-kind naming, or bind the three kinds through the untyped part of `RECORD_KIND_TOKENS` (tr18 S7) instead of `TYPED_RECORD_KINDS`.
  Cause: pre-existing.

- **cl20:23-25, :74, :113 vs tr53:94-96.** cl20: "`derive_record_kind` returns the row named by `canonical_kind(<the record's Serves kind>)` and None for a record with no Serves line"; edge: "the kind read from a record's Serves line". tr53 S21: "callers pass the kind `tree_lib.read_bindings` … classified, read once, and no Serves line is parsed inside the function". `read_bindings` reads only build folders (`tree_lib.py:421-425`), so every `memory/loop-review/` record is graded by no row. AC2's cut runs then exit 0, and S3's plant fails on a correct build.
  Change: re-ground §1, §3 Edges and §4 on tr53 S21. Turn the conditional hands-off at :75 into an ask filed now and a build-run precondition, since the ancestor text already decides the "when".
  Cause: pre-existing.

- **cl20:75: the contingent ask.** cl20: "when the landed `check_record_kinds` takes a record's kind only from `read_bindings` … the main loop files this ask on dTotalRecall". `memory/builds/dTotalRecall/BACKLOG.md` (asks 27-35, 101-106) has no row for it, and tr53 S21 already says callers take the kind from `read_bindings`.
  Change: file "THE RECORD-KIND CHECK READS NO SERVES LINE OUTSIDE THE BUILD FOLDERS" on dTotalRecall now, and list it among AC2's preconditions.
  Cause: pre-existing.

- **cl20:58 vs tr42:53, :84-97.** cl20: "a gap TOOL-dTotalRecall-42 §4 "The kind decides" names". tr42's §4 sections are "The row, after this unit", "The grading rule", "Inventory" and so on. "The kind decides, the home admits" is the title of S5 in §2 (tr42:53).
  Change: cite "TOOL-dTotalRecall-42 S5" or §4 "The grading rule".
  Cause: pre-existing.

- **cl42:1, :39-46 vs tr53:94-96.** cl42: the case calls `derive_record_kind` "in the form dTotalRecall's unit 53 gives it at its S21", while S2 reads the kind with `BIND_RE` and "does not call `read_bindings`". tr53 S21: "callers pass the kind `tree_lib.read_bindings` … classified". So the case reports records "graded by a row" that the shipped `check_record_kinds` never grades.
  Change: state the departure from S21's caller rule and that the case proves only the row lookup. Name cl20's dTotalRecall ask as what makes the real check grade these records.
  Cause: pre-existing.

#### 3. UNKNOWN UNTIL BUILT

- **cl1:390-391, AC9's fixture.** dl20:332-335 declares the `unattended.test.sh` arm but waives the unattended kit's suites for its landing. dl20's build run decides whether the `--trigger` fixture actually lands in that suite.
- **cl1:205, the position's literal form.** dl19 S1/S9 print `position` without fixing whether it reads `item.plan.exit` or `before item.plan.exit`. dl19's build run decides this, and with it how the step segment is parsed.
- **cl3:217, the `transition` route.** dl12:42 defines `transition` as "a cross-step move, read by the transition table", and a cadence program belongs to no step. The grading the cl3 F5 ask lands in `check_program`, or dl13's transition-table join, decides whether `recorded → transition` is legal.

#### 4. Ancestor text that looks wrong

- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-20.md:143` calls `python review_pin.py <subject paths> --opt-in …` with positional subjects. dFairHearing's `review_pin.py`, as cl1 AC4 calls it, takes `--subject`; one of the two grammars is off.
- `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-19.md:43-45` reads five `review.<stage>` keys while v2:1656 lists `review.maintain` (cited at cl1:151), and no unit in the build owns that sixth key.
- `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-53.md:94-96` routes every `derive_record_kind` caller through `read_bindings`, whose population is the build folders. No registry row with a home outside `memory/builds/` can then be graded by tr1 S4's field check.

Files read:
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-1.md`
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-3.md`
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-20.md`
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-35.md`
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dCalibratedLens/spec/2026-11-03-spec-TOOL-dCalibratedLens-42.md`
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dDeclaredLoop/spec/` (units 1, 12, 19, 20, 50)
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dTotalRecall/spec/` (units 1, 11, 18, 42, 43, 53)
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dDeclaredLoop/BACKLOG.md`
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/memory/builds/dTotalRecall/BACKLOG.md`
- `C:/projects/coding-governance/.claude/worktrees/musing-colden-d318c6/tools/memory-tree/tree_lib.py`
