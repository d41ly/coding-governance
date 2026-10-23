---
slug: dGroundRules
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-12 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64
spec-audit: 2026-10-21
parents: dTrueNorth
may: PLAY-dClosedLoop-3
---

# dGroundRules — the Policy build of the dClosedLoop chain

## The problem this build exists to solve

dGroundRules owns 3 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-spine-06,
gap-tool-24, gap-rt-34. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 11 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 3 owned gaps above close.

## Detriments if this is not built

- Its 3 owned gaps stay open.
- Its 1 child build waits on it: dSafePassage.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dGroundRules` green before the first pass; a moved instrument blob is
  a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dGroundRules`, a record per member "recorded by nobody", the same with `--write` (commit it
  as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dGroundRules-1` | `cl-dClosedLoop-0007@b0458b78` | `.governance/policy.toml` |
| 2 | `TOOL-dGroundRules-2` | `cl-dClosedLoop-0008@6598846f` | the reader extending `read_policy_key`'s contract |
| 3 | `TOOL-dGroundRules-3` | `cl-dClosedLoop-0009@7d93fce9` | each key resolved in one order: an override in the file |
| 4 | `TOOL-dGroundRules-4` | `cl-dClosedLoop-0010@cd629be7` | a malformed file or an out-of-set value read as `policy-file.on-invalid` says |
| 5 | `TOOL-dGroundRules-5` | `cl-dClosedLoop-0011@8312590d` | the JSON mirror regenerated at each landing and pinned to the landed revision |
| 6 | `TOOL-dGroundRules-6` | `cl-dClosedLoop-0012@937c308e` | the minimal guard |
| 7 | `TOOL-dGroundRules-7` | `cl-dClosedLoop-0013@8ae02ac2` | the legacy homes on a shrink-only list derived by query from the files they guard |
| 8 | `TOOL-dGroundRules-8` | `cl-dClosedLoop-0014@28a178b1` | an arm red when a key whose Owner build has landed has no reader |
| 9 | `TOOL-dGroundRules-9` | `cl-dClosedLoop-0015@8ce57bfb` | `budgets.enforce` |
| 10 | `TOOL-dGroundRules-10` | `cl-dClosedLoop-0016@df63b6eb` | `runtime.agents-in-flight` |
| 11 | `TOOL-dGroundRules-11` | `cl-dClosedLoop-0017@c5b54ae9` | each loop bound and deadline key declaring that raising it is a loosening |
| 13 | `TOOL-dGroundRules-13` | **Derived:** PLAY-dClosedLoop-2 | the mirror's bytes name no commit: each reason's revision phrase rendered as a placeholder the helper fills |
| 14 | `TOOL-dGroundRules-14` | **Derived:** PLAY-dClosedLoop-2 | the landing replay: the mirror a prepared merge carries is fresh at that merge |
| 15 | `TOOL-dGroundRules-15` | **Derived:** PLAY-dClosedLoop-2 | the `.agent-cap.conf` lowering in one home: inside `resolve_read`, so every reader of the limit sees it |
| 16 | `TOOL-dGroundRules-16` | **Derived:** PLAY-dClosedLoop-2 | the adopter's fresh target as a standing case: every arm of the shipped `policy check` leg green on install day |
| 17 | `TOOL-dGroundRules-17` | **Derived:** PLAY-dClosedLoop-2 | the legacy-home list withheld from installs and the cap census graded by what ships, so neither arm reds an adopter |
| 18 | `TOOL-dGroundRules-18` | **Derived:** PLAY-dClosedLoop-2 | a writer split bounded by the agent limit: rule 2 judges `gov:fixed-writers` against `runtime.agents-in-flight` and verifiers against `MAX_VERIFIERS` |
| 19 | `TOOL-dGroundRules-19` | **Derived:** PLAY-dClosedLoop-2 | the guard admits a regenerated mirror equal to its render, so an agent branch that edits the catalogue reaches a green bar |
| 20 | `TOOL-dGroundRules-20` | **Derived:** PLAY-dClosedLoop-2 | the `policy fixtures` guard covers the sibling files its cases run, and a join keeps the census's enforcers inside it |
| 21 | `TOOL-dGroundRules-21` | **Derived:** PLAY-dClosedLoop-2 | the round-1 spec audit's minors: forty-one findings closed in the code units 1 to 10 leave, one scope item each |
| 22 | `TOOL-dGroundRules-22` | **Derived:** PLAY-dClosedLoop-2 | each census row names where its kit installs the enforcer, and the census arm grades an adopter there |
| 23 | `TOOL-dGroundRules-23` | **Derived:** PLAY-dClosedLoop-2 | the registry join holds each census row's destination and entry to what the deployer installs |
| 24 | `TOOL-dGroundRules-24` | **Derived:** PLAY-dClosedLoop-2 | the fresh target installed by the deployer, so the case grades an install govkit makes |
| 25 | `TOOL-dGroundRules-25` | **Derived:** PLAY-dClosedLoop-2 | the round-1 audit of units 13 to 21, its minors: thirty-nine findings closed in the code those units leave, one scope item each |
| 26 | `TOOL-dGroundRules-26` | **Derived:** PLAY-dClosedLoop-2 | the fresh target installed from a commit of the tree under test, so the case grades the bytes the bar records |
| 27 | `TOOL-dGroundRules-27` | **Derived:** PLAY-dClosedLoop-2 | every policy case that drives the deployer runs it from the snapshot, and a call over the source's own root refuses |
| 28 | `TOOL-dGroundRules-28` | **Derived:** PLAY-dClosedLoop-2 | the historical-sha oracle class widened to HEAD, so a spec driving the deployer from gov's tree is handed it |
| 29 | `TOOL-dGroundRules-29` | **Derived:** PLAY-dClosedLoop-2 | a receipt-less target is gov's source tree only when it holds the registry, so the census arm never grades a scratch target as gov |
| 30 | `TOOL-dGroundRules-30` | **Derived:** PLAY-dClosedLoop-2 | the writer-marker floor decided by the installed hook's own verdict, never by a kit version the lander has not minted |
| 31 | `TOOL-dGroundRules-31` | **Derived:** PLAY-dClosedLoop-2 | the install-day scaffold defers the mirror over uncommitted inputs, so the first `--scaffold` in a repository with history exits 0 |
| 32 | `TOOL-dGroundRules-32` | **Derived:** PLAY-dClosedLoop-2 | the round-1 audit of units 22 to 25, its minors: twenty findings closed in the code those units leave, one scope item each |
| 33 | `TOOL-dGroundRules-33` | **Derived:** PLAY-dClosedLoop-2 | the `policy fixtures` guard holds `selftest.py`, and a trace of every source file a case reads reds one the guard misses |
| 34 | `TOOL-dGroundRules-34` | **Derived:** PLAY-dClosedLoop-2 | the round-1 audit of units 26 to 32, its minors: thirty-seven findings closed in the code those units leave, one scope item each |
| 35 | `TOOL-dGroundRules-35` | **Derived:** PLAY-dClosedLoop-2 | the guard trace records a bytecode-cache read as its source file, so a warm load still records `govkit.py` |
| 36 | `TOOL-dGroundRules-36` | **Derived:** PLAY-dClosedLoop-2 | a source read git ignores is set aside before the guard join, counted, and never offered to the guard |
| 37 | `TOOL-dGroundRules-37` | **Derived:** PLAY-dClosedLoop-2 | every `policy fixtures` guard entry names a file git tracks, so the trace's sweep cannot widen the guard with a path no diff carries |
| 38 | `TOOL-dGroundRules-38` | **Derived:** PLAY-dClosedLoop-2 | the guard trace keeps no read under the source's git directories, so its verdict does not depend on where `.git` sits |
| 39 | `TOOL-dGroundRules-39` | **Derived:** PLAY-dClosedLoop-2 | the census registry window held at both edges by a standing case, its fixture paths spelled whole |
| 40 | `TOOL-dGroundRules-40` | **Derived:** PLAY-dClosedLoop-2 | the overlap arm pins each pair's expected answer, so the render's rule and the dispatcher's are graded against the truth and not only against each other |
| 41 | `TOOL-dGroundRules-41` | **Derived:** PLAY-dClosedLoop-2 | the help page's install section held to the deferral line `--scaffold` prints, by the case that prints it |
| 42 | `TOOL-dGroundRules-42` | **Derived:** PLAY-dClosedLoop-2 | the criterion bug class gains the input respelled to pass a join, and is handed to every spec commit |
| 43 | `TOOL-dGroundRules-43` | **Derived:** PLAY-dClosedLoop-2 | the round-1 audit of units 33 and 34, its minors: fifteen findings closed in the code those units leave, one scope item each |
| 44 | `TOOL-dGroundRules-44` | **Derived:** PLAY-dClosedLoop-2 | the overlap arm's disjoint row is a real string-prefix trap, and the arm refuses a disjoint row that is not one |
| 45 | `TOOL-dGroundRules-45` | **Derived:** PLAY-dClosedLoop-2 | the overlap probes read their pairs from the arm's table, so no criterion spells a pair a second time |
| 46 | `TOOL-dGroundRules-46` | **Derived:** PLAY-dClosedLoop-2 | the spec-tokens checker refuses a criterion literal that sources a shell file by bare name |
| 47 | `TOOL-dGroundRules-47` | **Derived:** PLAY-dClosedLoop-2 | the criterion bug class's fix gains the re-run: a literal is run verbatim from the root before its spec commits, and a restated one is re-run, never copied |
| 48 | `TOOL-dGroundRules-48` | **Derived:** PLAY-dClosedLoop-2 | the help page's install-section count observed with its path whole, and paired with the break that empties it |
| 49 | `TOOL-dGroundRules-49` | **Derived:** PLAY-dClosedLoop-2 | the help page's guard line observed by the leg query with its path whole, and by the trace when it is taken out |
| 50 | `TOOL-dGroundRules-50` | **Derived:** PLAY-dClosedLoop-2 | the help-page parity prints where it found the deferral line, so the install section is read by one rule |
| 51 | `TOOL-dGroundRules-51` | **Derived:** PLAY-dClosedLoop-2 | the build-order evidence observed in the build README with its path whole, beside the root-README negative |
| 52 | `TOOL-dGroundRules-52` | **Derived:** PLAY-dClosedLoop-2 | the round-1 audit of units 35 to 43, its minors: twenty-five findings closed in the code and the observations those units leave, one scope item each |
| 53 | `TOOL-dGroundRules-53` | **Derived:** PLAY-dClosedLoop-2 | the trap row's shell verdict observed with the library sourced by its tracked path and the trap pair whole |
| 54 | `TOOL-dGroundRules-54` | **Derived:** PLAY-dClosedLoop-2 | the trap row's verdicts observed a second time through the whole overlap probe, which reads the pair from the suite and spells none |
| 55 | `TOOL-dGroundRules-55` | **Derived:** PLAY-dClosedLoop-2 | the criterion bug class gains the side read: a criterion observes its scope item by running the check, never by reading what the check reads |
| 56 | `TOOL-dGroundRules-56` | **Derived:** PLAY-dClosedLoop-2 | the row check observed refusing: the not-a-trap row run through the arm's own row function, never read off the table |
| 57 | `TOOL-dGroundRules-57` | **Derived:** PLAY-dClosedLoop-2 | the not-a-trap staging spelled whole, so the trap probe lists the row the row check refuses |
| 58 | `TOOL-dGroundRules-58` | **Derived:** PLAY-dClosedLoop-2 | the overlap probe sources the unattended library by its tracked path, so its shell column is a verdict and not a load failure |
| 59 | `TOOL-dGroundRules-59` | **Derived:** PLAY-dClosedLoop-2 | the overlap criteria of units 40 and 43 observed through the whole probe, the raw-compare staging included |
| 60 | `TOOL-dGroundRules-60` | **Derived:** PLAY-dClosedLoop-2 | unit 52's overlap observations taken through the whole probe, with the Python column shown graded on its own |
| 61 | `TOOL-dGroundRules-61` | **Derived:** PLAY-dClosedLoop-2 | rule 7 bounds every settings layer it can read, so a declared settings file never hides the project's |
| 62 | `TOOL-dGroundRules-62` | **Derived:** PLAY-dClosedLoop-2 | an unset `budgets.<cap>` reads as no file value: the derived-default refusal is a type the caps module catches, and only that refusal |
| 63 | `TOOL-dGroundRules-63` | **Derived:** PLAY-dClosedLoop-2 | the closing review's minors: unit 46's population re-measured with units 44 and 45, a packet join for each live chain run, and the owner-cap record's count named by range, one scope item each |
| 64 | `TOOL-dGroundRules-64` | **Derived:** PLAY-dClosedLoop-2 | the respelled literals no other repair covers, restored whole and observed: units 5, 21, 33 and 34 |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** DEFERRED · 63 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-12 TOOL-dGroundRules-13 TOOL-dGroundRules-14
ids TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28
ids TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42
ids TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55 TOOL-dGroundRules-56
ids TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dGroundRules-1 — the policy file, the policy kit, its catalogue and the catalogue's shape audit](spec/2026-10-23-spec-TOOL-dGroundRules-1.md) | 1 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-11 — every loop bound and deadline key declares that raising it is a loosening](spec/2026-10-23-spec-TOOL-dGroundRules-11.md) | 1 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-16 — the adopter's fresh target as a standing case: every arm of the shipped `policy check` leg green on install day](spec/2026-10-23-spec-TOOL-dGroundRules-16.md) | 2 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-2 — the policy reader, at the landed revision, parsed and never sourced](spec/2026-10-23-spec-TOOL-dGroundRules-2.md) | 2 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-3 — one resolution order: the file's override, then the catalogue default with its reason](spec/2026-10-23-spec-TOOL-dGroundRules-3.md) | 2 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-4 — an invalid policy file read as `policy-file.on-invalid` says, never as defaults](spec/2026-10-23-spec-TOOL-dGroundRules-4.md) | 2 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-24 — the fresh target installed by the deployer, so the case grades an install govkit makes](spec/2026-10-23-spec-TOOL-dGroundRules-24.md) | 3 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-5 — the JSON mirror, regenerated at each landing and read from the landed blob](spec/2026-10-23-spec-TOOL-dGroundRules-5.md) | 3 | 2 | DEFERRED | rev-4 | 2026-10-23 |
| [TOOL-dGroundRules-6 — the minimal guard over the policy file and its three neighbours](spec/2026-10-23-spec-TOOL-dGroundRules-6.md) | 3 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-13 — the mirror's bytes name no commit: each reason's revision phrase rendered as a placeholder the helper fills](spec/2026-10-23-spec-TOOL-dGroundRules-13.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-14 — the landing replay: the mirror a prepared merge carries is fresh at that merge](spec/2026-10-23-spec-TOOL-dGroundRules-14.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-19 — the guard admits a regenerated mirror equal to its render, so an agent branch that edits the catalogue reaches a green bar](spec/2026-10-23-spec-TOOL-dGroundRules-19.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-26 — the fresh target installed from a commit of the tree under test, so the case grades the bytes the bar records](spec/2026-10-23-spec-TOOL-dGroundRules-26.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-28 — the historical-sha oracle class widened to HEAD, so a spec driving the deployer from gov's tree is handed it](spec/2026-10-23-spec-TOOL-dGroundRules-28.md) | 4 | 1 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-7 — the legacy policy homes on a shrink-only list derived from the files they guard](spec/2026-10-23-spec-TOOL-dGroundRules-7.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-8 — the reader-coverage arm: a key whose Owner build has landed has a reader](spec/2026-10-23-spec-TOOL-dGroundRules-8.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-10 — the agent limit as runtime.agents-in-flight, rendered into the harness's settings, agent-cap's counting retired](spec/2026-10-23-spec-TOOL-dGroundRules-10.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-9 — one switch over every size cap, each cap's value through the policy reader](spec/2026-10-23-spec-TOOL-dGroundRules-9.md) | 5 | 2 | DEFERRED | rev-4 | 2026-10-23 |
| [TOOL-dGroundRules-15 — the `.agent-cap.conf` lowering in one home: inside `resolve_read`, so every reader of the limit sees it](spec/2026-10-23-spec-TOOL-dGroundRules-15.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-17 — the legacy-home list withheld from installs and the cap census graded by what ships, so neither arm reds an adopter](spec/2026-10-23-spec-TOOL-dGroundRules-17.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-18 — a writer split bounded by the agent limit: rule 2 judges `gov:fixed-writers` against `runtime.agents-in-flight` and verifiers against `MAX_VERIFIERS`](spec/2026-10-23-spec-TOOL-dGroundRules-18.md) | 6 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-20 — the `policy fixtures` guard covers the sibling files its cases run, and a join keeps the census's enforcers inside it](spec/2026-10-23-spec-TOOL-dGroundRules-20.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-21 — the round-1 spec audit's minors: forty-one findings closed in the code units 1 to 10 leave, one scope item each](spec/2026-10-23-spec-TOOL-dGroundRules-21.md) | 7 | 2 | DEFERRED | rev-4 | 2026-10-23 |
| [TOOL-dGroundRules-22 — each census row names where its kit installs the enforcer, and the census arm grades an adopter there](spec/2026-10-23-spec-TOOL-dGroundRules-22.md) | 7 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-23 — the registry join holds each census row's destination and entry to what the deployer installs](spec/2026-10-23-spec-TOOL-dGroundRules-23.md) | 7 | 2 | DEFERRED | rev-4 | 2026-10-23 |
| [TOOL-dGroundRules-25 — the round-1 audit of units 13 to 21, its minors: thirty-nine findings closed in the code those units leave, one scope item each](spec/2026-10-23-spec-TOOL-dGroundRules-25.md) | 8 | 2 | DEFERRED | rev-4 | 2026-10-23 |
| [TOOL-dGroundRules-29 — a receipt-less target is gov's source tree only when it holds the registry, so the census arm never grades a scratch target as gov](spec/2026-10-23-spec-TOOL-dGroundRules-29.md) | 8 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-27 — every policy case that drives the deployer runs it from the snapshot, and a call over the source's own root refuses](spec/2026-10-23-spec-TOOL-dGroundRules-27.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-30 — the writer-marker floor decided by the installed hook's own verdict, never by a kit version the lander has not minted](spec/2026-10-23-spec-TOOL-dGroundRules-30.md) | 9 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-31 — the install-day scaffold defers the mirror over uncommitted inputs, so the first `--scaffold` in a repository with history exits 0](spec/2026-10-23-spec-TOOL-dGroundRules-31.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-32 — the round-1 audit of units 22 to 25, its minors: twenty findings closed in the code those units leave, one scope item each](spec/2026-10-23-spec-TOOL-dGroundRules-32.md) | 10 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-33 — the `policy fixtures` guard holds `selftest.py`, and a trace of every source file a case reads reds one the guard misses](spec/2026-10-23-spec-TOOL-dGroundRules-33.md) | 11 | 2 | DEFERRED | rev-4 | 2026-10-23 |
| [TOOL-dGroundRules-34 — the round-1 audit of units 26 to 32, its minors: thirty-seven findings closed in the code those units leave, one scope item each](spec/2026-10-23-spec-TOOL-dGroundRules-34.md) | 12 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-35 — the guard trace records a bytecode-cache read as its source file, so a warm load still records `govkit.py`](spec/2026-10-23-spec-TOOL-dGroundRules-35.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-36 — a source read git ignores is set aside before the guard join, counted, and never offered to the guard](spec/2026-10-23-spec-TOOL-dGroundRules-36.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-37 — every `policy fixtures` guard entry names a file git tracks, so the trace's sweep cannot widen the guard with a path no diff carries](spec/2026-10-23-spec-TOOL-dGroundRules-37.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-38 — the guard trace keeps no read under the source's git directories, so its verdict does not depend on where `.git` sits](spec/2026-10-23-spec-TOOL-dGroundRules-38.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-39 — the census registry window held at both edges by a standing case, its fixture paths spelled whole](spec/2026-10-23-spec-TOOL-dGroundRules-39.md) | 13 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-40 — the overlap arm pins each pair's expected answer, so the render's rule and the dispatcher's are graded against the truth and not only against each other](spec/2026-10-23-spec-TOOL-dGroundRules-40.md) | 13 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-41 — the help page's install section held to the deferral line `--scaffold` prints, by the case that prints it](spec/2026-10-23-spec-TOOL-dGroundRules-41.md) | 13 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-42 — the criterion bug class gains the input respelled to pass a join, and is handed to every spec commit](spec/2026-10-23-spec-TOOL-dGroundRules-42.md) | 13 | 1 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-43 — the round-1 audit of units 33 and 34, its minors: fifteen findings closed in the code those units leave, one scope item each](spec/2026-10-23-spec-TOOL-dGroundRules-43.md) | 14 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-44 — the overlap arm's disjoint row is a real string-prefix trap, and the arm refuses a disjoint row that is not one](spec/2026-10-23-spec-TOOL-dGroundRules-44.md) | 14 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dGroundRules-45 — the overlap probes read their pairs from the arm's table, so no criterion spells a pair a second time](spec/2026-10-23-spec-TOOL-dGroundRules-45.md) | 14 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-46 — the spec-tokens checker refuses a criterion literal that sources a shell file by bare name](spec/2026-10-23-spec-TOOL-dGroundRules-46.md) | 14 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-47 — the criterion bug class's fix gains the re-run: a literal is run verbatim from the root before its spec commits, and a restated one is re-run, never copied](spec/2026-10-23-spec-TOOL-dGroundRules-47.md) | 14 | 1 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-48 — the help page's install-section count observed with its path whole, and paired with the break that empties it](spec/2026-10-23-spec-TOOL-dGroundRules-48.md) | 14 | 1 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-49 — the help page's guard line observed by the leg query with its path whole, and by the trace when it is taken out](spec/2026-10-23-spec-TOOL-dGroundRules-49.md) | 14 | 1 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-50 — the help-page parity prints where it found the deferral line, so the install section is read by one rule](spec/2026-10-23-spec-TOOL-dGroundRules-50.md) | 14 | 1 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-51 — the build-order evidence observed in the build README with its path whole, beside the root-README negative](spec/2026-10-23-spec-TOOL-dGroundRules-51.md) | 15 | 1 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-52 — the round-1 audit of units 35 to 43, its minors: twenty-five findings closed in the code and the observations those units leave, one scope item each](spec/2026-10-23-spec-TOOL-dGroundRules-52.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-53 — the trap row's shell verdict observed with the library sourced by its tracked path and the trap pair whole](spec/2026-10-23-spec-TOOL-dGroundRules-53.md) | 17 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-55 — the criterion bug class gains the side read: a criterion observes its scope item by running the check, never by reading what the check reads](spec/2026-10-23-spec-TOOL-dGroundRules-55.md) | 17 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-57 — the not-a-trap staging spelled whole, so the trap probe lists the row the row check refuses](spec/2026-10-23-spec-TOOL-dGroundRules-57.md) | 17 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-58 — the overlap probe sources the unattended library by its tracked path, so its shell column is a verdict and not a load failure](spec/2026-10-23-spec-TOOL-dGroundRules-58.md) | 17 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dGroundRules-61 — rule 7 bounds every settings layer it can read, so a declared settings file never hides the project's](spec/2026-10-23-spec-TOOL-dGroundRules-61.md) | 17 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-64 — the respelled literals no other repair covers, restored whole and observed: units 5, 21, 33 and 34](spec/2026-10-23-spec-TOOL-dGroundRules-64.md) | 17 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-54 — the trap row's verdicts observed a second time through the whole overlap probe, which reads the pair from the suite and spells none](spec/2026-10-23-spec-TOOL-dGroundRules-54.md) | 18 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-56 — the row check observed refusing: the not-a-trap row run through the arm's own row function, never read off the table](spec/2026-10-23-spec-TOOL-dGroundRules-56.md) | 18 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-59 — the overlap criteria of units 40 and 43 observed through the whole probe, the raw-compare staging included](spec/2026-10-23-spec-TOOL-dGroundRules-59.md) | 18 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-60 — unit 52's overlap observations taken through the whole probe, with the Python column shown graded on its own](spec/2026-10-23-spec-TOOL-dGroundRules-60.md) | 18 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-62 — an unset `budgets.<cap>` reads as no file value: the derived-default refusal is a type the caps module catches, and only that refusal](spec/2026-10-23-spec-TOOL-dGroundRules-62.md) | 18 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dGroundRules-63 — the closing review's minors: unit 46's population re-measured with units 44 and 45, a packet join for each live chain run, and the owner-cap record's count named by range, one scope item each](spec/2026-10-23-spec-TOOL-dGroundRules-63.md) | 20 | 2 | DEFERRED | rev-1 | 2026-10-23 |
<!-- /gen:build-units -->

Records: 87 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 TOOL-dGroundRules-53 TOOL-dGroundRules-54 TOOL-dGroundRules-55
TOOL-dGroundRules-56 TOOL-dGroundRules-57 TOOL-dGroundRules-58 TOOL-dGroundRules-59 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64.

Ids whose spec moved past its audited revision: TOOL-dGroundRules-1@rev-1 TOOL-dGroundRules-10@rev-1 TOOL-dGroundRules-13@rev-1 TOOL-dGroundRules-14@rev-1 TOOL-dGroundRules-15@rev-1 TOOL-dGroundRules-16@rev-1 TOOL-dGroundRules-17@rev-1 TOOL-dGroundRules-18@rev-1 TOOL-dGroundRules-19@rev-1
TOOL-dGroundRules-2@rev-2 TOOL-dGroundRules-20@rev-1 TOOL-dGroundRules-21@rev-1 TOOL-dGroundRules-22@rev-1 TOOL-dGroundRules-23@rev-1 TOOL-dGroundRules-24@rev-1 TOOL-dGroundRules-25@rev-1 TOOL-dGroundRules-26@rev-1 TOOL-dGroundRules-27@rev-1 TOOL-dGroundRules-28@rev-1 TOOL-dGroundRules-29@rev-1
TOOL-dGroundRules-3@rev-2 TOOL-dGroundRules-30@rev-1 TOOL-dGroundRules-31@rev-1 TOOL-dGroundRules-32@rev-1 TOOL-dGroundRules-33@rev-1 TOOL-dGroundRules-34@rev-1 TOOL-dGroundRules-35@rev-1 TOOL-dGroundRules-36@rev-1 TOOL-dGroundRules-37@rev-1 TOOL-dGroundRules-38@rev-1 TOOL-dGroundRules-39@rev-1
TOOL-dGroundRules-4@rev-2 TOOL-dGroundRules-40@rev-1 TOOL-dGroundRules-41@rev-1 TOOL-dGroundRules-42@rev-1 TOOL-dGroundRules-43@rev-1 TOOL-dGroundRules-5@rev-1 TOOL-dGroundRules-6@rev-1 TOOL-dGroundRules-7@rev-1 TOOL-dGroundRules-8@rev-1 TOOL-dGroundRules-9@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dGroundRules's 11 clause(s) and 5 owned node(s), over 63 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 11
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-23-spec-TOOL-dGroundRules-13.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-14.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-15.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-16.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-17.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-18.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-19.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-20.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-21.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-22.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-23.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-24.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-25.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-26.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-27.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-28.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-29.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-30.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-31.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-32.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-33.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-34.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-35.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-36.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-37.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-39.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-40.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-41.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-43.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-44.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-45.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-47.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-48.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-49.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-51.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-52.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-53.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-54.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-55.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-56.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-57.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-58.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-59.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-60.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-61.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-62.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dGroundRules-63.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dGroundRules-64.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0009, cl-dClosedLoop-0014, cl-dClosedLoop-0017
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dGroundRules-1`, `TOOL-dGroundRules-11` | yes |
| 2 | `TOOL-dGroundRules-16`, `TOOL-dGroundRules-2`, `TOOL-dGroundRules-3`, `TOOL-dGroundRules-4` | yes |
| 3 | `TOOL-dGroundRules-24`, `TOOL-dGroundRules-5`, `TOOL-dGroundRules-6` | yes |
| 4 | `TOOL-dGroundRules-13`, `TOOL-dGroundRules-14`, `TOOL-dGroundRules-19`, `TOOL-dGroundRules-26`, `TOOL-dGroundRules-28`, `TOOL-dGroundRules-7`, `TOOL-dGroundRules-8` | yes |
| 5 | `TOOL-dGroundRules-10`, `TOOL-dGroundRules-9` | yes |
| 6 | `TOOL-dGroundRules-15`, `TOOL-dGroundRules-17`, `TOOL-dGroundRules-18`, `TOOL-dGroundRules-20` | yes |
| 7 | `TOOL-dGroundRules-21`, `TOOL-dGroundRules-22`, `TOOL-dGroundRules-23` | yes |
| 8 | `TOOL-dGroundRules-25`, `TOOL-dGroundRules-29` | yes |
| 9 | `TOOL-dGroundRules-27`, `TOOL-dGroundRules-30`, `TOOL-dGroundRules-31` | yes |
| 10 | `TOOL-dGroundRules-32` | no |
| 11 | `TOOL-dGroundRules-33` | no |
| 12 | `TOOL-dGroundRules-34`, `TOOL-dGroundRules-35`, `TOOL-dGroundRules-36`, `TOOL-dGroundRules-37`, `TOOL-dGroundRules-38` | yes |
| 13 | `TOOL-dGroundRules-39`, `TOOL-dGroundRules-40`, `TOOL-dGroundRules-41`, `TOOL-dGroundRules-42` | yes |
| 14 | `TOOL-dGroundRules-43`, `TOOL-dGroundRules-44`, `TOOL-dGroundRules-45`, `TOOL-dGroundRules-46`, `TOOL-dGroundRules-47`, `TOOL-dGroundRules-48`, `TOOL-dGroundRules-49`, `TOOL-dGroundRules-50` | yes |
| 15 | `TOOL-dGroundRules-51` | no |
| 16 | `TOOL-dGroundRules-52` | no |
| 17 | `TOOL-dGroundRules-53`, `TOOL-dGroundRules-55`, `TOOL-dGroundRules-57`, `TOOL-dGroundRules-58`, `TOOL-dGroundRules-61`, `TOOL-dGroundRules-64` | yes |
| 18 | `TOOL-dGroundRules-54`, `TOOL-dGroundRules-56`, `TOOL-dGroundRules-59`, `TOOL-dGroundRules-60`, `TOOL-dGroundRules-62` | yes |
| 20 | `TOOL-dGroundRules-63` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dTrueNorth](../dTrueNorth/README.md)
- **Child builds:** [dSafePassage](../dSafePassage/README.md)
<!-- /gen:build-edges -->
