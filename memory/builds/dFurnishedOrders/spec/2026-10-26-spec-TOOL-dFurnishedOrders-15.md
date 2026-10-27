# TOOL-dFurnishedOrders-15 — the tester re-founded with its allowance, and the `probe` outcome on every role's return template

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 2193e25d · streams tooling · order 3 · advances TOOL-dFurnishedOrders-21

**Carries:** cl-dClosedLoop-0206@e18404dd whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-c.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-reuse-scout-c.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-16 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-fix-return.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 |
| [2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-1-spec-stage-returns.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-1-spec-fix-brief.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-14 |
| [2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-16 |

<!-- /gen:spec-records -->

## 1. Goal

No role may run an experiment that writes, and the tester dWitnessedBar ships plays only the Test
step's judgments (gap-roles-21). This unit re-founds `gov-tester` from TOOL-dWitnessedBar-23's minimal
one (WK-1): it plays its four items, `test.attribute`, `test.reason`, `probe.design` and
`probe.judge-claimed` (layer-roles.md:409), writes experiments under its scratch path, and uses a
browser where the harness has one. And it gives every role's return template the `probe` outcome, so
any role can raise a probe (night pass, point 2, item 8), through one factory that composes every
every-role arm.

## 2. Scope (IN)

- **S1** — The arm factory (shared interface J3). `derive_return_arms(schema)` in
  `tools/roles/roles_lib.py` reads every `[return.<arm>]` table of `tools/roles/role-schema.toml` in
  declaration order and returns one `(arm, outcome, fields)` per table. It replaces the refusal-only
  composition TOOL-dBoundRoles-43 S13 puts in `render_role`, which now renders every arm it returns,
  in that order, after the role's own template, each in the form S13 gives the refusal arm. The
  catalogue checker's refusal of a role whose `return` redeclares the refusal arm's outcome
  (TOOL-dBoundRoles-26 §4 "The arm") reads the factory, so redeclaring any arm's outcome is refused.
  The brief names this function `compose_return_arms`; the lexicon refuses its verb (§8 F1). Observed
  by AC1 and AC2.
- **S2** — The probe arm, the factory's second instance:

  ```toml
  [return.probe]
  outcome = "probe"
  fields = ["subject", "question", "kind"]
  kinds = ["verification", "reproduction", "experiment"]
  ```

  `validate_return` (TOOL-dBoundRoles-5 S1) refuses a return whose `outcome` is `probe` and whose
  `subject` or `question` is empty, or whose `kind` is outside `kinds`, naming the field, as it
  refuses a malformed refusal (TOOL-dBoundRoles-26 S2). The driver hands a valid one to
  TOOL-dPlacedRequest-7 S3's `probe.py trigger --cause raised --subject <subject>`, the asker the
  returning item, and S4's `pin` takes `--kind` and `--question` from it. Observed by AC2 and AC3.
- **S3** — The re-founded role file `tools/roles/agents/gov-tester.agent.md`, per §4 "### The role":
  its `tools` gain `Write` and `Edit` for experiments under its scratch path; `writes` stays `none`, so
  no repository class is granted; `reads` gains `input:question`; `verifies` is `verdict, claim`
  (TOOL-dFurnishedOrders-5's field), since it attributes each red and judges each claimed probe
  verdict; `slices` names the two sections its body cites; and its `return` template carries the
  four items' outcomes. Its body states the four acts. Observed by AC4 and AC5.
- **S4** — The probe items the tester takes over. The two `[[stand-in]]` rows of `tools/loop/loop.toml`
  that TOOL-dPlacedRequest-7 S2 declares for `item.probe.design` and `item.probe.judge-claimed`
  (TOOL-dDeclaredLoop-13 S8's table) are deleted, and the four tester items' `actor` cells name one
  slot, the form `item.test.attribute`'s row carries after TOOL-dWitnessedBar-23 S7. Observed by AC6.
  **Readers:** by name: READER NOT IN TREE — `read_stand_ins` (TOOL-dDeclaredLoop-13 S8),
  `check_transition_tables` and TOOL-dPlacedRequest-7's fixture plants read the table whole, and none
  is built at base ·
  by value: the engine's `move`, which answers `stand-in <owner>` for an item a row names, and now
  resolves the actor instead.
- **S5** — The browser, a stand-in. The tester's body says a visual check runs only where the harness
  grants a browser tool, and that where none is granted it designs the check as unrunnable, as
  night-pass point 2 item 9 states; no harness declares one at base. The hand-over is
  dWellOiledMachine's `browser` row in the harness capability table: once an adapter declares it, the
  tester's `tools` gains that adapter's browser tool and nothing else here moves. Observed by AC5.
- **S6** — The renders and the kit's text: `.claude/agents/gov-tester.md` and `.claude/roles.json` by
  `render_agents.py --write`, every other agent file re-rendered with the arm; `tools/roles/README.md`
  and `help/roles.md` name the tester's four acts and the `probe` outcome every role may return.
  Observed by AC7.

## 3. Non-goals (OUT)

- The probe program, its items, records, keys and the `probe` outcome on item rows:
  TOOL-dPlacedRequest-7. This unit gives role templates the outcome its S8 says no role returns yet.
- The capability table and its `browser` row, and the visual capture adapter: dWellOiledMachine's.
- The experiment shape and its scorer: dBoundRoles' and dFairHearing's.
- The `layer` and `acts-as` fields and the roster row: TOOL-dBoundRoles-1, which `gov-tester` already
  carries when this unit runs.
- Routing `code-miss` and `spec-wrong`: TOOL-dWitnessedBar-3 and -21, unchanged.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-5` — `verifies`, the field the tester carries as `verdict, claim`; without it the tester declares no subject and its `## Trust` block says nothing
- **hands-off** `TOOL-dFurnishedOrders-19` — `derive_return_arms`, the brief's `compose_return_arms` respelled for the lexicon, through which the established rows' arm is declared once
- **hands-off** `TOOL-dFurnishedOrders-7` — `derive_return_arms`, J3's factory as the lexicon spells it (§8 F1), through which `[return.repair]` joins every role's template
- **hands-off** `TOOL-dFurnishedOrders-9` — `gov-tester`, the role whose four items the matrix rows read
- **consumes-from** external — TOOL-dWitnessedBar-23's `gov-tester`, TOOL-dBoundRoles-26's `[return.refusal]`, TOOL-dBoundRoles-43 S13's composition, TOOL-dBoundRoles-5's `validate_return`, and TOOL-dPlacedRequest-7's items and `probe.py`, each specced and unbuilt at base
- **hands-off** `TOOL-dFurnishedOrders-22` — the re-founded `gov-tester` role file, its `reads` and its `verifies`, which unit 22 gives a `subject-reads` value (id 1)
- **hands-off** `TOOL-dFurnishedOrders-24` — `derive_return_arms`, whose triples unit 24 renders as one schema branch per outcome (id 4)
- **hands-off** `TOOL-dFurnishedOrders-29` — the tester's Write and Edit and AC7's docs, which unit 29 S3 confines and S7 tightens (ids 24, 51, 15)

## 4. Design

### The factory

```
derive_return_arms(schema) -> [(arm, outcome, fields), ...]   # every [return.<arm>] table, in file order
render_role(...)  ## Return: the role's template, then one line per arm, the form S13 gives refusal
check_roles R2    a role whose return names any arm's outcome is refused, naming the arm
validate_return   a return whose outcome is an arm's validates against that arm's table
```

Each arm keeps its own value sets beside `outcome` and `fields` (`actors` for refusal, `kinds` for
probe), and `validate_return` reads the set named for its field. Units 7 and 19 add their arms as
tables; no caller changes.

### The role

```markdown
---
name: gov-tester
description: Attributes the reds handed to it, answers the Test step's question, and designs and judges probes.
tools: Read, Grep, Glob, Bash, Write, Edit
model: inherit
workflow: gate-bar
reads: input:spec, input:diff?, input:question?
writes: none
verifies: verdict, claim
slices: doc.build-method#m6-passes-commits-parallelism, doc.build-method#m12-research-test-choose-when-the-solution-is-not-given
return: outcome:code-miss|spec-wrong|designed|judged, evidence:text, method:text?, losing:text?
---
```

The keys TOOL-dBoundRoles-1, -2 and -15 give every role (`layer`, `acts-as`, `never`, `budget`,
`rules`, `mandatory`, `output`) keep the values those units set; the block shows the keys this unit
moves. The body, under its `budget`, says: for each red you are handed, return `code-miss` or
`spec-wrong` with the evidence (`test.attribute`) or the Test step's answer (`test.reason`); for a
pinned probe, write its method and the outcome that would make it lose before anything runs, and
return `designed` (`probe.design`); for a verdict held as claimed, judge it from its recorded outputs
and return `judged` (`probe.judge-claimed`); an experiment's files go under the scratch path your task
names; a visual check runs where the harness grants a browser tool, and is designed unrunnable where
none is granted. Its `never` entries are TOOL-dBoundRoles-2's grammar: `runs a gate leg —
scratch-guard.js role-gate arm` and `writes a repository path — unenforced — the role arm grades the
spec and product classes, and this role declares neither`.

The two `slices` are the sections the body cites: M6 for the no-gate rule, M12 for writing the losing
outcome first.

### Rendered return

```
## Return

outcome:code-miss|spec-wrong|designed|judged, evidence:text, method:text?, losing:text?
- or outcome: refused — rule, remedy, actor (self|producer|driver|owner|build:<slug>)
- or outcome: probe — subject, question, kind (verification|reproduction|experiment)
```

The arm lines are S13's form, whatever its final bytes; this unit adds the third line to every role.

### Inventory

Minted: `derive_return_arms`; the `[return.probe]` table and its `kinds`; the outcomes `designed` and
`judged` on the tester's template. `python tools/lexicon/lexicon.py --suggest derive_return_arms --as
py.function` answered OK; `compose_return_arms` was refused (§8 F1).

### Migration

Every agent file gains the probe line, so every role-sha moves; landed handoffs are frozen. An
adopter's roles gain the arm through the roles kit's update, and an adopter role whose own `return`
spells `outcome: probe` is refused by name, its remedy to drop the line. The two stand-in rows leave
an adopter's `loop.toml` through the loop kit's update.

### Rollout

Live at landing. A role's probe is opened only as `probe.raise` allows (TOOL-dPlacedRequest-7 S7);
under `owner-only` or `off` the trigger refuses `raised` and the item continues. Each role's `budget`
gains exactly its rendered probe line's bytes, and the tester's its re-founded block's, by
TOOL-dBoundRoles-15 §4 "Pricing" (TOOL-dFurnishedOrders-5 §8 F3's precedent).

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/role-schema.toml`
- `tools/roles/check_roles.py`
- `tools/roles/render_agents.py`
- `tools/roles/handoff.py`
- `tools/roles/agents/gov-tester.agent.md`
- `tools/roles/agents/` (every role file's `budget`, re-derived for the probe line)
- `tools/roles/README.md`
- `tools/roles/adopt-roles.test.sh`
- `tools/loop/loop.toml`
- `.claude/agents/` and `.claude/roles.json` (renders)
- `help/roles.md`

### Alternatives rejected

- **The probe arm written into each role file.** Thirteen copies of one fact, the defect
  TOOL-dBoundRoles-26 rejected for the refusal arm.
- **A tester with `writes: product`.** An experiment that writes needs scratch, never the product
  tree; a product grant would let a test edit what it judges.

## 5. Production-readiness checklist

- security — no repository write class is granted; the tester's new `Write` and `Edit` reach its
  scratch path, and the role-gate arm still refuses it every gate leg.
- perf / scale — one more line per agent file; the factory reads one TOML file already loaded.
- error / empty / loading states — a malformed probe return is refused by field; a policy refusing
  `raised` leaves the item on its own route.
- observability — the refusal and the validation lines name the arm and the field.
- risks — a role may raise probes a designer did not expect; `probe.raise` is the owner's bound.
- testing — AC1 to AC7 by a pass over scratch fixtures; the arms of §7 at the close.
- migration — as §4 says.
- user docs — `help/roles.md`, by S6.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `roles_lib.derive_return_arms` over the kit's schema after the
  pass, it returns two arms in order, `refused` then `probe`, and every rendered agent file under
  `.claude/agents/` holds one `outcome: probe` line after its `outcome: refused` line.
  Red when: the factory hard-codes the refusal arm, so a second table is not composed.
- **AC2** — When a scratch role's `return` adds `outcome:probe`, `python check_roles.py` exits 1
  naming the role and the `probe` arm; and when `python -c` calls `validate_return` on a return
  `{"outcome": "probe", "subject": "x", "question": "q", "kind": "guess"}`, it refuses naming `kind`.
  Red when: an arm is validated only when it is the refusal arm.
- **AC3** — When `grep -n 'outcome = "probe"'` runs over the schema file and `grep -n '"probe"'` over
  the loop kit's `loop_lib.py`, the arm's outcome and the word `check_probe_outcomes` requires on
  role items are one spelling.
  Red when: the template arm and the item outcome spell the outcome two ways.
- **AC4** — When `python check_roles.py` runs over gov after the pass, it exits 0; `gov-tester`'s
  index entry in `.claude/roles.json` has `writes` `none`, `verifies` `["verdict", "claim"]` and no
  `gates` list.
  Red when: the tester gains a repository write class or a gate leg.
- **AC5** — When `grep -c` runs over the rendered `gov-tester.md` for `probe.design`,
  `probe.judge-claimed`, `scratch path` and `browser tool`, each prints at least 1, and its `## Trust`
  block holds `- Verifies: verdict, claim`.
  Red when: the body omits an act or the browser stand-in.
- **AC6** — When `grep -c 'item.probe.design\|item.probe.judge-claimed'` runs over the `[[stand-in]]`
  rows of `loop.toml` it prints 0, and the four tester items' `actor` cells print one spelling.
  Red when: a stand-in row survives, so a move through the item still answers `stand-in`.
  fixture: the loop kit's `loop.toml` as TOOL-dPlacedRequest-7 lands it; absent at base.
- **AC7** — When `grep -n "probe"` runs over `help/roles.md` and `tools/roles/README.md`, each names
  the outcome every role may return, and `grep -n "gov-tester"` over each names its four acts.
  Red when: the docs describe the minimal tester only.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `policy fixtures` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · a scratch schema with a third arm table and a role redeclaring `outcome:probe`, staged by a factory that composes the refusal arm alone · none

## 8. Open questions

- **FACT-QUESTION · F1 — May the factory be named `compose_return_arms`, as the brief's J3 spells
  it?** Probe: `python tools/lexicon/lexicon.py --suggest compose_return_arms --as py.function`.
  Observation: it answers that `compose` is not in the declared verb table, which `lexicon naming
  predicates` reds on; the liveness assertion is that the same probe answers OK for
  `derive_return_arms`, so it can tell the two apart. RESOLVED (agent, 2026-10-26, delegated):
  `derive_return_arms`, the lexicon's declared verb `derive`, rung 2. Units 7 and 19 read it under
  this name. widens: none · relaxes: none
- **F2 — Does the probe join both ways, items to templates and templates to items (D8)?** Options:
  (a) one spelling, the arm's `outcome` and `check_probe_outcomes`' word, observed by AC3; (b) a new
  check that every role acting in a role item carries the arm. (b) can never red: the factory
  composes every arm into every template, so a role without it cannot be rendered. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the only survivor with a red case; what it does not check is
  stated here. widens: none · relaxes: none
- **F3 — What is the tester's allowance (scratch)?** Options: (a) `writes: none` with `Write` and
  `Edit` tools, scratch writes admitted by the scratch verdict before the role arm reads the class;
  (b) a new `scratch` writes class; (c) `writes: product` held to an empty allowance. (b) mints a class
  the role arm would grade for nothing, since scratch is outside the repository; (c) grants what the
  clause does not. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor
  inside veto 3. widens: none · relaxes: none
- **F4 — The parents this unit calls are specced and unbuilt at base `2193e25d`.** TOOL-dWitnessedBar-23's
  role file, TOOL-dBoundRoles-26's arm, TOOL-dBoundRoles-43 S13, TOOL-dBoundRoles-5's `validate_return`
  and TOOL-dPlacedRequest-7's items do not exist in the tree; the open ask TOOL-dBoundRoles-36 already
  moves the minimal tester to the typed shape. RESOLVED (agent, 2026-10-26, delegated): the build run
  re-grounds on each at the pass and stops the unit if a called section is still absent then, rung 1
  (the brief's rule for DEFERRED parents). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 15, the brief's J3 and D8, scout C's
  row 15, and the source at `1a3ce03d`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dFurnishedOrders-22, TOOL-dFurnishedOrders-24, TOOL-dFurnishedOrders-29, promoted from the round-1 spec audit (`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: TOOL-dBoundRoles-26's `[return.refusal]` table and TOOL-dBoundRoles-43 S13's
composition in `render_role` (`tools/roles/roles_lib.py:604`), the first instance of an every-role
arm, whose second instance this is, so the charter's reuse rule extracts the factory here; the
minimal `gov-tester` of TOOL-dWitnessedBar-23, re-founded in place rather than beside it; the
`gate-bar` entry (`tools/roles/workflows.toml:72-78`, `roles = []` at base) that unit lists the tester
in. `python tools/codebase-map/reuse_lookup.py "compose one outcome arm into every role's return
template"` returned name-stem candidates only (`arm`, `run_arms`, `render_role`, `check_arm`), none an
arm composer, as scout C found; nothing composes return arms at base. The recall probe returned scout
C's row, TOOL-dPlacedRequest-7's item table (`item.probe.design` and `item.probe.judge-claimed` with
actor `role:tester`), the ask TOOL-dBoundRoles-36 on the minimal tester's retiring shape, and night
pass point 2 item 8. Scout C's line numbers match source at `1a3ce03d`.

Recall terms used: `python tools/memory-recall/query.py "how is the tester agent re-founded and how
does every role raise a probe from its return" --terms "gov-tester tester probe outcome return
template refusal arm role-schema WK-1 probe.design judge-claimed"`
