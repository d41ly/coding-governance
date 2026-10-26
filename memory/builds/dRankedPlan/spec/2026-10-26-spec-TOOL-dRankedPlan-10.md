# TOOL-dRankedPlan-10 — `plan.exit` falls back to the owner gate while the intake is not installed for the harness

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 4 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0378@ed811c10 whole
**Carries:** node:item.plan.exit

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-9 TOOL-dRankedPlan-15 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) | spec-audit | TOOL-dRankedPlan-16 TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 TOOL-dRankedPlan-2 TOOL-dRankedPlan-14 TOOL-dRankedPlan-13 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-15 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-7 |

<!-- /gen:spec-records -->

## 1. Goal

Under `plan.ratification: request` the owner's request is Plan's ratification, but the request is
witnessed only by dWellOiledMachine's prompt-submit hook writing the intake log (FR-1,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md:173-199`), and
neither that hook nor any adapter capability table exists: `.claude/settings.json` registers no
UserPromptSubmit, and the codebase map's harness-hook inventory lists PreToolUse, PostToolUse,
SessionStart, SubagentStart and Stop only. Until the intake lands and the harness's adapter declares
the prompt-submit event, `plan.exit` must fall back to dDeclaredLoop's owner gate, held for the
owner's disposition, its witness recorded as `intake not installed`, per harness, whichever of this
build and dWellOiledMachine lands first (RC-9, AF-1, DA-H1; v2:433-436). This unit is that fallback,
the capability read it rests on, and the arming of `item.plan.exit`, whose witness reader it lands.

## 2. Scope (IN)

