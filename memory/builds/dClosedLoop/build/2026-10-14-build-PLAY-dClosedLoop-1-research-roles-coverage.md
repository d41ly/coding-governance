# Research: role coverage — every step's checklist items against today's roles, and role work done outside a role

**Serves:** research PLAY-dClosedLoop-1

The gov-researcher's return for handoff `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-12-researcher.md`
(dispatch 17), verbatim.

---

# Role coverage of the DLG step checklists (researcher return, PLAY-dClosedLoop-1)

## 1. Inventory

- **Step checklists:** 70 items in all: Plan 11, Design 10, Build 10, Test 8, Deploy 10, Maintain 9, stage review 7, Loop Review 5. Source: `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow.md:77,226,359,441,511,583,666`.
- **Role catalogue:** 10 roles under `tools/roles/agents/`. 9 are agents. `gov-session` is `agent: false` (`.claude/roles.json`).
- **Workflows:** `tools/roles/workflows.toml:14-99` defines 10 workflows. `gate-bar` and `handoff` are programs, and `bookkeeping` is run by the main loop with no role.
- **Role arm:** `tools/hooks/scratch-guard.js:91-103`. It refuses writes to `spec/` and to product paths unless the writer's `agent_type` declares that write class.
- **Harness role binding:** `tools/workflows/tier2-review.js:230-245` and `unattended-build.js:538`.
- **Write classes:** `tools/roles/check_roles.py:94` defines `none spec product review records`.

## 2. Sequence

- The main loop starts a harness through Workflow or Agent. The harness gives each stage the role named in its `roles` map. **STATED:** a role key is optional ("leave the key out for an untyped stage", `tier2-review.js:238`).
- A spec or product write from the wrong writer is refused. **ENFORCED** by `scratch-guard.js:1057-1085`, but only for the Write, Edit and MultiEdit tools.
- **STATED only, nothing reads them:**
  - Writes of the `review` and `records` classes (`scratch-guard.js:102-103`).
  - Bash writes.
  - Any tree whose role index is absent: "An ABSENT index adds no arm" (`:99`).
- Who orients, who scouts for reuse, and who performs a role function inline is **STATED** (`mandatory: no — the main loop may orient itself`, `gov-orienter.agent.md:12`).
- The research workflow lists `enforced-by = agent-cap.js spawn guard` (`workflows.toml:86`). In the window, 74 general-purpose and 18 Plan agents were spawned beside 19 researchers, so the guard does not route research to the role. **Record and code disagree here.**
- `gov-builder.agent.md:17` says "gates are the main session's". The settled design gives gates to Test. **Record and settled design disagree here.**

**The 70 items, by who performs each today:**

| Step | Role | Main session | Command | Nobody |
|---|---|---|---|---|
| Plan | 0 | 1, 2, 4, 5, 6, 10 | 0 | 3, 7, 8, 9, 11 |
| Design | 2 (scout unused; spec-writer runs M5), 4, 5 (spec-writer), 8 (audit roles) | 1, 3, 6 | 9 (`plan_state`) | 7, 10 |
| Build | 3, 4, 5 (builder), 8 (review roles) | 1 | 6 (harness divergence), 7 (`routed_commits`) | 2, 9, 10 |
| Test | 0 | 4 (sending reds back) | 1, 2, 3 (bar) | 5, 6, 7, 8 |
| Deploy | 0 | 2, 5 | 1, 3 (`push-main.sh`) | 4, 6, 7, 8, 9, 10 |
| Maintain | 0 | 2, 4, 5 (by hand) | 0 | 1, 3, 6, 7, 8, 9 |
| Stage review | 3, 4, 5 | 1, 6 (folding findings) | 2 | 7 |
| Loop Review | 0 | 0 | 0 | 1–5 |
| **Total** | **11** | **18** | **9** | **32** |

**The owner's functions, and the role that holds each today:**

| Function | Role today | Matches? |
|---|---|---|
| Session orientation | gov-orienter | Yes, but 0 spawns. Under the settled design `next` does this, so it becomes a command. |
| Research | gov-researcher | Yes |
| Planning | none | Untyped Plan agents (18) |
| Reuse discovery | gov-reuse-scout | 0 spawns, and its body "adds nothing" (`gov-reuse-scout.agent.md`) |
| Feature architecture and design | none | Partly gov-spec-writer ("code architect") |
| Prompt writing | none | gov-session is a template (`agent: false`); the main session writes the briefs |
| Spec writing | gov-spec-writer | Yes. It also holds harness `disposal` (folding findings): split. |
| Code building | gov-builder | Yes |
| Testing | none | A program, not a role |
| Deployment | none | |
| Maintenance | none | |
| Review | spec-reviewer, diff-reviewer, skeptic, synthesizer | Design and Build only. diff-reviewer had 0 spawns. No Plan, Test, Deploy or Loop reviewer. |

