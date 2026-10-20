# Research: scenarios, prior art outside gov

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 128's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-9-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`.

---

**Prior art: how systems let users define, pick, compose, adapt and record variants of a default process (point 1, outside gov)**

**Short answer:** outside gov I found eight families of mechanism. None of them covers all five of the owner's cases alone. I pick a combination, K7, which reuses gov's existing composition and adds per-build selection of scenarios. It handles worst a piece of work that fits two scenarios whose changes conflict: the conflict is caught, but the owner has to decide it. The main gap in gov's design: a scenario can only be chosen per repository today, never per piece of work.

All outside sources were read on 2026-10-19. I wrote nothing in the repository. The temporary probe folders under the session scratchpad (`lgprobe`, `lgscripts`, `cmmn`, `wl`, `cy`) are deleted. A stray `inspect.py` left there by another session shadows Python's standard library; I worked around it with `python -I` and did not touch it.

The five losing cases from the question are numbered here:
- **E1:** an edge case needs its steps reordered and a role inserted.
- **E2:** a piece of work fits two scenarios at once.
- **E3:** a mid-build adaptation nobody records.
- **E4:** a recorded adaptation is promoted and breaks builds already using it.
- **E5:** a variant bypasses a gate gov requires.

## Families

### F1. One superset model, restricted by configuration
**Mechanism:** there is one "least common multiple" model, and a variant is an assignment that switches parts of it off or skips them.
- **Systems:**
  - Configurable workflow models (C-YAWL), https://vdaalst.com/publications/p462.pdf. A configurable element "can be either set to enabled, to blocked, or to hidden", and "requirements" constrain which configurations are allowed. Configuration only restricts behaviour: the base model "contains the maximal possible behavior".
  - GitLab `include` with `rules:if/exists/changes`, https://docs.gitlab.com/ci/yaml/includes/.
  - Azure's conditional stages and jobs with `${{ if }}`, https://learn.microsoft.com/en-us/azure/devops/pipelines/security/templates?view=azure-devops.
- **Point 2:**
  - **Declared as:** settings on the base model's ports, or `rules` on includes.
  - **Chosen:** at instantiation, by a person answering a questionnaire (La Rosa et al., per a search result summary, not read in full), or by CI variables. A wrong choice shows up as a configuration that breaks a requirement, or as an invalid or disconnected model.
  - **Composed:** none. Each configuration is one assignment.
  - **Changed on the fly:** not possible. You edit the base model.
  - **Worker shapes:** whatever the base model already contains.
  - **Coherence:** the requirements, checked when the model is configured.
- **Point 3:**
  - E1 loses: a reordering or a role the superset lacks cannot be expressed.
  - E2 loses: two assignments that disagree on a port (one blocks it, one enables it) cannot be merged.
  - E3 has nowhere to land.
  - E4: changing the base model changes every variant built on it.
  - E5 holds only if the gate is written as a requirement.

### F2. A fixed skeleton with typed slots, plus pinned templates included by reference
**Mechanism:** upstream owns the outer structure, and variants are named templates called or included at declared points, pinned to a revision.
- **Systems:**
  - Azure `extends` templates and the "required template" check, from the Azure page above: "If the pipeline doesn't extend from the required template, the check fails."
  - GitHub reusable workflows, https://docs.github.com/en/actions/sharing-automations/reusing-workflows. A ref is pinned by SHA, tag or branch ("Using the commit SHA is the safest option"). At most ten levels of nesting, no loops. A matrix job can call a reusable workflow.
  - GitLab parent-child pipelines, https://docs.gitlab.com/ci/pipelines/downstream_pipelines/. A child configuration can be generated as an artifact at run time; two child levels at most; up to 1000 downstream pipelines.
  - Argo `templateRef` and `workflowTemplateRef`, https://argo-workflows.readthedocs.io/en/latest/workflow-templates/.
  - Rundeck's Job Reference step (official docs, seen only through a search summary because the page redirected).
- **Point 2:**
  - **Declared as:** a template file with typed inputs.
  - **Chosen:** by the pipeline author at commit time. Choosing a template is static, but a dynamic matrix built with `fromJSON` decides how many copies run at run time (https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations). A wrong choice surfaces as a failed run, or as a failed required-template check.
  - **Composed:** by nested calls and includes. In GitLab, "the last included file takes precedence", the merge is deep, and arrays are replaced whole, never merged.
  - **Changed on the fly:** none inside a run. You commit a change, so version control is the only record.
  - **Worker shapes:** a matrix with `max-parallel` and `fail-fast`.
  - **Coherence:** pins, typed parameters, and checks on protected resources.
