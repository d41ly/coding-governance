# Research: the runtime layer, the executor and next

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 30's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-11-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`.

---

## Inventory

| Driver | Host | Who advances each step | file:line |
|---|---|---|---|
| `unattended.sh`: 24 slug verbs and 6 inline verbs | bash | **Code** checks every transition: phase vocabulary, terminal, HELD and LANDING guards, witness required (`verb_phase` 5998-6067), the DoD at `--close` (fail 13 at 10785/10797), the resume/take-over matrix (`run_takeover` 8856, `verb_resume` 9008), and dispatch order and readiness (13447+). **A model decides when to call each verb** and with which arguments. | 107, 114, 14303-14328 |
| Phases | code constant | `PREFLIGHT RESEARCHING TESTING SPECCING REVIEWING FOLDING BUILDING RUNNING HELD VERIFYING LANDING LANDED ABORTED`. A **model** picks the non-terminal moves. Only producers write the terminal ones (`--close`, `--landed`, `--abort`). | 852 |
| `next:` ladder | code | A pure function of 4 inputs (`NEXT_RUNGS` 5745-5751, `derive_next_shape` 5762-5783), fed by `verb_plan` (5785), which grades tracked specs. | — |
| `/unattended` Skill | model session | A router. The **model** picks the path, schedules the cron keepalive, and decides park, rescope, hold, handoff, abort and override. | `.claude/skills/unattended/SKILL.md:14-192` |
| `/build` Skill (attended) | model session | The stage-5 loop is **model**-run: flip the status to INPROGRESS, append the route, dispatch, and branch on `diverged`. | `.claude/skills/build/SKILL.md:59-72` |
| `unattended-build.js` | Workflow program | **Code** sequences Spec (934), Audit (1308) and Disposal (1976), and spawns 8 `agent()` sites. It hands back a prose `nextAction` (1938, 2401, 2501) for the **model** to act on. | — |
| `unattended-unit.js` | Workflow program | One unit and one agent (333). **Code** derives `diverged` from the `why` prefix (348). | 224-348 |
| `tier2-review.js` | Workflow program | **Code** runs the phases Resume (934), Find (1103), Verify (1277) and Synthesize (1649). It returns `exit:'deferred-platform'` when an agent dies (1243, 1630). | — |
| `drift-audit-{code,state}.js` | Workflow program | **Code** runs Find, Verify and Synthesize, with agents per lens. | code.js:270, 343, 443 |
| `workflows.toml` | declaration | Ten workflows, each with a `driver` of agent, workflow, program or main-loop. orient and bookkeeping are `main-loop`, which means a model. | 1-105 |

**Constraint that decides the shapes.** The Workflow runtime injects only `args agent parallel pipeline phase log budget workflow` (`tools/workflows/check-workflow-syntax.js:41`). It has no shell. Every `exec(` in the harnesses is a RegExp call (`unattended-build.js:671,688,1050`). So whenever a harness needs a driver verb, it **spawns an agent to run it**: "Run exactly: … --review … Return the CONVERGENCE token" (`unattended-build.js:1805-1823`).

**Where a record and the code disagree:**
- `.claude/rules/product.md` calls this "the four-verb driver". The code has 30 verbs (`unattended.sh:107,114`).
- `/build` claims spec-review is "identical" across the two modes (`build/SKILL.md:96-98`). The code differs: attended mode computes the token itself and only ever produces CONVERGED or CONVERGING (`unattended-build.js:1805-1806`).

## Sequence

An unattended main session works through these steps, as the transcripts and the verbs guide show:

1. CronCreate keepalive (SKILL:16).
2. `--preflight`, then `/session-kickoff`.
3. `--plan --paths` → a `unattended-build.js` call, which hands back a roster and a prose `nextAction`.
4. Per unit: `--brief`, `--dispatch`, a `unattended-unit.js` call, the commit, then `gotchas.py --for-diff`, then re-read `--plan` and branch on the shape (VERBS.md:753-764).
5. `--phase VERIFYING`, then `--close` (DoD), the lander, `--landed`.

**The judgments the model makes** (journal counts, 2026-09-13 to 2026-10-14): `--rescope` 71, `--park` 12, `--hold` 6, `--handoff` 5, `--phase` 46 (which phase to move to), `--attest` 22. On top of these, it writes its own drivers. Session b710e9c3 issued 17 inline `Workflow{script}` calls (`gated-prose-fold-2…5`, `gated-prose-disposal`, `dloggedflight-closing-fold`, …) next to its 32 `unattended-unit.js` calls. Session 2588f719 used 25+ ad-hoc scripts (`wave.js`×10, `merge-main.js`, `repair-merge2.js`, `promote-g8.js`, …).

