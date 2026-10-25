**Serves:** journal TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-84

# gov-spec-writer handoff — TOOL-dWitnessedBar-1

<!-- gov:handoff role=gov-spec-writer build=dWitnessedBar unit=- path=memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-84-1-spec-writer.md role-sha=06b14b1ac42a task-sha=82c47fcc46cf -->

## Role

You are a code architect, writing the specification for one or more units of a larger build. You are
not writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design.

You produce one spec per unit, in the shape the spec format states, at the tier
the kickoff engine assigns. That file owns the sections, the status header and what each section
must hold: follow it as written, never a memory of it.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite it by path and line. A claim
  you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the memory hygiene gate and the naming lexicon over your specs, and no other gate.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3). Never decide one
  silently.

You are not building. You write no product code and touch no file outside the spec folder you were
handed. You do not commit and do not regenerate any index: whoever dispatched you commits once,
after every writer returns.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## Task

This handoff is for build `dWitnessedBar`, and names no single unit.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dWitnessedBar specced and built, so that each of the 30 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 37 owned nodes (Owned nodes) is built, and each of its 27 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0339@8e7bc7ae` · now `8e7bc7ae`, as at the baseline · tokens: `measured`, `test.flakes`, `verdict.flakes.entry` — gate health measured and the reliability bar, with `verdict.flakes.entry`'s `measured` threshold derived from the flake records once every leg of the bar has 30 verdicts there: one more than the 90th percentile, across the bar's legs, of each leg's flakes in its last ten verdicts, re-derived at each gate-health measurement and written to the gate-health record with the verdicts it came from, which `test.flakes` reads, 2 in 10 holding until the record holds one, seen on a planted bar whose measured threshold differs from 2 in 10, a leg held at the measured threshold and not at 2 in 10, and red on a planted `test.flakes` that holds at 2 in 10 once the record holds a measured threshold (the closing pair's flakes-measured-no-writer, the owner's answer)
2. `cl-dClosedLoop-0340@1984aa46` · now `1984aa46`, as at the baseline · tokens: none, so the token arm cannot see this clause — bypasses recorded
3. `cl-dClosedLoop-0341@0f53eec5` · now `65d333f3` by deviation `2026-10-25-build-TOOL-dWitnessedBar-3-deviation-31` · tokens: none, so the token arm cannot see this clause — attribution decides what blocks by TOOL-dWitnessedBar-3's block table, under which a `DEAD PROBE` red, and a red the attribution names no class for, blocks under every value of `verdict.blocks`; `MIXED` and `CONTENDED` pass under `own-only` and block under the other two values
4. `cl-dClosedLoop-0342@a3fc832c` · now `a3fc832c`, as at the baseline · tokens: none, so the token arm cannot see this clause — the runner-written verdict the pre-push hook reads
5. `cl-dClosedLoop-0343@3d7be760` · now `3d7be760`, as at the baseline · tokens: none, so the token arm cannot see this clause — held legs by policy
6. `cl-dClosedLoop-0344@5cea08b4` · now `5cea08b4`, as at the baseline · tokens: `head_sha`, `remote-ci`, `verdict`, `verdict.remote.pin`, `verdict.remote.pin-scope`, `verdict.remote.trust` — the verdict backends registered under `verdict`, the local hook, the peer-node verifier and the remote verdict, the last a `remote-ci` slot the integrations expansion fills, a remote verdict standing as a witness only when its `head_sha` is the SHA it judges, its writer the platform's own app, the declared workflow path, a push event and the declared job, its bar step concluded and not skipped, and the pinned files at `head_sha` equal to `verdict.remote.pin` over the files `verdict.remote.pin-scope` names, as `verdict.remote.trust` says, seen red on a swapped workflow and on a planted unregistered backend, and the held-CI reader moved out of the unattended kit and registered as that remote verdict's reader (gap-test-11, gap-test-13)
7. `cl-dClosedLoop-0345@3265ae12` · now `72933671` by deviation `2026-10-25-build-TOOL-dWitnessedBar-7-deviation-71` · tokens: `build.acceptance`, `test.seen-red` — `test.seen-red` reading the seen-red records `build.acceptance` writes, one per gate a build adds or changes, the owed set being every leg whose `tools/gate-legs.json` row is added past the build's base or whose `argv` moved and every leg a `New arm:` line of the build's specs resolves to, a gate script edited with no `argv` change and no declared arm owing none, keyed by leg and red SHA, a planted gate with no recorded red turning it red, and, until dScopedBuild lands that writer, the attended session's agent observing each new arm red on its staged break and green once restored and recording both in the unit's acceptance ledger, which `test.seen-red` reads as the record (gap-test-06, the owner's FK-4-12 and FK-5-2; TOOL-dWitnessedBar-7 §2 S4, §8 F3)
8. `cl-dClosedLoop-0346@c53fd58e` · now `c53fd58e`, as at the baseline · tokens: `test.flakes`, `test.verdict`, `verdict.flakes.entry` — flake quarantine, a leg held once its flakes reach `verdict.flakes.entry` in its window of verdicts, two in its last ten until the gate-health record holds the measured threshold cl-0339 derives, and that threshold after, fed by the runner's mode re-running each red leg once on the same tree under `test.verdict`'s env, seen on a fixture leg that reds then greens reaching `test.flakes` and red on a planted leg held below the entry threshold (gap-test-04, the owner's FK-4-11)
9. `cl-dClosedLoop-0347@934d7dcb` · now `934d7dcb`, as at the baseline · tokens: `tests.product` — the product-test contract with runner adapters, product tests declared, declared with runners or none as `tests.product` says, each value seen on a planted repository
10. `cl-dClosedLoop-0348@ca24547a` · now `ca24547a`, as at the baseline · tokens: none, so the token arm cannot see this clause — derived pre-commit list and multi-node cost evidence
11. `cl-dClosedLoop-0349@79373aa7` · now `79373aa7`, as at the baseline · tokens: none, so the token arm cannot see this clause — the gate-leg factory and its conformance gate, every leg declaring the principles it enforces
12. `cl-dClosedLoop-0350@37beff65` · now `37beff65`, as at the baseline · tokens: `check`, `leg`, `pack`, `tag` — the `leg`, `check` and `pack` tag namespaces, each leg given a `tag` field beside its free-text name, which stays the join key
13. `cl-dClosedLoop-0351@d6eaa553` · now `d6eaa553`, as at the baseline · tokens: `compute_coverage`, `merge-rows.sh`, `merge-rows.test.sh`, `resolve_compare_base`, `tools/lib`, `tools/memory-tree/merge-rows.py` — retrofit's baseline ledger factory in `tools/lib`, one file per population, each registration declaring its direction (shrink-only debt, append-only history, declared set or ceiling) and its home, keyed never by line and carried across a rename, its both-ways arm `compute_coverage`, its base `resolve_compare_base`'s, moved to `tools/lib` by dOrderedCharter (H5), its TSV rows merged by the row-keyed driver that exists, `tools/memory-tree/merge-rows.py` with `merge-rows.sh`, given the ledger class with the factory's row key and its postconditions extended to it, `merge-rows.test.sh`'s append-collision case run on a planted ledger conflict, reaching copy-installed adopters as every `tools/lib` primitive does
14. `cl-dClosedLoop-0352@2cbf95b4` · now `2cbf95b4`, as at the baseline · tokens: `populated`, `ratchet`, `retrofit.widen`, `seed laundering` — the `ratchet` leg pack, with its `populated`, `seed laundering`, rename and merge rows, a population's growth admitted only through a widen record with its reason or refused, as `retrofit.widen` says, each value seen on a planted growth
15. `cl-dClosedLoop-0353@24ae0391` · now `24ae0391`, as at the baseline · tokens: `test.seed` — `test.seed` at every check's registration, seeding only an absent population and recording a failed or dead-probe seed unarmed
16. `cl-dClosedLoop-0354@1a484582` · now `13f6f9b8` by deviation `2026-10-25-build-TOOL-dWitnessedBar-16-deviation-161` · tokens: none, so the token arm cannot see this clause — TOOL-dWitnessedBar-16 converts every registry the population rule of `registry_directions.py` (`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md:1087-1090`) finds at the build run's base, derived there and never typed; at `19d6aae6` that is 28, 18 shrink-only debt, 2 append-only histories, 7 declared sets and 1 ceiling.
17. `cl-dClosedLoop-0355@0f895fff` · now `0f895fff`, as at the baseline · tokens: none, so the token arm cannot see this clause — the seven record and row pins as keyed populations, and the date cutoffs registered as cutoffs
18. `cl-dClosedLoop-0356@4d098894` · now `4d098894`, as at the baseline · tokens: none, so the token arm cannot see this clause — the positional references, IW-1's legacy list and the unpinned facts registered from dOrderedCharter's keyed lists, and dSafePassage's landed step rows as an append-only population keyed by step id
19. `cl-dClosedLoop-0357@4d3bcfbb` · now `4d3bcfbb`, as at the baseline · tokens: `gate-legs.json` — the leg's purpose field in `gate-legs.json`, today's 140 legs reviewed: each purpose derived from what the leg carries, or put to the owner (PM-5)
20. `cl-dClosedLoop-0358@a04b8b39` · now `a04b8b39`, as at the baseline · tokens: none, so the token arm cannot see this clause — the legacy-homes list dGroundRules declares, converted into a ledger population keyed by conf and key when its factory lands (M4)
21. `cl-dClosedLoop-0359@390176b3` · now `5c408077` by deviation `2026-10-25-build-TOOL-dWitnessedBar-21-deviation-211` · tokens: none, so the token arm cannot see this clause — a fix pass that keeps its check: its allowance excluding the red leg's own test files and gate script, a change to them routed through the tester's wrong-spec judgment to Design as a new unit, its arm seen red on a planted fix pass that writes the red leg's test file, and a fix pass after a failed acceptance leaving the acceptance commands' own check files alone, those being a `*.test.sh`, a name ending `selftest.py`, a `test_*.py` or a path under a `fixtures/` directory, each named by a backticked token of the spec's acceptance criteria (night pass, point 6; TOOL-dWitnessedBar-21 §2 S2, §8 F2)
22. `cl-dClosedLoop-0360@f873b4dc` · now `f873b4dc`, as at the baseline · tokens: `enforces=`, `tests=` — the `tests=` and `enforces=` edge fields on legs (night pass, point 4)
23. `cl-dClosedLoop-0361@59790344` · now `59790344`, as at the baseline · tokens: `test.attribute`, `test.reason` — a minimal tester agent in today's roles kit, its allowance scratch only, playing `test.attribute`, `test.reason` and the fix pass's wrong-spec judgment until dBoundRoles re-founds it with the other roles (WK-1)
24. `cl-dClosedLoop-0362@46f28632` · now `46f28632`, as at the baseline · tokens: `encoding_posture.py`, `sh_hygiene.py` — the portability leg pack: a line-ending class leg, encoding arms for stdout, JavaScript and Python text IO, the last moved in from gate-lint's `encoding_posture.py`, with `sh_hygiene.py`'s legs beside it, so every P37 rule has a core leg, path, temp-file and quoting arms, each seen red on a planted case, a bare-shell-name arm, an interpreter-floor arm that runs a real interpreter at the declared floor, with a feature census, and the shell-role ledger, the resolver's own floor being dSafePassage's (P37, AP-31)
25. `cl-dClosedLoop-0363@4ad46937` · now `4ad46937`, as at the baseline · tokens: `trace.leg-output` — the verdict record naming its bar run and its cause, and a failing leg's output tail kept by hash, as `trace.leg-output` says (P35)
26. `cl-dClosedLoop-0364@2fbc8cf5` · now `2fbc8cf5`, as at the baseline · tokens: `GOV_BASH`, `bash`, `bash.exe`, `bin/bash.exe`, `corpus_ids.py`, `git --exec-path`, `profile_bar.resolve_bash`, `resolve_bash`, `resolve_bash_shell`, `resolve_launcher`, `spawnSync('bash', …)`, `tools/lib`, `uname -s` — one bash resolver in `tools/lib` with its JavaScript twin, extracted from the execution-based resolvers that exist, `profile_bar.resolve_bash` and govkit's `resolve_bash`, whose contracts it keeps, copy-installed kits carrying it inline, and replacing every resolver and bare-bash launch site a query over tracked Python and JavaScript finds, each `resolve_bash`, `resolve_launcher` and `resolve_bash_shell`, the seven copies of the loop over `bash.exe` and `bash` and the stop guard's `spawnSync('bash', …)` among them: `GOV_BASH` first, a set but unusable value refused by name, then Git's own `bin/bash.exe` derived from `git --exec-path`, then PATH, System32 and WindowsApps launchers refused, a candidate accepted only once it runs, and on a Windows host only once it also answers `uname -s` as MINGW or MSYS, a staged WSL-first break seen red on Windows and a Linux node's own bash accepted on a Linux arm, govkit's and `corpus_ids.py`'s `GOV_BASH` arms green, and a refusal in place of any fall-back to a bare `bash`, which Windows resolves to WSL's launcher (AP-33)
27. `cl-dClosedLoop-0365@47113ea2` · now `47113ea2`, as at the baseline · tokens: `/mnt/` — a wrong-shell refusal at every entry point: a gov script started by WSL's bash on a Windows checkout, a `/mnt/` path over a Windows gitdir, refuses and names Git's bash (AP-33)
28. `cl-dClosedLoop-0366@a7d91105` · now `337938da` by deviation `2026-10-25-build-TOOL-dWitnessedBar-28-deviation-281` · tokens: `instructions.exclude` — a repository's legs from its overlay's leg rows through the leg factory, registered at Test's leg-pack point as the repository's pack and counted once each has its seen-red record, a manifest row with no source red, every target row no source produces at the first composed update, a hand-edited gov row included, kept on a shrink-only legacy list and landing as the adopter wrote it until the owner converts it into an `amends` patch and drains the entry, a gov leg's arguments, guard and ceiling changed by a pinned patch and dropped only through `instructions.exclude` while every other leg lands, the leg kind's fixed set declared, the canary's key set and the legs that check the composition, its open fields' widening directions declared, a ceiling widening as it rises, and leg tags joined to dSafePassage's step gate, each seen red on a planted unsourced row, a patch on a vanished leg, a dropped fixed leg, a patched fixed leg and a planted leg tag removed with no change record, green on one naming its successor (FA-1, FA-2, FA-5, the flow adoption's review; TOOL-dWitnessedBar-28 §2 S7, §8 F1)
29. `cl-dClosedLoop-0367@c53d0fb3` · now `c53d0fb3`, as at the baseline · tokens: none, so the token arm cannot see this clause — every size warning shown on a passing run, in the runner's summary and its verdict record, attributed to the unit that grew the file, seen on a planted breach under a green bar (the night pass two, point 5, the owner's NT-23)
30. `cl-dClosedLoop-0368@53672db0` · now `53672db0`, as at the baseline · tokens: `flow.wait-ceiling`, `verdict.flakes.release`, `verdict.held` — a quarantined leg released after `verdict.flakes.release`' streak of consecutive greens, three by default, and run at least once a day whatever `verdict.held` says so its greens accrue, and a blocking CONTENDED red re-run once on a quiet host, one running no other bar, a red there routed by its attribution and never re-run, and none found within `flow.wait-ceiling` raising an owner item, seen on a planted quarantine and a planted contended pair (P39)

### brief:acceptance

- At the Design exit, `carries.py --build dWitnessedBar --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dWitnessedBar` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dWitnessedBar --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 479 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dWitnessedBar by <decision>` line.
- Any path outside `memory/builds/dWitnessedBar/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.
- The surfaces of dBoundRoles, dScopedBuild, which this build's clauses use as stand-ins only (Later builds named).

### input:spec

memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-84-carry-h1-brief.md

### task:reuse

dDeclaredLoop's spec run (memory/builds/dDeclaredLoop/) as the procedure; seams per unit from the reuse scouts.

### Charter rules

- [yagni] YAGNI: build what this unit needs now, never scaffolding for later, and delete rather than disable.
- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [core] One shared core with thin adapters, so logic and authorization live once; data changes additively, with defaults and an upgrade step.
- [contract] A contract two parties share lands first, as one source with generated copies and a parity gate against a live re-derivation; deployables sharing one artifact release together.
- [derive] Derive over author: status, counts, inventories and indexes are generated or declared and checked both ways, never typed beside what they describe.
- [one-fact] One fact in one place: a document points at the source that owns a value, or a gate compares the two.
- [spec] Spec before code: every product-code unit commits its spec first, a micro-spec for a mechanical change and a full design pass for a substantive one.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [gate] A gate never seen red is not a gate: observe its failing case, state what it does not check, and never read a skip, an unmovable probe, an exemption or an empty population as coverage.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [small] Work in small units, one stream each, merged to local main often; risky behaviour lands dark behind a default-off switch.
- [docs] A user-facing change is not done until its page under `help/` is current.
- [security] Security first: validate once at the write boundary, deny by default, give automation the narrowest grant, and keep secrets out of files, memory and chat.

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

### Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
