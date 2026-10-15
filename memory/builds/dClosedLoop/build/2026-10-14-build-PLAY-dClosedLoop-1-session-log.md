# Session log — dClosedLoop: the kickoff card, every dispatch and its outcome, and where each record sits

**Serves:** research PLAY-dClosedLoop-1

Everything this build's sessions produce is kept in this folder, never only in a scratchpad (owner,
2026-10-14). This log holds what has no other home: the kickoff card as appended, each agent
dispatch and what became of it, events that changed the plan, and an index of the other records.

## Sessions

| Session | Node | Started | Outcome |
|---|---|---|---|
| `b73dcb0a-c6f8-44ce-865e-12f4b5031146` | d | 2026-10-14 14:01 +03:00 | Kickoff; manifest re-stamp `742957fcf`; build opened; five researcher handoffs rendered; four researchers dispatched and lost when the Claude Code process exited, the fifth never launched. |
| `1799cb98-0882-4ab8-a308-19495d2a487a` | d | 2026-10-14 | Resumed the build; owner note below; all five researchers re-dispatched from the same handoff files. |

## Owner notes

- 2026-10-14, session `1799cb98`: "One note, everything produced while working on the owner's task
  in this session - agent handoffs, suggestions, analysis, etc. must be saved in its build folder for
  future analysis, not lost in the scratchpad."

## The kickoff card, as appended in session b73dcb0a

The two kickoff questions and their answers are quoted in the brief,
`prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md`. The card's startup lines are the
SessionStart hook's and are not repeated; its body was:

```text
## task
- **Title:** dClosedLoop — re-architect gov onto one loop: Plan → Design → Build → Test → Deploy → Maintain, plus Review at any stage
- **Goal (1–2 sentences):** Agree with the owner on a target architecture in which every kit, skill, hook, gate and record of gov serves a declared stage contract of one loop for concurrent, multi-node, agentic development, and record today's gaps against it. Then open the ordered chain of builds that converges the product onto it.
- **IN scope:** (1) a derived inventory of what ships and how the parts call each other, mapped onto the stages; (2) a gap register per stage plus cross-cutting concerns: Review, multi-node concurrency, role agents, owner use, adopter deployment, cost; (3) design rounds with the owner until principles, stage contracts (entry/exit artifacts, roles, gates, enforcement) and Review triggers are ratified, each answer recorded as made; (4) the architecture record and gap register under memory/builds/dClosedLoop/; (5) the declared spec audit of that record, folded; (6) the chain: one build per stage plus a convergence build, each README naming its stage, scope, predecessor, acceptance, decisions and a planned unit roster; (7) a recommended mapping of the 24 non-terminal builds onto the chain.
- **OUT / non-goals** (explicit cut-line): no product code — nothing under tools/, skills/, coding-governance-agents.template.md or WIRE-INTO-PROJECT.md, no AGENTS.md re-render; no unit specs for chain builds, their own sessions write them (owner, 2026-10-14); no status change to an existing build or ask; no adopter-repo work; no merge or push without the owner's explicit ask.
- **To-do:** (1) commit the manifest re-stamp in memory/guides/SESSION-KICKOFF.md; (2) open memory/builds/dClosedLoop/ with `spec-audit: 2026-10-14` and route the card to it; (3) inventory from the map dossiers, tools/gate-legs.json, hooks and guides, via a bounded read-only role fan-out writing to disk; (4) the gap register, file-cited; (5) present state and gaps, run the design rounds, record each ratified answer in memory/DECISIONS.md; (6) the architecture record; (7) audit it through tools/workflows/tier2-review.js and fold; (8) open the chain folders, gen_build_index.py --write, stage; (9) bar and commit; merge and push only on ask.
- **Reuse:** memory/map/ and tools/gate-legs.json as the derived inventory; tools/drift-audit/drift_report.py as gap evidence; memory/builds/aDeployScout/spec/governance-deployer-research.md for Deploy; memory/guides/BUILD-METHOD.md for Build; tools/workflows/tier2-review.js for the audit; tools/memory-tree/gen_build_index.py for opening builds and memory/LIVE.md.
- **Acceptance check:** (a) the ratified answers exist as decision rows tools/memory-recall/query.py returns; (b) the regenerated memory/LIVE.md lists every chain build as non-terminal, each README naming its stage and predecessor; (c) a join of the gap register against the chain READMEs shows every gap owned by exactly one build and every build owning a gap, seen red on a planted orphan first; (d) the audit report sits under memory/builds/dClosedLoop/reviews/ with every finding folded or rejected with a reason.
- **Gates it must pass:** per pass on the staged tree: kickoff-manifest ratchet, memory hygiene, build README slot contract, no stale generated output (`bash tools/run-gates/run-gates.sh --regen`); the full bar `bash tools/run-gates/run-gates.sh` before any landing.

## manifest
manifest-audit: delta last-audit and last-body-change advanced to ebce889c7 after re-reading §B against the 15 watched commits; no claim stale (tools/gate-legs.json gained two legs §B points at, never restates) · watch-commits-since-stamp: 4

## read
AGENTS.md · coding-governance-agents.template.md · .claude/rules/product.md · memory/DECISIONS.md · memory/guides/BUILD-METHOD.md · memory/guides/REVIEW-PROTOCOL.md · memory/guides/UNATTENDED-PROTOCOL.md · memory/HYGIENE.md · WIRE-INTO-PROJECT.md · memory/LIVE.md · memory/map/features/

## records
DEPL-aDeployScout-1 (govkit, awaiting owner approval) · TOOL-aWrittenMethod-1 · PLAY-aOrientedCast-2 · KICK-aOrientedCast-2 · TOOL-aMooredAnchor-1 · open asks: TOOL-aLevelledCopy-24 (HIGH), TOOL-aHonedRuleset-15, KICK-aHonedRuleset-1, KICK-aReplayedCard-5, TOOL-dDerivedDocket-60
Recall terms used: charter template kit govkit deployer bar legs build-method unattended roles kickoff spec lifecycle

## classes
fixture-passes-by-finding-nothing · guard-above-a-fold-makes-its-fallback-dead · heredoc-escape-reaches-the-regex · inline-fence-swallows-the-rest-of-the-file · staged-break-substitutes-a-synthetic-value · two-answers-to-one-question · a-merge-of-the-default-branch-read-as-additions · amendment-leaves-its-other-half-standing · ledger-token-wrapped-across-a-line-joins-nothing · allowlist-narrower-than-the-root-it-guards · conf-value-interpolated-into-a-regex · fold-text-is-unreviewed-surface · one-value-field-records-a-mixed-outcome · overlap-judged-from-the-invocation-interval · record-file-read-by-line-position · retirement-inventory-misses-readers-by-value

## open
spec audit: declared 2026-10-14 (owner) · chain depth: README plus unit roster (owner) · 24 non-terminal builds and 17 remote claims to map · 15 nonzero drift signals are Maintain-stage evidence

READY — dClosedLoop · node d · branch/gov-architecture-plan-e34297 · base ebce889c7 · Tier-2 · gates kickoff-manifest ratchet, memory hygiene, build README slot contract, regen, full bar before landing
```

## Dispatches

Each handoff file under `prompts/` holds the full prompt its agent was handed, the research question
included; the agent lines derived by `tools/roles/handoff.py agents` go to this build's agent ledger.

