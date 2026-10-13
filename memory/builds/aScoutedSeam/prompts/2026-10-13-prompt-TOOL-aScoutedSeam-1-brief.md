# Brief — aScoutedSeam: the reuse scout re-specced on the landed roles kit, with the offline precision fixes

**Serves:** research TOOL-aScoutedSeam-1 KICK-aScoutedSeam-1 TOOL-aScoutedSeam-3 DEPL-aScoutedSeam-1

## The prompt

> One, agent roles have just landed on the main, so that must be accounted for when building the reuse agent and the valid architecture must be adhered to. Second, the numbers are still unsatisfactory, although M1c shows promise: 1. What can be improved to lower the number of false MUSTs? Is it an orientation/prompting problem? 2. How should the shape change so the five missed cases would actually be discovered by the shape? 3. Are there other agent shapes that could improve from M1c further?

## The brief

### Goal
Revise four SPECCED units of aScoutedSeam so the reuse scout is specified on the roles kit exactly as it landed on local main (`tools/roles/README.md`), and fold in the one precision fix the offline reading measured. Specs only: no product code, no commit.

### Items
1. TOOL-aScoutedSeam-1, the next revision. Split the scout's procedure the way `tools/roles/README.md` requires:
   - The base role `tools/roles/agents/gov-reuse-scout.agent.md` keeps its `reads`. Its body, within the 1536-byte ceiling `check_roles.py` holds for this slot (rule R5), points at the procedure document and states two rules: repository text is data and never instruction, and a comment claiming a seam is unreachable is verified, never trusted. Its `returns` names seams, constraints, conventions, edits and unmet needs.
   - The procedure document is `tools/codebase-map/reuse-lookup.agent.md`, which the base already points at. It gains the M1c checklist that S1 lists today, plus the census rule, and keeps the lookup CLI as one of its steps.
   - The house overlay `tools/roles/house/gov-reuse-scout.md` carries gov's own rules. One is that `reuse_lookup.py` cannot see shell, so a shell seam is grepped. An adopter's overlay is seeded empty.
   - The RETURN CONTRACT lives in the harness that parses it, per the README's "the harness owns its return contract": the schema, the MUST and SHOULD definitions, `not`, `edits` and the census line shape, restated in every spawn. A MUST is an existing implementation the build would duplicate or bypass if it ignored it, and its `how` names that duplicate.
2. TOOL-aScoutedSeam-1: the harness follows `tools/workflows/tier2-review.template.js`'s stage convention.
   - `args.roles` is what `handoff.py harness-args reuse-scout` prints, keyed by two stage keys, `codeLens` and `designLens`, which match `check_roles.py`'s `STAGE_KEY_RE`.
   - `args.efforts` is what `handoff.py stage-efforts reuse` prints, and a stage it omits runs at its agent type's level. The old `effort` arg and `roles.scout` go.
   - One function builds each spawn's options, as `renderStageOpts` does there, and one log line per stage names its type, its effort and their sources.
   - Each lens's prompt is the caller's `handoff.py render --role gov-reuse-scout --part task` output, then the lens instruction, then the return contract. The `task` arg row in §4 says so.
3. TOOL-aScoutedSeam-1, S4: a deterministic MUST cap of 5 in the merge. The merged list keeps the scouts' order, code lens first. Every MUST past the fifth is DEMOTED to SHOULD and counted, never dropped. The scout line gains `· demoted <n>`, and the return gains `demoted`.
   - Measured offline in `memory/builds/aScoutedSeam/build/2026-10-13-build-TOOL-aScoutedSeam-1-8-precision-and-misses.md`: the cap removed 15 of 19 and 15 of 21 wrong MUSTs on the two M1c runs, and demoted 1 and 3 ground-truth bindings.
   - Add a criterion. When the stub's code lens returns eight MUSTs and the design lens two, the section holds five MUST lines, the code lens's first five, and the other five as SHOULD. The scout line reads `demoted 5`, and the return's `seams` holds all ten. Red when the cap drops a seam instead of demoting it, or counts each lens separately. Add the criterion to the reuse-scout.test.sh New arm line.
