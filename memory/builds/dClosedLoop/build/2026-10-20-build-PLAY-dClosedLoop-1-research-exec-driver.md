# Research: the unattended driver, end to end, for the chain's execution

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 214's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-51-researcher.md`.

---

## The unattended driver, end to end: research return

**Answer.** Today's `/unattended` can carry one chain build on one node from start to landing: it writes the unit specs, runs the spec audit (only if the owner opts in), builds the units one after another, runs the closing review and lands. It cannot share one build across nodes, and it cannot run units in parallel inside one run. So the owner's distribution has to happen between builds: one chain build per run, one run per worktree, on any of nodes a, b and d. Before each run, someone has to prepare and commit (or land) the build folder by hand.

I wrote nothing in the repository. My probes are three read-only scripts in my scratch folder (`sizes.py`, `selfmod.py`, `clause.py`), plus `--plan`, `--version`, `carries.py`, `critical-path.py` and `schtasks /query`. The `session-log.md` change in the worktree is the parent's dispatch rows 214–218, not mine.

### Facts the answer rests on

**Authorization and start**
- The build folder's README is the authorization. The owner's act is `/unattended <slug>` (`memory/guides/UNATTENDED-PROTOCOL.md:21-27`). This repo declares `ANCHOR_SCOPE="local"` (`.unattended.conf:267`), so a README committed at HEAD authorizes a run with no push needed (`UNATTENDED-PROTOCOL.md:87-91`).
- The run's first act is scheduling a 10-minute idle-wake job (`.claude/skills/unattended/SKILL.md:16`). Then `--preflight` runs, then `/session-kickoff` (`SKILL.md:63-65`).
- Preflight refuses:
  - a dirty tree (`tools/unattended/unattended.sh:2929`);
  - the default branch (`:2937`);
  - on a first preflight, a branch that carries commits outside the build folder (check 114; `:3879-3904`, called at `:7421`). So every run needs a fresh worktree.
- Preflight observes the remote, so the node needs origin reachable (`memory/guides/UNATTENDED-VERBS.md:13-20`).

**Spec-audit opt-in and the `may:` grant**
- A `spec-audit:` line in a `slug` README is refused with fail 89 when the BASE came from the local anchor (`unattended.sh:4122-4126`).
- A `may:` grant is refused with fail 78 on the local anchor and in any non-`slug` mode (`:4160-4168`).
- Both are honoured only from a README the owner landed on the default branch.
- The project-wide default `SPEC_AUDIT_DEFAULT` is blank (`.unattended.conf:326`). It is read at the default-branch side of BASE, even under the local anchor (`unattended.sh:4016-4036`).
- Track record:
  - No unattended run has ever used a `may:` grant: all 29 recorded values are `may: none`.
  - The only runs that owed a spec audit were `prompt` mode (`memory/builds/aEvidencedLens/RUN.md`, `memory/builds/aGraftedHelix/RUN.ABORTED.6410435d.md`).
  - No `slug`-mode run has ever pinned `spec-audit`.

**Picking work**
- The run executes only the slug it is handed. Nothing reads parent builds or finds other work (gap register `gap-conc-16`).
- Inside a build, `--plan` takes its set and order from the generated units region and reports roster units with no spec as MISSING (`UNATTENDED-VERBS.md:72-87`).
  - Probe: `--plan dClosedLoop --paths` printed `next: PLAY-dClosedLoop-1 (MISSING - spec it first)`.
- Units that are MISSING, THIN or FORKED are never dispatched (`UNATTENDED-VERBS.md:753-761`).
- An `asks:` list is honoured only from a landed `slug` README (`unattended.sh:4139-4148`).

**What one pass does**
- A pass is exactly one of five things: a spec authored, a spec reviewed, a review's fixes folded in, a unit built, or the closing diff review (`memory/guides/BUILD-METHOD.md:182-183`).
- The build harness `tools/workflows/unattended-build.js` runs three stages:
  - SPEC: up to 5 spec writers in parallel, then one commit (`:104`);
  - AUDIT: only when `specAudit` is passed;
  - DISPOSAL: then it hands back the ordered unit list.
- **Units are dispatched strictly one at a time** (`unattended-build.js:76-80`, `:920`). The build method says disjoint delegated passes "MUST run concurrently" (`BUILD-METHOD.md:209-216`). The record and the code disagree here, and the code wins.
- Each unit goes through `--brief`, `--dispatch` (which also runs `SPEC_TOKENS_CLI`), `unattended-unit.js`, a commit with a `Pass:` trailer, then `gotchas.py` (`UNATTENDED-VERBS.md:697-768`).
- The harness takes an optional per-unit spec brief, `specBriefPath` (`unattended-build.js:170`). That is where a run can tell spec writers which design clauses each spec carries.

**Stops, asks and breakpoints**
- The run never asks the owner anything (`BUILD-METHOD.md:315-322`). Instead it adopts, parks, holds, hands off or aborts:
  - **Park:** a fork with no delegated resolver is parked and the run continues (`UNATTENDED-VERBS.md:36-46`).
  - **Hold:** there are 7 hold codes (`memory/guides/UNATTENDED-STOPS.md:45-46`).
  - **Hand off:** `owner-landing` or `owner-decision` (`UNATTENDED-VERBS.md:963-976`).
  - **Abort:** means discard.
