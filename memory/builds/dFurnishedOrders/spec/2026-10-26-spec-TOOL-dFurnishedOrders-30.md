# TOOL-dFurnishedOrders-30 — the round-1 audit's 16 workflows, unattended, kickoff and memory-tree minors: retired keys refused and observed, every cold carrier named, the card's map cell given a failure state, and the harness's rows checked in-script

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 5ff43572 · streams tooling · order 22 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-22-round1-fix-return.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-22-round1-fix-return.md) | research | TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-29 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-22-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-22-round1-fix-brief.md) | research | TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-29 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 20 unit specs
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`)
confirmed 35 MEDIUM and 16 LOW findings. BUILD-METHOD M4 batches them into two units because they split
into disjoint write sets by M6; `TOOL-dFurnishedOrders-29` §4 "Why two units" holds the cut. This unit
takes the 16 whose fixes write the workflows, unattended, kickoff and memory-tree kits: 12 MEDIUM and 4
LOW. Each report id is named once below and closed by its scope item.

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M3 | 6, 20, 49 | unit 4 S5, AC5, F4 | S1 |
| L2 | 11 | unit 4 S5 | S2 |
| M5 | 8, 22, 42, 53 | unit 5 S5, §4, AC6 | S3 |
| M6 | 21, 40 | unit 4 S5, S6 readers | S4 |
| M19 | 41 | unit 16 S11 | S5 |
| M23 | 54 | unit 13 S4, S6, §5 | S6 |
| M24 | 55 | unit 13 §4, S4; unit 1 S4 | S7 |
| L4 | 13 | unit 13 §4 | S8 |
| L10 | 28 | unit 19 S4, S8 | S9 |
| L12 | 46 | unit 4 S4, S6 | S10 |

## 2. Scope (IN)

- **S1** — ids 6, 20, 49. The `prebuild` refusal kept and observed. `tools/workflows/unattended-unit.js`
  refuses a caller passing `prebuild` before any spawn, naming the key and its step, as it refuses
  `checklist`; the absence check is scoped to the `prebuild` machinery, the paragraph, validation
  message and log line unit 4 S5 takes out (`unattended-unit.js:43-49`, `:142-143`, `:273-281`, `:325`), never
  the whole file. Unit 4's ledger answers AC5 AMENDED, naming this item. Observed by AC1.
- **S2** — id 11. Each refusal names the step of unit 4 S7: `unattended/retire-pass-checklist` for
  `checklist`, `review-harness/retire-prebuild` for `prebuild`. Observed by AC1.
  **Readers:** by name: READER NOT IN TREE — the two step ids are minted by `TOOL-dFurnishedOrders-4`
  S7 and no tracked file spells them at base · by value: NO VALUE READERS — the message is read by the
  caller it refuses and compared by nothing.
- **S3** — ids 8, 22, 42, 53. Every carrier of the author's commit messages, under `cold`. In
  `tools/workflows/tier2-review.template.js`, rendered to `tools/workflows/tier2-review.js`, the
  `{{VERIFIER_CONTEXT}}` value `cold` withholds: the instruction in `renderIntent` (`:1126`); the
  commit-message clause of the intent lens brief (`:798`), which every finder prompt carries as
  `LENS: ${L.brief}` (`:1197`), so a cold intent lens reads its specs and the caller's context only; the
  clause of the warning at `:885`; and the clauses of the synthesis lines at `:1804-1807`. Under `warm`
  each reads as at base. Observed by AC2.
- **S4** — ids 21, 40. The unattended suites' readers of the per-pass line re-pointed.
  `tools/unattended/adopt-unattended.test.sh`'s three `hit` lines on the per-pass command
  (`:257`, `:605`, `:627`) assert its absence, and arms 7 and 9 observe `MEMORY_TREE_DIR` through the
  line `tools/unattended/SKILL.template.md:67` renders; `tools/workflows/unattended-build.test.sh`'s
  PV-AC12 (`:2340-2357`) asserts the hand-out carries no `checklist` and the Skill no per-pass line.
  Both suites stay WAIVED at landing by the build README's rule, and these arms are owed by name to
  PLAY-dClosedLoop-18's clean reading. Observed by AC3.
- **S5** — id 41. The unattended Skill fits its row. Unit 16 S11's line is paid for by an equal trim of
  `tools/unattended/SKILL.template.md`, so the render `.claude/skills/unattended/SKILL.md` is at most
  10240 bytes (`tools/template-size-limits.txt:154`; 10237 at base, PINNED 2026-10-26); step 0's pointer
  at the build method, a row of `memory/project/method-carriers.txt`, stays. Observed by AC4.
- **S6** — id 54. A map renderer that fails. When `gov_map.py` resolves, `check_card_map`
  (`skills/session-kickoff/manifest-check.sh`, unit 13 S2 to S4) runs its level 0 itself under a
  10-second bound; a non-zero exit or an expired bound admits a body with no `project-map —` cell and
  writes `project-map — unavailable: gov_map.py exited <rc>` after `live —`; a body carrying a cell then
  is refused naming the unavailable state. Observed by AC5.
- **S7** — id 55. The cell lifted from a copy. `check_card_map` lifts the cell's lines from a copy of
  the body; the annotation `awk` (`manifest-check.sh:1170-1171`) runs over the body as appended, so
  each `UNVERIFIED — ` and unit 1's `RECALL — ` line keyed by `check_card_citations` (`:971`) sits under
  the row it was keyed to, and a miss keyed to a lifted row travels with the cell. Observed by AC6.
- **S8** — id 13. The card spells the not-installed state as unit 4 S1's J4 does:
  `project-map — not-installed: no gov_map.py in this tree (TOOL-dTotalRecall-14)`. Observed by AC5.
- **S9** — id 28. The harness route's rows checked in-script. After a builder returns,
  `unattended-unit.js` evaluates its `establishes` and `upstream` against the `returnRows` schema with
  `checkRowsSchema(schema, obj)`, which implements the keywords `addUpstreamSchema` emits and throws on
  any other; a failing return is treated as null and re-run under `retries`, so unit 19 S8 no longer
  rests on the runtime enforcing them. Observed by AC7.
- **S10** — id 46. The `memory-tree/gotchas` contract of `tools/memory-tree/kit.toml` (`:433-439`) gains
  a `[[contract.clause]]` whose probe runs `--for-names` with a class record the kit ships, expecting
  the checklist header, `consumer = "roles:handoff.py"`. Observed by AC8.

## 3. Non-goals (OUT)

- Rewording the spec text of units 1, 4, 5, 13, 16 and 19. Each item is closed by what this pass builds;
  where a landed criterion cannot hold as written (unit 4 AC5), that unit's ledger answers it AMENDED.
- The 35 minors of `TOOL-dFurnishedOrders-29`, and the BLOCKER and HIGH findings units 22 to 28 close.
- Raising the unattended Skill's row: the raise terms of `tools/template-size-limits.txt:16-23` need
  the unit's own change to cross it and a `memory/DECISIONS.md` row, and S5's trim needs neither.
- The report's left-shift gates. No clause of this build names them.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-1` — the `RECALL — ` annotation lines, whose placement S7 keeps under their rows (id 55)
- **consumes-from** `TOOL-dFurnishedOrders-4` — the retired dispatch keys, their steps, the Skill line and the gotchas contract, which S1, S2, S4 and S10 settle (ids 6, 20, 49, 11, 21, 40, 46)
- **consumes-from** `TOOL-dFurnishedOrders-5` — `{{VERIFIER_CONTEXT}}` and its cold brief, whose carriers S3 names and withholds (ids 8, 22, 42, 53)
- **consumes-from** `TOOL-dFurnishedOrders-13` — `check_card_map` and the card's map cell, which S6 to S8 settle (ids 54, 55, 13)
- **consumes-from** `TOOL-dFurnishedOrders-16` — the unattended Skill's asked-live line, which S5 fits under the Skill's row (id 41)
- **consumes-from** `TOOL-dFurnishedOrders-19` — `returnRows` and `addUpstreamSchema`, whose rows S9 checks in-script (id 28)

