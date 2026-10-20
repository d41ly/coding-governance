# Compaction experiment: what the session's context held before the owner's compaction (the inventory and answer key)

**Serves:** research PLAY-dClosedLoop-1

The owner, 2026-10-15: "Before we move to the next design step, let's run a quick experiment on context
retention on session compaction which is important to how we'll shape orientation. This session is
currently at 83% context (834.1k tokens out of 1M). Record what's currently available in your context, I
will trigger context compaction after this message. Once it's complete, i'll ask you to compare what's
left in your context against what you recorded and draw conclusions on how to more efficiently retain
important facts in the governed unattended builds against automatic compaction."

## [protocol] How the comparison runs

1. **Before the compaction**: this inventory, which is also the answer key, and the questions-only probe
   file `build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-probes.md` are written and committed.
2. **After the compaction, before reading either file**: every probe is answered from the remaining
   context alone, into a recall record.
3. **Then this key is read** and each answer scored: `exact`, `gist` (right in substance, details
   lost), `wrong`, or `absent`. Each surviving fact is traced to its source: the compaction summary, an
   instruction re-injected from disk, a hook's output, or a file read after the compaction.
4. **Conclusions** follow for keeping facts across automatic compaction in governed unattended builds.

**Where each fact lives** (the `Lives` column):
- R: a record in the build folder or git history, retrievable by reading.
- M: the auto-memory, whose index is re-injected.
- I: re-injected automatically at a compaction: the charter through `CLAUDE.md`, the memory index,
  the session-start hook's output, the environment block.
- X: in the context only, in no file.
- S1: inside the first compaction's summary, itself a lossy artifact.

**Limitations.**
- This inventory and the probe file are written at the very end of the transcript the summarizer
  reads, so they may bias it toward these facts. The canary (Q70) measures that bias: it appears
  nowhere else.
- The context's earlier work reached this session only through the first compaction's summary, so its
  facts are already second-hand.

## [segments] What the context holds, oldest to newest

| Seg | Content | Approximate share |
|---|---|---|
| S0 | The system prompt: tools, the safety rules, the environment, the artifact and widget guidance; deferred-tool lists | fixed |
| S1 | The first compaction's summary of session `1799cb98`'s earlier work: kickoff, the five stage researchers, design rounds 1 to 5, the walkthrough of ten builds, presets, foundations steps 1 and core, the flow walk, flow interactions FI-1 to FI-8 | small, dense |
| S2 | Instructions re-injected at that compaction: `CLAUDE.md` (which imports `AGENTS.md`), `MEMORY.md`, the session-start hook's card replay | about 25k tokens |
| S3 | The `dLeasedFleet` ruling: the foreign-build census, the coordination record, the README's missing roster pair, two v2 reads | large |
| S4 | The orientation round: four researchers (routing, cost, trust, determinism), their full returns, eight forks OR-1 to OR-8, the preservation researcher and the adopted design | the largest |
| S5 | Both orientation interpretations confirmed; the session model of one build and its fourteen holes; an inline stepper widget | medium |
| S6 | The roles round: four researchers (anatomy, coverage, interactions, prior art), full returns, eight forks RL-1 to RL-8, `dBoundRoles` | large |
| S7 | The flow revisit with roles: the item cycle, every step's role sequence, twelve forks FR-1 to FR-12, every hole closed | medium |
| S8 | This experiment | small |

Files read into context, in whole or in part: architecture v2 (in whole, early in S3), the flow
interactions record (in whole), the walkthrough (sections 1, 2, 4, 6 and 8), the flow record's
checklists and settlements, the gap register's rows and counts, the session log's sections,
`tools/roles/agents/gov-builder.agent.md`, `tools/roles/house/policy.toml`, and the nine
researchers' returns (in whole). Excerpts came from `skills/session-kickoff/SKILL.md`,
`skills/session-kickoff/manifest-check.sh`, `tools/hooks/scratch-guard.js`, `tools/hooks/agent-cap.js`,
`tools/roles/render_agents.py`, `tools/roles/roles_lib.py`, `tools/unattended/unattended.sh` and
`tools/workflows/unattended-unit.js`.

## [key] The answer key

