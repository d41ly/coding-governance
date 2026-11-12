# PLAY-dOrderedCharter-87 — the adopter-rules step types each rule `adopter-rule`, a level-0 repository statement type the grammar admits as written

**Status:** DEFERRED · rev-1 · 2026-11-12 · node a · Tier-2 · base 3aa7da3d6 · streams tooling · order 48 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-PLAY-dOrderedCharter-87-1-spec-writer.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-87-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-87-build-brief.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-87-build-brief.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-87-spec-brief.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-87-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's bar over the prepared merge `c7d7f75f1` red the `instruction edits (manifest checks)`
leg with 18 findings. The upgrade step `playbook/adopter-rules-to-overlay` had written gov's nine
adopter rules into the overlay as directives, and a directive must open with a modal and carry a
trigger. None of the nine does. This unit gives the grammar a seventh statement type,
`adopter-rule`, for an adopter's own rule carried as written, legal only on a level-0 `repo` unit.
The step writes that type and refuses any row the grammar still reds. The next `--prepare` then
writes an overlay the bar accepts, and the rendered rules stay byte-identical.

## 2. Scope (IN)

- **S1** — In `tools/playbook/instruction_units.py`, `STATEMENT_TYPES` gains the member
  `"adopter-rule"` as its seventh value. The unpacking line beneath it names it `ADOPTER_RULE`, and
  `TYPED_TYPES` gains `ADOPTER_RULE`. `check_statement` is not edited: an `adopter-rule` row reds
  only on empty text, through its existing `carries no text` branch. The module docstring's
  statement-grammar paragraph gains one sentence naming the type and its one legal place. Observed
  by AC1 and AC3.
- **S2** — `check_unit_row` reds an `adopter-rule` row whose namespace is not `repo` or whose level
  is not 0. The red names the field `type`, and its remedy lists the six other types. The check sits
  directly after the existing statement-type check. Observed by AC4.
- **S3** — In `tools/govkit/steps/adopter_rules_to_overlay.py`, `derive_rule_rows` takes a third
  parameter, `kind`, and writes it as each row's `type`. The `up` passes `ov.iu.ADOPTER_RULE`, so the
  type's spelling stays in one module. The docstring's THE ROWS paragraph reads
  `type = "adopter-rule"`. Observed by AC1, AC2 and AC5.
- **S4** — The step's `up` grades each converted row through `ov.iu.check_statement` before it
  writes anything. Any red refuses the `up` with exit 1 and nothing written, and the refusal names
  every red. Observed by AC6.
- **S5** — The fixture tables in `tools/playbook/instruction_units.py` gain two rows.
  `STATEMENT_ROWS` gains a well-formed `adopter-rule` row tagged `repo.rule-01-fx`. `SCHEMA_ROWS`
  gains a level-0 `adopter-rule` row tagged `unit.carried` in a kit manifest, whose red names
  `type`. Observed by AC3 and AC4.
- **S6** — `help/overlay.md` gains one paragraph under "Add a unit". It says what an `adopter-rule`
  unit is, that `update` writes it when it moves `[charter] adopter_rules`, that it needs no modal
  and no trigger, and that only a level-0 `repo.` unit may carry it. Observed by AC7.

## 3. Non-goals (OUT)

- Any change to the wording of an adopter rule, in `.governance/deploy.toml` or anywhere else.
- A new step id or a version on the step row. The row is unlanded (section 4, "Migration").
- An edit to `tools/govkit/entries/playbook.kit.toml`. The row's argv, witness and surfaces do not
  move.
- An edit to `check_statement`, to the directive's modal or trigger rule, or to the other five
  types' forms.
- The tutorial's sample unit, `help/tutorial/adopt-gov.md@7ae01625:53-54`. It is a level-0
  directive with no modal, so the same predicate reds it (PINNED, `check_statement` over that row at
  `3aa7da3d6`). It is not a row of this step, and it is handed off below.
- A version bump of the playbook or govkit kit. The lander mints kit versions into the prepared
  merge (`tools/push-main.sh@c7cd70b9:26-29`).
- `help/upgrade-steps.md`. Its paragraph on this step names no type, so it stays accurate.

### Edges

- **consumes-from** external — PLAY-dOrderedCharter-31's upgrade step
  `playbook/adopter-rules-to-overlay`, CLOSED, whose program this unit edits in place.
- **hands-off** external — the main loop re-runs `bash tools/push-main.sh --prepare` and the close
  after this unit lands on the run branch (section 7).
- **hands-off** external — the tutorial's sample unit reds the grammar the same way. A follow-up
  rewrites it with a modal or types it `adopter-rule`.

