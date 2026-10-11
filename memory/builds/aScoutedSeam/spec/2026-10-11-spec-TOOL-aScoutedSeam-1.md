# TOOL-aScoutedSeam-1 — the reuse scout: a checklist role and a harness running a code and a design pass, merged into a capped `## reuse` section

**Status:** SPECCED · rev-5 · 2026-10-11 · node a · Tier-2 · base d19938f3 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md](../build/2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md) | research | TOOL-aScoutedSeam-2 TOOL-aScoutedSeam-3 KICK-aScoutedSeam-1 DEPL-aScoutedSeam-1 |
| [2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md](../build/2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md) | research | TOOL-aScoutedSeam-3 |
| [2026-10-11-build-TOOL-aScoutedSeam-1-3-cases.json](../build/2026-10-11-build-TOOL-aScoutedSeam-1-3-cases.json) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-4-bench.py](../build/2026-10-11-build-TOOL-aScoutedSeam-1-4-bench.py) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-5-results.json](../build/2026-10-11-build-TOOL-aScoutedSeam-1-5-results.json) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-batch-all.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-batch-all.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-d1-diff-check.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-d1-diff-check.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-judge.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-judge.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-m1-single-scout.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-m1-single-scout.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-m1b-checklist-scout.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-m1b-checklist-scout.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-m1c-sketch-scout.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-m1c-sketch-scout.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-m2-lens-scout.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-m2-lens-scout.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-m3-complete.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-m3-complete.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-m3-halves.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-m3-halves.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-m3-lean-scout.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-m3-lean-scout.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-rerun-effort.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-rerun-effort.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-6-rerun.js](../build/2026-10-11-build-TOOL-aScoutedSeam-1-6-rerun.js) | research | — |
| [2026-10-11-build-TOOL-aScoutedSeam-1-7-m1c-trial.md](../build/2026-10-11-build-TOOL-aScoutedSeam-1-7-m1c-trial.md) | research | KICK-aScoutedSeam-1 |

<!-- /gen:spec-records -->

## 1. Goal

Ship the agent that orientation runs before any spec is written. It reads the code, not the names,
and returns the seams a request must build with as a short, binding, capped list. The design comes
from two measurements:
- In the benchmark (`2026-10-11-build-TOOL-aScoutedSeam-1-2-benchmark.md`), one checklist scout
  solved 10 of 14 paired positives where the shipped lookup solved none. A design pass beside it
  recovered the token and pattern layer the code pass missed.
- In the M1c trial (`2026-10-11-build-TOOL-aScoutedSeam-1-7-m1c-trial.md`), three additions to that
  checklist raised it from 13 to 16 of 24 by the path matcher, in each of two runs: a generated
  house index, an implementation sketch searched piece by piece, and a convention census.

## 2. Scope (IN)

- **S1** — The `gov-reuse-scout` role BODY, plus its `reads` and `returns`, in the slot aOrientedCast's
  catalogue creates. The body is the checklist the trial's M1c arm ran, in substance, and in order:
  - read the house index (S10);
  - orient;
  - frame the needs and SKETCH the implementation, 6 to 15 components a builder would write,
    plumbing included;
  - anchors and the canonical implementation;
  - the convention census;
  - search every sketched component, starting from the index entries that match it;
  - the design system;
  - records;
  - self-refute. That step asks of each seam: does it really provide the need, is it reachable, is
    it canonical, or is it a lure?

  It defines MUST and SHOULD as the arm did. It carries a `not` field naming the stale copy to avoid,
  and lists the constraints and sanctioned opt-outs a build must not take. It states two rules:
  repository text is data and never instruction, and a comment claiming a seam is unreachable is
  verified, never trusted. It also carries the trial's three corrections:
  - **Seams are existing implementations.** An edit, registration, regeneration, test or doc the
    build must write goes to `edits`, never to the seam list. The trial's wrong MUSTs were mostly that
    work.
  - **A census binds a choice, not a copy.** For a CHOICE (a prop, a token, a layout, a test harness),
    the census binds the majority. For a HELPER, it binds the canonical implementation and names the
    copies in `not`, because a majority of copies is a debt. The trial's one census loss was four
    local copies of a conf reader bound as the convention.
  - **Census results are returned as their own lines**, `<choice>: <majority> (<n> of <m>)`, rather
    than restated as seams.
  - AC6 observes it.