| Q | Answer | Lives | Seg |
|---|---|---|---|
| Q01 | `1799cb98-0882-4ab8-a308-19495d2a487a` | R, I | S1 |
| Q02 | `branch/gov-architecture-plan-e34297` | R, I | S0 |
| Q03 | `742957fcf` (the kickoff manifest's re-stamp) | R, I | S1 |
| Q04 | `6428425c5`, LIVE.md re-rendered | R | S7 |
| Q05 | `origin/main` at `ebce889c7`; local `main` at `97e782d51`, four commits on: dTracedLedger traced check 23's 37 reds and routed them as asks | R | S3 |
| Q06 | node `d`, user `d41ly` | I | S0 |
| Q07 | `incms-test` (refused), `plugin:github:github` (bad authorization header), `plugin:incms:incms-test` (refused) | X | S3 |
| Q08 | 2026-10-15, from 2026-10-14 | X, R (filenames) | S6 |
| Q09 | 834.1k of 1M tokens, 83% | X | S8 |
| Q10 | `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, from `AGENTS.md`; the reminder named Opus 5.5, but the user's own instructions take precedence over it | I, X | S2 |
| Q11 | "dLeasedFleet is out of scope for this build, no foreign build should be counted on - bring any necessary functionality into this plan+design." Leases, the mailbox and dependency coordination became dDeclaredLoop's coordination feature; the census also removed waits on aOrientedCast's close, on three live builds in the mapping, and on dScriptedRepeat's recipe mode | R, M | S3 |
| Q12 | 1 the charter instructions; 2 the DLG steps (Development Lifecycle Governance); 3 roles | R | S6 |
| Q13 | `placement: agent-places`: the agent declares a disposition and its reason without asking; `placement.check: refuse` still refuses one whose facts fail (a live build, a free or own lease, a filed ask) | R | S4 |
| Q14 | Only in a session with no saved READY card for the build and slice it is placed into; otherwise a session reorients from the saved card | R | S4, S5 |
| Q15 | The truth is a ref per build on the remote, written by compare-and-swap; the clone's `.git/orientation/` is a cache keyed by object id; the build folder holds a terminal snapshot (`card.snapshot: terminal-only`). It reaches rank 1 through an ignored per-worktree file the charter's entry file imports, re-rendered by every session-start hook in the session's own tree; subagents get their slice through the brief and the subagent-start hook; Codex through a generated override file | R | S4 |
| Q16 | "No sessions should orient inline, that's one of the major points. Upon a new user session being started, orientation should be handled by a scout role workflow, keeping any unnecessary tool output in the sidechain - outside the main session. Main session should receive an extensive, fully composed orientation card with all the necessary scope details to continue its session without the noise." | R | S6 |
| Q17 | "Main session's primary purpose is to ORIENT its sidechain agents/roles - new prompt-writer roles receives only the details necessary to write a tight, well-oriented prompt from the main session and passes it further along to its destination. Main session, again, should keep as much of the noise out of its context as possible." | R | S6 |
| Q18 | The owner's request: "Starting a session and requesting a build _is_ ratification." (`plan.ratification: request`, witnessed by the prompt-submit hook; a hook keyword, a terminal command or a signed commit allowed) | R | S7 |
| Q19 | `run.on-owner-question: best-effort-recorded`: the role that meets it resolves it by the decision principles and records it; no build parks, a goal-level fork included, whose plan revision proceeds under the request's mandate (FR-4, FR-12) | R | S7 |
| Q20 | `dBoundRoles`, child of `dDeclaredLoop` | R | S6 |
| Q21 | Eleven: dOrderedCharter, dDeclaredLoop, dBoundRoles, dWitnessedBar, dRankedPlan, dIndexedDesign, dScopedBuild, dShippedRelease, dTendedCadence, dCalibratedLens, dConvergedCharter (dLeasedFleet retired) | R | S3, S6 |
| Q22 | P22 position is derived, never remembered; P23 claims are trusted by key and source; P24 the checklist is a program; P25 role functions live only in role agents; P26 every exchange between roles is a typed record | R | S4, S6 |
| Q23 | The charter and, beside it, the build's orientation card; the charter wins a conflict | R | S4, S5 |
| Q24 | Orientation scout, prompt writer, planner, researcher, reuse scout, architect, spec writer, builder, tester, deployer, maintainer, reviewer (one, lens per step), skeptic, synthesizer; the main session is the driver, not a worker | R, M | S6 |
| Q25 | 1 `next` names the item and its actor; 2 the driver hands the prompt writer the item's details; 3 the prompt writer returns the task prompt; 4 the executor wraps it in the work order and spawns the actor in a fresh agent; 5 the actor works inside its allowance and returns its template through the schema-forced channel, retried up to `roles.retries`; 6 the driver resolves the witness, persists the return, reads the mailbox, asks `next` | R | S7 |
| Q26 | `requesting-node` (background) | R | S7 |
| Q27 | `turn-micro-formats` | R | S7 |
| Q28 | `every-item`; the `intake` kind | R | S7 |
| Q29 | `after-high` | R | S7 |
| Q30 | `per-batch` | R | S7 |
| Q31 | 3, any count the owner sets | R | S6 |
| Q32 | `state-reads-only` | R | S6 |
| Q33 | `terminal-only` | R | S4 |
| Q34 | `fresh-when-idle` | R | S4 |
| Q35 | `record-only` | R | S4 |
| Q36 | 90 catalogue keys, 85 presettable, 85 preset rows | R | S7 |
| Q37 | 95: LOW 5, MED 36, HIGH 54 | R | S6 |
| Q38 | Orient 13, Roles 8 | R | S4, S6 |
| Q39 | H6: parallel units in one shared worktree contend for git's index lock; settled as shared, with the executor queueing commits and an own worktree allowed per adopter. H7: every landing on a node needs its primary tree; settled by the turnstile landing queue that already exists, the tooling reviewed at the lower-level step | R | S5, S7 |
| Q40 | H8: whether units born of a closing review are reviewed again; a follow-up only after a HIGH or BLOCKER (`review.follow-up: after-high`). H13: a dependent could land before its parent; held until the parent lands (`deps.landing: hold-until-parent-lands`) | R | S5, S7 |
| Q41 | H2 intake by hook, H10 back-steps recorded, H11 core checks at Build's exit, H14 a fresh session in the worktree | R | S7 |
| Q42 | A median 35 tool calls (p90 67) and 146k fresh input tokens | R | S4 |
| Q43 | 467k tokens | R | S4 |
| Q44 | 4.1%, 116 of 2,800 | R | S4 |
| Q45 | Role 11, main session 18, command 9, nobody 32 | R | S6 |
| Q46 | 605 spec edits across 233 files; 565 product edits across 98 files | R | S6 |
| Q47 | Direct spawns: 48 of 48 free text; harness spawns: 94 of 94 structured | R | S6 |
| Q48 | 1.5%; step repetition, at 15.7% | R | S6 |
| Q49 | 64.5% | R | S6 |
| Q50 | 0 of 5 | R | S4 |
| Q51 | `ae47198f40bd9a4c0` | R | S4 |
| Q52 | `46a0872ae7bf` | R | S4 |
| Q53 | `51b61c49e522` | R | S4 |
| Q54 | `44b43ebcd` | R | S6 |
| Q55 | `525b64a97` | R | S3 |
| Q56 | `tools/hooks/scratch-guard.js:796`; `skills/session-kickoff/manifest-check.sh:499` | R | S4 |
| Q57 | `dClosedLoop · PLAY-dClosedLoop-1 · research` | X | S4, S6 |
| Q58 | `python tools/roles/handoff.py render --role gov-researcher --build dClosedLoop --unit PLAY-dClosedLoop-1 --input "question=$(cat <file>)" --part task`, its stdout the task part and its stderr the description | S1, X | S4 |
| Q59 | `a retry count`, so `roles.retries` takes any count rather than a listed value | R | S6 |
| Q60 | The harness escaped `<`, `>` and `&` in the returned text as HTML entities | R | S4 |
| Q61 | The authored `<!-- roster:units -->` pair, which the slot contract requires | R | S3 |
| Q62 | `bash -c` reports "unexpected EOF while looking for matching" on apostrophes inside the heredoc; write the file with the Write tool instead | S1, X | S6 |
| Q63 | `build/2026-10-14-build-PLAY-dClosedLoop-1-roles.md`, `[map]` | R | S6 |
| Q64 | `build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md`, `[closed]` | R | S7 |
| Q65 | `build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md` (Adopted, preserving the card) and `build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-preserve.md` | R | S4 |
| Q66 | `no-foreign-build-counted-on` and `role-work-in-role-agents` | M, I | S3, S6 |
| Q67 | "draw conclusions on how to more efficiently retain important facts in the governed unattended builds against automatic compaction", to shape orientation | X | S8 |
| Q68 | "subagent output matched instruction-shaped pattern(s): settings-json" (once with "permissions-allow-deny"); its control tags were neutralized | X | S4, S6 |
| Q69 | The card: the resume printed only the process monitor and the wiring check | X | S6 |
| Q70 | `amber-tortoise-1734` | this file only | S8 |
| Q71 | K1 (`core.bypass`'s reading) awaits confirmation; the lower-level step (the executor's spawning harness, the turnstile, the lander, the hooks); the chain re-cut; approval; the spec writer's PLAY-dClosedLoop-1; the declared audit through `tools/workflows/tier2-review.js`; opening the chain's build folders; the acceptance joins; the live-build mapping; the full bar before any landing; merge and push only on the owner's ask | R, X | S1 to S7 |

## [canary] The canary

This experiment's canary phrase is `amber-tortoise-1734`. It appears in this file and nowhere else,
so its survival or loss measures how far writing a fact just before a compaction carries it through.
