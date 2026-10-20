# Research: Cloud coordination: the census and the layer

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 148's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-23-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-cloud-and-scale.md`.

---

**The census: where gov assumes one node, where it is ready for nodes coordinating in real time, and which layer owns cloud coordination**

**Short answer.** The design's truth layer is already multi-node: leases, the mailbox, the registers, the card, bindings and the change feed all live on the remote as git refs written by compare-and-swap, and all of it works offline. Memory sharing in real time already has its seam: the change feed plus the memory-mirror point. What is missing is any way to decide *which node does what*. The design has no record of a node's presence or capacity and no way to address a node or the whole project. Nothing makes a node pick up a lease another node released, nothing measures plan usage per account, and an owner's command cannot reach another node's supervisor. Those gaps belong to scheduling, which by the design's own layer rules goes in a new expansion layer. The core has to declare about seven points now so that the expansion can attach later.

Today's tree has used almost none of the designed coordination. The remote holds only 17 run claims. Their history is not kept, they name users rather than fleet tags, they never expire, and 8 of the 9 that are not marked landed belong to builds that are already CLOSED.

**Record disagreements I found:**
- The coordination record says dDeclaredLoop builds the feature (`coordination.md [design]`, line 54). v2 moved leases to dPlacedRequest and the mailbox and dependency notices to dKeptSession (v2:505-507, the chain at v2:1545-1546). The coordination record is stale.
- layer-memory lists the mailbox message among Runtime's kinds (`layer-memory.md:435`), while P5 makes it the flow's.
- The code lines the coordination record cites are current: `unattended.sh:2070`, `:2410`, `:3409` and `gen_build_index.py:3478` all re-verified.

## 1. One row per coordination point

"Endpoint needs" uses three labels: **nothing** (already behind an adapter point or already correct across nodes), **seam** (a point the core must declare), or **redesign**.