## 4. Design

### Evidence

Read at `3aa7da3d6`. A role agent's scratch guard refuses the leg's command, so each figure below
comes from the leg's own entry, `run_check` in `tools/playbook/instructions_edit.py`, called by a
probe. Every probe ran over scratch clones of `3aa7da3d6` that keep its history, with a local `main`
at `origin/main` and `origin/HEAD` set to `main`.

- The mismatch. The step writes each `- ` line of `[charter] adopter_rules` as one row with
  `type = "directive"`, the line as `text`, and no `trigger`
  (`tools/govkit/steps/adopter_rules_to_overlay.py@19bdde65:106-110`). The leg grades every overlay
  row through `check_unit_row` and `check_statement`
  (`tools/playbook/instructions_edit.py@57e11a29:516-519`). A directive reds when its text opens
  with no modal from `MODALS` and again when it carries no `trigger`
  (`tools/playbook/instruction_units.py@1ac380c7:786-790`).
- The reds reproduced (PINNED, the probe at `3aa7da3d6`). Before the step the leg reads 4 rows and
  reports `instructions-edit: check · 0 red`. After `adopter_rules_to_overlay.py up .` it reads 13
  rows and reports `instructions-edit: check · 18 red`, exit 1. All 18 lines open
  `instruction-units: red · repo.rule-`, two for each of `repo.rule-01-` to `repo.rule-09-`: one
  for the missing modal and one for the missing trigger.
- Why no earlier bar saw them. The step had never run on gov's tree before the lander's prepare.
  The receipt `.governance/install.json` records the step id 0 times at `3aa7da3d6` (PINNED,
  `grep -c`), and the prepared merge `c7d7f75f1` records it once. That merge is on no branch
  (PINNED, `git branch -a --contains`).
- Why the step wrote rows the leg reds. The step validates its rows through `read_overlay`
  (`tools/govkit/steps/adopter_rules_to_overlay.py@19bdde65:180-184`). That reader refuses what
  `check_unit_row` reds, and it never calls `check_statement`
  (`tools/playbook/overlay.py@4d7c5119:106-139`). The schema and the grammar are two arms, and the
  step consulted only one.
- No existing type fits the rules as written. Each of the nine holds a backticked span but no modal
  and no em dash, and none opens with a pointer trigger (PINNED, read from
  `.governance/deploy.toml@f611ca4a`). A `constraint` would pass on the backticked span with an
  `enforced-by` of `none — <why>`. The fixture plant's rule,
  `Name the upgrade-walk plant adopter-rules in every walk.`
  (`tools/govkit/fixtures/release-0/plants.toml@81431ed3:116-122`), holds no digit and no
  backticked span, so it fits none of the six. Under the base code the plant's row reds the same
  two directive rules (PINNED, the probe).
- Other adopters. The two adopters on this machine, in four checkouts with a
  `.governance/deploy.toml`, carry no `[charter] adopter_rules` key and no overlay (PINNED, read on
  2026-11-12). Adopters receive steps from `main`,
  and `main` (`47ed57fab`) has no such row, so no adopter has met the step.
- The render ignores the type. The project block renders `- ` plus `render_unit`'s line for each
  level-0 every-reader unit, in overlay order
  (`tools/playbook/render_playbook.py@ffeba50c:1389-1414`). `render_unit` returns the unit's `text`
  for every type except `policy-value` and `fact`
  (`tools/playbook/instruction_units.py@1ac380c7:479-486`). A unit with no `trigger` composes
  (`tools/playbook/overlay.py@4d7c5119:217-229`).

### The type (S1, S2)

`adopter-rule` is a statement type for an adopter's rule carried as written. It is a typed type: it
needs text, its pinned text joins the one-fact check, and `render_unit` renders its text. That is
the whole of what `TYPED_TYPES` decides (`tools/playbook/instruction_units.py@1ac380c7:939-940`,
`tools/playbook/instruction_units.py@1ac380c7:972-986`). `check_statement` grades its form like the
others' and finds no form to grade. The type adds no `elif` branch, so its only red there is the
shared `carries no text`.

S2 confines the type to the one place an as-written rule belongs: the project block, which renders
the level-0 `repo` units (`tools/playbook/render_playbook.py@ffeba50c:1398`). The added lines are:

```python
    if unit.type == ADOPTER_RULE and (ns != "repo" or unit.level != 0):
        add_red("type", f"{unit.type!r} types a level-0 `repo` unit only",
                f"type it one of {', '.join(t for t in STATEMENT_TYPES if t != ADOPTER_RULE)}")
```