## 3. Measurements

The window is the last 60 days: commits since 2026-08-15, and transcript events with timestamp ≥ 2026-08-15. Every probe below is read-only.

**P1: git populations.** `git log --all --since=2026-08-15 …`:

| Population | Count |
|---|---|
| Spec files touched (`memory/builds/*/spec/*`) | 1,373 |
| Spec files added | 1,252 |
| Non-merge commits touching `tools`/`skills` | 2,074 |
| Review files added | 488 |
| Research records added (`memory/builds/*/build/*research*`) | 35 |
| Role trailers on commits | 0 (trailers: Co-Authored-By 5,210, Decided 1,516, Pass 1,353) |

Because commits carry no role trailer, git alone cannot attribute authorship. Attribution comes from transcripts.

**P2: transcript writes.** I streamed the Python transcript scan over all 3,268 transcript files (3,204 of them subagent transcripts), counting Write, Edit and MultiEdit calls by actor. A subagent's actor comes from its `agentType` in `.meta.json`. Counts are calls / distinct files:

| Class | Typed role | Untyped | Main session |
|---|---|---|---|
| spec | 605 / 21 | 3,164 / 137 | 605 / 233 |
| product | 219 / 16 | 1,993 / 107 | 565 / 98 |
| review | 4 / 4 | 252 / 129 | 14 / 14 |
| research | 0 | 10 / 3 | 15 / 14 |
| plan (README, `build/`) | 29 | 418 | 336 / 142 |
| briefs (`prompts/`) | 0 | 2 | 74 / 58 |

Bash `git commit` calls: main 1,459, untyped 1,354, typed 55.

**P3: before and after the role arm.** The role index commit `06194e750` is dated 2026-10-12. Write calls, as typed / untyped / main:

| Class | Before 2026-10-12 | After 2026-10-12 |
|---|---|---|
| spec | 0 / 3,164 / 591 | 605 / 0 / 14 |
| product | 0 / 1,983 / 452 | 219 / 0 / 105 |
| review | 0 / 249 / 14 | 4 / 3 / 0 |

- Main session spec edits before the arm: 551 content edits and 40 status-only.
- **P3b, outcomes after the arm.** Main session: 14 spec content edits and 101 product writes were admitted, and 4 were refused by the route arm. All of these were in one session, in worktree `musing-lumiere-ab7980`. Its tip `2a9d8191d` does not contain `06194e750` (`git merge-base --is-ancestor` → "lacks"), so that tree had no role index.

**P4: Bash write shapes.** Bash calls that redirect, `tee`, `sed -i`, `write_text` or `git apply` into spec, review or product paths:

| Actor | Before the arm | After the arm |
|---|---|---|
| Main session | 977 | 85 |
| Untyped | 1,400 | 1 |
| Typed | — | 66 |

The role arm never sees these.

**P5: folding findings.** Main session spec or product edits made after reading a `reviews/` file in the same session: 167 spec and 200 product, across 8 sessions.

**P6: spawns by agent type** (meta files with mtime in the window):

| Agent type | Spawns |
|---|---|
| workflow-subagent | 2,151 |
| general-purpose | 74 |
| gov-spec-writer | 56 |
| gov-builder | 23 |
| gov-spec-reviewer | 20 |
| gov-skeptic | 20 |
| gov-researcher | 19 |
| Plan | 18 |
| gov-synthesizer | 4 |
| Explore | 1 |
| gov-orienter, gov-reuse-scout, gov-diff-reviewer | 0 each |

**Main session spawns of harnesses or agents:** Workflow 344 and Agent 60 before the arm; Workflow 32 and Agent 56 after.

**Role functions the main session performed itself, with counts:**

- Writing or editing specs: 605 calls on 233 files.
- Editing product code: 565 calls on 98 files.
- Folding review findings: 367 edits.
- Drafting plans or briefs: 336 plan writes and 74 brief writes.
- Writing review reports inline: 14.
- Writing research records from researchers' returns: 14 files.

## 4. Gaps

