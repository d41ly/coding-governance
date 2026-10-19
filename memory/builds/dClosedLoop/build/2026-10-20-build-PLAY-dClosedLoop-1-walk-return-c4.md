# Walk return: run C, walker 4, dWellOiledMachine and dWitnessedBar

**Serves:** research PLAY-dClosedLoop-1

Dispatch 188's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-29-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed because one of these clauses retires the node tick that hosts the supervisor, refuses every bash on a Linux node, or loads a 31 KB map through a hook channel that keeps 10,000 characters. In each case a build stalls or loses its context, and nothing goes red.

### C4-F1 — The unattended-kit dissolve retires the supervisor's own seam and removes the tick that hosts it
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0306
- **Class:** K10 (a migration across a drain), c2
- **Severity:** high
- **Evidence:**
  - 0306 says "`resume-tick.sh` and the `RESUME_SCHEDULE_*` task retired with an adopter's hand-registered resume task removed".
  - 0284 says the opposite: "the supervisor: `resume-tick.sh` grown, started and restarted by the node tick".
  - layer-runtime `[supervise]` gives the supervisor's host: "The OS-scheduled `gov-resume-tick` registration runs every 10 minutes … starts the supervisor … Preflight refuses a node that declares itself a run host without that registration". It retires only "The desktop durable-restart task (`RESUME_SCHEDULE_*`)".
  - fates rows 145–146 mark `resume-tick.sh` "RESHAPED | the supervisor" and `RESUME_SCHEDULE_*` "RETIRED".
  - night-pass `[p1-unattended]` names "`resume-tick.sh` as the supervisor's seam".
  - Probe: `grep -n 'gov-resume-tick' tools/unattended/README.md` printed `211:schtasks /create /sc minute /mo 10 /tn gov-resume-tick … resume-tick.sh --repo <root>` and `218:*/10 * * * * <kit-dir>/resume-tick.sh … # gov-resume-tick`. So the adopter's hand-registered resume task is the node tick itself.
- **Consequence:** the upgrade step deletes the supervisor's script and the node tick that starts and restarts it.
  - Every run host then fails preflight, and the `host` fixture cannot pass.
  - A crashed or rebooted supervisor never comes back, so unattended builds stop short of a terminal.
- **Fix:** in 0306, retire only `RESUME_SCHEDULE_*` and resume-tick's `--dangerously-skip-permissions` launch, and keep `resume-tick.sh` as the supervisor's seam (0284). Keep the `gov-resume-tick` registration as the node tick, re-pointed rather than removed.

### C4-F2 — The shared bash resolver accepts only MINGW or MSYS, which refuses every bash on Linux
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0364
- **Class:** K10 (a trust boundary and portability), c1
- **Severity:** high
- **Evidence:**
  - 0364 replaces "every resolver and bare-bash launch site", "a candidate accepted only once it runs and answers `uname -s` as MINGW or MSYS … and a refusal in place of any fall-back". It also says the resolver keeps the existing contracts ("whose contracts it keeps").
  - away-pass `[p4-compat]` settles "a declared platform matrix, Windows with Git-Bash and Linux at tier 1".
  - 0315 itself plans for "libsecret on a Linux desktop" and "a headless Linux node".
  - The existing contracts are not MINGW checks. `tools/govkit/govkit.py:1138` accepts a candidate that runs `-c :`, and `tools/run-gates/profile_bar.py:282` accepts one that can `test -f "$1"` the script.
- **Consequence:** on any Linux node, `uname -s` prints `Linux`, so every gov launch site refuses. The bar, the hooks and the lander cannot run there, so builds cannot land from a tier-1 platform.
- **Fix:** scope the MINGW/MSYS acceptance to a Windows host (`os.name == 'nt'`). Elsewhere, accept a candidate that runs and meets the bash floor, and add a Linux arm to the staged-break fixture.