`check_unit_row` already receives the namespace from each caller
(`tools/playbook/instructions_edit.py@57e11a29:517`). The overlay reader calls it with `repo`, and
the schema leg calls it with the default `unit`. So a kit unit typed `adopter-rule` reds the schema
leg, and an overlay unit at another level is refused by the overlay reader, which every render goes
through.

### The step (S3, S4)

```python
def derive_rule_rows(lines: list[str], fold, kind: str) -> list[dict]:
```

`kind` replaces the literal `"directive"`. In `cmd_up`'s `derive_after`, the call and the new
refusal read:

```python
        rows = derive_rule_rows(lines, tag_index.derive_heading_seg, ov.iu.ADOPTER_RULE)
        reds = [red for row in rows for red in ov.iu.check_statement(row)]
        if reds:
            raise Refusal("the converted rows break the instruction-unit grammar:\n" + "\n".join(reds))
```

The refusal runs inside `derive_after`. With no before-image, `write_before_image` calls
`derive_after(None)` before it writes the image (`tools/govkit/upgrade_steps.py@c812b44e:1121-1151`),
so a refusal there writes nothing, like the order and reader refusals beside it. S4 closes the gap
the evidence names. After S1 the one grammar red an `adopter-rule` row can take is
`carries no text`, and `check_unit_row` catches an empty text but not a whitespace-only one.
Measured over the pass: a key line `-   ` passes `check_unit_row` and reds `check_statement`. The
base step writes that row, exit 0, and the pass step refuses it, exit 1, with only the planted
`deploy.toml` edit in `git status` (PINNED, the probe). `check_statement` resolves pointer targets
only, so the call needs no resolver.

The step's `down` and `witness` are not edited. The `down` restores from the before-image, whatever
type the `up` wrote. The `witness` compares the before-image's lines with the level-0 units' texts,
and the texts do not move. Over the pass, `witness .` exits 0 after `up .`, and `down .` restores
both files, leaving `git status --porcelain` empty (PINNED, the probe).

### The rendered rules

Over the pass, after `up .` and a commit, `render_playbook.py --render-scope charter` exits 0 and
leaves `AGENTS.md` byte-identical: its blob is `30520e73945057365a62c810c7b97d355485e3b0` before and
after (PINNED, the probe). The lock moves only in line endings under the probe clone's
`core.autocrlf`, with 0 content lines in `git diff` (PINNED).

### What it does not check

- An adopter may type any level-0 `repo` unit `adopter-rule`, and its form is then not graded. This
  takes no coverage away. Before the step, the same rules sat in `[charter] adopter_rules`, which no
  leg grades as units: the leg read 4 rows there, none of them a rule (PINNED, the probe).
- The type does not prove that a rule gives direction, which is what P11 asks
  (`tools/playbook/principles.toml@701c20bb:69-71`). It records that the adopter wrote the rule, and
  the adopter's wording stands.
- S4 grades each row alone. Two rules with one text are the one-fact check's to red, as they were
  as directives.
- The upgrade walk's skip case runs the step over the fixture plant but grades no unit row. Under the
  pass the plant's row passes both checks (PINNED, the probe), and no walk observes that.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| the statement type `adopter-rule` and its constant `ADOPTER_RULE` | `tools/playbook/instruction_units.py` | no cell grades a py constant: `lexicon.py --suggest` reports the `py.constant` cell UNDECLARED |
| the parameter `kind` of `derive_rule_rows` | `tools/govkit/steps/adopter_rules_to_overlay.py` | a parameter, not a name the lexicon grades |
| the fixture tags `repo.rule-01-fx` and `unit.carried` | `tools/playbook/instruction_units.py` | no cell grades a fixture tag |

No function is minted.

### Migration

The step keeps its id and gains no version. Its `[[upgrade]]` row is unlanded: `main` at
`47ed57fab` holds neither the row nor the program (PINNED, `git show`). `step-rows-frozen` grades
only rows landed at the base, and says so (`tools/govkit/upgrade_steps.py@c812b44e:36-42`), so
editing the program is legal. The only tree the old program wrote is the prepared merge `c7d7f75f1`,
which is on no branch. The next `--prepare` merges afresh from the run branch and runs
`govkit.py update --target "$top" --write` over it (`tools/push-main.sh@c7cd70b9:1015`), so it runs
the new program.