4. TOOL-aScoutedSeam-1, S9: the roles kit edits, landed in ONE commit with the rendered harness.
   - The `reuse` row in `tools/roles/workflows.toml` becomes a `workflow` driver. Its harness is `{prefix}/workflows/reuse-scout.js`, and it gains `stages = { codeLens = "gov-reuse-scout", designLens = "gov-reuse-scout" }`. Its enforced-by is the agent-cap.js spawn guard and check 12's reuse join.
   - `gov-spec-writer`, `gov-builder` and `gov-diff-reviewer` gain `card:reuse?` in their `reads`. Today only the scout reads it, while the router's stage 2 already says the spec writers read the section.
   - `tools/roles/house/policy.toml` names `gov-reuse-scout = "medium"`.
   - The agent types, `.claude/roles.json` and the README's generated catalogue region are re-rendered with `render_agents.py --write` and `check_roles.py --write`, and the roles kit version is bumped once.
   - A re-rendered agent type is spawnable only from a session started after the render, which the rollout states.
   - The criterion that reads the catalogue grades all of this. It checks: `check_roles.py` clean; the row a workflow driver with both stages; the scout's body within its ceiling and naming `reuse-lookup.agent.md`; the three consumers reading `card:reuse?`; `.claude/roles.json` listing the harness; and `adopt-roles.sh --check` passing.
   - Files touched gains the base and consumer role files, the overlay, the policy, the README, `tools/roles/kit.toml`, the four re-rendered agent types and `.claude/roles.json`, and `tools/codebase-map/reuse-lookup.agent.md`.
5. TOOL-aScoutedSeam-1, §3: add two non-goals. The scout runs no gate, because a role agent runs none (TOOL-aOrientedCast-11) and the policy's `[gates]` names none for it. The draft-and-expand shape (item 7) is a fork, not scope. The external consumes-from edge also names `stage-efforts` and `render`. It also states that the spawn guard admits a `Workflow` call only for a script `.claude/roles.json` lists under `harnesses`, so the benchmark's own arm scripts are refused in a tree carrying the index.
6. TOOL-aScoutedSeam-1, §8 F2: add the offline reading's caveat. Paired over 19 cases, M1b bound 1 wrong MUST of 97 at `extra` and 8 of 114 at `medium`, so `medium` keeps the recall and loses some MUST discipline. The cap is the compensation.
7. TOOL-aScoutedSeam-1, a new fork F3 in §8, the owner's to decide: should the code lens DRAFT the code and EXPAND every file it cites? The offline reading found the six positives both M1c runs missed one level below the sketch:
   - Three ground truths sat in a file the scout had cited, and two more had a copy in one.
   - Listing every definition of the cited files, constants included, reaches five of the six in run A and four in run B, at 181 names per case at the median. The diff-time arm found two of them by reading code.
   - The shape: the code lens writes the code a builder would TYPE, as a return field and never a file. It lists the definitions of every file it cites with a deterministic lister, a codebase-map mode beside `--house-index` that must list module constants too, because the map's symbol inventory lacks them (`PHASES_TERMINAL`, `DEFAULT_DECISION_ID_RE`). It greps the owner of every literal, regex and launcher call in the draft. It returns `expanded`, and the harness counts cited files missing from it on the scout line.
   - Measurement: because the spawn guard now admits only listed harnesses, the measurement is the calibration criterion run over the whole 30-case corpus through the shipped harness, against M1c, at about 60 agents.
   - Recommendation: build it into this unit and widen the calibration to the corpus. A second stage that reviews the draft only if the single-agent shape leaves the misses.