**Recovery:**
- **After a compaction**, the protocol says re-read `--status` first (VERBS.md:822). In practice, 1 of 20 compactions called `--status`, `--resume` or `--plan` within the next 10 tool calls. The other 19 resumed from the summary.
- **After a process death**, the protocol path is the take-over matrix (`run_takeover` 8856). The journal shows only 11 `--resume` calls across 18 slugs.

## Measurements

**M1. Unattended main sessions** (30 transcripts contain `--preflight`; main thread only):

```
$ python3 scratchpad/tx.py   # excerpt
start sess slug tot bash read edit agent wf disp drvcalls compacts errs
2026-09-12 b710e9c3 dLoggedFlight     1092  793 72 128 3 64 0  52 3 13
2026-09-12 2588f719 dAligned+dDerived 1852 1380 86 216 3 94 1 124 4 19
2026-10-04 564117a5 dUnstuckLanding    438  348 17  40 7 14 0  47 0  5
2026-10-05 f0ae2e44 dThriftyLanding    360  307  6  37 1  4 17 50 0  5
2026-10-09 ffd5c89b dHomedResolver     366  317  5  28 0  1 6  39 0  6
2026-10-11 72a45fd5 dRemeasuredRender  358  298  5  39 0  1 10 45 0 12
2026-10-13 b5b52897 dSweptBranches     794  579 12 180 0  3 18 82 1 15
```

Units come from the journal's distinct successful `--dispatch` per slug.

| Session | Tool calls | Units | Calls per unit |
|---|---|---|---|
| dLoggedFlight | 1092 | 25 | 44 |
| dUnstuckLanding | 438 | 10 | 44 |
| dThriftyLanding | 360 | 11 | 33 |
| dSweptBranches | 794 | 21 | 38 |
| dHomedResolver | 366 | 5 | 73 |
| dRemeasuredRender | 358 | 5 | 72 |
| 2588f719 (3 builds) | 1852 | 28 | 66 |

The median is about 44 main-session calls per unit, and about 75% of all calls are Bash. All 21 compactions were automatic, at `preTokens` 914,072 to 1,001,711.

**M2. Driver journal** (`.git/runlog/driver.log`, 1,964 lines):

```
$ grep ev=end driver.log | grep -o 'exit=[^\t]*' | sort | uniq -c
    974 exit=clean
      7 exit=unclean
start without end: 2
nonzero rc by verb+check: 26 --dispatch/49, 11 --review/37, 11 --close/13,
  10 --dispatch/14, 5 --check-commit/49, 2 --close/62, ...
```

Check 49 is the dispatch preconditions: out of order, MISSING, THIN, a bad write path (13447+). Check 37 is a malformed `--review` argument (12541-12559). Check 14 is an unknown argument (14296). That makes 47 refusals of transitions the model issued wrongly. The 7 unclean exits are `--status`, `--resume`, `--close` and `--phase` killed mid-verb.

**M3. Cost of a position read:**

```
$ time bash tools/unattended/unattended.sh --plan aClosedDocket   → real 0m1.041s
$ … aHeardState → 1.077s · aBatchedArm → 1.133s
```

## Gaps

**[position]** The determinism test below passed. The other answers diverge:

```
$ for s in aTunedCompass dLandedVerdict aTetheredScratch; do a=$(--plan $s|tail -4); b=$(--plan $s|tail -4); [ "$a" = "$b" ] && echo identical; done
next: TOOL-aTunedCompass-9 (READY - build it)      [two runs byte-identical]
next: TOOL-dLandedVerdict-1 (READY - build it)     [two runs byte-identical]
next: TOOL-aTetheredScratch-1 (FORKED)             [two runs byte-identical]
```

| Divergence | Evidence |
|---|---|
| With `.unattended.conf` absent, the attended path has **no** position answer: the driver exits 2. | 549-550 |
| `--plan` grades ask rows at the run's pinned `m-base` when RUN.md exists, and at HEAD otherwise. Attended and unattended can therefore grade different trees. | 5613-5616 |
| `--status` "next" is the first README row that is not CLOSED or WONTDO, with no READY, THIN or FORKED grade and no order verb. `--plan` grades specs and the order. For aTetheredScratch, `--status` would name unit 1 bare, while `--plan` says FORKED (do not dispatch). | 4815, 8072 vs 5785 |
| Run phase and spec position contradict each other. aTunedCompass is `phase: LANDED`, but `--plan` says `next: TOOL-aTunedCompass-9 (READY)`. aClosedDocket is `BUILDING`, but `--plan` says everything is terminal. | RUN.md and the run above |
| Attended review convergence is computed from the blocker count, so it never reaches NON-CONVERGENT, BOUNDED or CEILING. | unattended-build.js:1805-1806 |
| The harness hands its position back as prose (`nextAction`) for a model to act on. | 1938, 2401, 2501 |
| No `next` CLI exists. `handoff.py`'s verbs are render, harness-args, stage-efforts, check, roster and agents. | handoff.py:931-947 |

