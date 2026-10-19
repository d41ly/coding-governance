# Research: flow and roles adoption, prior art outside gov

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 125's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-7-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-flow-roles-adoption.md`.

---

I found eight mechanism families. My pick for gov combines six of them. It handles worst one case: gov adds an earlier item that changes what an adopter item's input *means*, while the input's key and type stay the same. Every mechanism I found passes that case silently.

All outside sources below were read on 2026-10-19. Real probes ran against pre-commit 4.7.0 and LangGraph 1.2.16 in a scratchpad venv. Nothing was written in the repository.

The six scenarios are labelled:
- **A1:** upstream changes an item the adopter amended.
- **A2:** upstream renames or retires a step or role the adopter depends on.
- **A3:** upstream adds an earlier item that changes the adopter item's inputs.
  - **A3a:** the input's type changes.
  - **A3b:** the input keeps its key and type but its meaning changes.
- **A4:** the adopter disables a gov item another item requires.
- **A5:** the adopter's added item has no witness.
- **A6:** the adopter's role is spawned by a shape that does not know it.

## Families

**F1. A fixed skeleton with typed slots** (upstream owns the outer structure; the user fills declared slots).
- **Systems:**
  - Azure Pipelines `extends` templates. A `stepList` parameter is iterated into the template, which "inserts steps before and after the user steps". A template can rewrite user steps ("Script removed by template"). The required-template check fails "if the pipeline doesn't extend from the required template". It advises anchoring templates to a tag. https://learn.microsoft.com/en-us/azure/devops/pipelines/security/templates
  - GitHub reusable workflows: `{owner}/{repo}/.github/workflows/{file}@{ref}`, called at job level with typed `with`/`secrets`, ten levels at most. https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
  - GitHub composite actions: `uses: OWNER/action@SHA`. https://docs.github.com/en/actions/tutorials/create-actions/create-a-composite-action
    - **Ambiguous:** neither GitHub page says whether a caller can change the inner steps. Only inputs are shown.
  - Maven lifecycle: the phases are fixed. The packaging's goals run first, then the POM's goals "in the same order as they are declared". https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html
  - Maven plugin configuration: parent executions run first, and Maven 4 adds `phase[n]` ordering. https://maven.apache.org/guides/mini/guide-configuring-plugins.html
  - dbt `dispatch`: a root project overrides a package macro only where the package dispatches it, via `search_order`. https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch
- **How it behaves:**
  - **Add:** put steps in a slot, or bind a goal to a phase.
  - **Change or remove a shipped one:** not possible, except through parameters the template offers. Maven has `<inherited>false</inherited>`.
  - **Order:** the skeleton fixes it.
  - **When upstream changes the same element:** the user never owned it, so the change flows through at the pinned ref.
  - **Conflict:** the template silently strips or rewrites user steps at expansion. Only the missing-template case fails a check.
- **Against gov:**
  - A1 cannot occur: the adopter cannot amend at all, which defeats "adjust gov's".
  - A2: the docs don't say what happens to a renamed slot.
  - A3 is silent: the template inserts steps before the user's.
  - A4 is impossible, which is good.
  - A5 can be enforced only by template rewriting.
  - A6 does not apply.

**F2. Keyed override by id, where the user's key wins** (a deep merge over the shipped element).
- **Systems:**
  - GitLab `include` and `extends`. Keys merge deeply, the main file wins, and arrays are replaced ("you cannot add or modify individual items in an array"). `null` removes a key. https://docs.gitlab.com/ci/yaml/includes/ and https://docs.gitlab.com/ci/yaml/yaml_optimization/
  - pre-commit. Per-hook keys override the manifest through `ret.update(dct)` in the source. https://raw.githubusercontent.com/pre-commit/pre-commit/main/pre_commit/repository.py
  - Renovate. The repository's config beats resolved presets, and the last preset in `extends` wins. https://docs.renovatebot.com/config-overview/ and https://docs.renovatebot.com/key-concepts/presets/
  - Maven. A child's execution with the same id "overwritten by child configuration".
  - Claude Code subagents. On a name collision the higher-priority location wins, and plugin agents rank lowest. https://code.claude.com/docs/en/sub-agents
  - dbt. Add a model with the same name, then `+enabled: false` on the package's model; this "can cause compilation errors". https://docs.getdbt.com/reference/resource-configs/enabled
  - Gradle. `enabled = false` marks a task SKIPPED. https://docs.gradle.org/current/userguide/controlling_task_execution.html