| # | Role | Stage | Handoff | Session | Outcome | Return recorded in |
|---|---|---|---|---|---|---|
| 1 | gov-researcher | Plan | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md` | b73dcb0a | lost: process exited | — |
| 2 | gov-researcher | Design | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md` | b73dcb0a | lost: process exited | — |
| 3 | gov-researcher | Build | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md` | b73dcb0a | lost: process exited | — |
| 4 | gov-researcher | Test | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md` | b73dcb0a | lost: process exited | — |
| 5 | gov-researcher | Deploy | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-5-researcher.md` | b73dcb0a | never launched: the tool call returned an internal error | — |
| 6 | gov-researcher | Plan | handoff 1, unchanged | 1799cb98 | returned, 5m17s, 23.0k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-plan.md` |
| 7 | gov-researcher | Design | handoff 2, unchanged | 1799cb98 | returned, 5m24s, 29.0k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-design.md` |
| 8 | gov-researcher | Build | handoff 3, unchanged | 1799cb98 | returned, 4m39s, 24.0k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-build.md` |
| 9 | gov-researcher | Test | handoff 4, unchanged | 1799cb98 | returned, 3m47s, 20.9k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-test.md` |
| 10 | gov-researcher | Deploy | handoff 5, unchanged | 1799cb98 | returned, 4m08s, 22.6k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-deploy.md` |
| 11 | gov-researcher | Orientation: routing and step | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-6-researcher.md` | 1799cb98 | returned, 6m21s, 27.1k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-routing.md` |
| 12 | gov-researcher | Orientation: cost | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-7-researcher.md` | 1799cb98 | returned, 7m01s, 35.9k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-cost.md` |
| 13 | gov-researcher | Orientation: trust | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-8-researcher.md` | 1799cb98 | returned, 7m53s, 32.4k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-trust.md` |
| 14 | gov-researcher | Orientation: determinism | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-9-researcher.md` | 1799cb98 | returned, 8m43s, 47.9k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-determinism.md` |
| 15 | gov-researcher | Orientation: preserving the card | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-10-researcher.md` | 1799cb98 | returned, 4m45s, 22.8k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-preserve.md` |
| 16 | gov-researcher | Roles: anatomy | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-11-researcher.md` | 1799cb98 | returned, 3m55s, 21.8k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-roles-anatomy.md` |
| 17 | gov-researcher | Roles: coverage | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-12-researcher.md` | 1799cb98 | returned, 4m37s, 23.9k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-roles-coverage.md` |
| 18 | gov-researcher | Roles: interactions | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-13-researcher.md` | 1799cb98 | returned, 4m40s, 22.0k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-roles-interactions.md` |
| 19 | gov-researcher | Roles: prior art | `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-14-researcher.md` | 1799cb98 | returned, 4m41s, 24.5k out | `build/2026-10-14-build-PLAY-dClosedLoop-1-research-roles-priorart.md` |
| 20 | gov-researcher | Flow layer: Plan, Design and Build items | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-1-researcher.md` | 1799cb98 | returned, 7m54s, 46.3k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-a.md` |
| 21 | gov-researcher | Flow layer: Test, Deploy, Maintain and review items | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-2-researcher.md` | 1799cb98 | returned, 7m02s, 37.8k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-b.md` |
| 22 | gov-researcher | Memory layer: builds | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-3-researcher.md` | 1799cb98 | returned, 10m58s, 39.4k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-builds.md` |
| 23 | gov-researcher | Memory layer: the ask register and the decision index | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-4-researcher.md` | 1799cb98 | returned, 7m05s, 39.7k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-asks-decisions.md` |
| 24 | gov-researcher | Memory layer: the codebase map and the reuse tools | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-5-researcher.md` | 1799cb98 | returned, 6m23s, 27.9k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-map-reuse.md` |
| 25 | gov-researcher | Memory layer: code annotations, the gotchas and the lexicon | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-6-researcher.md` | 1799cb98 | returned, 6m32s, 29.0k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-annotations.md` |
| 26 | gov-researcher | Memory layer: the tooling map | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-7-researcher.md` | 1799cb98 | returned, 7m55s, 33.0k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-tooling.md` |
| 27 | gov-researcher | Lexicon: the kit as built and as enforced | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-8-researcher.md` | 1799cb98 | returned, 5m23s, 28.0k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-kit.md` |
| 28 | gov-researcher | Lexicon: the offender population and the pin's history | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-9-researcher.md` | 1799cb98 | returned, 7m43s, 38.9k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-population.md` |
| 29 | gov-researcher | Lexicon: prior art and the forced-name mechanism | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-10-researcher.md` | 1799cb98 | returned, 8m15s, 38.8k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-prior-art.md` |
| 30 | gov-researcher | Runtime: the executor and `next` | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-11-researcher.md` | 1799cb98 | returned, 7m21s, 30.8k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-executor.md` |
| 31 | gov-researcher | Runtime: the spawn harness | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-12-researcher.md` | 1799cb98 | returned, 11m10s, 41.5k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-spawn.md` |
| 32 | gov-researcher | Runtime: hooks, isolation and supervision | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-13-researcher.md` | 1799cb98 | returned, 9m00s, 30.1k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-hooks.md` |
| 33 | gov-researcher | Runtime: sessions, context, scheduling, harnesses and nodes | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-14-researcher.md` | 1799cb98 | returned, 8m02s, 33.7k out | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-sessions.md` |
| 34 | `tier2-review.js`: five `gov-spec-reviewer`, five `gov-skeptic` and one `gov-synthesizer`, all at medium | Runtime: Tier-2 review, run A | the args in `build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md` `[runs]` | 1799cb98 | returned, CLEAN WITH FIXES, 56 of 60 confirmed | `reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md` |
| 35 | the same | Runtime: Tier-2 review, run B | the same | 1799cb98 | returned, CLEAN WITH FIXES, 57 of 61 confirmed | `reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-b.md` |

Maintain, and the machinery by which the loop corrects itself, is researched by the main loop in
this session rather than by a sixth agent: the direct-spawn budget is five per owner turn
(`tools/hooks/agent-cap.js`, `CAP` and `SLOT_TTL_MS`). Its record is
`build/2026-10-14-build-PLAY-dClosedLoop-1-research-maintain.md`.

The lines `tools/roles/handoff.py agents --handoff <path>` derived for the five handoffs, verbatim.
The verb's `--write` held the agent ledger back, because no spec defines `PLAY-dClosedLoop-1` yet;
it is re-run once the spec lands. Rows 1 to 4 have no `returned` line: their process died.

```text
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md) · writes none · gates none · run direct/aa7e3d6c065321e82
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-1-researcher.md) · writes none · gates none · run direct/adedd1eec07881ab6
- returned — gov-researcher · wrote 0 files · 5m17s · 23.0k out · run direct/adedd1eec07881ab6
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md) · writes none · gates none · run direct/accff2d8daecc1566
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-2-researcher.md) · writes none · gates none · run direct/a0cce9c329c0c17d2
- returned — gov-researcher · wrote 0 files · 5m24s · 29.0k out · run direct/a0cce9c329c0c17d2
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md) · writes none · gates none · run direct/a6e0851dac91f6647
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md) · writes none · gates none · run direct/a5886ceb960724423
- returned — gov-researcher · wrote 0 files · 4m39s · 24.0k out · run direct/a5886ceb960724423
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md) · writes none · gates none · run direct/af05ef0640a026274
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-4-researcher.md) · writes none · gates none · run direct/a636d8714b2045642
- returned — gov-researcher · wrote 0 files · 3m47s · 20.9k out · run direct/a636d8714b2045642
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-5-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-5-researcher.md) · writes none · gates none · run direct/aaf0e3ee001682096
- returned — gov-researcher · wrote 0 files · 4m08s · 22.6k out · run direct/aaf0e3ee001682096
```

The orientation round's four handoffs (dispatches 11 to 14), their lines derived the same way and held
from the ledger for the same reason:

