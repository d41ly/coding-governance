# Skeptic brief: run C, batch 3

**Serves:** research PLAY-dClosedLoop-1

**Your task is to refute each finding below, and then to break each clean cell after them.** This brief is your
instructions, not the subject of your review: do not review it, the audit's seal or its instruments. A defect you see
in them goes in one line at the end of your return, and nowhere else.

You are one of four skeptics in run C of the whole-design audit (`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`, whose `[rubric]` grades
what you confirm). Each finding below was returned by a walker reading the sealed copy of the design at
`C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`. Try to refute each one: re-read its address in the copy, and confirm it
only when the defect is there and does what the finding says. Then try to break each clean cell listed after them, a
cell a walker judged to hold.

## What you may read, and nothing else

1. **The sealed copy's design records,** under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/memory/builds/dClosedLoop/build/`, but not its
   `*-compared.md`, `*-instruments.md` or session-log records, and nothing in the copy's `reviews/` or `prompts/`.
2. **The design map,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/design-map.txt`, as your index, and **Stage 0's leads,** `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/tree/stage0-leads.md`,
   which some findings cite.
3. **Code** under the working tree's `tools/`, `skills/` and `.githooks/`, to test a claim the design makes about
   today, and the protocol files your charter names: `memory/guides/`, `memory/HYGIENE.md` and `memory/TEMPLATE-SPEC.md`.
4. **This brief,** and your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-c3/`.

Read nothing else: not the working tree's other records, not the walkers' returns, not the session's scratchpad or
temp folders, not other briefs, not git history. The copy is the subject: judge every finding against it alone, since
the working tree may differ from it.

## Findings to refute

### C3-F18 — `reuse_lookup.py` is retired without its by-value readers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0240
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** layer-memory [reuse] lists the by-value readers: "hygiene check 12's §10 arm accepts the token `reuse_lookup` as reuse evidence (`SPEC10_EVIDENCE_CUTOFF`) … `MAP_CLI` … the `reuse-probed` DoD item". In code, `tools/memory-tree/check-memory-hygiene.sh:2474` reads `index(s10p, "reuse_lookup") > 0`, `tools/unattended/kit.toml:174` declares `MAP_CLI`, and `tools/unattended/PROTOCOL.template.md:356` declares `reuse-probed`. Clause 0240 says only "with their readers rewritten".
- **Consequence:** After the tool retires, check 12 still certifies a spec's reuse audit on a citation of a retired tool.
- **Fix:** Name the by-value readers in 0240. See red a planted spec citing `reuse_lookup` after the new cutoff.

### C3-F19 — The resolve check can go green on an empty population
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0241
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** layer-memory [annotations] says: "Its first green proves nothing … the population is empty. Three planted red cases are owed … a dangling `refs=` id, a dangling `refs=` path, and a `gov:feature` tag with no entry … The check asserts a non-empty population once the first annotation lands". Clause 0241 says: "the generated annotation index and its resolve check (`annotations.grammar`), the shipped-evidence signal re-checked first".
- **Consequence:** A gate never seen red, over an empty population, is read as coverage, against the charter's [gate] rule.
- **Fix:** Carry the three planted reds and the non-empty assertion in 0241.

### C3-F20 — README routing and the relation graph are each built by two builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0242
- **Class:** K8
- **Severity:** medium
- **Evidence:** Clause 0242 (dLinkedLibrary) says: "the generated views: README routing, the relation graph, …". 0215 (dTotalRecall) says: "a generated routing region by purpose", and 0217 (dTotalRecall) says: "… rendered as the relation graph". memory-plan [practice] says: "every node gov ships names one owning build".
- **Consequence:** Two specs build one view, and the one-owner check reds, or two renderers diverge.
- **Fix:** Drop the two views from 0242, or have 0242 say it consumes dTotalRecall's renders.

### C3-F21 — The touched-block comment budget is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0244
- **Class:** K8
- **Severity:** medium
- **Evidence:** systems [design-annotations] says: "Budget. A block a commit touches is at most 12 lines, and a head line at most 160 B". The annotations leg's checks include "the touched-block budget; history inside a note's body; one anchor per feature tag". gap-mem-18 says: "Comment load is unbudgeted". Clause 0244 says only: "the `annotations` leg, the marker query … and the read hook". 0248 covers only the untouched blocks.
- **Consequence:** New long comment blocks pass, and gap-mem-18 stays open.
- **Fix:** List the leg's checks in 0244, the touched-block cap among them, each seen red on a planted case.

