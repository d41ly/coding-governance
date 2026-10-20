# PLAY-dClosedLoop-1: the architecture and the chain plan for gov's one lifecycle loop

**Status:** INPROGRESS · rev-1 · 2026-10-20 · node d · Tier-2 · base 742957fc · streams playbook+kickoff+tooling+deployer

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Agree with the owner on the architecture that puts every part of gov under one lifecycle loop. Record every gap
between today's product and that architecture, and plan the ordered chain of builds that converges the product onto
it. The kickoff record owns the goal (`memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:32-38`).
The unit is design only, and its product is records under `memory/`, never product code
(`memory/builds/dClosedLoop/README.md:39-40`).

## 2. Scope (IN)

The kickoff's three items (`memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:40-45`)
and the execution plan's Phase 0 make up the unit.

- **S1** — What exists, how its parts interact, and the gaps per stage, recorded as the stage research and the gap
  register (kickoff item 1). Observed by AC3.
- **S2** — The converged architecture, defined with the owner by questions, suggestions and iteration, audited, and
  frozen at its baseline (kickoff item 2). Observed by AC1, AC4 and AC5.
- **S3** — The chain: its builds and rosters in the architecture, and the plan for building them under today's gov
  across nodes a, b and d (kickoff item 3, and the owner's execution question in the execution record's
  `[question]`). Observed by AC2 and AC3.
- **S4** — Phase 0, the unit's remaining work: P0.1 to P0.9 of the execution plan, ending in one landing the owner
  asks for. Observed by AC6, AC7, AC8, AC9, AC10, AC11 and AC12.

## 3. Non-goals (OUT)

The kickoff record's Non-goals own the cut-line
(`memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:63-70`). The build README's
build-level rules extend it (`memory/builds/dClosedLoop/README.md:37-51`). Phase 0 keeps it, because every file
Phase 0 writes is a record under `memory/`
(`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:126-130`).

This spec restates no design fact. Section 4 names the record that owns each one.

### Edges

- **consumes-from** external — today's gov, under which the chain is planned and Phase 0 runs: the unattended
  driver, the build index generator, the roles kit's handoffs and the tier-2 harness. The execution plan's
  `[constraints]` table names what each one forces, and without them the plan's steps rest on nothing.
- **hands-off** external — every build of the architecture's chain table. Phase 0's opening, P0.5, opens each one
  with a README and a planned unit roster, and each build's own runs write its specs, never this unit.
- **hands-off** external — Phase 1, dTrueNorth's whole run on node a, which starts only after the opening lands, as
  the execution plan's `[phase-1]` section says.

## 4. Design

### Where the design lives

Each question below has one owning record. This spec points at it and never answers it a second time.

| Question | Owning record and section |
|---|---|
| What the converged architecture is | architecture v2, whole, from `[layers]` (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:805`) on |
| Which builds form the chain, with their parents, rosters and owned gaps | v2 `[chain]` (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1760`) |
| How a clause is identified and pinned, and which commit froze the design | v2 `[clause-ids]` (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1794`), its `Baseline:` line at `:1809` |
| Which clauses enforce each principle | v2 `[enforcement]` (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1813`) |
| What v2 left to confirm or owed | v2 `[open]` (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1915`) and `[owed]` (`:1955`) |
| Every gap, its evidence and its owning build | the gap register, `## Register` (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:67`), and its ownership rule (`:5-12`) |
| How the design was audited, folded and frozen | the whole-design audit, `[plan]` (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md:20`) through `[baseline]` (`:575`) |
| What the declared spec audit found and how each item was folded | its report, `memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md`, and the fold record's `[fold]` (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md:45`) |
| How the chain is built under today's gov, and the owner's answers on it | the execution record, `[question]` to `[handoff]` (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md:9`), and the execution plan, `[answer]` (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:32`) to `[disagreements]` |
| What the unit still has to do | the execution plan's `[phase-0]` (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:126`), and the handoff that hands it to a new session (`memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-59-session.md:68-91`) |
| What happened, in order | the session log's `## Dispatches` (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:58`) and `## Events` (`:1970`) |
| What the owner asked for, verbatim | the kickoff record's `## The prompt` (`memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:8`) |

### Rollout

The execution plan's "The plan in brief" owns the order: Phase 0 on node d, then Phase 1, then Phase 2 across the
chain (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:83`). Its `[owner]`
section owns the owner's steps (`:1229`), and its `[cannot]` section owns what today's gov cannot do (`:1247`).

### Alternatives rejected

- Restating v2 or the execution plan here. Two copies of one design make two answers to one question, so this spec
  points instead (the unit spec brief's `[settle]`, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-unit-spec-brief.md`).

## 5. Production-readiness checklist

- security — N/A for this spec: the unit adds no write path, surface or credential, since it writes records only
  (`memory/builds/dClosedLoop/README.md:39-40`). The grant and the governance-carrier list that Phase 0 records are
  the execution plan's P0.8 rows 2 and 9.
- perf / scale — the atlas page measured past its size limit, and the records leave the remedy to the owner (F2).
- error / empty / loading states — N/A: the unit ships no product surface.
- observability — the session log records each dispatch and event
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:58`, `:1970`).
- risks — the execution plan's "bad news first" (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:34-81`)
  and its `[cannot]` section (`:1247`).