## 4. Design

### Why this unit stands apart

`TOOL-dFurnishedOrders-29` §4 holds the cut: each kit's version line moves with its own bytes, so the
halves follow the kits. This unit's write set is its Files touched below, none in unit 29's. No
criterion here reads a file unit 29 writes: S3's renders read the workflows template, S6 and S7 read
the card and a stub renderer, S9 reads a schema planted in its fixture, and S10's probe runs
`gotchas.py`, which neither half writes. The scratch-guard suite's guard spans the kickoff directory,
but no criterion of unit 29 reads `manifest-check.sh`. The two build concurrently.

### S3's carriers

| Site | Reads | Under `cold` |
|---|---|---|
| `:798` intent lens brief | every finder prompt (`:1197`) | "Read any spec or design document the diff touches …", no commit messages |
| `:885` warning | the report | the clause "beyond the range's commit messages" left out |
| `:1126` `renderIntent` | the intent block | the `git log --format=%B` instruction left out |
| `:1804-1807` synthesis lines | the synthesis prompt | the commit-message clauses left out |

The probe that found them is `grep -n "commit messages" tools/workflows/tier2-review.template.js`,
which printed exactly these five lines at `5ff43572`.

### Inventory

Minted: `checkRowsSchema`, answered OK by `python tools/lexicon/lexicon.py --suggest checkRowsSchema
--as js.function`; the card cell form `project-map — unavailable:`; one contract clause.

