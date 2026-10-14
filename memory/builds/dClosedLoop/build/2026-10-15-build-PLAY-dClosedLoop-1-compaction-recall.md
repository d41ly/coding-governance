# Compaction experiment: the blind recall

**Serves:** research PLAY-dClosedLoop-1

Written after the owner's `/compact` (2026-10-15), and before the inventory, the answer key
(`build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-inventory.md`), was read. Every answer comes
from the context that survived. No file was read before answering. The probe file
(`build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-probes.md`) did not need a read: the compaction
re-attached it whole. This record is committed before the key is opened, so the commit order shows the
answers were blind. The scores and their sources are in
`build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-results.md`.

## [context] What the context held when answering

- **env**: the system prompt's environment block. It holds the model, the working directory, the
  scratchpad path (which contains the session id) and today's date.
- **charter**: the re-injected `CLAUDE.md`, which imports `AGENTS.md`. That brings the whole charter,
  including section 3's node registry, roles, tools and facts.
- **memindex**: the re-injected `MEMORY.md`, one line per memory and no bodies.
- **git**: the re-injected git snapshot: the branch, a clean tree, and five recent commits with their
  subjects (`bba25eb6b`, `6428425c5`, `b0b3f29bc`, `e56f13caa`, `44b43ebcd`).
- **reminder**: the commit-attribution reminder, which names "Claude Opus 5.5".
- **summary**: this compaction's summary, in nine sections.
- **tail**: the last assistant message before the compaction, kept verbatim after the summary. The
  summary says that message "was not sent before compaction began"; the tail shows it was.
- **reattached**: files the compaction attached again after the summary:
  - the probe file, whole;
  - the scratchpad's `amend_flow_roles.py`, whole;
  - the memory file `role-work-in-role-agents.md`, whole.

  The inventory and `build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md` were named as read but
  "too large to include".
- **hook**: the `SessionStart:compact` hook's output. It is the kickoff session's card, written
  2026-10-14T14:30:02+0300 by `manifest-check.sh --card --write`, with these sections:
  - `## task`, `## manifest`, `## read`, `## records`, `## classes` and `## open`;
  - the `READY` line;
  - a `now —` line reading `HEAD 97e782d5… · main · clean`. That is the primary tree, not this worktree
    (gap-orient-05 again). Its `dirty 11` is the kickoff's, not now's.

The `From` column names the channel each answer came from when it was written. Two values are not
channels: `inference` means reasoned from retained facts, and `prior` means the model's general
knowledge. `none` means nothing held it.

Confidence is one of four values:
- `sure`: the fact is held;
- `partial`: part of it is held, or it is reconstructed;
- `guess`: inferred or prior knowledge, not retained;
- `absent`: no answer.

## [answers]