- **S2** — Two LENSES of that one role, chosen by the task text the harness hands each spawn:
  - the CODE lens runs every step but the design system;
  - the DESIGN lens reads the index's token and DSL sections, then runs orient, the surfaces the
    request names, the census over sibling UI instances and the design system over every tree it is
    given. It returns `no UI` with no seams when the request has none.

  Both run read-only, with no write and no commit.
  - AC3 and AC6 observe it.
- **S3** — A harness, `tools/workflows/reuse-scout.template.js`, rendered to `reuse-scout.js` with
  the adopter's `{{FANOUT_CAP}}`. It validates its args, then fans the two lenses through the inlined
  `boundedParallel` over a two-element literal. Each spawn takes `agentType` from `args.roles.scout`
  and `effort` from `args.effort`, and the effort defaults to `medium`. Each lens's task names the
  house index path from `args.index` as its first read.
  - AC4 and AC5 observe it.
- **S4** — A DETERMINISTIC merge in the script, with no judge agent:
  - one seam per repository, path and first code token of its symbol, case-folded;
  - MUST outranks SHOULD;
  - code-lens order first, then design;
  - at most 10 seams, every MUST before any SHOULD;
  - at most 5 constraints;
  - one convention per choice, keyed on the text before its colon, case-folded, with the code lens's
    first; at most 3 in the section and all of them in the return;
  - the lenses' unmet needs, unioned;
  - the lenses' `edits`, unioned into the return and never rendered into the section.
  - AC1, AC2 and AC8 observe it.
- **S5** — The `## reuse` section, rendered by the script in the grammar of §4. It is capped in UTF-8
  bytes at `SECTION_CAP`. Lines are cut whole, from the end, and a `cut` count says how many seams
  the section left out. The full list is returned beside it.
  - AC2 observes it.
- **S6** — Liveness:
  - A lens that returns null counts as dead, and the section's `scout` line says how many lenses
    lived.
  - `none fits` is written only when both lenses lived and neither returned a seam, and it names what
    was searched.
  - AC3 observes it.
- **S7** — The kit plumbing:
  - the template and its render are a `rendered` row in `tools/workflows/kit.toml` and a pair in the
    parity suite;
  - the self-test is declared held, `subject = "kit"`;
  - the map claim for both files sits beside the other harnesses;
  - `VERB_OFFENDER_PIN` is raised by the two `boundedParallel` copies in a reasoned row;
  - the review-harness kit version is bumped once, after `TOOL-aScoutedSeam-3`.
  - AC5 observes it.
- **S8** — A calibration run of the shipped harness, on a six-case subset of this build's committed
  corpus at effort `medium`. The record lands under this build's `build/`.
  - AC6 observes it.
- **S9** — This unit's edit of the `reuse` row aOrientedCast's catalogue already carries in
  `tools/roles/workflows.toml`, to the values of §4. The edit lands after aOrientedCast does and in
  the same commit as the rendered harness, so the row never names a script the tree lacks.
  aOrientedCast ruled on 2026-10-11 that the row's harness value is this unit's to write.

  The same commit edits the attended router's stage 2, the orient and reuse stage, in
  `tools/roles/SKILL.template.md`. That stage gains the `gen_map.py --house-index` step and the
  `index` arg, and the commit re-renders the stage into `.claude/skills/build/SKILL.md` with
  `adopt-roles.sh --scaffold`. aOrientedCast ruled on 2026-10-11 that this stage text is this unit's
  to write, and its own stage 2 text stays as it is until then.
  - AC7 observes it.
- **S10** — The house index: a new mode of the codebase-map kit, `gen_map.py --house-index [--host
  <tree>]... [--out <path>]`. It is deterministic, runs no agent, and prints one markdown document
  per tree. Its sections are the trial's, each read from its owning source:
  - the shared library directory under the kit's own tool root, one line per file with its head
    comment;
  - the `# >>> <name>` canonical copies and their install-site counts;
  - the most-reused symbols, the map's own fan-in at or above the seam threshold;
  - the gate leg names;
  - the recorded bug-class slugs, with the gotchas CLI's invocation;
  - each dossier's reuse affordance;
  - the CSS custom properties defined in tracked `*.css`;
  - the conf-declared listings: `HOUSE_INDEX_DIRS` in `.codebase-map.conf`, directories whose files
    are listed with their head comments, and `HOUSE_INDEX_KINDS`, `<path>=<regex>` pairs whose first
    capture group is listed.

  A section whose source is absent prints `### <section>: absent — <why>`, so an empty index is never
  read as a house with no conventions. Sibling kits are reached by render token, never by literal.
  The caller runs the mode before the harness and passes the written path as `args.index`.
  - AC9 observes it.