```text
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-6-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-6-researcher.md) · writes none · gates none · run direct/aeec60231dad94d52
- returned — gov-researcher · wrote 0 files · 6m21s · 27.1k out · run direct/aeec60231dad94d52
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-7-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-7-researcher.md) · writes none · gates none · run direct/a20e50b8f18ac8f59
- returned — gov-researcher · wrote 0 files · 7m01s · 35.9k out · run direct/a20e50b8f18ac8f59
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-8-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-8-researcher.md) · writes none · gates none · run direct/ae47198f40bd9a4c0
- returned — gov-researcher · wrote 0 files · 7m53s · 32.4k out · run direct/ae47198f40bd9a4c0
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-9-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-9-researcher.md) · writes none · gates none · run direct/a5adf84caf1a988de
- returned — gov-researcher · wrote 0 files · 8m43s · 47.9k out · run direct/a5adf84caf1a988de
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-10-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-10-researcher.md) · writes none · gates none · run direct/a9189c646b6ed94eb
- returned — gov-researcher · wrote 0 files · 4m45s · 22.8k out · run direct/a9189c646b6ed94eb
```

The roles round's four handoffs (dispatches 16 to 19), derived the same way and held from the ledger.
Dispatch 18's `returned` line says `wrote 0 files`, while its return reports saving a helper script in the
session scratchpad through its shell: the derivation, like the write gate, counts only Write and Edit
calls.

```text
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-11-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-11-researcher.md) · writes none · gates none · run direct/a1c33d3cab73979e7
- returned — gov-researcher · wrote 0 files · 3m55s · 21.8k out · run direct/a1c33d3cab73979e7
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-12-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-12-researcher.md) · writes none · gates none · run direct/a64b914ce553c4ab5
- returned — gov-researcher · wrote 0 files · 4m37s · 23.9k out · run direct/a64b914ce553c4ab5
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-13-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-13-researcher.md) · writes none · gates none · run direct/a444485861ad18d2b
- returned — gov-researcher · wrote 0 files · 4m40s · 22.0k out · run direct/a444485861ad18d2b
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-14-prompt-PLAY-dClosedLoop-1-14-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-14-researcher.md) · writes none · gates none · run direct/a2750bbc386a192e4
- returned — gov-researcher · wrote 0 files · 4m41s · 24.5k out · run direct/a2750bbc386a192e4
```

The flow layer's item audit is two handoffs, dispatches 20 and 21. Their lines were derived the same
way and held from the ledger:

```text
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-1-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-1-researcher.md) · writes none · gates none · run direct/a9cb53e6fd6bb4661
- returned — gov-researcher · wrote 0 files · 7m54s · 46.3k out · run direct/a9cb53e6fd6bb4661
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-2-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-2-researcher.md) · writes none · gates none · run direct/a2e4ed3684d8964ea
- returned — gov-researcher · wrote 0 files · 7m02s · 37.8k out · run direct/a2e4ed3684d8964ea
```

The memory layer's five handoffs, dispatches 22 to 26, were derived the same way and held from the
ledger. Five is the direct-spawn budget for one owner turn:

```text
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-3-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-3-researcher.md) · writes none · gates none · run direct/ad130bc5b0b446984
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-4-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-4-researcher.md) · writes none · gates none · run direct/a683df94188e34f7a
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-5-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-5-researcher.md) · writes none · gates none · run direct/aa631366c077d00d1
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-6-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-6-researcher.md) · writes none · gates none · run direct/a0f40dd21c9243c66
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-7-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-7-researcher.md) · writes none · gates none · run direct/aaba36be47df28242
- returned — gov-researcher · wrote 0 files · 10m58s · 39.4k out · run direct/ad130bc5b0b446984
- returned — gov-researcher · wrote 0 files · 7m05s · 39.7k out · run direct/a683df94188e34f7a
- returned — gov-researcher · wrote 0 files · 6m23s · 27.9k out · run direct/aa631366c077d00d1
- returned — gov-researcher · wrote 0 files · 6m32s · 29.0k out · run direct/a0f40dd21c9243c66
- returned — gov-researcher · wrote 0 files · 7m55s · 33.0k out · run direct/aaba36be47df28242
```

The lexicon review's three handoffs, dispatches 27 to 29, were derived the same way and held from
the ledger:

```text
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-8-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-8-researcher.md) · writes none · gates none · run direct/a8c799ae3f8451de3
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-9-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-9-researcher.md) · writes none · gates none · run direct/ab88368be2b01aaa5
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-10-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-10-researcher.md) · writes none · gates none · run direct/a3c14cf4c0062421b
- returned — gov-researcher · wrote 0 files · 5m23s · 28.0k out · run direct/a8c799ae3f8451de3
- returned — gov-researcher · wrote 0 files · 7m43s · 38.9k out · run direct/ab88368be2b01aaa5
- returned — gov-researcher · wrote 0 files · 8m15s · 38.8k out · run direct/a3c14cf4c0062421b
```

The runtime round's four handoffs, dispatches 30 to 33, were derived the same way and held from
the ledger:

```text
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-11-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-11-researcher.md) · writes none · gates none · run direct/a27a0b29a52118e7c
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-12-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-12-researcher.md) · writes none · gates none · run direct/a09d005d5401a1ffa
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-13-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-13-researcher.md) · writes none · gates none · run direct/abd9da98c6527b6eb
- agent — gov-researcher · effort medium · model claude-opus-5-5 · PLAY-dClosedLoop-1 · prompt [2026-10-15-prompt-PLAY-dClosedLoop-1-14-researcher.md](memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-14-researcher.md) · writes none · gates none · run direct/aa94d21851651d208
- returned — gov-researcher · wrote 0 files · 7m21s · 30.8k out · run direct/a27a0b29a52118e7c
- returned — gov-researcher · wrote 0 files · 11m10s · 41.5k out · run direct/a09d005d5401a1ffa
- returned — gov-researcher · wrote 0 files · 9m00s · 30.1k out · run direct/abd9da98c6527b6eb
- returned — gov-researcher · wrote 0 files · 8m02s · 33.7k out · run direct/aa94d21851651d208
```

The two Tier-2 rounds, dispatches 34 and 35, ran as Workflow runs. `tools/roles/handoff.py agents --run <run> --session <transcript>`
derived their lines, which are held from the ledger. Each run's first agent is the harness's resume probe.

```text
- agent — workflow-subagent · effort max · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, resume:probe · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/abb3225c4744455e9
- returned — workflow-subagent · wrote 0 files · 12s · 964 out · run wf_6508cb22-7d6/abb3225c4744455e9
- agent — gov-spec-reviewer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, find:coherence · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/aec30d37d8e3e0066
- returned — gov-spec-reviewer · wrote 0 files · 3m52s · 23.7k out · run wf_6508cb22-7d6/aec30d37d8e3e0066
- agent — gov-spec-reviewer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, find:grounding · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/aac52732c1ab4dba5
- returned — gov-spec-reviewer · wrote 0 files · 3m34s · 20.9k out · run wf_6508cb22-7d6/aac52732c1ab4dba5
- agent — gov-spec-reviewer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, find:reuse · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/ab20566ea04b1fe57
- returned — gov-spec-reviewer · wrote 0 files · 6m10s · 32.7k out · run wf_6508cb22-7d6/ab20566ea04b1fe57
- agent — gov-spec-reviewer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, find:blast-radius · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/a97f86e719bdd4bc1
- returned — gov-spec-reviewer · wrote 0 files · 5m23s · 33.9k out · run wf_6508cb22-7d6/a97f86e719bdd4bc1
- agent — gov-spec-reviewer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, find:failure-envelope · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/a72d89ac95c36c16a
- returned — gov-spec-reviewer · wrote 0 files · 2m30s · 14.9k out · run wf_6508cb22-7d6/a72d89ac95c36c16a
- agent — gov-skeptic · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, verify:ids-1-12 · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/a53450609f1bc4f83
- returned — gov-skeptic · wrote 0 files · 1m07s · 7.2k out · run wf_6508cb22-7d6/a53450609f1bc4f83
- agent — gov-skeptic · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, verify:ids-13-24 · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/a714bedf2ad6a7db8
- returned — gov-skeptic · wrote 0 files · 1m56s · 11.8k out · run wf_6508cb22-7d6/a714bedf2ad6a7db8
- agent — gov-skeptic · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, verify:ids-25-36 · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/a991ea8bb7b171f83
- returned — gov-skeptic · wrote 0 files · 1m28s · 9.2k out · run wf_6508cb22-7d6/a991ea8bb7b171f83
- agent — gov-skeptic · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, verify:ids-37-48 · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/add182940bcb49d6e
- returned — gov-skeptic · wrote 0 files · 1m29s · 8.9k out · run wf_6508cb22-7d6/add182940bcb49d6e
- agent — gov-skeptic · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, verify:ids-49-60 · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_6508cb22-7d6/ad5c98bb748a9d16a
- returned — gov-skeptic · wrote 0 files · 55s · 5.8k out · run wf_6508cb22-7d6/ad5c98bb748a9d16a
- agent — gov-synthesizer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, synth · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes review · gates none · run wf_6508cb22-7d6/a3dc8caf010741d61
- returned — gov-synthesizer · wrote 1 file · 5m01s · 42.2k out · run wf_6508cb22-7d6/a3dc8caf010741d61
```