- testing — every instrument is seen red on a plant before it is trusted, as the audit's plan
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md:27-29`) and P0.1 require.
- migration — N/A: the unit changes no data; each migration the design needs is a chain build's unit.
- user docs — N/A: no user-facing change, so no page under `help/` moves.

## 6. Acceptance criteria

The kickoff's acceptance check, (a) to (d), is criteria AC1 to AC4. The baseline taken is AC5, and Phase 0's
acceptance as the execution plan states it is AC6 to AC12. Each criterion cites the record that shows it DONE or
OPEN. Every probe named below ran at `72b65c083` on 2026-10-20.

- **AC1** — When `tools/memory-recall/query.py` is asked for the owner's ratified answers, it returns each one as a
  row of `memory/DECISIONS.md` (kickoff (a),
  `memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:49`).
  Red when: an answer the build's records quote verbatim has no decision row.
  OPEN. `grep -n dClosedLoop memory/DECISIONS.md` prints nothing (PINNED, at `72b65c083`). P0.8 mints nine rows for
  the execution answers (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:541-599`).
  Whether the design rounds' answers owe rows too is F3.
- **AC2** — When `memory/LIVE.md` is regenerated after the opening, it lists every chain build as non-terminal, and
  each chain README names its stage and its predecessor (kickoff (b),
  `memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:50-51`).
  Red when: a build of v2's `[chain]` is missing from `memory/LIVE.md`, or its README carries no stage in its H1 or
  no `parents:` line.
  OPEN, owed by P0.5, which writes each README's stage H1 and its `parents:` line
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:340-346`). No chain
  build's folder exists yet.
- **AC3** — When `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-gap-join.py` joins the gap
  register against the chain, every gap is owned by exactly one build and every build owns at least one, after the
  join is seen red on a planted orphan row (kickoff (c),
  `memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:52-53`).
  Red when: a planted orphan row exits 0.
  DONE against v2's `[chain]`: exit 1 on two planted orphans, and exit 0 on the register and v2
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:3336-3339`), and rc 0 on the
  folded tree (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md:535`). OPEN
  against the chain READMEs, which do not exist yet, and no P0.7 check runs the join over them (F4).
- **AC4** — When the declared spec audit's report is read, it sits under `memory/builds/dClosedLoop/reviews/`, and
  every finding is folded or rejected with its reason (kickoff (d),
  `memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:54-55`).
  Red when: an item of the report has no row in the fold.
  DONE. The report is `memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md`, and
  the fold's `[fold]` table takes each item
  (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md:45`), as the session log
  records (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:2772-2774`).
- **AC5** — When `grep -n '^Baseline:' memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
  runs, it prints the commit the whole-design audit's `[baseline]` names, and that commit resolves.
  Red when: the two records name different commits, or v2 carries a `Revised:` paragraph written after the baseline.
  DONE (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1809`;
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md:579`).
- **AC6** — When `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py`,
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py` and
  `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py` run their plants and run on the
  tree, each exits as P0.1's acceptance states
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:162-165`).
  Red when: a P0.1 plant exits other than as its row says.
  OPEN. The deviations instrument carries no `--policy` arm yet (PINNED, a grep at `72b65c083`).
- **AC7** — When the departures report's `--fixture` runs, it lists each population plant P0.2's acceptance names
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:226`).
  Red when: one of P0.2's red tests stays green.
  OPEN. The deviations instrument carries no `--report` mode yet (PINNED, a grep at `72b65c083`).
- **AC8** — When the packet instrument renders dTrueNorth's packet, the result is what P0.3's acceptance states, and
  `tools/roles/handoff.py` renders and checks it green
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:286-291`).
  Red when: the rendered packet differs from the worked example P0.3 cites.
  OPEN. No packet instrument exists under the build folder (PINNED, at `72b65c083`).
- **AC9** — When `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py` is re-run on the
  plants of P0.4's red-test table, each result matches its row
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:299-325`).
  Red when: a plant's output differs from its row.
  OPEN. The plan observed them on 2026-10-20 and owes a re-run before the landing (`:308-309`).
- **AC10** — When the opening is committed, every check and red test of P0.7 gives the result its row states,
  P0.6's bare-id predicate printing nothing among them
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:530-539`).
  Red when: a P0.7 red test stays green.
  OPEN. The opening is not written.
- **AC11** — When each of P0.8's decision rows in `memory/DECISIONS.md` is read, it quotes its answer from the
  execution record or names the `[defaults]` item it carries
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:598-599`).
  Red when: a row quotes no answer.
  OPEN. No row exists yet, as AC1 measures.
- **AC12** — When P0.9's steps have run on a node, its four acceptance observations hold there
  (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:615-622`).
  Red when: `tools/check-wiring.sh` in check mode still reports the unset merge driver.
  OPEN on every node. Node d did not find the resume tick (`:610`).