A tree that had applied the old program would not converge by a second `up`. With the key gone,
that `up` prints `nothing to move` and leaves the directive rows in place. It converges by `down`
then `up`. Over a clone that applied the old program, the new `down` restored both files, and the
new `up` then wrote nine `adopter-rule` rows, with `instructions-edit: check · 0 red` (PINNED, the
probe). No such tree exists outside the discarded merge.

### Rollout

No switch. The type is additive to a closed set, and the only writer of it is the step, which no
landed release carries.

### Files touched (estimate)

- `tools/playbook/instruction_units.py` (S1, S2, S5)
- `tools/govkit/steps/adopter_rules_to_overlay.py` (S3, S4)
- `help/overlay.md` (S6)

### Alternatives rejected

- **Exempting `repo.rule-` directives from the modal and trigger rules.** The exemption keys on a tag
  shape any author can type, and it keeps calling a row a directive when its text gives no modal.
- **Typing each rule `constraint` with `enforced-by = "none — <why>"`.** It passes gov's nine only
  because each holds a backticked span. The fixture plant's rule fits no type, and a constraint names
  a bound, which these rules do not.
- **Prefixing each rule with a modal.** It changes what the rules say and the rendered bytes. The
  brief rules it out.

## 5. Production-readiness checklist

- security — Deny by default. The type is refused everywhere except a level-0 `repo` unit, so gov's
  kit units keep the full grammar. The step gains a refusal and no new write.
- perf / scale — One `check_statement` call per converted rule, once per `up`.
- error / empty / loading states — A rule whose text is whitespace now refuses the `up` with exit 1,
  naming the row, and nothing is written. A key with no lines still converts nothing.
- observability — The refusal prints every grammar red it found.
- risks — The probes ran on scratch clones, not on the lander. The main loop's `--prepare` is the
  observation over the real walk (section 7).
- testing — AC1, AC2, AC5 and AC6 are direct probes of the step over a throwaway clone. AC3 and AC4
  are the module's own fixture plants, and section 7 declares the suite arm.
- migration — No data migration. The step's id stays, and section 4, "Migration", says why.
- user docs — `help/overlay.md` names the type (S6).

## 6. Acceptance criteria

The commands of AC1, AC2, AC5 and AC6 run in a throwaway clone of the pass's tip. The clone keeps
its history, has a local `main` at `origin/main`, and has `origin/HEAD` set by
`git remote set-head origin main`. No one runs them in the run's worktree.

- **AC1** — When `python tools/govkit/steps/adopter_rules_to_overlay.py up .` runs in the clone and
  then `python tools/playbook/instructions_edit.py check` runs there, the check exits 0, prints no
  line opening `instruction-units: red`, and ends `instructions-edit: check · 13 row(s)` then
  `instructions-edit: check · 0 red`.
  Red when: the step still types each rule a directive, so the check exits 1 with 18 reds naming
  `repo.rule-`, as at the base.
  figure: PINNED, the leg's own `run_check` over clones at `3aa7da3d6` and over the pass.
  permission: the main loop runs the check; a role agent's scratch guard refuses this leg's command.
- **AC2** — When the clone commits the output of AC1's `up` and then
  `python tools/playbook/render_playbook.py --render-scope charter` runs, it exits 0, its notes
  include `units     ADOPTER_RULES — no [charter] adopter_rules · 9 level-0 unit(s) after it`, and
  `git diff --exit-code -- AGENTS.md` exits 0.
  Red when: the project block renders an `adopter-rule` unit other than as its text, or the overlay
  reader refuses the type at level 0.
  figure: PINNED, the probe over the pass at `3aa7da3d6`.
- **AC3** — When `python tools/playbook/instruction_units.py fixture --plant statements` runs after
  the build, it exits 0 and prints
  `instruction-units:   ok · a well-formed adopter-rule (repo.rule-01-fx) passes` and
  `instruction-units: fixture · green · 0 expectation(s) failed`.
  Red when: `adopter-rule` is not a member of `STATEMENT_TYPES`, so the row reds as no statement
  type.
- **AC4** — When `python tools/playbook/instruction_units.py fixture --plant schema` runs after the
  build, it exits 0, prints an `ok` line holding `unit.carried reds naming the manifest`, and prints
  `instruction-units: fixture · green · 0 expectation(s) failed`.
  Red when: S2's check is absent, so a kit unit typed `adopter-rule` passes the schema and the line
  reads `FAILED`.
  figure: PINNED, the plant over the pass with S2's lines removed at `3aa7da3d6`.