```text
- agent — workflow-subagent · effort max · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, resume:probe · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/a8438ea97f460b4ac
- returned — workflow-subagent · wrote 0 files · 13s · 1.2k out · run wf_3c895b43-8da/a8438ea97f460b4ac
- agent — gov-spec-reviewer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, find:coherence · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/ac1f84d585e57cf3f
- returned — gov-spec-reviewer · wrote 0 files · 3m36s · 22.5k out · run wf_3c895b43-8da/ac1f84d585e57cf3f
- agent — gov-spec-reviewer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, find:grounding · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/afad235c65dfad5b5
- returned — gov-spec-reviewer · wrote 0 files · 3m35s · 22.2k out · run wf_3c895b43-8da/afad235c65dfad5b5
- agent — gov-spec-reviewer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, find:reuse · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/a0ec620f344b61b05
- returned — gov-spec-reviewer · wrote 0 files · 5m53s · 34.8k out · run wf_3c895b43-8da/a0ec620f344b61b05
- agent — gov-spec-reviewer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, find:blast-radius · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/ac299fe825c339c31
- returned — gov-spec-reviewer · wrote 0 files · 5m05s · 29.3k out · run wf_3c895b43-8da/ac299fe825c339c31
- agent — gov-spec-reviewer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, find:failure-envelope · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/a96c66cc22cfbe0b4
- returned — gov-spec-reviewer · wrote 0 files · 2m37s · 16.0k out · run wf_3c895b43-8da/a96c66cc22cfbe0b4
- agent — gov-skeptic · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, verify:ids-1-13 · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/a09b4ac363774f558
- returned — gov-skeptic · wrote 0 files · 1m19s · 7.9k out · run wf_3c895b43-8da/a09b4ac363774f558
- agent — gov-skeptic · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, verify:ids-14-26 · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/a39412b7f80540c2a
- returned — gov-skeptic · wrote 0 files · 1m36s · 9.6k out · run wf_3c895b43-8da/a39412b7f80540c2a
- agent — gov-skeptic · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, verify:ids-27-39 · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/a0a2c8589fee727c9
- returned — gov-skeptic · wrote 0 files · 1m49s · 10.7k out · run wf_3c895b43-8da/a0a2c8589fee727c9
- agent — gov-skeptic · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, verify:ids-40-52 · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/a0954856760f1be49
- returned — gov-skeptic · wrote 0 files · 2m26s · 12.9k out · run wf_3c895b43-8da/a0954856760f1be49
- agent — gov-skeptic · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, verify:ids-53-61 · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes none · gates none · run wf_3c895b43-8da/aa0c743c242313573
- returned — gov-skeptic · wrote 0 files · 1m02s · 6.0k out · run wf_3c895b43-8da/aa0c743c242313573
- agent — gov-synthesizer · effort medium · model claude-opus-5-5 · dClosedLoop, spec-audit round 1, synth · prompt [tier2-review.js](tools/workflows/tier2-review.js) · writes review · gates none · run wf_3c895b43-8da/a0c25d653455d9690
- returned — gov-synthesizer · wrote 1 file · 5m21s · 44.9k out · run wf_3c895b43-8da/a0c25d653455d9690
```

## Events

- 2026-10-14, session b73dcb0a: the kickoff manifest failed checks 5 and 9; re-read §B, nothing
  stale, re-stamped in `742957fcf`.
- 2026-10-14, session b73dcb0a: the build folder was opened unregistered, and `gen_build_index.py
  --check-format` named the missing generated regions; registered in
  `memory/project/readme-contract.txt` and rendered with `--write`.
- 2026-10-14, session 1799cb98: the full memory-hygiene run reds check 21 on this build's records
  until the spec defines `PLAY-dClosedLoop-1`, which is expected, and check 23 on acceptance-ledger
  lines of `aSparedSpawn` and `aOrientedCast`, which this build did not write: Test-stage evidence.
- 2026-10-14, session 1799cb98: the context was compacted, and the session reoriented from this
  build's records and the card the compact hook re-rendered. Local main sits at `97e782d51`, four
  commits past this branch's base `742957fcf`: dTracedLedger traced check 23's 37 reds at
  `ebce889c7` and routed them to their owners as asks. `origin/main` is still `ebce889c7`.
- 2026-10-14, session 1799cb98: the owner ruled dLeasedFleet out of scope, with no build outside the
  chain counted on. The census found four reliances: dLeasedFleet itself, aOrientedCast's close,
  three more live builds' closes in the adopted mapping, and dScriptedRepeat's recipe mode. The
  coordination record moves leases, the mailbox and dependency coordination into dDeclaredLoop;
  the chain has ten builds.
- 2026-10-14, session 1799cb98: the owner asked how sessions and agents enter, orient, resume and
  progress along the flow. Four researchers measured routing, cost, trust and determinism; the
  orientation record holds the design and eight forks, answered; a fifth researcher was sent at the
  owner's request to find a better way to preserve the build's card.
- 2026-10-14, session 1799cb98: the owner confirmed both orientation interpretations and asked for a
  session modelled through every step; the model found fourteen holes, recorded and not yet decided.
- 2026-10-14, session 1799cb98: the owner deferred the flow steps' polish until all three layers are
  consolidated and opened the roles layer; four researchers were sent on anatomy, coverage,
  interactions and prior art.
- 2026-10-14, session 1799cb98: the owner answered eight roles forks: one reviewer, three operations
  roles, orientation as a scout's sidechain workflow, a prompt writer for every task, cheap state reads
  only for the main session, a roles build of its own (`dBoundRoles`), schema-forced returns with three
  retries, and a harness that can always spawn subagents.
- 2026-10-15, session 1799cb98: the owner opened the flow revisit with roles in place; the flow-roles
  record sets one cycle for every role item and maps each step's role sequence and routes.
- 2026-10-15, session 1799cb98: twelve forks answered across three rounds settled every hole the session
  model left, H1 to H16; the owner's request became the ratification, and no fork parks a build.
- 2026-10-15, session 1799cb98: the owner set up a compaction-retention experiment at 834.1k of 1M
  tokens; the inventory (the answer key) and a questions-only probe file were committed before the
  owner's compaction, to be answered blind afterwards and scored.