- **S1** — The capability read, shared interface I9: `read_adapter_capabilities(harness, table=None)`
  in `tools/loop/ratify.py` returns `(events, why)`, the event words the `[[adapter]]` row named
  `harness` declares in the capability table `tools/loop/adapters.toml`. Each row carries `name`,
  `events` (a list of event words, `prompt-submit` among the vocabulary) and `measured` (the harness
  version the events were measured on). The table is not shipped by this unit. An absent table, an
  absent row and a row with no `measured` each declare nothing, `why` naming which ("measured and
  never claimed", `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:829`).
  Observed by AC1, AC4.
- **S2** — The intake read: `check_intake_installed(kit_dir)` answers whether the composed item rows
  `read_items` returns (TOOL-dDeclaredLoop-12 S1, composed by TOOL-dDeclaredLoop-24 S3) declare
  `item.entry.intake`, dWellOiledMachine's hook item (PM-9). Observed by AC3.
- **S3** — The fallback, shared interface I8: `derive_plan_exit_ratification(repo, slug, harness)` in
  `tools/loop/ratify.py` calls TOOL-dRankedPlan-9's `read_plan_ratification(slug)` (I6) once. Under
  any value but `request` it returns that answer unchanged. Under `request`, when S2 answers no or
  `prompt-submit` is not among S1's events, it returns the mode `fallback` with the witness
  `intake not installed` and the reason; otherwise it returns the predicate's answer as `met` or
  `unmet`. `python tools/loop/ratify.py <slug> --exit [--harness <name>]` prints one line, §4
  "### The answer"; a harness not passed is `unknown`, which no row names. Observed by AC1 to AC5.
- **S4** — The gate, `check_plan_exit(repo, slug, harness)` in `tools/loop/ratify.py`: Plan's exit is
  admitted when S3 answers `met`; when TOOL-dDeclaredLoop-19's plan gate is not held for the build,
  which TOOL-dDeclaredLoop-53 S2 prints as `passed before placement`; or when a disposition record
  (TOOL-dDeclaredLoop-16 S4) names `item.plan.exit` and that unit's `check_disposition_record` admits
  it. Otherwise it is refused `plan.exit — held · owner gate · <witness>`. Under `fallback` no
  ratification witness counts, so only the owner's disposition releases the gate. Observed by AC1, AC6.
- **S5** — `item.plan.exit` armed, as TOOL-dDeclaredLoop-13 §4 "The stand-ins" says an owning build
  arms its item: `write_transition` (`tools/loop/loop_transition.py`, TOOL-dDeclaredLoop-3 S5) calls
  S4 for a move whose item is `item.plan.exit` and exits 1 on its refusal before anything is written;
  `ratification` and `harness` join `TRANSITION_FIELDS`, so the move's trailer and log record carry
  ` · ratification=<how> · harness=<name>` (§4 "### The record"); and the `[[stand-in]]` row
  `item = "item.plan.exit"` is deleted from `tools/loop/loop.toml` in the same pass.
  **Readers:** by name: READER NOT IN TREE — the loop kit is absent at base 0689e7fa; the row's
  readers are TOOL-dDeclaredLoop-13's stand-in reader in its `loop_table.py` and TOOL-dDeclaredLoop-3's
  writer, both specced and unbuilt · by value: `write_transition`, which appends `stand-in=dRankedPlan`
  to a plan.exit move while the row stands, and the `move` verb of TOOL-dDeclaredLoop-13, which prints
  `stand-in dRankedPlan` beside it; both stop printing it at this pass, the arming that row waits for.
  Observed by AC1, AC2, AC7.
- **S6** — The driver's hold: the plan gate's arm of `check_owner_gates` (TOOL-dDeclaredLoop-19 S6,
  `tools/unattended/unattended.sh`) reads the gate as met only when `ratify.py <slug> --exit` answers
  `met`, and on `fallback` holds it as S6 holds every owner gate, released by
  `check_owner_disposition` (TOOL-dDeclaredLoop-31 S6) alone, the `decision` row its hold writes
  carrying the reason `intake not installed`. TOOL-dRankedPlan-9 wires no release arm of its own, so
  S4 and S6 are the only readers of Plan's exit, and neither bypasses the fallback. Observed by AC8.
- **S7** — The plants of §4 "### The plants", joined to TOOL-dRankedPlan-9 S7's `python
  tools/loop/ratify.py --fixture --plant <case>`, which `tools/loop/selftest.py` runs. Observed by AC1
  to AC6.
- **S8** — `help/plan.md` (TOOL-dRankedPlan-16 S9), beside TOOL-dRankedPlan-9's "Ratification"
  section, gains a section, "Plan's exit without the intake hook": the fallback, its witness, the
  capability table's row shape, and how the owner releases the gate. Observed by AC9.

## 3. Non-goals (OUT)

- The intake log, its hook, its record kind and its redaction: dWellOiledMachine's (`entry.intake`,
  PM-9, `cl-dClosedLoop-0282`). This unit reads whether the item is declared and never writes intake.
- The capability table's rows and the adapters themselves: dWellOiledMachine's
  (`runtime.harnesses`, layer-runtime `[harness]`). This unit reads a table no file supplies yet and
  plants one in its fixture.
- The ratification predicate and the other three values of `plan.ratification`: TOOL-dRankedPlan-9's
  `read_plan_ratification`, called and never re-specced.
- The owner gate, its placement, its hold and its release: TOOL-dDeclaredLoop-19, -53, -16 and -31.
  This unit decides when the plan gate is met and adds no second gate.
- Draining the fallback: dWellOiledMachine re-points Plan's ratification to the intake record and
  keeps fallback witnesses readable (`cl-dClosedLoop-0283`, DA-M14, DA-M15, FM3).
- The plan revision's re-entry into Plan: TOOL-dRankedPlan-15's. A revised plan crosses `plan.exit`
  again through S4 unchanged.

### Edges

- **consumes-from** `TOOL-dRankedPlan-9` — `read_plan_ratification`, the one predicate S3 asks under every value, and its `ratify.py --fixture` S7 joins; without it no ratification witness exists to count, and every exit falls to the owner gate
- **consumes-from** external — dDeclaredLoop, built before this build run: `read_items` (TOOL-dDeclaredLoop-12 S1), `write_transition` and `TRANSITION_FIELDS` (-3 S1, S5), the `[[stand-in]]` row (-13 S8), `derive_breakpoints` and `check_owner_gates` (-19 S1, S6), the pre-placement exemption (-53 S2), `check_disposition_record` (-16 S5) and `check_owner_disposition` (-31 S6)
- **hands-off** external — dWellOiledMachine: the `item.entry.intake` row, the capability table `tools/loop/adapters.toml` with each harness's measured `[[adapter]]` row, the `--harness` its executor passes, and readers that accept a `ratification=intake-not-installed` witness from an adapter lacking `prompt-submit` (`cl-dClosedLoop-0283`)
- **hands-off** `TOOL-dRankedPlan-19` — `check_plan_exit`, which that unit gives the precondition of a witnessed plan record (round-1 spec audit, id 1)
- **hands-off** `TOOL-dRankedPlan-21` — S5's `ratification` and `harness` fields on the `plan.exit` move, which that unit reads back as the durable fact of a ratified row (round-1 spec audit, id 3)
- **hands-off** `TOOL-dRankedPlan-25` — `check_plan_exit`'s disposition admission, which that unit bounds to the current crossing (round-1 spec audit, id 5)
- **hands-off** `TOOL-dRankedPlan-26` — `check_plan_exit`'s disposition admission, which that unit holds on a disposition of `ask` or `none` (round-1 spec audit, id 39)
- **hands-off** `TOOL-dRankedPlan-29` — `check_plan_exit`'s harness and the capability reader, which that unit's S15 and S38 correct (round-1 spec audit, ids 18, 48)

## 4. Design

### Evidence

- No harness capability table, prompt-submit hook or intake kind exists at base: `git grep -i
  "capability table\|UserPromptSubmit\|prompt-submit" -- tools skills .claude/settings.json` prints
  nothing, and `runtime.harnesses` (`tools/policy/catalogue.toml:505-509`) names its registry, "named
  harness adapters", which no file holds.
- `plan.ratification` is catalogued with `request` as default, owner dRankedPlan
  (`tools/policy/catalogue.toml:530-534`).
- The plan gate: `autonomy` `plan-only`, the default, places an owner gate at `item.plan.exit`
  (TOOL-dDeclaredLoop-19 S3), held at `--phase` and `--close` until a disposition record names it
  (S6), for builds opened after the placement only (TOOL-dDeclaredLoop-53 S2). FR-1 settles that
  "where `autonomy` keeps the owner's gate at Plan, that gate is met as `plan.ratification` says"
  (flow-roles.md:195-200), and flow-steps.md:193-194 routes Plan's exit before the intake lands: "the
  owner's words are taken as the owner gate's disposition, which `plan.exit` holds under
  `plan.ratification: request`".
- `item.plan.exit` is a stand-in owned by dRankedPlan, "the mover names the witnessing commit"
  (TOOL-dDeclaredLoop-13 §4 "The stand-ins"), and the list "shrinks only: an owning build arms its
  item by landing its witness reader and deleting the row together".
- The trailer value grammar is `[A-Za-z0-9._:+@-]+` (TOOL-dDeclaredLoop-3 §4 "The trailer"), so a
  value never holds a space.

### The answer

```
derive_plan_exit_ratification(repo, slug, harness)
  value, witness = read_plan_ratification(slug)          # TOOL-dRankedPlan-9, I6
  value != "request"                    -> (value, met|unmet as the predicate answers)
  not check_intake_installed(kit)       -> (request, fallback, "intake not installed", "intake item not declared")
  "prompt-submit" not in events         -> (request, fallback, "intake not installed", why from S1)
  otherwise                             -> (request, met|unmet, witness)
```

| Line `ratify.py <slug> --exit` prints | When |
|---|---|
| `plan.exit — request · fallback · intake not installed · <why>` | S2 says no, or S1 declares no `prompt-submit` |
| `plan.exit — <value> · met · <witness>` | the predicate counts a witness |
| `plan.exit — <value> · unmet · <why>` | the predicate counts none; the gate holds for a disposition |

`<why>` is one of `intake item not declared`, `capability table absent`, `adapter <h> not
registered`, `adapter <h> claims, never measured` and `adapter <h> declares no prompt-submit`. Exit
0 on every answer, 2 on an unknown slug or a refused policy read, naming it.

### The capability table

```toml
# tools/loop/adapters.toml — dWellOiledMachine's; absent at this unit's landing
[[adapter]]
name = "codex"
events = ["pre-tool-use", "subagent-start", "subagent-stop", "pre-compact", "session-end"]
measured = "codex-cli 0.139"
```

The planted Codex-shaped row leaves `prompt-submit` out although Codex 0.139 documents
UserPromptSubmit (layer-runtime.md:833-835): a documented event is not a measured one, and the
reader honours only what a measured row declares. One table per loop kit, read from the kit directory
`read_items` already resolves, so the reader takes no second resolution path.

### The record

| How Plan's exit was met | `ratification=` | Admitted by |
|---|---|---|
| the predicate's witness counted | `witness` | S3 `met` |
| the fallback held and the owner disposed | `intake-not-installed` | a disposition record naming `item.plan.exit` |
| no witness counted, the owner disposed | `disposition` | the same record |
| the gate was placed after the build opened | `before-placement` | TOOL-dDeclaredLoop-53 S2 |

`harness=<name>`, `unknown` when none is passed, rides beside it, so dWellOiledMachine's re-pointed
readers can tell a fallback witness from an adapter lacking the event from one written after its
drain (FM3). The clause's literal is recorded verbatim on the hold's `decision` row and on the
printed line; the trailer spells it in the value grammar.

### The plants

`python ratify.py --fixture --plant <case>` builds a scratch repository under a short `%TEMP%` path
with a loop kit copy, a policy file, a build in `planning` opened after the placement, and the plant:

| Plant | Table | `item.entry.intake` | Owner-origin intake | Expected |
|---|---|---|---|---|
| `codex-adapter` | the Codex-shaped row | declared | planted | `fallback`, held until a disposition |
| `claude-adapter` | a measured row declaring `prompt-submit` | declared | planted | `met`, admitted with no disposition |
| `no-intake` | the `claude-adapter` row | undeclared | planted | `fallback`, `intake item not declared` |
| `no-table` | none | declared | planted | `fallback`, `capability table absent` |
| `unmeasured` | the `claude-adapter` row less `measured` | declared | planted | `fallback`, `claims, never measured` |
| `other-value` | none | undeclared | none | under `terminal-command`, the predicate's answer unchanged |
| `pre-placement` | none | undeclared | none | admitted, `ratification=before-placement` |

The plants join TOOL-dRankedPlan-9's fixture, which builds the repository, the claim ref, the request
record and the policy file; the owner-origin intake is its `request` plant's typed request.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_adapter_capabilities`, `check_intake_installed`, `derive_plan_exit_ratification`, `check_plan_exit` | functions, `tools/loop/ratify.py` | `py.function`, asked at the pass |
| `--exit`, `--harness` | flags of `ratify.py` | none |
| `ratification`, `harness` | `TRANSITION_FIELDS` members | none |
| `[[adapter]]` with `name`, `events`, `measured` | capability-table row shape, read only | none |
| `codex-adapter`, `claude-adapter`, `no-intake`, `no-table`, `unmeasured`, `other-value`, `pre-placement` | fixture plants | none |

### Migration

None at base. A build crossing Plan's exit after this landing writes the two fields; earlier
transition records carry none and read as written before the fallback existed.

### Rollout

Live at landing, and conservative: with no table and no intake item, every harness falls back, so
every `request` build's Plan exit waits for the owner's disposition, which TOOL-dDeclaredLoop-19
already holds under the default `autonomy`.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S4 and S7's plants
- `tools/loop/loop_transition.py`: the S4 call and the two `TRANSITION_FIELDS` members
- `tools/loop/loop.toml`: the `item.plan.exit` stand-in row deleted
- `tools/unattended/unattended.sh`: S6's plan-gate arm and the `decision` row's reason
- `tools/unattended/unattended.test.sh`: the arm §7 declares
- `help/plan.md`: S8's section

### Alternatives rejected

- **Mint a minimal adapter row now.** A shipped table would claim measurements dWellOiledMachine has
  not taken, and the clause's own plant is a harness that must not declare the event.
- **Read the intake from the record-kind registry.** The `intake` kind and the item land together in
  dWellOiledMachine, and `read_items` is the loop kit's own reader, so S2 needs no sibling kit.
- **Treat dPlacedRequest's `.typed` request store as the intake.** It is the stand-in TOOL-dRankedPlan-9
  reads for its predicate; the clause names the intake kind and the event, which the store is
  neither, so counting it would drain the fallback before either lands.

## 5. Production-readiness checklist

- security — the fallback is deny-by-default: an absent, unregistered or unmeasured row declares
  nothing. A run that commits a forged table row still needs the gov-owned `item.entry.intake` row
  and an owner-origin intake the predicate counts, so a forged declaration alone releases nothing.
- perf / scale — one policy read through the predicate, one TOML read and one item composition per
  `plan.exit` move.
- error / empty / loading states — each fallback line names its reason; an unknown slug or a refused
  policy read exits 2.
- observability — the printed line, the two trailer fields and the hold's `decision` row.
- risks — every `request` build waits for the owner at Plan's exit until dWellOiledMachine lands,
  which is the clause's intent; an attended owner releases it with one disposition record.
- testing — the plants of §4, red and green, and the driver arm.
- migration — none.
- user docs — `help/plan.md`, S8.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant codex-adapter` runs, `ratify.py tFix --exit
  --harness codex` prints `plan.exit — request · fallback · intake not installed · adapter codex
  declares no prompt-submit`, the plan.exit move through `python loop_transition.py record --build
  tFix --from planning --item item.plan.exit --outcome pass --witness <sha>` exits 1 printing
  `plan.exit — held · owner gate · intake not installed`, and after the plant commits a disposition
  record naming `item.plan.exit` the same move exits 0 with a trailer carrying
  `ratification=intake-not-installed · harness=codex`.
  Red when: the Codex-shaped adapter reaches `designing` with no disposition record, or never reaches
  it once one is committed.
- **AC2** — When the plant `claude-adapter` runs the same move with no disposition record, it exits 0
  and the trailer carries `ratification=witness · harness=claude-code`.
  Red when: an adapter declaring a measured `prompt-submit` beside a declared intake item still falls
  back, so the fallback never drains.
- **AC3** — When the plant `no-intake` runs `ratify.py tFix --exit --harness claude-code`, it prints
  `fallback · intake not installed · intake item not declared`.
  Red when: an adapter's declaration alone drains the fallback before the intake item exists.
- **AC4** — When the plants `no-table` and `unmeasured` run `--exit --harness claude-code`, they print
  `capability table absent` and `adapter claude-code claims, never measured`, each as a `fallback`.
  Red when: an absent table or a claimed, unmeasured row declares `prompt-submit`.
- **AC5** — When the plant `other-value` sets `plan.ratification = "terminal-command"`, `ratify.py
  tFix --exit` prints the predicate's `terminal-command` answer and no `fallback`.
  Red when: the fallback reaches a value other than `plan.ratification: request`.
- **AC6** — When the plant `pre-placement` runs the plan.exit move with no disposition record, it
  exits 0 with `ratification=before-placement`.
  Red when: a build TOOL-dDeclaredLoop-53 exempts is held at `plan.exit`.
- **AC7** — When `python loop_table.py move --level build --from planning --item item.plan.exit
  --outcome pass` runs at the pass tip, it prints the move with no `stand-in dRankedPlan` beside it.
  Red when: the `item.plan.exit` stand-in row survives the arming.
- **AC8** — When a fixture repository under `%TEMP%` with a run-state file, a build in `planning`,
  no intake item and no disposition record runs `bash tools/unattended/unattended.sh --phase tFix
  RESEARCHING --witness <sha>`, it is refused naming the plan gate, and the `decision` row its hold
  writes carries `intake not installed`; after a disposition record naming that row is committed,
  the move is admitted.
  Red when: the driver releases the plan gate on a predicate answer while the intake is not installed.
  fixture: a committed repository with a run-state file, a policy file and one spec, built by the
  probe.
- **AC9** — When `grep -n "intake not installed" plan.md` runs over the help page, it finds S8's
  section naming `plan.ratification: request`, `prompt-submit` and the disposition record.
  Red when: the page does not describe the fallback.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · the seven plants under `--fixture`, the failing case the `codex-adapter` plant reaching `designing` with no disposition record · none

New arm: tools/unattended/unattended.test.sh · covers AC8 · the plan gate under the fallback, the failing case a `--phase RESEARCHING` move admitted with no disposition record · none

## 8. Open questions

- **F1 — Where does the capability table live, when no adapter grammar exists anywhere?** Options:
  (a) a reader over `[[adapter]]` rows of `tools/loop/adapters.toml`, absent at landing, so every
  harness declares nothing and falls back, dWellOiledMachine supplying the rows; (b) a minimal
  adapter row shipped now, which widens a dWellOiledMachine surface (scout B F10a); (c) no reader,
  the fallback unconditional until dWellOiledMachine edits this unit. (c) fails the clause's planted
  case, which needs an adapter to read; (b) claims a measurement nobody took. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the most feature-rich survivor: the reader is armed and seen
  on both plants, and the table's owner stays dWellOiledMachine. widens: none · relaxes: none
- **F2 — Does the Codex-shaped plant declare `prompt-submit`, which Codex 0.139 documents?**
  RESOLVED (agent, 2026-10-26, delegated): no, rung 1: layer-runtime.md:829 holds each adapter's table
  "measured and never claimed", and the clause plants a Codex-shaped adapter that reaches Plan's exit
  through the fallback. widens: none · relaxes: none
- **F3 — Is a build opened before the gate's placement held by the fallback?** RESOLVED (agent,
  2026-10-26, delegated): no, rung 1: the fallback is TOOL-dDeclaredLoop-19's plan gate, and
  TOOL-dDeclaredLoop-53 S2 never holds that gate for such a build; S4 reads its answer and the record
  says `before-placement`. widens: none · relaxes: none
- **F4 — How is the witness `intake not installed` recorded, when the trailer's value grammar admits
  no space?** Options: (a) verbatim on the hold's `decision` row and the printed line, and as
  `ratification=intake-not-installed` on the transition; (b) a new free-text field on the log record
  alone, which TOOL-dDeclaredLoop-3's `check` would red as unequal to its trailer. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3: every channel carries the witness, each in the grammar it
  admits. widens: none · relaxes: none
- **F5 — What counts as "the intake kind lands"?** Options: (a) `item.entry.intake` declared in the
  composed item rows; (b) an `intake` row in TOOL-dTotalRecall-1's record-kind registry. Both land in
  dWellOiledMachine's one pass. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, tie-broken by
  reuse of the loop kit's own `read_items`, where (b) is a sibling kit's file. widens: none ·
  relaxes: none
- **F6 — The ask on dDeclaredLoop: `item.entry.intake`'s fixed row is never armed.**
  TOOL-dDeclaredLoop-24 §4 "The schema" writes that fixed row "when dPlacedRequest declares it as an
  item", while dWellOiledMachine declares it (TOOL-dPlacedRequest-3 §3 and §8 F8), so the row S2 reads
  would carry no fixed witness and an overlay patch could reshape it. The ask, for the main loop to
  file once in dDeclaredLoop's `BACKLOG.md`: target dDeclaredLoop, TOOL-dDeclaredLoop-24's trigger
  re-worded to "when dWellOiledMachine declares it". Accept: the pass that declares `item.entry.intake`
  writes its `[[fixed-row]]` in `tools/loop/item-schema.toml`, seen as a patch of that item's
  `witness` refused once `read_items` lists it. RESOLVED (agent, 2026-10-26, delegated): file the ask,
  rung 3, since the parent spec is never edited here and S2 holds without it. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 10, v2:433-436 and :1779, flow-steps.md
  :164-194, flow-roles.md:173-199, layer-runtime.md:827-844, TOOL-dDeclaredLoop-3, -12, -13, -16, -19,
  -31 and -53 at base, and scout B's row -10.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-19`, the hands-off edge to `TOOL-dRankedPlan-21`, the hands-off edge to `TOOL-dRankedPlan-25`, the hands-off edge to `TOOL-dRankedPlan-26`, the hands-off edge to `TOOL-dRankedPlan-29`, each the reciprocal of that promoted unit's own edge (round-1 spec audit, `reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams are TOOL-dDeclaredLoop-19's owner gate and hold (`derive_breakpoints`, `check_owner_gates`),
released by the disposition record (-16 S4, S5; -31 S6) and exempted by -53 S2; TOOL-dDeclaredLoop-3's
`write_transition` and `TRANSITION_FIELDS`, extended by two members as -27 S8 extends them; the loop
kit's `read_items` (-12 S1); and TOOL-dRankedPlan-9's `read_plan_ratification`, called once. The
capability read has no seam: `python tools/codebase-map/reuse_lookup.py "fall back to an owner gate
when the prompt-submit hook capability is not declared by the harness adapter"` ranked name stems
(`note`, `declares`, `owners_of`, `check_gate_wall`, `resolve_harness_path`), none of which reads an
adapter's events; `resolve_harness_path` (`tools/roles/roles_lib.py:620`) resolves a workflow
harness's file path, not a runtime adapter, and the map's harness-hook inventory lists no
UserPromptSubmit, so no existing seam fits and S1 is new. The recall query returned the packet's
clause, scout B's row and TOOL-dPlacedRequest-5's breakpoint disposition, which agree with source.
Where records and source disagree: scout B cites the fixed-row gap as blocking "the intake kind
lands" probe; S2 reads the item row, which needs no fixed row, so the gap is F6's ask, not a blocker.

Recall terms used: `python tools/memory-recall/query.py "how does plan exit fall back to the owner gate when the intake hook is not installed for a harness" --terms "plan.exit plan.ratification request fallback owner gate intake prompt-submit adapter capability table Codex disposition"`
