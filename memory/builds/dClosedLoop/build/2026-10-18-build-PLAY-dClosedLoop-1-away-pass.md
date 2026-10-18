# The away pass: the owner's six points, worked unattended

**Serves:** research PLAY-dClosedLoop-1

The owner handed six points to work into the design and stepped away, asking for each to be researched, designed
and fitted to the project, then for a report and the resulting state, with every fork parked to be put at once on
the owner's return. This record holds the pass: the owner's words, the research dispatched, each point's finding
and design, what the pass did to the chain, the forks, the closing review and the checks as run. Point 2's plan is
its own record, `build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md`.

## [words] The owner's words, 2026-10-18

Verbatim, as handed after the walk closed (`build/2026-10-18-build-PLAY-dClosedLoop-1-walk.md` `[wave-4-answers]`):

> Several more ideas need to be reviewed, evaluated, and worked into the design. I'm stepping away for the time
> being, so this pass is continuing unattended until fully worked out. Do what's necessary to go through each point
> step by step, understand their viability and their fit into the project. Run agents/workflows at medium effort to
> assist you in research and design:
> 1. Memory layer isn't properly represented in the Atlas, so I do not have a visual understanding of its design
> right now.
> You need to give the system a thorough pass and account for the larger idea - memory+instruction layer should
> follow the same writing (instruction) practices, unified through the same relational syntax and the tagging
> system. The whole design should bring together and use all of the available pieces, not leaving any of them out
> to simple prose - charter, instruction layer protocols, prompt writing methotodology, build memory, decisions, git
> commit trees with their commit messages and SHAs, agentic (Claude, can Codex do the same?) session IDs for
> inter-session communication. What other memory pockets are available? The entire system should be able to
> cyclically relate between its pieces through the syntax.
> 2. Based on the findings, a full instruction/memory plan, with its integrations into the new architecture
> thoroughly explained, should be laid down before the build proceeds.
> 3. Claude Code CLI. This is already being used in part by the existing processes and their tooling but a larger
> question - is there benefit to integrating more of the CLI instead of relying on Claude Desktop/Codex Desktop
> applications? How to achieve agnosticism from the application the owner would use? This should be
> researched/tested.
> 4. Compatibility. We have not reviewed this previously, and this is important. Currently, Gov's tooling is
> written using different languages and frameworks - bash/js/python/etc.. The kit itself can run in
> Windows/WSL/Linux/and possibly other environments. Does it make sense to ensure that Gov follows one consistent
> coding practice for maximum portability/compatibility? This should be researched/tested.
> 5. Observability - will it be possible to analyze any part of the flow effortlessly when the full rearchitecture
> is complete? Without evidence, fixes and improvements are impossible. It should be possible to point at any part
> of the flow, worker, task, or issue and be able to tell what was happening.
> 6. Distribution - how will the rebuilt kit replace it's older, superceded versions? It should be seamless.
>
> Don't stop until you've worked out each step, once you have - prepare a report for me on this and a resulting
> state of the project, and park all the forks for me to go at once when I return.

## [research] Dispatched, 2026-10-18

Six researchers ran at the owner's medium effort, read-only, one question each. Point 1 was split in two, the
memory the repository's files hold and the memory outside them, and its session-id part went with point 3. Point 2
is this pass's own synthesis. Each handoff is in `prompts/`, and each return is saved verbatim beside this record.