**[outcomes]** 98 run records: 89 `RUN.md` plus 9 archived `RUN.<PHASE>.<sha>.md`.

| Outcome | Count | Causes and examples |
|---|---|---|
| Landed | 75 (57 LANDED, 18 LANDING) | A LANDING record on the remote tip derives LANDED by protocol (`UNATTENDED-STOPS.md:477`). All 18 LANDING witnesses are in `origin/main`. |
| Aborted | 13 | gate-red-out-of-scope 4 (aMeteredTurnstile: "merge bar RED on this host for an environmental reason"). scope-approval-needed 3 (dScriptedRepeat: "added … without the owner ruling … I am the one who skipped it"). fork-unresolvable 3 (dClosedLexicon: "did not converge across three adversarial rounds"). repo-state-out-of-mandate 3 (dTieredTribunal: "ABANDONED … record untouched … no process on the node named it"). |
| Parked (HELD) | 8 | owner-decision 5, host-owner-action 2, host-degraded 1 |
| Stalled or died | 2 | aClosedDocket and aUnblockedFleet sit at BUILDING. `--plan` says every spec is terminal, and their last rows are dated 2026-08-31 and 2026-09-01. Neither was ever closed. |

## Candidates

**A. A deterministic program as a CLI (bash or python) over the loop declaration.** It calls a model only for role items and judgment items.
- **Losing test (the build must run it):** spawn one role item from the CLI. Then assert that the item's SubagentStart and SubagentStop hooks fire and that `agent_type` is present in the hook payload.
- **Result:** not runnable read-only. On the code: a CLI's only route to a model is a separate session (`roles.no-spawn`), not a subagent. RL-8 asks for a harness that can always spawn subagents. **A loses as the primary executor, pending that test.** It survives as the no-spawn fallback.

**B. A model-driven session following a checklist (today's shape).**
- **Losing test (pass bar defined before running):** after compaction the session re-derives its position from witnessed state, and it issues no transition that the driver refuses.
- **Result: lost.**
  - 19 of 20 compactions resumed from the summary (M1).
  - The driver refused 47 malformed or out-of-order transitions (M2).
  - Sessions improvised drivers outside the shipped harnesses: 17 inline workflows in one session.
  - 2 runs were left at BUILDING with all work terminal.

**C. A Workflow program as the executor** (one long Workflow script runs the whole loop; RL-8's "built-in harness" taken literally).
- **Losing test:** the program can read witnessed state itself, without a model in between.
- **Result: lost.** The runtime has no shell (`check-workflow-syntax.js:41`). The shipped harness already pays a model call to relay a one-line CLI token (`unattended-build.js:1805-1823`). A death in the agent fan already needs a `deferred-platform` exit (tier2-review.js:1243, 1630; unattended-build.js:1667). Judgment items still return to a session (`nextAction`).

**D. Hybrid.** A deterministic `next` (a pure function of witnessed state) chooses every item. A thin session loop executes: it calls `next` before each act, runs role items through the harness one item per call (the `unattended-unit.js` shape), and handles judgment items as declared items with a return schema. A tool-boundary hook refuses any spawn or phase move that differs from `next`'s answer.

| Losing test | Result |
|---|---|
| (i) `next` is byte-stable on a fixed tree | **Passed** (M3, 3 builds × 2 runs) |
| (ii) The same folder gives the same answer attended and unattended, conf absent | **Fails today** (the Gaps table). The repair is to merge the derivations, not to reject D. |
| (iii) Hook cost: one position read per spawn | **Passed.** About 1.05 s per read, about 181 dispatches a month, so about 3 minutes in total. |
| (iv) Every main-session act in the 9 journaled builds maps to a declared item: park, rescope, hold, handoff, abort, attest, review, or a dispatch/phase move that `next` named | **Owed by the build.** It replays each act in `driver.log` against the declared loop. More than 5% of acts falling outside a declared item makes D lose. The improvised inline workflows are the likely failures. |

## Pick

**I recommend D.** It extends the seam that already exists: `NEXT_RUNGS` and `derive_next_shape` (5745-5783) become `next`. The build should make these changes:
1. Widen `next`'s inputs from spec grades alone to witnessed run state: the phase and its witness (`read_derived_phase` 1439), review rounds, and holds.
2. Retire the second derivation in `--status` (8072).
3. Make the m-base choice explicit, so both modes grade the same tree.
4. Replace the harness's prose `nextAction` with a `next` re-read.

D's open risk is test (iv), which the build must run first. C is rejected by its shell test. B is rejected by its compaction and refusal test. A stays the no-spawn fallback, pending its hook test.

Scripts, all in the scratchpad: `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\tx.py`, `cmp.py` and `cmp2.py`.