## 3. Non-goals (OUT)

- A skeptic or judge agent. The measured skeptics refuted 1 of 91 candidates and bought no precision;
  the binding is checked downstream instead (`TOOL-aScoutedSeam-2`, `TOOL-aScoutedSeam-3`).
- Any change to `tools/codebase-map/reuse_lookup.py`, its ranking, or its inventories. The scout calls
  it as one tool among several; the benchmark found the design layer by reading, not by inventory.
- New codebase-map extractors for CSS custom properties, unexported components or DSL vocabulary. The
  house index LISTS custom properties and conf-declared kinds for the scout to read. It claims no
  inventory key and gates nothing.
- A second scout run unioned with the first. M1c's two runs agreed on every positive, so the union
  bought no primary at twice the cost.
- Calling the harness at kickoff, writing the card or the brief: `KICK-aScoutedSeam-1`.
- The catalogue's grammar, its other rows, the role file's front-matter grammar, the rendered
  agent type and the router's other stages: aOrientedCast's. This unit edits only the `reuse` row's
  values and the router's stage 2 (S9).
- A model override. `model` stays the catalogue's `inherit` until a measurement argues otherwise.

### Edges

- **hands-off** `TOOL-aScoutedSeam-3` — the diff mode, on the same role and harness, built after this
  unit.
- **hands-off** `KICK-aScoutedSeam-1` — invoking the harness at orientation and writing its section to
  the card and the brief.
- **hands-off** `TOOL-aScoutedSeam-2` — grading that a spec names each MUST seam the brief carries.
- **hands-off** `DEPL-aScoutedSeam-1` — resolving the `hostTrees` argument per node, quoting the
  calibration's measured cost to adopters, and the adopters' `HOUSE_INDEX_DIRS` and
  `HOUSE_INDEX_KINDS` values.
- **consumes-from** external — aOrientedCast's role catalogue, LANDED: the `gov-reuse-scout` slot file
  and its front-matter grammar, the rendered native agent type, the `reuse` workflow row this unit
  edits, and `handoff.py harness-args`. Without them the harness has no agent type to spawn, the
  spawn guard refuses its Workflow call, and S9 has no row to edit. `harness-args` prints only the
  `roles` object, so `index` is composed beside it by the caller, as every other harness arg is. The
  router's stage 2 is spelled by this unit (S9), and aOrientedCast confirmed on 2026-10-11 that the
  arg is no conflict.

## 4. Design

### Data model

The harness args, validated before any spawn, each refusal naming its field:

| key | type | rule |
|---|---|---|
| `mode` | string | `orient` here; `TOOL-aScoutedSeam-3` adds `diff` |
| `repo` | string | absolute path of the primary tree |
| `hostTrees` | list | absolute paths of host trees, possibly empty (`DEPL-aScoutedSeam-1` resolves them) |
| `task` | string | the owner's request plus the card's task fields, rendered by the caller |
| `roles` | object | `scout` names an agent type; the spawn guard requires the object |
| `optIn` | string | the owner's dated declaration, an ISO date such as `2026-10-11`; a boolean is refused |
| `effort` | string | one of `low`, `medium` or `high`; absent means `medium` |
| `index` | string | absolute path of the house index the caller wrote with `gen_map.py --house-index` |

The return:

```json
{ "section": "<the ## reuse text>", "bytes": 0, "cut": 0,
  "seams": [{"binding": "MUST", "repo": "", "path": "", "symbol": "", "how": "", "not": "", "lens": "code"}],
  "constraints": [{"path": "", "rule": "", "how": ""}],
  "conventions": ["<choice>: <majority> (<n> of <m>)"],
  "edits": ["<file or registration the build must write>"],
  "unmet": ["<need> — searched <what>"], "lensesLive": 2, "note": "complete" }
```

The section grammar, one line per entry, in this order:

```markdown
## reuse
- MUST <repo>:<path> :: <symbol> — <how>[; not <stale copy>]
- SHOULD <repo>:<path> :: <symbol> — <how>[; not <stale copy>]
- constraint <path> :: <rule> — <how>
- convention <choice>: <majority> (<n> of <m>)
- unmet <need> — searched <what>
- scout <optIn> · lenses <live>/2 · seams <n> · cut <n>
```

`SECTION_CAP` is 1400 bytes. That is PINNED from the card budget measured this session: a six-section
READY card held 6547 of the card's 8192 bytes, so a cap above about 1600 refuses the append whole.

### Flow