- Two owner turns can exist at all: a directive-waiver question at preflight in `slug` mode, or one opening question in `prompt` mode (`UNATTENDED-VERBS.md:456-463`, `:548-557`).
- Forks that need a governance-carrier change or a new public surface are parked unless a `may:` grant names them (`BUILD-METHOD.md:80-97`). "Governance carrier" is defined nowhere: the term appears only at `BUILD-METHOD.md:83,90`, `UNATTENDED-PROTOCOL.md:668` and `UNATTENDED-VERBS.md:706`.

**Run state and records**
- The run-state file is `memory/builds/<slug>/RUN.md`, with authored facts only (`UNATTENDED-PROTOCOL.md:141-251`).
- A finished record is rotated to `RUN.<phase>.<blob8>.md` (`unattended.sh:4384`).
- Each build folder carries at most one live record (`UNATTENDED-PROTOCOL.md:337`).
- The run log is `runlog/driver.log` in the git common dir. It is machine-local and nothing reads it back (`unattended.sh:13785,13930`).

**Definition of Done**
- 13 core items, `CORE_FLOOR="13:13"` (`UNATTENDED-PROTOCOL.md:345-359`; `.unattended.conf:179`).
- Two items have no override: `authorization-reachable` and `pieces-complete`.
- `build-complete` carries a unit forward only if all five terms of `UNATTENDED-STOPS.md:698-711` hold.

**Landing**
- Landing is in-place: `--phase VERIFYING`, `push-main.sh --prepare`, `--authorization`, `--close` (which runs the bar), `--land`, then `--landed` (`.unattended.conf:23`; `tools/push-main.sh:14-24`; `UNATTENDED-VERBS.md:849-947`).
- Any touch under `tools/` makes the close owe the full flagged bar (`SELFTESTS_OWED_PATHS="tools/"`, `.unattended.conf:40`), with a whole-run wall of 21600 s (`:67`).
- `LANDING_NODES` is undeclared (absent from `.unattended.conf`), so every node may land (`UNATTENDED-VERBS.md:23-26`).

**Concurrency and resume**
- Concurrent runs of different builds are permitted (`UNATTENDED-PROTOCOL.md:333`).
- With `RUN_CLAIMS="on"` (`.unattended.conf:162`), a second node starting the same slug is refused with check 107 (`UNATTENDED-STOPS.md:213-222`).
- Under the local anchor a hold does not require a push, so held work may exist on one node only (`UNATTENDED-STOPS.md:98-99`; `gap-rt-33`).
- The resume tick is not registered on node d: `schtasks /query /tn gov-resume-tick` answered "cannot find". All 23 recorded resumes were manual (`gap-rt-37`).

**Size of the chain**
- 22 builds and 509 clauses. The largest are dWellOiledMachine (61), dOrderedCharter (37) and dDeclaredLoop (34) (`sizes.py` over the architecture v2 `[chain]` section).
- The critical path is 276 units (`critical-path.py`).
- Largest one-run precedent: aMendedFleet, 109 specs, landed in about 29 h (git log span).

**Builds that rewrite the driver they run under**
- dDeclaredLoop `cl-dClosedLoop-0106` re-points `unattended.sh`.
- dPlacedRequest `cl-dClosedLoop-0120` migrates run claims.
- dWellOiledMachine `cl-dClosedLoop-0306` dissolves the unattended kit.
- The driver runs from the worktree (`SKILL.md:11-12`), and "nothing binds the executing code" (`UNATTENDED-PROTOCOL.md:575-576`).

**The deviation instrument**
- `carries.py` reads specs only under `memory/builds/<chain build named in v2>/spec` (`2026-10-19-build-PLAY-dClosedLoop-1-carries.py:121-128`).

### How to authorize and open each chain build

| Candidate | Mechanism | Test that could make it lose | Result |
|---|---|---|---|
| **A** | **Slug mode, README landed on origin main by the owner,** with `spec-audit:` and `may:` as needed. Fresh worktree off main on any node. | Do fail 89 or fail 78 fire at the default-branch anchor? Can one run hold a 61-unit build? | **Survives.** The refusals key only on `local` or non-`slug` (`unattended.sh:4108,4122,4160,4166`). 109 specs landed in one run. Untested in practice: no run ever pinned `slug` with `spec-audit`, or any `may:` grant. |
| **B** | Slug README committed only on the run branch (local anchor). | Does `spec-audit:` survive preflight? | **Loses:** fail 89 (`:4122`), and `may:` gets fail 78. It survives for the audit only if `SPEC_AUDIT_DEFAULT` is set on main and READMEs carry no `spec-audit:` key. It never gets `may:`. |
| **C** | Prompt mode: the run writes its own README and prompt record (one owner turn). | Does the owner's own sentence opt the audit in? | **Partial.** The probe showed the owner's sentence does **not** match `SPEC_AUDIT_ASK_RE` (`unattended.sh:3547`), while "Opt in to the spec audit for this build." does. `may:` is refused (`:4160`). |
| **D** | Split one chain build into several slugs, spread across nodes. | Does the deviation join see the sub-build specs? | **Loses:** `carries.py:124` globs chain-build folders only. Probe: `--build dWellOiledMachine` reported "specs measured 0". Every clause would read uncarried unless an owner-approved `Moved:` record is written per clause. |
| **E** | One slug driven by several nodes at once. | Is a second node's preflight refused? | **Loses:** check 107 under `RUN_CLAIMS=on`, and one live `RUN.md` per build (`UNATTENDED-PROTOCOL.md:337`). |