- **How it behaves:**
  - **When upstream changes the same element:** the user's key silently wins. My pre-commit probe confirmed it: upstream v2 changed hook `a`'s default args to `--upstream-v2-required-flag`, the user's `args: [--mine]` was kept, and the run exited 0. Keys the user didn't set flow through. An array the user replaced freezes out upstream's later additions.
  - **Conflict:** loud only when a reference dangles. GitLab: "'job1' job needs 'job2' job, but it was not added to the pipeline", and the pipeline fails to start.
- **Against gov:**
  - A1 is silent.
  - A2 is loud for references, but overriding a renamed key leaves an orphan stub. That is from my model only; GitLab's docs don't say.
  - A3 and A5 are silent.
  - A4 is silent where disable means skip (Gradle). Where disable means removal, a dependent fails loudly.
  - A6 is shadowing: a same-named role replaces the shipped one for every spawn. Claude Code also "ignores a field it doesn't recognize without reporting an error".

**F3. A dependency graph checked when it is composed** (the user adds nodes and edges to named upstream nodes).
- **Systems:**
  - Gradle `dependsOn`, `mustRunAfter` and `finalizedBy` (link above).
  - GitLab `needs`, with `optional: true` for a job that may be absent. https://docs.gitlab.com/ci/yaml/
  - LangGraph `add_node` and `add_edge`, and subgraphs added as nodes. https://docs.langchain.com/oss/python/langgraph/use-subgraphs
- **LangGraph probe results:**
  - When upstream renamed `review` to `check`, the user's edge raised `ValueError: Found edge starting at unknown node 'review'`.
  - Adding a node under an upstream name raised `Node 'review' already present.`
  - There is no `remove_edge` API, so changing upstream's wiring means rebuilding the graph.
  - A node with no edges compiled silently and never ran.
- **Against gov:**
  - A1 is silent: there is no notion of an amendment.
  - A2 is loud.
  - A3a is loud only if inputs are typed. A3b is silent.
  - A4 is loud if `requires` is validated.
  - A5 is silent (the orphan-node probe).
  - A6 does not apply.

**F4. A pinned upstream revision, bumped by a validating update.**
- **Systems:**
  - pre-commit: `rev` "is an immutable ref", and `autoupdate` has a `--freeze` option. https://pre-commit.com/
  - GitHub: "Using the commit SHA is the safest option".
  - Renovate: `#tag`.
  - Azure: `ref: refs/tags/v1`.
  - GitLab: `component@version`, and a SHA for `include:project`.
- **pre-commit probe results:**
  - When upstream renamed `b` to `b2`, `autoupdate` refused with "Cannot update because the update target is missing these hooks: b", exited 1, and left `rev: v1`.
  - With the rev forced to v2, the run printed "`b` is not present in repository … Typo? …" and exited 1.
  - The hook upstream added in v2 never ran for the consumer, because new hooks are opt-in. That is a silent miss of A3.
- **Against gov:** this family is about keeping current, not about composition, so it is orthogonal to the others. It makes A2 loud at update time.

**F5. Policy that inspects, rewrites or rejects user definitions when they load.**
- **Systems:**
  - Airflow cluster policies. `dag_policy` and `task_policy` run at DagBag load, can rewire parameters, or "raise AirflowClusterPolicyViolation". https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/cluster-policies.html
  - Azure's template rewriting and required-template check (F1 link).
  - pre-commit's `meta` hooks, which are weaker.
- **Against gov:** this is the enforcement for the fixed set, A4 and A5. It does nothing for A1 to A3.

**F6. Copy-and-own of a shared definition.**
- **Systems:**
  - Jira workflow schemes: "changing a shared workflow scheme will affect all spaces using that scheme", and "Default workflow schemes cannot be configured… create a copy". https://support.atlassian.com/jira-cloud-administration/docs/configure-workflow-schemes/
  - dbt's same-name model plus disabling the package's version (F2 link).
- **When upstream changes the same element:** the copy never receives it, silently.
- **Against gov:** A1 to A3 are all lost silently. A4 is "handled" only because it is frozen.