### C4-F3 — The default load is replayed through a hook channel smaller than the map, and no clause carries the owed cap measurement
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0301 (also cl-dClosedLoop-0290)
- **Class:** K10
- **Severity:** high
- **Evidence:**
  - 0301 says "the session-start hook loading the set `memory.default-load` names, the card and the map by default … at a compaction".
  - night-pass-two `[p5-caps]` says "The harness keeps 10,000 characters of hook context … past them text is silently lost".
  - v2 `[owed]` gives the level-0 map's headroom as "31,203 of 32,768 B". The same `[owed]` lists "the compact and resume hooks' output cap, measured with a 32 KiB map, so the default load comes back whole (point 5)", and night-pass `[p5-compaction]` item 4 says the same.
  - layer-runtime `[build]` unit 9 lists "the card's size check", and `[sessions]` says "a size check holds the card under it". Neither 0290 nor 0301 carries the size check.
- **Consequence:** after a compaction, the map is truncated at about a third of its size, and nothing reports it. The fix that gap-orient-18 owns ships without restoring the map, and the session works from a partial map it does not know is partial.
- **Fix:** add to 0301 the owed measurement of the hook channel's cap against the 32 KiB map. Add a size check that sends the over-cap remainder through an instruction-file channel, or fails red, before the clause closes. Add the card's size check to 0290.

### C4-F4 — The settling row names an orientation scout as `entry.intake`'s actor, though 0282 builds it as a hook
- **Address:** flow-steps `[entry]` `entry.intake` row, against architecture-v2 [chain] cl-dClosedLoop-0282
- **Class:** K1
- **Severity:** medium
- **Evidence:**
  - The flow-steps `entry.intake` row reads "Actor: orientation scout, in an owner-bound session only … Proven by: the intake entry the scout writes".
  - The same record's amendment row `hook-actor-kind` says "`entry.intake` is a hook". Its own Owner note calls it "`entry.intake`'s hook".
  - layer-roles line 414 lists it as "| hook | `entry.intake` |".
  - 0282 builds "the prompt-submit hook writing each owner prompt verbatim".
- **Consequence:**
  - The item join and the owner check will read a scout, an agent, as the writer of the intake record.
  - That record is "the mandate to land" (gap-rt-14), so the owner's verbatim mandate would be agent-typed.
  - A builder of 0282 or of `entry.orient` meets two contradictory actors.
- **Fix:** set the flow-steps row's actor to "hook: prompt-submit, owner-bound sessions only", and its witness to "the intake entry the hook writes".

### C4-F5 — The session-limit hold hands the lease over without the owner item the settling records require
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0325
- **Class:** K10
- **Severity:** medium
- **Evidence:**
  - 0325 says "the session-limit hold releasing the build's lease as a hand-over at `runtime.hold-ceiling` so a node with quota takes the build over and the wake tick stops". Its red cases are "the lease still held or the tick firing again past the ceiling, a hand-over no second node takes".
  - The v2 catalogue's `runtime.hold-ceiling` row says "past it an owner item is raised and the build's lease released".
  - layer-runtime `[supervise]` says "the supervisor raises an owner item and releases the build's lease as a hand-over".
  - layer-runtime `[tests]` `limits` says "it raises an owner item and releases the lease".
- **Consequence:** when no node with quota exists, which is the "hand-over no second node takes" case, the build sits released and nobody is told.
- **Fix:** add to 0325 "and raises an owner item", with a red arm on a ceiling passed and no owner item.

### C4-F6 — The no-progress and repeat detectors arm as blocking with no false-positive measurement first
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0324
- **Class:** K10
- **Severity:** medium
- **Evidence:**
  - stall-and-loop `[owed]` says "The no-progress and repeat detectors' false positives measured on gov's own run logs before either blocks (dWellOiledMachine)".
  - 0324 builds both detectors ("`runtime.no-progress` acts with no new witness making the item stuck … journaled by the loop detector") but has no measurement step and no gate on arming.