### Migration

None: no stored data changes shape. A card appended before this unit keeps its `not installed` cell
as written.

### Rollout

Live at landing, at order 22. The workflows kit's version line in `tier2-review.template.js`,
`KIT_MANIFEST_VERSION` and the unattended and memory-tree kits' versions move for the kit epoch leg.

### Files touched (estimate)

- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/tier2-review.template.js`, rendered to `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `tools/unattended/adopt-unattended.test.sh`
- `tools/unattended/SKILL.template.md`, rendered to `.claude/skills/unattended/SKILL.md`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `tools/memory-tree/kit.toml`

### Alternatives rejected

- **A scout-reported `unavailable` cell (S6).** The orientation scout's role file is the roles kit's,
  in unit 29's write set, and the append can observe the renderer's failure itself.
- **A whole-file `prebuild` count (S1).** The refusal S1 keeps spells the key, so the count cannot pass
  on a faithful build.
- **Trusting the runtime's schema enforcement (S9).** Nothing in this tree probes the Workflow
  runtime's `agent({schema})` validator; an in-script check holds whatever it enforces.

## 5. Production-readiness checklist

- security — S1 refuses a retired key before any spawn; S3 withholds the author's reasoning from every
  cold verifier prompt.
- perf / scale — S6 adds one bounded renderer run per READY append; S9 one evaluation per return.
- error / empty / loading states — S6 gives a failed renderer a named state; S9's failing return re-runs.
- observability — the card names `unavailable` with its exit; S1's refusal names the step.
- risks — S5's trim must keep every line the Skill's readers act on; AC4 checks the line S11 adds and
  step 0's pointer.
- testing — AC1 to AC8 by `node` fixtures, renders, byte counts and greps; the arms of §7 at the close.
- migration — none.
- user docs — none under `help/`: the Skill and the card are the surfaces, and S5 and S8 fit them.

## 6. Acceptance criteria

- **AC1** — When `grep -c -e "pre-build checklist" -e "prebuild checklist" -e "cfg.prebuild +"` runs
  over `tools/workflows/unattended-unit.js` it prints 0; and a `node -e` fixture running the script over
  a stub `agent` throws before any spawn when `args` carry `prebuild`, naming `prebuild` and
  `review-harness/retire-prebuild`, and when they carry `checklist`, naming
  `unattended/retire-pass-checklist`.
  Red when: a caller passing `prebuild` is silently ignored, or the absence check bans the refusal.
- **AC2** — When `tier2-review.template.js` is rendered with `VERIFIER_CONTEXT` `cold` and run in a `vm`
  context over a stub `agent` recording every prompt, no finder or synthesis prompt contains
  `commit messages`; rendered `warm`, the intent finder's prompt does.
  Red when: a cold verifier is still told to read the author's reasoning.
- **AC3** — S4's own code is the two suites' assertion text, read here by a probe and never run. When
  `git grep -n "for-diff HEAD~1" -- tools/unattended/adopt-unattended.test.sh` runs, every line it prints
  is an absence assertion; and when
  `git grep -n "dispatch.args.checklist" -- tools/workflows/unattended-build.test.sh` runs, every line
  it prints is an absence assertion.
  Red when: an adopter arm still requires the retired line.
- **AC4** — When `wc -c < .claude/skills/unattended/SKILL.md` runs it prints at most 10240, and
  `grep -c "asked live"` and `grep -c "BUILD-METHOD.md"` over it each print at least 1.
  Red when: the Skill outgrows its row, or the trim takes a line a reader needs.
  figure: the byte count is DERIVED at observation time.