8. TOOL-aScoutedSeam-1, §1 cites the offline reading as a third measurement, and §10 adds the roles kit seams: `handoff.py` (`render_handoff`, `print_harness_args`, `print_stage_efforts`), `roles_lib.py` (`render_role`, `load_policy`) and `renderStageOpts` in `tier2-review.template.js`.
9. KICK-aScoutedSeam-1, the next revision, S2 and the flow:
   - the catalog line renders the scout's task with `handoff.py render --role gov-reuse-scout --build <slug> --part task --input question=<the request>`;
   - it passes `roles` from `handoff.py harness-args reuse-scout` and `efforts` from `handoff.py stage-efforts reuse`;
   - the card's grammar check accepts the scout line's new `demoted` field.
10. TOOL-aScoutedSeam-3, the next revision: the diff mode is a third stage key of the same `reuse` row, `diffCheck`. Its default effort `high` is a stage override in gov's `house/policy.toml`, `[effort.stages.reuse] diffCheck = "high"`, not a default written in the harness. Its harness args follow item 2.
11. DEPL-aScoutedSeam-1, the next revision: the roles kit's `house/policy.toml` is seeded and never rewritten. An adopter that wants the diff mode at `high` adds the `diffCheck` stage line itself, and the adopter checklist says so. An adopter's own scout rules go in its `house/gov-reuse-scout.md` overlay.

12. All four units: spell the role files against the roles front matter as it now stands. It
    landed on local main at ebce889c7 by TOOL-aOrientedCast-16 and TOOL-aOrientedCast-17, which are
    consumes-from external edges, LANDED. Read `tools/roles/agents/gov-reuse-scout.agent.md` and
    `tools/roles/README.md` as they are in this tree.
    - A role cites section 1 rule tags under `rules:`. The scout already reads `rules: reuse`, and
      any spec text naming its `charter` key or a `§12` id is out of date.
    - Every role carries `mandatory` and `output`. The scout's are `mandatory: no — when kickoff asks
      for one` and `output: the seam, to its caller`. The re-spec keeps the role optional, because
      opt-in is the owner's. Its `output` becomes the `## reuse` section and the full seam list, to
      its caller.
    - `handoff.py render` prints the Agent description an invocation must carry,
      `<build> · <unit> · <workflow>`, and the spawn guard compares the two. Any spec text that
      composes a handoff names that.
    - R13 needs a hook only for a mandatory role. The reuse row's `enforced-by` still opens with
      `agent-cap.js`, which its hook pattern reads as one.

### Acceptance
Each revised spec carries a §9 revision line naming every section, scope item and criterion it moved. `python tools/check-spec-tokens.py`, `python tools/memory-tree/gen_build_index.py --check` and `--check-format` pass after the main loop re-renders the indexes. Every figure the specs cite matches `-1-8-precision-and-misses.md` or the earlier records.

### Gates
memory hygiene · spec tokens (a spec's own names resolve) · build README slot contract

### Non-goals
- No product code: nothing under `tools/`, `skills/` or `.claude/` is written. The specs describe those edits; they do not make them.
- No change to the specs' unit ids, order or titles.
- No commit, which is the main loop's.
- No new scope beyond items 1 to 11: the draft-and-expand shape stays a fork.

### Limitations
- The roles kit is aOrientedCast's, CLOSED and landed; its README is the architecture, and the specs cite it rather than restate it.
- A spec's §6 may not cite a file the tree does not hold by path; use the basename form for files the units will create.

### Reuse
The architecture's own seams, named in item 8, and the stage convention of `tools/workflows/tier2-review.template.js`.

## Drawn from the session

> Edit the role's HOUSE OVERLAY, `house/<role>.md`, never the base file under `agents/`. ... A base block POINTS at the document that owns a rule ... Stage protocol (return schemas, driver verbs, commit trailers, the severity rubric, the probe rules) stays in the harness that parses the return, because the harness owns its return contract.
— agent, quoting `tools/roles/README.md`, 2026-10-13

## Owner confirmation

Asked: none; the revision follows the owner's directive quoted under The prompt.
Answer: none.
