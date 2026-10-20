# Research: the census of the design's cycles, retries, waits and holds

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 143's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-18-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-stall-and-loop.md`.

---

I read the records at `d56d7da4d` and today's tree for this census. I wrote nothing, ran no gate or test, and ran no probe beyond read-only `grep` and `sed`. Each finding below comes from reading a record clause or a line of code. No fixture was needed: a cycle's bound either has a clause or it does not.

**Record keys** (all under `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\`): V2 = `…-architecture-v2.md` · FS = `…-flow-steps.md` · RT = `…-layer-runtime.md` · LR = `…-layer-roles.md` · RO = `…-roles.md` · FR = `…-flow-roles.md` · FI = `…-flow-interactions.md` · CO = `…-coordination.md` · NP2 = `…-night-pass-two.md` · NP = `…-night-pass.md` · FRA = `…-flow-roles-adoption.md` · EX = `…-layer-expansions.md` · LL = `…-layer-library.md` · LM = `…-layer-memory.md`. Defaults are the `standard` preset's, with velocity/strict/guarded shown where they differ (V2 [presets] :1240–1407).

**Classes:** **B** = bounded, with a terminal outcome · **B→W** = bounded, but it ends in a wait nothing bounds (usually an owner item) · **U** = unbounded · **?** = the records leave the count or its home ambiguous.

## 1. Inventory

| id | where | what repeats or waits | bound, default | counted per | reset by | outcome at the bound | who notices | class |
|---|---|---|---|---|---|---|---|---|
| C1 | FS [rules] :37–39; V2 [policies] :1040 | **The general route-back rule:** any return to an earlier item, a review round included | `flow.route-backs` 3 (velocity 5, strict 2, guarded 3) | "in the build's transition record", "returns to the same item": read as per (build, target item), though per build is also readable | nothing stated. Each route back mints a new instance (RT [decide] :336–343). A scenario re-pick or a composition move doesn't say whether it carries the count | an owner item, "resolved as [breakpoint]'s owner gate is". Under the default `best-effort-recorded` that is "the supervisor's recorded choice" (FS :449–454). No record lists that choice for a route-back overflow, or says whether the counter re-arms | owner item; Loop Review's "route-backs per build" metric (V2 dCalibratedLens row) | B→W ? |
| C2 | FS [entry] :78; [plan] :126 | `entry.place` failed check → `entry.place`; `plan.dedupe` duplicate → `entry.place`; observation → `probe.trigger` → `entry.place` | `flow.route-backs` is in Entry's policy list (:93) | the count lives in the build's transition record (:37), and **no build exists before `entry.claim`** | — | none stated | journal | U ? |
| C3 | FS `entry.claim` :81 | slug claimed under another key → fresh slug; remote unreachable → claim queued (`leases.offline: warn`) | "within `flow.route-backs`" | same pre-claim gap as C2 | reconnection | claim queued until the remote returns | none stated | U ? (the wait for the remote has no ceiling) |
| C4 | FS :129–130, :180–181 | `plan.record` ↔ `plan.research`; `design.decompose` ↔ `design.research` ("back to the item that asked") | none stated. A research round trip isn't in RT's route-back list (:337–341) | — | — | — | — | U ? |
| C5 | FS [transitions] :622; NP2 [p1-scenarios] 2–3 | plan revision (designing → planning); scenario re-pick at a step boundary through a plan revision | C1, as a backward transition (RT :341) | per C1 | a re-picked scenario's preset slot can change `flow.route-backs` itself mid-build | per C1 | per C1 | B→W ? (the bound can change mid-build) |
| C6 | FS `design.ready` :186, `design.unit-spec` :183 | a unit not READY → its spec writer; a feature fork → decompose | C1 | per unit item | — | owner item | owner item | B→W |
| C7 | FS [design] :202–207, [open] S-1 :685–691; V2 :1036–1037, :1327–1328 | spec-audit rounds | `review.design.rounds` one (strict until-no-high, guarded until-no-blocker); `round-count` 2 under fixed-count, held below `RUNAWAY_CEILING`=8 (`tools/unattended/unattended.sh:774`, `:783`). The audit is opt-in under standard (V2 :1390), so 0 rounds by default | per spec subject | — | one / fixed-count: released. until-*: each round counts against C1 → owner item. Today's strictly-decreasing NON-CONVERGENT stop (`unattended.sh:12476–12477`) has no stated carrier for the until-* rules | owner item | B (one, fixed-count); B→W (until-*) |
| C8 | FS [build] :239–247, `review.dispose` :477; FR FR-9 :255–259; V2 :1019, :1313 | closing-review follow-up rounds after a HIGH; each round's findings become **new units** through Design and back | `review.follow-up` after-high (velocity never, strict while-finding). **No count in the item.** Only C1's "a review round included" might apply | if counted, per build's closing-review breakpoint; the new units' items start fresh counters | each round's new units | unstated. Today the diff review has a convergence predicate plus ceiling 8 (`unattended.sh:766–772`, `:12632`), and the promotion chain is "bounded by PRECISION" (`tools/memory-tree/BUILD-METHOD.template.md:144`). Neither is carried into the design | review report | U ? (at best B→W) |
| C9 | FS :483–485, :714–715 | `review.unverified: block` verification rounds; default `ask` files an ask | C1 under block; under ask, none | per C1 | — | block: owner item. ask: the ask waits in triage for "a review round confirms or refutes it" | owner item; ask register | B→W |
| C10 | FS `review.report` :476; LL :185–186 | `new:` slug claimed elsewhere → re-disposed; `owner-rules` none → owner item | "within `flow.route-backs`"; `review.unclassed: refuse` has an escape (file a `new:` class) | per C1 | — | owner item | owner item | B→W |
| C11 | FS `build.unit-pass` :229, `build.acceptance` :230, `build.scope` :231, `build.distill` :235, `test.seen-red` :293 | fix pass after failed acceptance; revert pass on a refused stray; divergence → spec writer or architect; an unclassed fork → its resolver; missing seen-red → fix pass | C1 | per unit item | — | owner item | owner item | B→W |
| C12 | FS `build.reuse-check` :232 | `duplicate`/`bypassed` → fix pass; disputed → closing review; overflow past 60 → a further pass over the remainder | "re-entries past `flow.route-backs` → the owner"; the overflow passes shrink and terminate | per unit | — | owner item | owner item | B→W |
| C13 | FS `build.core` :236 | own red → fix unit through Design → back | C1, as a backward transition; or excepted (`core.exceptions`) | per build | — | owner item | owner item | B→W |
| C14 | FS `build.ratify` :234; [breakpoint] :448–459; V2 :1304 | ratifications (`decisions.major: author-owner-ratifies`; `plan.ratification` other than request: strict terminal-command, guarded hook-keyword) | none: "a ratification `run.on-owner-question` never resolves" | — | — | held until the owner's disposition record | owner item | U (owner wait; not the default) |
| C15 | FS `test.merge` :287, `test.verdict` :289, `test.attribute` :291, `test.flakes` :292 | conflict → Build or architect; stale verdict → `test.merge`; red → fix pass or new unit; flake re-entries | C1 (`test.flakes` says so explicitly) | per C1 | — | owner item | owner item | B→W |
| C16 | FS `test.route` :290; V2 :1338 | a blocking CONTENDED red → "re-run on a quiet host" (it blocks only under guarded's own-mixed-contended) | none; "quiet host" is undefined | — | — | — | — | U |
| C17 | FS `test.select` :288, `test.flakes` :292; V2 :1049–1050 | a quarantined leg held until a threshold of consecutive greens, or a change to its manifest row | `verdict.flakes` quarantine. **The threshold has no default** ("a threshold"). `verdict.held: on-demand` means a held leg runs, and so earns greens, only on request | per leg | a manifest-row change | the held-flaky-leg ask stays open | ask | U (a loss of coverage, not a stalled build) |
| C18 | FS `deploy.current` :359, `deploy.land` :362; FI :137–138 | stale verdict → Test; landing race → Test; every landing stales the other builds' verdicts | C1, if a stale re-verify counts as a backward transition | per C1 | — | counted: a busy main sends a low-priority build to an owner item after 3. Uncounted: starvation with no bound | — | B→W or U ? |
| C19 | FS `deploy.land` :362, `deploy.core` :363 | remote unreachable → "the supervisor's retry, then an owner item"; REFUSED → one re-run; publication retried once; still running → waits within the act ceiling | retry count unstated; otherwise 1 re-run, 1 publication retry, 1.5 h | per landed SHA | — | owner item | owner item | B→W |
| C20 | FS `deploy.parents` :361; CO :126–133, :183–184; FI :134–136 | dependent's landing held until the parent lands; Build waits for `confirmed` interfaces; parent paused → holds | none. "Reachable" means the parent's lease is live, and a paused parent's lease is renewed (FS :583–584) | per dependent build | parent lands, is withdrawn (→ `deps.on-parent-withdrawn` replan) or superseded | holds | card | U |
| C21 | CO :130–131; FS [transitions] :625 | parent posts `changed` → dependent's interface-change re-entry | unstated whether an externally caused re-entry counts against the dependent's C1 | — | — | — | mailbox | U ? |
| C22 | CO :113–114 | "every transition … is refused while a message addressed to the build is neither answered nor acknowledged" | none | per build | an answer or ack | refused transition | card, `next` | U |
| C23 | FS [breakpoint] :448–464; V2 :1240, :1308 | owner gates: `autonomy` (strict every-stage), `attendance` confirm-steps or confirm-acts | default `best-effort-recorded` resolves non-ratification gates. Strict pairs every-stage with `park-item` | per gate | — | parked until the owner | owner item; notify (pushes nothing by default, FR :204–206) | B under defaults; U under strict |
| C24 | NP :538, :668 | the owner-item queue itself | NP-18 "Measure first": depth reported "with no bound" | repository | — | — | Loop Review | U (the owner's choice) |
| C25 | FS [probe] :501–502, :526–529, :551, :555–562 | a raised or placed probe; the asking item re-enters with the probe record; the role may raise again | `flow.route-backs` is in the probe's policy list, but no clause counts a re-entry; claimed or unrunnable → owner item; stand-ins → owner item | — | — | owner item | owner item | U ? |
| C26 | FS `probe.experiment` :526; V2 :1034 | experiment fan | `probe.experiment.authority` within-cap; one act ≤ 1.5 h | per experiment act | — | beyond authority → owner item | owner item | B |
| C27 | RT [spawn] :552–556; RO RL-7 :359–366, :382–384 | a failing return held with exit 2 and retried | `roles.retries` 3 (velocity 5, strict 1) | per return (item instance, task-sha, spawn site) | a new act or instance | persisted as a refusal and routed by the outcome table (→ C28) | journal | B (→ C28) |
| C28 | FS [rules] :29–31; RT :892, :505–506, :555–556 | a refusal "routes by default: … `next` returns the frontier, the unwitnessed items whose needs are witnessed", so the refused item is on the frontier again; also an agent outside the declaration "voids the act's witness, so the item re-runs", and a crashed SubagentStop leaves the item "re-dispatchable" | **none**. A refusal isn't in the route-back list (RT :337–341), and "an unwitnessed one can always be dispatched again" (RT :892) | — | — | — | journal | **U** |
| C29 | LR :290–313 | `roles.on-contradiction`: a second, differing repair → divergence to the producer; `return` → contradicted; `ask` → parks | C1 for the divergence | per fact | — | owner item / park | owner item | B→W |
| C30 | LR :226–232 | work order over budget → back to the producer of its largest input | C1 (memory slices never route back) | per C1 | — | owner item | owner item | B→W |
| C31 | RT [supervise] :388–394; `tools/unattended/resume-tick.sh:68–74`, `:121–122`; `tools/unattended/PROTOCOL.template.md:485–486` | act relaunch after death, a session limit or `--max-turns` exhausted | `RESUME_ATTEMPTS` 6; each launch capped at `RESUME_TURNS` 40 and `runtime.act-ceiling` 1.5 h (reaped, RT :448); the backoff between relaunches is unspecified | **design: "relaunches of one act"; code: CONSECUTIVE fruitless launches per run, reset by any move, a transcript-only move included** | code: any commit, write or transcript entry | the item parks with an owner item | journal, owner item | B→W (U under the code's reset) |
| C32 | RT :395–400 | session-limit hold until the parsed reset time | `runtime.hold-ceiling` 6 h → owner item "and keeps holding"; whether a limit relaunch spends a C31 attempt is unstated | per node | the limit's reset | owner item, the hold continues | owner item | B→W |
| C33 | RT :365–371, :464–465 | the node tick (every 10 min) restarts a crashed supervisor | none | per node | — | — | journal | U |
| C34 | RT [decide] :334 | `next` answers `invalid-input` | none: "refuses to act, and journals it", with no owner item | per beat | a fixed input | — | **journal only** | U |
| C35 | RT :331–333 | `stuck` / `blocked` | `stuck` → owner item at once; `blocked` → owner item once nothing it waits on is in flight | per build | — | holds | owner item | B→W |
| C36 | RT :330 | `awaiting` an event or record | only waits with a ceiling get one, from the sweep; for a hook item whose event never fires, none | per item | the event | holds, lease renewed | — | U (except C32, C37, C50) |
| C37 | RT :335 | `stale-remote` | holds and retries; parks after `leases.expiry-hours` 24 (guarded 12) | per build | a readable remote | parks | journal | B→W |
| C38 | CO :83–91; RT :330; FS :583–584 | lease expiry and take-over | 24 h unrenewed. **CO says it is renewed "at transitions and pass commits"; RT and FS have the supervisor renew it while awaiting or paused**, so a build that waits but still beats never expires | per lease | renewal | take-over, posted to the mailbox | mailbox | B, U for waiting builds (it blocks only under `leases: refuse`) |
| C39 | FS [lifecycle] :574–584 | owner pause | none; leases are kept and renewed | per build | resume | — | card | U (the owner's own control) |
| C40 | V2 dWellOiledMachine admission-queue clause; RT :428–445; NP2 :532–534 | admission queue for spawns and Workflow calls over `runtime.agents-in-flight` 6 | **no wait ceiling**; FIFO. A slot frees at SubagentStop, the run's saved result or the liveness sweep. A hung agent in a live owner session keeps its slot, since the act ceiling covers act sessions only (RT :758–759). Before the queue lands, a direct spawn over the limit is refused | per session or node | a freed slot | waits | "a notice naming the wait" | U |
| C41 | RT [sessions] :740–759; V2 :1021–1022, :968–969 | owner-session restart at 60% context (fresh-at-boundary); `resume.partial` continue-item; PreCompact flush | ends at an item boundary, so at least one item per session; act sessions are bounded by max-turns | — | — | — | — | B (by construction) |
| C42 | NP2 :109–113; V2 :1043, :1334 | `flow.adapt`: additive changes applied at each step boundary; removals, reorders and loosenings wait for the owner while the build carries on | **no cap on changes per build.** "Stricter values" has no declared direction for loop counts (`flow.route-backs`, `review.design.rounds`, `roles.retries`); FRA :213–217 declares a widening direction for row fields only | per build | — | the owner-wait never blocks the build | build folder, order | U ? |
| C43 | NP2 :120–121; V2 :1042 | `flow.scenario-conflict: refuse` → wait for the owner to order | none | per build | owner ordering | waits | owner | U |
| C44 | FRA :221–222, :253–255; FS :607, :639–641 | repository item routes; a build moving to a new composition at its next step boundary (FA-7) | the composition checks that `needs` is acyclic and that routes join the build table. **Nothing checks that a cycle of repository item routes passes a counted route back** (the item-level tables are owed, `gap-flow-15`). Whether the C1 count carries across a move is unstated | — | — | — | — | U ? |
| C45 | FRA :235–246; V2 :1029, :1320, :1074, :1364–1365 | `instructions.stale` re-applies a patch at each update; under `refuse` the update is held until the owner re-pins | order: re-applied at each update, and no dedupe key is stated for the orders. Strict pairs `refuse` with `currency.on-behind: red` and max-behind 1, so the currency leg reds **every landing** until the owner re-pins | per row, per update | owner re-pin | held update / red landings | order, currency leg | B→W; U under strict |
| C46 | EX :222–225 | Maintain re-filing; dead probe; patch | asks keyed (reading, offender) with `seen` rows; dead after `maintain.dead-after` 10; a patch intake keyed (reading, offender). **If the patch lands and the reading stays over its pin, either `entry.claim`'s idempotent key (FS :81) swallows the second patch or a new build is minted each period**, and the records don't say which | per (reading, offender) | — | ask in triage | ask | B (asks); U ? (patches) |
| C47 | EX :259–263; NP2 :426–427 | Loop Review proposals; persisting cap breach | one ask per (ledger kind, id), a weekly `seen` row, re-proposed `review.loop.window-days` 60 after a keep; owner item only for a new or grown breach | per ledger row | a keep record | owner breakpoint | owner item | B→W |
| C48 | FS `deploy.core` :363, `deploy.distill` :365, landing review :414–415 | patch-build chains: a post-landing red, missing rows, or landing-review findings → a patch build, which may itself red or find again | **none**; every new build starts fresh C1 counters | per build | a new build | — | landing record | **U** |
| C49 | EX :385–387 | `release.promote` refused or unreachable → retry → owner item resolvable as "retry again"; verify dead probe → owner item "verify again" | retry count unstated; `best-effort-recorded` may keep choosing retry | per (SHA, environment) | — | owner item | owner item | U ? |
| C50 | FS `deploy.released` :368; RT :452–456 | release hold under `after-release-verifies` | `build.release-ceiling` 72 h (velocity 24, strict 168) → owner item; a keep-waiting answer restarts the ceiling | per (build, landed SHA) | keep-waiting | repeats every 72 h | owner item | B per cycle, U in cycles |
| C51 | RT :784–792 | event-wait wake per exit record | one wake per record and waiting build | per (event, record, build) | — | — | — | B |
| C52 | RT :606–612; `tools/unattended/stop-guard.js:53–58`, `:92–94`, `:153`; `tools/hooks/format-guard.js:62–64`, `:469`; `tools/unattended/stall-recorder.js:11–15` | Stop-hook blocks and the stall record (today's tree) | stop-guard: 6 lifetime blocks under a harness cap of 8 consecutive; format-guard: once per turn end; stall-recorder records and "CANNOT BLOCK". Design: stop-guard retired for act sessions, format-guard kept, stall-recorder becomes the limit signal | per session | — | allowed | sidecar or journal | B |
| C53 | RT [act] :510–513 with C31 | a hook refusal inside an act: the agent retries the refused call | `RESUME_TURNS` 40 and 1.5 h per launch, then C31 | per launch | — | act ends → C31, or a refusal return → C28 | journal | B per launch; U through C28 |
| C54 | FS `test.route` :290; CO :122–125 | red leg re-run once; mail fetch bounded by a timeout; detached fetch every 60 s | 1 re-run; timeout | — | — | — | — | B |

## 2. Worst-case arithmetic for one feature

**Inputs (standard defaults):**
- R = `flow.route-backs` 3, so 1+R = 4 instances of a looping item.
- `review.follow-up` after-high: 1+R = 4 closing-review rounds if C1 counts follow-ups, otherwise unbounded.
- r = `roles.retries` 3, so 4 attempts per return.
- A = `RESUME_ATTEMPTS` 6 launches per act; T = `RESUME_TURNS` 40 turns per launch; `runtime.act-ceiling` 1.5 h per launch.
- The spec audit is opt-in, so 0 design rounds.

**Per item instance:** ≤ 6 launches, ≤ 240 turns, ≤ 9 h of act time, plus an unspecified backoff.

**Per looping item, reading C1 per (build, item):** ≤ 4 instances, so ≤ 24 act sessions, ≤ 960 turns and ≤ 36 h, and ≤ 4 × 6 × 4 = 96 return attempts per spawn site.

**The requested product:** route-backs (4) × closing-review rounds (4, if counted) × role retries (4) × resume attempts (6) = **384** return attempts per spawn site along one chain before any owner item.
- Reading C1 per build in total (R = 3 for the whole build): 4 × 4 × 6 = 96.
- velocity: 6 × 1 × 6 × 6 = 216.
- strict: 3 × 3 × 2 × 6 = 108, with design rounds until-no-high also inside R. Under strict, every stage exit is also an owner gate under `park-item` (C23), a wait with no bound.

**Instantiated, U = 3 units, per (build, item):**
- Route-back targets: 7 that aren't per unit (`entry.place`, `plan.record`, `design.decompose`, the closing review, `test.merge`, `test.verdict`, `test.select`) plus 3 per unit (`design.unit-spec`, `build.unit-pass`, `build.reuse-check`), so L = 16.
- That allows ≤ 16 × 3 = 48 route backs with no owner item, so long as none returns to the same item more than 3 times.
- Each route back re-runs its whole downstream path as new instances. That re-execution is forward work, not a route back, so nothing counts it.
- Act time on the target items alone: ≤ 16 × 36 h = **576 act-hours**.
- Each closing-review round's findings mint new units with fresh counters (C8). With 2 findings per round over 4 rounds, that is +8 units and +24 items, so ≤ 40 × 36 h = **1,440 act-hours** before the build reaches Test's exit.
- `runtime.agents-in-flight` (6) only throttles how many run at once; it limits nothing in total.

**Wall time the ceilings allow:** 1.5 h per act session; 6 h of session-limit hold before an owner item, after which the hold continues (C32); 24 h of stale remote before a park (C37); 72 h per release-hold cycle, repeating (C50). Nothing else carries a ceiling.

**Products with no ceiling at all:**
- builds in a patch chain (C48)
- re-dispatches after a refusal, a voided witness or a crashed SubagentStop (C28)
- supervisor restarts (C33) and `invalid-input` beats (C34)
- closing-review rounds, if follow-ups are uncounted (C8)
- research round trips (C4) and probe re-entries (C25)
- entry-stage loops before the claim (C2, C3)
- `flow.adapt` changes (C42)
- release retries (C49) and release-hold cycles (C50)
- every wait without a ceiling (C20, C22, C24, C36, C39, C40, C43, C45 under strict, C17)

## 3. Unbounded, each with the clause that leaves it unbounded

1. **C28 refusal re-dispatch:** "A refusal routes by default: it is recorded, and `next` returns the frontier, the unwitnessed items whose needs are witnessed" (FS :29–31). Also "an unwitnessed one can always be dispatched again" (RT :892) and "voids the act's witness, so the item re-runs" (RT :505–506). A refusal isn't among the routes back that mint and count (RT :337–341).
2. **C48 patch-build chains:** "red → a patch build through the entry-point table's post-close row" (FS :363), and the landing review's "findings enter as patch builds" (FS :414–415). C1's count lives in each build's own transition record (FS :37), so every new build starts at zero.
3. **C8 follow-up rounds:** "a follow-up round runs after a HIGH finding (`review.follow-up`)" (FS :244), with no count. Its findings "become new units" (FS :242), and new items have fresh counters. Today's two bounds, the convergence predicate (`unattended.sh:12473–12481`) and the precision rule for promotion chains (`BUILD-METHOD.template.md:144`), have no carrier in the design.
4. **C2/C3 before the claim:** the count "counts in the build's transition record" (FS :37–38), and no build exists before `entry.claim` (FS :81).
5. **C4 research round trips:** "back to the item that asked" (FS :181), and `plan.research` → `plan.record` (FS :130), with no count stated.
6. **C25 probe re-entry:** "the probe's record returns as its input on re-entry" (FS :502), with no count stated.
7. **C33 supervisor restarts:** the node tick "restarts it after a crash or a reboot" (RT :367–368), with no cap.
8. **C34 `invalid-input`:** "refuses to act, and journals it" (RT :334). No owner item and no ceiling.
9. **C36 awaits without a ceiling:** "It raises no owner item itself: a wait with a ceiling is raised by the supervisor's sweep" (RT :330). Only C32, C37 and C50 have one.
10. **C20 parent holds:** "a parent unlanded or paused → holds" (FS :361). "Live means reachable … there is no separate timeout" (CO :183–184). A paused parent's lease is renewed (FS :583–584).
11. **C22 mailbox disposal:** "refused while a message addressed to the build is neither answered nor acknowledged" (CO :113–114).
12. **C40 admission queue:** "never refused for want of a slot", with no wait ceiling (V2, dWellOiledMachine row). The act ceiling doesn't cover the owner's session (RT :758–759).
13. **C16 CONTENDED re-run:** "a blocking CONTENDED red → a re-run on a quiet host" (FS :290), with no count and no definition of "quiet host".
14. **C17 quarantine:** released only after "the threshold … of consecutive greens since its hold" (FS :288). The threshold has no default (V2 :1050), and under `verdict.held: on-demand` (V2 :1049) a held leg runs only on request.
15. **C42 `flow.adapt`:** "a change that only adds … applies unattended at the next step boundary" (NP2 :109–111). No per-build cap, and no stated direction for whether raising a loop count is "stricter".
16. **C44 repository routes:** the checks cover "the needs graph acyclic … every route joined to its level's transition table" (FRA :221–222), not route cycles. The item-level tables are owed (FS :607).
17. **C49 release retries:** "retry, then an owner item, resolved as `run.on-owner-question` says: retry again" (EX :385).
18. **C1 (and every B→W row) after the bound:** the owner item is resolved by "the supervisor's recorded choice" (FS :454). No record lists that choice for a route-back overflow, or says whether the counter re-arms. A supervisor holds no model context (RT :894), so "best effort" has no stated actor here.
19. **Owner waits:** C14 ratifications ("never resolves", FS :234), C23 strict gates under `park-item`, C24 the owner queue ("with no bound", NP :538), C39 pause, C43 scenario conflict, C45 under strict, C50 cycles.

## Where a record and the code disagree, or records disagree

- **`RESUME_ATTEMPTS`:** RT :393 caps "relaunches of one act". The code caps "CONSECUTIVE fruitless launches per run" and resets on "a commit, a write or a transcript entry" (`tools/unattended/resume-tick.sh:68–74`; `PROTOCOL.template.md:485`). Carrying the code's semantics forward would make C31 unbounded for an act that keeps writing to its transcript.
- **Lease renewal:** CO :86 says "Renewed at transitions and pass commits". RT :330 and FS :583–584 have the supervisor renew the lease while a build waits or is paused (C38).
- **`RUNAWAY_CEILING`:** today it backstops the closing diff review (`unattended.sh:12632`: `bound=$RUNAWAY_CEILING` for the build slug). V2 :1037 binds it only to `review.design.round-count`, so the closing review loses that backstop.

## Belongs to the other researchers, one line each

- Refusal census: which hook refusals an agent cannot satisfy, which C53 and C28 then feed.
- Concrete stall scenarios: the chained cases C18 + C48, and C45 under strict.
- Measured history: today's CEILING and NON-CONVERGENT exits in `tools/runlog/model.py:110`.
- Prior art: how other systems bound retries and re-dispatch.
