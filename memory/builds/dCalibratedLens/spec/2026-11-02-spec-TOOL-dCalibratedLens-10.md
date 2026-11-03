# TOOL-dCalibratedLens-10 — instruction evals: a replay suite of recorded items with known outcomes, scored through the scorer factory, owed again by a held leg when an instruction unit changes

**Status:** DEFERRED · rev-4 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 12 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0467@0bd9d49f whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-10-deviation-101.md](../build/2026-11-02-build-TOOL-dCalibratedLens-10-deviation-101.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-token-fix-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-14 |

<!-- /gen:spec-records -->

## 1. Goal

A change to the charter, a role file, a Skill or a hook pack's text is never replayed against recorded
tasks (gap-review-14). This unit lands instruction evals: a replay suite of recorded items with known
outcomes, each a case file in TOOL-dFairHearing-1's known-set grammar, scored through dFairHearing's scorer
factory as its `instruction-eval` instance; a held leg, guarded by the instruction units' files, that
re-runs the suite when one changes and reds every case whose replay the change has made owed or whose
score fell; and a confirmed finding whose cause is an instruction adding a case (night pass, point 6, S2).

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`, re-grounded by the build run, which
stops this unit when one is absent: TOOL-dFairHearing-12 (`tools/workflows/replay_scorer.py`,
`INSTANCES`, `read_raw_output`, `derive_paired_cases` and its arms in `review-replay selftest`),
TOOL-dFairHearing-1 S1 to S3 (the known-set grammar, `parse_known_set`, the adjudicated `--matched`
scoring) and TOOL-dFairHearing-25 (the owed replays' verdict record the seed case reads);
TOOL-dCalibratedLens-5 (the appendix's `units` column, `read_finding_units` and `PROPOSERS`);
PLAY-dOrderedCharter-9 (the instruction manifests, `instructions.toml`).

- **S1** — The case. A case is one file under `tools/workflows/evals/`, its header the lines of §4 "The
  case" and its known outcomes either a `**Known:**` line naming a known-set source or its own
  `**Population:**` line and `| tag | address | grade | escaped |` rows, both read by
  `parse_known_set` (TOOL-dFairHearing-1 S2). `parse_eval_case(text, repo)` in the factory returns the
  header and the rows, reading a `**Known:**` source through `read_raw_output`, and refuses a missing or
  malformed header line by name. Observed by AC1.
- **S2** — The score and its record. `measure_instruction_eval(case, candidate, matched)` scores a
  replay's candidate report through TOOL-dFairHearing-1 S3's adjudicated matches: an `**Expect:**
  found` case scores the known rows matched, an `**Expect:** absent` case the known rows NOT matched,
  each as `<k>/<n>`. `python replay_scorer.py --instance instruction-eval --record --case <path>
  --candidate <src> --matched <src>` writes the score into the case's `**Replayed:**` line with `HEAD`'s
  sha and the candidate's source, and raises `**Baseline:**` to the score when it is higher, through a
  temp file and `os.replace`; it writes nothing else. Observed by AC2.
- **S3** — (amended, id 8) The check. `check_eval_suite(suite, guard, repo)` reads every case under `suite` and prints
  one line per case, `instruction-eval — <case> · <verdict> · <detail>`: `owed` when `**Replayed:**` is
  `none`, or when `git diff --name-only <replayed sha> HEAD -- <the case's Loads>` names a path, the
  detail naming those paths and the README section that runs a replay; `fell` when the replayed score is
  below `**Baseline:**`; `held` otherwise. It reds a case's `**Loads:**` path outside the guard
  (`unguarded`) and every tracked `instructions.toml` the guard lacks (`guard misses <path>`), and an
  empty suite prints `instruction-eval — unarmed · no case under <suite>`, never a pass. Exit 0 only when
  every case is held and nothing else red; 1 otherwise; 2 on a refusal. Observed by AC3 and AC4.
- **S4** — (amended, id 41) The held leg. A row `instruction-eval` in `tools/gate-legs.json`: argv `["python3",
  "{prefix}/workflows/evals/check_evals.py"]`, `subject = "kit"`, `chunk = "selftests"`, and the guard of §4
  "The guard". `tools/workflows/evals/check_evals.py` runs `check_eval_suite` over its own directory with
  the guard it reads from that row by name, so the guard is one fact. `tools/workflows/kit.toml`'s
  `project-owned` rule (`:36-37`) gains `evals/**`, withholding the suite and its entry from every
  adopter, and `silenced_legs` (`tools/govkit/govkit.py:3842`) leaves the leg out of an adopter's manifest with them; the leg is an
  `[[exempt_leg]]` row of `tools/govkit/registry.toml` in the form `tier2-review self-test`'s takes, and
  `memory/map/features/review-harnesses.md` claims it. Because no kit ships its entry, `GATE_SELFTESTS=changed`
  selects it by its guard (`tools/run-gates/run-gates.sh:3075-3080`, §8 F1). Observed by AC5.
- **S5** — (amended, id 4) The seed case, `tools/workflows/evals/design-audit-runtime-record.md`: the design-audit replay
  of the runtime record at blob `767187aa` (TOOL-dFairHearing-1 S5), `**Known:**` that unit's known set,
  `**Expect:** found`, its `**Replayed:**` and `**Baseline:**` the reviewed score TOOL-dFairHearing-25's
  verdict record states for that replay, or `none` and `0/59` when no adjudicated score is recorded.
  (r2 id 6) Its `**Loads:**` line is `tools/workflows/tier2-review.template.js,
  tools/workflows/lenses.toml, tools/roles/agents/gov-spec-reviewer.agent.md,
  tools/roles/agents/gov-skeptic.agent.md, tools/roles/agents/gov-synthesizer.agent.md,
  coding-governance-agents.template.md`, the files a design audit's agents load, each inside §4 "The
  guard". Observed by AC6.
- **S6** — A case added from a finding. `python replay_scorer.py --instance instruction-eval --add-case
  --from <review record> --finding <id> --brief <src> --loads <path>[,<path>]` runs
  `derive_eval_case(...)` and writes `tools/workflows/evals/<record stem>-<id>.md` with `**Expect:**
  absent`, one known row built from the finding (§4 "A case from a finding"), `**Baseline:** 0/1` and
  `**Replayed:** none`. It refuses a finding whose appendix row is not `confirmed`, one whose `units` cell
  is `-` (no instruction is its cause, TOOL-dCalibratedLens-5 S2), and a finding a case's `**From:**`
  already names. Observed by AC7.
- **S7** — The Loop Review finds them. `derive_eval_proposals` joins `PROPOSERS` (TOOL-dCalibratedLens-5
  S6): for each confirmed finding in the window whose `units` cell names a tag, read through
  `read_finding_units`, and that no tracked case's `**From:**` names, one proposal `{"kind":
  "eval-case", "id": "<record stem>#<id>", "action": "add-case", "accept": …, "row": "<units> ·
  <ref>"}`, its `accept` the case added by S6's command or the finding kept by a keep record; a
  `METRICS` entry `eval-candidates` answers `<n> finding(s) · <m> case(s) · <glob>`. Observed by AC8.
- **S8** — The docs. `tools/workflows/README.md` gains "Instruction evals": the case grammar, the leg,
  the replay procedure (the item run in an isolated clone at `**Base:**` as TOOL-dFairHearing-1 S5 runs
  its replay, the output reviewed by `tier2-review.js`, the matches adjudicated, then `--record`) and
  `--add-case`; `help/roles.md` gains "When an instruction changes". Observed by AC9.

## 3. Non-goals (OUT)

- Running a replay inside the leg. A replay is a role agent's item and a review of its output, which the
  bar cannot launch; the leg reds and names the replay owed (§8 F2, deviation 101).
- The scorer, the known-set grammar and the adjudication: TOOL-dFairHearing-12 and -1. This unit adds an
  instance and reads both.
- Choosing when held legs run: `verdict.held` (`tools/policy/catalogue.toml`, owner dWitnessedBar).
- Per-unit staleness. A case owes a replay when a file it loads moves, not when a unit's text moves
  (§4 "The guard", `ponytail:` ceiling).
- Pricing the suite in the value ledger: its leg is a `leg` row of TOOL-dCalibratedLens-2 like any other.
- The `units` citation itself: TOOL-dCalibratedLens-5.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-5` — the appendix's `units` column, which marks a finding's cause an instruction, `read_finding_units`, and `PROPOSERS`, which gains `derive_eval_proposals`
- **consumes-from** `TOOL-dCalibratedLens-3` — `METRICS` and `run_loop_file`, through which the proposal is filed
- **consumes-from** external — TOOL-dFairHearing-12, -1 and -25 (the factory, the known-set grammar and adjudicated scoring, the seed's verdict) and PLAY-dOrderedCharter-9 (the instruction manifests), each DEFERRED at base and of a parent or ancestor build
- **hands-off** `TOOL-dCalibratedLens-23` — `check_evals.py`, the seed case and `replay_scorer.py --record`, which that unit observes held and owed (id 4)
- **hands-off** `TOOL-dCalibratedLens-36` — the seed case and the `--fixture` frame of `replay_scorer.py --instance instruction-eval`, which that unit's `seed-loads` plant copies (round-2 id 6)

## 4. Design

**Waits on:** TOOL-dFairHearing-12, TOOL-dFairHearing-1, TOOL-dFairHearing-25, TOOL-dCalibratedLens-5,
TOOL-dCalibratedLens-3 and PLAY-dOrderedCharter-9; none exists at `8bec4cef`
(`tools/workflows/replay_scorer.py`, `tools/workflows/evals/` and every `instructions.toml` are absent).

### Evidence

- A held leg's `changed` selection: "the owner is every govkit entry whose `shipped` rows carry one of
  the leg's suite files ... A leg no entry owns ... selects by its guard plus its suite file"
  (`tools/run-gates/run-gates.sh:3075-3080`). `python tools/govkit/govkit.py shipped --epoch` lists
  `tools/workflows/review_replay.py` under `review-harness` and does not list the withheld
  `tools/workflows/tier2-review.test.sh`, so a leg whose argv names a withheld file is selected by its
  guard, and one naming `replay_scorer.py` by the kit's shipped sources (§8 F1).
- A gov-only leg is a `gate-legs.json` row plus an `[[exempt_leg]]` row, never a `[[gate_leg]]`
  (`tools/govkit/registry.toml:666-668`, the `tier2-review self-test` row), and the kit withholds its
  suite by claiming it `project-owned` (`tools/workflows/kit.toml:36-37`).
- The review harness's design-audit replays cost a full spec audit each, about 0.81 M tokens and 11 or 12
  agents (gap-review-03, PINNED by the gap register); that is why the leg owes a replay rather than
  running one.

### The case

```markdown
# Eval — a skipped recall probe in a spec writer's §10

**Item:** item.design.spec
**Subject:** memory/builds/dExample/spec/2026-10-30-spec-TOOL-dExample-3.md
**Base:** <40-hex sha the item ran at>
**Brief:** <commit>:<path of the brief the item ran from>, or `-` for a review item
**Expect:** absent
**Loads:** tools/roles/agents/gov-spec-writer.agent.md, coding-governance-agents.template.md
**From:** memory/builds/dExample/reviews/2026-10-31-review-TOOL-dExample-3-spec-audit.md#7
**Baseline:** 0/1
**Replayed:** none

**Population:** 1 · reviewed 1 · escaped 0 · high 1

| tag | address | grade | escaped |
|---|---|---|---|
| 2026-10-31-review-TOOL-dExample-3-spec-audit-7 | memory/builds/dExample/spec/2026-10-30-spec-TOOL-dExample-3.md:[§10] | high | no |
```

`**Replayed:**` once scored reads `<40-hex sha> · <k>/<n> · <candidate src>`. `**Known:** <src>` replaces
the `**Population:**` line and the table where the known set lives elsewhere, as the seed's does.
`**Loads:**` lists the files whose text the item's agents and its review's agents load. `**From:**` is
`seed` for a case not added from a finding.

### Scoring

| `**Expect:**` | The replay is | Score `<k>/<n>` counts |
|---|---|---|
| `found` | a review of the subject at `**Base:**` | known rows the review's adjudicated matches name |
| `absent` | the item re-run from `**Brief:**` at `**Base:**`, then reviewed | known rows NOT among the adjudicated matches |

One rule judges both: a replay that scores below the case's best recorded score, `**Baseline:**`, fell.

### The guard

The leg's guard, each a path the build run finds tracked, and checked both ways by S3: every tracked
`instructions.toml` (PLAY-dOrderedCharter-9's kit manifests, listed with `git ls-files --
'*instructions.toml'` at the build run) and `.governance/instructions.toml`;
`coding-governance-agents.template.md`; `tools/roles/agents/`; `tools/hooks/`; every tracked
`SKILL.template.md` and `skills/session-kickoff/`; `tools/workflows/tier2-review.template.js`,
`tools/workflows/unattended-build.template.js` and `tools/workflows/unattended-unit.js`. The guard selects
the leg; each case's `**Loads:**` decides which cases a change owes. `ponytail:` a moved file owes every
case that loads it, whichever unit in it moved; per-unit pins are the upgrade once a unit hash has a
reader outside the playbook kit.

### A case from a finding

The appendix row (TOOL-dFairHearing-8 S8's columns and TOOL-dCalibratedLens-5 S2's `units`, read by
header name): `tag` is `<record stem>-<id>`; `address` the row's `ref`; `grade` `high` for a `blocker` or
`high` severity and `medium` otherwise; `escaped` `no`. `**Subject:**` is the path of the row's `ref`,
`**Base:**` the commit that added the review record (`git log --diff-filter=A --format=%H -1 --
<record>`), `**Item:**` the item that wrote the subject as `--brief`'s record names it, and `**Loads:**`
the `--loads` paths, each within the guard. The file name is built from the record's stem and an id
held to `^[0-9]+$`, so no argument is a path.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `instruction-eval` | `INSTANCES` key, leg name | none |
| `parse_eval_case`, `measure_instruction_eval`, `check_eval_suite`, `write_eval_case`, `derive_eval_case` | functions, `tools/workflows/replay_scorer.py` | `parse`, `measure`, `check`, `write`, `derive`, each answered OK by `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at base |
| `derive_eval_proposals`, `read_eval_candidates` | functions, `tools/loop/loop_review.py` | `derive`, `read`, OK at base |
| `--record`, `--add-case` | `replay_scorer.py` flags under the instance | none |
| `tools/workflows/evals/`, `check_evals.py` | the suite and its entry | none |
| `held`, `owed`, `fell`, `unguarded`, `unarmed` | verdicts | none |
| `eval-case`, `add-case`, `eval-candidates` | proposal kind and action, `METRICS` name | none |

### Amendments (round-1 spec audit)

The round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Each bullet supersedes the text it
names; the unit it names owns the finding and its proof.

- **id 4 · S5, AC6 (H5, `TOOL-dCalibratedLens-23`)** — The seed's `**Replayed:**` and
  `**Baseline:**` are the adjudicated score TOOL-dFairHearing-25's verdict record states for the
  design-audit replay of the runtime record, a build-run precondition; the value none is not
  admitted at landing, and AC6 reds on `owed`. The later units that edit a guard path,
  TOOL-dCalibratedLens-8 and -1, owe one replay, recorded by the main loop after the last of them
  builds and before the close bar.
- **id 8 · §4 "The guard", S3 (M4, `TOOL-dCalibratedLens-30`)** — The guard gains
  `tools/workflows/lenses.toml`, and S3's both-ways check reds every tracked file declaring
  instruction units that the guard lacks, `lenses.toml` among them, not only `instructions.toml`.
- **id 41 · S4, Files touched, §7 (M21, `TOOL-dCalibratedLens-30`)** — The held leg ships with its
  measured row in `tools/run-gates/selftest-budgets.txt`, its subject pin in
  `tools/govkit/subject-pins.tsv` regenerated by `govkit.py selfcheck --write`, and its evidence row
  in `tools/run-gates/ceiling-evidence.txt`, as `tier2-review self-test` has.

### Amendments (round-2 spec audit)

The round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Its ids restart at 1, so each bullet
spells `r2 id`; each supersedes the text it names, and the unit it names owns the finding and its
proof.

- **r2 id 6 · S5 (H3, `TOOL-dCalibratedLens-36`)** — The seed case states its `**Loads:**`, the six
  paths S5 now names, so which edits owe it is decidable from the case; `TOOL-dCalibratedLens-36`'s
  `seed-loads` plant proves an edit outside them leaves it held and an edit inside owes it.

### Amendments (round-3 spec audit)

The round-3 spec audit
(`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`) confirmed the
findings below, and its disposal amended this text. Its ids restart at 1, so each bullet spells
`r3 id`; each supersedes the text it names, and the unit it names owns the finding and its proof.

- **r3 id 2 · AC6, id 4's bullet (M1, `TOOL-dCalibratedLens-48`)** — The seed is already owed when
  this unit lands, because unit 5 (order 11) edits two of its loads after the replayed sha. At this
  unit's order AC6 accepts `owed` naming the paths unit 5 moved, and red on `owed` applies only at the
  close, after the main loop records the one replay (`TOOL-dCalibratedLens-23` S2 and AC2). The id-4
  bullet's "AC6 reds on `owed`" reads at the close and nowhere else.
- **r3 id 3 · id 4's bullet (M2, `TOOL-dCalibratedLens-48`)** — The units that edit the seed's loads,
  and so owe the one replay, are `TOOL-dCalibratedLens-5` and `TOOL-dCalibratedLens-1`;
  `TOOL-dCalibratedLens-8` edits a guard path the seed does not load and owes it nothing.
- **r3 id 13 · S5, §4 "The guard" (M7, `TOOL-dCalibratedLens-48`)** — The seed's `**Loads:**` names the
  three audit agents in their rendered form, `.claude/agents/gov-spec-reviewer.md`,
  `.claude/agents/gov-skeptic.md` and `.claude/agents/gov-synthesizer.md`, in place of their
  `.agent.md` sources: the rendered file is what an agent loads, and it carries the source, the roles
  policy's `effort:` line and the charter blocks `tools/roles/render_agents.py` builds it from. The
  guard gains `.claude/agents/`, a pathspec check 7c classes `verbatim-repo-root`, so each load stays
  inside the guard and S3's `unguarded` red does not fire.
- **r3 id 31 · S3 (M14, `TOOL-dCalibratedLens-48`)** — The owed rule reads the working tree: a case is
  `owed` when `git diff --name-only <replayed sha> -- <the case's Loads>` names a path, staged or
  not, or `git ls-files --others --exclude-standard -- <the case's Loads>` names an untracked one. A
  bar run on a tree with an uncommitted edit to a loaded path reads `owed` for the bytes it reads,
  never `held` for bytes the replay never saw.

### Files touched (estimate)

- `tools/workflows/replay_scorer.py` (S1 to S3, S6, the fixture plants)
- `tools/workflows/evals/check_evals.py` (S4, new)
- `tools/workflows/evals/design-audit-runtime-record.md` (S5, new)
- `tools/workflows/kit.toml` (S4)
- `tools/workflows/README.md` (S8)
- `tools/gate-legs.json` (S4)
- `tools/govkit/registry.toml` (S4)
- `memory/map/features/review-harnesses.md` (S4)
- `tools/loop/loop_review.py` (S7)
- `help/roles.md` (S8)
- `tools/run-gates/selftest-budgets.txt`, `tools/govkit/subject-pins.tsv` and `tools/run-gates/ceiling-evidence.txt` — the held leg's budget, pin and ceiling evidence (id 41)

### Alternatives rejected

- **The leg's argv naming `replay_scorer.py`.** The probe of §8 F1: the review harness ships that file,
  so `changed` would select the leg by the kit's sources and an `instructions.toml` change would hold it.
- **An unheld leg.** It would run on every bar that touches the guard, and the clause names a held leg.
- **A case per review record, the whole record its known set.** A record's findings are mostly not an
  instruction's doing; `units` is what marks the ones that are, so a case holds those alone.

## 5. Production-readiness checklist

- security — `--add-case` and `--record` write only under the suite, through temp files, from validated
  ids and paths; the check runs git with argument lists and reads committed bytes; nothing reaches a
  shell.
- perf / scale — the check is one `git diff --name-only` per case and one manifest read, seconds; the cost
  is the replay, owed only by a change to what a case loads.
- error / empty / loading states — an empty suite is `unarmed` and red; a case missing a header line is
  refused by name; a `**Replayed:**` sha git cannot resolve is `owed`, never `held`.
- observability — one verdict line per case and a count line; `owed` names the moved paths and the
  README section that runs a replay.
- risks — the leg reds on an instruction change until someone replays (the deviation's risk); a replay
  costs a review's tokens, so a broad `**Loads:**` makes evals expensive, which the case author narrows.
- testing — §6's plants and §7's arms.
- migration — none: new files, a new instance and a new leg.
- user docs — `help/roles.md` and the kit README (S8).

## 6. Acceptance criteria

- **AC1** — When `python tools/workflows/replay_scorer.py --instance instruction-eval --fixture --plant
  case-grammar` parses a case holding its own known rows and a case whose `**Known:**` names a known set,
  both return their rows; a case lacking `**Expect:**` is refused naming the line.
  Red when: a case with no `**Expect:**` parses, which would score it under neither rule.
- **AC2** — When the plant `record` scores a `found` case of three rows against a candidate whose
  adjudicated matches name two, `--record` writes `· 2/3 ·` into `**Replayed:**` and raises
  `**Baseline:**` from `1/3` to `2/3`; an `absent` case of one row whose row is matched scores `0/1` and
  leaves its baseline.
  Red when: an `absent` case counts the matched row as a pass, or the baseline falls.
- **AC3** — When the plant `suite` holds three cases, one held, one whose `**Loads:**` file a later commit
  changes, and one replayed below its baseline, `python check_evals.py` in the
  fixture prints `held`, `owed` naming the changed path, and `fell`, and exits 1; with only the held case
  it exits 0; with no case it prints `unarmed` and exits 1.
  Red when: a moved load reads `held`, or an empty suite exits 0.
- **AC4** — When the plant `guard` tracks a kit's `instructions.toml` outside the leg's guard, and a case
  loads a path outside it, the check prints `guard misses` naming that manifest's path and `unguarded`,
  and exits 1.
  Red when: a manifest the guard misses passes, so a change to it never selects the leg.
- **AC5** — When the leg manifest `gate-legs.json` is read with `json.load` and filtered to the row
  whose `name` is `instruction-eval`, it holds one row with `subject` `kit` and an `argv` naming `check_evals.py`;
  `python tools/govkit/govkit.py shipped --epoch` prints no `tools/workflows/evals/` path; and `grep -n
  'name = "instruction-eval"' tools/govkit/registry.toml` prints the `[[exempt_leg]]` row.
  Red when: a kit ships the entry, so `changed` ignores the guard.
- **AC6** — (amended, id 4; r3 id 2) When `python check_evals.py` runs over the tree at this unit's
  order, it prints one line for `design-audit-runtime-record`, `owed` naming the paths unit 5 moved
  after the replayed sha, or `held` where none moved, and never `unarmed`; red on `owed` is
  `TOOL-dCalibratedLens-23` AC2's, at the close after the main loop's replay.
  Red when: the seed case is missing or refused.
  figure: DERIVED, the verdict depends on the tree at observation time.
- **AC7** — When the plant `add-case` runs `--add-case --from <record> --finding 7` over a review record
  whose row 7 is confirmed with `units` `unit.reuse-first`, it writes `<record stem>-7.md` with
  `**Expect:** absent`, `**Baseline:** 0/1` and one known row at the row's `ref`; finding 8, confirmed
  with `units` `-`, and finding 9, refuted, are each refused by name; a second `--add-case` for finding 7
  is refused naming the existing case.
  Red when: a finding with no cited unit becomes a case, or a finding gets two.
- **AC8** — When `python loop_review.py --fixture --plant eval-candidates` holds two confirmed
  findings citing units in the window, one named by a case's `**From:**`, `propose --dry-run` prints one
  `eval-case <stem>#<id> add-case` proposal, and `gather --dry-run` prints `eval-candidates: 1
  finding(s) · 1 case(s) · …`.
  Red when: the covered finding is proposed again.
- **AC9** — When `grep -n "Instruction evals" tools/workflows/README.md` and `grep -n "When an instruction
  changes" help/roles.md` run, each prints the section heading.
  Red when: either is absent.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `docs` · `review-replay selftest` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test` · `policy fixtures` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor` · `recall floor arms` · `codebase-map gate coverage` · `every held leg is budgeted, every budget row resolves` · `govkit selfcheck` · `leg ceilings clear their evidenced maximum`

The new leg `instruction-eval` is not in the manifest at base and is named here in prose; the loop kit's
`loop-review selftest` grades S7's plant once TOOL-dCalibratedLens-2 lands.

New arm: tools/workflows/replay_scorer.py · covers AC1 AC2 AC3 AC4 AC7 · the instance's `--fixture` plants, run inside `review-replay selftest`, staged red by an `absent` case scored as `found`, a check that reads a moved load as held, and an empty suite exiting 0 · none
New arm: tools/loop/loop_review.py · covers AC8 · the `eval-candidates` plant, staged red by a proposer that ignores `**From:**` · none

## 8. Open questions

- **FACT-QUESTION · F1 — Will `GATE_SELFTESTS=changed` select the leg when an instruction file moves?**
  The probe: `python tools/govkit/govkit.py shipped --epoch`, reading whether the leg's argv file is in a
  kit's shipped rows. The observation that decides: a withheld file is absent from the output and selects
  by its guard; a shipped one is present and selects by its kit's sources
  (`tools/run-gates/run-gates.sh:3075-3080`). Liveness: the same output lists
  `tools/workflows/review_replay.py`, a positive, and omits `tools/workflows/tier2-review.test.sh`, the
  negative the probe can produce. Run 2026-11-02 on node a at `22a8efac3`: `review_replay.py` listed under
  `review-harness`, `tier2-review.test.sh` absent. RESOLVED (agent, 2026-11-02, delegated): the leg's entry
  is a withheld file, `tools/workflows/evals/check_evals.py`, so its guard selects it; rung 2. widens:
  none · relaxes: none
- **F2 — What does "re-run as a held leg" run?** Options: (a) the leg re-runs the suite's scoring and
  freshness check, and reds each case a change made owed, naming the replay procedure; (b) the leg spawns
  each case's item and review headless and scores them; (c) a cadence step replays every case each
  period. The clause scores the suite "through dFairHearing's scorer factory", which re-derives every
  figure from committed raw outputs and runs no agent (TOOL-dFairHearing-12 §1, §3), so the suite the
  leg re-runs is a scoring of committed replays, and a change makes a replay owed rather than producing
  one. (b) puts agent sessions and their tokens, about 0.81 M per design audit, inside a bar that
  launches none, a new automation surface (veto 3) and a harness dependency at bar time (veto 2); (c)
  replays unchanged instructions and misses the change. RESOLVED (agent, 2026-11-02, delegated): (a),
  rung 3, the one survivor of the vetoes, recorded as deviation 101 because the leg re-runs the suite's
  scoring and check and never its items. widens: none · relaxes: none
- **F3 — Which findings have "an instruction" as their cause?** Options: (a) a confirmed finding whose
  `units` cell names a tag, TOOL-dCalibratedLens-5's citation; (b) a confirmed finding a person marks
  by hand; (c) every confirmed finding. (b) has no field to read; (c) makes every defect an instruction
  eval. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — What does a case added from a finding replay?** Options: (a) the item that wrote the defect,
  re-run from its brief at its base and reviewed, the defect expected absent; (b) the review that found
  it, the defect expected found. (b) tests the reviewer's instructions, not the instruction the finding
  cites as the cause. RESOLVED (agent, 2026-11-02, delegated): (a), with `**Expect:**` carrying both
  polarities so the seed, a review replay, keeps (b)'s; rung 3. widens: none · relaxes: none
- **F5 — Where does a case live?** Options: (a) under `tools/workflows/evals/`, withheld, as the brief's
  S10 states; (b) under the memory tree, a record home. (b) puts the leg's input outside the kit whose
  factory scores it and needs a new home. RESOLVED (agent, 2026-11-02, delegated): (a), rung 1, the
  brief's shared interface S10. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the packet's Items 10 (`cl-dClosedLoop-0467@58bd6ee5`), the night
  pass's point 6 S2, the brief's row for unit 10 and its S10 interface, TOOL-dFairHearing-12, -1 and -25 at
  their current revisions, and the run-gates held-tier selection at base.
- rev-2 · 2026-11-02 · §3 §4 §7 S3 S4 S5 AC6 · amended at the disposal of the round-1 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4 "Amendments (round-1 spec
  audit)": ids 4 (`TOOL-dCalibratedLens-23`), and 8 and 41 (`TOOL-dCalibratedLens-30`); §3 gains the
  hands-off to unit 23.
- rev-3 · 2026-11-02 · §3 §4 S5 · amended at the disposal of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`, §4 "Amendments (round-2 spec audit)": r2 id
  6 (`TOOL-dCalibratedLens-36`), the seed's `**Loads:**` stated; §3 gains the hands-off to unit 36.
- rev-4 · 2026-11-03 · §4 S3 S5 AC6 · amended at the disposal of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, §4 "Amendments (round-3 spec audit)": r3 ids
  2, 3, 13 and 31 (`TOOL-dCalibratedLens-48`), AC6 at this unit's order, the editors of the loads, the
  rendered agent files as loads with `.claude/agents/` in the guard, and the owed rule over the
  working tree.

## 10. Reuse audit

The seams extended: TOOL-dFairHearing-12's factory, a new `INSTANCES` row as TOOL-dLinkedLibrary-16 adds
`code-replay`; TOOL-dFairHearing-1's known-set grammar, reader and adjudicated scoring, which the case
reads rather than restates; the held tier's guard selection (`tools/run-gates/run-gates.sh:3075-3080`);
the withheld-suite pattern of `tools/workflows/kit.toml:36-37` and its `[[exempt_leg]]` rows; and
TOOL-dCalibratedLens-5's `units` column and `PROPOSERS`. `python tools/codebase-map/reuse_lookup.py
"replay recorded tasks with known outcomes when an instruction changes and score them"` ranked name stems
only (`records`, `changed` in `run-gates.sh`, `score` in `tools/memory-recall/bench.py`, `render_record`),
none a replay of an instruction change; the recall query below returned the brief, v2's row and the
replays of TOOL-dLinkedLibrary-16 and TOOL-dTotalRecall-17, each a scorer instance and none an eval over
instruction units. So no existing seam fits the suite and it is a new instance over the factory. Where
the brief and source disagree: the brief's leg is guarded by the instruction units, and a guard alone does
not select a held leg whose entry a kit ships (§8 F1), so the entry is withheld.

Recall terms used: `python tools/memory-recall/query.py "how are instruction changes replayed against
recorded items with known outcomes and scored" --terms "instruction eval replay suite known set scorer
factory held leg guard instruction unit case confirmed finding"`