- 2026-10-15, session 1799cb98: after the owner's compaction, the probes were answered blind into the
  recall record, committed at `ae229d4ee` before the key was opened, then scored and traced in the
  results record. The summary kept decisions, policies, procedure and the owner's words, and dropped
  identifiers, measured numbers, qualifiers and harness notices. The compact hook replayed the
  kickoff's card. Conclusions for unattended builds were drawn, and three forks, CX-1 to CX-3, put to
  the owner.
- 2026-10-15, session 1799cb98: the owner settled CX-1 to CX-3. Compaction with the current card is the
  default and a fresh session at the boundary is allowed; the card's pointers are updated as the build
  progresses; notices are recorded by default nowhere, and all three values are allowed; both gaps and
  the compaction checks are recorded. v2, the register and the results record were amended.
- 2026-10-15, session 1799cb98: the owner asked how the product design looks at this stage. An
  overview was composed from the records rather than from the compaction summary, saved with its two
  diagrams, and shown.
- 2026-10-15, session 1799cb98: K1 was explained and put back to the owner as a fork, and the owner
  confirmed "the violator pays" (`with-hooks-report` as read). The foundations record and v2 were
  amended, and dShippedRelease's lander gains a core re-check on the landed tree.
- 2026-10-15, session 1799cb98: the owner opened a layer-by-layer review: four mandatory layers
  (instruction, DLG, roles, memory) and expansion layers, then added instrument, monitoring and
  deployment mid-turn. The instruction layer was measured and set against the design, and the layer
  model was reframed as capabilities, with Runtime proposed as a core layer. Forks were put to the owner.
- 2026-10-15, session 1799cb98: the owner settled L1 to L4: capabilities with Runtime as a core layer,
  all four expansions, the charter at level 0 with the card at level 1, and Skills as level-4 thin
  entries. v2 gains `[layers]`, P11 and P13 are amended, and P27 and P28 are added; nine gaps join the
  register.
- 2026-10-15, session 1799cb98: the owner opened the flow layer's review. It was set against the
  design, and three new gaps were proposed. An item-by-item audit of the 70 checklist items went to two
  researchers (dispatches 20 and 21). Forks were put to the owner.
- 2026-10-15, session 1799cb98: both researchers returned, and the owner settled F2-1 to F2-4: Maintain
  as an expansion, breakpoints anywhere, withdraw or supersede, and programs with dependencies. P6,
  P7, P20 and P24 were amended, two policies and five gaps added, and the audit's consistency fixes
  recorded.
- 2026-10-15, session 1799cb98: before layer 3, the owner asked for each flow step to be defined.
  Entry, the five core steps and the breakpoint were defined item by item, from the audit with its
  fixes applied. Three open questions were put to the owner.
- 2026-10-15, session 1799cb98: the owner answered all three:
  - one spec-audit round by default (`review.design.rounds`);
  - an unverified finding filed as an ask (`review.unverified`), with the owner's question about
    what an ask is answered in the record;
  - the slower test levels run at landing without Maintain (`tests.without-cadence`).

  Four keys joined the catalogue.
- 2026-10-15, session 1799cb98: the owner opened the roles layer's review. It was set against the
  settled roles, orientation and flow designs. The main loop measured what role agents receive and
  re-derive over 171 transcripts, and derived the role-by-step matrix from the step definitions.
  It proposed a trust mechanism (P29) and recorded eight gaps, all owned by dBoundRoles. Four
  questions were put to the owner.
- 2026-10-15, session 1799cb98: the owner settled F3-1 to F3-4:
  - every keyed fact is acted on;
  - answered calls are refused, naming the anchor;
  - verifiers start cold;
  - a false handed fact is repaired, recorded and filed against its producer's record. This is the
    owner's answer, over the recommended return.

  P29 and four keys joined v2.
- 2026-10-15, session 1799cb98: the owner opened the memory layer's review. The same message noted
  that layer 3 still owes its mechanical shape, with aScoutedSeam's benchmark as evidence. The note is
  recorded with layer 3 as `gap-roles-18`, for a later revisit. Five researchers were dispatched,
  22 to 26, one per part of the memory layer. Their briefs hand the settled facts as content.
- 2026-10-15, session 1799cb98: all five researchers returned. Their returns are saved verbatim,
  and their probe scripts are gathered into one evidence record. The memory design was written
  against them:
  - one memory contract;
  - decisions split by kind, with reuse entries as ranked instruction units;
  - a generated caller map;
  - a `gov:note` annotation grammar;
  - the tooling verdicts.

  Eight questions were put to the owner. Two harness notices fired on the returns of dispatches 25
  and 26, pattern `settings-json`, because both cite `.claude/settings.json`. Neither return asked
  for an action, and under `notices.record` (`none`) the notices are not kept.
- 2026-10-15, session 1799cb98: the owner settled F4-1 to F4-8, each with the recommended option:
  - dTotalRecall joined the chain as the memory layer's build;
  - P30 and eight keys joined v2;
  - seventeen gaps were registered.
- 2026-10-15, session 1799cb98: the owner asked for a full review of the lexicon kit:
  - sessions raise its offender pin for verbs that third-party kits force, which are not debt;
  - the kit should exclude such verbs by default, perhaps from tables per popular kit;
  - its enforcement of naming should be reviewed and improved.

  Three researchers were dispatched, 27 to 29.
- 2026-10-15, session 1799cb98: the three lexicon researchers returned. Their returns are saved
  verbatim, and their probe files are gathered into one evidence record. Dispatch 29 downloaded
  wheels and `@types` packages to the scratchpad to size the tables, parsed them without importing
  them, and none is kept. The review surfaced two reds:
  - this branch's `.html` and `.svg` records red the wiring leg;
  - main reads 1,088 offenders against a pin of 1,087, since `8ddc0a482`.

  The design was written, and six questions were put to the owner.
- 2026-10-15, session 1799cb98: the owner settled L-1 to L-6:
  - L-1 to L-4 with the recommended options;
  - L-5 with their own answer, "detected + declared by the owner (custom packs?)": custom packs are
    allowed;
  - L-6 by declaring `html` and `svg` dark, which was committed the same day as `0ac38b016`.

  dMindYourWords joined the chain, four keys joined v2, and seven gaps were registered.
- 2026-10-15, session 1799cb98: the owner opened the runtime layer's review, with no framing. The
  main loop scoped it from the layer model and v2's owed items. Four researchers were dispatched,
  30 to 33.
- 2026-10-15, session 1799cb98: the owner handed Runtime's framing and architecture to the main
  loop, and asked for two medium-effort Tier-2 review rounds afterwards, their results compared.
  All four researchers returned; their returns and probes are saved, and one probe was lost to the
  shared scratchpad. Three returns tripped the harness's `settings-json` notice. One also tripped
  `dangerously-skip-permissions`, because it cites `resume-tick.sh:385`, which the main loop
  verified. The design was written: deciding by `next`, supervising by a process, acting through
  thin bound sessions, and one enforcement surface failing closed.
- 2026-10-15, session 1799cb98: agent-cap's rule 0 refused review run A. The owner was asked,
  verbatim: "agent-cap refused review round A: a pre-code spec audit needs your opt-in where a run
  cannot write it, and this build's README is prompt-authorized, so its own `spec-audit:` key admits
  nothing. The only owner-level opt-in the guard reads is `SPEC_AUDIT_DEFAULT` in `.unattended.conf`,
  honoured for builds whose README declares no key. How should I record your opt-in?"

  The owner chose "Only for these two rounds". That option read: "Set the default in the working
  tree, run both rounds, then restore the file uncommitted; the one-off is recorded in the session
  log. The build's own later audit stays blocked."

  So, in the working tree only:
  - `SPEC_AUDIT_DEFAULT` was set to `2026-10-15`;
  - the README's `spec-audit: 2026-10-14` line was set aside.

  Both rounds then ran: run A as `wf_6508cb22-7d6`, run B as `wf_3c895b43-8da`. Afterwards both files
  were restored to HEAD uncommitted, and `git diff --quiet` checked them clean. The build's own
  declared audit stays blocked by rule 0.