**F7. Versioning a process that is already running.**
- **Systems:**
  - Temporal patching: `patched()` writes a marker so in-flight runs keep their path, and `deprecatePatch()` later retires it. https://docs.temporal.io/develop/typescript/versioning
  - Temporal Worker Versioning: Pinned versus Auto-Upgrade, with Draining and Drained states. https://docs.temporal.io/worker-versioning
  - Jira: drafts, then "Publish", and Associate starts a migration. The migration's mechanics are undocumented.
- **Against gov:** this covers a build that is mid-flight when a gov update renames the item it is positioned on, which is A2 for a running build.

**F8. A role or action registry keyed by id, looked up when it is dispatched.**
- **Systems:**
  - Backstage scaffolder. Registering an existing id throws a ConflictError ("Template action with ID '…' has already been registered"), and an unknown id throws a NotFoundError ("…is not registered."). Both come from the source: https://raw.githubusercontent.com/backstage/backstage/master/plugins/scaffolder-backend/src/scaffolder/actions/TemplateActionRegistry.ts The docs advise namespacing ids "so that they won't collide with future built-in actions". https://backstage.io/docs/features/software-templates/writing-custom-actions
  - Claude Code subagents: plugin-scoped names (`my-plugin:reviewer`). A resumed session whose agent is gone "continues with the default tools and shows a warning".
  - AutoGen SelectorGroupChat: the model picks the next speaker from each agent's name and description. https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/selector-group-chat.html Teams take any list of agents. https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html
  - CrewAI: tasks name their agent. https://docs.crewai.com/en/concepts/agents
- **Against gov:**
  - A6: none of these systems declares which team shapes a role may run in. An unknown role fails only at dispatch (Backstage) or falls back silently (Claude Code on resume).
  - A2 for a renamed role behaves the same way.

**Ambiguous or undocumented in the sources:**
- GitLab: what happens when an override targets a removed included job.
- Gradle: a `dependsOn` naming a missing task.
- Renovate: how `packageRules` merge in file config.
- CrewAI: a missing YAML key.
- LangGraph: compile-time validation is documented nowhere I read; the probe is the evidence.
- pre-commit: hook order is undocumented. The probe ran the hooks in the order listed.

## Candidates for gov

I ran each candidate against all six scenarios in a throwaway model, `govmodel.py`.

- **K1, keyed override (F2).** It loses A1.
  - The model composed `--packs=core,repo` and dropped gov's new `--require-sbom`, matching the real pre-commit probe.
  - It also loses A4 silently ("dependents run without their input"), and A2 on an amended item leaves a stub.
  - **Rejected.**
- **K2, slots only (F1).** This is P28's extension points opened to adopters. It loses as soon as an adopter adjusts a gov item's args or allowance: the model returns IMPOSSIBLE.
  - **Rejected as the whole answer, because the owner's question includes "or adjusts gov's."** Kept as the place where adopter items attach.
- **K3, typed graph with a pinned revision (F3 + F4).**
  - It loses A1: the model passed it silently.
  - It loses A5: the model, and LangGraph's orphan node, both pass.
  - It catches A2, A3a and A4.
  - **Rejected alone.**
- **K4, fork or copy (F6).** It loses on any gov update: SILENT-WRONG in every upstream scenario. **Rejected.**
- **K5, the combination below.** It extends the seam the owner just settled for instructions, plus P28.
  - **What it combines:**
    - The adopter's own items and roles live in its own namespace (`item.repo.*`, `role.repo.*`), as Backstage and Claude Code namespace theirs.
    - The adopter changes gov's items only through `amends`/`supersedes` edges keyed by tag and pinned to a hash of gov's declaration.
    - Disabling is allowed only for items outside the fixed set that nothing `requires` (F5).
    - Inputs and outputs are typed, and the graph is checked when composed (F3).
    - Roles declare the shapes they run in, and the check happens at composition, not dispatch (F8 moved earlier).
    - The gov revision is pinned, and the update refuses and files orders the way `autoupdate` does (F4).
    - A build in flight stays pinned to the flow revision it started under (F7, Pinned).
  - **Model results:** A1, A2 (both the dependency and the amended target), A3a, A4, A4b, A5, A6 and A6b were all LOUD, each with a named reason.
  - **It loses A3b** (OK, silently).
  - **Its noise cost:** in `pinprobe.py`, a whole-declaration pin goes red when gov changes an unrelated field or adds a route. A pin on only the amended field stays green on a new route that could interact with the adopter's change.
  - **Not tested:** the F7 part needs a test the build must run: a build positioned on `item.test.run-legs`, then a gov update that renames it, and the position engine must resolve or refuse instead of losing the build's position.