- **HIGH:** 32 of the 70 items have no performer, and 18 are done by the main session. Only 11 are done by a role (table in §2).
- **HIGH:** The role arm grades 2 of the 5 write classes. `review` and `records` are read by nothing (`scratch-guard.js:102-103`), and 85 main-session Bash writes after the arm passed it (P4).
- **HIGH:** A tree with no role index is unarmed (`scratch-guard.js:99`). 115 main-session spec and product writes were admitted after the arm (P3b).
- **HIGH:** No role exists for planning, feature design or decomposition, finding disposal, test attribution, release, maintenance, or the Plan, Test, Deploy and Loop reviews (§2).
- **MED:** A harness stage may run untyped (`tier2-review.js:238`). Before the arm, 100% of harness spec writes were untyped (3,164).
- **MED:** Three roles had 0 spawns in 60 days (P6), and one of them (reuse-scout) has an empty body.
- **MED:** gov-spec-writer holds two functions, authoring and disposal (`workflows.toml` line 38 `stages`).
- **MED:** Folding findings is done by the main session: 367 edits in 8 sessions (P5).
- **LOW:** Research records are written by the main session from researchers' returns (14 of 35). This is legitimate bookkeeping, but no role or command owns `records`.

## 5. Candidates

**A. Path-class gating, extended.** Add write classes for review, records, plan and brief to the role arm. Refuse when the role index is absent in a governed tree. Gate Bash writes as well.

- **Seam:** `scratch-guard.js` role arm, plus `check_roles.py:94` `WRITES`.
- **Losing test:** a role function that leaves no distinguishable path, so the path class cannot separate role work from bookkeeping.
- **Result: loses.** Plan drafting and bookkeeping both write `memory/builds/*/build/` (main session: 336 writes). Running a review inline writes nothing until its report. Bash writes are 85 after the arm and reach no write gate.

**B. Item-bound actors.** Each checklist item names one actor (a role slot, a command or the owner). The executor spawns only that role, with a rendered brief. The item's witness accepts an artifact only from a spawn whose `agent_type` comes from the hook payload. Outside an item only read-only probes are free, with A's arm as the floor.

- **Seam:** the `workflows.toml` `stages` map, `handoff.py render`, and the `roles` argument to `tier2-review.js`.
- **Losing test:** some item that needs judgment cannot be given one actor, or the harness cannot bind a type.
- **Result: passes, with a stated condition.** All 18 main-session items and all 11 role items map to one slot each in the roster below. The harness already binds types: after the arm, 605 typed spec writes and 0 untyped. B needs the optional-key escape at `tier2-review.js:238` closed.

**C. One session per role.** Launch each role as its own session through the gov-session handoff. The main loop becomes a role.

- **Seam:** `gov-session.agent.md` and `handoff.py`.
- **Losing test:** whether the role's identity comes from a source no agent typed.
- **Result: loses.** "a session launched AS a role, whose payload carries that role's type" escapes the gate (`scratch-guard.js:101`), because the launcher types the role. It also brings back per-session orientation cost, which the design removes.

**Roster the steps need, under B:**

- **Keep:** builder, spec-writer (authoring only), researcher, skeptic, synthesizer.
- **Split:**
  - A designer (Design items 3 and 6, absorbing reuse-scout) splits from spec-writer.
  - A disposer/fixer (Review item 6, Build item 8 fold) splits from spec-writer's `disposal`.
- **Merge:** spec-reviewer and diff-reviewer become one reviewer whose lens is set by the stage artifact. It also covers Plan, Test and Deploy reviews.
- **Add:**
  - A planner (Plan items 3, 5 and 6).
  - A test attributor (Test item 4).
  - A releaser/maintainer (Deploy item 5, Maintain items 4 and 5).
  - A loop reviewer (Loop item 3).
- **Retire into commands:** orienter (`next` does this) and gov-session (a message format, not a worker).

The 32 items with no performer go to commands, not roles, except the four review and Loop-proposal items that need judgment.

## 6. Pick

I recommend B with A's arm kept as the floor beneath it. Path classes cannot tell planning from bookkeeping and cannot see Bash writes or inline reviews, so they fail the owner's rule that role functions happen only in oriented agents. Binding each item to one actor, with an untyped source checking the witness, does pass it.

B rests on three seams that already work: the harness's type binding (0 untyped spec writes after the arm), the `stages` map, and `handoff.py render`. Two things must be closed first: the optional role key (`tier2-review.js:238`) and the unarmed state of a tree with no role index (`scratch-guard.js:99`).

**Hand-offs to the parallel researchers:** role anatomy and enforcement owns the Bash write gate and the trust in `agent_type`; the interactions researcher owns how the new disposer and designer exchange work with the spec-writer.