- 2026-10-15, session 1799cb98: both rounds returned CLEAN WITH FIXES:
  - run A: 56 of 60 findings confirmed, 6 of them high;
  - run B: 57 of 61 confirmed, 9 of them high.

  `build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md` places every finding on the defect it names. There are 59 defects:
  - 32 found by both rounds;
  - 14 found by run A only;
  - 13 found by run B only.

  All 59 were folded into the runtime record, and RT-1 to RT-3 went to the owner.

## Instruments

### The gap-ownership join

The check behind acceptance (c), run first against the architecture records and, once the chain
opens, against the chain READMEs. It reads two files and writes nothing:

```python
"""Join the gap register's keys against architecture v1's chain table: every gap owned exactly once,
every chain build owning at least one. Reads both records; writes nothing. Ranges like
`gap-test-01 to gap-test-09` are expanded."""
import re
import sys

reg_path, arch_path = sys.argv[1], sys.argv[2]
with open(reg_path, encoding="utf-8") as fh:
    keys = [m.group(1) for m in re.finditer(r"^\| (gap-[a-z]+-\d\d) \|", fh.read(), flags=re.M)]
with open(arch_path, encoding="utf-8") as fh:
    arch = fh.read()

owners = {}
for line in arch.splitlines():
    m = re.match(r"^\| (d[A-Z][A-Za-z]+) \| [^|]+ \| [^|]+ \| [^|]+ \| (.+) \|$", line)
    if not m:
        continue
    build, cell = m.group(1), m.group(2)
    owned = set()
    for a, b in re.findall(r"(gap-[a-z]+-\d\d) to (gap-[a-z]+-\d\d)", cell):
        stem, lo, hi = a.rsplit("-", 1)[0], int(a.rsplit("-", 1)[1]), int(b.rsplit("-", 1)[1])
        owned |= {f"{stem}-{i:02d}" for i in range(lo, hi + 1)}
    owned |= set(re.findall(r"gap-[a-z]+-\d\d", re.sub(r"gap-[a-z]+-\d\d to gap-[a-z]+-\d\d", "", cell)))
    owners[build] = owned

count = {k: [b for b, s in owners.items() if k in s] for k in keys}
unowned = [k for k, bs in count.items() if not bs]
multi = {k: bs for k, bs in count.items() if len(bs) > 1}
phantom = sorted({g for s in owners.values() for g in s} - set(keys))
empty = [b for b, s in owners.items() if not s]
print(f"register keys {len(keys)} · chain builds {len(owners)}")
print("unowned:", unowned or "none")
print("owned twice or more:", multi or "none")
print("owned but not in the register:", phantom or "none")
print("builds owning nothing:", empty or "none")
sys.exit(1 if (unowned or multi or phantom or empty) else 0)
```

Runs, 2026-10-14:

| Against | Result |
|---|---|
| the register and architecture v1 | exit 0: 57 keys, 10 builds, none unowned, none owned twice, none phantom, none empty |
| the register with `gap-review-03` renamed `gap-review-99`, and v1 | exit 1: `gap-review-99` unowned, `gap-review-03` phantom |
| the register and architecture v2 | exit 0: 57 keys, 10 builds, the same four clean lines |
| the register with `gap-plan-07` renamed `gap-plan-99`, and v2 | exit 1 |

### The preset check

Checks architecture v2's `[presets]` table against its `[policies]` catalogue. It reads one file and
writes nothing:

```python
"""Check architecture v2's preset table against its policy catalogue: every presettable key assigned
in every preset, no excluded key present, every enumerated value allowed, and the `standard` column
equal to the catalogue's defaults. Reads one file; writes nothing; exit 1 on any finding."""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()


def section(tag):
    m = re.search(r"^## \[" + re.escape(tag) + r"\].*?(?=^## \[|\Z)", text, flags=re.M | re.S)
    return m.group(0) if m else ""


def rows(block, ncols):
    out = []
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == ncols and cells[0].startswith("`"):
            out.append([cells[0].strip("`")] + cells[1:])
    return out


STAGES = ["plan", "design", "build", "test", "deploy", "maintain"]
EXCLUDED = {"floor", "policy.guard", "policy.proof", "preset", "charter.practices", "instructions.edit"}
catalogue = {}
for key, allowed, default, _src in rows(section("policies"), 4):
    keys = [key.replace("<stage>", s) for s in STAGES] if key == "review.<stage>" else [key]
    for k in keys:
        if key == "review.<stage>":
            d = "owed" if k == "review.build" else "opt-in"
        else:
            d = default
        catalogue[k] = (allowed, d)

presets = {r[0]: r[1:] for r in rows(section("presets"), 5)}
findings = []
expected = {k for k in catalogue if k not in EXCLUDED}
for k in sorted(expected - set(presets)):
    findings.append(f"presettable key missing from the preset table: {k}")
for k in sorted(set(presets) - expected):
    findings.append(f"preset table names a key that is excluded or not in the catalogue: {k}")

FREE = re.compile(r"hours|days|set of named|each cap|any subset|the role efforts|a repo-declared|a retry count|a share of the window|a round count|a word range")
for k, vals in presets.items():
    if k not in catalogue:
        continue
    allowed_text, default = catalogue[k]
    if not FREE.search(allowed_text):
        allowed = {a.strip() for a in re.split(r"[,;]", allowed_text) if a.strip()}
        for name, v in zip(["velocity", "standard", "strict", "autonomous"], vals):
            if v not in allowed:
                findings.append(f"{k}: {name} = '{v}' is not an allowed value ({allowed_text})")
        if vals[1] != default:
            findings.append(f"{k}: standard = '{vals[1]}' but the catalogue default is '{default}'")

