# Research — the Build stage: how an approved spec becomes landing-ready code today, and the contract it should have

**Serves:** research PLAY-dClosedLoop-1

Returned by `gov-researcher` at its role's effort on handoff
`prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-3-researcher.md`, session `1799cb98`, 2026-10-14:
110.0k subagent tokens, 44 tool uses, 279 s. Recorded verbatim below the rule. The main loop's
reading of it lives in the gap register, not here.

---

## 1. Inventory

- **/build Skill**: the attended router. It flips a spec to INPROGRESS, appends `## route`, dispatches the unit harness, folds review blockers as fix passes and runs the bar once. `.claude/skills/build/SKILL.md:57-85`
- **workflows.toml**: the stage table. `build` (stage 5) runs `unattended-unit.js` as `gov-builder`, `closing-review` (6) runs `tier2-review.js`, and `gate-bar` (7) runs `run-gates.sh`. `tools/roles/workflows.toml:51-78`
- **gov-builder role**: builds one unit, writes only the paths it declared, runs no gate, commits a new commit with the unit id, and returns `DIVERGENCE:` instead of editing the spec. `tools/roles/agents/gov-builder.agent.md:1-47`
- **handoff.py and house/policy.toml**: render the hashed prompt, the `harness-args` and the `stage-efforts`. The builder's gate allowlist is `lexicon naming predicates?` only. `tools/roles/house/policy.toml:28-30`
- **Spawn guard (agent-cap RULE 6)**: admits an `Agent` call only with a rendered handoff and a matching description, and a `Workflow` call only for a listed harness with roles. `tools/hooks/agent-cap.js:38-60`
- **Fan-out cap**: CAP 5, slot claims made with O_EXCL. Agents a harness spawns internally are not counted. `tools/hooks/agent-cap.js:19-26,107`
- **Write gate (scratch-guard)**: an Edit under `ROUTED_PATHS` needs the card's `## route` to name a BUILDABLE unit, and then a `writes=product` role. `tools/hooks/scratch-guard.js:1113-1200`; `.memory-tree.conf:9`
- **Role-gate arm**: refuses a role agent any gate leg or suite outside its allowlist. `scratch-guard.js:104-127`
- **Orientation check**: refuses a main-loop `git commit` while the card still reads `READY — none yet`. `scratch-guard.js:50-56`
- **format-guard**: a Stop hook. It refuses a turn end with no BUILD/SPEC pair, an unreported commit, or a missing agent/returned line. `tools/hooks/format-guard.js:1-30`
- **unattended-unit.js**: one unit, one agent. It passes back `committed`, `sha` and `diverged`. `tools/workflows/unattended-unit.js:1-60`
- **unattended-build.js**: runs SPEC, then AUDIT, then DISPOSAL, then hands out the roster. It buys "ORDER and not ENFORCEMENT". `memory/guides/BUILD-METHOD.md:222-230`
- **BUILD-METHOD M6–M9**: one commit per pass with the unit id in the subject; the gotchas checklist after each commit; `parallel-when-disjoint`; the bar runs once; closing review from a pinned BASE; derived wrap-up. `memory/guides/BUILD-METHOD.md:180-310`
- **routed-commits leg**: every product commit names a unit whose spec existed at its first parent. Its F1 says it does not read scope. `tools/memory-tree/routed_commits.py:1-40`
- **pass-order history leg**: refuses a CLOSED unit built before it was specced. `tools/unattended/check-pass-order.sh:2`
- **brief-recorded leg**: a gate leg in `tools/gate-legs.json`.
- **Unattended driver**: `--dispatch` records write sets; `--close` evaluates a 13-item DoD, including `closing-review-recorded`. `tools/unattended/unattended.sh:868,11626`; `memory/guides/UNATTENDED-PROTOCOL.md:340-379`
- **RUN.md, run-lease.js, stop-guard, gate-guard**:
  - run-lease.js binds a session to a run. `tools/unattended/run-lease.js:1-30`
  - stop-guard refuses a turn end while a run is non-terminal. `stop-guard.js:1-30`
  - gate-guard refuses the flagged bar before VERIFYING, and refuses AskUserQuestion. `gate-guard.js:1-30`
