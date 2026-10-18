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
| 113 | 4, asked while the owner answered: AP-19's floor and AP-17's future plan | `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-15-researcher.md` | `build/2026-10-18-build-PLAY-dClosedLoop-1-research-python-floor.md` | keep 3.11 now and raise it to 3.12 by 2027-10, which the owner replaced with 3.15 now (AP-31); macOS and pwsh-launch planned behind triggers; a TOML 1.1 split at 3.15 |

- **A harness notice on three returns.** The returns of dispatches 107, 108 and 109 matched the harness's
  instruction-shaped patterns: `settings-json` on all three, and `bypass-permissions` and
  `dangerously-skip-permissions` on 108. Each is a finding. The second two name `tools/unattended/resume-tick.sh`'s
  launch line, which has never run; the first names the hook wiring in `.claude/settings.json`. Nothing in any of
  them was acted on as an instruction.
- **What the tests touched outside the repository.** Dispatch 108 ran two headless Claude sessions and one resume,
  from its probe directory, which wrote two transcripts in the harness's own store; the resume cost 51 times the
  fresh run. Dispatch 109 ran read-only checks under WSL, PowerShell 7 and PowerShell 5.1. Nothing in the
  repository was written by any researcher.
- **Dispatch 113,** a seventh researcher at the owner's medium, ran while the owner answered the forks, on AP-17's
  and AP-19's answers. Its return matched the harness's `settings-json` pattern, since it cites the hook wiring in
  `.claude/settings.json` as evidence. Nothing in it was acted on as an instruction. It wrote no repository file, and
  its probes are kept in the instruments record.

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
   trailers; sessions join through the act, and committed memory may name the harness session
   id beside it (AP-8); transcripts and the auto-memory are witnesses the bindings point at.
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
unsupported until a node runs it; and two keys, `platforms.supported` and `platforms.verify`. The owner then set the
floor at Python 3.15, every node upgrading (AP-31), and placed macOS and pwsh-launch in v2's `[planned]` behind
their triggers (AP-17, AP-34).

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
   `install.deprecation-window` releases, through dSafePassage's forwarding shim, and an old conf or record shape is
   read until its step runs. The window is at least `currency.max-behind`, so an adopter inside its currency budget
   never meets a removed surface.
5. **A release-0 fixture tree** is walked up, down and up again, byte-identical down, each step seen load-bearing.
6. **The receipt records the steps**, and the currency watch and the fleet register read steps pending and shim
   calls, so the owner sees a stuck migration, not only an adopter behind.
7. **Where the step kind is built.** It must exist before dOrderedCharter, the first build to change what an adopter
   sees. The owner gave it a build of its own, dSafePassage, between dGroundRules and dOrderedCharter (AP-25), as the
   researcher recommended and at the same path cost. The recovery, receipt and fleet units stay with dShippedRelease.
8. **Four keys**: `install.deprecation-window`, `install.on-shim-call`, `install.retired-edits`, `install.steps`.

## [chain-impact] What the away pass did to the chain

The chain keeps its twenty builds; no build is added, split or reordered, and the one structural question, where
the upgrade-step kind lives, is parked as AP-25. Fourteen builds gain units, 32 in all, two of them from the closing
review, each clause on its own build or one it depends on:

| Build | Units added | For |
|---|---|---|
| dGroundRules | 5 | the upgrade-step kind, its walk, its down steps, its fixture and the forwarding shim (point 6) |
| dOrderedCharter | 4 | the edge grammar, the writing practice's checks, the portable practice, its own upgrade steps (points 1, 4, 6) |
| dDeclaredLoop | 1 | the commit node, its kind and its trailer keys (point 1) |
| dPlacedRequest | 1 | the kickoff manifest as instruction units (point 1) |
| dWitnessedBar | 2 | the portability leg pack, and the verdict's cause and leg tails (points 4, 5) |
| dKeptSession | 1 | the catalogue's reader join (the closing review) |
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
critical path: 191 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 13, dFairHearing 25, dOrderedCharter 44, dDeclaredLoop 67, dPlacedRequest 75, dWitnessedBar 92, dKeptSession 94, dBoundRoles 109, dTotalRecall 111, dRankedPlan 124, dFurnishedOrders 127, dLinkedLibrary 135, dIndexedDesign 147, dWellOiledMachine 148, dScopedBuild 159, dTendedCadence 163, dMindYourWords 165, dShippedRelease 173, dCalibratedLens 175, dConvergedCharter 191
```

It grows by 20 units. Its run moves from dLinkedLibrary and dIndexedDesign onto dWellOiledMachine, whose six new
units make it finish one unit after dIndexedDesign. AP-25's homes for the step kind, priced the same way:

```text
as placed, in dGroundRules: 191 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
in dShippedRelease, adopters held until it lands: 189 units, dGroundRules > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dShippedRelease > dConvergedCharter
a build of its own between dGroundRules and dOrderedCharter: 191 units, dGroundRules > dHandedOverStandIn > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
```

Holding adopters back until dShippedRelease saves two units, because dShippedRelease then becomes the critical
build, and it would freeze every adopter on today's kits through the whole chain. The other effects:
- **The gap register** grows by 41 gaps, every one owned by exactly one build: Memory 6, Roles 1, Spine 3,
  Runtime 7, Orient 2, Test 1, Maintain 1, Deploy 10, Tooling 10. Two Codex rows, `gap-rt-09` and `gap-rt-11`, are
  rewritten with Codex's current hooks.
- **The catalogue** gains 16 keys, 12 of them in every preset and 4 among the keys presets never touch, and the
  systems round's `memory.legacy-anchors` gains a `retag` value.
- **The principles** gain P34 to P38, and P33's closed set eleven types.
- **The kind registry** gains six kinds: commit, view, registry, archive, instrument and witness. The card's row now
  names its writer item, and the 32 rows that name none carry the marker `writer item not named`.
- **The level-0 map** now uses its degrade order, shortening purposes to 40 characters to stay within its budget,
  as its design allows; gap-mem-30's owed measurement covers it.
- **The atlas** gains its Memory view, derived from the plan record and the kind registry.

## [forks] Parked for the owner, 2026-10-18

Thirty forks, each with the recommendation first, and five more, AP-31 to AP-35, that dispatch 113 raised while the
owner answered. A key's default stands as recommended until the owner answers.

| Fork | Question | Options, the recommendation first | What the answer sets |
|---|---|---|---|
| AP-1 | How does a record section declare its edges? (a structural decision) | one `**Edges:**` line under the heading, as the Serves line declares the record's; front matter keyed by section; a sidecar per record | the plan's `[sites]` |
| AP-2 | How far does the closed edge set grow? (a structural decision) | the eleven types, each needed by a measured hop; a core four (`serves`, `made-by`, `caused-by`, `answers`) with the rest as record fields; `part-of` and `cites` widened to carry them | P33's closed set |
| AP-3 | `memory.legacy-anchors`, widened: how do today's records reach the plan? | derived: anchors derived and Serves lines read as edges, no file rewritten; retag every record's headings; none | the key's default |
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
| AP-31 | What is the next interpreter floor, once 3.11 nears its end of life in 2027-10? | 3.12 by 2027-10, as a P38 step after the chain closes; 3.14; 3.15 | the interpreter floor |
| AP-32 | `platforms.provision`: how does a node get to the floor? | name: the refusal names the install command for its platform, recommending uv; uv, offered while the owner attends; off | the key's default |
| AP-33 | A bare `bash` from Python runs WSL's bash on Windows: how is it fixed, and when? | one shared resolver and a wrong-shell refusal on dWitnessedBar now; the same, deferred with pwsh-launch; a PATH precondition | dWitnessedBar's units |
| AP-34 | When does the macOS work start? | on a registered node, after dWellOiledMachine dissolves `unattended/`; now | v2 `[planned]` |
| AP-35 | `maintain.interpreter-eol`: what happens as the floor's end of life nears? | file: an intake six months before it; warn; off | the key's default |

The owner answered all thirty-five on 2026-10-18 (`[answers]`), and the design carries the answers
(`[folded-answers]`).

## [review-fold] The closing review, folded

The closing review, dispatch 112, read everything design-bearing since the night pass's review fold, `a66c855f3` over
`15cec9200`: the night pass's folded answers, the walk's four waves and the away pass. It ran `tier2-review.js` light,
at the owner's medium effort: three `gov-diff-reviewer` lenses (correctness, seams, verification), four `gov-skeptic`
batches and one `gov-synthesizer`. Its report, `reviews/2026-10-18-review-PLAY-dClosedLoop-1-away-pass-closing.md`,
reads CLEAN WITH FIXES: 16 raw findings, 15 confirmed and 1 refuted, as 13 items, 2 high, 6 medium and 5 low. Every
item is folded:

| Item | What it found | The fold |
|---|---|---|
| H1 | the plan's `[chain]` put three units on builds v2 does not | the plan's `[chain]` now names each unit by its v2 clause's opening words and its build, and the design map's chain-echo arm reds on a mismatch |
| H2 | no unit built `install.deprecation-window` or `install.on-shim-call` | dGroundRules gains the forwarding shim, each value seen on a planted retired path, and `gap-deploy-24` |
| M1 | the window's presets contradicted its own rule | the window is at least `currency.max-behind` by a pair rule in v2 `[presets]`, its presets now 4, 2, 1 and 2, and the preset check's pair arm reds on the old velocity row |
| M2 | the same misplacement as H1, seen by another lens | folded with H1 |
| M3 | no edge type carried a commit to a unit or an item | `serves` takes a commit, `Gov-Unit` and `Gov-Item` map to it and `Gov-Act` to `made-by`, and a planted `Gov-Item:` joins the commit gates |
| M4 | the Memory view passed kinds it could not place | the atlas resolves each writer token as an item, a key or a file, and refuses a ghost token or a kind with neither a writer item nor a marker; 32 kinds carry `writer item not named`, the card names `entry.orient`, and `gap-mem-37` counts them |
| M5 | an unread edge status became P33, and an undeclared hop edge vanished | the status is read from P33, new or derived, and every hop edge must be declared |
| M6 | the no-stale-facts arm witnessed its own zero | the arm counts its records and quotes, prints both, and reds on no record, on fewer quotes than its floor of 15, or on a record ending inside an open fence |
| L1 | layer-runtime kept the stale Codex hook set beside its revision | the Codex row states the twelve events with the revision kept as provenance, and the same stale claim is rewritten in layer-instruction, `gap-rt-09` and `gap-rt-11` |
| L2 | the commit and registry kinds had two owners | the commit kind is named in dDeclaredLoop's row, the registry kind moves to dTotalRecall, and dTotalRecall's row names view, registry, archive, instrument and witness |
| L3 | a kind was grouped under a step that only names it | a kind is grouped by the first writer item its row names |
| L4 | a mistyped second hop edge dropped silently | folded with M5 |
| L5 | only `[pockets]` was counted against its raw lines | every plan table and the kind registry are counted, and a split table stops the run |

**Found while folding.**
- `memory.legacy-records` duplicated the systems round's `memory.legacy-anchors`. The duplicate is dropped, and
  `memory.legacy-anchors` gains `retag`; AP-3 asks about the widened key.
- `install.retired-edits` was dGroundRules' while dShippedRelease's row honours it. It moves to dShippedRelease, and
  every key the away pass added is now named by a unit on its owner's row.
- H2's proposed gate, a key that no unit on its owner's row names, was run over the tree first: 116 of 220 keys fail
  it, so it cannot arm as a red. dKeptSession's catalogue reader join holds them as a shrink-only population, and
  `gap-spine-10` registers them.

**The gates, each seen red on its planted case before it is trusted:**

```text
$ python map.py --check --plant <case>
FINDING no stale facts: 2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md ends inside an open fence, which mutes every line after it
FINDING no stale facts: read no design record
FINDING chain echo: memory-plan [chain] puts 'the shared edge grammar at every site the memory p' on dGroundRules, whose v2 row holds no clause opening so
$ python atlas.py --check --plant <case>
atlas: layer-memory [contract] kind 'ghost kind' names no writer item and carries no marker
atlas: layer-memory [contract] kind 'ghost kind' names ['plan.ghost-writer'], resolving to no item, key or file
atlas: memory-plan [edges] row '`made-by`': status 'nwe' unread
atlas: memory-plan [cycle] hop 'work order → act': a family, its state or an edge is unread ['answered-by-typo']
atlas: memory-plan [edges] holds 24 row lines but its table parsed 1: a split table drops rows
$ python atlas.py --check   (the fixed generator on the registry before its markers)
atlas: layer-memory [contract] kind 'exception' names no writer item and carries no marker
$ python preset_check_canonical.py v2-at-a66c855f3.md
catalogue keys 225 · presettable 207 · preset rows 207
pair rule: velocity sets install.deprecation-window 1 under currency.max-behind 4
```

The fold is one round, as the knee of earlier rounds advises: it changes records and instruments, every check is
green on the folded tree, and the planted cases above show each new arm can fail. The security and intent lenses
did not run, since the review was light.

## [state] The report, and the state the pass leaves

**Each point, in one line:**
- **1, memory and instruction.** Yes. One writing practice (P34), one edge grammar at every site, eleven new edge
  types, and all 45 pockets placed as node, witness or out. Git joins by typed trailers, sessions through the act,
  and Codex keeps ids and transcripts without a live inbox. The atlas shows it in its new Memory view.
- **2, the plan.** `build/2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md`, laid down before any chain build
  proceeds: every pocket, site, edge, hop, door, layer, unit, migration step, check and key.
- **3, the CLI.** Yes, as the runtime, never as the owner's window. A headless session ran and was resumed by its id,
  and harness adapters measured by one conformance fixture keep gov independent of the owner's application (P36).
- **4, compatibility.** One practice, a role per language, ratcheting toward Python (P37). Only Windows is tested
  today. Under WSL, two of three checks failed, so a declared platform matrix and its runners are owed.
- **5, observability.** Not as designed; yes with a cause on every record, cost on every act, and `gov trace` and
  `gov why` (P35).
- **6, distribution.** Release-chained upgrade steps, up and down, gov first, with a forwarding window for moved
  surfaces (P38). Today's engine refuses a retired kit outright and cannot roll back.

**The state:**
- **The design, at `a9b00addd`:** 20 builds, 367 planned units, 38 principles, 224 keys, 296 gaps and 76 record
  kinds.
- **The checks:** every one green on the folded tree, re-run in the instruments record's `[final]`.
- **The chain's path:** it grows by 20 units, now through dWellOiledMachine; `[chain-impact]` holds the run.
- **The closing review:** CLEAN WITH FIXES, every item folded, `[review-fold]`.
- **Forks parked:** AP-1 to AP-30, seven of them structural: AP-1, AP-2, AP-5, AP-10, AP-15, AP-24 and AP-25. The
  owner has answered them since, with five more (`[answers]`), and `[folded-answers]` holds the state after them.
- **Not done:** nothing merged or pushed, no product code, no chain spec written. The build's exit still waits on the
  owner's word that the design has its full shape.

## [answers] The owner's answers, 2026-10-18

Asked on the owner's return, "put the forks to me", through AskUserQuestion in nine batches of up to four, the
recommendation first. Each answer is quoted as the tool returned it.

- AP-1, asked as "AP-1 (structural): how does a record section declare its edges?": "Edges line under heading (Recommended)" with its preview
- AP-2, asked as "AP-2 (structural): how far does P33's closed edge set grow?": "The eleven types (Recommended)"
- AP-3, asked as "AP-3: how do today's records reach the plan (memory.legacy-anchors)?": "derived (Recommended)"
- AP-4, asked as "AP-4: how does a design-only build's unit become a node in the graph?": "README ids defines it (Recommended)"
- AP-5, asked as "AP-5 (structural): how does git join the syntax?": "Typed trailers (Recommended)" with its preview
- AP-6, asked as "AP-6: where are the commit trailers checked (commits.edge-check)?": "push-leg (Recommended)"
- AP-7, asked as "AP-7: what happens to the trailers when an adopter squashes (commits.squash)?": "re-emit-union (Recommended)"
- AP-8, asked as "AP-8: may committed memory name a session id (trace.identity, never set by a preset)?": "session"
- AP-9, asked as "AP-9: what are transcripts and the auto-memory to the graph?": "Witnesses with pointers (Recommended)"
- AP-10, asked as "AP-10 (structural): how does gov stay independent of your application?": "Harness adapters, CLI first (Recommended)"
- AP-11, asked as "AP-11: which CLI does the supervisor launch (runtime.binary)?": "newest-conforming (Recommended)"
- AP-12, asked as "AP-12: which application is your viewer (runtime.owner-harness, never set by a preset)?": "auto (Recommended)"
- AP-13, asked as "AP-13: which harness runs acts (runtime.act-harness)?": "claude-code by default, but owner-switchable."
- AP-14, asked as "AP-14: how does an act authenticate (runtime.act-auth, never set by a preset)?": "setup-token by default, oauth-shared fallback, with api-key as the last owner-selectable option from the all the options as necessary"
- AP-15, asked as "AP-15 (structural): which coding practice does gov follow?": "Role per language (Recommended)"
- AP-16, asked as "AP-16: what language do harness hooks use?": "node, declared (Recommended)"
- AP-17, asked as "AP-17: which platforms does gov promise (platforms.supported, never set by a preset)?": "gitbash + linux at start, but add a potential future plan for macos and pwsh-launch."
- AP-18, asked as "AP-18: how are the promised platforms verified (platforms.verify)?": "held, then ci (Recommended)"
- AP-19, asked as "AP-19: which Python does gov require?": "3.11 but let's plan this ahead, do we need a newer python version for any reason? Now is the time to price it in."
- AP-20, asked as "AP-20: how are worktree pointers written?": "relative (Recommended)"
- AP-21, asked as "AP-21: what does a committed act record carry (trace.cost)?": "tokens+wall (Recommended)"
- AP-22, asked as "AP-22: where does a failing gate leg's output live (trace.leg-output)?": "tail-by-hash (Recommended)"
- AP-23, asked as "AP-23: how many rows does a `gov trace` timeline show (trace.rows)?": "120"
- AP-24, asked as "AP-24 (structural): how do the rebuilt kits supersede today's?": "Release-chained steps (Recommended)"
- AP-25, asked as "AP-25 (structural): where is the upgrade-step kind built (five units, the forwarding shim among them)?": "A build of its own"
- AP-26, asked as "AP-26: how long does an old command or hook path keep working (install.deprecation-window)?": "2 releases (Recommended)"
- AP-27, asked as "AP-27: what does a call through a forwarded old path do (install.on-shim-call)?": "warn (Recommended)"
- AP-28, asked as "AP-28: what happens to an adopter's edit of a file that a step retires (install.retired-edits)?": "order (Recommended)"
- AP-29, asked as "AP-29: who runs an upgrade step (install.steps)?": "offer (Recommended)"
- AP-30, asked as "AP-30: how does gov itself migrate (P8)?": "Steps on gov first (Recommended)"
- AP-25, its name, asked as "AP-25's new build sits between dGroundRules and dOrderedCharter and holds the step kind, the update walk, down steps, the release-0 fixture and the forwarding shim. What is it called?": "dSafePassage (Recommended)"
- AP-31, asked as "AP-31 (new, from the research): what is the next Python floor, once 3.11 nears its end of life in 2027-10?": "3.15 now, all the nodes will upgrade."
- AP-32, asked as "AP-32: how does a node get to the 3.15 floor (platforms.provision)?": "name (Recommended)"
- AP-33, asked as "AP-33 (new): on Windows, Python's bare `bash` runs WSL's bash 5.1.16 on every launch shell (I reproduced it). How is it fixed, and when?": "Shared resolver, now (Recommended)"
- AP-34, asked as "AP-34 (new): when does the macOS work start?": "On a registered node (Recommended)"
- AP-35, asked as "AP-35 (new): what does gov do as the Python floor's end of life nears (maintain.interpreter-eol)? 3.15's is 2031-10.": "file (Recommended)"

- **AP-19 asked for a pricing.** Dispatch 113 ran while batches 6 and 7 were put, and its return raised AP-31 to
  AP-35, put in batches 8 and 9. AP-31's answer, 3.15 now, replaces AP-19's 3.11.
- **AP-25 chose a build of its own without naming it,** so its name was asked in batch 8.
- **Five answers are in the owner's own words:** AP-13, AP-14, AP-17, AP-19 and AP-31.

## [folded-answers] What the answers changed

Twenty-seven answers took the recommendation, which the design already carried: each fork's pending marker in v2's
catalogue now names the fork. Eight departed from the recommendation or added to it, AP-19's by asking for the
research that AP-31 then answered, and dispatch 113's return changed the design with them.
- **AP-25, AP-30 and AP-31: dSafePassage.** The upgrade-step kind's five units leave dGroundRules for a build of its
  own, dSafePassage, between dGroundRules and dOrderedCharter, named at the owner's word. dOrderedCharter and
  dFairHearing now follow it. It owns the five gaps dGroundRules held for the step kind, and
  `install.deprecation-window` and `install.on-shim-call` move with the shim that reads them. Its sixth unit is the
  step kind's first step: the interpreter floor raised to Python 3.15, the template a later raise
  copies. Its seventh puts gov's own executors at the floor in the same landing and applies the step to gov's tree
  first (AP-30).
- **AP-31 and AP-32: the floor.** The research recommended keeping 3.11 and raising it to 3.12 by 2027-10, its end of
  life. The owner chose 3.15 now, every node upgrading. With every reader at 3.15, `tomllib` reads TOML 1.1
  everywhere and UTF-8 is the default encoding. The research's TOML 1.0 arm is not built: the floor step's down
  refuses while a tracked TOML file fails to parse under the floor it restores, which covers the one way back to an
  older reader, and the step itself is the template a later raise copies. The floor is declared once. dSafePassage's
  resolver refuses an interpreter below it and names the install command, gov's own remote CI sets one up in the
  same landing, dWitnessedBar's floor arm runs a real interpreter at the floor, and dShippedRelease's emitted CI
  sets one up for adopters. `platforms.provision` joins the catalogue, `name` by default.
- **AP-33: one bash resolver, now.** dWitnessedBar gains the shared resolver, which replaces every bare-bash launch
  site a query over Python and JavaScript finds, asks git where its bash is before it searches PATH, and refuses
  rather than fall back to a bare `bash`, and a wrong-shell refusal at every entry point.
  The pwsh runner adapter waits in v2's `[planned]`. `gap-tool-20` records the class at its measured size.
- **AP-8: session ids in committed memory.** `trace.identity` defaults to `session`. Committed records may name the
  harness session id beside the act, a commit carries a `Gov-Session` trailer, and `runs-in` widens to take a commit.
  dLoggedFlight's run log keeps its closed schema until dWellOiledMachine's act-key unit makes that leg read the key.
- **AP-14: an ordered credential.** `runtime.act-auth` is an ordered list: a setup token, then the shared OAuth login,
  and an API key tried last, only when the owner adds it. Each is read from the node's credential store, never from a
  file. An absent, expired or rejected credential moves to the next, and a transient failure relaunches on the
  same credential under its own cap before it moves on.
- **AP-13, AP-23 and AP-35.** `runtime.act-harness` stays claude-code, switched by the owner. A timeline shows 120
  rows before it folds. dTendedCadence gains a detector that files an intake six months before the floor's end of
  life, under the new key `maintain.interpreter-eol`.
- **AP-17 and AP-34: planned platforms.** macOS and pwsh-launch are in v2's new `[planned]` section, each with its
  trigger, runner, units and gaps, counted in no build until its trigger holds.
- **The gap register** gains five gaps, `gap-tool-20` to `gap-tool-22`, `gap-rt-32` and `gap-maint-15`, each owned
  once, and its tally is re-measured. The join reads 301 gaps over 21 builds, each owning at least one.
- **The catalogue** holds 226 keys, 206 of them presettable, and the presets follow.
- **The recut record's** `check` homonym row moves with its clause to dSafePassage, after the reconciliation probe
  reddened on it.
- **The atlas** shows v2's `[planned]` in its records view.

**The chain after the answers, at `fe3d09aba`,** recomputed by `critical_path.py` with its build count raised to 21:

```text
critical path: 195 units, dGroundRules > dSafePassage > dOrderedCharter > dDeclaredLoop > dWitnessedBar > dTotalRecall > dWellOiledMachine > dTendedCadence > dCalibratedLens > dConvergedCharter
each build's earliest finish, in units: dGroundRules 8, dSafePassage 14, dFairHearing 26, dOrderedCharter 45, dDeclaredLoop 68, dPlacedRequest 76, dKeptSession 95, dWitnessedBar 95, dBoundRoles 112, dTotalRecall 114, dRankedPlan 127, dFurnishedOrders 130, dLinkedLibrary 138, dIndexedDesign 150, dWellOiledMachine 151, dScopedBuild 162, dTendedCadence 167, dMindYourWords 168, dShippedRelease 176, dCalibratedLens 179, dConvergedCharter 195
```

The path grows by four units: dSafePassage's floor step, dWitnessedBar's two AP-33 units and dTendedCadence's
detector. It now runs through dSafePassage.

**Corrections.**
- **The rule of 2026-09-13 is dLoggedFlight's.** Its committed run-log record has a closed schema, and a schema leg
  refuses session ids there (`memory/builds/dLoggedFlight/README.md`). The away pass, its AP-8 row and the plan's
  `[sessions]` read it as a rule over all committed memory. The plan and v2's catalogue now state it at its size.
- **AP-33 was put larger than the tree shows.** Its question said a bare `bash` from Python runs WSL's bash on every
  launch shell. That holds for a bare `bash`, reproduced from a Git-Bash launch:

  ```text
  $ python bare_bash_repro.py
  bare bash (bash): rc 2
    err: /bin/bash: -c: line 1: syntax error near unexpected token `('
    err: /bin/bash: -c: line 1: `echo 5.1.16(1)-release; uname -s'
  PATH's bash (C:\Program Files\Git\usr\bin\bash.EXE): rc 0
    out: 5.3.9(1)-release
    out: MINGW64_NT-10.0-22621
  ```

  But tracked Python makes no bare `bash` call:

  ```text
  $ python bare_bash_census.py
  tracked .py files 111, unparsed 0
  bare-bash call sites 0 in 0 files; by area:
  $ python bare_bash_lists.py
  argv-shaped literals starting with bash: 30 in 13 files; branch-reconcile 1, codebase-map 4, drift-audit 1, govkit 12, lexicon 1, memory-tree 1, process-monitor 1, roles 1, run-gates 6, runlog 1, settings-merge.py 1
  ```

  Those literals reach a resolver first. The class reaches WSL through govkit's fall-back to a bare `bash` when no
  PATH bash resolves, and through seven copies of a resolver loop that search PATH only. Tracked JavaScript holds
  one more site, the stop guard's, which reaches the launcher wherever System32 precedes Git's bash on PATH, as the
  closing review's run B found:

  ```text
  $ python js_bare_bash.py
  tracked JavaScript files 21; bare-bash spawn sites 1 in 1 files
    tools/unattended/stop-guard.js:111  const r = spawnSync('bash', [driver, '--liveness', slug],
  ```

  The answer stands, and `gap-tool-20` states the class at that size.

**Interpretations, for the owner to correct:**
- AP-13's "owner-switchable" reads as switched by the owner alone: `runtime.act-harness` joins the keys presets
  never touch, so picking a preset never changes the harness.
- AP-14's api-key, "the last owner-selectable option", reads as outside the default order: the owner adds it to
  `runtime.act-auth`'s list, and it is tried last.
- AP-8 reaches dLoggedFlight's run log too, once dWellOiledMachine lands its act-key unit. Until then that build's
  rule stands as written, and its README is untouched.
- AP-25's dSafePassage precedes dFairHearing as well as dOrderedCharter, since the review harness is a shipped kit
  and so changes what an adopter sees. It costs the path nothing.
- AP-31's "now" reads as the chain's first change an adopter sees: dSafePassage raises the floor and its resolver
  refuses below it before any later build, so each may rely on 3.15.
- AP-32's `platforms.provision` joins the keys presets never touch, since how a node gets its interpreter is the
  operator's.
- AP-17's future plan counts in no build's units. macOS adds its gaps to the register when its trigger holds, and
  pwsh-launch's measured gaps are there already, under AP-33.

**The checks** are re-run in the instruments record's `[final]`, all green. The reconciliation probe's one red run
on the way is in its `[answers-fold]`.

**The closing review,** run twice at the owner's word, found seventeen defects in this fold, three of them high, and
every one is folded: `build/2026-10-18-build-PLAY-dClosedLoop-1-answers-reviews-compared.md` `[folded]`.
