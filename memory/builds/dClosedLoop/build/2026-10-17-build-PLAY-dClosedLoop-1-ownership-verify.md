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

## [round-1] Round 1: three reviewers, and what they returned

Dispatches 89 to 91 ran `prompts/2026-10-17-prompt-PLAY-dClosedLoop-1-3-spec-reviewer.md`, each a
gov-spec-reviewer handed `[task]` as its spec.

### [return-1a] Dispatch 89, reviewer 1 of 3

Its returned line, derived by the roles kit:

- returned — gov-spec-reviewer · wrote 0 files · 4m04s · 20.7k out · run direct/a4e9719ecf4cd40c8

Its return, verbatim, with any heading demoted below this record's:

I found five defects in the reviewer task: two high, three medium. Neither high one is a wrong count or path. They are about whether the three returns can be compared and audited. Everything below was read at commit `a169b3350`, extracted with `git show a169b3350:<path>` into the session scratchpad. I wrote nothing in the repository and ran no gate.

**Spec reviewed:** `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md`, section `[task]`.

#### What I checked and found correct

- **The pinned commit is the right one.** `git diff a169b3350 36c2a2183 -- …-ownership.md` only appends `[answers]` and `[folded]`. `[answers]` reads "Approve as proposed (Recommended)". So the tables at `a169b3350` are the approved owners. Pinning there also keeps the reviewers away from the owner columns that 36c2a2183 later folded into the evidence files.
- **The counts all match at the pin.** Table rows (minus header and separator) are items 81, keys 187, points 10, tag namespaces 25, systems 7, record kinds 41, `[look]` 47.
  - The flow-steps rows by section are 6+11+12+10+10+13+8+6+5, which is 81.
  - The `[policies]` block has 189 `|` lines, which is 187 rows.
  - The `[extend]` table has 10 rows.
  - The 25 tag namespaces are R-B's twelve (v2's dOrderedCharter row: "reader, level, layer, step, item, role, policy, practice, principle, kind, record, kit") plus the thirteen listed in systems `[design-tags]`.
- **Every named section exists**, including `[design-tags]` and the other `[design-*]` sections at systems.md:224/285/336/388/454, and layer-memory's `### [contract]` at line 299.
- **No policy key is declared outside the catalogue.** I compared the key tables in systems, retrofit, project-map, layer-runtime and layer-memory against v2's catalogue, and every key-shaped first cell is in it. Flow-steps' 81 first cells are its items, not keys.

#### Findings

**F1 (high): the task never says how the ownership rule applies to a record kind.**
- **Evidence:**
  - The task gives one rule: the owner is "the build that implements the behaviour the node names or switches". It adds no reading for record kinds.
  - The approved table used a different reading: `git show a169b3350:…-ownership.md` line 730 says "A kind's owner is the build of its writer". Its `[record-kinds]` rows follow that, e.g. "plan | dRankedPlan | stage | its writer is `plan.record`".
  - Layer-memory `[contract]` (line 299 onward) points the other way: "One write command, `record`, is the only writer of authored record structure". v2's dTotalRecall row builds "the one `record` write command" and the registry.
- **Consequence:** A reviewer can reasonably give most of the 41 kinds to dTotalRecall (it builds the registry and the only writer), or to the build that owns the writing item. The resulting disagreements would come from the definition, not from wrong owners, and the three returns would not be comparable.
- **Fix:** State the reading for each kind in the task. For record kinds, say whether the owner is the build of the writing item or of the registry and write command. For systems and tag namespaces, say "the build that registers or declares it". This states the rule without giving away any owner.

**F2 (high): the return shape cannot show that a reviewer agreed, or that it derived blind.**
- **Evidence:** The return asks only for counts, disagreements and unsure rows. Phase 1's blind owners for agreed nodes are never returned, and the phase split is only an instruction ("Do not open … in this phase") with nothing to witness it.
- **Consequence:** A return with zero disagreements looks the same whether the reviewer derived 351 owners or copied the table. That counts an empty population as coverage, which charter rule [gate] forbids. The agreed counts also cannot be re-computed.
- **Fix:** Have phase 1 return the full derived table: node, kind, owner, and evidence as file:line. Then diff it against the approved tables with a script, outside the agent, and send the reviewer only the differing rows to explain in phase 2. Better still, make the two phases separate dispatches, so the blind return exists before the ownership record is in reach.

**F3 (medium): the population check has no bound, and the task hands the reviewers the population it asks them to check.**
- **Evidence:**
  - The task states "41 record kinds: intake, card, …" as a closed list. Layer-memory at the pin says the opposite: "the list below is the memory layer's, not a closed set" and "one witness record per witness the flow declares (acceptance, verdict, attribution, transition, landing among them)". The ownership record says the same: "the list is not closed".
  - A declared kind missing from the 41 is the triage record:
    - flow-steps:99, "It keys its triage records by the entry's content";
    - flow-steps:115, `plan.triage-rule`'s witness is "the triage record naming its rule";
    - layer-memory `[contract]`, "The records a build writes before its lease (dupes, triage, plan)".
  - flow-steps `[expansions]` (line 537) adds `maintain.*` and `loop.*` cadence programs that are not among the 81 items.
- **Consequence:** Each reviewer will stop the population search somewhere different (the triage record, one witness record per item, the claim ref, Maintain programs), so the three population sections will not line up. Giving them the exact counts and the 41 names also anchors the blind derivation on the population under review.
- **Fix:**
  - Give a membership test for each kind instead of the list. For example: "a record kind is any noun that layer-memory `[contract]` or a v2 `[chain]` row calls a record or kind, or that a flow-steps Witness cell names as a record".
  - Alternatively, declare that the stated sources are authoritative and limit the population check to them.
  - Either way, drop the counts from the blind phase.

**F4 (medium): rows the owner decided are not marked as settled.**
- **Evidence:**
  - `grep '| decided |' own.md` returns 13 rows: six `entry.*` items on PM-9, six `life.*` items on RT-3, and the intake record kind.
  - flow-steps:86–88 says "dDeclaredLoop builds the step's items, and `entry.intake`'s hook stays dWellOiledMachine's (PM-9)", while `[look]` notes "dRankedPlan's row also describes the hook".
  - flow-steps:466 says "Runtime executes the owner's controls (dWellOiledMachine, RT-3)".
- **Consequence:** The bare rule invites reviewers to dispute what the owner has already decided. Those rows would be reported as rule breaks, when the review protocol treats a resolved fork as by design.
- **Fix:** Add a line saying that an owner's recorded decision (PM-n, RT-n) at the pin settles the owner. A reviewer who thinks the rule conflicts with one reports it in a separate "decided, conflicts with rule" list, not in Disagreements.

**F5 (medium): the record does not say what happens to the three returns.**
- **Evidence:**
  - The record says only "and later their returns". It names no synthesis step, no agreement threshold (unanimous, 2 of 3), and no refute pass, although REVIEW-PROTOCOL's Tier-2 pattern is find → verify → synthesize.
  - Commit 36c2a2183 has already folded the approved owners into five owner fields (flow-steps, v2's catalogue, `[extend]`, the systems Owners bullet, layer-memory's kind table) and into `map.py`.
- **Consequence:** A confirmed disagreement has no defined route. It is not said whether it re-opens PM-10 as an owner question, or which owner fields and map checks change. The verification therefore has no outcome that can fail.
- **Fix:** Add a `[disposition]` section that defines:
  - the agreement rule, for example a node is flagged when at least 2 of 3 reviewers differ from the approved owner;
  - a batched skeptic pass that tries to refute each flagged row;
  - the result: the surviving rows go to the owner as one PM question, and only on approval are the five owner fields edited and `map.py --check` re-run.

### [return-1b] Dispatch 90, reviewer 2 of 3

Its returned line, derived by the roles kit:

- returned — gov-spec-reviewer · wrote 0 files · 4m34s · 25.6k out · run direct/adb66b5d6dfb35701

Its return, verbatim, with any heading demoted below this record's:

I found four defects in the reviewer task in `2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md`, section `[task]`. Two are high severity: the population check can't catch the omissions that actually exist, and the blind phase can leak the table it is meant to check. I read every file at the pinned commit `a169b3350` (copied into my session scratchpad), ran no gate and wrote nothing in the repository.

**What checks out.**
- All the counts match the pinned files: 81 items with no duplicate ids, 187 catalogue rows, 10 `[extend]` points, and 12 + 13 = 25 tag namespaces.
- The 15 build names match v2's `[chain]` rows, and every cited section exists. `[extend]` is at layer-runtime line 812, the `[design-*]` sections at systems lines 224–454, and `[contract]` at layer-memory line 299.
- The ownership record's six tables hold 81/187/10/25/7/41 rows, and `[look]` holds 47 rows. These reconcile with the per-table "yes" flags (7 items + 30 keys + 10 record kinds).
- The owner approved the table "as proposed", and `git diff a169b3350 HEAD` on the ownership record only adds lines. So the pinned table really is the approved one.

---

**F1 (high). The population is defined as exactly the table's own population, so the population check cannot fail for items, and has no rule for record kinds.**
- **Section:** `[task]`, the six-kinds list ("the flow's 81 items: the item tables of flow-steps' nine step sections") and the record-kind list typed out inline.
- **Evidence:**
  - At the pin, layer-expansions declares 24 more items in the same `| Item | Actor | Does | Witness | Routes |` tables. They are `maintain.*` (lines 221–227, 7), `loop.*` (256–261, 6), `release.*` (382–387, 6) and `kits.*` (450–454, 5).
  - flow-steps `[expansions]` (line 537 on) calls them items: "each item below attaches at a core point".
  - project-map line 676 defines the owner check as covering "a node a build must build … an item", with no carve-out for expansions.
  - `git grep -n -E 'maintain\.(lease|read|record)|loop\.gather|release\.pick' a169b3350 -- *-ownership.md` matches only policy-key rows (`maintain.reading-tree` and similar), never these items. So the Maintain stage's items have no owner row at all.
  - Record kinds have the same problem. At the pin, v2 `[chain]` names "seen-red records" (line 1118), "the spec-audit kind" (1112) and "change record" (1111). layer-memory line 327 names "triage records", and layer-expansions `release.record` writes "the release record". None of these is among the 41.
  - The ownership record's own `[rule]` says the record-kind list "is not closed", yet the task hands reviewers that same list of 41.
- **Consequence:** reviewers who follow the definition confirm the table's 81 items and 41 kinds by construction. The 24 items are never reported. Record-kind population findings will differ between the three reviewers by interpretation, not by error, so their returns can't be compared.
- **Fix:**
  - Define items as every id in any `Item | Actor` table across the design records, or state explicitly that expansion items are excluded and why.
  - Give a membership rule for a record kind (for example, "a kind with a writer item or a home in a record"), and don't type the 41 names into the task.
  - Probe: `git grep -n -E '^\| Item \| Actor' a169b3350 -- memory/builds/dClosedLoop/build/` should list exactly the tables the definition covers.