- **AC5** — When `python tools/govkit/steps/adopter_rules_to_overlay.py witness .` runs in a fresh
  clone after `up .`, it exits 0 and prints
  `adopter-rules: witness · no [charter] adopter_rules, and each of its 9 rule(s) is a unit: applied`.
  When `python tools/govkit/steps/adopter_rules_to_overlay.py down .` then runs, it prints a line
  opening `adopter-rules: down · restored` that names the descriptor and the overlay, and
  `git status --porcelain` prints nothing.
  Red when: the new type breaks the witness's text match or the down's restore.
- **AC6** — When a fresh clone's `[charter] adopter_rules` gains the line `-   ` and
  `python tools/govkit/steps/adopter_rules_to_overlay.py up .` runs, it exits 1, prints
  `adopter-rules: up refused · the converted rows break the instruction-unit grammar:` with a line
  naming `carries no text`, and `git status --porcelain` lists only the edited deploy file.
  Red when: the step writes a row the grammar reds, as the base step does with exit 0.
  figure: PINNED, the probe over the pass and over `3aa7da3d6`.
- **AC7** — When `git grep -n -e "adopter-rule" -- help/overlay.md` runs after the build, it prints
  at least one line, inside the "Add a unit" section.
  Red when: the overlay page does not name the type an adopter now finds in the overlay.

## 7. Gates

`instruction edits (manifest checks)` · `instruction units selftest` · `instruction units (schema, one fact)` · `instruction grammar (statement types, provenance lock)` · `instruction render (one renderer of record)` · `upgrade-walk` · `step-rows-frozen` · `docs` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `spec tokens (a spec's own names resolve)`

The guarded legs the three estimated paths trip are `govkit acceptance matrix`,
`playbook render selftest`, `policy fixtures`, `recall floor arms`, `govkit selftest` and
`govkit refusal join` (DERIVED, the spec-token checker's `--legs-for` over the estimate at
`3aa7da3d6`; `help/overlay.md` trips none). The rest carry no guard and run on every change.
`instruction edits (manifest checks)` is the leg that red. The four `instruction` legs grade the
type set and its readers. `upgrade-walk` and `step-rows-frozen` grade the step and its row, and
`docs` grades the help page.

After this unit lands on the run branch, the main loop re-runs
`bash tools/push-main.sh --prepare --slug dOrderedCharter` and then the close's bar over the new
prepared merge. That bar is where AC1's leg first reads gov's own walked overlay.

New arm: tools/playbook/instruction_units.py · covers AC3 AC4 · with S2's three lines removed the `schema` plant's `unit.carried` row passes the schema and the plant prints FAILED · none

## 8. Open questions

- **F1 — Where does the fix live: in the step, in the grammar, or both?** The step alone cannot pass
  a directive without changing a rule's text. The grammar alone cannot tell an adopter's rule from a
  malformed directive.
  - (a) Both. A seventh statement type, `adopter-rule`, legal only on a level-0 `repo` unit, which
    the step writes and grades before it writes. The text and the render stay as they are. This is
    the recommendation.
  - (b) The grammar alone. `check_statement` exempts `repo.rule-` directives from the modal and
    trigger rules. That is one line, but it keys on a tag shape, and the row's type would misstate
    its text.
  - (c) The step alone. Each rule is typed `constraint` with `enforced-by = "none — <why>"`. Gov's
    nine pass, the fixture plant's rule fits no type, and the row misstates what it is.

  RESOLVED (agent, 2026-11-12, delegated): (a), under the owner's standing ruling of 2026-11-10 to
  take each fork's recommendation.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft, from
  `2026-11-12-prompt-PLAY-dOrderedCharter-87-1-spec-writer.md`. The 18 reds were reproduced on a
  scratch clone of `3aa7da3d6` through the leg's own `run_check`. F1 was resolved to the grammar and
  the step together, under the owner's standing ruling.

## 10. Reuse audit

This unit extends existing seams and adds no mechanism. The type joins the one closed set,
`STATEMENT_TYPES` (`tools/playbook/instruction_units.py@1ac380c7:158-160`). Its restriction joins
the one row check, `check_unit_row` (`tools/playbook/instruction_units.py@1ac380c7:914-953`), which
the overlay reader already applies to every overlay row. The step reuses `check_statement` as its
grammar check, rather than a copy. `tools/codebase-map/reuse_lookup.py` ranked `parse_unit_rows`,
`check_unit_row`, `read_units` and `render_row` among the playbook seams, and the grammar seams of
other kits, `id_grammar.py` and `corpus_ids.py`, which grade record ids and not unit rows. No other
seam fits.

Recall terms used: `reuse_lookup.py "a unit row statement type an adopter rule carried as written passes the instruction grammar"`