### C3-F22 — `annotations.resolve-scope` and `annotations.lookup` are not named
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0244
- **Class:** K4
- **Severity:** low
- **Evidence:** v2 [policies] lists `annotations.resolve-scope` (notes, every-comment-ref) and `annotations.lookup` (query-and-map, query, map-index), both dLinkedLibrary's. Stage 0's K4 lists both as unread. 0244 carries AN-1's default in prose only, and no clause carries resolve-scope.
- **Consequence:** `notes` and `map-index` never route.
- **Fix:** Name both keys in 0241 and 0244.

### C3-F31 — The span rule's owed re-measure is not carried
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0254
- **Class:** K10
- **Severity:** low
- **Evidence:** v2 [owed] says: "the span share re-measured with the map's own extractors: the hybrid loses if 80% or more of a feature's outside spans sit in a derivable definition (point 4)". Clause 0254 builds the span rule with no losing test.
- **Consequence:** The hybrid span rule is built with no test that could reject it.
- **Fix:** Add the re-measure and its 80% bound to 0254.

### C3-F27 — The "one pin over three seams" rule is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0262
- **Class:** K10
- **Severity:** low
- **Evidence:** lexicon [classes] says: "`VERB_OFFENDER_PIN` becomes the debt pin. `SUFFIX_OFFENDER_PIN` folds into it … The per-cell `PINS:` block retires". It also says "Two cells re-arm. `py.file` and `py.constant`". In code, `tools/lexicon/lexicon.py:121` reads `PIN_KEYS = {"verb": "VERB_OFFENDER_PIN", "suffix": "SUFFIX_OFFENDER_PIN"}`. Clause 0262 names only "the shrink-only pin".
- **Consequence:** The suffix pin and the per-cell pins survive as separate waivers beside the debt pin.
- **Fix:** Carry the fold, the `PINS:` retirement and the two cells' re-arming in 0262 and 0276.

### C3-F24 — The forced-name packs contradict the rule that closed sets apply by name
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0263
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [forced] item 1 says: "A namespaced closed set applies by name, and its rows carry a namespace pattern … (`pytest_*`, `__*__`)". Clause 0263 says: "packs keyed by base member, base prefix and host namespace, applied only where the site resolves statically through its imports to that base". The clause also omits the three outcome cases: unresolved base, in-repo parent and marker.
- **Consequence:** Module-level pytest hooks and dunders on classes with no outside base stay debt and are refused at commit under `lexicon.at-commit: refuse`, which leaves gap-lex-01 open.
- **Fix:** Split the rule in 0263: member and prefix rows resolve statically, and namespace closed sets apply by name. Add the three cases, each with its fixture.

### C3-F30 — The lexicon declaration kind has no declared writer or reader in any clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0269
- **Class:** K3
- **Severity:** low
- **Evidence:** layer-memory [contract] says: "lexicon declaration | dMindYourWords | … dMindYourWords builds the declaration and its packs; writer item not named". Stage 0's K3 lists it as both "no writer item" and "no reader". Clause 0269 says: "declared by the owner, custom packs included (`lexicon.packs`)".
- **Consequence:** The kind's registry row has no door, and the one-door check cannot grade it.
- **Fix:** Name the declaration as a registered kind in 0269, its door `instructions.edit` and its reader the lexicon's pack loader.

