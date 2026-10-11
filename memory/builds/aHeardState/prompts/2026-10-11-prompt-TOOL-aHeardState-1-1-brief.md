# Brief — aHeardState: the turn end refuses a final message without the BUILD/SPEC pair

**Serves:** research TOOL-aHeardState-1 TOOL-aHeardState-2

## The prompt

The `--prompt` value was the path `memory/builds/aHeardState/prompts/2026-10-11-prompt-TOOL-aHeardState-1-0-run-handoff.md`; its bytes follow, verbatim.

> # Run handoff — aHeardState
>
> **Serves:** journal TOOL-aHeardState-1 TOOL-aHeardState-2
>
> node a · 2026-10-11 · written by the attended session that kicked the build off
> (`7ecabc14-b395-43a9-8f32-9e036af87174`), for the unattended run that specs and builds it ·
> authorized-by prompt
>
> No build folder, README or spec exists yet: this file is the whole hand-over. Read it whole after
> `memory/guides/BUILD-METHOD.md` and before the first pass.
>
> ## Starting the run
>
> - The owner's act is `/unattended --prompt <this file>` in a fresh session in the worktree
>   `C:/projects/coding-governance/.claude/worktrees/blissful-khayyam-69a7df`, on
>   `branch/blissful-khayyam-69a7df` at BASE `9b7438315fd16e23f71598c092f7d64985f76640` (=
>   `origin/main` at kickoff, zero commits of its own). `ANCHOR_SCOPE=local`, so this is the
>   `prompt` path.
> - This file is untracked in that worktree. Step 3 of the prompt path writes
>   `memory/builds/aHeardState/README.md` with `authorized-by: prompt` beside it, and the prompt record
>   with its brief. Commit this file in that same commit. scratch-guard exempts the commit that
>   creates an `authorized-by:` README, so it lands before any `## route` exists.
> - The owner has answered the kickoff's questions already (2026-10-11): **no `spec-audit:`**, and
>   **item 4 is built as unit 2**. The step-2 `AskUserQuestion` therefore has nothing left to ask.
>   Skip it and say so in the brief's `## Owner confirmation`.
> - No directive is waived.
> - **This run does NOT land.** The owner's words: "Ask the owner before landing; this changes every
>   session's stop behaviour." Carry the build through the close, then hand off with
>   `unattended.sh --handoff aHeardState --code owner-landing --reason "<the stop-behaviour change
>   needs the owner's ask>" --reaped <id>`. Never `--abort` sound work, never the lander, never a
>   push to `main`. Pushing the BRANCH is fine, and the prompt path's step 4 requires it.
>
> ## The prompt — the owner's words, verbatim, for the brief's `## The prompt`
>
> > In the coding-governance repo (C:/projects/coding-governance), the charter (AGENTS.md section 3, "Micro-formats", rendered from coding-governance-agents.template.md) makes micro-formats mandatory: `- committed — <sha> · <branch> · <subject>` per commit, `- ⏳ — <what is running>` per long phase, and an adjacent `- BUILD — …` / `- SPEC — …` pair in the state block of EVERY final message while a build is in progress. Emission has no machine gate; the old §16 said so outright ("Pre-send self-check (documented check — emission has no universal machine gate)"), and the v4.x render dropped even that self-check line.
> >
> > Observed failure: session 86a064cd-3532-4202-93cd-dd26651975d3 (unattended build aPrimedIndex, node a) emitted ZERO micro-formats across 1,162 assistant entries, before and after a compaction. The probe was a grep over the transcript JSONL at C:/Users/daily-agent/.claude/projects/C--projects-coding-governance--claude-worktrees-enforce-index-regen-before-bars-acdde6/86a064cd-3532-4202-93cd-dd26651975d3.jsonl for `- committed —`, `- BUILD —`, `- SPEC —`, `- ⏳ —` and `- gates —` in assistant text. Contributing pressures: the unattended `minimal-prose` directive (BUILD-METHOD M10) read as "say less", harness "say in a few words" nudges answered in freeform prose, and turn-ending status messages not treated as "final messages".
> >
> > Task: spec and build a gate for the class, per the repo's own rules (spec first, run /session-kickoff, follow memory/guides/BUILD-METHOD.md):
> > 1. A Stop hook (see tools/hooks/ for existing hook kits, and how agent-cap.js and scratch-guard.js are wired via settings fragments) that, when the session's orientation card routes a build whose RUN.md / spec set is non-terminal, inspects the last assistant message and blocks the stop with a reason when the `- BUILD — ` / `- SPEC — ` pair is missing, not adjacent, or not bare list items (rule r1). Optionally, when HEAD moved since the previous stop, it also requires a `- committed — <sha>` line naming the new commits.
> > 2. Decide whether the shape grammar is read from the charter's Micro-formats block rather than restated (one fact in one place).
> > 3. Observe the gate red on a staged break (a final message without the pair), then green; state in its header what it does NOT check (emission mid-turn, the ⏳ heartbeat, field VALUES).
> > 4. Consider the chat-prose audit script the old charter named as "none yet" (thresholds: mid-turn narration >40% of session prose, or >3 interjections per final message) as a second, transcript-level measure.
> > Ask the owner before landing; this changes every session's stop behaviour.
>
> ## The roster
>
> | Step | Unit | Tier | Disposition |
> |---|---|---|---|
> | 1 | `TOOL-aHeardState-1` — `format-guard`, the Stop hook | 2 | spec, then build |
> | 2 | `TOOL-aHeardState-2` — `runlog.py prose <sid>`, the transcript measure | 2 | spec, then build |
>
> The two units are disjoint in their writes (`tools/hooks/`, `.claude/settings.json` and
> `tools/gate-legs.json` against `tools/runlog/`). Both still write the generated
> `memory/map/generated/` and `memory/LIVE.md` through their generators, so M6 clause 3 SEQUENCES
> them. Unit 1 goes first, because unit 2's acceptance reads the pair grammar unit 1 settles.
>
> ## Unit 1 — design as the kickoff settled it
>
> Each point below is a design default, not an owner ruling. Record each in the spec's §8 as
> `RESOLVED (agent, 2026-10-11, delegated)`. Re-open one only by M3's vetoes.
>
> - **Home.** `tools/hooks/format-guard.js` in the agent-cap kit (`tools/hooks/kit.toml`, id
>   `agent-cap`), beside `scratch-guard.js`. It needs a `format-guard.fragment.json`
>   (`"event": "Stop"`, `"matcher": "*"`, `"marker": "format-guard.js"`), a `kit.toml` `[[files]]`
>   rule per file, a section in `tools/hooks/README.md`, a held self-test `format-guard.test.sh`
>   (`role = "project-owned"`) with a `gate-legs.json` row shaped like `scratch-guard self-test`'s,
>   and the `.claude/settings.json` wiring through `settings-merge.py --fragment`. Use a new
>   fragment, never a widened `stop-guard` group: the marker is a different basename, so
>   settings-merge keeps both. Check the name with `/lexicon` before writing it, and every function
>   name inside it too.
> - **When it fires.** It arms only when all three hold:
>   - the payload's `session_id` has an orientation card at `<git-common-dir>/orientation/<sid>.md`;
>   - that card carries a `## route` with a `- build: <slug>` line;
>   - `<slug>` is a row of the payload `cwd` toplevel's `memory/LIVE.md`.
>
>   LIVE.md is the generated non-terminal set, so the hook restates no terminal-status list.
>   Reuse scratch-guard's `resolveToplevel`, `resolveCommonDir`, `readCard` and `extractRouteUnits`.
>   At this second instance, extract them into a shared module rather than copying them (charter
>   `[reuse]`), or record in §10 why the kit's one-file-per-rule shape forbids it.
> - **What it reads.** The payload's `last_assistant_message`. The aWokenSentinel keepalive research
>   record says Stop's stdin carries it. When it is absent, allow, with one stderr witness line.
> - **The grammar.** Derive the `BUILD`, `SPEC` and `committed` shapes from the
>   `<!-- microformats -->` fence of the rendered charter at the toplevel (`AGENTS.md`). Compile each
>   definition into a line regex:
>   - a placeholder `<…>` becomes a run with no ` · `;
>   - literal text stays literal;
>   - `[ · …]` becomes an optional group;
>   - the line must start with `- ` at column 0.
>
>   `tools/check-microformats.sh` reads the same fence: share its keying or cite it. No fence,
>   or no definition for a head keyword → allow with a witness line, never a fabricated shape. This
>   answers item 2 with YES: read the grammar, never restate it.
> - **What blocks.** A block is `{"decision":"block","reason":…}` on exit 0, as in stop-guard. It
>   fires when any of these holds:
>   - **Missing.** The `BUILD` line is missing. Or the `SPEC` line is missing while the route names a
>     unit with a `· spec` path. `[pair]`: SPEC is omitted only before a spec exists.
>   - **Not adjacent.** SPEC is not on the line right after BUILD.
>   - **Not bare.** Either line fails r1: backticked, bold, indented, a heading, inside a fence, or
>     without its `- `.
>   - **Wrong shape.** Either line fails its compiled shape.
>   - **Commit unreported.** HEAD moved since this session's previous armed stop and a new
>     first-parent commit has no `- committed — <sha>` line. Its sha must be a prefix of the
>     commit's, at least 7 hex.
>
>   For the commit check, keep the last HEAD in a per-worktree sidecar under the git dir, and
>   write it on every armed stop. The first stop of a session records a baseline and requires
>   nothing. A prev that is not an ancestor of HEAD (reset or rebase) gets a witness line, not a
>   block. Spawn git only when HEAD moved: one spawn costs ~751 ms on this node.
>
>   The reason names each defect and quotes the definition line from the charter.
> - **Loop bound.** Never block when `stop_hook_active` is true. That allows one correction per turn
>   end, keeps no state, and cannot loop under the harness's cap of 8.
> - **Fail open.** A payload with `agent_id`, any event but `Stop`, or any thrown error → exit 0.
> - **The header's DOES-NOT-CHECK paragraph** must name all of these:
>   - emission mid-turn;
>   - the ⏳ heartbeat;
>   - every other micro-format (`gates`, `pushed`, `merged`, `READY`, `up`, `unchanged`, `skipped`);
>   - field VALUES (slug, counts, ids, link target);
>   - where in the message the pair sits (the `[state]` rule);
>   - sub-agent stops;
>   - every stop after a block in the same chain, whichever hook blocked. This includes stop-guard's
>     `run-open` blocks, so inside an unattended run the hook grades only the first stop of each
>     chain;
>   - whether it is wired.
>
> ### Unit 1 acceptance — the spec's §6 must say at least this
>
> 1. **Red, staged break.** Pipe a Stop payload into the hook. Point the card fixture at a LIVE build,
>    and put a `last_assistant_message` with no pair. Observe `decision: block` naming the missing
>    pair. Then backticked, indented and fenced pairs: each blocks for r1. A SPEC line before BUILD
>    blocks for adjacency.
> 2. **Green.** The same payload with a well-formed adjacent bare pair exits 0, with nothing on stdout.
> 3. **Unarmed.** No card; a card with no route; a routed build absent from LIVE.md: each exits 0
>    silently.
> 4. **Commit check.** Arrange prev ≠ HEAD with no `committed` line → block naming the sha. Add the
>    line → exit 0.
> 5. **Liveness.** Point the grammar reader at a charter copy with the fence removed → it allows with a
>    witness. So the arms in 1 cannot pass by matching nothing (`fixture-passes-by-finding-nothing`).
>
> ## Unit 2 — design as the kickoff settled it
>
> - **Home.** A `prose` subcommand of `tools/runlog/runlog.py`. It reuses `extract.py`'s
>   `resolve_session_tree` and `read_records`, never a second JSONL reader. Main transcript only;
>   sub-agent files are out.
> - **Definitions.** The spec writes each down, with its edge cases.
>   - A *turn* runs from one real user prompt to the next. A `tool_result` user record is not a
>     prompt.
>   - The *final message* is the assistant text after the turn's last tool call.
>   - *Narration* is every other assistant text block in the turn.
>   - *Interjections per final message* is the turn's narration-block count.
>   - *Pair emission* is whether the final message carries the BUILD/SPEC pair as unit 1 defines it.
>     Reuse unit 1's grammar derivation through a shared reader or one spec'd re-implementation
>     with a parity arm, never a third spelling.
> - **Output.** Print, per session:
>   - narration chars / all assistant prose chars, with `ALARM` above 40%;
>   - the per-turn interjection distribution (mean, max, turns above 3), with `ALARM` above 3;
>   - final messages carrying the pair / all final messages.
>
>   Report-only, exit 0 on a readable transcript. It gates nothing and adds no leg.
> - **Acceptance.**
>   - On session `86a064cd-3532-4202-93cd-dd26651975d3` (path in the prompt above), it reports 0
>     pair emissions across its final messages.
>   - On a small fixture under `tools/runlog/fixtures/` with known counts, every figure matches.
>   - A fixture with the pair present moves the count off zero: the liveness arm.
>
> ## Enforcement starts inside this run
>
> - A settings edit is live on the next tool call (`memory/gotchas/settings-edit-takes-effect-mid-session.md`).
>   The commit that wires `format-guard` into this worktree's `.claude/settings.json` arms it against
>   THIS run's own stops. From then on, every final message carries the pair, plus a `committed` line
>   per new commit.
> - `minimal-prose` (M10) does not excuse the state block. A final message may be short. It may not
>   drop the pair. This is the exact failure the build exists for. Do not reproduce it while building
>   the gate.
> - Write the live witness: after wiring, end one turn deliberately without the pair. Record the
>   `Stop hook feedback:` block the transcript shows in a `build/` record. It is the end-to-end
>   observation, and it complements the piped acceptance.
> - Before each unit's first write under `ROUTED_PATHS`, its spec must be at INPROGRESS (Tier-2), and
>   the session's card must carry a `## route` naming it, appended through
>   `bash skills/session-kickoff/manifest-check.sh --card --append --session <sid>`. The new
>   session's card is its own: this file's kickoff card (session `7ecabc14-…`) routes nothing for it.
>
> ## Gates and suites
>
> - A pass runs only the direct checks its spec's §6 names: no merge bar and no self-test suite.
>   Put "fast diff-scoped gates only, nothing held" in every unit brief's ground text.
> - The main loop runs `bash tools/hooks/format-guard.test.sh` once, at VERIFYING. The close's bar is
>   `GATE_FULL=1 bash tools/run-gates/run-gates.sh` alone. The other owed kit suites are not run at
>   the close; the owner runs them from the merged tree.
> - Kit versions bump once per kit, after its last unit: `KIT_AGENT_CAP_VERSION` in
>   `tools/hooks/agent-cap.js` for unit 1, and `KIT_RUNLOG_VERSION` in `tools/runlog/runlog_lib.py`
>   for unit 2. Run `python tools/govkit/govkit.py epoch --base 9b7438315fd16e23f71598c092f7d64985f76640`
>   before the close.
> - A new `.js`/`.py` function stales `memory/map/generated/symbols.json`. Run
>   `python tools/codebase-map/gen_map.py --write` before the close. `gen_map` reads untracked files,
>   so delete any slice script first.
>
> ## Known at hand-over
>
> - Local `main` (`75a1a52e`) and `origin/main` (`9b743831`) have diverged: local main carries 12
>   unpushed commits from aSparedHolder. This branch bases on `origin/main`. Reconciling is the
>   owner's call at landing, not this run's.
> - `help/` does not exist in this repository, so the charter's `[docs]` rule has no page to update.
>   Record that in each spec's §2 rather than inventing the directory.
> - The card append flagged both unit ids and both hook files as `UNVERIFIED`, because none existed
>   yet. The run's own kickoff card will verify them once the specs land.