- **Point 3:**
  - E1 works inside a slot only.
  - E2 composes, but the last include silently wins.
  - E3 loses.
  - E4 is safe only when pinned. A branch ref floats.
  - E5 is the family's strength: the required-template check.

### F3. A late-bound sub-process chosen per work item from a repertoire, refined by recorded exceptions
**Mechanism:** a task in the parent process is a placeholder. At run time, rules over the case's data pick one member of an extensible repertoire. A wrong pick is recorded and becomes a refining rule.
- **Systems:**
  - YAWL Worklet Service, Adams et al. 2006, https://www.vdaalst.com/publications/p350.pdf:
    - It is "an extensible repertoire of self-contained sub-processes aligned to each task, from which a dynamic runtime selection is made".
    - Selection uses ripple-down rules. "Each time the worklet service selects a worklet … a file is created that contains certain descriptive data about the selection process."
    - A user rejects an unsuitable choice. A new rule is added as a refinement of its parent, with the current case kept as its "cornerstone case".
    - The repertoire and rules can grow "even during process execution". Replacing the running instance is optional: "the Editor provides an administrator with the choice to replace the previously started (inappropriate) worklet instance".
  - Camunda 8 ad-hoc subprocesses, https://docs.camunda.io/docs/components/modeler/bpmn/ad-hoc-subprocesses/:
    - `activeElementsCollection` chooses which inner elements run, or a job worker or AI agent chooses ("only one active job for the ad-hoc sub-process at a time").
    - `completionCondition` ends the subprocess, and `cancelRemainingInstances` defaults to true.
- **Point 2:**
  - **Declared as:** a repertoire per task, plus a rule tree.
  - **Chosen:** by rules evaluated by the engine, or by a worker or agent. A wrong choice is a user rejection, recorded through the selection file and the cornerstone case.
  - **Composed:** by nesting. A worklet is an ordinary specification and can be reused across repertoires.
  - **Changed on the fly:** add a worklet or rule while running. Promotion is the new rule itself, reached only by future cases that match it.
  - **Worker shapes:** a multiple-instance task gets one worklet per child item, each chosen separately.
  - **Coherence:** the parent model stays fixed, and every rule is a refinement of its parent.
- **Point 3:**
  - E1 works inside a task's slot, but cannot reorder the parent.
  - E2 loses: one conclusion per work item.
  - E3 is handled: the selection file plus the rejection.
  - E4 is mostly safe: a refinement only catches matching cases, and running instances are replaced only by an administrator.
  - E5: the parent model's gates stay, because worklets only fill tasks.

### F4. A case plan with discretionary items and sentries, or declarative constraints
**Mechanism:** there is no fixed order. Work items become available under entry and exit criteria, and people plan optional items into the case at run time.
- **Systems:**
  - OMG CMMN 1.1, https://www.omg.org/spec/CMMN/1.1/PDF, extracted with `pdftotext`. §5.4.9 says:
    - "Planning is a run-time effort. A PlanningTable defines the scope of planning".
    - "Users (Case workers) are said to 'plan' … when they select DiscretionaryItems from a PlanningTable".
    - Roles can be authorised per item, and ApplicabilityRules "dynamically control what DiscretionaryItems … are exposed".
  - Flowable CMMN, https://www.flowable.com/open-source/docs/cmmn/ch06-cmmn:
    - Sentries have onParts and ifParts, and "when one is satisfied, the plan item moves from state available to active".
    - Repetition rules and `maxInstanceCount`.
    - Manual activation with `startPlanItemInstance`.
  - DECLARE (Pesic, Schonenberg, van der Aalst), https://research.tue.nl/en/publications/declare-full-support-for-loosely-structured-processes/: a constraint-based model with "changing models at run-time".
- **Point 2:**
  - **Declared as:** stages, plan items, a planning table, and sentries.
  - **Chosen:** by an authorised caseworker, filtered by applicability rules. A wrong choice surfaces as a sentry that is never satisfied, or a stage that never completes.
  - **Composed:** by nested stages.
  - **Changed on the fly:** the planned case instance is the record. I found no step that promotes a planned instance into the model, in the spec passages I read.
  - **Worker shapes:** repetition and instance counts.
  - **Coherence:** sentries and applicability.