### How a build too large for one session continues

| Candidate | Mechanism | Test that could make it lose | Result |
|---|---|---|---|
| **S1** | One run across many sessions: hold, resume or take-over on the same `RUN.md`. | Can another node take it over? | **Survives on the same node** (dDerivedDocket: 3 resumes, 2 holds). Across nodes it **loses unless the branch is pushed**: under the local anchor no push is owed (`UNATTENDED-STOPS.md:98-99`). |
| **S2** | Land part of the build: `--rescope --act defer` and spec `DEFERRED`, then the next `--preflight` rotates `RUN.md`. | Can a unit added during the run, such as a promoted review finding, be carried forward? | **Loses for added units** (`UNATTENDED-STOPS.md:703-704`). It also needs an open ask in this build's `BACKLOG.md` for each deferred unit (`:707-709`). Works for units on the original roster. `DEFERRED` stays non-terminal, so the next run picks it up (`unattended.sh:4815,11553`). |

### Recommendation
1. Use **A**: one chain build per `slug` run, one run per worktree. Parallelize only across chain builds whose parents have landed. Continue long builds with **S1**. Use **S2** only when a child build on another node needs a parent's units landed sooner.
2. Make **dTrueNorth (6 units)** the pilot. It is the test A's untested parts must pass: preflight prints `spec-audit — opted in by README spec-audit: <date>`, and `RUN.md` records `anchor-kind: default-branch` and the `may:` grants.

**To prepare by hand for each build:**
- the README: six front-matter keys, a `roster:units` table mapping each unit to the clause ids it carries, and the `gen:build-index` and `gen:build-units` markers;
- its row in `memory/project/readme-contract.txt`, in the same commit (it is a shared record, `.unattended.conf:383-396,405`);
- landed by the owner through the lander;
- a fresh worktree on the chosen node.

Specs are not needed by hand: the harness authors any that are missing (`BUILD-METHOD.md:51-53`). The per-unit spec brief the run writes is where clause pins go.

### Limits the owner's plan would hit, each with its smallest change
1. **No spec audit unless the owner opts in.** As configured, nothing makes a run audit its specs. Change: a **policy**, one line `SPEC_AUDIT_DEFAULT="<date>"` on main, or `spec-audit:` in each landed README. Note that a closing-review round can be bounded at 1 (`REVIEW_ROUNDS`, `.unattended.conf:111`) and every finding gets promoted to a new unit. Only precision bounds that chain of promotions (`gap-flow-23`, which records one chain costing about 12M tokens).
2. **Governance-carrier and public-surface forks get parked.** The fix is a `may:` grant, which has never been exercised. Change: a **manual step**, where the owner names the paths in each landed README. Separately, "governance carrier" needs a definition: a **policy**.
3. **No parallelism within a build, and no sharing one build across nodes.** Change: none today. It is a **chain build's unit**: dPlacedRequest's unit leases (`cl-dClosedLoop-0120`), plus `gap-conc-11`.
4. **Builds that rewrite their own driver.** dDeclaredLoop, dPlacedRequest and dWellOiledMachine change the unattended kit, the lander or gates mid-run. Change: a **policy** that those units go last in their build and the build ends by `--handoff --code owner-landing`, or that those builds run attended.
5. **Cross-node take-over needs the branch on the remote.** Change: a **policy** to push the run branch at every hold, hand-off and pass boundary.
6. **The resume tick isn't registered on node d** (the other nodes are unverified). Change: a **manual step** per node, the `schtasks` line in `tools/unattended/README.md:211`.
7. **Every chain build pays the full flagged bar** (up to 21600 s), and there is no landing queue across nodes (`gap-flow-08`). Change: a **policy** to stagger landings by owner order. A real queue is a **chain build's unit** (`gap-flow-08`).
8. **Nothing orders builds by their parents.** The run executes the slug it is handed. Change: a **manual step**, where the owner or plan hands out each slug only after its parents have landed.
9. **The driver has no Definition-of-Done item that compares specs to the design.** `DOD_EXTRA` items are only attested (`gap-flow-19`). Until dTrueNorth lands, the comparison is a pass check a run chooses to run.

Key paths:
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/unattended/unattended.sh`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/tools/workflows/unattended-build.js`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/.unattended.conf`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/guides/UNATTENDED-PROTOCOL.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/guides/UNATTENDED-VERBS.md`
- `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/guides/UNATTENDED-STOPS.md`