## The brief

### Goal
A session whose orientation card routes a build still listed in `memory/LIVE.md` cannot end its turn
without the charter's `BUILD`/`SPEC` pair, adjacent and bare, plus a `committed` line for each commit
since its previous stop; and any session's transcript can be measured for prose discipline after the
fact.

### Items
1. A Stop hook refuses the turn end when the `BUILD`/`SPEC` pair is missing, not adjacent, or not bare list items (rule r1). [planned TOOL-aHeardState-1]
2. When HEAD moved since the previous stop, it also refuses a final message lacking a `committed` line per new first-parent commit. [planned TOOL-aHeardState-1]
3. The shape grammar is read from the charter's `<!-- microformats -->` fence, never restated. [planned TOOL-aHeardState-1]
4. It is observed red on a staged break and then green, and its header names what it does not check. [planned TOOL-aHeardState-1]
5. A transcript-level measure reports narration share (alarm above 40%), interjections per final message (alarm above 3) and pair emission per final message. [planned TOOL-aHeardState-2]

### Acceptance
Item 1-4: a piped Stop payload under a card routing a LIVE build blocks with no pair, with a
backticked, indented or fenced pair, and with SPEC before BUILD; exits 0 silently with a well-formed
adjacent bare pair; blocks with HEAD moved and no `committed` line and clears once the line is
present; allows with a witness when the charter's fence is removed. Item 5: `runlog.py prose` on
session 86a064cd reports zero pair emissions; on a fixture with known counts every figure matches;
a fixture carrying the pair moves the count off zero.