- **AC5** — When the card append runs with a stub `gov_map.py` that exits 1, the READY body lands and the
  stored card holds `project-map — unavailable: gov_map.py exited 1`; with no `gov_map.py`, it holds
  `project-map — not-installed:` and `grep -c "project-map — not installed"` over
  `skills/session-kickoff/manifest-check.sh` prints 0.
  Red when: every kickoff append exits 1 on a renderer crash, or two spellings name one state.
- **AC6** — When a READY body carries a map cell above a `## records` row citing a missing path, the
  stored card's `UNVERIFIED — ` line sits directly under that row.
  Red when: the lift shifts an annotation under an unrelated line.
- **AC7** — When `node` runs `unattended-unit.js` in a `vm` context with a `returnRows` line handing two
  rows and a stub `agent` whose first return doubles one row, the stub is spawned a second time; a
  well-formed return is accepted at once; a schema carrying `oneOf` throws naming it.
  Red when: a doubled row passes on the harness route.
- **AC8** — When `grep -n -- "--for-names" tools/memory-tree/kit.toml` runs it prints a probe line of
  the `memory-tree/gotchas` contract, and the next `consumer` line names `roles:handoff.py`.
  Red when: an adopter's older memory-tree kit gives no install-time signal.

## 7. Gates

`unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `workflow script syntax` · `manifest-check self-test` · `scratch-guard self-test` · `kickoff-manifest ratchet` · `check-wiring self-test` · `unattended skill size` · `unattended kit gate` · `unattended skill wiring` · `gotchas selftest` · `govkit selftest` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/unattended-build.test.sh · covers AC1 AC7 · a dispatch passing each retired key and a rows return that doubles a row, staged by ignoring `prebuild` · none
New arm: tools/workflows/tier2-review.test.sh · covers AC2 · a cold and a warm render over a recording stub, staged by restoring the intent brief's clause · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC5 AC6 · a failing stub renderer and a map cell above a missing citation, staged by lifting the cell from the body itself · none

## 8. Open questions

- **F1 — What does a cold intent lens read?** Options: (a) its specs and the caller's context only;
  (b) the commit messages, as today. (b) is the carrier the verifier-context key withholds. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 1, layer-roles `[trust]` item 6, "a verifier's packet …
  never holds the author's reasoning". widens: none · relaxes: none
- **F2 — How is a failed map renderer seen?** Options: (a) the append runs level 0 itself under a bound;
  (b) the scout reports an `unavailable` form. (b) writes the roles kit's scout file, outside this
  half's write set, and trusts the reporter. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  skeptic-judged alternative in the report. widens: none · relaxes: none
- **F3 — Is the Skill's growth funded or the row raised?** Options: (a) an equal trim; (b) a raise. (b)
  fails the raise terms' first and fourth conditions for this unit. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the survivor. widens: none · relaxes: none
- **F4 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F5 — The units this one lands on are unbuilt.** Units 1, 4, 5, 13, 16 and 19 are specced and
  unbuilt at `5ff43572`. RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on each at
  the pass and records any item a landed unit already closed, rung 1, the brief's rule. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the round-1 spec audit's workflows, unattended, kickoff and
  memory-tree minors batched.

## 10. Reuse audit

The seams extended: unit 4 S5's refusal in `unattended-unit.js`; the `{{VERIFIER_CONTEXT}}` token unit 5
S5 adds beside `{{FANOUT_CAP}}`; `add_card_body`'s annotation pass (`manifest-check.sh:1141-1191`) and
`check_card_citations`' keying (`:971`); the `[[contract]]` grammar of `tools/memory-tree/kit.toml:433-439`;
and `addUpstreamSchema` (unit 19 S8). `python tools/codebase-map/reuse_lookup.py "refuse a retired
workflow argument before any agent spawn and withhold commit messages from a cold verifier"` ranked
`before`, `build_commit`, `load_workflows` and two refusal classes of the process-monitor kit, none a
dispatch refusal or a brief renderer, so no existing seam fits beyond the ones named; no workflow script
imports a module, so S9's evaluator is inline, as the template's own header says of its fan-out helper
(`tier2-review.template.js:16`). The recall probe returned scout B's retirement inventory and unit 4's
S7 rows, neither disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which minor findings land on the workflows
unattended and kickoff kits" --terms "prebuild checklist retired tier2-review cold commit messages
adopt-unattended PV-AC12 skill size project-map card"`
