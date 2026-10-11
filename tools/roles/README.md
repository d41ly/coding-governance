<!-- gov:kit roles@1.0 -->
# roles — the role catalogue: one agent definition per role, the workflow table, and the checker

A governed session runs its LLM work through ten declared WORKFLOWS — `orient`, `research`, `reuse`,
`handoff`, `spec-write`, `spec-review`, `build`, `closing-review`, `gate-bar` and `bookkeeping` —
each driven by an agent ROLE, a harness, a program or the main loop. A role is an agent-definition
file under `agents/`: a CONSTANT block its agent starts from, plus front matter saying which
workflow it serves, which inputs it reads, which path class it may write and which sections of the
governing doc it needs. The workflow table, `workflows.toml`, says which roles drive each workflow,
which harness stage spawns as which role, and what refuses a bypass. The library, `roles_lib.py`, is
the one reader of all of it and the one composition of a role with its house overlay
(`render_role`): every route that hands a role to an agent goes through it, so a role reaches an
agent the same way by every route.

## Editing a role

Edit the role's HOUSE OVERLAY, `house/<role>.md`, never the base file under `agents/`. The base
block is the kit's and is overwritten on update; the overlay is yours and is kept. A non-empty
overlay is appended to the base block under a `## House rules` heading when the role is rendered;
an empty or absent one adds nothing. An overlay carries no `#` or `##` heading of its own and no
render token but `{{MEMORY_ROOT}}`. Its size is printed on every check run and never graded.

A base block POINTS at the document that owns a rule — the spec format, the build method, the
review protocol, all under `{{MEMORY_ROOT}}` — and never restates it. Stage protocol (return
schemas, driver verbs, commit trailers, the severity rubric, the probe rules) stays in the harness
that parses the return, because the harness owns its return contract.

## Where the enforcement points live

Each workflow's `enforced-by` names, by description, what refuses a bypass once the catalogue is
wired: the kickoff kit's card writer for `orient`; the hooks kit's write gate, keyed on a role's
`writes`, for `spec-write` and `build`, beside the routed-commits leg for `build`; the hooks kit's
spawn guard for `research`, `spec-review` and `closing-review`; the pre-push hook for `gate-bar`;
the memory-tree hygiene leg for `bookkeeping`. `handoff` and `reuse` read `none` with the reason.
The checker grades that each entry names something, not that the thing exists.

## The handoff renderer

`python handoff.py render --role <name> --build <slug> [--unit <id>] [--card <path>]
[--input <key>=<value>]... [--out <path> | --stdout] [--part full|task]` turns a role and one task
into the prompt its agent is handed (TOOL-aOrientedCast-2). The file holds the role as `render_role`
renders it under `## Role`, then `## Task`: one block per key of the role's `reads`, in declared
order, then one block per `charter` id. A `task:` key is read from the session card's `## task`
field by the kickoff checker's field grammar, a `card:` key from that card's section, a `brief:` key
from the build's brief record, and an `input:` key from `--input`. A required key that resolves to
nothing, an empty value or a placeholder refuses by name and writes nothing; an optional one is named
on the task block's `Not supplied` line.

The card is `--card`, else the file the kickoff checker's `--card --path` prints for
`CLAUDE_CODE_SESSION_ID`, so the card's location stays that checker's rule. The brief record is
`--input prompt=`, else the one file under the build's `prompts/` folder carrying both a
`## The prompt` and a `## The brief` line; two such files refuse.

The file is written under the build's `prompts/` folder as
`<date>-prompt-<id>-<n>-<role without gov->.md`, and its `gov:handoff` marker line carries a hash of
each section. `python handoff.py check <file>` re-derives both hashes and the marker's path;
`--part task` prints the marker and the task section alone, which is what a typed agent spawn
carries. `python handoff.py harness-args <harness>` prints the `roles` object a harness takes: the
union of the `stages` tables of every workflow whose harness is that script, as one line of JSON.
Exit 0, 1 on a refusal, 2 on usage or an unarmed tree; the script's header states what it does not
check.

## The checker

`python check_roles.py [--root <dir>] [--write]`, run as the `roles catalogue` gate leg. It grades
the role files, the overlays and the workflow table against each other in both directions, and every
`charter` id against a `## §<n> — ` heading of the governing doc, which it locates through the
memory-tree conf's `CHARTER` key. It prints one line per defect naming the file and the rule (R0 to
R11, listed in its header with what it does not check), then a summary of every count it graded.
Exit 0 clean, 1 on a defect or an empty catalogue (DEAD PROBE), 2 when the conf or its `CHARTER`
is missing. `--write` re-renders the region below from the table and the front matter, and nothing
else; the check compares the two on every run.

<!-- gen:roles-catalogue -->
**Workflows**, from `workflows.toml`:

| name | stage | driver | harness | roles | stages | enforced-by | trigger |
|---|---|---|---|---|---|---|---|
| orient | 1 | main-loop | /session-kickoff | gov-orienter | — | manifest-check.sh --card --append | once per session, at kickoff, before the first work-unit is opened |
| reuse | 2 | agent | none | gov-reuse-scout | — | none — the scout's trigger is the kickoff opt-in that aScoutedSeam owns | before a new behaviour is designed, when kickoff asks for a scout |
| spec-write | 3 | workflow | {prefix}/workflows/unattended-build.js | gov-spec-writer, gov-builder, gov-spec-reviewer, gov-skeptic, gov-synthesizer | specWriter → gov-spec-writer, disposal → gov-spec-writer, builder → gov-builder, specFinder → gov-spec-reviewer, skeptic → gov-skeptic, synthesis → gov-synthesizer | scratch-guard.js role arm | once per build, after orientation, for every unit whose spec is missing or thin |
| spec-review | 4 | workflow | {prefix}/workflows/tier2-review.js | gov-spec-reviewer, gov-skeptic, gov-synthesizer | specFinder → gov-spec-reviewer, skeptic → gov-skeptic, synthesis → gov-synthesizer | agent-cap.js spawn guard, on the build harness's Workflow call whose roles carry the audit's review keys | after the spec set is written, where the build or its project declares a spec audit |
| build | 5 | workflow | {prefix}/workflows/unattended-unit.js | gov-builder | builder → gov-builder | scratch-guard.js role arm, routed commits name a specced unit | once per unit, in stage order, after its spec is READY |
| closing-review | 6 | workflow | {prefix}/workflows/tier2-review.js | gov-diff-reviewer, gov-skeptic, gov-synthesizer | diffFinder → gov-diff-reviewer, skeptic → gov-skeptic, synthesis → gov-synthesizer | agent-cap.js spawn guard | once per build, after the last unit is terminal, over the cumulative diff |
| gate-bar | 7 | program | bash {prefix}/run-gates/run-gates.sh | — | — | the pre-push hook | once, after the closing review, at the close or the push boundary |
| research | 0 | agent | none | gov-researcher | — | agent-cap.js spawn guard | any time a design must choose between candidates that no existing seam decides |
| handoff | 0 | program | python {prefix}/roles/handoff.py render | gov-session | — | none — a session-to-session message is no tool call the spawn guard sees | any time work passes to another session of this repository |
| bookkeeping | 0 | main-loop | none | — | — | memory hygiene | any time a record, an index or the run state is updated |

**Roles**, from `agents/*.agent.md`:

| role | workflow | writes | reads | charter | agent | returns |
|---|---|---|---|---|---|---|
| `gov-builder` | build | product | input:spec, card:route?, brief:non-goals? | §3, §7, §9, §11, §12 | true | whether the unit was committed, the commit, why when it was not, and which check ran for which gate |
| `gov-diff-reviewer` | closing-review | none | input:diff, input:spec? | §7, §8, §9, §10 | true | concrete findings, each with its file and line, the input that reaches it, the consequence and a proposed fix |
| `gov-orienter` | orient | none | input:question, input:prompt? | §1, §2, §5 | true | the orientation card body: the derived task, the manifest audit line, the rows read, the records found, the bug classes and the open rows |
| `gov-researcher` | research | none | input:question, brief:goal?, brief:non-goals? | §5, §12 | true | the candidates, each with its mechanism, the smallest test that would make it lose and that test's result, then the pick and its reason |
| `gov-reuse-scout` | reuse | none | input:question, task:in?, card:reuse? | §12 | true | the seam to extend, cited by path, or "no existing seam fits" with the evidence |
| `gov-session` | handoff | none | input:question, brief:goal?, task:todo?, card:route? | §2, §3 | false | nothing to the sender; the receiving session acts on the task block and reports in its own session |
| `gov-skeptic` | closing-review | none | input:diff?, input:spec? | §8, §10 | true | a verdict per finding, confirmed or refuted, with the reason observed and, for a confirmed one, its severity |
| `gov-spec-reviewer` | spec-review | none | input:spec, brief:goal?, brief:non-goals? | §7, §8, §9, §10 | true | concrete findings, each with the spec and section, the evidence probed, the consequence and a proposed fix |
| `gov-spec-writer` | spec-write | spec | brief:goal, brief:items, brief:acceptance, brief:gates, brief:non-goals, input:spec?, task:reuse?, card:route? | §1, §7, §9, §12 | true | the units authored, already present and refused, each by its unit id, with the reason for every refusal |
| `gov-synthesizer` | closing-review | review | input:diff?, input:spec? | §8, §16 | true | the report's path and the items it adjudicated, each with its severity and the ids of the findings it covers |

<!-- /gen:roles-catalogue -->