### Gates
In-pass: each unit's direct checks above. At VERIFYING: the held `bash tools/hooks/format-guard.test.sh`
and `GATE_FULL=1 bash tools/run-gates/run-gates.sh`. Owed kit suites run later from the merged tree.

### Non-goals
Grading emission mid-turn, the ⏳ heartbeat, any other micro-format, or any field VALUE. Any change to
the charter template or its rules. Blocking a sub-agent's stop. A gate leg for the prose measure.
Landing.

### Limitations
The run does not land: it closes into `unattended.sh --handoff aHeardState --code owner-landing`,
because the owner asked to be asked before a change to every session's stop behaviour. The run
starts in a fresh worktree off local `main` (`75a1a52e`), not the handoff's named tree, because that
branch sat at `origin/main`, which local `main` does not hold, so a first preflight would refuse it
as carried (check 114). One kit-version bump per kit, after its last move.

### Reuse
Unit 1 reuses scratch-guard's card and route readers (`resolveToplevel`, `resolveCommonDir`,
`readCard`, `extractRouteUnits`), stop-guard's Stop payload and block shape, and the fence keying of
`tools/check-microformats.sh`. Unit 2 reuses runlog's `resolve_session_tree` and `read_records`.
Recall returned TOOL-aHonedRuleset-2, TOOL-aHonedRuleset-8 and TOOL-aFusedCharter-2 (the grammar
gate), and the aWokenSentinel keepalive research record (Stop's stdin carries
`last_assistant_message`).

