# Research: coordination across nodes a, b and d, for the chain's execution

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 215's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-52-researcher.md`.

---

## Coordination across nodes a, b and d: findings

**Answer.** Today's gov keeps two nodes off one build. It does not keep them off one path, and nothing on the remote orders the chain's builds. The plan works with today's tools if the unit of distribution is the whole chain build, run as one `/unattended` run per build. Each node takes the next build whose parents have landed, checking the claims first. Four manual rules make up the rest: open all 22 build folders in one landing first, push run branches after every pass, hold rather than go silent, and reconcile on the branch when `--prepare` conflicts.

Paths are relative to the repository root, `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/`. The probes are under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/exec/d215/`. No network or model call was made. The claim cache I read is this clone's copy as of its last fetch.

### 1. Facts the answer rests on

**Claims (the driver is `tools/unattended/unattended.sh`, not `lib-unattended.sh`)**
- **The record.** A claim is one ref per slug, `refs/gov/runs/<slug>`. It is a parentless commit carrying eight keys: slug, node, host, session, keepalive, status, lease-utc and beat-utc (`unattended.sh:2077-2080,2087`).
- **Switched on here.** Claims are off by default (`unattended.sh:2082,673`), and gov declares `RUN_CLAIMS="on"` (`.unattended.conf:162`).
- **The node field is a user name, not a fleet tag** (`unattended.sh:2410`). The three users are distinct in `tools/playbook/fleet.toml`, so the field still tells nodes apart.
- **How a claim is read.** One bounded fetch copies every claim into `refs/gov/remote/runs/*` (`unattended.sh:2136`). Each claim gets one verdict (`:2177-2186`):
  - `held` never ages.
  - `landed` and `aborted` read as terminal.
  - `live` turns `stale` once the beat is older than `RESUME_STALE_BOUND`, which is 5400 s (`.unattended.conf:95`).
- **How a claim is written.** The write is a compare-and-swap, `push --force-with-lease=<ref>:<sha read>` (`:2423`). A rejection marked `stale info` or `fetch first` means the claim was lost (`:2434`, check 108).
- **Who may write it** (`:2284-2301`):
  - `--preflight` refuses a foreign live or foreign held claim with check 107.
  - `--preflight` silently takes over a foreign stale claim (`take-announced`, `:2291`).
  - A take-over takes a held or stale claim (`:2290-2291`).
  - A holder that finds a foreign claim gets check 108 and must abort with `claim-lost` (`:2297`).
- **When it is written.**
  - Live at preflight: `:7340,7455`.
  - Live at take-over: `:8899-8904`.
  - Re-read and renewed before `--close`: `:10697-10709`.
  - `held` at hold: `:6914-6916`.
  - `landed`: `:6244-6246`.
  - `aborted`: `:6631-6633`.
- **Heartbeats.** A beat is due at a quarter of the stale bound (`:2269-2275`). The resume tick's `--beat` renews it only for a run that is LIVE on this host (`:2464-2499`).
- **The resume tick skips any run leased on another host** (`tools/unattended/resume-tick.sh:281-285`).
- **Reading claims.** `--claims` prints slug, node, status, beat age and verdict, and decides nothing (`:2194-2206`). The kickoff card shows it in its `claims —` cell (`skills/session-kickoff/manifest-check.sh:630-655`).
- **Measured probe: the race is real.** Two clones each created `refs/gov/runs/dX` against one local bare remote. The first got `[new reference]` and the second got `[rejected] (stale info)`, which the driver reads as LOST. The probe is in `cas/`.

**The overlap probe**
- `check_cross_run_overlap` always returns 0 (`unattended.sh:3409`) and prints "this run is NOT blocked" (`:3514`).
- It compares only remote-tracking refs as of the last fetch (`:3438-3439,3513`). It ignores refs older than 14 days (`:3382`) and excludes `SHARED_RECORDS` (`:3433-3435`).
- Preflight calls it (`:7355`), and the kickoff card calls it through `--overlaps` (`manifest-check.sh:564`).
- The protocol permits concurrent runs: "a run is never refused because another build is live" (`memory/guides/UNATTENDED-PROTOCOL.md:333-335`).

**Landing**
- gov uses `LANDER_MODE="in-place"` (`.unattended.conf:18-23`).
- `--prepare` merges the run's branch `--no-ff` onto the tip the remote advertises (`tools/push-main.sh:873-884`). On a conflict it changes nothing and prints the recipe: merge `origin/main` on the branch, then re-prepare (`:881-882`).
- `--land` pushes HEAD. The bar runs inside the push.
- If the remote moved, it re-prepares and re-gates, up to `GOV_PUSH_MAIN_MAX_RETRIES`, default 3 (`:188,949-1006`).
- `--carry` refuses another build's commits that came in through local main (`:21-23,959`).
- Kit versions and generated outputs are minted and regenerated at landing (`:26-40`).
- There is no lock across nodes. The default branch's fast-forward check on the remote is the only serializer.
- A raw push to the default branch is refused without the lander's marker (`.githooks/pre-push:1215-1223`). A push to any other branch skips the bar (`:1163`).
- The `pre-rebase` hook steers to "merge, never rebase" (`.githooks/pre-rebase:1-8`). The charter says the same at `AGENTS.md:31,33`.
- **Doc-only pushes get a lighter bar.** A push that changes only `memory/`, `README.md`, `AGENTS.md` and the other listed docs skips each leg that declares `doc_reads` (`.githooks/gate-env.sh:69-73,108`).
- `INHERITED_RED=land` (`.githooks/gate-env.sh:103`).
- No `GATE_POST_MERGE` is declared, so every landing runs its bar before the push.
- The bar's wall ceiling is 21600 s (`.unattended.conf:67`).
- The only per-node lock is the claim-push lock against the lander marker, inside one git dir (`unattended.sh:2305-2359`; `push-main.sh:294-317`).
- `LANDING_NODES` is undeclared, so every node may land (`UNATTENDED-PROTOCOL.md:528,436-438`).

**Shared records**
- **Merge rules.** `DECISIONS.md`, the backlog shards and the per-build `BACKLOG.md` files use `merge=rows`. `LIVE.md`, the ledger and the gotcha index use `merge=ours` and are re-rendered at landing (`.gitattributes:71-86`).
- **Both drivers are per-node git config.** Without them git falls back to a text merge that conflicts. `check-wiring.sh` sets them (`tools/check-wiring.sh:1200-1215,1433-1462`).
- **`memory/project/readme-contract.txt` has no merge attribute.** Every build that opens a folder appends one row to it (`.unattended.conf:383-396,405`).
  - **Measured probe:** two branches each opened one build. `DECISIONS.md` merged clean through the rows driver. `readme-contract.txt` gave `CONFLICT (content)`.
  - With a `merge=union` line it merged clean. The probe is in `fx/`.
  - History matches: the census counts `readme-contract.txt` twice among the conflicted files (`build/2026-10-19-…-research-cloud-census.md:68`).
  - Concurrent builds' reconciles reported 30 and 33 conflicts, mostly version markers and pins (merge messages `dd0d1cece`, `dd2f6ba68`).
- **Ids.** The slug is the guarantee, with no shared counter, and the later merge re-mints any unmerged id (`memory/HYGIENE.md:173-187`). All chain slugs are pre-named `d…` in v2. So disjointness rests on the claim (one run per slug), not on the node's tag letter.
- **Build parents.** A README's `parents:` must name a build folder that exists in the tree, or the index render raises an error (`tools/memory-tree/gen_build_index.py:2335-2345`).

**Take-over across nodes**
- Under `ANCHOR_SCOPE="published"` a hold must publish the branch first. gov declares `local` (`.unattended.conf:261-267`), so a held run's tip may exist on one node only (`unattended.sh:6802-6825`).
- `--handoff` takes only `owner-landing` or `owner-decision` (`unattended.sh:1036,6994-6995`). There is no hand-off from one node to another.
- A take-over works only through a manual `--resume <slug> --keepalive-id <new>` on a node that has the branch (`:8856-8904`).

**Joining a node**
- **Fleet tag:** a row in `tools/playbook/fleet.toml`, claimed with `--claim-node` (`AGENTS.md:102-114`; `WIRE-INTO-PROJECT.md:37-43`). Node d's `host` is blank.
- **Kickoff skill:** junctioned once per machine (`AGENTS.md:90`; `WIRE-INTO-PROJECT.md` §1).
- **Per-node git config:** `core.hooksPath` and both merge drivers (`check-wiring.sh:740-773`).
- **Remote:** exactly one remote (`unattended.sh:2100-2101`) with `origin/HEAD` set (`:2373-2376`; `push-main.sh:180-186`).
- **Settings:** `.claude/settings.json` is tracked.
- **Worktrees:** recreated by hand.
- **"Seed local memory from the in-repo mirror"** (`AGENTS.md:114`): no tool or path names that mirror.

**Where the records and the code disagree**
- gap-conc-02 ("claims never age", register line 323) and theme T5 ("never expire", lines 58-59) are half wrong. A `live` claim ages to `stale` at 5400 s and preflight takes it over (`unattended.sh:2184-2185,2291`). Only a `held` claim never ages (`:2182`).
- The cached claims match the register's "8 of 17 held". All 17 are from users daily-agent (node a) or d41ly (node d); none from node b.

### 2. Shape of the chain (measured, `width.py`, `static.py`)
- **Size.** 509 units over 22 builds, with a critical path of 276 units, matching the `critical-path.py` output.
- **Three nodes are already enough.** With one build per node and a parent's landing gating its children, 3 nodes reach 276 units and so do 4. Two nodes need 310.
- **Width.** The chain is one build wide from unit 0 to 30 and from 67 to 101, and at most four wide anywhere.
- **Path overlaps.** Of the 34 pairs of builds the chain does not order, 3 name a shared path in v2: `handoff.py`, `check_roles.py` and `tools/lib`. This is a lower bound, because rows mostly name keys rather than files.

### 3. Which gap-register coordination rows bite this plan

| Row | Predicted failure | Bites? |
|---|---|---|
| gap-conc-01 (322) | Two builds edit one path and meet only at `--prepare` CONFLICT | Yes, moderate: 3 named pairs plus hot files (`unattended.sh` at 14,346 lines, `gate-legs.json`, renders) |
| gap-conc-02 (323) | Opening a folder or speccing before preflight is unclaimed, so two nodes could open one build | Yes, unless preflight comes first |
| gap-flow-06 (111), gap-plan-01 (341) | Nothing stops a node preflighting a child before its parents land | Yes, high |
| gap-rt-33 (298) | A held run on a node out of quota cannot be taken over, because its branch is unpublished | Yes |
| gap-conc-16 (337) | Nobody finds a stalled foreign run; the resume tick skips it | Yes, with an added hazard: preflight auto-takes a claim stale for over 90 minutes, and the original holder then hits check 108 |
| gap-conc-05 (326) | A parent's landing is seen only at the next fetch | Mild: idle time only |
| gap-conc-08 (329) | Two builds record contradictory decisions on one policy key; both rows merge clean (probe) | Yes, silent |
| gap-conc-10 (331), gap-conc-17 (338) | No channel to the build that owns a found problem | Yes: a deviation found on node b against a build on node a |
| gap-test-02 (370), gap-test-05 (373), gap-conc-07 (328) | Each node re-runs its own bar; a race costs a re-gate | Low: one landing per build, at most 2 interlopers, inside the 3 attempts |
| gap-orient-11 (142) | The card of a build taken over is not findable | Only on a take-over |
| gap-conc-03 (324), gap-rt-06 (271) | Shared worktree or scratch inside one node | Not cross-node |
| gap-conc-04, 06, 09, 11, 12, 13, 15, 18, 19; gap-rt-41 | Faults of the designed lease and mail system | No: those systems do not exist yet. They bite dPlacedRequest's design, not this plan |
| gap-conc-14 (335), gap-rt-08 (273) | Clock skew | No: node d's 8-13 s against a 5400 s bound |

### 4. Candidates and their losing tests

**C1. Build claims plus dynamic pick (recommended).**
- **Mechanism:** one `/unattended` run per chain build. Its claim is the mutual exclusion. A free node takes the ready build with the longest remaining tail. Each run lands itself in place.
- **Losing tests:**
  1. A second create of one claim is admitted. Result: refused (`cas/` probe). Passed.
  2. The claim keeps two nodes off one path. Result: it does not (`unattended.sh:3409,3514`), so C1 needs a path rule and the reconcile step.
  3. A take-over works across nodes. Result: only if the branch was pushed (`:6802-6825`), so it needs a push policy.
  4. Landing races exhaust the retries. Result: peak concurrency is 3, so at most 2 interlopers against 3 attempts (`push-main.sh:188`). Passed, unless attended landings pile on.

**C2. A static stream for each node.**
- **Mechanism:** a written partition of the builds across nodes (`WIRE-INTO-PROJECT.md:48`), with no runtime claim.
- **Losing test:** a 2x slowdown of one node (quota).
- **Result:** static 350 / 408 / 502 units against dynamic 313 in every case. Nothing refuses a node that ignores the document; the claim would.
- **Rejected** as the mechanism. Kept as a tie-break: send builds that share files to one node.

**C3. Split by phase (nodes that spec, nodes that build).**
- **Mechanism:** hold, push the branch, then `--resume` on another node at SPECCING→BUILDING.
- **Losing test:** count the manual cross-node steps.
- **Result:** 22 hand-offs, each a branch push, a fetch, a worktree and a take-over. There is no node-to-node hand-off code (`unattended.sh:6994-6995`), and gap-orient-11 bites on each one.
- **Rejected** as the default. Reserve it for rescuing a stalled node.

**C4. A single landing node.**
- **Mechanism:** `LANDING_NODES` names node d only; the others `--handoff --code owner-landing`.
- **Losing test:** whether landing stays unattended.
- **Result:** `owner-landing` means "HELD for an owner to land" (`unattended.sh:25`), which breaks the owner's "built by /unattended". C1's test 4 also shows contention is too low to need it.
- **Rejected.**

A further candidate, a head node that assigns work, is C2 or C1 with the owner as dispatcher; no offer mechanism exists (gap-conc-19, line 340). It differs only in detail.

### 5. Recommended protocol with today's tools

**Before the first run (once, from one node, as a doc-only landing):**
1. Open all 22 chain folders in one commit: README, planned roster, `parents:`, and their 22 `readme-contract.txt` rows.
   - This is dClosedLoop's own "open the chain" step.
   - It removes the readme-contract conflict entirely.
   - It satisfies the `parents:` existence check (`gen_build_index.py:2335-2345`).
   - It gives every node the same board in `LIVE.md`.
2. On each node:
   - Run `bash tools/check-wiring.sh --fix`, which sets hooksPath and both merge drivers.
   - Run `git remote set-head origin -a`.
   - Confirm the node has exactly one remote, its fleet row, the kickoff junction, and a resume-tick scheduler.

**Each node's loop:**
1. **Pick.**
   - `git fetch` and run `unattended.sh --claims`.
   - A build is ready when every parent's claim shows status `landed` (not `aborted`) and its LANDING commit is on `origin/main`.
   - Pick the ready build with no claim and the longest tail. The node with the most quota takes the critical path.
2. **Claim before writing anything.** Run `--preflight <slug>` from a fresh worktree on `origin/main`. Then spec and build inside that run.
3. **Push the run branch after every pass.** It is ungated (`.githooks/pre-push:1163`). This lets other nodes' `--overlaps` see your files, and lets a take-over reach your work.
4. **Stopping.** For quota or an outage, `--hold --code platform-limit` (held never ages). Never go silent for more than 90 minutes on a live claim.
5. **Landing.** Land in place (`--prepare`, `--close`, `--land`). Never merge a build into local main.

**Points of serialization:**
- The claim's compare-and-swap for each slug.
- The fast-forward of the remote's default branch, with re-prepare up to 3 times.
- The order of the chain's parents, which is checked by hand.
- The one-time opening commit.
- Inside one node, the claim-push lock against the lander marker.

**When a node finds another node's work in its way:**
- **A claim on the slug, `live` or `held`:** pick another build. Never preflight over any claim, because preflight silently takes a stale one.
- **A stale claim:** check whether the holder's branch is on the remote (`git ls-remote origin`).
  - If it is: take over with `--resume --keepalive-id`.
  - If it is not: leave it and tell the owner.
- **An overlap line at preflight or on the card:**
  - If the other ref is a parent, wait.
  - Otherwise proceed, files go first. The later lander merges `origin/main` into its branch on `--prepare` CONFLICT (`push-main.sh:881-882`), then re-prepares.
  - Generated files are re-rendered, never hand-merged.
- **A problem in another build:** file an ask in that build's `BACKLOG.md` (`merge=rows`) under your own session slug, and push.
- **Foreign commits on local main:** `--carry` refuses them. Land from your branch.

### 6. What today's gov cannot do, and the smallest change for each

| Missing | Smallest change | Kind |
|---|---|---|
| A dependency gate: preflight does not refuse a child whose parent has not landed | Preflight reads the README's `parents:` against `--claims` status `landed` | A dPlacedRequest unit. Until then, a manual step (step 1 above) |
| Path exclusion between builds | Make the overlap probe refuse at a declared threshold | A dPlacedRequest unit. Until then: push branches, plus the C2 tie-break |
| Reaching a stalled run across nodes | Hold publishes the branch | Policy: push after every pass. Or a one-key change, `ANCHOR_SCOPE` to `published`, which carries the costs at `.unattended.conf:254-260` |
| Preflight silently takes a stale claim | Make `preflight:foreign-stale` refuse unless asked | A unit in the unattended kit. Until then: the "never preflight over a claim" policy |
| `readme-contract.txt` conflicts on concurrent opens | Open all folders in one commit, or add a `merge=union` line | Manual step. A union line would need its own red test for duplicate rows, given `.gitattributes:63-65` |
| A cross-node channel and question-keyed decisions (gap-conc-08, -10) | None with today's tools | The owner arbitrates; the chain's coordination build owns it |
| "Seed local memory from the in-repo mirror" names no mirror | Name the source path, or drop the step | A record fix for the playbook stream |