| Dispatch | Point | Handoff | Return | Outcome |
|---|---|---|---|---|
| 106 | 1, memory in the repository | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-9-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-memory-pockets.md` | 27 pockets; one typed link works end to end, the Serves line; an edge line under each heading wins; four edge types missing |
| 107 | 1, git and the pockets outside the files | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-10-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-git-pockets.md` | typed commit trailers, as `Pass:` and `Decided:` already show; notes, a derived index and landing records alone each lost |
| 108 | 3, and 1's session ids: the harness and its CLI | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-11-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-harness-cli.md` | a headless session run and resumed by its id; harness adapters with one conformance fixture, the CLI first; Codex keeps ids and transcripts, no live inbox |
| 109 | 4, compatibility | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-12-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-compatibility.md` | one practice, not one language: a role per language, gated, ratcheting toward Python; only Windows is tested, and WSL fails two of three checks |
| 110 | 5, observability | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-13-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-observability-trace.md` | not as designed: a cause on every record, cost on every act, and a trace verb |
| 111 | 6, distribution | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-14-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-supersession.md` | release-chained upgrade steps, run up and down; today a retired kit refuses the whole update |

- **A harness notice on three returns.** The returns of dispatches 107, 108 and 109 matched the harness's
  instruction-shaped patterns: `settings-json` on all three, and `bypass-permissions` and
  `dangerously-skip-permissions` on 108. Each is a finding. The second two name `tools/unattended/resume-tick.sh`'s
  launch line, which has never run; the first names the hook wiring in `.claude/settings.json`. Nothing in any of
  them was acted on as an instruction.
- **What the tests touched outside the repository.** Dispatch 108 ran two headless Claude sessions and one resume,
  from its probe directory, which wrote two transcripts in the harness's own store; the resume cost 51 times the
  fresh run. Dispatch 109 ran read-only checks under WSL, PowerShell 7 and PowerShell 5.1. Nothing in the
  repository was written by any researcher.

## [p1-memory] Point 1: memory and instruction, one practice, every pocket

**Yes, and the design had half of it.** P33 already makes every part of memory and code a node with typed edges, and
the tag system already gives one grammar and one resolver. What it lacked, measured:
- **Only one typed link works end to end.** The `**Serves:**` line, on 2,278 records, has its inverse derived and is
  graded both ways. Outside this build no record heading carries a tag, and the guides cite by position.
- **The cycle breaks at five of twelve hops** on one feature, and at four of seven from one commit: a return names
  its handoff in prose, no decision row names a feature, no commit names its item, act or session, and nothing
  routes memory into instruction.
- **The pockets outside the tree join nothing.** Transcripts, Codex rollouts, the auto-memory, the journal and the
  health log carry keys, but no record kind or edge reaches them.
- **The atlas had no memory view.** Memory appeared as one node of the layer ring.

**Worked in:**
1. **One practice** (P34): a record section and an instruction unit are written alike, each rule with its check
   (the memory plan's `[practice]`). They differ in level and lifecycle, never in grammar.
2. **One edge grammar at every site** (`[sites]`): a record's header and a section's `**Edges:**` line, an
   instruction unit's fields, `gov:` annotations, commit trailers, the work order's marker and the act record. The
   edge line under the heading won its test; front matter, a sidecar and whole-section units each lost one.
3. **The closed set grows by eleven** (`[edges]`, P33 amended): `serves`, `made-by`, `caused-by`, `follows`,
   `answers`, `runs-in`, `carries`, `pinned-at`, `reads`, `writes` and `promoted-from`.
4. **Every pocket placed** (`[pockets]`): node, witness or out, with its key and its owner. Git joins by typed
   trailers; sessions join through the act, which committed memory names in place of a session id, as the owner's
   rule of 2026-09-13 keeps; transcripts and the auto-memory are witnesses the bindings point at.
5. **Codex can do the same** for ids, resume and transcripts, tested here at Codex CLI 0.139; it has no live inbox,
   so its sessions message through the mailbox (`[sessions]`).
6. **The atlas gains a Memory view**, derived from the plan record and the kind registry, built in this pass.

## [p2-plan] Point 2: the instruction and memory plan

The plan is `build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md`. It lays down, before any chain build
proceeds:
- the frame and the eight families (`[frame]`, `[families]`);
- every pocket and its place (`[pockets]`);
- the practice, its sites and the closed edge set (`[practice]`, `[sites]`, `[edges]`);
- the cycle walked by key (`[cycle]`), and session ids with Codex's parity (`[sessions]`);
- the doors that write and the verbs that read (`[doors]`);
- where it lands in each layer and each build (`[integration]`, `[chain]`);
- how today's memory moves onto it with nothing rewritten by hand (`[migration]`);
- the checks it arms, the view it draws and the keys it adds (`[gates]`, `[view]`, `[keys]`).

What lands first: dOrderedCharter's grammar and registry, then dDeclaredLoop's commit node, dTotalRecall's kind
registry and `record` header, dLinkedLibrary's decision edges, and dWellOiledMachine's act key. The rest follows
the chain's order, and every unit sits on its own build or a build it depends on.

## [p3-harness] Point 3: the CLI, and staying independent of the owner's application

**Yes, integrate more of the CLI, as the runtime and never as the owner's window.** The runtime design already
launches act sessions as CLI processes. The test showed what that buys and costs:
- **It works headless.** `claude -p` returned a session id and a structured result; a resume by that id remembered
  the earlier turn. `--session-id` presets the id, `--json-schema` forces a typed return, and the result carries
  cost, turns and the terminal reason.
- **It has four costs.** The first run failed on an OAuth token refresh another process held. A resume cost 51 times
  a fresh run, which `runtime.relaunch: fresh` already chooses against. A nested process inherited its parent's
  entrypoint, session variables and messaging token. And the app's Claude Code (2.1.299) and the one on PATH
  (2.1.292) differ, the PATH one lacking a hook field the design needs.
- **The apps add viewing, not running.** gov's flows used the desktop app's browser pane, chapters, widgets and session
  list, none load-bearing; the one desktop-only launch path, its scheduled tasks, was never called. A program cannot
  start an act in the app and receive a typed return, so the app as the runtime lost its test.
- **Codex is installed here**: CLI 0.139 and its desktop app. It keeps session ids and transcripts, resumes by id,
  and now documents twelve hook events trusted by hash, so two gap rows and the runtime record's Codex facts were
  stale and are amended.

**Worked in** (P36):
1. **Harness adapters, each measured by one conformance fixture**: launch by a program, id preset or returned,
   resume, headless fork, schema return, the hook events and fields the packs read, the fail-closed path, the live
   inbox, transcript homes and interpreters. The supervisor picks the act harness by those rows, and the core relies
   only on the rows every act adapter passes.
2. **The CLI is the first act adapter**; the owner's application, Claude's or Codex's, desktop or IDE, is a viewer
   chosen by `runtime.owner-harness`.
3. **Preflight refuses** a launch that skips hooks (`--bare`, `--safe-mode`) or permissions, an allowlist scrubs the
   launch environment, and an authentication failure relaunches as a transient class.
4. **Four keys**: `runtime.binary`, `runtime.owner-harness`, `runtime.act-harness`, `runtime.act-auth`.

## [p4-compat] Point 4: one coding practice across platforms

**One practice makes sense; one language does not.** Measured over the tracked tree, outside `memory/`:

| Language | Files | Lines |
|---|---|---|
| bash | 132 | 134,819, of which 58,613 sit in the unattended kit the chain dissolves |
| Python | 88 | 129,572 |
| JavaScript | 20 | 18,265 |

- **Only Windows with Git-Bash is tested.** Under WSL Ubuntu 22.04, two of three read-only kit checks failed: its
  Python 3.10 lacks `tomllib`, and it has no node. A worktree's pointer holds a Windows path WSL's git cannot open.
- **node is an undeclared hard dependency**: ten of thirteen hook commands run it, while the charter's toolchain
  line names bash and Python only.
- **The resolver accepts a Python below the floor**, and prefers the Store alias, which spawns four times slower than
  the direct executable on this node.
- **Of 25 recorded portability classes**, 11 hit bash, 6 Python, 5 cross languages, 2 PowerShell and 1 JavaScript.
  Line endings, encoding and paths hit Python as hard as bash, so no single language removes them.
- **Every single-language option lost a test.** Python-first passes only once the resolver enforces the floor; node
  is absent where gov's hooks would need it; a compiled binary breaks the adopter who runs a patched kit, and
  `Workflow` scripts stay JavaScript in any case.

**Worked in** (P37): a role per language, Python for logic, shell as thin shims, JavaScript on the harness's
surfaces, with new and rebuilt code moving to Python by a shrink-only ratchet; one rule set, each rule with its leg
(the compatibility return's section 4); a declared platform matrix, Windows with Git-Bash and Linux at tier 1, macOS
unsupported until a node runs it; and two keys, `platforms.supported` and `platforms.verify`.

## [p5-observe] Point 5: pointing at anything and telling what happened

**Not as designed; yes with three additions, for everything committed.** Four past events were rebuilt from
today's evidence, a researcher dispatch, an unattended run, a red bar and a process reap. Each took six sources and
eight or nine lookups, and each left a question no record answers: which tree the agent read, what a unit cost,
which session ran the bar, what a reaped process was. As designed, every chain build writes its own record kind,
but none carries a key that joins it to the others, P33's edges relate no runtime kind, and committed cost covers
review acts' output tokens only.

**Worked in** (P35):
1. **Every record names its cause.** A `caused-by` edge on every kind, its inverse derived, with the root kinds
   declared (the intake, the session binding, a cadence lease); `record` refuses a missing cause.
2. **Every act carries its cost.** The supervisor writes the act session's own usage and duration from its JSON
   result, never from a transcript.
3. **One query from any key.** `gov trace <key>` walks the causes down into a timeline and `gov why <key>` walks up to
   the instruction units and the request. Each row reads time, kind, actor, item, outcome, cost and source, and is
   filled, `not-local: node <x>` or `pruned`, never empty, bounded by `trace.rows`.
4. **Keys on every line.** Journal lines carry the act or the session; the health and stall logs fold into the
   journal grammar; the verdict names its bar run; a failing leg's output tail is kept by hash.
5. **Readers.** Maintain reads acts with no outcome, runs left unrecorded and commits missing their keys; the Loop
   Review prices cost per item kind from trace rows.
6. **Four keys**: `trace.identity`, `trace.cost`, `trace.leg-output`, `trace.rows`.

## [p6-distribution] Point 6: superseding today's kits seamlessly

**Release-chained upgrade steps; today's engine cannot do it.** Measured on gov's own tree and govkit's fixture:
- **A retired kit refuses the whole update**, a planted receipt showed, and a downgrade is refused outright, so no
  version can be rolled back.
- **Moved conf keys are only reported**, an edited file of a retired part stays silently, a withdrawn hook stays
  wired, and a half-applied update needs a lock removed by hand.
- **gov cannot update itself**, and its own deploy file is refused by `plan`.
- **107 of the fates table's 131 rows** change shape, move or retire, and an absorbed kit's files mostly do not pair
  as renames.

**Worked in** (P38):
1. **Each build that changes what an adopter can see ships an upgrade step**: id, introducing commit, up and down
   argv run from gov's checkout, witness, surfaces, whether it needs the target's own code. The registry's
   `[[retired]]` rows name each retired entry's successor.
2. **`update` walks every step** between an adopter's receipt and its target, oldest first, each skipped when its
   witness holds, and rolls back by running the down steps in reverse.
3. **gov runs every step on itself first**, through the lander in the prepared merge.
4. **Two bounded windows** keep old surfaces working: a command or hook path forwards and warns for
   `install.deprecation-window` releases, and an old conf or record shape is read until its step runs.
5. **A release-0 fixture tree** is walked up, down and up again, byte-identical down, each step seen load-bearing.
6. **The receipt records the steps**, and the currency watch and the fleet register read steps pending and shim
   calls, so the owner sees a stuck migration, not only an adopter behind.
7. **Where the step kind is built.** It must exist before dOrderedCharter, the first build to change what an adopter
   sees. It is placed in dGroundRules, beside the legacy homes the translation window reads, and the recovery,
   receipt and fleet units go to dShippedRelease. The researcher recommended a build of its own; at four units the
   path cost is the same either way, so the split is the owner's (AP-25).
8. **Four keys**: `install.deprecation-window`, `install.on-shim-call`, `install.retired-edits`, `install.steps`.

## [chain-impact] What the away pass did to the chain

The chain keeps its twenty builds; no build is added, split or reordered, and the one structural question, where
the upgrade-step kind lives, is parked as AP-25. Thirteen builds gain units, 30 in all, each clause on its own build
or one it depends on:

| Build | Units added | For |
|---|---|---|
| dGroundRules | 4 | the upgrade-step kind, its walk, its down steps and its fixture (point 6) |
| dOrderedCharter | 4 | the edge grammar, the writing practice's checks, the portable practice, its own upgrade steps (points 1, 4, 6) |
| dDeclaredLoop | 1 | the commit node and its trailer keys (point 1) |
| dPlacedRequest | 1 | the kickoff manifest as instruction units (point 1) |
| dWitnessedBar | 2 | the portability leg pack, and the verdict's cause and leg tails (points 4, 5) |
| dTotalRecall | 2 | the completed kind registry, and `record`'s header and edge line (points 1, 5) |
| dLinkedLibrary | 1 | decision and bug-class edges (points 1, 4) |
| dBoundRoles | 1 | markers on every work order, `answers` on every return (point 1) |
| dWellOiledMachine | 6 | the act key, trailers, the trace verbs, the session node, the conformance fixture, preflight (points 1, 3, 4, 5) |
| dTendedCadence | 1 | readings for missing outcomes, runs and keys (point 5) |
| dCalibratedLens | 1 | the Loop Review priced from trace rows (point 5) |
| dShippedRelease | 4 | the receipt and fleet for steps, gov first, the platform matrix, landings and publications (points 1, 3, 4, 6) |
| dConvergedCharter | 2 | the migration to tags and class pins, and the steps that close the convergence (points 1, 4, 6) |

The path, recomputed by `critical_path.py` on the folded tree, against the one the walk closed with at `fa62092db`:

```text
before, at fa62092db: critical path 171 units over 335
critical path: 190 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 12, dFairHearing 24, dOrderedCharter 43, dDeclaredLoop 66, dPlacedRequest 74, dWitnessedBar 91, dKeptSession 92, dBoundRoles 108, dTotalRecall 110, dRankedPlan 123, dFurnishedOrders 126, dLinkedLibrary 134, dIndexedDesign 146, dWellOiledMachine 147, dScopedBuild 158, dTendedCadence 162, dMindYourWords 164, dShippedRelease 172, dCalibratedLens 174, dConvergedCharter 190
```

It grows by 19 units. Its run moves from dLinkedLibrary and dIndexedDesign onto dWellOiledMachine, whose six new
units make it finish one unit after dIndexedDesign. AP-25's homes for the step kind, priced the same way:

```text
as placed, in dGroundRules: 190 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
in dShippedRelease, adopters held until it lands: 188 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dShippedRelease > dConvergedCharter
a build of its own between dGroundRules and dOrderedCharter: 190 units, dGroundRules > dHandedOverStandIn > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
```

Holding adopters back until dShippedRelease saves two units, because dShippedRelease then becomes the critical
build, and it would freeze every adopter on today's kits through the whole chain. The other effects:
- **The gap register** grows by 39 gaps, every one owned by exactly one build: Memory 6, Roles 1, Spine 2,
  Runtime 7, Orient 2, Test 1, Maintain 1, Deploy 9, Tooling 10. Two Codex rows, `gap-rt-09` and `gap-rt-11`, are
  amended with Codex's current hooks.
- **The catalogue** gains 17 keys, 13 of them in every preset and 4 among the keys presets never touch.
- **The principles** gain P34 to P38, and P33's closed set eleven types.
- **The kind registry** gains six kinds: commit, view, registry, archive, instrument and witness.
- **The level-0 map** now uses its degrade order, shortening purposes to 40 characters to stay within its budget,
  as its design allows; gap-mem-30's owed measurement covers it.
- **The atlas** gains its Memory view, derived from the plan record and the kind registry.

## [forks] Parked for the owner, 2026-10-18

Thirty forks, each with the recommendation first. A key's default stands as recommended until the owner answers.

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| AP-1 | How does a record section declare its edges? (a structural decision) | one `**Edges:**` line under the heading, as the Serves line declares the record's; front matter keyed by section; a sidecar per record | the plan's `[sites]` |
| AP-2 | How far does the closed edge set grow? (a structural decision) | the eleven types, each needed by a measured hop; a core four (`serves`, `made-by`, `caused-by`, `answers`) with the rest as record fields; `part-of` and `cites` widened to carry them | P33's closed set |
| AP-3 | `memory.legacy-records`: how do today's records reach the plan? | backfill: Serves lines read as edges, derived anchors, no file rewritten; anchors-only; retag every record | the key's default |
| AP-4 | How does a design-only build's unit become a node? | the build README's `ids:` defines it; design-only builds exempt from the bindings check | dTotalRecall's registry |
| AP-5 | How does git join the syntax? (a structural decision) | typed trailers, one key per edge, mapped in the registry; one `Gov-Edge:` key; git notes; a derived commit index alone | dDeclaredLoop's commit node |
| AP-6 | `commits.edge-check`: where are the trailers checked? | push-leg, reading the binding; commit-msg; off | the key's default |
| AP-7 | `commits.squash`: what happens to trailers on a squash? | re-emit-union; refuse; accept-loss | the key's default |
| AP-8 | `trace.identity`: may committed memory name a session? | act-only, as the owner's rule of 2026-09-13 keeps; session; salted | the key's default, never set by a preset |
| AP-9 | What are transcripts and the auto-memory to the graph? | witnesses with keyed pointers; nodes; out | the plan's `[pockets]` |
| AP-10 | How does gov stay independent of the owner's application? (a structural decision) | harness adapters with one conformance fixture, the CLI first, any application a viewer; the desktop app as the runtime; the CLI alone | P36 |
| AP-11 | `runtime.binary`: which CLI does the supervisor launch? | newest-conforming, read from the node registry; path; app-bundled; a pinned path | the key's default |
| AP-12 | `runtime.owner-harness`: which application is the owner's viewer? | auto, taken from the session's binding; a named adapter | the key's default, never set by a preset |
| AP-13 | `runtime.act-harness`: which harness runs acts? | claude-code; codex, once its rows pass | the key's default |
| AP-14 | `runtime.act-auth`: how does an act authenticate? | oauth-shared, with transient retries; setup-token; api-key | the key's default, never set by a preset |
| AP-15 | Which coding practice does gov follow? (a structural decision) | a role per language, gated, ratcheting toward Python; Python-first now; node-first; a compiled binary | P37 |
| AP-16 | What language do harness hooks use? | node, declared as a dependency; Python | P37's roles |
| AP-17 | `platforms.supported`: which platforms does gov promise? | windows-gitbash and linux; add macos; add pwsh-launch | the key's default, never set by a preset |
| AP-18 | `platforms.verify`: how are they verified? | held, until the Linux half is green, then ci; bar; ci; off | the key's default |
| AP-19 | Which Python does gov require? | 3.11, the resolver naming how to provision it; 3.10, with a vendored TOML parser | the interpreter floor |
| AP-20 | How are worktree pointers written? | relative, tested first against WSL's git; absolute, WSL worktrees unsupported | dWellOiledMachine's isolation |
| AP-21 | `trace.cost`: what does a committed act record carry? | tokens and wall time, from the act's own output, never a journal time of day; tokens; none | the key's default; the owner's rule of 2026-09-16 bears on it |
| AP-22 | `trace.leg-output`: where does a failing leg's output live? | tail-by-hash, committed; node-local | the key's default |
| AP-23 | `trace.rows`: how long is a timeline? | 60 rows, folding by kind past that; 120; all | the key's default |
| AP-24 | How do the rebuilt kits supersede today's? (a structural decision) | release-chained upgrade steps, up and down; one epoch release; shims alone; a translation layer alone | P38 |
| AP-25 | Where is the upgrade-step kind built? (a structural decision) | in dGroundRules, as placed; a build of its own between dGroundRules and dOrderedCharter, named by the owner, at the same path; in dShippedRelease, adopters held at today's kits until it lands, two units shorter | the chain |
| AP-26 | `install.deprecation-window`: how long does an old surface keep working? | 2 releases; 0; 1; 4 | the key's default |
| AP-27 | `install.on-shim-call`: what does a forwarded call do? | warn, journaled for the fleet view; journal only; refuse | the key's default |
| AP-28 | `install.retired-edits`: what happens to an adopter's edit of a retired file? | order: kept, marked forked, with an order; keep silently; delete | the key's default |
| AP-29 | `install.steps`: who runs an upgrade step? | offer: gov's no-target-code mode, a step needing the target's code falling back to attended; attended always | the key's default |
| AP-30 | How does gov itself migrate? (P8) | the lander runs each new step on gov first, recorded in its source-mode receipt; gov's own diff is its migration | dShippedRelease's lander unit |