## Drawn from the session

> Declare `spec-audit:` for build aHeardState (two Tier-2 units: the format-guard Stop hook, and a transcript prose measure)? — "No audit"
— owner, kickoff AskUserQuestion, 2026-10-11

> Item 4, the chat-prose measure: build it in this build, or record it and park it? — "Build it as unit 2 (Recommended)"
— owner, kickoff AskUserQuestion, 2026-10-11

> write an unattended prompt handoff to continue this session
— owner, 2026-10-11

> the hook fires only when the routed build is listed in `memory/LIVE.md`;
— agent, the handoff report, 2026-10-11

## Owner confirmation

Asked: Accept this brief for unattended run aHeardState? Goal: a session routed to a live build can't end its turn without the BUILD/SPEC pair, and a transcript measure reports prose discipline. Items: (1) Stop hook blocks on a missing, non-adjacent or non-bare pair [planned TOOL-aHeardState-1]. (2) It also requires a `committed` line per new first-parent commit since the previous stop [planned TOOL-aHeardState-1]. (3) The grammar is read from the charter's microformats fence, never restated [planned TOOL-aHeardState-1]. (4) Red on a staged break, then green; the header names what it does not check [planned TOOL-aHeardState-1]. (5) `runlog.py prose <sid>`: narration share >40%, interjections >3, pair emissions per final message [planned TOOL-aHeardState-2]. Limits: no landing, it ends in `--handoff owner-landing`. The run starts in a fresh worktree off local main (75a1a52e), because this branch sits at origin/main, which local main lacks, so preflight would refuse it as carried.
Answer: Accept