### C3-F25 — The noun canon's source contradicts the amended design
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0271
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [drift] (amended by the debt fold's `nouns-table` row) says: "noun clusters, written exogenously, such as `sha` against `oid` … The corpus decides only which clusters are live". Clause 0271 says: "a noun canon seeded from the corpus and frozen", which is L-3's pre-fold offer wording.
- **Consequence:** A corpus-seeded canon makes today's variants canonical, the opposite of the fix.
- **Fix:** Reword 0271: clusters written exogenously, with liveness from the corpus.

### C3-F26 — `ratified` is retired without its readers by value
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0272
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [vocabulary] says: "`ratified` gives way to that path's record, and its readers move with it … `adopt-lexicon.sh --check`, the kit's `lexicon-pins` hole and the scaffold read that record too. The leg pack's arm is seen red on a planted LANGS change newer than the record". The debt fold classes this `retirement-inventory-misses-readers-by-value`. In code, `ratified` is read in `tools/lexicon/{adopt-lexicon.sh,kit.toml,lexicon.py,lexicon_conf.py,scaffold_lexicon.py,selftest.py}` and `tools/drift-audit/{drift_report.py,drift_signals.py}`. Clause 0272 says only: "with `ratified` replaced by its record".
- **Consequence:** The drift signal and adopt check keep reading a dead field, and their signal silently stops moving.
- **Fix:** Name the readers in 0272, with the planted LANGS red.

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

### C5-F19 — Plan's triage, kickoff and authority keys are built only at their defaults
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0371, cl-dClosedLoop-0375 and cl-dClosedLoop-0370
- **Class:** K4
- **Severity:** low
- **Evidence:**
  - v2: `plan.triage | owner-batches, rules, archive-legacy`; `plan.kickoff | offer-next, binding, advisory`; `plan.authority | planner-drafts-owner-ratifies, planner-within-themes, owner-orders`.
  - Stage 0's leads K4 lists all three as unread.
  - The clauses read "rule-based triage" and "kickoff offering the next item".
- **Consequence:** The other values are accepted by the schema and never take effect.
- **Fix:** Name each key in its clause, with each value's arm planted.

### C5-F14 — Plan Review and the landing review run before or beside the build that supplies their lenses
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0374 and cl-dClosedLoop-0424 (with cl-dClosedLoop-0458)
- **Class:** K7
- **Severity:** medium
- **Evidence:**
  - cl-0374 (dRankedPlan): "Plan Review". cl-0424 (dShippedRelease): "the landing review blocking the build's close".
  - cl-0458 (dCalibratedLens): "lenses for Plan, Test, Deploy and Maintain".
  - gap-review-01 ("Plan, Test, Deploy and Maintain have none") is dCalibratedLens's. gap-plan-04 is dRankedPlan's, and gap-deploy-06 is dShippedRelease's.
  - dCalibratedLens descends from dRankedPlan. dShippedRelease and dCalibratedLens do not descend from each other.
- **Consequence:**
  - From dRankedPlan's landing until dCalibratedLens's, the Plan breakpoint has no lens, and no stand-in is named.
  - The landing review's gap and its lens's gap are owned by two builds that do not descend from each other, which the gap register's split rule forbids.
- **Fix:**
  - cl-0374 and cl-0424 each name their stand-in lens from dFairHearing's catalogue until dCalibratedLens lands.
  - Re-key gap-plan-04 and gap-deploy-06 to the build that completes them, or split them.

### C5-F13 — gap-flow-04's closure spans two builds that do not descend from each other, and gap-flow-03 has no closing clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0382 (dRankedPlan, Gaps owned)
- **Class:** K8
- **Severity:** medium
- **Evidence:**
  - gap-flow-04: "no recorded plan revision and no re-design inventory of completed work".
  - The inventory kind is dIndexedDesign's (map `record-kind.inventory — owner=dIndexedDesign`; ownership-population P15, "refuted: owner dIndexedDesign"), and `design.inventory` is dIndexedDesign's item.
  - The gap register's rule: "a gap whose closers do not descend one from the other is split, one key per build".
  - dIndexedDesign's parents do not include dRankedPlan, and dRankedPlan's do not include dIndexedDesign.
  - cl-0382 only names "a plan revision". No clause builds the plan-revision record. gap-flow-03 (card, plan and brief levels) is matched by no clause.
- **Consequence:**
  - The gap join reads dRankedPlan as closing a gap whose inventory half lands elsewhere.
  - No unit builds the plan-revision record, and the three-times-written plan stays.
- **Fix:**
  - Split gap-flow-04 into a dRankedPlan key (the plan-revision record, built by a clause) and a dIndexedDesign key (the inventory).
  - Add a dRankedPlan clause that declares the card, plan and brief levels, for gap-flow-03.

## Clean cells to attack

- `cl-dClosedLoop-0012` in dGroundRules
- `cl-dClosedLoop-0210` in dFurnishedOrders
- `cl-dClosedLoop-0238` in dLinkedLibrary
- `cl-dClosedLoop-0155` in dKeptSession
- `cl-dClosedLoop-0432` in dShippedRelease
- `cl-dClosedLoop-0359` in dWitnessedBar
- `cl-dClosedLoop-0328` in dWellOiledMachine
- `cl-dClosedLoop-0351` in dWitnessedBar

## What you return

Your final message, nothing else:
- for each finding, `- <id>: confirmed <severity>` or `- <id>: refuted`, then one line with the reason you observed,
  quoting its address; a severity the rubric grades otherwise than the walker did, said so;
- for each clean cell, `- <clause> <build>: holds`, or `- <clause> <build>: defect` with the defect written as a new
  finding in the walkers' grammar, its id `CS3-F<n>`;
- last, `- **Read outside the list above:** none`, or each path you read outside it and why.

Write nothing to the repository; any probe you run writes under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-c3/` only. Your effort is the one the owner's
role definition sets.
