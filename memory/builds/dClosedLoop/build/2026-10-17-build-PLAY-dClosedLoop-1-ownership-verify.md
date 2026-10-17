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