print(f"catalogue keys {len(catalogue)} · presettable {len(expected)} · preset rows {len(presets)}")
print("\n".join(findings) if findings else "no findings")
sys.exit(1 if findings else 0)
```

Runs, 2026-10-14:

| Against | Result |
|---|---|
| v2 as first written | exit 1: `hooks.bypass`'s catalogue default read "allowed, every use recorded", a note fused into the value |
| a copy with strict `leases` set to `sometimes` and standard `build.scope` set to `refuse` | exit 1, naming both planted defects |
| v2 with the catalogue cell corrected to `allowed`, the recording left to the floor | exit 0: 47 catalogue keys, 43 presettable, 43 preset rows, no findings |
| v2 after foundations step 1, with `EXCLUDED` gaining `"charter.practices"` in the source above (presets never touch the practice set) | exit 0: 49 catalogue keys, 44 presettable, 44 preset rows, no findings |

The gap-ownership join after foundations step 1, against the register (61 keys, the four owner-raised
`gap-found-*` rows added) and v2 (dOrderedCharter added as the root): exit 0, 61 keys, 11 builds,
none unowned, none owned twice, none phantom, none empty.

After step 1's continuation (`gap-found-05` owned by dOrderedCharter, `gap-found-06` by
dDeclaredLoop): the join exits 0 on 63 keys and 11 builds; the preset check exits 0 on 49 catalogue
keys, 44 presettable, 44 preset rows.

After the core consistency step (`gap-found-07` and `gap-found-08` owned by dOrderedCharter;
`core.bypass` and `core.exceptions` added to the catalogue and every preset): the join exits 0 on 65
keys and 11 builds; the preset check exits 0 on 51 catalogue keys, 46 presettable, 46 preset rows.
The four chain-row amendments were applied by a script that refused unless each old row matched
exactly once.

After the flow walk's Plan and Design stages (four `gap-flow-*` rows; `design.forks` and
`design.reentry` added; the preset `autonomous` renamed `guarded`, and the preset check's column
names updated to match): the join exits 0 on 69 keys and 11 builds; the preset check exits 0 on 53
catalogue keys, 48 presettable, 48 preset rows. The v2 amendments ran through a script that refused
unless each old text matched exactly once.

After the flow walk's Build, Test, Deploy, Maintain and Review stages and the flow-interactions round
(`gap-flow-05` to `gap-flow-09`; seventeen policies added in all since the Design stage): the join
exits 0 on 74 keys and 11 builds; the preset check exits 0 on 69 catalogue keys, 64 presettable,
64 preset rows.

After the owner's no-foreign-build directive (dLeasedFleet's row removed, its three gaps moved to
dDeclaredLoop): the join exits 0 on 74 keys and 10 builds; with `gap-flow-06` struck from
dDeclaredLoop's row and `gap-conc-01` added to dRankedPlan's in a copy, it exits 1 naming both; the
preset check exits 0 on 69 catalogue keys, 64 presettable, 64 preset rows, unchanged.

After the orientation round (`gap-orient-01` to `gap-orient-10`; eight policies added): the join exits
0 on 84 keys and 10 builds; the preset check exits 0 on 77 catalogue keys, 72 presettable, 72 preset
rows.

After the adopted preservation research (`gap-orient-11` to `gap-orient-13`; `card.snapshot` added): the
join exits 0 on 87 keys and 10 builds; the preset check exits 0 on 78 catalogue keys, 73 presettable,
73 preset rows.

After the roles round (`gap-roles-01` to `gap-roles-08`; four policies added; `dBoundRoles` joins the
chain): the join exits 0 on 95 keys and 11 builds. The preset check's free-value pattern gains `a retry
count`, for `roles.retries`, in the source above; it exits 0 on 82 catalogue keys, 77 presettable, 77
preset rows, and exits 1 on a copy with strict `roles.no-spawn` set to `sometimes` and standard
`prompts.author` set off its default, naming both.

After the flow revisit with roles (eight policies added; units added to six chain rows): the join exits 0
on 95 keys and 11 builds; the preset check exits 0 on 90 catalogue keys, 85 presettable, 85 preset rows.

After the compaction settlement (`gap-orient-14` to dDeclaredLoop and `gap-roles-09` to dBoundRoles;
four policies added; the preset check's free-value pattern gains `a share of the window`, for
`context.threshold`, in the source above), both instruments were run as extracted from this record.
- The join exits 0 on 97 keys and 11 builds. On a copy with `gap-orient-14` struck from dDeclaredLoop's
  row, it exits 1 naming it unowned.
- The preset check exits 0 on 94 catalogue keys, 89 presettable, 89 preset rows. On a copy with
  standard `context.on-full` set to `fresh-at-boundary` and strict `notices.record` set to
  `sometimes`, it exits 1 naming both.

After layers round one, both instruments were run as extracted from this record:
- **The changes:** `gap-found-09` to `gap-found-17` went to dOrderedCharter, dConvergedCharter and
  dCalibratedLens; `instructions.checks` joined every preset; `instructions.edit` joined the catalogue
  and was kept from the presets, so `EXCLUDED` gains `"instructions.edit"` in the source above.
- **The join** exits 0 on 106 keys and 11 builds. On a copy with `gap-found-17` struck from
  dOrderedCharter's row, it exits 1 naming it unowned.
- **The preset check** exits 0 on 96 catalogue keys, 90 presettable, 90 preset rows. On a copy with
  standard `instructions.checks` set to `warn` and strict set to `sometimes`, it exits 1 naming both.

After layers round two, both instruments were run as extracted from this record:
- **The changes:** `gap-flow-10` to `gap-flow-14` went to dDeclaredLoop and dCalibratedLens, and
  `review.breakpoints` and `deps.on-parent-withdrawn` joined the catalogue and every preset.
- **The join** exits 0 on 111 keys and 11 builds. On a copy with `gap-flow-14` struck from
  dDeclaredLoop's row, it exits 1 naming it unowned.
- **The preset check** exits 0 on 98 catalogue keys, 92 presettable, 92 preset rows. On a copy with
  standard `deps.on-parent-withdrawn` set to `adopt-parent-work` and strict set to `sometimes`, it
  exits 1 naming both.

After the step definitions' answers, both instruments were run as extracted from this record:
- **The changes:** `review.design.rounds`, `review.design.round-count`, `review.unverified` and
  `tests.without-cadence` joined the catalogue and every preset. The preset check's free-value
  pattern gains `a round count` in the source above.
- **The preset check** exits 0 on 102 catalogue keys, 96 presettable, 96 preset rows. On a copy with
  standard `review.unverified` set to `block` and strict set to `maybe`, it exits 1 naming both.
- **The join** still exits 0 on 111 keys and 11 builds.

After layers round three registered its gaps, the join was run as extracted from this record:
- **The changes:** `gap-roles-10` to `gap-roles-17` went to dBoundRoles.
- **The join** exits 0 on 119 keys and 11 builds. On a copy with `gap-roles-17` struck from
  dBoundRoles' row, it exits 1 naming it unowned.

After the roles layer's answers, both instruments were run as extracted from this record:
- **The changes:** `roles.trust`, `roles.answered-calls`, `roles.verifier-context` and
  `roles.on-contradiction` joined the catalogue and every preset.
- **The preset check** exits 0 on 106 catalogue keys, 100 presettable, 100 preset rows. On a copy with
  standard `roles.on-contradiction` set to `return` and strict `roles.answered-calls` set to
  `sometimes`, it exits 1 naming both.
- **The join** still exits 0 on 119 keys and 11 builds.

After round four opened, the join was run as extracted from this record:
- **The changes:** `gap-roles-18` went to dBoundRoles.
- **The join** exits 0 on 120 keys and 11 builds. On a copy with `gap-roles-18` struck from
  dBoundRoles' row, it exits 1 naming it unowned.

After the memory layer's answers, both instruments were run as extracted from this record:
- **The changes:**
  - dTotalRecall joined the chain;
  - `gap-mem-01` to `gap-mem-11` and `gap-tool-01` to `gap-tool-06` were registered and owned;
  - eight keys joined the catalogue and every preset;
  - the preset check's free-value pattern gained `a word range`, in the source above.
- **The join** exits 0 on 137 keys and 12 builds. On a copy with `gap-mem-05` struck from
  dTotalRecall's row, it exits 1 naming it unowned.
- **The preset check** exits 0 on 114 catalogue keys, 108 presettable, 108 preset rows. On a copy
  with standard `asks.acceptance` set to `grade` and strict `builds.slug-date` set to `sometimes`,
  it exits 1 naming both.

After the lexicon review's answers, both instruments were run as extracted from this record:
- **The changes:**
  - dMindYourWords joined the chain, taking `gap-mem-10` from dTotalRecall;
  - `gap-lex-01` to `gap-lex-07` were registered and owned;
  - four keys joined the catalogue and every preset.
- **The join** exits 0 on 144 keys and 13 builds. On a copy with `gap-lex-07` struck from
  dMindYourWords' row, it exits 1 naming it unowned.
- **The preset check** exits 0 on 118 catalogue keys, 112 presettable, 112 preset rows. On a copy
  with standard `lexicon.at-commit` set to `warn` and strict `lexicon.drift` set to `always`, it
  exits 1 naming both.
- **The lexicon itself,** after `0ac38b016`, no longer reports the undeclared `html` and `svg`. It
  still exits 1 on 1,088 verb offenders against the pin of 1,087, a red inherited from `8ddc0a482`.

### The foreign-build census

Lists every build slug a design record names that is not a chain build, the chain read from v2's
chain table. It reads one or two files, writes nothing and judges nothing: whether a hit is counted
on is decided by reading it (the coordination record's `[audit]`), and a reliance worded without a
slug is invisible to it.

```python
"""List every build slug a design record names that is not a chain build, with the lines naming it.
The chain is read from the record's own chain table (rows `| dXxx | stage | parents | units | gaps |`)
plus dClosedLoop. Reads one file, writes nothing, judges nothing: whether a hit is counted on or only
cited as evidence is decided by reading it, and the census exits 0 either way."""
import re
import sys