| # | Point | Layer · build | Transport | Assumption | Endpoint needs | Losing test (result) |
|---|---|---|---|---|---|---|
| 1 | Build, unit and cadence leases: acquire, renew, release, take over, epoch | flow core · dPlacedRequest (v2:1545 clause 1; keys v2:967-972); Runtime renews and expires (layer-runtime `[supervise]`, 454) | git refs `refs/gov/leases/...`, compare-and-swap, a parent chain (v2:1545 clause 10) | the origin remote is the only shared medium; renewals ride transitions and pass commits; 24 h expiry | nothing for the truth: P2 and P23 keep it in git, and the mirror's reads exclude lease decisions (v2:1552 clause 44) | Mirror on and off must give byte-equal `next`, gate and transition output. The design already holds this test; it is unbuilt. |
| 2 | Take-over of a released or expired lease ("a node with quota takes the build over", v2:1017) | Runtime · dWellOiledMachine | none: no item makes a node look | the work's owner node, or the owner, starts it again | **seam**: a discovery item, so a node's supervisor sees leases it does not hold | Grepped v2, layer-runtime and stall-and-loop for an item that scans foreign leases: none. Today `resume-tick.sh:281-285` skips any lease whose host is another node. **Seam missing.** |
| 3 | Overlap | flow core · dPlacedRequest (`leases.overlap`) | reads live leases | all writers are visible on the remote | nothing | Today `check_cross_run_overlap` "always returns 0" (`unattended.sh:3409`) |
| 4 | Offline (`leases.offline` warn: queue, CAS on reconnect, yield) | flow core · dPlacedRequest (v2:972) | a local queue, then CAS | a node is often disconnected | nothing. This is the guarantee an offline node keeps, so it must stay core | An endpoint-held lease would fail `leases.offline` by construction, which is the right outcome |
| 5 | Mailbox: kinds, disposal, notice | flow core · dKeptSession (v2:1546 items 5-7 and 10; coordination 99-126) | `refs/gov/mail/<slug>/<fleet tag>/<session>`; local copy refreshed at most every `mailbox.fetch-seconds`, 60 | the recipient is "a build, or one of its units" (coordination:104) | **seam**: a node- or project-addressed recipient for intake not yet placed in a build | The recipient grammar admits no node or fleet address. **Seam missing.** |
| 6 | Live delivery (the doorbell) | dKeptSession, through the harness adapter's inbox (v2:1552 clause 35) | harness session messaging, Claude only | one harness, one machine or Remote Control | **seam**: night pass two places NATS, ntfy or Postgres NOTIFY "behind the doorbell, as an optional adapter" (`night-pass-two.md:253-254`), but `deps.messaging` is a closed list | Probe below: `deps.messaging` allows `live-and-mailbox, live-only, mailbox-only`, with no registered name. The `[extend]` table (layer-runtime:834-846) has no doorbell point. **Seam missing.** |
| 7 | Dependencies between builds (`deps.*`, reachability = the parent's live lease) | flow core · dKeptSession | mailbox plus leases | as rows 1 and 5 | nothing beyond row 5 | — |
| 8 | Decision and problem registers (create-only refs) | flow core · dPlacedRequest (v2:1545 clause 11) | `refs/gov/decisions/...`, `refs/gov/problems/...` | none on one node | nothing (fed into the change feed) | — |
| 9 | Change feed | flow core · dPlacedRequest (v2:1545 clause 12) | a node-local file in the git common dir (`memory-plan.md:95`) | rebuildable from git | nothing: it *is* the seam ("a real-time mirror needs no change to the core") | Already designed: the feed deleted and rebuilt equal; red on a dropped event |
| 10 | Memory-mirror point (`memory.mirror`) | Runtime · dWellOiledMachine (v2:1552 clause 44; layer-runtime:846); the adapter is integrations' (`layer-expansions.md:315`) | an adapter's store | git stays the store of record; verdicts stay local | nothing (an open registered name). The database is planned (v2:1595) | Already designed: a stand-in adapter must give mirror-on and mirror-off output that is equal |
| 11 | Card (remote ref, pointers) | flow core · dPlacedRequest; `card.store` is closed | a ref per build | the card is current only to its step | partly behind the mirror ("card's pointers") | `research-handoffs-design.md:133`: pointers update every item with no store named. Ambiguous. |
| 12 | Commit queue and `build.push` (every pass) | Runtime · dWellOiledMachine (clause 40) | pushes the build branch | other nodes see witnesses after a fetch | nothing: commits that touch a record join the feed (`memory-plan.md:95`) | Already designed: a node dies after 3 of 5 units and its successor's `next` names the 4th |
| 13 | Unit holders (`build.unit-holders` any-session) | Runtime · dWellOiledMachine (clause 41) | unit leases plus branch pushes | pull only: a unit is offered at placement to whoever places | **seam**: a placement or offer source an outside proposer can fill. `placement` is closed (`agent-places, declared-checked, owner-places`) | The record names no store for the offer itself (ambiguous), and no value of `placement` lets anyone outside the session propose. **Seam missing.** |
| 14 | Landing queue and order | flow core Deploy · dShippedRelease (v2:1557 item 10; `landing.order` closed) | order read from the leases' verified trees; the push to the default branch | git fast-forward serialises landings | nothing for correctness | Today `push-main.sh` never takes the turnstile (0 matches), and the turnstile is per host at `$HOME/.gov/gate-turnstile` (`run-gates.sh:1513`) |
| 15 | Lander lock against lease and claim writes | dPlacedRequest clause 10 removes it | a git-dir marker today | one git dir | nothing once clause 10 lands | Today the claim push is refused while `push-main-active` exists (`unattended.sh:2414-2415`) |
| 16 | Admission queue and `runtime.agents-in-flight` (6) | Runtime · dWellOiledMachine (clauses 43, 45) | a hook ledger, local process | one **session's** agents | **seam**: no node or account capacity. Under `oauth-shared`, every node on one login draws on one plan limit | Grepped v2 and layer-runtime for quota, usage, capacity or per-account: nothing. The only limit signal is StopFailure after the fact (layer-runtime:399). **Seam missing.** |
| 17 | Supervisor, node tick, `run <build>` | Runtime · dWellOiledMachine | a local process registered with the OS scheduler | the supervisor holds what `run` registered *on its node* (layer-runtime:346) | where it runs: nothing (host adapters). Being told what to run remotely: **seam** (rows 2 and 5) | — |
| 18 | Hosts: `run.host`, `kits.host`, `maintain.host`; cadence items | Runtime (`[schedule]`) | host adapters; a cadence lease keyed by period | — | nothing (open names; a late node skips a period another node already ran, layer-runtime:784-788) | — |
| 19 | Node identity (`fleet.toml`, AGENTS.md registry, `--claim-node`) and the node registry's runtime facts | distribution and Runtime · dWellOiledMachine (clause 15) | a tracked file | a static, committed list of 4 nodes. Runtime facts: binary, clock offset, cost class (layer-runtime:825-830) | **seam**: a node presence and capacity record kind (liveness, load, quota), keyed by fleet tag | `fleet.toml` fields are tag, user, host, projects_root and variances. Nothing dynamic. **Seam missing.** |
| 20 | Fleet register | distribution · dShippedRelease | `adopters.toml` | — | nothing: it registers *adopters*, not nodes (`layer-expansions.md:116`). The name collides with "fleet tag" | — |
| 21 | Derived SQLite index; `memory/LIVE.md` | memory core (`systems.md [cross]`); LIVE is a view "re-rendered, never merged" (`layer-memory.md:468`) | per-node SQLite; LIVE committed | consistency only after a merge and a pull | the index: nothing (derivable). A *live* cross-node view needs mirror reads of leases and cards, not LIVE | LIVE's "Node" column is the slug prefix, and it lists landed state only |
| 22 | Verdict and the peer-node verifier; `refs/gov/bar-red` | flow Test · dWitnessedBar (`verdict` open) | candidate ref, then a declared peer re-runs (`walkthrough.md:262-264`); bar-red read by the pre-push hook (`.githooks/pre-push:1907-1912`) | "a declared fleet node", static, which must be awake | the backend: nothing. Choosing the peer is a scheduling input (row 19) | bar-red is the one cross-node signal live today |
| 23 | Notifications and owner items | Runtime (`notify.channel` open) | an adapter | — | nothing | — |
| 24 | Integrations point | expansion, adapters at core points; "extension points declared: none" (`layer-expansions.md:325`) | — | — | nothing | — |
| 25 | Harness and auth (`runtime.act-harness` open; `runtime.act-auth` closed) | Runtime | an OS credential store per node | one operator per node | the account-usage seam from row 16. Terms belong to the platform researcher | — |
| 26 | The owner's session, owner controls, owner intake | flow (`life.request`, `flow-steps.md:579`) and Runtime (v2:1552 clause 27) | "the command's record"; mailbox `intake` "carrying the owner binding's proof" | the owner sits at a terminal on the lease holder's node: `tty-cli` proves presence locally (v2 `[witnesses]`) | **seam**: a cross-node control and intake path with an owner proof a relay can carry. The layered proof is only `[planned]` (v2:1585-1590) | No transport is named for a control issued on node d to reach node a's supervisor, and "owner binding's proof" is not defined. **Seam missing; ambiguous.** |
| 27 | Bindings (`refs/gov/bindings`) | Runtime · dWellOiledMachine (clause 39) | a ref | — | nothing | — |
| 28 | Journal and transcripts | Runtime | node-local, `not-local` elsewhere (P35) | — | nothing (journal-reader point) | — |
| 29 | Secret scan at publishing boundaries | Runtime (layer-runtime:866-872) | the lander's prepare and the ref-push path | git is the only publisher | **seam**: the mirror and a doorbell are new publishing boundaries, and neither is named a scan population | One line for the security researcher |

**Probe: which coordination keys accept a registered adapter.** A Python script read v2's catalogue rows 935-1200. Its output, abridged: only `run.host`, `kits.host`, `maintain.host`, `notify.channel`, `memory.mirror`, `verdict`, `runtime.act-harness` and `runtime.owner-harness` read "OPEN (registered name)". Every lease, `deps.*`, `mailbox.*`, `placement`, `card.store`, `landing.order`, `build.push`, `build.unit-holders`, `runtime.agents-in-flight`, `runtime.act-auth` and `verdict.held` row read `closed`. The script ran in `scratchpad/d148/`, now deleted.

## 2. Measured history

| What | Command | Measured |
|---|---|---|
| Shared refs on the remote | `git ls-remote origin 'refs/gov/*'` (0.633 s) | `17 refs/gov/runs`. No leases, mail, cards, decisions, problems, bindings or bar-red. |
| Claim shape | refs fetched into a scratch bare repo; `git rev-list --parents -n1` | All 17 are parentless, so the remote keeps no history (`gap-conc-06`). `node:` is a user name: `daily-agent` 14, `d41ly` 3 (`unattended.sh:2410`). Two hosts: compeeto-agent and compeeto. |
| Stale claims | beat ages at 2026-10-19 15:06Z | landed 8 · held 8 · live 1, with beats 145-301 h old. `aFrugalTurnstile` reads `live` with a 205 h beat. 8 of the 9 that are not landed name CLOSED builds (checked against each README's Build status). `aOrientedCast` reads held (beat 145 h) yet landed twice since. |
| Work with no claim | `git log origin/main --first-parent --since=2026-10-13T14:00` | 9 landing merges for aOrientedCast, aScoutedSeam, aSweptBar and dRenderedAnchor since the last claim. None of the last three ever had a claim; claims cover unattended runs only. |
| Landings by node | first-parent `merge: <slug>` since 09-15, by slug prefix | a 47, d 13, b 1, c 1 (the rest unprefixed) |
| Races at landing | first-parent subjects matching reconcile since 09-15 | 21 reconcile-related subjects, 18 of them merges. Cross-node: `aSparedHolder` with `dRemeasuredRender` (a×d, 10-11) and `dSweptBranches` with `cListedCensus` (d×c, 10-13). A version mint was redone "over the reconcile" (10-11). |
| Conflicts | merges in the last 30 days whose message lists `Conflicts:` | 8. Every conflicted file is a shared generated or guide file: `SESSION-KICKOFF.md` ×5, `.claude/skills/unattended/SKILL.md` ×2, `readme-contract.txt` ×2, dDerivedDocket README ×3. |
| Merge-only consistency cost | `git log --since=2026-09-19 -- memory/LIVE.md` | 331 commits in 30 days; 163 subjects naming reconcile or conflict |
| Lander window | `pushes.log` (node d only), full-bar durations | n=12; 133-630 s; median 334 s (288.7 and 379.8 s are the middle pair). For that long, no claim leaves the git dir. |
| Waits and abandonment | `research-stall-history.md` §1, rows re-read | Row 11: a weekly-limit wake loop, 115 entries over 4.8 days; no node took over, ended by a manual resume. Rows 13-14: an abandoned LANDING record blocked every run until the owner stopped it. Row 16: node a's pre-push hook refused every claim. Row 26: 23 of 23 HELD resumes were manual. Row 25: 37 aborts, 36 landed anyway. |
| Visibility | `ls .git/runlog` | The run logs, health log and stall logs exist on this node only, so node a's bars and stalls cannot be counted from here. |

No duplicated work turned up. Slug prefixes keep slugs unique: 173 builds and no collision after stripping the prefix. One orphaned-id case is recorded across nodes (`memory/gotchas/record-citing-a-foreign-id-defines-or-orphans-it.md:26`).

## 3. Which layer owns coordination, scheduling and load balancing

| Candidate home | Mechanism | Test that makes it lose | Result |
|---|---|---|---|
| **C1. Core Runtime** (the supervisor grows a fleet scheduler) | the per-node supervisor also assigns work across nodes | P28's sorting test (v2:637-639): is it needed to carry one build from request to landing on one offline node? Plus the `no-model-context` invariant (layer-runtime:899) | **Loses.** A per-node supervisor already carries a build alone, so a scheduler is not core. The invariant also rules out an agent head here. |
| **C2. Core Flow** (scheduling added to the coordination feature) | leases, mailbox and placement do the scheduling | Same P28 test; P5 limits the flow to leases, the mailbox and dependencies | **Loses for scheduling. Wins for the primitives**, which must stay (rows 1, 4, 5, 8, 9, 11, 12, 14). |
| **C3. Integrations alone** | the endpoint and head as adapters | Its contract: adapter kinds only (verdict, host, notification, deploy, verify), "extension points declared: none", records limited to remote-verdict, release, delivery and grant (`layer-expansions.md:313-326`). A head has its own programs, policies and records. | **Loses as the whole home. Wins as the home of the transports**: mirror, doorbell, cloud host. |
| **C4. Observability** | load monitoring plus the head | "read and filed but never deciding" (v2:648) | **Loses for the head. Wins for node-scoped readings** of load and quota (`maintain.node-readings`, the reading class with node scope). |
| **C5. A new expansion layer** (e.g. `scheduling`; avoid "fleet", taken twice) | owns the head, whether agentless or agent-driven, plus placement proposals and load balancing. It attaches only at core points (P28, EX-1), reads observability's readings as records, and uses integrations' transports | Does every point it needs exist in the core today? | **Wins only if the core declares the 7 missing points.** Present today: host adapters, the memory mirror, notification, cadence items, the change feed. Missing: rows 2, 5, 6, 13, 16, 19 and 26 (plus row 29's scan). |

**Recommendation:** C5, with the core keeping the truth and the expansion only proposing.

**What must stay in the core** so an offline node loses nothing:
- leases with their epoch and compare-and-swap on git, including the offline queue and yield-on-conflict;
- mailbox refs and the create-only registers;
- the change feed;
- the local verdict (P3);
- the per-node supervisor, admission queue and commit queue;
- the card ref and bindings.

**Points the core must declare now**, each with a core fallback so that P28 holds:
1. Lease discovery and take-over by a node that does not hold the lease. Fallback: today's behaviour.
2. A node- or project-addressed mailbox recipient. Fallback: build-addressed only.
3. A doorbell adapter point, with `deps.messaging` taking registered names. Fallback: the fetch interval.
4. A placement and offer source whose output is a `claimed` fact that `placement.check` re-derives (P23, P29). Fallback: `agent-places`.
5. A node presence and capacity record kind keyed by fleet tag. Fallback: none recorded.
6. An account usage reading for the admission queue. Fallback: StopFailure.
7. A cross-node owner control and intake path with a relayable owner proof. Fallback: the local terminal.

**The head may never** write a lease, position or verdict on a node's behalf. Each node acquires its own lease (P5, P22, P23), which preserves the offline guarantee.

**One-line pointers for the other researchers:**
- **Agentless head:** fits Runtime's `no-model-context` invariant only if it lives outside Runtime, as a C5 cadence program.
- **Agent-driven head:** under P25 and P26 it must be a role act reached through work orders, never a driver.
- **Headless shape:** that is rows 1-9 plus points 1-3 above.
- **Platform and security:** the account-shared plan limit under `oauth-shared`; the mirror and doorbell as unscanned publishing boundaries (row 29); the relayed owner proof (row 26).

No file in the repository was written, and no gate leg or test suite was run. The worktree's status is unchanged from the start. The scratch folder `.../scratchpad/d148/` was created for the claim fetch and the key probe, then deleted.

Main records read, under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`:
- `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `2026-10-14-build-PLAY-dClosedLoop-1-coordination.md`
- `2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`
- `2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`
- `2026-10-18-build-PLAY-dClosedLoop-1-memory-plan.md`
- `2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md`

Code read: `tools\unattended\unattended.sh`, `tools\unattended\resume-tick.sh`, `tools\run-gates\run-gates.sh`, `tools\push-main.sh`, `.githooks\pre-push`, `tools\playbook\fleet.toml`.