**F2 (high). The prescribed search method leaks the hidden table during the blind phase.**
- **Section:** `[task]` "Read at a pinned commit, and in two phases". It prescribes `git grep -n <pattern> a169b3350 -- <path>` and says "every path is under `memory/builds/dClosedLoop/build/`", while only forbidding *opening* the ownership record.
- **Evidence:**
  - `git grep -n 'placement.check' a169b3350 -- memory/builds/dClosedLoop/build/` prints `…-ownership.md:83:| \`placement.check\` | key | dRankedPlan |…` and `:267:` (the approved owner), plus the proposal script's dictionary at `:644`.
  - `git grep -c dTendedCadence … -- memory/builds/dClosedLoop/build/` returns 24 hits in the ownership record, more than any other file.
  - Adding the pathspec `':!*-ownership.md'` drops that file to 0 hits.
- **Consequence:** any directory-wide search for a node or a build name shows the approved owner. Independence is lost without anyone noticing, and the three reviewers' agreement can't be told apart from contamination.
- **Fix:** prescribe `git grep -n <pattern> a169b3350 -- memory/builds/dClosedLoop/build/ ':!*-ownership.md'` for phase 1. Also ask each return to state that no phase-1 output showed the ownership record.

**F3 (medium). The rule is undefined for the kinds where most flagged rows sit.**
- **Section:** `[task]` "The rule the table applies".
- **Evidence:** the rule is "implements the behaviour the node names or switches", which has no stated meaning for a record kind or a tag namespace. Is the owner the build that writes the record, the one that registers its schema, or the one that declares the namespace?
  - The ownership record flags exactly these splits. `lease` and `mailbox message` are each marked "judgment" with the note "layer-memory lists [it] among Runtime's kinds" while dDeclaredLoop builds it.
  - 10 of the 41 record kinds are flagged.
  - The systems record's Owners bullet credits whole kinds of tag to dOrderedCharter while other builds "register" namespaces.
- **Consequence:** many disagreements will come from reading the rule differently rather than from wrong owners. The required column "why the approved owner breaks the rule" can't be judged.
- **Fix:** state, for each kind, what "implements" means: for example, for a record kind, the build that declares its schema and writer; for a tag namespace, the build that registers it and its extractor. This can be done without revealing the table's evidence ranking.