- **Consequence:** an untested detector can mark healthy items stuck and route them, spending the build's rework budget until it is exhausted, with no check that could show the error.
- **Fix:** add to 0324 the replay over gov's recorded run logs, and keep the detectors journal-only until its false-positive rate is recorded.

### C4-F7 — Lease expiry by "tip unchanged" cannot fire while the fenced pushes keep moving the tip
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0324 (with cl-dClosedLoop-0284 and cl-dClosedLoop-0293)
- **Class:** K10 (a race across nodes)
- **Severity:** medium
- **Evidence:**
  - 0324's red case is "a planted holder that loops while active, its lease lost after `leases.expiry-hours`". The `renewal` fixture plants a holder "whose acts write commits".
  - The catalogue's `leases.expiry-hours` row says "an observer seeing the tip unchanged this long".
  - cloud-and-scale `[design]` 2 says "Every effect push, a pass push … carries the holder's new lease beat".
  - `build.push` defaults to every-pass (0318).
  - 0284 says "its liveness its build lease's beat".
- **Consequence:** a looping holder that commits pushes a new lease beat at every pass, so the observer never sees the tip unchanged. The lease never expires, and the P39 arm cannot go red as specified.
- **Fix:** in 0324 (and 0293), state that expiry reads the last progress-renewal stamp carried in the lease record, never the tip's movement. Add an arm in which a committing, witness-free holder loses its lease.

### C4-F8 — Five of dWellOiledMachine's own runtime keys are read by no clause, two of them guard-bearing
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0288 (also cl-dClosedLoop-0279, cl-dClosedLoop-0284, cl-dClosedLoop-0295)
- **Class:** K4
- **Severity:** medium
- **Evidence:**
  - Stage 0's K4 lists "runtime.attended-allowance … (guard-bearing)", "runtime.hook-failure", "runtime.relaunch", "runtime.secret-scan … (guard-bearing)" and "runtime.spawn-backend: read by no chain clause and no item". The v2 catalogue gives each owner as dWellOiledMachine.
  - 0288 says "`onFailure` written on every entry" and "as `runtime.attended-judge` says", but never names `runtime.hook-failure`'s `open` value ("Under `open`, the class check reports the policy in force", `[invariants]`) or `runtime.attended-allowance`.
  - 0279's spike decides the backend but never names `runtime.spawn-backend`. 0284 says "relaunch capped" without `runtime.relaunch`. 0295 says "the secret value scan" without `runtime.secret-scan`'s two values.
- **Consequence:**
  - Under `attended-judge: allowance` the dispatcher has no allowance to read.
  - `hook-failure: open`, `relaunch: resume` and `secret-scan: value-gate` are dead values.
  - The `coverage` fixture's "every `runtime.*` key … has a reader" goes red with no clause owning the read.
- **Fix:** name each key in its clause: `runtime.spawn-backend` in 0279, `runtime.relaunch` in 0284, `runtime.hook-failure` (both values) and `runtime.attended-allowance` in 0288, and `runtime.secret-scan` in 0295. Give each value an arm.

### C4-F9 — Three remote-verdict gaps and their keys sit on dWitnessedBar with no clause to build them
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0344 (also cl-dClosedLoop-0342, cl-dClosedLoop-0347, cl-dClosedLoop-0352)
- **Class:** K4
- **Severity:** medium
- **Evidence:**
  - The dWitnessedBar row owns `gap-test-11` ("A remote verdict certifies itself"), `gap-test-12` and `gap-test-13`.
  - The catalogue owner is dWitnessedBar for `verdict`, `verdict.remote.trust`, `verdict.remote.pin` and `verdict.remote.pin-scope`.
  - Stage 0's K4 lists all four, plus `tests.product` (guard-bearing), as "read by no chain clause and no item". `retrofit.widen` is listed the same way, with dWitnessedBar as its owner.
  - layer-expansions sets the rule: "A remote verdict stands as a witness only when … the pinned files at `head_sha` equal the pin". None of 0339–0368 names a pin, a backend registry, the held-CI reader's adapter, `tests.product` or a widen record.