## 7. Gates

The legs the kickoff named for each pass on the staged tree
(`memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:57-61`), as `tools/gate-legs.json`
names them:

`kickoff-manifest ratchet` · `memory hygiene` · `build README slot contract`

The kickoff also names the runner's stale-generated-output check, which is a runner mode and no leg, and the full
bar before any landing. P0.7 owns the opening's own checks and its one landing.

## 8. Open questions

- **F1 — Phase 0 is the unit's remaining work, and none of it has run. How does the unit finish?**
  - Option (a): run Phase 0 in the plan's order from the handoff, stop at the owner's opening read, and land on the
    owner's ask (`memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-59-session.md:68-91`).
  - The records hold no other option.
  - Recommendation: (a), as the owner approved it
    (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:3275`).
- **F2 — The Closed Loop Atlas measured 16.4 MB with the execution records, past its 16 MB limit, so it was not
  republished. Does it skip the execution records, or split?**
  - The figure is PINNED, measured on 2026-10-20
    (`memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-59-session.md:116-119`). The opening's
    READMEs add to it.
  - Option (a): the atlas skips the execution records. Option (b): the atlas is split.
  - Recommendation: put both to the owner, as the handoff directs. The records weigh neither.
- **F3 — Kickoff (a) asks for the owner's ratified answers as decision rows. P0.8 mints rows for the execution
  answers only. Are the design rounds' answers owed rows too?**
  - Option (a): P0.8's rows answer (a) for the execution, and the design answers stay in the build records that
    quote them verbatim, recorded as a departure from (a).
  - Option (b): Phase 0 also mints rows for the design rounds' ratified answers.
  - Recommendation: raise it with the owner at the opening read, since the plan's decided answers stand and a gap in
    them is raised, never fixed silently
    (`memory/builds/dClosedLoop/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-59-session.md:120-121`).
- **F4 — Kickoff (c) joins the gap register against the chain READMEs. The join reads v2's `[chain]` table, and no
  P0.7 check runs it over the opened READMEs. Is it owed there?**
  - Option (a): add the join over the opened READMEs to P0.7's checks.
  - Option (b): take the join over v2 as the witness, since P0.5 derives each README's problem slot from the build's
    owned gaps (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:347`).
  - Recommendation: raise it with the owner at the opening read, for the reason F3 gives.
- **F5 — The kickoff record's route names this unit's spec at a 2026-10-14 path that was never written, while this
  spec is dated 2026-10-20. Is the route re-appended?**
  - The route is at `memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:104-107`.
  - Option (a): re-append the card's route naming this spec, as the route's own comment says to when its set
    changes (`:103`).
  - Option (b): leave the route as written.
  - Recommendation: (a), the route's own procedure, run by the main loop.

## 9. Revision log

- rev-1 · 2026-10-20 · initial draft, written at the landing. Hygiene check 21 binds a record's Serves id only to a
  spec H1, and the unit's design had lived in its build records.

## 10. Reuse audit

The unit builds no mechanism. It extends the seams its kickoff named
(`memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:80-85`), and Phase 0 extends the
same ones. `tools/codebase-map/reuse_lookup.py` ran at `72b65c083` on three phrases: "open a build folder and render
the live builds index", "scaffold a new build README and fill its generated regions" and "render a role agent handoff
prompt". Each exited 0. Across the three, its output names every seam in the table below, the gate-legs manifest as
its `gate-legs` inventory, except the Deploy research spec, which the kickoff's card names instead
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:35`). The third phrase names
`tools/roles/handoff.py` and `tools/workflows/tier2-review.js` among its candidates, and the first two name
`tools/memory-tree/gen_build_index.py` as an affordance seam.

| Seam | What the unit took from it | Where the records show it |
|---|---|---|
| `memory/map/` and `tools/gate-legs.json` | the derived inventory of what ships | the kickoff's card (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:35`) |
| `tools/drift-audit/drift_report.py` | the gap evidence for Maintain | the Maintain research (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-research-maintain.md:12`) |
| `memory/builds/aDeployScout/spec/governance-deployer-research.md` | the Deploy stage's design origin | the Deploy research (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-research-deploy.md:31`) |
| `memory/guides/BUILD-METHOD.md` | the Build stage, and the method the plan cites | the plan's conventions (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:26-27`) |
| `tools/memory-tree/gen_build_index.py` | the build folder opened and registered, and the opening's heading canon | the Events (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:1974-1976`); P0.5 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:335-338`) |
| `tools/roles/handoff.py` | every role dispatch, rendered as a handoff | the Phase 0 handoff's render (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md:561-564`) |
| `tools/workflows/tier2-review.js` | the declared spec audit and every review pair | dispatch 98 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-log.md:162`) |

Recall terms used: charter template kit govkit deployer bar legs build-method unattended roles kickoff spec
lifecycle, the kickoff's own
(`memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md:85-87`).