**F4 (medium). The record has no rule for combining the three returns, and the returns point at a superseded location.**
- **Section:** the record header ("…and later their returns") and the `[task]` return shape.
- **Evidence:** no section says what a 1-of-3 or 2-of-3 disagreement leads to (an owner question, a skeptic round as the review protocol's refutation step expects, or a change to the fold). Commit `36c2a2183` has since copied the owners into the owner fields of five files: flow-steps (81 rows), v2's catalogue (187), layer-runtime `[extend]` (10), systems' Owners bullet, and a new layer-memory table (41). The return shape only cites the pinned ownership table.
- **Consequence:** the verification has no criterion that can fail. A confirmed disagreement has no defined route into the fields the map generator now reads.
- **Fix:**
  - Add a section that sets the adjudication rule, for example: a disagreement two or more reviewers report goes to a skeptic and then to the owner.
  - Require each accepted change to name the field's file and line at the current HEAD.
  - Probe the build must run: after the fold, the map's owner check reports no `owner=?` and no node with two owners.

All file paths are under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`, read at `a169b3350`. The spec under review is the untracked `2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md` in that same folder.

### [return-1c] Dispatch 91, reviewer 3 of 3

Its returned line, derived by the roles kit:

- returned — gov-spec-reviewer · wrote 0 files · 5m13s · 27.6k out · run direct/a60ffc9267914d82c

Its return, verbatim, with any heading demoted below this record's:

I found two High, three Medium and two Low defects in the ownership-verify task spec. All of the spec's counts and section references check out at `a169b3350`. The defects are in how the task protects blindness, states the rule, fixes the population and handles the returns. I ran no gate, wrote nothing in the repository, and every probe below is a read at `a169b3350` or `HEAD`.

**Spec:** `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md`, section `[task]`.

**A mistake of mine, outside the repository.** My first snapshot command wrote into the parent session's scratchpad root (`.../1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/`). It overwrote eight files that were already there: `flow-steps.md`, `architecture-v2.md`, `layer-runtime.md`, `systems.md`, `layer-memory.md`, `ownership.md`, `retrofit.md` and `project-map.md`. Each now holds that record as it was at `a169b3350`. I can't restore what they held before. Everything after that went to `scratchpad/specreview-ownverify/` only.

#### What I checked and found true at `a169b3350`
- **15 builds:** v2 `[chain]` has 15 rows, the same names as the task.
- **81 items:** across the nine flow-steps sections (`[entry]` 6, `[plan]` 11, `[design]` 12, `[build]` 10, `[test]` 10, `[deploy]` 13, `[breakpoint]` 8, `[lifecycle]` 6, `[adopt]` 5).
- **187 keys:** the `[policies]` catalogue has 187 key rows, `review.<stage>` among them.
- **10 points:** layer-runtime `### [extend]`, at line 812.
- **25 tag namespaces:** the 12 in the v2 row, plus the 12 the systems `[design-tags]` Namespaces bullet adds, plus `marker`.
- **7 systems:** five `[design-*]` sections, plus retrofit and the project map.
- **Totals:** 41 record kinds, 47 `[look]` rows (7 items, 30 keys, 10 record kinds), 351 nodes.
- **Pinned table matches the fold for items and keys:** the pin predates the fold commit `36c2a2183`, and the table at the pin is the approved one ("Approve as proposed"). For items (81) and keys (187), the folded `Owner` fields at `HEAD` diff identical to the pinned table. I did not check points, namespaces or record kinds.
- **Header:** the `Serves` line matches its siblings.

#### Findings

**F1 (High): The blind phase leaks the answers through the task's own search instruction.**
- **Where:** the "Read at a pinned commit" paragraph and phase 1. Phase 1 says not to open the ownership record. But the task tells verifiers to search with `git grep ... -- <path>`, and it describes the evidence by a file pattern (`2026-10-1?-build-PLAY-dClosedLoop-1-<name>.md`) that also matches the ownership record.
- **Probe:**
  - `git grep -n "entry.intake" a169b3350 -- memory/builds/dClosedLoop/build/ | grep -c ownership.md` printed `6`.
  - `git grep -n '`review.pin`' a169b3350 -- 'memory/builds/dClosedLoop/build/2026-10-1?-build-PLAY-dClosedLoop-1-*.md' | grep -c ownership.md` printed `2`. One hit is `ownership.md:219: | `review.pin` | breakpoint | dFairHearing | row | dFairHearing's row cites it, where the stage rule would give it to dCalibr…`
  - The working tree the verifier sits in is at `HEAD`. `git show HEAD:...flow-steps.md | grep "^| Item"` prints `| Item | ... | Then | Owner |`. So one stray `Read` of a working-tree file shows every approved owner.
  - Smaller leaks: the pinned `project-map.md` holds 9 rendered `owner=d…` lines.
- **Consequence:** a search that looks blind returns the approved owner and its reasoning. Three "independent" verifiers can end up anchored on the proposal, and their agreement then proves nothing.
- **Fix:**
  - Give every search pathspec `':!memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership.md'`.
  - Name the leaking sources (the project map's rendered lines) as off-limits in phase 1.
  - Better: the orchestrator creates a detached worktree at `a169b3350` with the ownership record deleted, and runs phase 1 from there. That way the working tree is the pin.

**F2 (High): Nothing shows that phase 1 was blind, and the derivation itself is never returned.**
- **Where:** phases 1–2 and "Return exactly this shape".
- **Evidence:** the return holds only summary counts, disagreements, unsure rows and population. The 351 blind-derived owners are never recorded before the table is opened. Nothing fixes phase 1's output before phase 2 begins.
- **Consequence:**
  - A verifier that reads the table first and "agrees" cannot be told apart from a blind one, so the `agreed` count can't fail.
  - The three returns can't be compared node by node.
- **Fix:** before phase 2, each verifier writes its full derivation (node, kind, owner, evidence) to a file outside the repository and returns that file's path and sha256. Or run the two phases as two separate spawns, the second handed the first's file. The merge step then checks that each `agreed` count matches the file.

**F3 (Medium): The task leaves out the narrower rule the table applied to record kinds, so verifiers will disagree over interpretation, not evidence.**
- **Where:** "The rule the table applies".
- **Evidence:**
  - The pinned table's instrument (`ownership.md:730`) says: "A kind's owner is the build of its writer."
  - dTotalRecall's v2 row builds "the record-kind registry (per kind: tag, layer, home, id rule, schema, writer, readers, lifecycle, check)". Under the task's one-line rule ("implements the behaviour the node names"), that registry is a defensible claim to every kind.
  - The table gives 26 of the 41 kinds to builds other than dTotalRecall (`uniq -c`: dWellOiledMachine 6, dDeclaredLoop 4, dIndexedDesign 4, …).
  - Tag namespaces have the same split between the registrar and the declaring build.
- **Consequence:** up to 26 disagreements per verifier could come from reading the rule differently, mixed in with real evidence errors.
- **Fix:** state how the rule reads for each kind (a record kind belongs to its writer's build, a namespace to its registering build). Or, if leaving that open is deliberate, add a "rule reading" column to the Disagreements table so interpretation splits are kept separate.

**F4 (Medium): The record-kind population is handed over as a closed list copied from the table under review, which defeats the population check.**
- **Where:** the six-kinds list, "41 record kinds: intake, card, …"
- **Evidence:**
  - A diff of the task's list against the pinned `[record-kinds]` first column shows the same 41 names in the same order.
  - The table itself says "the list is not closed" (`ownership.md:30-31`, `:729`).
  - The pinned flow-steps names record kinds written by items that are not among the 41:
    - "the triage record naming its rule" (line 115, `plan.triage-rule`; also lines 99 and 101);
    - "the recommendation record" (lines 121, 170, 218 and 278).
- **Consequence:** verifiers check the table's population against the table's own list, so an omitted kind can only be found by someone who ignores the brief.
- **Fix:** give the sources and the claimed count, not the names. Ask verifiers to list the kinds themselves from layer-memory `[contract]`, the chain rows, and the "Proven by" columns of flow-steps.

**F5 (Medium): The spec says nothing about what happens to the three returns once they come back.**
- **Where:** the opening ("and later their returns") and the return shape.
- **Evidence:**
  - There is no merge rule (for example, a row reopens when one verifier, or two, disagree with quoted evidence).
  - There is no skeptic pass, which the charter's [risk] rule requires for a substantive review.
  - The owner approved "as proposed" (`HEAD` `[answers]`), but the spec doesn't say that any change needs a new owner ask.
  - The Disagreements table has no column for the approved row's evidence class. So a challenge to one of the 13 owner-settled rows (6 `entry.*` rows under PM-9, 6 `life.*` rows under RT-3, the `intake` kind) looks the same as a new defect.
- **Consequence:** the three returns produce no defined outcome, and the review has no criterion that can fail.
- **Fix:**
  - State the merge and adjudication rule and the skeptic pass.
  - State that a changed owner goes back to the owner.
  - Have verifiers report disagreements with settled rows separately.

**F6 (Low): Two templated catalogue rows go unnamed.**
- **Where:** "the 187 policy keys … `review.<stage>` among them as one row".
- **Evidence:** the pinned catalogue also has `review.<stage>.effort` and `budgets.*`. The task singles out only `review.<stage>`.
- **Consequence:** a verifier who expands those two rows gets a population that is not 187, and reports a false population gap.
- **Fix:** list all three templated rows as one row each.

**F7 (Low): "v2" doesn't resolve to a file under the stated pattern.**
- **Where:** the evidence paragraph.
- **Evidence:** the file is `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`, and `-architecture-v0` and `-v1` also exist. The task never spells out `architecture-v2`.
- **Fix:** name the file in full.

#### Supporting paths
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership.md` (read at `a169b3350`)
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md` (read at `a169b3350` and at `HEAD`)
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` (read at `a169b3350` and at `HEAD`)
- My snapshots: `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/specreview-ownverify/`

## [misfire] Why round 1 did not re-verify the table

- **Each reviewer audited the task, not the table.** A spec reviewer hunts defects in the spec it is handed,
  and the handoff handed it `[task]` as `input:spec`. So all three returned findings about the brief: four,
  five and seven of them, none an owner derived. The owner's ask was not done by round 1.
- **The class is filed** as `task-handed-as-the-spec-is-reviewed-not-done`. A task that must be performed
  goes to a role whose input is a question, the researcher, or through a harness's context, never through a
  reviewer's spec slot.
- **Dispatch 91 also wrote into the parent's scratchpad root,** about 110 record snapshots, 8 of them over
  files already there. No script read those 8, so nothing was lost that counted. The class is filed as
  `subagent-scratch-overwrites-the-parents-files`. Round 2's task gives each verifier its own folder.

## [found-1] What round 1 found that bears on the table

The three audits agree on defects in the table itself, not only in the brief:
- **Its item population misses the expansions' items.** layer-expansions declares 24 items in tables headed
  `| Item | Actor |`: `maintain.*` 7, `loop.*` 6, `release.*` 6 and `kits.*` 5 (dispatch 90's F1). The map
  missed them for the same reason: its item extractor and its census read flow-steps alone.
- **Its record kinds miss some the records name:** the triage record (all three), the recommendation record
  (91), and the seen-red, change and release records (90).
- **Its rule is ambiguous for record kinds.** It says "the build of its writer", yet dTotalRecall builds the
  registry and the one `record` command every kind passes through (all three).
- **Two templated catalogue rows** besides `review.<stage>` count as one key each: `review.<stage>.effort` and
  `budgets.*` (91).
- **What the brief got wrong:**
  - its blind phase could leak the table through a directory-wide search or a stray working-tree read;
  - it returned no derivation, so agreement could not be witnessed;
  - it named no disposition for the returns.

Round 2 answers each of these.

## [task-2] Round 2: the re-verification itself

- **The role is the researcher,** whose input is a question it answers. Its handoff is
  `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-1-researcher.md`.
- **It reads a worktree pinned at `a169b3350`,** in the session's scratchpad, from which the ownership
  record is removed in both the index and the tree. A search cannot reach the table.
- **The rule is stated for each kind,** the owner's settled rows are named, the population is found by
  membership rather than handed over as a list, and the expansions' items are inside it.
- **Each verifier returns its full derived table** as a TSV file in its own folder, with the file's sha256,
  so agreement is computed by script, node by node.

The question, as handed:

**Context.** dClosedLoop re-architects gov (coding-governance) onto one loop for agentic development. Its
design names 15 chain builds that will build it: dOrderedCharter, dFairHearing, dDeclaredLoop, dBoundRoles,
dTotalRecall, dMindYourWords, dWellOiledMachine, dWitnessedBar, dRankedPlan, dIndexedDesign, dScopedBuild,
dShippedRelease, dTendedCadence, dCalibratedLens and dConvergedCharter. The owner settled that every node a
build must build declares its one owning build (PM-8), approved a table of owners (PM-10), and then asked, in
these words:

> run a review of the ownership table in parallel - instruct 3 independent agents to re-verify ownership

You are one of three verifiers. The other two receive this same task and work apart from you, so the owners
you derive must be your own. Your task is the re-verification itself: derive an owner for every node.

**Where to read.** A worktree pinned at commit `a169b3350` sits at `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/verify-wt`. Read every file there, under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/verify-wt/memory/builds/dClosedLoop/build/`. The ownership table you are checking has been removed from that
worktree. Do not reach it by any other route: no `git show` of it, and no reads of the main working tree,
whose files now carry the approved owners. The project-map record's rendered map lines carry owners an older
derivation inferred, so do not use them as evidence.

**The rule.** A node's owner is the one chain build that implements what the node names or switches. A build
that only calls, reads or runs the node is not its owner. Read it, for each kind of node, as:
- an item: the build that builds the item's program step;
- a policy key: the build that implements the behaviour the key switches;
- an extension point: the build that builds the point's registration;
- a tag namespace: the build that registers the namespace with its extractor;
- a system: the build its own record names as its owner;
- a record kind: the build that registers the kind, with its schema and its writer, through its layer's
  contract. dTotalRecall builds the registry and the `record` command that every kind passes through, and
  that alone does not make it every kind's owner.

**Rows the owner settled.** PM-9 gives the entry step's items to dDeclaredLoop, and `entry.intake`'s hook to
dWellOiledMachine. RT-3 gives the lifecycle step's items to dWellOiledMachine (flow-steps `[lifecycle]`). Take
those owners as given. If you believe the rule would assign one elsewhere, say so in your rule-conflicts
list, not in your table.

**The population: find it by membership.**
- Items: every row of every table whose header begins `| Item | Actor |` in the design records. That covers
  flow-steps' step sections and layer-expansions' expansion programs both.
- Policy keys: every row of the catalogue table in `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
  `[policies]`. Each templated row, such as `review.<stage>`, `review.<stage>.effort` and `budgets.*`, counts
  as one key.
- Extension points: the rows of layer-runtime's `### [extend]` table.
- Tag namespaces: the list in v2's dOrderedCharter row ("the namespaced tag system (...)"), plus the systems
  record's `[design-tags]` Namespaces bullet.
- Systems: the five `### [design-*]` sections of the systems record, plus retrofit and the project map.
- Record kinds: every noun that layer-memory's `[contract]`, a row of v2's `[chain]`, or a "Proven by" or
  "Witness" cell in flow-steps or layer-expansions names as a record kind, or as a record a step writes. Say
  which kinds you judged in or out, and why.

**Return in this shape:**
1. **The derived table, as a file.** Write it to a new folder of your own inside `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/verify2`, named with a
   suffix you pick, as `owners.tsv`: one line per node, tab-separated, with the columns `kind`, `node`,
   `owner`, `evidence` and `settled`.
   - `kind` is item, key, point, namespace, system or record-kind.
   - `node` is an item's or a key's tag as its table writes it, a point's first cell, or a namespace's,
     system's or record kind's name in lower case.
   - `evidence` is a file and line in the worktree, with the deciding words quoted.
   - `settled` is yes for the rows the owner settled, and no for the rest.
   - Write every node, not only the hard ones.
2. **Your final message:** the file's path and its sha256; your counts by kind; the nodes whose membership
   you judged, and why; your rule conflicts; and your method, meaning what you read, in what order, and
   anything you could not place.

Write nothing in the repository, and keep every scratch file inside your own folder, never at the
scratchpad's root.

## [disposition] What the returns lead to

- **Per verifier:** its population, and its agreement with the approved table, node by node.
- **Across verifiers:** where two or three name an owner other than the approved one, a gov-skeptic tries to
  refute the disagreement. Each survivor goes to the owner in one question, before any owner field changes.
  A disagreement only one verifier names is listed for the owner and not escalated.
- **Population:** a node two or three verifiers find, and the table lacks, is proposed to the owner in the
  same question, with its majority owner.
- **No owner field changes before the owner answers,** and the map's owner check is run after the fold.

## [round-2] Round 2: three verifiers, and what they returned

Dispatches 92, 93 and 95 ran `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-1-researcher.md`, each a
gov-researcher handed `[task-2]`'s question. Each named its folder by a suffix it picked: v-kestrel, v-heron
and v-osprey. The third waited for agent-cap to free a slot, so it ran as dispatch 95, after the order review.

### [return-2a] Dispatch 92, verifier 1 of 3, v-kestrel

Its returned line, derived by the roles kit:

- returned — gov-researcher · wrote 0 files · 16m40s · 114.7k out · run direct/a8dc62a43ba33f323

Its return, verbatim, with any heading demoted below this record's:

I derived an owner for all 408 nodes and wrote them to the table. None of the 12 settled rows breaks the rule outright, but three show strain, listed under rule conflicts.

#### 1. The file

`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/verify2/v-kestrel/owners.tsv`

sha256 `5e1af4f4f105bfb1d58e2ddee397b3499712e3ce7f68ef83320194804af23e2e`

It has a header line, then 408 rows with the columns `kind`, `node`, `owner`, `evidence`, `settled`. Every evidence quote was found by an exact-substring search in the pinned worktree, and the generator stops if any quote is missing. Every row that cites v2's `[chain]` lands on the owner's own chain row (checked). The generator `gen.py` sits beside the table, in my own folder.

#### 2. Counts

| kind | count | settled |
|---|---|---|
| item | 107 | 12 |
| key | 187 | 0 |
| record-kind | 72 | 0 |
| namespace | 25 | 0 |
| point | 10 | 0 |
| system | 7 | 0 |

By owner: dTotalRecall 54, dShippedRelease 53, dWellOiledMachine 44, dDeclaredLoop 43, dWitnessedBar 36, dCalibratedLens 33, dIndexedDesign 25, dOrderedCharter 25, dRankedPlan 24, dTendedCadence 22, dBoundRoles 20, dScopedBuild 19, dMindYourWords 6, dFairHearing 4, dConvergedCharter 0.

dConvergedCharter owns no node. It builds the record-kind factory and its gate, and under the rule that is not registering any one kind.

#### 3. Membership judgments

**Items (107 nodes from 106 rows):**
- In: 81 flow-steps tags and 26 layer-expansions tags.
- Split: the row `` `kits.install`, `kits.update` `` holds two tags, so I counted two nodes.
- Out: flow-roles' six `| Item | Actor |` tables (flow-roles.md:59–113). Their rows are retired checklist numbers ("1 to 4"), not tags, and flow-steps says "Checklist numbers are retired".
- Out: the 17 such tables in `research-*.md` files. Those are research inputs, not design records.

**Keys (187):** every row of v2 `[policies]` (v2:652–838). `review.<stage>`, `review.<stage>.effort` and `budgets.*` count once each. 97 keys have no chain row or owner table that names them, so I derived their owner from the behaviour the key switches. Those evidence cells quote that behaviour, not the key.

**Points (10):** the rows of layer-runtime `[extend]`. Three of layer-expansions' eight `[core-points]` (reading/fix classes, grants, install targets) are fields on existing Runtime rows, and cadence items already is the tenth row. The other four (verdict backends, release slot, version slot, memory homes) are not `[extend]` rows. All eight are out as separate points.

**Namespaces (25):** R-B's twelve plus systems' thirteen. `record` appears in both lists and counts once. Out: `chain`, `gap`, `orient`, `build`, `skill` and `bug class`, which the map and other records use but neither list names.

**Systems (7):** tags, code annotations, instruction writing, role workflow shapes, memory structure, retrofit, project map.

**Record kinds:** 72 in. My test for inclusion: named as a kind, or as a record a step writes, in layer-memory `[contract]`, a v2 `[chain]` row, or a Proven-by/Witness cell. I merged synonyms:
- per-SHA post-merge verdict and pre-push "bar record" → verdict
- snapshot commit → card
- population files → baseline
- class-claim ref → claim
- fork record and reconstructed decisions → decision
- lease record → lease
- mailbox posts → mailbox message

Out:

| Excluded | Why |
|---|---|
| keep record | named only in a Routes cell and integrations' contract table |
| remote-verdict, delivery, grant | named only in integrations' contract table |
| metric set, proposal list | intermediate outputs |
| allow record, lander marker | hook or lander artifacts no contract declares |
| SHAs, commits, refs, tags, deployment id, pushed ref | git or outside objects |
| schema checks, predicates, wiring and version verdicts | checks, not records |
| design index, house index, plan view, relation graph, slice manifest | views or indexes the sources never call a kind |
| reuse entry | layer-memory says it is an instruction unit the registry does not list |
| spawn marker, role index, progress cell, parents' records | not a record this item writes |

#### 4. Rule conflicts

**Settled rows** (I kept the owner's assignment in each case):
- **`entry.intake`:** PM-9 gives the entry step's items to dDeclaredLoop and the intake hook to dWellOiledMachine. This item's actor *is* that hook, so I wrote dWellOiledMachine. If the owner meant the item itself stays dDeclaredLoop, this one row flips.
- **`entry.claim`:** the step rule gives dDeclaredLoop, but the compare-and-swap claim ref it takes is designed into dTotalRecall (layer-memory: "dTotalRecall owes both refs (`gap-mem-13`)").
- **`entry.orient` and `entry.place`:** the rule gives dDeclaredLoop, yet dBoundRoles' row builds the scout that composes the card. dRankedPlan's row builds placement ("a disposition for every request, made by `placement`").

**Other rows:**
- **The breakpoint step, all 8 items → dCalibratedLens.** Read per item instead of per step, `review.lens`, `review.refute`, `review.report` and arguably `review.pin` go to dFairHearing. They are the stages of its harness, and its row maps `review.pin`'s arguments.
- **Items inside stage steps whose mechanism another build's row names.** I kept the stage build for each:
  - `plan.lease` and `build.unit-lease`: the lease engine is dDeclaredLoop's.
  - `test.merge`: it is the lander's `--prepare`.
  - `deploy.released`: event waits are dWellOiledMachine's.
  - `build.distill`: the decision log is dTotalRecall's.
  - `design.seams`: the house index is dTotalRecall's.
  - `review.cost`: it writes shape-run rows.
- **The adopt section has no stage.** I gave its four `adopt.*` items to dTotalRecall (retrofit's adopt program). `test.seed` went to dWitnessedBar, although it sits in the adopt table.
- **The Loop Review.** dTendedCadence's row says "Maintain and the Loop Review delivered as cadence steps". dCalibratedLens's row says "the weekly Loop Review" and owns `gap-review-02`. I gave `loop.*` and the Loop Review record to dCalibratedLens.
- **Where two records disagree:**
  - Layer-memory `[contract]` says Runtime registers lease and mailbox message. Layer-runtime `[settled]` puts both under dDeclaredLoop. I chose dDeclaredLoop.
  - Layer-memory lists the run record as a core kind, while layer-expansions has observability register it. I chose dTendedCadence.
  - dRankedPlan's row still claims the prompt-submit hook that PM-9 moved. I gave the intake kind to dRankedPlan, but its writer is now dWellOiledMachine's hook.
- **`return` → dWellOiledMachine.** Runtime's contract registers it, but dBoundRoles owns the return contract's schema.
- **`memory.default-load` → dWellOiledMachine.** dWellOiledMachine's row builds the session-start load (PM-7), while dTotalRecall's row says "the default load of the charter and the card".
- **Keys implemented inside another build's step:**
  - `reuse.propose` and `decisions.major` → dTotalRecall, though they take effect at `build.unit-pass` and `build.distill`.
  - `retrofit.reconstruct`'s default `on-touch` arm runs in `build.unit-pass`.
  - `placement.check` is also run by dBoundRoles' driver.
  - `review.unverified`, `review.left-shift` and `review.blocks` → dCalibratedLens through `review.dispose` and the breakpoint, though the harness side is arguable for dFairHearing.
- **Systems whose records name several builds:**
  - Retrofit's `[owners]` names seven. I took v2's "whose ledger dWitnessedBar builds".
  - Instruction writing names four. I took dOrderedCharter, which builds the schema and renderer.
  - Role shapes names four. I took dBoundRoles, which builds the registry.

#### 5. Method

**Order of reading:**
1. The worktree's build listing.
2. Flow-steps in full.
3. v2: `[chain]`, `[contracts]`, `[policies]`, the revision notes, `[layers]` and `[principles]`.
4. Layer-expansions: design, settled, revised and open sections.
5. Layer-runtime: `[settled]`, `[design]` through `[act]`, `[extend]`, `[contract]`, `[policies]`, `[build]`.
6. Systems: `[cross]`, `[design-*]`, `[answers]`.
7. Layer-memory: `[contract]`, `[asks]`, `[revised-*]`.
8. Retrofit: `[cross]` through `[keys]`.
9. Project-map: `[design]` and `[owners]`.
10. Layer-library `[settled-lb]`, layer-instruction R-B, the gap register in full, and targeted searches. Research returns were read only to learn what a key means.

**How I built the table:** a script read only the pinned worktree. It extracted the populations by table membership and joined them against my owner map, refusing any missing or extra key or namespace. It then resolved every evidence quote to a file and line.

**Disclosures:**
- Listing the scratchpad root showed files named `ownership*.md` and `own.md`. I read none of them.
- Project-map's `[reload-pointer]` probe output (lines 1136–1144) prints an older generator's step owners. I saw it while reading, but no evidence cell uses it.

**Could not place with direct evidence:**
- `integrations.tracker` (no record names a build; I gave dShippedRelease as integrations' adapter builder).
- The `design record` kind (dTotalRecall).
- The `decision` kind (dIndexedDesign; dBoundRoles is the alternative).
- The `disposition` kind (dCalibratedLens).
- The `owner request` kind (dWellOiledMachine).
- The `actor kinds` point (dWellOiledMachine by Runtime's contract; dDeclaredLoop's loop definition is the alternative).

### [return-2b] Dispatch 93, verifier 2 of 3, v-heron

Its returned line, derived by the roles kit:

- returned — gov-researcher · wrote 0 files · 14m04s · 94.3k out · run direct/a6907abe57526497e

Its return, verbatim, with any heading demoted below this record's:

I derived an owner for all 402 nodes and wrote them to the table. Every evidence quote was checked by script against the exact line it cites (0 misses). I also checked the item and key rows against their source tables: none missing, none extra.

**File:** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/verify2/v-heron/owners.tsv`
**sha256:** `4385284e405ce614946413564cb9a2dfb4f0ac9f92fb4d843297afdeb9190dc2`

The scripts I used are in `.../verify2/v-heron/work/`. Nothing was written in the repository.

#### Counts by kind
| kind | rows |
|---|---|
| item | 107 |
| key | 187 |
| point | 10 |
| namespace | 25 |
| system | 7 |
| record-kind | 66 |
| **total** | **402** (12 marked settled) |

By owner: dTotalRecall 55, dShippedRelease 49, dDeclaredLoop 45, dWellOiledMachine 41, dWitnessedBar 34, dCalibratedLens 33, dOrderedCharter 27, dIndexedDesign 23, dTendedCadence 22, dRankedPlan 21, dBoundRoles 21, dScopedBuild 14, dFairHearing 11, dMindYourWords 6, dConvergedCharter 0.

#### Membership judgements
- **Items**
  - **In:** every tagged row of flow-steps' 9 tables (81 items) and layer-expansions' 4 tables (26).
  - **One row split into two:** the row that writes `` `kits.install`, `kits.update` `` is two tags, so I counted it as two items.
  - **Out, flow-roles:** its six `| Item | Actor |` tables list numbered checklist rows ("1 to 4"), not tags. flow-roles:42 keeps them only as the record of a revisit, and flow-steps:15 says "Checklist numbers are retired."
  - **Out, research returns:** the 15 research files with `| Item | Actor |` tables are research returns, not design records.
- **Keys:** 187 catalogue rows. `review.<stage>`, `review.<stage>.effort` and `budgets.*` count once each.
- **Namespaces:** 25 — R-B's twelve plus systems:231's thirteen. `record` appears in both lists and is counted once.
- **Record kinds: 66 in.**
  - **In, from layer-memory [contract]:** 35 kinds.
  - **In, from v2's chain rows:** override, exception, instruction change record, tag index, build readme, baseline, census, shape-run, seen-red, maintenance, value ledger, fleet register, kit-release.
  - **In, from Proven-by and Witness cells:** triage, recommendation, diff, re-entry, overlap, selection, routing, comparison, owner disposition, control request, workspace, ruling, loop review, fleet, currency, receipt, release, release exit. "Witness cells" includes the Witness column of flow-steps' `[transitions]` table, which is where re-entry, routing and comparison come from.
- **Merged into an existing kind, not counted again:**
  - fork record and decision-log row → decision
  - research record → research return
  - report → review
  - class record → gotcha
  - population files → baseline
  - mailbox posts → mailbox message
  - placement disposition → intake
  - intake entry → intake
  - ledger blob → value ledger
  - the executor's quiesce record → act
- **Out:**
  - Refs, SHAs, commits and blobs: the claim ref, deleted refs, the snapshot commit, the prepared merge, the base SHA, pushed refs, the tag and notes blob.
  - Checks, verdict lines and fields: the version-check verdict, the cost field, the outcome class, the wake's witness.
  - Things never called a record in the source cells: inventory, roster, core result, plan view.
  - Reconstructed records, which is an `origin` value, not a kind.
  - Reuse entry, which LR-6 makes an instruction unit and the registry does not list.
  - Relations.
  - keep record, which appears only in a Routes cell.
  - remote-verdict, delivery, grant and outbox order, which are named only in layer-expansions' contract tables. Those tables are outside the three sources you listed.

#### Rule conflicts
1. **entry.intake.** The rule would give it to dWellOiledMachine, because the whole item is the hook (gap-rt-14). I kept PM-9's dDeclaredLoop. Separately, v2's dRankedPlan row (v2:1119) also claims "the prompt-submit hook writing each owner prompt verbatim to the session's intake log", which contradicts PM-9.
2. **Where an item's mechanism belongs to another build.** I used the step's own build unless a record names the item's function:
   - `*.recommend` and `*.reason` → dCalibratedLens (v2:1124, gap-flow-12)
   - `build.acceptance` → dDeclaredLoop ("acceptance re-run by the executor")
   - `review.pin`, `review.lens`, `review.refute`, `review.report`, `review.dispose` → dFairHearing
   - `review.cost` → dCalibratedLens (gap-review-11)
   - `build.ratify`, `build.distill`, `deploy.distill` and `decisions.major` → dTotalRecall (gap-mem-02, "the major-decision log"). This is a judgement call: the step's own build (dScopedBuild, dShippedRelease) is the alternative.
   - Items that only call another build's mechanism stayed with their step's build: `deploy.notify`, `deploy.snapshot`, `deploy.unlease`, `plan.lease`.
3. **Loop Review.** v2:1123 has dTendedCadence deliver "Maintain and the Loop Review" as cadence steps. v2:1124 and review-system:269 keep "the weekly Loop Review" with dCalibratedLens. I gave the `loop.*` items to dCalibratedLens.
4. **Kinds layer-memory:376 assigns to Runtime.**
   - lease and mailbox message: dDeclaredLoop builds their grammar and writers (v2:1113, layer-runtime:1013), so I chose dDeclaredLoop.
   - run record: layer-memory:373 calls it core (RUN.md), but layer-expansions:211 makes it observability's. I chose dTendedCadence.
5. **Keys where the build named in the chain row is not the one that implements the behaviour.**
   - `roles.shape-enforce` → dWellOiledMachine, which builds the binding.
   - `memory.default-load` → dWellOiledMachine (PM-7 hook), although dTotalRecall's row names "the default load".
   - `context.on-full` → dDeclaredLoop, per its chain row, although Runtime's `[sessions]` reads it.
   - `build.closes` → dShippedRelease. dDeclaredLoop only refuses presets on it.
   - `preset` → dDeclaredLoop. A plain search hits dFairHearing's `preset` argument, which is a different thing.
6. **Retrofit has no single owner in its own record.** RF-1 spreads its parts over seven builds. I named dWitnessedBar, which owns the ledger factory at its core.

#### Method and what I could not place
- **Order of reading:**
  1. v2 `[policies]`, `[chain]`, `[owed]` and `[layers]`.
  2. flow-steps in full.
  3. flow-roles' tables.
  4. layer-expansions in full.
  5. layer-runtime `[schedule]` through `[build]`.
  6. layer-memory `[contract]` and its revisions.
  7. systems `[cross]` and `[design-*]`.
  8. layer-instruction R-B.
  9. retrofit `[design]` through `[answers]`.
  10. project-map `[design]`, `[owners]`, `[reload]` and `[fixes]`.
  11. layer-library `[design]`.
  12. review-system `[adjudication]` and `[where]`.
  13. layer-flow `[uncovered]`.
  14. gap-register rows, by targeted search.
- **Not read whole:** the other files in the build folder (research returns, compaction and atlas records, the session log). I did not read the ownership table by any route, and the project map's rendered owners played no part.
- **Weakly placed:**
  - `design record`: no build names it; dTotalRecall by the memory contract alone.
  - `integrations.tracker`: no chain row names it; I gave it to dShippedRelease.
  - `patch.ratify`: dTendedCadence, but it also governs patch builds that enter through entry.
  - `owner disposition`: dCalibratedLens.
  - `review.fold`: dIndexedDesign.
  - the `role harnesses` point: dWellOiledMachine against dBoundRoles' shapes registry.
  - the `kit` and `kind` namespaces: dOrderedCharter by systems:268, though dShippedRelease builds the kit factory.

### [return-2c] Dispatch 95, verifier 3 of 3, v-osprey

Its returned line, derived by the roles kit:

- returned — gov-researcher · wrote 1 file · 18m36s · 134.6k out · run direct/a7e7aa8fdfea6aa74

Its return, verbatim, with any heading demoted below this record's:

The table is written: an owner for 405 nodes, each with evidence. Every quoted citation was checked by script against the line it cites in the pinned worktree, and all of them match. My item and policy-key populations match the records exactly. My total differs from the approved table's 351, mostly because I counted 69 record kinds.

**File:** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/verify2/v-osprey/owners.tsv`
**sha256:** `543a744c8925b4906a380187502148141112312337e30b193d48ec55f842c074`

The other files in that folder are scratch: `build_table.py` assembles the table and checks every quote, and `check.py` checks the populations. I wrote nothing in the repository.

#### Counts by kind
| Kind | Rows |
|---|---|
| item | 107 (12 settled) |
| key | 187 |
| record-kind | 69 |
| namespace | 25 |
| point | 10 |
| system | 7 |
| **total** | **405** |

By owner: dTotalRecall 54, dShippedRelease 51, dDeclaredLoop 44, dWellOiledMachine 39, dCalibratedLens 37, dWitnessedBar 34, dOrderedCharter 25, dIndexedDesign 24, dRankedPlan 23, dTendedCadence 21, dBoundRoles 21, dScopedBuild 19, dFairHearing 8, dMindYourWords 5, dConvergedCharter 0.

#### Membership I judged
**Items**
- **In:** flow-steps' 9 item tables (81 items) and layer-expansions' 4 programs (26 items).
- **Split:** I counted the row `kits.install`, `kits.update` as two items.
- **Out:** flow-roles has 6 tables whose header starts `| Item | Actor |`, but their rows are checklist numbers ("1 to 4", "5, 6"). flow-steps:15 says "Checklist numbers are retired", so they name no node. Research returns are not design records. roles.md and session-model use other headers.

**Keys:** all 187 catalogue rows, each template row counted once.

**Namespaces:** 25. That is v2's twelve plus the systems record's thirteen additions.

**Record kinds in (69):**
- **From layer-memory `[contract]`:**
  - the core list;
  - the kinds Flow and Runtime register;
  - the optional components' dossier, symbols, callers and recall index;
  - the annotation index.
- **From v2 chain rows:** baseline, census, shape-run, seen-red, landing, maintenance, value ledger, build README, override.
- **From Proven-by and Witness cells:** dupes, triage, diff, inventory, roster, overlap, core result, selection, routing, merge, comparison, card snapshot, workspace, ruling, claim, disposition, recommendation, instruction proposal, keep, loop review, release, release routing, release exit, kit-release, currency, fleet, receipt.

**Record kinds out:**
- "the lexicon": it names a component, not a kind.
- remote-verdict, delivery, grant, fleet-register rows and outbox orders: they appear only in layer-expansions' contract tables, which are not among the three named sources.
- reconstructed records: that is an `origin` value, not a kind.
- the patch intake: it is the intake kind.
- Generic or non-record witnesses: "the command's record", the owner's request record, the metric set, the proposal list, pinned SHAs, the cost field, a deployment id, refs and commits.
- v2 `[contracts]`' per-SHA deploy and verify records and gate health: that section is not a named source.

#### Rule conflicts (settled rows only)
- **`entry.orient`:** the rule points to dBoundRoles. v2:1114 says "the orientation scout composing the card in a sidechain at session start".
- **`entry.place`, `entry.place-check`, `entry.place-owner`:** the rule points to dRankedPlan. v2:1119 says "placement: a disposition for every request, made by `placement` … its facts checked by `placement.check`".
- **`entry.claim`:** the rule points to dTotalRecall. layer-memory:332 says "dTotalRecall owes both refs (`gap-mem-13`)", meaning the claim ref.
- **`entry.intake`:** dRankedPlan's row (v2:1119) also claims "the prompt-submit hook writing each owner prompt verbatim to the session's intake log", which competes with PM-9's dWellOiledMachine.
- **`life.close`:** its terminal transition is arguably dDeclaredLoop's. layer-runtime:1006-1008 says "The terminal states … stay dDeclaredLoop's".

#### Method
**Reading order:**
1. v2 in full: `[chain]`, `[policies]`, the revision notes, `[floor]` and `[owed]`.
2. flow-steps in full.
3. layer-expansions in full.
4. layer-runtime `[schedule]` through `[build]`.
5. layer-memory `[contract]` through `[views]`.
6. systems `[cross]` through `[answers]`.
7. retrofit `[cross]` through `[gaps-proposed]`.
8. project-map `[cross]` through `[keys]`, `[reload-pointer]` and `[fixes]`. I used its prose only, not its rendered map lines.
9. The library and layer-flow records, the gap register's rows, and targeted parts of the walkthrough and flow records.

I did not read the ownership table, the main working tree, or the other two verifiers' folders.

**Rule I applied:**
- A step's items go to the build whose v2 Stage is that step.
- A design record or chain row overrides that when it names the item's tag, or the mechanism that is the item's whole job. On that basis:
  - every `*.recommend` and `*.reason` item goes to dCalibratedLens (gap-flow-12, "the stage-exit recommendation");
  - `review.pin`, `review.lens`, `review.refute` and `review.report` go to dFairHearing;
  - `review.dispose` and `review.cost` go to dCalibratedLens.
- An item that only calls another build's engine (a lease verb, the mailbox, an event wait) keeps its step's build.

**Low-confidence placements, flagged for review:**
- **`design.inventory` and the inventory kind:** I gave both to dRankedPlan because it owns gap-flow-04, "no re-design inventory of completed work".
- **`review.fold`, `review.design.rounds`, `review.design.round-count`:** dIndexedDesign, from "design review by policy".
- **`patch.ratify`:** dIndexedDesign. No record names an owner.
- **`integrations.tracker`:** dShippedRelease. I could not place it with direct evidence.
- **The retrofit system:** dWitnessedBar, from v2:350 "ledger dWitnessedBar builds". RF-1 says its parts belong to several builds, so it names no single owner.
- **`loop.*`:** dCalibratedLens ("the weekly Loop Review"), although dTendedCadence's row says it delivers the Loop Review.
- **The `kit` namespace:** dShippedRelease, from project-map:666-667, which puts kits among the namespaces whose owning build lands after dTotalRecall.
- **`hooks.bypass`:** dDeclaredLoop, as part of the default floor (walkthrough:129), rather than dWitnessedBar's "bypasses recorded".
- **Record kinds where two records disagree:**
  - return: dWellOiledMachine by layer-runtime's contract, though dBoundRoles owns the return template;
  - lease: dDeclaredLoop's lease grammar, though layer-memory says Runtime registers it;
  - run record: observability's (dTendedCadence) per layer-expansions, though layer-memory lists it as core.
- **Disagreements between records:** v2 `[owed]` asks whether the kit confs fold into the policy file, which is still undecided. layer-memory:376 says Runtime registers the lease and the mailbox message, while v2:1113 puts both grammars in dDeclaredLoop. I followed v2.

## [compare-2] The three tables, compared

The tables are filed byte for byte beside this record, and each hash is the one its verifier returned:

- `2026-10-18-build-PLAY-dClosedLoop-1-owners-v-kestrel.tsv`: v-kestrel's, from dispatch 92, 408 nodes, sha256 `5e1af4f4f105bfb1d58e2ddee397b3499712e3ce7f68ef83320194804af23e2e`
- `2026-10-18-build-PLAY-dClosedLoop-1-owners-v-heron.tsv`: v-heron's, from dispatch 93, 402 nodes, sha256 `4385284e405ce614946413564cb9a2dfb4f0ac9f92fb4d843297afdeb9190dc2`
- `2026-10-18-build-PLAY-dClosedLoop-1-owners-v-osprey.tsv`: v-osprey's, from dispatch 95, 405 nodes, sha256 `543a744c8925b4906a380187502148141112312337e30b193d48ec55f842c074`

- **The approved table is read as the proposal wrote it,** `ownership.json`, from the script in
  `2026-10-17-build-PLAY-dClosedLoop-1-ownership.md` `[instrument]`, run at `248ef556d`.
- **v-heron's evidence cells spell each record's date as a number,** such as `11194-build-` for
  `2026-10-14-build-`. The comparison reads owners only, so it is unaffected. The skeptics' briefs restore the
  dates.
- **The run below is from the filed tables.** It prints byte for byte what the first run, from the
  verifiers' own folders, printed.

```python
"""Compare round 2's derived owner tables with the approved one, and with each other, node by node.

Usage: python compare_r2.py <approved ownership.json> <owners.tsv> [<owners.tsv> ...]   (from the worktree root)

The approved table is the proposal's output, which the owner approved as proposed. A node is keyed by its kind
and a normalised name: lower case, backticks and the trailing record/s stripped, spaces and hyphens folded.
Prints each verifier's population and agreement, the nodes two or more verifiers own differently from the
approved owner (escalated, by the disposition), the nodes one verifier does (listed), and the population the
approved table lacks.
"""
import collections
import json
import pathlib
import re
import sys

KIND = {"items": "item", "keys": "key", "points": "point", "tagns": "namespace", "systems": "system",
        "kinds": "record-kind"}


# One node's two names, seen in the verifiers' tables: a system's full title, a kind named by its component.
ALIAS = {("system", "role-workflow-shapes"): ("system", "role-shapes"),
         ("system", "code-annotations"): ("system", "annotations"),
         ("record-kind", "lexicon"): ("record-kind", "lexicon-declaration")}


def norm(kind, node):
    n = node.strip().strip("`").lower()
    if kind == "record-kind":
        n = re.sub(r"\s+records?$", "", n)
        n = re.sub(r"\s+kind$", "", n)
    key = (kind, re.sub(r"[\s_-]+", "-", n))
    return ALIAS.get(key, key)


approved = {}
for sec, rows in json.load(open(sys.argv[1], encoding="utf-8")).items():
    for r in rows:
        approved[norm(KIND[sec], r["node"])] = r["owner"]
tables = []
for path in sys.argv[2:]:
    t = {}
    for i, line in enumerate(open(path, encoding="utf-8")):
        cells = line.rstrip("\n").split("\t")
        if i == 0 and cells[0].strip().lower() == "kind":
            continue
        if len(cells) < 3 or not cells[0].strip():
            continue
        t[norm(cells[0].strip().lower(), cells[1])] = cells[2].strip()
    # A table is named by its verifier's suffix, from its folder in the scratchpad or its filed name.
    tables.append((re.findall(r"(?<![a-z])v-[a-z]+", pathlib.Path(path).as_posix())[-1], t))

print(f"approved nodes {len(approved)}")
for path, t in tables:
    common = set(t) & set(approved)
    agree = sum(1 for k in common if t[k] == approved[k])
    print(f"{path}: nodes {len(t)}, in the approved table {len(common)}, agreeing {agree} "
          f"({100 * agree / max(1, len(common)):.1f}%), not in it {len(set(t) - set(approved))}, "
          f"approved and missing here {len(set(approved) - set(t))}")
    print("  by kind: " + ", ".join(f"{k} {v}" for k, v in sorted(collections.Counter(k for k, _ in t).items())))
for (pa, ta), (pb, tb) in [(tables[i], tables[j]) for i in range(len(tables)) for j in range(i + 1, len(tables))]:
    common = set(ta) & set(tb)
    print(f"pairwise {pa} vs {pb}: {sum(1 for k in common if ta[k] == tb[k])} of "
          f"{len(common)} agree")

against = collections.defaultdict(list)
for path, t in tables:
    for k, own in t.items():
        if k in approved and own != approved[k]:
            against[k].append((path, own))
esc = {k: v for k, v in against.items() if len(v) >= 2}
one = {k: v for k, v in against.items() if len(v) == 1}
print(f"\nescalated, two or more verifiers against the approved owner: {len(esc)}")
for k, v in sorted(esc.items()):
    print(f"  {k[0]} {k[1]}: approved {approved[k]}; " + "; ".join(f"{who} {own}" for who, own in v))
print(f"listed, one verifier against: {len(one)}")
for k, v in sorted(one.items()):
    print(f"  {k[0]} {k[1]}: approved {approved[k]}; " + "; ".join(f"{who} {own}" for who, own in v))
extra = collections.defaultdict(list)
for path, t in tables:
    for k, own in t.items():
        if k not in approved:
            extra[k].append((path, own))
print(f"\npopulation the approved table lacks, by how many verifiers found it: "
      f"{dict(collections.Counter(len(v) for v in extra.values()))}")
for k, v in sorted(extra.items(), key=lambda x: (-len(x[1]), x[0])):
    owners = collections.Counter(own for _, own in v)
    print(f"  {len(v)}x {k[0]} {k[1]}: " + ", ".join(f"{o} {n}" for o, n in owners.most_common()))
```

```text
$ python -X utf8 compare_r2.py ownership.json 2026-10-18-build-PLAY-dClosedLoop-1-owners-v-heron.tsv 2026-10-18-build-PLAY-dClosedLoop-1-owners-v-kestrel.tsv 2026-10-18-build-PLAY-dClosedLoop-1-owners-v-osprey.tsv
approved nodes 351
v-heron: nodes 402, in the approved table 350, agreeing 321 (91.7%), not in it 52, approved and missing here 1
  by kind: item 107, key 187, namespace 25, point 10, record-kind 66, system 7
v-kestrel: nodes 408, in the approved table 350, agreeing 331 (94.6%), not in it 58, approved and missing here 1
  by kind: item 107, key 187, namespace 25, point 10, record-kind 72, system 7
v-osprey: nodes 405, in the approved table 349, agreeing 325 (93.1%), not in it 56, approved and missing here 2
  by kind: item 107, key 187, namespace 25, point 10, record-kind 69, system 7
pairwise v-heron vs v-kestrel: 371 of 395 agree
pairwise v-heron vs v-osprey: 377 of 394 agree
pairwise v-kestrel vs v-osprey: 376 of 397 agree

escalated, two or more verifiers against the approved owner: 23
  item build.recommend: approved dScopedBuild; v-heron dCalibratedLens; v-osprey dCalibratedLens
  item deploy.recommend: approved dShippedRelease; v-heron dCalibratedLens; v-osprey dCalibratedLens
  item design.reason: approved dIndexedDesign; v-heron dCalibratedLens; v-osprey dCalibratedLens
  item design.recommend: approved dIndexedDesign; v-heron dCalibratedLens; v-osprey dCalibratedLens
  item plan.reason: approved dRankedPlan; v-heron dCalibratedLens; v-osprey dCalibratedLens
  item plan.recommend: approved dRankedPlan; v-heron dCalibratedLens; v-osprey dCalibratedLens
  item review.fold: approved dCalibratedLens; v-heron dIndexedDesign; v-osprey dIndexedDesign
  item test.reason: approved dWitnessedBar; v-heron dCalibratedLens; v-osprey dCalibratedLens
  item test.recommend: approved dWitnessedBar; v-heron dCalibratedLens; v-osprey dCalibratedLens
  key annotations.delivery: approved dBoundRoles; v-heron dTotalRecall; v-kestrel dTotalRecall; v-osprey dTotalRecall
  key instructions.slices: approved dOrderedCharter; v-heron dBoundRoles; v-kestrel dBoundRoles
  key instructions.task-charter: approved dOrderedCharter; v-heron dBoundRoles; v-kestrel dBoundRoles; v-osprey dBoundRoles
  key integrations.tracker: approved dTotalRecall; v-heron dShippedRelease; v-kestrel dShippedRelease; v-osprey dShippedRelease
  key memory.default-load: approved dTotalRecall; v-heron dWellOiledMachine; v-kestrel dWellOiledMachine
  key review.build.when: approved dCalibratedLens; v-heron dScopedBuild; v-kestrel dScopedBuild; v-osprey dScopedBuild
  key review.design.round-count: approved dCalibratedLens; v-heron dIndexedDesign; v-kestrel dIndexedDesign; v-osprey dIndexedDesign
  key review.design.rounds: approved dCalibratedLens; v-heron dIndexedDesign; v-kestrel dIndexedDesign; v-osprey dIndexedDesign
  key roles.shape-enforce: approved dBoundRoles; v-heron dWellOiledMachine; v-kestrel dWellOiledMachine; v-osprey dWellOiledMachine
  namespace kit: approved dOrderedCharter; v-kestrel dShippedRelease; v-osprey dShippedRelease
  record-kind acceptance: approved dScopedBuild; v-heron dDeclaredLoop; v-kestrel dDeclaredLoop
  record-kind decision: approved dTotalRecall; v-kestrel dIndexedDesign; v-osprey dIndexedDesign
  record-kind intake: approved dWellOiledMachine; v-heron dRankedPlan; v-kestrel dRankedPlan; v-osprey dRankedPlan
  record-kind run: approved dWellOiledMachine; v-heron dTendedCadence; v-kestrel dTendedCadence; v-osprey dTendedCadence
listed, one verifier against: 17
  item build.acceptance: approved dScopedBuild; v-heron dDeclaredLoop
  item build.distill: approved dScopedBuild; v-heron dTotalRecall
  item build.ratify: approved dScopedBuild; v-heron dTotalRecall
  item deploy.distill: approved dShippedRelease; v-heron dTotalRecall
  item design.inventory: approved dIndexedDesign; v-osprey dRankedPlan
  item entry.intake: approved dWellOiledMachine; v-heron dDeclaredLoop
  item review.dispose: approved dCalibratedLens; v-heron dFairHearing
  item review.lens: approved dFairHearing; v-kestrel dCalibratedLens
  item review.pin: approved dFairHearing; v-kestrel dCalibratedLens
  item review.refute: approved dFairHearing; v-kestrel dCalibratedLens
  item review.report: approved dFairHearing; v-kestrel dCalibratedLens
  key hooks.bypass: approved dWitnessedBar; v-osprey dDeclaredLoop
  key patch.ratify: approved dTendedCadence; v-osprey dIndexedDesign
  key review.left-shift: approved dCalibratedLens; v-heron dFairHearing
  key review.unverified: approved dCalibratedLens; v-heron dFairHearing
  key run.on-owner-question: approved dBoundRoles; v-kestrel dWellOiledMachine
  point role-harnesses: approved dWellOiledMachine; v-osprey dBoundRoles

population the approved table lacks, by how many verifiers found it: {3: 43, 2: 9, 1: 19}
  3x item kits.currency: dShippedRelease 3
  3x item kits.cut: dShippedRelease 3
  3x item kits.fleet: dShippedRelease 3
  3x item kits.install: dShippedRelease 3
  3x item kits.offer: dShippedRelease 3
  3x item kits.update: dShippedRelease 3
  3x item kits.version: dShippedRelease 3
  3x item loop.file: dCalibratedLens 3
  3x item loop.gather: dCalibratedLens 3
  3x item loop.lease: dCalibratedLens 3
  3x item loop.price: dCalibratedLens 3
  3x item loop.propose: dCalibratedLens 3
  3x item loop.record: dCalibratedLens 3
  3x item maintain.direct: dTendedCadence 3
  3x item maintain.file: dTendedCadence 3
  3x item maintain.lease: dTendedCadence 3
  3x item maintain.levels: dTendedCadence 3
  3x item maintain.patch: dTendedCadence 3
  3x item maintain.read: dTendedCadence 3
  3x item maintain.record: dTendedCadence 3
  3x item release.approve: dShippedRelease 3
  3x item release.pick: dShippedRelease 3
  3x item release.promote: dShippedRelease 3
  3x item release.record: dShippedRelease 3
  3x item release.route: dShippedRelease 3
  3x item release.verify: dShippedRelease 3
  3x record-kind build-readme: dTotalRecall 3
  3x record-kind comparison: dShippedRelease 3
  3x record-kind currency: dShippedRelease 3
  3x record-kind fleet: dShippedRelease 3
  3x record-kind kit-release: dShippedRelease 3
  3x record-kind loop-review: dCalibratedLens 3
  3x record-kind overlap: dIndexedDesign 3
  3x record-kind override: dOrderedCharter 3
  3x record-kind receipt: dShippedRelease 3
  3x record-kind recommendation: dCalibratedLens 3
  3x record-kind release: dShippedRelease 3
  3x record-kind routing: dWitnessedBar 3
  3x record-kind seen-red: dWitnessedBar 3
  3x record-kind selection: dWitnessedBar 3
  3x record-kind triage: dRankedPlan 3
  3x record-kind value-ledger: dCalibratedLens 3
  3x record-kind workspace: dWellOiledMachine 3
  2x record-kind claim: dTotalRecall 2
  2x record-kind core-result: dScopedBuild 2
  2x record-kind diff: dIndexedDesign 2
  2x record-kind disposition: dCalibratedLens 2
  2x record-kind exception: dOrderedCharter 2
  2x record-kind fleet-register: dShippedRelease 2
  2x record-kind inventory: dRankedPlan 2
  2x record-kind release-exit: dShippedRelease 2
  2x record-kind roster: dIndexedDesign 2
  1x record-kind card-snapshot: dDeclaredLoop 1
  1x record-kind change: dOrderedCharter 1
  1x record-kind control-request: dWellOiledMachine 1
  1x record-kind decision-log: dTotalRecall 1
  1x record-kind decision-log-row: dTotalRecall 1
  1x record-kind exit: dShippedRelease 1
  1x record-kind instruction-change: dOrderedCharter 1
  1x record-kind instruction-proposal: dOrderedCharter 1
  1x record-kind keep: dCalibratedLens 1
  1x record-kind merge: dWitnessedBar 1
  1x record-kind outbox-order: dShippedRelease 1
  1x record-kind owner-disposition: dCalibratedLens 1
  1x record-kind owner-request: dWellOiledMachine 1
  1x record-kind re-entry: dIndexedDesign 1
  1x record-kind re-entry-diff: dIndexedDesign 1
  1x record-kind release-routing: dShippedRelease 1
  1x record-kind reuse-proposal: dTotalRecall 1
  1x record-kind tag-index: dOrderedCharter 1
  1x record-kind wake-witness: dWellOiledMachine 1
```

## [disposition-amended] The disposition, amended before the population went to the owner

- **The 23 escalated owners went to a skeptic, as set.** Dispatch 96 tried to refute each
  (`build/2026-10-18-build-PLAY-dClosedLoop-1-ownership-skeptic.md`).
- **The population faced a skeptic too, which the disposition did not set.** It proposed the 52 nodes two
  or three verifiers found straight to the owner. Their evidence showed candidates that may be one node under
  two names, such as `release` and `release-exit`, or `fleet` and `fleet-register`. So dispatch 97 tested each
  on membership, identity and owner first (`build/2026-10-18-build-PLAY-dClosedLoop-1-ownership-population.md`).
- **The skeptics are 2 of the review's 5 verify agents** (`[bound]`).

## [pm-12] What the skeptics left standing, put to the owner

Both skeptics' verdicts are in their records' `[verdicts]`: dispatch 96 in
`2026-10-18-build-PLAY-dClosedLoop-1-ownership-skeptic.md`, and dispatch 97 in
`2026-10-18-build-PLAY-dClosedLoop-1-ownership-population.md`. This section is what goes to the owner as PM-12.
No owner field changes before the owner answers.

### [pm-12-moves] The 13 disputed owners the skeptic confirmed

| Id | Node | Kind | Approved | Proposed | Why |
| --- | --- | --- | --- | --- | --- |
| F1 | `build.recommend` | item | dScopedBuild | dCalibratedLens | v2's dCalibratedLens row builds "the stage-exit recommendation" and "the recommendation's score computed and its reasoning returned by the step's producing role" |
| F2 | `deploy.recommend` | item | dShippedRelease | dCalibratedLens | as F1 |
| F3 | `design.reason` | item | dIndexedDesign | dCalibratedLens | as F1, and dCalibratedLens owns gap-flow-12, "The driver reasons in four items" |
| F5 | `plan.reason` | item | dRankedPlan | dCalibratedLens | as F3 |
| F6 | `plan.recommend` | item | dRankedPlan | dCalibratedLens | as F1 |
| F8 | `test.reason` | item | dWitnessedBar | dCalibratedLens | as F3 |
| F9 | `test.recommend` | item | dWitnessedBar | dCalibratedLens | as F1 |
| F11 | `instructions.slices` | key | dOrderedCharter | dBoundRoles | the key removes method-document reads (gap-orient-07), which is dBoundRoles's gap; the skeptic's confidence is moderate |
| F12 | `instructions.task-charter` | key | dOrderedCharter | dBoundRoles | systems: "dBoundRoles builds the role static block and the single carry", and the single-carry check reads the key |
| F15 | `review.build.when` | key | dCalibratedLens | dScopedBuild | the key was minted in dScopedBuild's own fork B3, for its unit "The closing review, recorded" |
| F18 | `roles.shape-enforce` | key | dBoundRoles | dWellOiledMachine | the key's values apply at act binding, and systems says "dWellOiledMachine the binding, the reconcile" |
| F20 | `acceptance` | record kind | dScopedBuild | dDeclaredLoop | v2: "each item's witness is declared by the loop (dDeclaredLoop)", and acceptance is one of those witness records |
| F23 | `run record` | record kind | dWellOiledMachine | dTendedCadence | layer-expansions: observability's journal reader writes it, and dTendedCadence delivers observability |

The seven stage items move as one: every stage's exit recommendation is one mechanism, so it has one owner.
That owner lands late in the chain, after dTendedCadence, so until it lands no stage's recommendation is
scored. The ancestor probe, re-run after the fold, shows which rows cite these items
and need a class.

### [pm-12-unsettled] The 5 the records do not settle, each with a recommendation

| Id | Node | Kind | Approved | Verifiers | Recommended | Why |
| --- | --- | --- | --- | --- | --- | --- |
| F4 | `design.recommend` | item | dIndexedDesign | dCalibratedLens | dCalibratedLens | one mechanism, one owner, as its seven siblings; dIndexedDesign's "design review by policy" keeps `review.design`'s opt-in, effort and audit guard, and its walkthrough clause naming the recommendation is narrowed |
| F13 | `integrations.tracker` | key | dTotalRecall | dShippedRelease | dShippedRelease | `mirror-out` is an allowed value and needs an adapter; the re-cut has dShippedRelease deliver integrations, and no row names this adapter, so dShippedRelease's row gains it |
| F14 | `memory.default-load` | key | dTotalRecall | dWellOiledMachine | dWellOiledMachine | the key selects the load set, which the harness adapter lists and the session-start hook loads, both dWellOiledMachine's; dTotalRecall keeps its auto-memory check on that load |
| F16 | `review.design.round-count` | key | dCalibratedLens | dIndexedDesign | dCalibratedLens | as F17 |
| F17 | `review.design.rounds` | key | dCalibratedLens | dIndexedDesign | dCalibratedLens | the round loop sits in the breakpoint program dCalibratedLens builds (`review.fold` routes "the next round as `review.design.rounds` says"), the reading that refuted F7; its row then names the key, with `REVIEW_ROUNDS` re-pointed |

### [pm-12-kept] The 5 the skeptic refuted: the approved owner stays

| Id | Node | Kind | Owner kept | Why the skeptic refuted the move |
| --- | --- | --- | --- | --- |
| F7 | `review.fold` | item | dCalibratedLens | part of the breakpoint program dCalibratedLens builds; "design review by policy" holds no fold |
| F10 | `annotations.delivery` | key | dBoundRoles | its default fills the work order's code-notes slot, which dBoundRoles builds; the verifiers cited the system's owner, the rule for systems, not keys |
| F19 | `kit` | tag namespace | dOrderedCharter | the tags system's builder registers it, and v2 now lists it among dOrderedCharter's seven |
| F21 | `decision` | record kind | dTotalRecall | the verifiers' evidence names the fork record, a separate kind already dIndexedDesign's |
| F22 | `intake` | record kind | dWellOiledMachine | it rested on a row the re-cut changed: the hook now sits in dWellOiledMachine's row |

### [pm-12-population] The 52 nodes the table lacks, after the skeptic

| Finding | Nodes | Kind | Owner | Verdict |
| --- | --- | --- | --- | --- |
| P1 | `maintain.direct`, `maintain.file`, `maintain.lease`, `maintain.levels`, `maintain.patch`, `maintain.read`, `maintain.record` | item | dTendedCadence | confirmed |
| P2 | `loop.file`, `loop.gather`, `loop.lease`, `loop.price`, `loop.propose`, `loop.record` | item | dCalibratedLens | confirmed |
| P3 | `release.pick`, `release.approve`, `release.promote`, `release.verify`, `release.route`, `release.record` | item | dShippedRelease | confirmed |
| P4 | `kits.version`, `kits.cut`, `kits.currency`, `kits.fleet`, `kits.offer`, `kits.install`, `kits.update` | item | dShippedRelease | confirmed |
| P5 | `build-readme` | record kind | dTotalRecall | confirmed |
| P6 | `claim` | record kind | dTotalRecall | confirmed |
| P7 | `comparison` | record kind | dShippedRelease | confirmed |
| P8 | `core-result` | record kind | dScopedBuild | confirmed |
| P9 | `currency` | record kind | dShippedRelease | confirmed |
| P10 | `diff` | record kind | dIndexedDesign | confirmed |
| P12 | `exception` | record kind | dOrderedCharter | confirmed |
| P13 | `fleet` | record kind | dShippedRelease | confirmed |
| P14 | `fleet-register` | record kind | dShippedRelease | confirmed |
| P15 | `inventory` | record kind | dIndexedDesign | refuted on owner: its writer is `design.inventory`, dIndexedDesign's |
| P16 | `kit-release` | record kind | dShippedRelease | confirmed |
| P17 | `loop-review` | record kind | dCalibratedLens | confirmed |
| P18 | `overlap` | record kind | dIndexedDesign | confirmed |
| P19 | `override` | record kind | dOrderedCharter | confirmed |
| P20 | `receipt` | record kind | dShippedRelease | confirmed |
| P21 | `recommendation` | record kind | dCalibratedLens | confirmed |
| P22 | `release` | record kind | dShippedRelease | confirmed |
| P23 | `release-exit` | record kind | dShippedRelease | confirmed |
| P24 | `roster` | record kind | dIndexedDesign | confirmed |
| P25 | `routing` | record kind | dWitnessedBar | confirmed; `release.route`, dShippedRelease's, also writes a routing record |
| P26 | `seen-red` | record kind | dWitnessedBar | confirmed |
| P27 | `selection` | record kind | dWitnessedBar | confirmed |
| P28 | `triage` | record kind | dRankedPlan | confirmed |
| P29 | `value-ledger` | record kind | dCalibratedLens | confirmed |
| P30 | `workspace` | record kind | dWellOiledMachine | confirmed |

- **51 are proposed for the table:** the 26 items and 25 record kinds above. `inventory` takes the owner the
  skeptic found, dIndexedDesign, not the verifiers' majority.
- **`disposition` (P11) is not settled.** The owner's disposition record is "written by whichever channel
  carried it", the mailbox, a terminal command or a prompt, and it witnesses `entry.place-owner`
  (dDeclaredLoop's), `build.ratify` (dScopedBuild's) and the breakpoints (dCalibratedLens's). No record names the
  build that registers it. The recommendation is dDeclaredLoop: the loop declares every item's witness, the reading
  the skeptic confirmed for `acceptance` (F20), and `entry.place-owner` writes it first.
- **No candidate was one node under two names.** `release-exit` and `release`, and `fleet-register` and
  `fleet`, are each two kinds.

### [pm-12-listed] Single dissents, for information

`[compare-2]`'s "listed" block holds the 17 owners one verifier alone disputes. By the disposition they are
listed, not escalated, and no move is proposed for them.

### [pm-12-fold] What lands once the owner answers

- **The owner fields:** flow-steps' Owner cells for the moved items, v2's catalogue Owner cells for the moved
  keys, and layer-memory's `[contract]` kind table for the moved and added kinds.
- **The expansions' items:** layer-expansions' four `| Item | Actor |` tables gain an Owner column, and the
  map's item extractor and its census read them.
- **The chain rows:** each row that claims a moved behaviour is narrowed to what it still builds, and the
  receiving row names it. That covers dIndexedDesign's "design review by policy", dTotalRecall's default load,
  dShippedRelease's tracker mirror and dCalibratedLens's design-review rounds.
- **The checks:** the map's owner check and the ancestor probe are re-run, then the atlas is republished.

## [answers-2] The owner's answers, 2026-10-18

- PM-12a, asked as "PM-12a: the skeptic confirmed 13 of the disputed owners. Move them?": "Move all 13 (Recommended)"
- PM-12b, asked as "PM-12b: 5 owners the records don't settle. Take the recommendations?": "Take recommendations (Recommended)"
- PM-12c, asked as "PM-12c: add the 51 nodes the table lacks?": "Add all 51 (Recommended)"
- PM-12d, asked as "PM-12d: who registers the owner's disposition record?": "dDeclaredLoop (Recommended)"

Each answer takes `[pm-12]`'s recommendation whole. The answers are structural, so they add no policy key.

## [folded-2] What landed

- **The owner fields:**
  - flow-steps: the eight stage reason and recommend items' Owner cells read dCalibratedLens;
  - v2's catalogue: six keys' Owner cells move, as `[pm-12-moves]` and `[pm-12-unsettled]` say;
  - layer-expansions: the four program tables gain an Owner column over their 26 items;
  - layer-memory `[contract]`: `acceptance` and the run record move, and 26 kinds join, 67 in all.
- **The rule and the sort, corrected in layer-memory:**
  - the ownership rule reads "the build that registers it" in place of "the build of its writer", which the
    moved and added kinds need;
  - the P28 sort moves the run record out of core to observability, as layer-expansions and layer-runtime
    already had it.
- **The chain rows,** with a revision note in v2:
  - dIndexedDesign's design review leaves the stage-exit recommendation to dCalibratedLens;
  - dTotalRecall keeps the default load's memory share and its session-start report, and the loading is
    dWellOiledMachine's, whose hook now names `memory.default-load`;
  - dCalibratedLens names the design audit's two round keys;
  - dShippedRelease gains the tracker mirror, 20 units from 19.
- **The instruments:**
  - the map and the atlas read the expansions' items, and the map's census counts them by its own route;
  - the parity check spans the steps' items and the programs' items both;
  - the ancestor probe found one new citation, dTotalRecall's `roster`. It is the README's derived field, a
    homonym of the new kind, and is now classed in the re-cut record's `[reconciled-order]`.
- **PM-12d's reason, corrected.** The question and `[pm-12]` said the loop declares every item's witness.
  That over-reaches: `verdict`, `attribution` and `landing` are loop-declared witnesses too, and they stay
  with their stage builds. The kind table carries the reason that holds. dDeclaredLoop is the earliest of
  the disposition record's writers' builds and an ancestor of the others, and `entry.place-owner` writes it
  first.

The checks after the fold, the ancestor probe's first run among them:

```text
$ python 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check
atlas: derived — 142 records, 2467 sections, 169 decision sections, 16 comparison areas, 30 principles
rc 0
$ python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --check
map: 2139 nodes in 30 namespaces; 29688 B of 32768 (no degrade); folded 14; unarmed none
map: purposes declared 1419, derived 243, pending 477
rc 0
$ python 2026-10-17-build-PLAY-dClosedLoop-1-map.py --check --plant <case>, for each case
orphan: FINDING owner: item.entry.intake names no owning build rc 1
two-owners: FINDING owner: policy-key.preset names 2 owning builds rc 1
inferred: FINDING no inference: point.actor-kinds's owner comes from no declared field rc 1
no-owner: FINDING owner: tag-namespace.reader names no owning build rc 1
drop-line: FINDING complete: layer has nodes on no line and in no count: ['instruction'] rc 1
bad-count: FINDING count: item.* counts 108, the table holds 107 rc 1
ghost-rel: FINDING resolves: chain.dGroundRules names owner=dGhostBuild, which resolves nowhere rc 1
census: FINDING census: tools/newkit/kit.toml is on disk with no kit node rc 1
$ python ancestor_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md
chain rows 16 · owned nodes read 396 (items, keys, points, record kinds, tag namespaces; systems are cited in prose and left out) · backticked citations 268 · of a non-ancestor's node 10
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dDeclaredLoop's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): tolerance
  dTotalRecall cites `roster` (dIndexedDesign's, not an ancestor): UNCLASSED
findings 1
rc 1
$ python critical_path.py
critical path: 176 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 6, dFairHearing 21, dOrderedCharter 28, dDeclaredLoop 65, dWitnessedBar 85, dBoundRoles 115, dTotalRecall 117, dIndexedDesign 126, dRankedPlan 128, dShippedRelease 137, dWellOiledMachine 141, dScopedBuild 150, dTendedCadence 151, dMindYourWords 157, dCalibratedLens 164, dConvergedCharter 176
rc 0
```

After the class row, the probe green, and red with that row planted away:

```text
$ python ancestor_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md
chain rows 16 · owned nodes read 396 (items, keys, points, record kinds, tag namespaces; systems are cited in prose and left out) · backticked citations 268 · of a non-ancestor's node 10
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dDeclaredLoop's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): tolerance
  dTotalRecall cites `roster` (dIndexedDesign's, not an ancestor): homonym
findings 0
$ python ancestor_probe.py 2026-10-18-build-PLAY-dClosedLoop-1-recut.md --plant-drop dTotalRecall:roster
chain rows 16 · owned nodes read 396 (items, keys, points, record kinds, tag namespaces; systems are cited in prose and left out) · backticked citations 268 · of a non-ancestor's node 10
  dDeclaredLoop cites `build.closes` (dShippedRelease's, not an ancestor): tolerance
  dDeclaredLoop cites `intake` (dWellOiledMachine's, not an ancestor): homonym
  dFairHearing cites `class` (dTotalRecall's, not an ancestor): homonym
  dFairHearing cites `preset` (dDeclaredLoop's, not an ancestor): homonym
  dGroundRules cites `policy.guard` (dDeclaredLoop's, not an ancestor): not a use
  dGroundRules cites `policy.proof` (dDeclaredLoop's, not an ancestor): not a use
  dOrderedCharter cites `check` (dWitnessedBar's, not an ancestor): homonym
  dOrderedCharter cites `memory.map-purpose` (dTotalRecall's, not an ancestor): moved
  dRankedPlan cites `entry.intake` (dWellOiledMachine's, not an ancestor): tolerance
  dTotalRecall cites `roster` (dIndexedDesign's, not an ancestor): UNCLASSED
findings 1
```

The other instruments the PM-10 fold ran:

```text
$ python role_matrix_v5.py flow-steps layer-roles
items 81 of 81 body rows; actor-item pairs 81; actors 15; items with a role 20; cycle roles 1; findings 0
rc 0
$ python gap_join_filed.py gap-register architecture-v2
owned twice or more: none
owned but not in the register: none
builds owning nothing: none
rc 0
$ python preset_check_canonical.py architecture-v2
catalogue keys 192 · presettable 182 · preset rows 182
no findings
rc 0
```

- **The role matrix still reads flow-steps' 81 items alone.** It joins items to the roles layer's matrix,
  and the expansions' 26 items name no role.
- **A stale copy of the preset check was found and deleted.** It read 0 catalogue keys and exited 0, at HEAD
  and after the fold alike. The canonical check above reads the catalogue whole.