| Q | Conf | From | Answer |
|---|---|---|---|
| Q01 | sure | hook, env, summary, reattached | `1799cb98` (`1799cb98-0882-4ab8-a308-19495d2a487a`); it continues session `b73dcb0a`, whose card holds the original kickoff |
| Q02 | sure | git, hook, summary | `branch/gov-architecture-plan-e34297` |
| Q03 | sure | hook | `742957fcf` (`742957fcf301507aa62449fb1ee4cd3e95eb99fa`), the kickoff's re-stamp commit |
| Q04 | partial | git, inference | `6428425c5`, the parent of the inventory's own commit `bba25eb6b`; if the LIVE.md commit came after the inventory was drafted, it was `b0b3f29bc` |
| Q05 | sure | summary, hook | `origin/main` at `ebce889c7`, local `main` at `97e782d51`; the dTracedLedger landing moved local `main` |
| Q06 | sure | hook, charter | node `d`, user `d41ly` |
| Q07 | absent | none | — |
| Q08 | sure | env, summary | 2026-10-15, from 2026-10-14 |
| Q09 | sure | summary | 83%: 834.1k tokens of 1M |
| Q10 | sure | charter, reminder, summary | `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. AGENTS.md's Facts name it, and the user's own instructions take precedence over the reminder, which names Claude Opus 5.5 |
| Q11 | sure | summary, memindex | Out of scope for this build. No build outside the chain may be counted on, so what it was to provide is designed in. Coordination went into dDeclaredLoop: leases as refs on the remote written by compare-and-swap, the mailbox, and dependency coordination. dLeasedFleet is retired from the chain |
| Q12 | sure | summary | (1) charter instructions: what every session or API call ingests first, and their hierarchy; (2) the DLG flow steps; (3) roles: deterministic workers with static system instructions plus tasks. They form the loop Instructions → Flow Step → Roles |
| Q13 | partial | summary | `placement` agent-places: the agent places the request alone, by disposition (continue, amend, new, patch, ask, none), and the placement's facts are checked. A placement whose facts fail the check is still refused (`placement.check` refuse, OR-6) |
| Q14 | sure | summary | Only when the session has no saved READY card (`kickoff.runs` no-ready-card). A resumed build or step looks its card up first and reorients from it |
| Q15 | sure | summary | Its truth is a ref per build on the remote. A session-start hook re-renders it, in the session's own tree, into an ignored per-worktree file that the charter's entry file imports, so it loads beside the charter at rank 1. The clone's cache is keyed by object id, and a terminal snapshot is committed (`card.store` all three, `card.snapshot` terminal-only) |
| Q16 | sure | summary, reattached | RL-3: "No sessions should orient inline, that's one of the major points. Upon a new user session being started, orientation should be handled by a scout role workflow, keeping any unnecessary tool output in the sidechain - outside the main session. Main session should receive an extensive, fully composed orientation card with all the necessary scope details to continue its session without the noise." |
| Q17 | sure | summary, reattached | RL-4: "Main session's primary purpose is to ORIENT its sidechain agents/roles - new prompt-writer roles receives only the details necessary to write a tight, well-oriented prompt from the main session and passes it further along to its destination. Main session, again, should keep as much of the noise out of its context as possible." |
| Q18 | sure | summary, reattached | The request is the ratification: starting a session and requesting a build ratifies it (`plan.ratification` request; hook-keyword, terminal-command and signed-commit are allowed values). The prompt-submit hook's intake record witnesses Plan's item 10 |
| Q19 | sure | summary, reattached | The role that meets it resolves it with its best effort, by the decision principles (P18), and records it. No build parks on it. That includes a fork the goal cannot survive, whose plan revision proceeds under the request's mandate (`run.on-owner-question` best-effort-recorded; FR-4, FR-12) |
| Q20 | sure | summary | dBoundRoles, a child of dDeclaredLoop |
| Q21 | sure | summary | 11: dOrderedCharter, dDeclaredLoop, dBoundRoles, dWitnessedBar, dRankedPlan, dIndexedDesign, dScopedBuild, dShippedRelease, dTendedCadence, dCalibratedLens, dConvergedCharter |
| Q22 | sure | summary | P22 position is derived, never remembered; P23 claims are trusted by key and source; P24 the checklist is a program; P25 role functions live only in role agents; P26 every exchange is a typed record. Only the titles are held, not the bodies |
| Q23 | sure | summary | The charter plus the build's orientation card; the charter wins a conflict |
| Q24 | sure | summary | orientation scout, prompt writer, planner, researcher, reuse scout, architect, spec writer, builder, tester, deployer, maintainer, reviewer (one role, its lens set per step, the loop included), skeptic, synthesizer |
| Q25 | sure | summary | (1) `next` names the item and its actor; (2) the driver hands the prompt writer the item's details, batching same-role tasks; (3) the prompt writer returns the task prompt; (4) the executor wraps it in a work order, hashed into a spawn marker, and spawns a fresh agent; (5) the agent returns its template through the schema-forced channel, with retries; (6) the driver resolves the witness, persists the return, reads the mailbox and calls `next` |
| Q26 | sure | summary, reattached | requesting-node |
| Q27 | sure | summary, reattached | turn-micro-formats |
| Q28 | sure | summary, reattached | every-item; the `intake` kind |
| Q29 | sure | summary, reattached | after-high |
| Q30 | sure | summary, reattached | per-batch |
| Q31 | sure | summary | 3 |
| Q32 | sure | summary | state-reads-only |
| Q33 | sure | summary | terminal-only |
| Q34 | sure | summary | fresh-when-idle |
| Q35 | sure | summary | record-only |
| Q36 | sure | summary | 90 keys, 85 presettable |
| Q37 | sure | summary | 95: HIGH 54, MED 36, LOW 5 |
| Q38 | sure | summary | Orient 13, Roles 8 |
| Q39 | partial | summary, reattached | H6, whether parallel units share one worktree: settled as shared, with commits queued by the executor and a worktree of its own as an owner-adjustable option per adopter (FR-5). H7, how landings are serialised: settled as the existing turnstile landing queue, its tooling and the lander reviewed at the lower-level step (FR-6). The holes' wording is reconstructed from their settlements |
| Q40 | partial | summary, reattached | H8, when a closing review runs a follow-up round: settled as `review.follow-up` after-high, adjustable per adopting repo (FR-9). H13, whether a dependent may land before its parent: settled as `deps.landing` hold-until-parent-lands (FR-7). The wording is reconstructed |
| Q41 | sure | summary | H2, H10, H11, H14 (FR-11) |
| Q42 | absent | none | — |
| Q43 | absent | none | — |
| Q44 | absent | none | — |
| Q45 | absent | none | — (only the per-step split survives: Plan 11, Design 10, Build 10, Test 8, Deploy 10, Maintain 9, stage review 7, Loop Review 5) |
| Q46 | sure | reattached | 605 spec edits and 565 code edits, plus 367 review folds, from the re-attached memory file; the summary does not hold them |
| Q47 | guess | inference | Harness returns are structured; direct-spawn returns are free prose. Inferred from the design's schema-forced channel, not retained |
| Q48 | guess | prior | Not retained. From prior knowledge of the MAST taxonomy (Cemri et al., 2025): disobeying the role specification is about 1.5%, and the largest category is specification issues (about 42%) |
| Q49 | absent | none | — |
| Q50 | absent | none | — |
| Q51 | absent | none | — |
| Q52 | absent | none | — |
| Q53 | absent | none | — |
| Q54 | sure | git | `44b43ebcd` |
| Q55 | absent | none | — (not among the five commits the git snapshot lists) |
| Q56 | absent | none | — |
| Q57 | absent | none | — (the rule survives: it must equal the `handoff: description — …` line `handoff.py` prints on stderr; the value does not) |
| Q58 | sure | summary | `python tools/roles/handoff.py render --role gov-researcher --build dClosedLoop --unit PLAY-dClosedLoop-1 --input "question=$(cat <file>)" --part task` |
| Q59 | sure | summary | `a retry count`, because `roles.retries` takes a free number rather than a named set, so the check must accept it as a free value |
| Q60 | sure | summary | The harness HTML-escapes `<`, `>` and `&` in a return, so a verbatim save unescapes them |
| Q61 | sure | summary | The authored `<!-- roster:units -->` pair, so the slot contract was red |
| Q62 | sure | summary | Apostrophes in a heredoc inside `-c` end in "unexpected EOF while looking for matching `''". The workaround: write the files with the Write tool and combine them in Python |
| Q63 | sure | summary | `build/2026-10-14-build-PLAY-dClosedLoop-1-roles.md` |
| Q64 | sure | summary, reattached | `build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md`, section `[closed]` |
| Q65 | sure | summary | `build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md` (the adopted preservation and both confirmations) and `build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-preserve.md` (the return); v2 carries `card.store` and `card.snapshot` |
| Q66 | sure | summary, memindex, reattached | `no-foreign-build-counted-on.md` and `role-work-in-role-agents.md` |
| Q67 | sure | summary | "Before we move to the next design step, let's run a quick experiment on context retention on session compaction which is important to how we'll shape orientation … Once it's complete, i'll ask you to compare what's left in your context against what you recorded and draw conclusions on how to more efficiently retain important facts in the governed unattended builds against automatic compaction." |
| Q68 | absent | none | — |
| Q69 | sure | summary | The orientation card: the resume delivered none (gap-orient-12) |
| Q70 | absent | none | — |
| Q71 | sure | summary | (1) this comparison: recall, score, trace, conclude, save and commit; (2) K1, the `core.bypass` default with-hooks-report, awaiting the owner's confirmation; (3) the lower-level design step: the executor's always-spawn harness and checklist engine, the turnstile landing queue and the lander, the hooks, and the card-import fixture; (4) the chain re-cut (the executor's home, and whether gap-orient-08 moves with it), then the owner's approval of the chain; (5) after approval: the spec writer writes the unit's spec; the declared audit runs through tier2-review.js and is folded; `handoff.py agents --write`; the chain folders are opened (README, roster, parents, gap ownership), registered, and `gen_build_index.py --write` run; DECISIONS.md rows; acceptance (c), seen red on a planted orphan; the live-build mapping; the full bar before any landing; merge and push only on the owner's ask. Hygiene check 21 stays red until the spec exists |