- **Run claims**: `refs/gov/runs/<slug>` on the remote, one per unattended run, "no lock". `unattended.sh:2076-2086`; `.unattended.conf:162`
- **Overlap probe**: `--overlaps` and the kickoff `overlaps —` cell. It "always returns 0". `unattended.sh:3409,3523`; `skills/session-kickoff/manifest-check.sh:555`
- **Id minting**: `FAMILY-<slug>-<seq>`. The node letter keeps slugs disjoint; the later to merge re-mints. `memory/HYGIENE.md:168-187`
- **Row-keyed merge drivers**: `merge=rows` for DECISIONS and BACKLOG, `merge=ours` for the generated views. `.gitattributes:61-89`
- **Landers**: push-main.sh reconciles before the gate and retries up to 3 times. `LANDER_MODE="in-place"`, and `LANDING_NODES` decides which node lands. `tools/push-main.sh:1-30`; `UNATTENDED-PROTOCOL.md:422-461`
- **Pre-commit branch guard**: refuses a commit in the primary tree when it is off the default branch. `.githooks/pre-commit:64`
- **[isolate] practice**: "every unit in its own worktree". `AGENTS.md:30`
- **tier2-review.js and REVIEW-PROTOCOL**: the closing diff review. Finders, then skeptics, then synthesis; `kind` defaults to `diff-review`. `tools/workflows/tier2-review.js:183-184`; `memory/guides/REVIEW-PROTOCOL.md:190-230`
- **process-monitor**: identifies and reaps processes a session forgot. `memory/map/features/process-monitor.md`

## 2. Flow

**Coming in from Design:** a spec at READY or SPECCED, the brief under `prompts/`, the owner's go on the card, and the reuse audit in spec §10.

**For each unit:**
1. The main loop flips the status to INPROGRESS. This is the only spec edit the role arm admits from the main loop (ENFORCED, `scratch-guard.js:95-98`).
2. It appends `## route` through `manifest-check.sh --card --append`.
3. It calls `unattended-unit.js` with `roles.builder`. ENFORCED: the spawn guard checks the harness and its roles.
4. The builder edits product paths. ENFORCED: the write gate, but only "is some routed unit buildable" and "is the writer a product role".
5. The builder commits with the unit id. ENFORCED at push: routed-commits checks that some specced id is named.
6. The builder runs `gotchas.py --for-diff`. STATED only.

**Diverged:** the spec writer revises the spec and the unit is re-dispatched. STATED in the Skill.

**Closing review:** `tier2-review.js` runs from BASE (round 1) or from the prior tip (round N), with `reviewDir` set. Blockers are fixed as passes of the unit they land in; highs and below are carried forward. On the attended path this is STATED only. Under a mandate it is ENFORCED by `closing-review-recorded` at `--close`.

**Owed arms:** observed RED then GREEN by the main loop. STATED (M8).

**Bar:** one bar after the last unit is terminal. ENFORCED at push by the pre-push hook. A pass running a gate is ENFORCED against by the role-gate arm and by gate-guard.

**Landing:** the owner's ask (attended) or a mandate. ENFORCED by the pre-push marker that push-main sets.

**Concurrency:**
- `parallel-when-disjoint` is STATED. Write sets are recorded only by unattended `--dispatch`.
- Overlap and claims are ADVISORY. The probe printed "this run is NOT blocked".
- Ids are collision-free by construction of the slug.
- Shared records merge by row.

**Going out:** to Test, a committed range plus the owed arms and the bar verdict. To Deploy, the lander and kit-version mints (`push-main.sh:25-30`).

## 3. The implicit contract today

- **Entry:** a READY card with the owner's go quoted; the spec is BUILDABLE (INPROGRESS for Tier-2); `## route` names the unit.
- **Exit, attended:** every tracked spec is terminal; one bar is green; the owner asks to merge and push. A closing review record is owed by M8 but checked by nothing.
- **Exit, unattended:** a 13-item DoD at `--close`, including `build-complete`, `closing-review-recorded` and `gates-green`, followed by `landed-via-lander`.
- **Artifacts:** one commit per pass carrying the unit id, `Pass:` and `Decided:` trailers; review records under `builds/<slug>/reviews/` with `**Serves:** diff-review`; RUN.md (mandated runs only); the agent ledger; the wrap-up.
- **Who does what:**
  - gov-builder writes the code.
  - The main loop flips status, routes units, runs the bar and folds the review.
  - The owner gives the go and lands.
  - gov-diff-reviewer, gov-skeptic and gov-synthesizer run the review.
- **Review at this stage:**
  - Owed once per build over `BASE..HEAD`, with re-review of each fold.
  - Only blockers are fixed. Each confirmed finding must be left-shifted to a gate or a gotcha class.
  - The record is renamed to the check-5 grammar.

## 4. Gaps

- **HIGH: scope is not bound to the unit.**
  - The write gate admits any `ROUTED_PATHS` write once any routed unit is buildable (`scratch-guard.js:1191-1197`).
  - routed-commits passes any named id (`routed_commits.py:32`, F1).
  - Measured since 2026-10-01: 120 of 584 unit-attributed product commits touched a file outside their unit's Files touched. At kit-directory granularity it is 42 of 582, 4 of them mints.