- **Consequence:** a remote verdict can be built with no source check, so a pusher's workflow edit certifies itself (c3 once `verdict: remote-ci` is selected). `tests.product` and `retrofit.widen` have no reader, and gap-test-12 and gap-test-13 close with nothing built.
- **Fix:**
  - Add a clause to dWitnessedBar for the verdict-backend registry under `verdict`, and the remote verdict's source check under `verdict.remote.*`, seen red on a swapped workflow.
  - Name the held-CI reader's adapter registration.
  - Name `tests.product` in 0347 and `retrofit.widen` in 0352.

### C4-F10 — No clause builds the runner's same-tree re-run, so a flaky leg never reaches `test.flakes`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0346
- **Class:** K2
- **Severity:** medium
- **Evidence:**
  - flow-steps `[test]` says "`test.route`'s re-run of a red leg on the same tree is a runner mode dWitnessedBar owes (`gap-test-04`), with its probe … Today the bar retries only timeouts".
  - 0346 says only "flake quarantine", and 0368 covers release and the quiet host. No clause names the same-tree re-run mode or its probe.
- **Consequence:** `test.route` cannot tell a nondeterministic red from a real one. Flaky reds route to `test.attribute` as OWN reds, and the quarantine never receives a leg.
- **Fix:** add to 0346 "the runner's mode re-running a red leg once on the same tree under `test.verdict`'s env, seen on a fixture leg that reds then greens reaching `test.flakes`".

### C4-F11 — The card's retirement re-points an incomplete list of readers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0316
- **Class:** K10 (a retirement by value)
- **Severity:** medium
- **Evidence:**
  - 0316 re-points the write gate, `readCard`, `extractRouteUnits`, the route notice and `manifest-check.sh --card --write`, "with `check-wiring.test.sh` and `format-guard.test.sh`".
  - Probe: `grep -rn "orientation/" tools skills .githooks` also printed `tools/hooks/scratch-guard.test.sh:537` (it plants an absent-card case under `orientation/`). It printed `skills/session-kickoff/manifest-check.test.sh:861,895,917,960,1008…` (asserting "the card is at <common-dir>/orientation/<sid>.md").
  - `grep -rln orientation …` lists `skills/session-kickoff/orientation-card.fragment.json` and `orientation-replay.fragment.json`.
- **Consequence:** these tests and the wiring fragments still assert the retired card path. Either the unit lands red, or the tests are edited to pass and stop checking the binding.
- **Fix:** inventory the readers by value in 0316: add `scratch-guard.test.sh`, `manifest-check.test.sh` and the two `orientation-*.fragment.json` files, each re-pointed in the same unit.

### C4-F12 — The portability pack moves in a "shell-hygiene mode" that `encoding_posture.py` does not have
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0362
- **Class:** K6
- **Severity:** medium
- **Evidence:**
  - 0362 says "the last moved in from gate-lint's `encoding_posture.py` with its shell-hygiene mode".
  - Probe: the argv rows in `tools/gate-legs.json` show shell hygiene as a separate script, `["python3","{prefix}/gate-lint/sh_hygiene.py",…]`, three legs plus `--selftest`. Encoding posture is `encoding_posture.py memory/project/encoding-posture-sites.txt …`.
  - `grep -n shell tools/gate-lint/encoding_posture.py` finds no mode.
  - research-compatibility §4 puts P-launch's legs in the "`shell hygiene` spawn-idioms and loop legs".
- **Consequence:** a builder either looks for a mode that does not exist or leaves `sh_hygiene.py` in gate-lint. Then P-launch has no core leg, though the clause claims "every P37 rule has a core leg".
- **Fix:** read "moved in from gate-lint's `encoding_posture.py`, with `sh_hygiene.py`'s legs beside it".

