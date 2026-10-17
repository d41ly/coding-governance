# Ownership re-verified: three independent reviewers

**Serves:** research PLAY-dClosedLoop-1

The owner approved PM-10's ownership table and asked for it to be re-verified by three agents working
apart. This record holds the task each reviewer is handed, as `[task]`, and later their returns.

## [task] The task each reviewer is handed

**Context.** dClosedLoop re-architects gov (coding-governance) onto one loop for agentic development. Its
design names 15 chain builds that will build it: dOrderedCharter, dFairHearing, dDeclaredLoop, dBoundRoles,
dTotalRecall, dMindYourWords, dWellOiledMachine, dWitnessedBar, dRankedPlan, dIndexedDesign, dScopedBuild,
dShippedRelease, dTendedCadence, dCalibratedLens and dConvergedCharter. The owner settled that every node a
build must build declares its one owning build (PM-8), approved a proposed table of 351 owners (PM-10), and
then asked, in these words:

> run a review of the ownership table in parallel - instruct 3 independent agents to re-verify ownership

You are one of the three. The other two receive this same task and work apart from you, so your owners
must be your own.

**The rule the table applies.** A node's owner is the chain build that implements the behaviour the node
names or switches. A build that only calls, reads or runs the node is not its owner. Each node has exactly
one owner, and it is one of the 15 builds above.

**The six kinds of node, and where the design declares each:**
- the flow's 81 items: the item tables of flow-steps' nine step sections, `[entry]` to `[adopt]`;
- the 187 policy keys: the catalogue table of v2's `[policies]`, one row each, `review.<stage>` among them as
  one row;
- the 10 extension points: the table of layer-runtime's `[extend]`;
- the 25 tag namespaces: the systems record's `[design-tags]`, its Namespaces and Owners bullets, and the
  namespaced tag system v2's dOrderedCharter row lists;
- the 7 systems: tags, annotations, instruction-writing and role-shapes and memory-structure (the systems
  record's `[design-*]` sections), retrofit (its own record) and the project map (its own record);
- 41 record kinds: intake, card, plan, dupes, seams, feature design, spec, fork, acceptance, scope, verdict,
  attribution, flake, landing, transition, lease, mailbox message, return, act, session binding, journal,
  run record, work order, review, research return, design record, ask, backlog row, decision, gotcha,
  dossier, symbols, callers, annotation index, recall index, baseline, census, ruling, shape-run,
  maintenance record and lexicon declaration. layer-memory's `[contract]` lists most of them in prose; the
  chain rows of v2's `[chain]` name the rest.

The evidence lives in v2's `[chain]` table, whose Stage and Planned units columns say what each build
builds; in each step section of flow-steps; in the layer records (layer-instruction, layer-flow,
layer-roles, layer-memory, layer-library, layer-runtime, layer-expansions); in the systems, retrofit and
project-map records; and in flow-roles and the gap register. Every path is under
`memory/builds/dClosedLoop/build/`, and each file is named `2026-10-1?-build-PLAY-dClosedLoop-1-<name>.md`.

**Read at a pinned commit, and in two phases.** The working tree is being edited while you work, so read
every evidence file only at commit `a169b3350`: `git show a169b3350:<path>` for a whole file, and
`git grep -n <pattern> a169b3350 -- <path>` for a search. Never read an evidence file from the working
tree. This task file is the one exception: it is handed to you there.

1. **Derive, blind.** For every node of the six kinds, derive its owner from the evidence above under the
   rule. Do not open `2026-10-17-build-PLAY-dClosedLoop-1-ownership.md` in this phase: it holds the table
   you are checking. A node whose evidence names no build, or names two, is yours to judge; say how you
   judged it.
2. **Compare.** Only then read the ownership record at `a169b3350`. Its `[items]`, `[keys]`, `[points]`,
   `[tag-namespaces]`, `[systems]` and `[record-kinds]` tables hold the approved owners, and its `[look]`
   table holds the 47 rows the proposal flagged. List every node where your owner differs from the
   approved one.

Also check the population: a node of the six kinds that the records declare and the table omits, or a row
the table holds that the records do not declare.

**Return exactly this shape:**

1. **Summary.** Nodes checked, agreed, disagreed and unsure, for each kind and in total.
2. **Disagreements.** A table, one row per node: the node; its kind; the approved owner; your owner; the
   evidence, as a file and line at `a169b3350` with the words quoted; and why the approved owner breaks the
   rule.
3. **Unsure.** A table, one row per node: the node; its kind; the approved owner; your candidates; and what
   would settle it.
4. **Population.** Each omitted or undeclared node, with its evidence.
5. **Method.** How you derived the owners, which sources you read, and any node you could not place.

Return nothing else, and write nothing in the repository.