- **Ambiguous:** neither the Flowable chapter nor the Camunda 7 stage page (https://docs.camunda.org/manual/7.21/reference/cmmn11/grouping-tasks/stage/) covers planning tables. Whether either engine implements run-time planning is unconfirmed.
- **Point 3:**
  - E1 is natural, but only with items already in the planning table.
  - E2: you can plan both sets of items into one case.
  - E3: an instance record exists, with no promotion.
  - E4 is not applicable.
  - E5 holds only for gates written as sentries. An exit criterion can be planned around.

### F5. Structure computed by code, with versioned execution
**Mechanism:** a variant is a branch or child in workflow code, the fan-out width is a value at run time, and running instances survive code changes through patching or version pinning.
- **Systems:**
  - Temporal versioning:
    - Child workflows, https://docs.temporal.io/child-workflows: "a single Parent should not spawn more than 1,000 Child Workflow Executions".
    - Patching, https://docs.temporal.io/develop/go/versioning: an unversioned change gives "a nondeterminism error".
    - Worker Versioning, https://docs.temporal.io/worker-versioning: "A Pinned Workflow is guaranteed to complete on a single Worker Deployment Version". Auto-Upgrade workflows move when the current version changes.
  - Airflow dynamic task mapping, https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html. `max_map_length` defaults to 1024, `max_active_tis_per_dag` caps how many run at once, and "Task-mapping in a mapped task group is not permitted".
  - LangGraph, https://docs.langchain.com/oss/python/langgraph/graph-api. Conditional edges, `Send`, `Command` and subgraphs; `compile()` gives "a few basic checks … (no orphaned nodes, etc)"; `recursion_limit` caps super-steps.
  - CrewAI Flows, https://docs.crewai.com/en/concepts/flows. `@router`, `or_`/`and_`, `@persist`, and `restore_from_state_id` to fork a run.
- **Probe:** LangGraph 1.2.16, isolated venv, my own script. Each test was written to make this family lose:
  - **T1, a variant's router fans out 12 workers against a cap of 5:** `workers run: 12 peak concurrent: 12`. With `{'max_concurrency': 5}`: `workers run: 12 peak concurrent: 5`. The cap is the caller's setting, and the framework refuses nothing.
  - **T2, a variant reorders review before build:** `reordered variant compiled: True`, then `failed at RUN: KeyError 'built'`.
  - **T2b, an inserted role node never wired in:** `orphan inserted role compiles: True`. (The docs' "no orphaned nodes" check did not refuse it.)
  - **T2c, a misspelled edge:** `refused at compile: ValueError Found edge ending at unknown node`.
  - **T3, two scenario subgraphs on the same work, writing one key:** `InvalidUpdateError At key 'plan': Can receive only one value per step.` So the conflict is loud.
  - **T4, what a checkpointed run records:** `next per checkpoint: [(), ('review',), ('build',), ('design',), ('__start__',)]`. That is the path taken, not a reusable variant.
- **Point 2:**
  - **Declared as:** code.
  - **Chosen:** by code, or by a model inside a router. A wrong choice surfaces at run time (T2).
  - **Composed:** child workflows and subgraphs.
  - **Changed on the fly:** deploy new code. The record is the commit plus the event history. Promotion uses pinned or auto-upgrade versions.
  - **Worker shapes:** any shape, with caps that are configuration.
  - **Coherence:** determinism and replay tests (Temporal); otherwise none beyond compile.
- **Point 3:**
  - E1 loses late (T2).
  - E2 is loud (T3).
  - E3 loses (T4).
  - E4 is handled by Temporal's pinned versions.
  - E5 loses (T1).

### F6. Changing a running instance, then evolving the type and migrating instances that still comply
**Mechanism:** structural edits (insert, delete, move) to one running instance, checked for correctness. The type's own changes are later propagated to instances that comply.
- **Systems:**
  - ADEPT2 and AristaFlow, https://uni-ulm.de/in/iui-dbis/forschung/abgeschlossene-projekte/adeptevolution: "automatic migration of compliant workflow instances to a changed schema". It handles "biased" instances, meaning those already carrying ad-hoc changes, and "conflicts between workflow type and workflow instance changes".
  - Camunda 8 process instance migration, https://docs.camunda.io/docs/components/concepts/process-instance-migration/:
    - "The migration plan is validated before the migration is executed".
    - It is transactional, "all active elements or nothing".
    - The number of active elements cannot change; process instance modification covers that case.
- **Point 2:**
  - **Declared as:** a change applied to one instance.
  - **Chosen:** by an operator. A wrong change is refused by the correctness check.
  - **Composed:** none.
  - **Changed on the fly:** this is the family's core. The record is the biased instance, and promotion is a type change plus a compliance check on each instance.
  - **Worker shapes:** whatever the model allows.
  - **Coherence:** the correctness criteria and the migration plan check.
- **Point 3:**
  - E1 is handled per instance.
  - E2 is not addressed.
  - E3 is handled: the change is itself recorded.
  - E4 is the family's strength: only compliant instances migrate.
  - E5 holds only if the correctness criteria encode the gate.

### F7. Routing chosen by the model through handoffs
**Mechanism:** each agent declares which agents it may hand off to, and the model picks the next one with a tool call.
- **Systems:**
  - OpenAI Agents SDK handoffs, https://openai.github.io/openai-agents-python/handoffs/. "Handoffs are represented as tools to the LLM"; `is_enabled`, `input_filter` and `on_handoff`.
  - AutoGen Swarm, https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/swarm.html. "The speaker agent is selected based on the most recent HandoffMessage".
  - AutoGen GraphFlow, https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/graph-flow.html. Fan-out, conditional edges and `activation_condition` all/any; marked experimental.
  - Claude Agent SDK subagents, https://code.claude.com/docs/en/agent-sdk/subagents:
    - "Claude automatically decides when to invoke subagents based on the task and each subagent's `description`".
    - Caps: nesting depth 3 by default, 20 concurrent, and an optional `maxBudgetUsd`.
    - Per-agent `tools`, `model`, `effort` and `maxTurns`.
- **Point 2:**
  - **Declared as:** an agent definition plus a description.
  - **Chosen:** by the model. A wrong choice surfaces only in the output.
  - **Composed:** handoff chains.
  - **Changed on the fly:** the factory function builds definitions per request. The record is the transcript.
  - **Worker shapes:** caps set by environment variable, plus per-agent tool restrictions.
  - **Coherence:** tool restrictions and caps only.
- **Point 3:**
  - E1 works in practice but is never declared.
  - E2 is open.
  - E3 loses.
  - E4 is not addressed.
  - E5 loses unless the gate is a tool restriction or a cap.

### F8. Mining recorded runs into models, checking conformance, repairing the model
**Mechanism:** discover a model from event logs, align each run against the model, and repair the model where runs keep deviating.
- **Systems:**
  - pm4py: `discover_petri_net_inductive` and `conformance_diagnostics_alignments`. I saw these through a search summary; the pm4py API page refused the connection.
  - Fahland and van der Aalst, "Model Repair", https://vdaalst.com/publications/p807.pdf, as summarised by search. Non-fitting subtraces become inserted subprocesses or loops.
  - Declare discovery (Maggi et al., per search).
- **Point 2:**
  - **Declared as:** variants derived from traces.
  - **Chosen:** none; this family is analysis only. A wrong choice surfaces as a conformance deviation.
  - **Composed:** none.
  - **Changed on the fly:** a deviation is observed after the fact. Promotion is repair.
  - **Worker shapes:** not modelled.
  - **Coherence:** fitness and precision measures.
- **Point 3:** E3 is caught, but only for what the log records. It is not a mechanism for E1, E2, E4 or E5 on its own.

**Where I stopped:** Prefect differs from Airflow and Argo only in detail within F5, and GitLab `rules` versus Azure conditions only in detail within F1 and F2.

## Candidates for gov

**Reuse first.** Gov's existing seams are:
- the one composition per repository: `flow-roles-adoption [design]` items 1 to 16, and P8 in `architecture-v2 [principles]`;
- `entry.place`, which picks a disposition from a closed set (continue, amend, new, patch, repeat, ask, none) under three placement modes, checked by `placement.check` (`flow-steps [entry]`);
- `repeat`, which runs a pinned playbook (`night-pass [p1-unattended]` item 6);
- the shape kinds and `FANOUT_CAP`, which a repository may lower but never raise, with 5 as the ceiling (`tools/hooks/agent-cap.js:61-71`);
- the lens arrays, still literals in code (`tools/workflows/tier2-review.js:705`, `:735`, `:741`, `:773`).

| # | Candidate | Smallest scenario that makes it lose | Result |
|---|---|---|---|
| K1 | The repository-scoped composition alone, as handed | One repository runs a design build and a mobile-app build at the same time, each needing its own role roster | **Loses.** "a repository names one preset and overrides individual keys on top of it" (`architecture-v2 [presets]`). The overlay is one home per repository (`flow-roles-adoption [design]` 1). I grepped v2, flow-steps and the adoption record for per-build, build-scoped and similar terms: nothing selects a composition per build. |
| K2 | F1 plus F2: static scenario templates, pinned, included per build | An agent adds one security-review item mid-build for this build only | **Loses E3.** The only record is a commit to the template, which reaches every build using it. With pins, E4 holds and E5 holds through fixed rows. |
| K3 | F3 alone: a repertoire chosen by rules at placement, with rejections refining the rules | Work that is both "mobile" and "high-precision" | **Loses E2.** One conclusion per work item (worklets paper, §on multiple instances). |
| K4 | F5: scenarios as code (a script or graph) | A variant's router asks for 12 workers | **Loses E5 and E1.** Measured in T1 and T2. Gov's agent-cap would still catch a Workflow script's width (`agent-cap.js:61-71`), but not a skipped item or gate. T4: the run records its path, not an adaptation. |
| K5 | F7: routing chosen by the model | Any gate that is not a tool restriction | **Loses E5 and E3.** The choice is a tool call, and the record is a transcript. |
| K6 | F4: a declarative case plan replacing stage order | A build planned with Deploy before Test | **Rejected on fit.** It contradicts P20 as FA-3 amended it: gov's stages stay whole and in order (`flow-roles-adoption [folded]`). Two parts are borrowed into K7: applicability rules and authorised roles on optional items. |
| K7 | A combination, described below | E2 with conflicting patches | Described below. |

**K7, how the combination works:**
- **What a scenario is (F2 rows).** A scenario is a named, pinned fragment of overlay rows in gov's existing kinds. It reuses the composition, its patches, its exclusions and its fixed set unchanged. Gov ships a set; a repository adds its own.
- **How it is chosen (F3 plus CMMN).** It is chosen per build at `entry.place` by applicability rules over the request's facts, under the existing three placement modes. Several may be chosen and are composed in a declared order. Any two patches that set one field to different values red at composition, which matches the loud conflict LangGraph showed in T3.
- **How it is pinned (Temporal-style).** The chosen set is pinned in the build's transition record, as FA-7 already pins the composition per step.
- **How an adaptation is recorded (ADEPT's biased instance).** A mid-build adaptation is the build's own fragment, written through the overlay's existing door, so it is recorded by construction. At each step boundary, the build's witnessed path is compared with its pinned composition (F8), and a deviation files an order.
- **How it is promoted (F3 and F6).** The fragment becomes a new scenario version, with that build as its cornerstone. Builds in flight keep their pin until their next step boundary, then pass a compliance check before they move.
- **What no scenario can change (Azure's required template).** The floor, the stages, `FANOUT_CAP`'s ceiling, the five lens slots and the required legs stay fixed. A scenario's cap may only lower the ceiling.
- **The test the build must run:** plant two chosen scenarios that set `roles.effort.builder` to `high` and `xhigh`; composition must red and name both. Plant one that patches a fixed row; it must red. Plant a build that skips a pinned item without a fragment; the step boundary must file an order.

## Pick

**K7.** No single outside family covers all of E1 to E5. Each part of K7 extends a seam gov already has: the composition, `entry.place`, the FA-7 pin, and agent-cap's lower-only cap. The owner's flexibility cases map onto it as follows:
- **Reordered steps and inserted roles:** `needs` patches, repository roles, and FA-3 stages between gov's.
- **Single agent, parallel set, single step, multi-step, mixed roles:** the shape kinds.
- **Variable agent caps:** a scenario value at or under `FANOUT_CAP`.
- **Adding or removing a lens:** a catalogue row inside a fixed slot.

**The scenario it handles worst: E2 with conflicting patches.** For example, a mobile scenario and a high-precision scenario both set the builder's effort, or both insert a stage between Test and Deploy. K7 catches the conflict at composition, but it only refuses and asks. An unattended run stops there until the owner decides, unless the owner has declared a precedence order between scenarios.

E3 also stays partly open. An adaptation made only in prose, such as a handoff's wording or a lens brief changed for one call, leaves no structural deviation for the step-boundary comparison to see. This is the same kind of gap the earlier prior-art pass found: a change of meaning under an unchanged key and type passes every mechanical check (`flow-roles-adoption [outside]`).

Gov records I relied on, all under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`:
- `2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md`
- `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`
- `2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`

Code cited, under the same worktree:
- `tools\hooks\agent-cap.js`
- `tools\workflows\tier2-review.js`
- `tools\roles\check_roles.py`, where line 90 still holds `WORKFLOW_NAMES` as a closed list in code