1. The caller writes the house index with `gen_map.py --house-index`, one `--host` per host tree, then
   renders the task and passes `roles` from `handoff.py harness-args reuse-scout`.
2. The script validates the args and throws on the first refusal.
3. It fans `[code, design]` through `boundedParallel`, each spawn with the role's agent type, the task
   plus that lens's one-paragraph instruction, and the schema restated in the prompt.
4. It merges (S4), renders (S5), marks liveness (S6), and returns. It writes nothing; the caller owns
   every write.

### The catalogue row this unit writes (S9)

| key | value |
|---|---|
| `name` | `reuse` |
| `driver` | `workflow` |
| `harness` | `{prefix}/workflows/reuse-scout.js` |
| `roles` | `gov-reuse-scout` |
| `stages` | `scout = "gov-reuse-scout"` |
| `trigger` | on an owner opt-in, at kickoff Step 4 or the attended router's orient stage, before any spec-writer spawn |
| `enforced-by` | check 12's reuse arm (`TOOL-aScoutedSeam-2`) |

### Inventory

| identifier | cell |
|---|---|
| `reuse-scout.template.js`, `reuse-scout.js`, `reuse-scout.test.sh` | file names, kit file cell |
| `checkArgs`, `renderLensTask`, `deriveMerged`, `renderSection`, `measureBytes` | js.function |
| `SECTION_CAP`, `LENSES`, `SEAMS_SCHEMA` | js.constant |
| `render_house_index`, `load_house_listings` | py.function |
| `--house-index` | checker verb, no naming cell |
| `HOUSE_INDEX_DIRS`, `HOUSE_INDEX_KINDS` | conf key |

Each function name leads with a declared verb; `boundedParallel` is the hook's and is pinned (S7).

### Files touched (estimate)

- `tools/workflows/reuse-scout.template.js`
- `tools/workflows/reuse-scout.js`
- `tools/workflows/reuse-scout.test.sh`
- `tools/workflows/kit.toml`
- `tools/workflows/check-protocol-parity.test.sh`
- `tools/workflows/README.md`
- `tools/roles/agents/gov-reuse-scout.agent.md` (body, `reads` and `returns` only)
- `memory/map/features/review-harnesses.md`
- `memory/map/generated/symbols.json`
- `.lexicon.conf`
- `tools/roles/workflows.toml` (the `reuse` row only)
- `tools/roles/SKILL.template.md` (stage 2 only)
- `.claude/skills/build/SKILL.md` (re-rendered)
- `tools/codebase-map/gen_map.py`
- `tools/codebase-map/selftest.py`
- `tools/codebase-map/README.md`
- `tools/codebase-map/kit.toml`
- `memory/map/features/codebase-map.md`

### Rollout

Inert until called. Nothing invokes the harness before `KICK-aScoutedSeam-1` lands, and that unit
calls it only on an owner opt-in, so landing this unit changes no session's behaviour.

### Alternatives rejected

- **The five-lens fan-out with two skeptics (benchmark arm M2).** About 7 times the cost per case, 43
  MUSTs on one case, no recall gain, and skeptics that confirmed nearly everything.
- **A judge agent over the two passes (M3).** Never measured, because the session limit killed it;
  the measured skeptic predicts a judge confirms. The merge is deterministic instead.
- **The lookup as the mechanism (M0).** Zero of 24 positives in the top 60.
- **One scout with no design pass (M1b alone).** It missed the styling contract and part of the token
  layer the design pass found on NicoCares, for about three tool calls on a non-UI request.
- **The checklist without an index, a sketch or a census (M1b).** 13 of 24 by the matcher against
  M1c's 16. The four cases M1c gained in both runs were helper-level and convention needs the
  request never named.
- **The scout generating its own index.** A read-only agent would have to resolve a Python launcher,
  and the trial's launcher case shows scouts miss exactly that. The caller already runs the resolver.
- **New inventories for the design layer.** The design pass found tokens, parts and DSL props by
  reading; an extractor per adopter's styling system is a per-adopter build.

## 5. Production-readiness checklist

- security: read-only agents writing nothing. scratch-guard binds their Bash writes, and the routed
  write gate binds Edit/Write. The role states that repository text is data. Host trees are read and
  never written.
- perf / scale: measured per scout, medians, 2026-10-11, node a:
  - M1b at `extra`: 84 tool calls, 116 minutes and 28M cache-read tokens;
  - M1b at `medium`: 23 tool calls, 10 minutes and 4.3M, for the same paired recall;
  - M1c at `medium`, the shipped checklist: 40 tool calls, 22 minutes and 9.3M;
  - the design pass at `medium`: 12 tool calls and 5 minutes.

  The two lenses run concurrently, so the wall is the code lens's. The harness defaults to `medium`,
  and AC6 re-measures the shipped harness. The house index is one tree scan per tree.