- **HIGH: the attended closing review is unenforced.** Builds with a CLOSED unit that carry a `diff-review` record:
  - attended: 29 of 59
  - unattended: 86 of 89

  `diff-review` appears in no push-time leg (absent: grep of `.githooks/`, `push-main.sh` and `check-memory-hygiene.sh`).
- **HIGH: cross-node work overlap is advisory.**
  - `check_cross_run_overlap` "always returns 0" (`unattended.sh:3409`), and the live probe printed "NOT blocked".
  - It sees only pushed refs.
  - Claims are per unattended run only (`unattended.sh:2076-2086`).
  - There is no unit or path claim (absent: grep for "claim" in `scratch-guard.js` and `manifest-check.sh`).
- **MED: [isolate] has no mechanism.** `AGENTS.md:30` says one worktree per unit. In practice the harness shares a worktree and meets "git's index lock" (`unattended-build.js:134`). No `worktree add` exists for units (absent: grep across `tools/` and `skills/`).
- **MED: the Build contract depends on the mode.** The DoD's review predicate needs RUN.md's pinned base (`unattended.sh:11662-11665`). The attended BASE lives only on the untracked card.
- **MED: the guard shares state with what it guards.** The write gate reads a status and a route the agent writes (`scratch-guard.js:88-89`), which breaks the charter's [class] rule.
- **MED: Bash and PowerShell product writes escape the write gate** (`scratch-guard.js:85-87`). Only push-time attribution backs it.
- **LOW: the per-pass gotchas checklist is unverified.** Nothing reads whether it ran (absent: grep for `for-diff` in the hooks and legs).
- **LOW: agents a harness spawns internally are uncounted by the fan-out cap** (`agent-cap.js:23-25`).

## 5. Candidates

**A. Push-boundary history legs.**
- **Mechanism:**
  - Extend routed-commits so a commit's product paths must fall inside the kit directories that its named units' Files touched declare.
  - Add a leg that, for every build whose units reach CLOSED in the pushed range, requires a tracked `diff-review` record naming a commit in that range.
  - The base is derived from history: the parent of the build's first pass commit. Both run in pre-push and remote CI, for every mode.
- **Seam:** `tools/memory-tree/routed_commits.py`, plus the join in `unattended.sh:11626-11700`.
- **Losing test:** it loses if real history violates the scope rule often enough that it is noise. It also loses if the review join cannot run without RUN.md.
- **Result:**
  - At file granularity, 20.5% of commits violate, so A loses there.
  - At kit granularity, 7.2% violate, so it survives with a cutoff.
  - The join's base can be derived from git, so it survives.

**B. Pre-act unit lease.**
- **Mechanism:**
  - The `## route` line carries the unit's declared write set, and the write gate refuses an Edit outside it.
  - `--card --append` acquires `refs/gov/units/<id>` on the remote, extending the run-claim namespace.
  - The overlap probe turns a claimed shared path into a refusal.
- **Seam:** `scratch-guard.js` `checkRouted`, the claim code at `unattended.sh:2076`, and `manifest-check.sh --card --append`.
- **Losing tests and results:**
  - (i) The remote must accept `refs/gov/*`. `git ls-remote` shows 17 `refs/gov/runs` refs, so B passes this one.
  - (ii) The declared sets must be faithful enough not to stop legitimate passes. 20.5% of historical commits would have been refused mid-pass at file granularity, so B loses there and needs kit granularity.
  - (iii) It reads agent-written state, which the charter's [class] rule forbids for a sole guarantee.

**C. One exit through the lander's DoD.**
- **Mechanism:** attended builds close the way mandated runs do. `push-main --prepare` evaluates `DOD_CORE` on the prepared merge, and the in-place lander serializes the landing order across nodes.
- **Seam:** `tools/push-main.sh`, plus `DOD_CORE` at `unattended.sh:868`.
- **Losing test:** it loses if the DoD cannot evaluate without a run-state file.
- **Result: loses.** `closing-review-recorded` refuses with "the run-state file records no usable pinned base" (`unattended.sh:11662-11665`). It also does nothing about scope.

## 6. Pick

I recommend A: the Build stage's exit contract becomes two push-boundary legs, unit-scoped attribution at kit granularity and a recorded closing review per build, run identically in pre-push and remote CI for attended and unattended builds. It is the only candidate whose guard reads committed history rather than state the agent writes, which is what the charter's [class] rule asks. It survived its losing test once file granularity was dropped (7.2% at kit level, 4 of the 42 being mints, so it lands behind a cutoff). C lost outright, because the DoD needs RUN.md. B's pre-act lease should come next as the concurrency layer, at kit granularity and with A as its backstop; it is the only one of the three that closes the advisory-overlap gap. That gap stays open under A, and it is the Deploy-facing hand-off on landing order to raise with the neighbouring stage.