## Pick

**K5.** Use a whole-declaration pin, with gov marking each declaration change as editorial or semantic in its upgrade step. That matches the instruction decision and keeps the noise down.

**It handles A3b worst.** A new upstream item changes what an adopter item's input means while the key and type stay the same. Nothing mechanical catches it.

There are two mitigations:
1. Gov versions an output's type whenever its meaning changes (`diff` becomes `diff@2`). That turns A3b into A3a, which fails loudly, but it only works while gov keeps that discipline.
2. The update report lists every new gov item that is an ancestor of an adopter item in the dependency graph. This is computable, but it can only advise.

All probe files are in `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\flowprobe\`:
- `lgscripts\lg.py`, the LangGraph probe;
- `lgscripts\govmodel.py`, the six-scenario model;
- `lgscripts\pinprobe.py`, the pin comparison;
- `up\` and `consumer\`, the pre-commit probe repos.

The design text I mapped to is in `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`:
- `2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md` (F-C, F-D, F-F);
- `2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md` (around line 461);
- `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (P28, line 773).

Sources (all read 2026-10-19):
- [Azure Pipelines: templates for security](https://learn.microsoft.com/en-us/azure/devops/pipelines/security/templates)
- [GitHub: reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows)
- [GitHub: create a composite action](https://docs.github.com/en/actions/tutorials/create-actions/create-a-composite-action)
- [GitLab CI: includes](https://docs.gitlab.com/ci/yaml/includes/)
- [GitLab CI: YAML optimization](https://docs.gitlab.com/ci/yaml/yaml_optimization/)
- [GitLab CI: YAML reference](https://docs.gitlab.com/ci/yaml/)
- [pre-commit](https://pre-commit.com/)
- [pre-commit `repository.py` source](https://raw.githubusercontent.com/pre-commit/pre-commit/main/pre_commit/repository.py)
- [Renovate: config overview](https://docs.renovatebot.com/config-overview/)
- [Renovate: presets](https://docs.renovatebot.com/key-concepts/presets/)
- [Renovate: config presets](https://docs.renovatebot.com/config-presets/)
- [Danger: extending Danger](https://danger.systems/js/usage/extending-danger)
- [Maven: introduction to the lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)
- [Maven: configuring plugins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
- [Gradle: controlling task execution](https://docs.gradle.org/current/userguide/controlling_task_execution.html)
- [dbt: `enabled` config](https://docs.getdbt.com/reference/resource-configs/enabled)
- [dbt: `dispatch`](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch)
- [Temporal: TypeScript versioning](https://docs.temporal.io/develop/typescript/versioning)
- [Temporal: Worker Versioning](https://docs.temporal.io/worker-versioning)
- [Airflow: plugins](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/plugins.html)
- [Airflow: cluster policies](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/cluster-policies.html)
- [Claude Code: subagents](https://code.claude.com/docs/en/sub-agents)
- [CrewAI: agents](https://docs.crewai.com/en/concepts/agents)
- [LangGraph: use subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
- [AutoGen: teams](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html)
- [AutoGen: SelectorGroupChat](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/selector-group-chat.html)
- [Jira Cloud: configure workflow schemes](https://support.atlassian.com/jira-cloud-administration/docs/configure-workflow-schemes/)
- [Atlassian: Configuring workflow schemes](https://confluence.atlassian.com/servicedeskcloud/configuring-workflow-schemes-1097176560.html)
- [Backstage: writing custom actions](https://backstage.io/docs/features/software-templates/writing-custom-actions)
- [Backstage `TemplateActionRegistry.ts` source](https://raw.githubusercontent.com/backstage/backstage/master/plugins/scaffolder-backend/src/scaffolder/actions/TemplateActionRegistry.ts)