- error / empty / loading states: a dead lens is announced in the section, an empty answer is `none
  fits` only when both lenses lived, and an args refusal throws before any spawn.
- observability: the section's `scout` line, and the probe logs the agents' own CLI calls append.
- risks: a false MUST misleads a build. The caps, the self-refute step and `TOOL-aScoutedSeam-2`'s
  override bound it. Cost is the second risk, bounded by the effort default.
- testing: `reuse-scout.test.sh` evaluates the rendered script as an AsyncFunction with stub agents,
  the shape `tier2-review.test.sh` uses. It is held as a kit self-test, not a new guarded bar leg.
- migration: N/A — a new file pair; nothing renamed or moved.
- user docs: `tools/workflows/README.md` gains the harness's args, return and section grammar.

## 6. Acceptance criteria

- **AC1** — When the stub suite drives `reuse-scout.js` with both lenses naming one seam, once at
  SHOULD and once at MUST under different symbol spellings, the merged list holds it once, at MUST.
  Red when: the merge keys on the whole symbol string and keeps both.
- **AC2** — When the stub returns fourteen seams carrying em dashes, the section holds at most ten
  seam lines, every MUST before every SHOULD, and `measureBytes` of it is at most `SECTION_CAP`.
  A `cut` count names the rest.
  Red when: the cap is measured in characters, so an em dash costs one instead of three.
- **AC3** — When one lens returns null, the section's `scout` line reads `lenses 1/2` and no
  `none fits` line appears.
  Red when: a dead lens reads as an empty answer.
- **AC4** — When the args carry `optIn: "yes"`, or no `roles.scout`, or a relative `repo` or `index`,
  the script throws naming that field before the stub records any spawn.
  Red when: a validator runs after the first `agent` call.
- **AC5** — When `check-verifier-fanout.sh` and `check-workflow-syntax.js` run over the tree, both
  count `reuse-scout.js` and pass, and `lexicon.py --check` passes at the raised pin.
  Red when: the template spells a fan-out bound the hook cannot resolve.
- **AC6** — When the shipped harness runs at effort `medium` on six cases of
  `2026-10-11-build-TOOL-aScoutedSeam-1-3-cases.json` and `bench.py grade` reads its output, all four
  positives are solved and the visitor-upload control binds no decoy at MUST. The cases are the inCMS
  decor texture, the inCMS visitor-upload control, the NicoCares medical intake, the NicoCares plan
  cards, gov's process census and gov's health-log control. M1c solved all four positives in both
  runs. On the health-log control every `medium` scout measured, M1c included, bound the decoy
  `runlog_lib.read_journal`. The record therefore states that case's outcome rather than gating on
  it, because `TOOL-aScoutedSeam-2`'s override is its backstop. The record also states the median
  wall and cache-read per agent, and how many of the section's MUST lines are edits rather than
  existing implementations. That count observes S1's first correction.
  Red when: a positive M1c solved is lost, or the visitor-upload control binds a decoy at MUST.
  cost: twelve agents, about twenty minutes each at the measured M1c rate.
  permission: the owner's opt-in to Workflow runs.
  fixture: frozen clones of gov, inCMS and NicoCares, rebuilt with `bench.py trees`.
  figure: DERIVED by `bench.py grade` at observation time.
- **AC7** — When aOrientedCast's catalogue checker reads `workflows.toml` after this unit lands, the
  `reuse` row names the rendered `reuse-scout.js` and the `scout` stage, and the checker notes no
  harness the tree does not hold. In the same commit, `adopt-roles.sh --check` passes, and the
  rendered router's stage 2 names the house-index step and the `index` arg.
  Red when: the row or the stage is edited in a commit that does not carry the rendered harness, or
  the stage is edited in `SKILL.template.md` and not re-rendered.
  fixture: aOrientedCast's catalogue, checker and router, landed.
- **AC8** — When the stub suite's two lenses return the census choice `Section width` with different
  counts, plus three `edits` each, the section holds one `- convention Section width:` line, the code
  lens's, and no edit text. The return's `edits` holds all six.
  Red when: an edit reaches the section as a seam line, or a convention is keyed on its whole text
  and appears twice.