### C4-F13 — The event-wait sweep and the atomic landing rely on dShippedRelease items that no ancestor lands
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0296 (also cl-dClosedLoop-0337)
- **Class:** K6
- **Severity:** medium
- **Evidence:**
  - 0296 says "the sweep that raises a wait past `build.release-ceiling` once, under the release hold's one key". 0337 says "the build's release with its landed notice carried in one atomic push".
  - The catalogue's `build.release-ceiling` row says "how long `deploy.released` waits for an exit record".
  - flow-steps gives `deploy.released`, `deploy.notify`, `deploy.unlease` and `deploy.close` the owner "dShippedRelease".
  - The design map gives dShippedRelease as "after=…dWellOiledMachine…".
  - Stage 0's K2 already shows "dWellOiledMachine→deploy.released: … not an ancestor, UNCLASSED".
  - layer-runtime's `event-wait` and `lifecycle` fixtures run those items.
- **Consequence:** the sweep and fixtures cannot run when dWellOiledMachine lands, so its arms are either never seen red or are built against items that do not exist yet.
- **Fix:** have 0296 and 0337 name a stand-in release slot and notice, with the same contract and owned by this build, until dShippedRelease lands. Alternatively, move the fixtures' release arms to dShippedRelease.

| clause | build | read against | verdict |
|---|---|---|---|
| cl-dClosedLoop-0279 | dWellOiledMachine | layer-runtime [tests] spike, [spawn]; catalogue runtime.spawn-backend; stall-and-loop [owed] | C4-F8 |
| cl-dClosedLoop-0280 | dWellOiledMachine | layer-runtime [build] unit 2; v2 [owed] `next` row; gap-found-06 | holds |
| cl-dClosedLoop-0281 | dWellOiledMachine | flow-steps [lifecycle]; night-pass [p1]; catalogue attendance.scope; cloud-and-scale [design] 3 | holds |
| cl-dClosedLoop-0282 | dWellOiledMachine | flow-steps [entry] entry.intake; layer-roles hook row; gap-rt-14 | C4-F4 |
| cl-dClosedLoop-0283 | dWellOiledMachine | research-harness-cli dWellOiledMachine row (DA-M14); layer-runtime [harness] | holds |
| cl-dClosedLoop-0284 | dWellOiledMachine | layer-runtime [supervise], [build] unit 3; fates rows 145-146; catalogue runtime.relaunch | C4-F1, C4-F7, C4-F8 |
| cl-dClosedLoop-0285 | dWellOiledMachine | layer-runtime [act] binding, [enforce] | holds |
| cl-dClosedLoop-0286 | dWellOiledMachine | layer-runtime [spawn] returns and deferral | holds |
| cl-dClosedLoop-0287 | dWellOiledMachine | layer-runtime [supervise] agents in flight; catalogue runtime.agents-in-flight | holds |
| cl-dClosedLoop-0288 | dWellOiledMachine | layer-runtime [enforce], [invariants] fail-closed; catalogue runtime.hook-failure, runtime.attended-allowance; Stage 0 K4 | C4-F8 |
| cl-dClosedLoop-0289 | dWellOiledMachine | layer-runtime [isolate]; catalogue build.worktree; gap-conc-03 | holds |
| cl-dClosedLoop-0290 | dWellOiledMachine | layer-runtime [sessions], [build] unit 9; night-pass [p5]; gap-orient-12/14 | C4-F3 |
| cl-dClosedLoop-0291 | dWellOiledMachine | layer-runtime [schedule] | holds |
| cl-dClosedLoop-0292 | dWellOiledMachine | layer-runtime [harness]; gap-rt-19 | holds |
| cl-dClosedLoop-0293 | dWellOiledMachine | catalogue leases.expiry-hours; cloud-and-scale [design] 4; layer-runtime [harness] | C4-F7 |
| cl-dClosedLoop-0294 | dWellOiledMachine | layer-runtime [schedule] retention; catalogue runtime.journal; gap-rt-16 | holds |
| cl-dClosedLoop-0295 | dWellOiledMachine | layer-runtime [extend] grant and secret scan; catalogue runtime.secret-scan | C4-F8 |
| cl-dClosedLoop-0296 | dWellOiledMachine | layer-runtime [schedule], [supervise]; catalogue build.release-ceiling; flow-steps [deploy] owners; Stage 0 K2 | C4-F13 |
| cl-dClosedLoop-0297 | dWellOiledMachine | v2 system.role-shapes; layer-runtime [act] | holds |
| cl-dClosedLoop-0298 | dWellOiledMachine | v2 system.tags; gap-rt-13 | holds |
| cl-dClosedLoop-0299 | dWellOiledMachine | gap-rt-13, gap-rt-20 | holds |
| cl-dClosedLoop-0300 | dWellOiledMachine | gap-rt-13; v2 system.tags | holds |
| cl-dClosedLoop-0301 | dWellOiledMachine | night-pass [p5]; night-pass-two [p5-caps]; v2 [owed] map headroom; catalogue memory.default-load | C4-F3 |
| cl-dClosedLoop-0302 | dWellOiledMachine | v2 system.project-map; gap-orient-18 | holds |
| cl-dClosedLoop-0303 | dWellOiledMachine | night-pass [p1] item 3; v2 [owed] spike row; P25 | holds |
| cl-dClosedLoop-0304 | dWellOiledMachine | night-pass [p1] item 4; P4; gap-orient-16 | holds |
| cl-dClosedLoop-0305 | dWellOiledMachine | night-pass [p1] item 5; gap-orient-17 | holds |
| cl-dClosedLoop-0306 | dWellOiledMachine | layer-runtime [supervise]; fates rows 145-146; night-pass [p1]; tools/unattended/README.md:211 | C4-F1 |
| cl-dClosedLoop-0307 | dWellOiledMachine | night-pass [p2] item 7; gap-rt-23 | holds |
| cl-dClosedLoop-0308 | dWellOiledMachine | night-pass [p2] item 6 | holds |
| cl-dClosedLoop-0309 | dWellOiledMachine | gap-rt-24; stall-and-loop [design] 7 | holds |
| cl-dClosedLoop-0310 | dWellOiledMachine | away-pass AP-8 fold; catalogue trace.identity, trace.cost; P35, P36 | holds |
| cl-dClosedLoop-0311 | dWellOiledMachine | catalogue commits.edge-check, trace.identity; presets (strict commit-msg); away-pass AP-6, SA-4 | holds |
| cl-dClosedLoop-0312 | dWellOiledMachine | P35; catalogue trace.rows; gap-rt-25, gap-rt-27; tools/runlog/model.py:1558 | holds |
| cl-dClosedLoop-0313 | dWellOiledMachine | P33, P36; gap-orient-19 | holds |
| cl-dClosedLoop-0314 | dWellOiledMachine | P36, P37; away-pass AP-16; gap-rt-31, gap-rt-32, gap-tool-14, gap-tool-18 | holds |
| cl-dClosedLoop-0315 | dWellOiledMachine | catalogue runtime.act-auth; away-pass AP-14 fold; gap-rt-28, gap-rt-30, gap-tool-16 | holds |
| cl-dClosedLoop-0316 | dWellOiledMachine | memory-plan [pockets] row 107; code readers of `orientation/` | C4-F11 |
| cl-dClosedLoop-0317 | dWellOiledMachine | shape-reviews-compared SA-10; memory-plan refs row | holds |
| cl-dClosedLoop-0318 | dWellOiledMachine | night-pass-two [p4], NT-19; catalogue build.push; .githooks/pre-push:1163 | holds |
| cl-dClosedLoop-0319 | dWellOiledMachine | night-pass-two [p4], NT-20; catalogue build.unit-holders | holds |
| cl-dClosedLoop-0320 | dWellOiledMachine | night-pass-two [p4] contradiction 2, NT-21; `gov-session` readers by grep | holds |
| cl-dClosedLoop-0321 | dWellOiledMachine | night-pass-two [p7]; layer-runtime [supervise], [tests] in-flight; research-agent-cap fallback | holds |
| cl-dClosedLoop-0322 | dWellOiledMachine | catalogue memory.mirror; night-pass-two NT-14 fold; layer-runtime [extend] | holds |
| cl-dClosedLoop-0323 | dWellOiledMachine | night-pass-two NT-28 and answers' review; layer-runtime [supervise], [tests] in-flight | holds |
| cl-dClosedLoop-0324 | dWellOiledMachine | stall-and-loop [design] 5, [owed]; catalogue runtime.no-progress, leases.renewal, leases.expiry-hours; layer-runtime [tests] renewal | C4-F6, C4-F7 |
| cl-dClosedLoop-0325 | dWellOiledMachine | stall-and-loop [design] 6; catalogue runtime.hold-ceiling; layer-runtime [supervise], [tests] limits, act-ceiling | C4-F5 |
| cl-dClosedLoop-0326 | dWellOiledMachine | stall-and-loop [design] 6, 10, SL-4 to SL-6; catalogue run.*, notify.owner-items | holds |
| cl-dClosedLoop-0327 | dWellOiledMachine | stall-and-loop [design] 7; catalogue runtime.refusal-repeats | holds |
| cl-dClosedLoop-0328 | dWellOiledMachine | stall-and-loop [design] 9; catalogue deps.on-parent-withdrawn | holds |
| cl-dClosedLoop-0329 | dWellOiledMachine | catalogue build.spend-cap; SL-8 | holds |
| cl-dClosedLoop-0330 | dWellOiledMachine | cloud-and-scale [design] 6, [fleet] | holds |
| cl-dClosedLoop-0331 | dWellOiledMachine | cloud-and-scale [design] 7, [fleet]; catalogue runtime.admission-scope | holds |
| cl-dClosedLoop-0332 | dWellOiledMachine | cloud-and-scale [design] 8, 18; gap-conc-16 | holds |
| cl-dClosedLoop-0333 | dWellOiledMachine | cloud-and-scale [design] 11; catalogue deps.messaging | holds |
| cl-dClosedLoop-0334 | dWellOiledMachine | cloud-and-scale [design] 12; catalogue roles.harness/auth.<role> | holds |
| cl-dClosedLoop-0335 | dWellOiledMachine | cloud-and-scale [design] 10, 13; gap-rt-44 | holds |
| cl-dClosedLoop-0336 | dWellOiledMachine | cloud-and-scale [design] 14; gap-rt-45 | holds |
| cl-dClosedLoop-0337 | dWellOiledMachine | cloud-and-scale [design] 2; layer-runtime [supervise] fencing; flow-steps [deploy] owners | C4-F13 |
| cl-dClosedLoop-0338 | dWellOiledMachine | cloud-and-scale [design] 18, [fleet]; gap-rt-46 | holds |
| cl-dClosedLoop-0339 | dWitnessedBar | gap-test-01; flow-steps [test] | holds |
| cl-dClosedLoop-0340 | dWitnessedBar | layer-runtime [enforce] bypasses; gap-test-09 | holds |
| cl-dClosedLoop-0341 | dWitnessedBar | flow-steps test.route; catalogue verdict.blocks | holds |
| cl-dClosedLoop-0342 | dWitnessedBar | flow-steps test.verdict; P3; catalogue verdict; gap-test-02 | C4-F9 |
| cl-dClosedLoop-0343 | dWitnessedBar | flow-steps [test] held legs; catalogue verdict.held | holds |
| cl-dClosedLoop-0344 | dWitnessedBar | P3; layer-expansions remote verdict; catalogue verdict.remote.*; gap-test-11 to gap-test-13; Stage 0 K4 | C4-F9 |
| cl-dClosedLoop-0345 | dWitnessedBar | gap-test-06, gap-test-10; night-pass [p2] seen-red choice | holds |
| cl-dClosedLoop-0346 | dWitnessedBar | flow-steps test.route, test.flakes, the "Where a flake is seen" note; gap-test-04 | C4-F10 |
| cl-dClosedLoop-0347 | dWitnessedBar | gap-test-03; catalogue tests.product; Stage 0 K4 | C4-F9 |
| cl-dClosedLoop-0348 | dWitnessedBar | gap-test-07, gap-test-08 | holds |
| cl-dClosedLoop-0349 | dWitnessedBar | gap-tool-01; P16 | holds |
| cl-dClosedLoop-0350 | dWitnessedBar | systems record (leg name the join key); retrofit [owners] pack namespace | holds |
| cl-dClosedLoop-0351 | dWitnessedBar | retrofit [ledger]; v2 dOrderedCharter row (H5); tools/memory-tree/merge-rows.*; map_lib.py:1404,1502 | holds |
| cl-dClosedLoop-0352 | dWitnessedBar | retrofit [ratchet]; catalogue retrofit.widen | C4-F9 |
| cl-dClosedLoop-0353 | dWitnessedBar | retrofit [seed]; catalogue retrofit.unseeded | holds |
| cl-dClosedLoop-0354 | dWitnessedBar | retrofit [ledger] directions 17/2/7/1, RF-5; gap-test-14, gap-test-15 | holds |
| cl-dClosedLoop-0355 | dWitnessedBar | retrofit [ledger] pins, [owners] | holds |
| cl-dClosedLoop-0356 | dWitnessedBar | retrofit [owners]; v2 dOrderedCharter and dSafePassage rows | holds |
| cl-dClosedLoop-0357 | dWitnessedBar | tools/gate-legs.json (140 legs, no purpose field); PM-5 | holds |
| cl-dClosedLoop-0358 | dWitnessedBar | v2 dGroundRules row; retrofit [ledger] | holds |
| cl-dClosedLoop-0359 | dWitnessedBar | flow-steps [test] "A fix pass keeps its check"; gap-test-19 | holds |
| cl-dClosedLoop-0360 | dWitnessedBar | night-pass [p4]; P33 | holds |
| cl-dClosedLoop-0361 | dWitnessedBar | flow-steps [test] WK-1 note; test.attribute and test.reason rows | holds |
| cl-dClosedLoop-0362 | dWitnessedBar | P37; research-compatibility §4; away-pass [p4]; tools/gate-legs.json argv | C4-F12 |
| cl-dClosedLoop-0363 | dWitnessedBar | catalogue trace.leg-output; P35; gap-test-20 | holds |
| cl-dClosedLoop-0364 | dWitnessedBar | away-pass AP-33 fold and [p4] platform matrix; gap-tool-20; govkit.py:1138; profile_bar.py:282 | C4-F2 |
| cl-dClosedLoop-0365 | dWitnessedBar | away-pass AP-33; research-python-floor §1 | holds |
| cl-dClosedLoop-0366 | dWitnessedBar | flow-roles-adoption [design] 9 to 14, [chain]; catalogue instructions.exclude; gap-test-21 | holds |
| cl-dClosedLoop-0367 | dWitnessedBar | night-pass-two [p5] item 4, NT-23; gap-test-22 | holds |
| cl-dClosedLoop-0368 | dWitnessedBar | catalogue verdict.flakes, flow.wait-ceiling; stall-and-loop [folded]; flow-steps test.route, test.select | holds |

| dWellOiledMachine | C4-F1, C4-F3, C4-F4, C4-F5, C4-F6, C4-F7, C4-F8, C4-F11, C4-F13 |
|---|---|
| dWitnessedBar | C4-F2, C4-F9, C4-F10, C4-F12 |

Read outside the list above: `AGENTS.md` and `coding-governance-agents.template.md` at the working tree's root, through a filename-only grep for `gov-session`, to test 0320's "the charter's roster line" reader. The grep matched `AGENTS.md`.