path = sys.argv[1]
chain_src = sys.argv[2] if len(sys.argv) > 2 else path
with open(chain_src, encoding="utf-8") as fh:
    chain = {"dClosedLoop"} | set(re.findall(r"^\| (d[A-Z][A-Za-z]+) \| [^|]+ \| [^|]+ \| [^|]+ \| [^|]+ \|$",
                                              fh.read(), flags=re.M))
with open(path, encoding="utf-8") as fh:
    lines = fh.read().splitlines()
hits = {}
for n, line in enumerate(lines, 1):
    for slug in re.findall(r"\b[abcd][A-Z][a-z]+[A-Z][a-z]+\b", line):
        if slug not in chain:
            hits.setdefault(slug, []).append(n)
print(f"chain builds {len(chain) - 1} (+ dClosedLoop) · foreign slugs {len(hits)}")
for slug in sorted(hits):
    print(f"{slug}: lines {', '.join(str(n) for n in sorted(set(hits[slug])))}")
```

Runs, 2026-10-14:

| Against | Result |
|---|---|
| the six design records, before the directive's changes, chain from v2 | v2: aOrientedCast, dPolishedVitrine; walkthrough: aDeployScout, aOrientedCast, dNarrowedAnchor, dScriptedRepeat; flow: four evidence citations; flow interactions and foundations: none; v1: 24, all in the live-build mapping |
| v2 after the changes, its own chain of ten | dLeasedFleet only in the revision lines, and dPolishedVitrine in the mapping's Plan action |

## Records index

| Record | What it holds |
|---|---|
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md` | The owner's prompt, verbatim; the brief; the owner's confirmation; the route. |
| `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-{1..5}-researcher.md` | The five research handoffs, one stage each. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md` | This log. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-research-{plan,design,build,test,deploy}.md` | The five stage researchers' returns, verbatim. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-research-maintain.md` | The main loop's Maintain research, with every instrument beside its output. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-{routing,cost,trust,determinism}.md` | The four orientation researchers' returns, verbatim, the harness's entity escapes restored. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-research-orientation-preserve.md` | The fifth orientation researcher's return, verbatim: how the build's card is preserved and reaches priority 1, adopted at the owner's request. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-session-model.md` | One build modelled through every step under the `standard` preset, the owner's part in it, and the fourteen holes the model exposed. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-roles.md` | The roles layer: the owner's words, what it must answer, the research dispatched, then the design, forks and answers. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-research-roles-{anatomy,coverage,interactions,priorart}.md` | The four roles researchers' returns, verbatim, the harness's entity escapes restored. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-flow-roles.md` | The flow revisited with roles: the item cycle, each step's role sequence and routes, the record chain, the owner's touchpoints, and the holes as forks. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-inventory.md` | The compaction experiment's inventory of the context before compaction, by segment, and its answer key. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-probes.md` | The compaction experiment's seventy-one probes, questions only, answered blind after the compaction. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-recall.md` | The compaction experiment's blind recall: every probe answered from the context that survived, with its confidence and channel, committed before the key was read. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-compaction-results.md` | The compaction experiment's results: each answer scored and traced, the derived tallies and their instrument, findings, conclusions for unattended builds, and the forks they raise. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-design-overview.md` | The design at `2323a2a23`, a snapshot for the owner: the three layers, the mechanics that hold them together, the chain and what is open, each section pointing at its owning record. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-design-overview-{layers.svg,cycle.html}` | The two diagrams shown with that overview: the three layers, and the item cycle as a stepper. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md` | The layer review's first round: the owner's layer model and the instruction layer, measured against the current design, with the gaps, the recommendations and the forks. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-model.svg` | The layer model as capabilities: the core cycle on Runtime, expansions plugged in at declared points, Distribution beneath. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-flow.md` | The layer review's second round: the flow layer, each step at a glance, the owner's requirements against the design, the gaps, the recommendations and the forks. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-research-flow-items-{a,b}.md` | The flow layer's item audit, verbatim: every item of the 70 declared (tag, actor, witness, inputs by layer, instruction scope, routes, dependencies), with each step's extension points and the findings. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md` | The flow's steps defined item by item: Entry, the five core steps and the breakpoint, each with its actors, witnesses, routes and layer ingredients, with the audit's fixes applied. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md` | The layer review's third round: the roles layer set against the settled roles, orientation and flow designs, what role agents receive and re-derive measured over 171 transcripts, the trust mechanism proposed, the role-by-step matrix derived, eight gaps and four forks, with the instruments. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md` | The layer review's fourth round: the memory layer, the owner's words, what the design already fixes, the five researchers' returns measured, the design proposed, and the forks asked. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-{builds,asks-decisions,map-reuse,annotations,tooling}.md` | The memory layer's five researcher returns, verbatim: builds; the ask register and the decision index; the codebase map and the reuse tools; code annotations, the gotchas and the lexicon; the tooling map. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-lexicon.md` | The lexicon kit's review: the owner's words, what the design already fixes, the kit's history, the three researchers' findings, the design (classes, forced names, packs, enforcement, drift, vocabulary, integration) and the forks. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-{kit,population,prior-art}.md` | The lexicon review's three researcher returns, verbatim. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md` | The layer review's fifth round: the runtime layer, what earlier rounds fix for it, its four researchers, the design the owner delegated, two Tier-2 rounds folded into it, and the questions. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md` | The two Tier-2 rounds compared defect by defect: their args, the numbers, what one round alone would have missed, the map from every finding to its defect and fold, and the instrument. |
| `reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-{a,b}.md` | The two Tier-2 reports on the runtime design, as their synthesizers wrote them. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-{executor,spawn,hooks,sessions}.md` | The runtime round's four researcher returns, verbatim. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-instruments.md` | The runtime researchers' probe scripts, as fenced text, with the one lost probe noted. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-research-lexicon-instruments.md` | The lexicon researchers' probe files, as fenced text. |
| `build/2026-10-15-build-PLAY-dClosedLoop-1-research-memory-instruments.md` | The memory researchers' probe scripts, gathered from their scratch paths as fenced text. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md` | The gaps, keyed, graded and evidenced, each owned by one chain build; the register derives its counts. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v0.md` | The first proposal, before the owner's rounds, unedited. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-design-rounds.md` | Rounds 1 to 5: every question, option and answer verbatim, and what each changed. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v1.md` | The design after rounds 1 to 4, unedited. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-walkthrough.md` | The ten chain builds' designs as presented, each fork and answer, and each revision. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md` | The converged design, amended in place under dated `Revised:` lines: principles, the policy catalogue and presets, the chain's rosters. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-foundations.md` | The owner's foundations revisit, step by step: their words, the measured current state, the response, the forks and answers. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md` | The flow walk, stage by stage: the layers, each stage's scope, boundaries and checklist, the forks and answers. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md` | Each step's scope, the eighteen interaction edges, the shared state, and the six interactions settled after. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md` | The owner's no-foreign-build directive, the census of what the design counted on, and leases, the mailbox and dependency coordination designed into dDeclaredLoop. |
| `build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md` | The owner's questions on how sessions and agents enter, orient, resume and progress along the flow; the research dispatched; then the current state, the design and the forks. |