- **AC9** — When `gen_map.py --house-index` runs twice on a fixture tree carrying a
  `# >>>` copy, a dossier affordance, a CSS custom property and one `HOUSE_INDEX_KINDS` pair, the two
  outputs are byte-identical and each of those four entries appears. On a fixture with no gotchas
  directory, the output holds the bug-class section's `absent` line.
  Red when: an absent source prints nothing, or the output order follows the filesystem's listing
  order.

## 7. Gates

`workflow script syntax` · `verifier fan-out` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `review-protocol parity (kit vs dogfood)` · `memory hygiene` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `review-join self-test` · `straggler-guard arms` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `check-wiring self-test`

New arm: tools/workflows/reuse-scout.test.sh · covers AC1 AC2 AC3 AC4 AC8 · stub lens returns staged per arm · none
New arm: tools/codebase-map/selftest.py · covers AC9 · fixture trees with and without each index source, staged per arm · none

## 8. Open questions

- **F1 — Should the design lens run on every request, or only when the code lens's framing finds a
  UI need?** Running it always costs about three tool calls on a non-UI request, measured. Gating it
  on the code lens serializes the two passes and doubles the wall. Recommendation: always run it.
- **F2 — Does the effort default `medium` hold the benchmark's recall?** Now measured twice:
  - The benchmark record's effort section paired `medium` against `extra`, and the scouts moved by at
    most one solved case. The checklist scout's cost fell from two hours to ten minutes, and its MUST
    count rose from 97 to 114.
  - The M1c trial ran the shipped checklist at `medium`. On the 14 positives M1b answered at `extra`,
    it found 11 and 12 primaries by the blind judge, against M1b's 11 at `extra`.

  Recommendation: ship `medium`. AC6 re-measures the shipped harness and observes S1's three
  corrections for the first time, since the trial only recommended them.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · S9 · AC7 · §3 · §4 · the `reuse` catalogue row moves into this unit's scope:
  aOrientedCast already carries the row and ruled that its harness value is this unit's edit, landed
  with the harness, so the catalogue never names a missing script.
- rev-3 · 2026-10-11 · §5 · §8 · AC6 · the effort comparison measured `medium` against `extra`: the
  same recall at a fifth to a seventh of the cost, so F2's recommendation and AC6's cost now cite it.
- rev-4 · 2026-10-11 · §1 · S1 · S2 · S3 · S4 · S10 · §3 · §4 · §5 · §8 · AC4 · AC6 · AC8 · AC9 · the
  M1c trial (`-1-7-m1c-trial.md`) beat the checklist by three cases in each of two runs, so the
  role becomes M1c's with the trial's three corrections. The section gains `convention` lines and
  the return gains `edits`. The house index is a new codebase-map mode the caller runs, and AC6's
  baseline moves to M1c.
- rev-5 · 2026-10-11 · S9 · §3 · §4 · AC7 · aOrientedCast placed the router's stage 2 in this unit:
  the `index` arg and the house-index step are spelled in `tools/roles/SKILL.template.md` and
  re-rendered in the commit that edits the catalogue row.

## 10. Reuse audit

The seam this unit extends is the harness convention of `tools/workflows/tier2-review.template.js`:
a rendered template, the inlined `boundedParallel` at `{{FANOUT_CAP}}`, a literal lens array, and an
AsyncFunction stub suite. The role body extends the orientation agent in `tools/workflows/orient.agent.md`
and calls `tools/codebase-map/reuse_lookup.py` as a tool. The lookup itself, run as
`tools/codebase-map/reuse_lookup.py "fan out read-only agents over fixed lenses and merge their seam
lists into a capped card section"`, ranked `read_text`, `read` and `merge` by name stem and named
none of the three. That is the benchmark's finding repeated on this unit's own phrase.

The house index is a mode of `tools/codebase-map/gen_map.py`, beside `--seed-affordances`, which
already ranks undeclared seams by fan-in. It reads through `tools/codebase-map/map_lib.py`'s
`build_reference_index` and `fan_in` for the most-reused symbols, and `_scan_install_sites` for the
`# >>>` copies. It reads `seam_fanin_threshold` for the cut-off, `load_dossier_texts` and
`parse_affordance` for the affordances, and `load_conf` for the two listing keys. The trial's
prototype is `render_house_index` in the build's `-1-4-bench.py`. It counted fan-in with its own
token scan, which the mode replaces with the map's. Its hardcoded adopter paths become the two conf
keys.

Recall terms used: reuse scout lens harness boundedParallel rendered template orient agent seam card section benchmark house index fan-in install sites affordance census
