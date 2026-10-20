# Execution plan: the chain specced, built and landed on nodes a, b and d under today's gov

**Serves:** research PLAY-dClosedLoop-1

The plan the execution record asked for, written from the five execution returns and the owner's four answers. It
opens nothing and changes nothing. Every step below that writes a chain build's file, a policy line, a decision row
or product code runs only after the owner approves this plan, and the baseline's stop holds until then
(`build/…-execution.md:5-7`). The schedule is not typed here. It is the output of
`build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`, kept beside this record and re-run at every landing.

**Conventions.**
- `build/` is `memory/builds/dClosedLoop/build/`, and a file there is named by its suffix: `build/…-carries.py`.
- ER is `build/…-execution.md`, v2 is `build/…-architecture-v2.md`, FQ is `build/…-final-questions.md`, GR is
  `build/…-gap-register.md` and IR is `build/…-research-exec-instruments.md`.
- The five returns are named by facet (driver, coordination, handoffs, schedule, deviation). Each is
  `build/…-research-exec-<facet>.md`.
- "Rests on" cites the line a step depends on. Each was re-read for this plan; a fact cited only to a return was not.
- VERBS, STOPS, PROTOCOL and ASKS are `memory/guides/UNATTENDED-VERBS.md`, `-STOPS.md`, `-PROTOCOL.md` and
  `-ASKS.md`. METHOD is `memory/guides/BUILD-METHOD.md`.
- A time is the schedule script's unit: one clause's work on a full-pace node. It is never hours, because no unit's
  wall time is recorded (GR:291).
- An id no build has minted is written `missing:<id>`.

## [answer]

**The bad news first.**

1. Until dTrueNorth lands, nothing in the merge bar compares a spec with the design. A spec whose pin is stale
   passes today's spec-tokens leg, while the bootstrap `carries.py` reds it (IR:844-860). dTrueNorth's own specs are
   checked only by instruments its runs run by hand.
2. Today's driver cannot fully meet the owner's "nothing is parked or blocked". A run settles a fork itself only in
   these cases:
   - v2 already answers it (STOPS:692);
   - a stated probe decides it (METHOD:100-104);
   - the mandate delegates it, with a `may:` grant lifting veto 2 (METHOD:80-97).

   Three kinds still park: a fork whose only options widen a security, data or write surface (veto 3), one with no
   surviving option, and one the goal cannot survive (METHOD:81, :93-97). The plan carries such a unit forward, so
   its build still lands, and lists it in that build's departures report. Finishing the unit still needs one owner
   ruling and one more run, until dOrderedCharter's fork-resolving decision principles land (`cl-dClosedLoop-0032`).
3. The spec-run close ratified in answer 1 works only for the units a run started with. A unit the run adds is never
   carried forward (STOPS:703-704). That covers a unit promoted from an audit or review finding and an adopted
   discovery. Every confirmed finding is promoted (METHOD:144, :274). So a spec run whose audit or closing review
   confirms anything cannot close by carry-forward. Default D6 asks for the ruling that lets it close.
4. Two readings of the owner's answers do not hold as written. R1: the `may:` derivation has no input, because v2's
   owned nodes carry keys and no paths. R2: dTrueNorth's `cl-dClosedLoop-0004` fixes its stand-in join to the
   by-risk table, so answer 3 does change a clause. The plan applies neither reading. The opening waits on R1, and
   dTrueNorth's spec run waits on R2.
5. Node b buys little. At Pro pace (0.25 of a or d) the chain takes 270 units with b and 272 without it. b gets six
   spec runs, no build run, and 41 of 509 units of work ([schedule]).
6. Three builds rewrite the driver they run under: dDeclaredLoop (`cl-dClosedLoop-0106`), dPlacedRequest
   (`cl-dClosedLoop-0120`) and dWellOiledMachine (`cl-dClosedLoop-0306`). Every run still in flight at one of those
   landings then lands through the new code. The driver runs from the worktree, and the prepare merges the new tip
   in (`.claude/skills/unattended/SKILL.md:9-12`; PROTOCOL:575-576; `tools/push-main.sh:873-884`).
7. The owner starts 44 runs, at 38 distinct moments, nearly one per landing ([schedule]). Nothing picks the next run
   or offers it to a node (GR:337, :340).
8. No driver mode stops a run once its specs are written. A spec run stops because its README's rule says so, and
   nothing refuses one that goes on to build (`tools/workflows/unattended-build.js:6-8`; VERBS:753-762).

**The plan in brief.**
- **Phase 0, node d, records only, one owner landing.** dClosedLoop's session hardens the three instruments, adds a
  departures report, builds the packet instrument, commits the schedule script and opens all 22 builds in one
  landing the owner makes. It also records the ratified policies as decision rows and prepares nodes a, b and d.
- **Phase 1, node a.** dTrueNorth runs as a spec run, then a build run. It proves the landed-README opt-in, the
  grants, the spec-run close, the build run's pickup and the product comparison that replaces the instruments.
- **Phase 2, the chain.** Every build gets a spec run, then a build run. Each runs on the node the schedule script
  names when re-run at each landing. Policy J holds: a spec starts once dTrueNorth has landed, its parents' specs
  have closed and its grandparents have landed; a build starts once its parents have landed.
- **Deviations.** A departure is recorded by the run that makes it and approved by its author. A report generated at
  each build's end explains it, and nothing waits for the owner except the residue named in bad news 2 to 4.

## [constraints]

What today's gov forces on the plan.

| What it forces | Rests on |
|---|---|
| The owner's act starts every run, `/unattended <slug>`; the build README is the authorization | PROTOCOL:21-27 |
| One driver per slug: a live or held claim refuses a second (check 107), a terminal one is taken over | `.unattended.conf:162`; STOPS:186-222 |
| Units inside a run are dispatched one at a time | `tools/workflows/unattended-build.js:76-80`, `:918-921` |
| Preflight refuses a dirty tree, the default branch, and on a first preflight a branch carrying commits outside the build folder, so every run starts in a fresh worktree | `tools/unattended/unattended.sh:2929`, `:2937`, `:3879-3884` |
| `spec-audit:` and `may:` count only from a `slug` README the owner landed on the default branch; on the local anchor fail 89 and fail 78 refuse them | `unattended.sh:2655`, `:4108-4126`, `:4160-4168`; PROTOCOL:87-91, :116-125; IR:862-869 |
| A `may:` grant names decision ids or repo paths, and lifts veto 2 only | `tools/unattended/lib-unattended.sh:1440-1478`; PROTOCOL:116-119; METHOD:82 |
| A fork with no delegated resolver parks; a decision kind the close table does not list becomes an `owner-decision` hand-off | VERBS:36-46; STOPS:674-696; METHOD:93-97 |
| A partial build lands only when every unfinished unit meets all five carry-forward terms | STOPS:698-711 |
| Nothing holds a build until its parents land; `parents:` must only name a folder that exists | `tools/memory-tree/gen_build_index.py:2335-2345` |
| Nothing finds work for a node or offers it one | GR:337, :340 |
| Under the local anchor a hold owes no push, so held work may live on one node only | STOPS:98-99; `.unattended.conf:267` |
| Landing is in place: prepare onto the advertised tip, close under `GATE_FULL=1`, land, landed; the remote's fast-forward is the only serializer, with three race retries | PROTOCOL:428-432; `push-main.sh:188`, `:873-884` |
| A close whose range touches `tools/` owes the flagged bar with its self-tests, under a 21600 s wall | `.unattended.conf:40`, `:67`; VERBS:851-871 |
| `readme-contract.txt` has no merge attribute; `DECISIONS.md` and every `BACKLOG.md` merge by rows; `LIVE.md` and the ledgers take one side and are re-rendered; the merge drivers are per-node config | `.gitattributes:71-86`; `tools/check-wiring.sh:1198-1215` |
| The driver runs from the worktree, and nothing binds the code it executes | `SKILL.md:9-12`; PROTOCOL:575-576 |
| Nothing runs the three instruments; a `DOD_EXTRA` item is attested, never executed; `tools/` is a routed path | `unattended.sh:12225-12226`; `.memory-tree.conf:9` |
| One live `RUN.md` per build; the next preflight rotates a finished one | PROTOCOL:153-158, :337 |
| The resume tick skips a run leased on another host | `tools/unattended/resume-tick.sh:281-285` |
| A spec revised before its unit's first `Pass:` commit is no member of the bootstrap population; under `cl-dClosedLoop-0004` a revision after its pinned audited revision is one | `build/…-deviations.py:20-27`; v2:1764 |

## [phase-0]

dClosedLoop's remaining work. It runs on node d, is written by dClosedLoop's session (the main loop) unless a step
names another actor, and lands once, on the owner's ask. Every file is a record under `memory/`. None is product
code (`memory/builds/dClosedLoop/README.md:39-40`).

### P0.1 The three instruments hardened

Each escape now reds on its plant, and each false red now goes green. Rows 1 to 6 are escapes and row 10 is a guard,
all found by the deviation and handoffs returns. Rows 7 and 8 are false reds, and rows 9 and 11 are placement rules
rather than fixes. The plants are the deviation return's scratch steps, kept verbatim at IR:754-838, ported into each
instrument's own `--fixture --plant`.

| Escape or false red | Fix | Plant that proves it |
|---|---|---|
| A spec carrying another build's clause counts as carried for its owner (`build/…-carries.py:183-204`) | A carried id's build must be the spec's own folder's, unless a `**Moved:** … to <this build> by <decision>` line names it | `crossbuild`: red after the fix, green before |
| A dropped clause escapes after the next edit, because the drop arm reads only the last two revisions (`carries.py:125-126`, `:205-211`) | Compare against every revision of the spec since its first commit | `drop`, then `typo`: red |
| A revision after a pass named only in the commit subject (`build/…-deviations.py:150`) | Attribute a pass from subject and trailer together, as `tools/memory-tree/routed_commits.py:22-26` does | A pass commit with the id only in its subject, then a revision: red |
| A revision on node a while node b's pass is in flight, both merged, is not a descendant of the pass (`deviations.py:153-158`) | Count every revision that is not an ancestor of the first pass | Two branches, merged: red |
| Baseline re-pointed after a loosening, read from v2's working tree (`deviations.py:132-136`) | Pin `59ff8f2ac` in the instrument, and refuse a v2 whose `Baseline:` differs | Loosen `cl-dClosedLoop-0119`, re-point: red |
| An approver written as "owner" passes on a prefix match (`deviations.py:81-87`) | Under the chain's value `author-recorded`, any recorded approver role passes, and one naming the owner must cite a decision id the default branch holds | "owner" with no id: red |
| False red: `AMENDED` read on any spec line (`deviations.py:160`), where the ledger form is `amended rev-N` in journal records (`memory/HYGIENE.md:604-606`) | Read `amended rev-N` from the ledgers | A spec quoting `cl-dClosedLoop-0004`: green; a ledger row with no record: red |
| False red: revisions numbered by commit count (`deviations.py:153-158`), where the header `rev-N` moves only on a material edit (`memory/TEMPLATE-SPEC.md:61-67`) | Address a revision by its header `rev-N` | A status-only commit, then a record at the header's rev-1: green |
| Two specs on two branches each carrying one clause whole are caught only on the merged tree | Placement: the instruments run on the prepared merge, after `--prepare` | The deviation return's two-node plant on the merged tree: red |
| Any run can edit the instruments under `memory/`, the class `TOOL-aStandingWrit-7` names (`memory/builds/aStandingWrit/BACKLOG.md:11`) | Every report and packet prints each instrument's blob hash, and the packet pins it | A one-byte edit to `carries.py`: the next `packet.py --check` reds |
| `asbuilt.py --check` reds on each new record until `--write` runs (`build/…-asbuilt.py:81`) | Placement: the record's own commit carries the re-rendered view | None owed; it is the instrument working |

**The owner's chain values.** Answer 3 also reaches the instruments (ER:126-127). `deviations.py` takes `--policy
report|refuse`, which defaults to `report`: report prints every member and exits 0, and refuse keeps today's exit 1.
Plant: one unjoined member exits 0 and is listed under `report`, and exits 1 under `refuse`.

**Acceptance.**
- Every plant above exits as its row says.
- On today's tree, `carries.py` exits 2 (no spec measured), `deviations.py` exits 0 with 0 members and `asbuilt.py
  --check` exits 0, as the deviation return measured.

### P0.2 The departures report

A new mode of `deviations.py`, `--report <slug> [--write|--check]`, extending the instrument that already computes
the population rather than adding one beside it.

**Its sources:**
- the population for the build: clause moves, revisions after the first pass or after the pinned audited revision,
  ledger `amended` rows, rescope rows from `RUN.md` and every rotated `RUN.*.md`, and divergence hand-backs;
- the records under `memory/builds/<slug>/build/`;
- the forks the build resolved, as M9 derives them (METHOD:299): every §8 `RESOLVED` mark, every `Decided:` trailer in
  the build's commits (METHOD:316-320) and every park row;
- the units carried forward;
- the outputs of `carries.py --report <slug>` and `asbuilt.py --check`.

**What it lists:**
- each member, with its address and hand-off, the record it joins or "recorded by nobody", and the record's reason,
  risk, approver and follow-through;
- each fork, with its question, pick, reason and source line;
- each carried unit, with its ask.

`--write` writes it as `memory/builds/<slug>/build/<date>-build-<first unit>-departures.md`, and `--check` renders it
again and compares the bytes.

**Acceptance.** `--fixture` lists each population plant of P0.1.

**Red tests.**
- A planted `Decided:` trailer missing from the written report reds `--check`.
- A hand edit reds `--check`.

### P0.3 The packet instrument

`build/<date>-build-PLAY-dClosedLoop-1-packet.py`, built from the handoffs return's probe (IR:197-283), from
`carries.py`'s `design()` (`carries.py:83-113`) and from `asbuilt.py`'s view.

**One packet per chain build.** It is written as
`memory/builds/<slug>/prompts/<date>-prompt-<first unit>-packet.md`. It carries `## The prompt` and `## The brief`, so
`handoff.py render --input prompt=<packet>` reads `brief:*` from it (`tools/roles/handoff.py:283-294`).

**Its fields** (the handoffs return's §3):
1. Pins: the baseline sha, the blobs of v2, the as-built view and each instrument, the HEAD it was rendered at, and
   the generator's version.
2. Each clause: its id and hash at the baseline, its hash now with the record behind any change, its text and its
   tokens, flagging a clause the token arm cannot see.
3. Owned nodes.
4. Parents: each one's state, derived from the tree as the schedule script derives it, and each parent clause this
   build's clauses name.
5. Children.
6. Gaps, each with its severity and register line.
7. Policy keys the build owns, and keys it reads that a later build owns.
8. Every mention of a later build, verbatim, with stand-ins flagged.
9. The `[owed]`, `[open]`, `[enforcement]` and `[policies]` lines that name the build.
10. Must-not-touch.
11. The coverage report.
12. The reading order ([handoffs]).

**`--check <slug>`** renders the packet again and compares the bytes. It has completeness arms: every clause id and
hash of the build's row, every gap it owns, every parent, and every `[owed]` line naming it. Each arm is red on a
planted omission.

**Acceptance.**
- Rendering dTrueNorth's packet reproduces the handoffs return's worked example: six clauses, with
  `cl-dClosedLoop-0001@83b6b117` through `cl-dClosedLoop-0006@06ceb3cc`; the node `record-kind.deviation`; and the
  gaps gap-design-13, gap-build-07 and gap-mem-47.
- Once the opening exists in a scratch clone, `handoff.py render --build dTrueNorth --unit <its first unit> --input
  prompt=<packet>` renders, and `handoff.py check` is green on the result.

### P0.4 The schedule script

This record's script: `build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`. Its docstring names its inputs, its
model and what it does not model.

**Acceptance.** It reads v2, the chain builds' specs and the cached claims at a ref. At every landing a node runs
`python <script> --ref origin/main` after `git fetch` and starts the run its table shows on that node at time 0.

**Red tests**, observed on 2026-10-20 in a `--shared` clone in the plan writer's scratch folder; phase 0 runs them
again before the landing:

| Plant | Result |
|---|---|
| `cl-dClosedLoop-0509` dropped from v2 | Exit 1: "holds 22 builds and 508 clause ids … not 22 and 509" |
| Two dTrueNorth specs carrying `cl-dClosedLoop-0001` to `-0006`, at `DEFERRED` | Its spec run reads `done`, and its build run starts at 0 |
| The same specs at `CLOSED` | Both of dTrueNorth's runs read `done`; dGroundRules' spec run starts at 0 |
| A cached `live` claim of user `d41ly` on dGroundRules | Its spec run is pinned to node d at 0 |
| A claim naming user `nobody` | Exit 1: the fleet names no such node |

### P0.5 The opening, in one landing

`build/<date>-build-PLAY-dClosedLoop-1-open.py --write|--check` writes every file below for all 22 builds, in one
commit, from the named source.

**Reuse.** `gen_build_index.py`'s README scaffold refuses a slug any tracked file already names
(`gen_build_index.py:3478-3504`), and v2 names all 22. So the instrument imports the generator's heading canon and
marker pairs (`gen_build_index.py:73`, `:85`, `:125-131`) and writes the authored half itself, never copying them.
`gen_build_index.py --write` then fills the generated regions.

| What | Derived from | Rests on |
|---|---|---|
| Front matter `slug`, `node: d`, `opened`, `streams`, `roster`, `ids:` (left for the generator), `status: OPEN` | The six required keys, and the scaffold's own `node: <slug's tag>` | `gen_build_index.py:190`, `:3528-3537` |
| `spec-audit: <the opening date>` | Answer 2 | ER:86-92 |
| `parents:` | v2's Parents cell; dClosedLoop for dTrueNorth | v2:1762-1785 |
| `may:` | Waits on R1 | ER:139-140 |
| H1 and stage | `# <slug> — the <Stage> build of the dClosedLoop chain` | v2:1762-1785 |
| The five slots | Derived bodies, as the scaffold writes them: the problem slot is the build's owned gaps at the baseline (it is the goal bound); the improvements are its clauses carried and built; the detriments are its gaps left open and its children waiting; the build-level rules are below; the parked decisions are "none" | `gen_build_index.py:122-131`, `:3507-3560` |
| `roster:units` | One unit per clause, in clause order: its id, `cl-dClosedLoop-NNNN@<hash8>`, and the clause's text to its first comma | v2:1762-1785; `carries.py:78-80` |
| Unit family | TOOL for every unit; a unit's spec header `streams` records the disciplines it serves | `.memory-tree.conf:42`; TEMPLATE-SPEC:56-77 |
| `BACKLOG.md`, one ask | "build every roster unit of this build from its spec", filed for the spec run's carry-forward, with its `SEV` row | STOPS:707-709; ASKS:92-100 |
| Packet | P0.3 | above |
| `readme-contract.txt` rows | 22 bound rows (bare paths); the exempt pin is unchanged | `memory/project/readme-contract.txt:1-29`; `.unattended.conf:383-405` |

**Build-level rules each README carries:**
1. A run that finds any roster unit `MISSING` is this build's spec run. It specs every unit, runs the audit, defers
   every unit and closes by carry-forward. A run that finds none `MISSING` is the build run. The phase is read from
   the tree, never typed (METHOD:39-42; VERBS:72-87).
2. The reading order ([handoffs]), and `packet.py --check <slug>` green before the first pass.
3. Push the run branch after every pass commit, hold and hand-off.
4. Before `--close`, write the departures report with `deviations.py --report <slug> --write`.
5. The chain's deviation values are `report` and `author-recorded` (ER:121-127).
6. Forks are settled as [phase-2] says.

**The `may:` derivation.** As read, it has no input. v2's owned nodes are keys such as `record-kind.deviation` and
`item.entry.intake`. The map gives every node an `owner` relation and no path; the plan writer probed every namespace
of `build/…-map.py`'s `derive()`, and the only relations are `owner`, `after`, `fate` and `layer`. `carries.py:104-113`
reads only `owner`. R1 asks which derivation to use, and the opening's `may:` lines wait on its answer.

### P0.6 The two opening hazards

**Bare dTrueNorth ids.** `gen_build_index.py`'s `rosters()` reads every tracked text file under `memory/`, `.py`
included, and joins each id to the build its slug names (`gen_build_index.py:767-805`). A `missing:` id joins
nothing (`:820-828`). The predicate is `git grep -nE` over `memory/` for an id of any of the 22 chain slugs not
preceded by `:` or a letter. Run over the tree, it finds 16 lines in 4 files, all of them dTrueNorth ids:

- `build/…-deviations.py`: lines 178, 180, 181, 183, 184, 185, 189, 191, 193 and 197;
- `build/…-asbuilt.py`: lines 106 and 107;
- IR: lines 7, 776 and 789;
- `build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md`: line 24483.

Once dTrueNorth's folder exists, `--write` joins all of them into its `ids:`.

**The fix** marks each with `missing:`, in both the fixture strings and the verbatim copies. Afterwards, each
instrument's `--fixture` and every `--plant` must give the same verdicts as before.

**The red test.** In a scratch clone, create `memory/builds/dTrueNorth/README.md` and run `gen_build_index.py
--write`:
- before the fix, the README's `ids:` gains the fixture ids;
- after it, it gains none;
- the predicate prints nothing, and a planted bare id makes it print one line.

**Who may mint in a chain build.** The rule follows the claims, because two nodes share the tag letter `d` in all 22
slugs:
1. The opening (dClosedLoop's session) mints each build's roster ids and its one carry-forward ask under that
   build's slug. It mints them once, in one landing, before any claim exists. A session's ids are its own, and the
   later merge re-mints unmerged ones (HYGIENE.md:172-187). This departs from minting one slug per session, so it is
   default D8.
2. After the opening, only the run holding a slug's claim mints under that slug (`unattended.sh:2284-2301`). Its
   next id is the build's highest id in that family plus one (HYGIENE.md:177-179).
3. A run filing an ask about another build mints it under its own build's slug and files it in the other build's
   `BACKLOG.md` (coordination return). Any other row about a foreign ask stays in its own file (ASKS:167-168).
4. An attended session takes a fresh slug of its own, never a chain slug (HYGIENE.md:174-176).

### P0.7 The opening's gates, and its one landing

| Actor | Step | Rests on |
|---|---|---|
| Node d's session | Commit P0.1 to P0.6 and the opening on a branch | the charter's `[land]`, `AGENTS.md:31` |
| Node d's session | `open.py --check`; `packet.py --check` for all 22; `gen_build_index.py --check` and `--check-format` (the contract, both directions); the memory hygiene gate; the bare-id predicate, which must print nothing; `carries.py` (exit 2 expected), `deviations.py` (0) and `asbuilt.py --check` (0) | `readme-contract.txt:2-5`; `gen_build_index.py:2341-2344` |
| Node d's session | Red tests: a one-byte README edit reds `open.py --check`; a roster missing one clause reds the arm that reads every clause in exactly one row; a `parents:` typo raises; a removed contract row reds `--check-format` | as above |
| Owner | Reads the opening diff: every README, its `may:` line, every packet and every decision row | ER:139-140 |
| Owner | Asks for the landing | the charter's `[land]`, `AGENTS.md:31` |
| Node d's session | Lands through `bash tools/push-main.sh`. The pre-push bar takes the doc-only class, because the diff is `memory/` only | `.githooks/pre-push:1215-1223`; `.githooks/gate-env.sh:106-108` |

### P0.8 The policies the answers ratify, as decision rows

One `memory/DECISIONS.md` row each, minted under dClosedLoop's slug (`missing:PLAY-dClosedLoop-2` onward) and landed
with the opening. Each row cites its source:

1. The spec-run close by carry-forward (answer 1), with D6's ruling for units a run adds.
2. The 22 READMEs carry `spec-audit:` and a grant (answer 2), in the form R1 settles.
3. The chain's deviation values, `report` and `author-recorded`, applied to every run and to the instruments
   (answer 3), with R2's ruling on `cl-dClosedLoop-0004`.
4. Node b's slack-first share of both phases (answer 4), as the schedule script's rule.
5. The coordination rules: push after every pass, never preflight over a claim, re-run the schedule at every landing,
   and reconcile at a prepare conflict ([coordination]).
6. Defaults D1, D2, D4, D7 and D8 as the owner settles them.

**Acceptance.** Every row cites ER `[answers]` or a `[defaults]` item.

**Not checked.** No gate reads what a row says. Each is tested where a run applies it, in phase 1.

### P0.9 Each node's preparation

| Actor | Step | Rests on |
|---|---|---|
| Each node | Exactly one remote, and `git remote set-head origin -a` | `unattended.sh:2099-2102`; `push-main.sh:180-186` |
| Each node | `bash tools/check-wiring.sh --fix`, which sets `core.hooksPath` and both merge drivers | `check-wiring.sh:1198-1215`; `.gitattributes:69-86` |
| Each node | The kickoff skill's junction | `AGENTS.md:90` |
| Each node | Register the resume tick and confirm it with `schtasks /query /tn gov-resume-tick`. Node d answered "cannot find" | `tools/unattended/README.md:211`; driver return |
| Each node | Confirm `bash tools/lib/resolve-python.sh` resolves a Python | Facts: Toolchain |
| Each node | `USERNAME` must equal the fleet row's `user`, because a claim's `node:` is that variable and the schedule script maps it through the fleet | `unattended.sh:2410`; `tools/playbook/fleet.toml:21-46` |
| Node b, onboarding | Clone gov to its primary tree, then every step above. Its tag `b` is already claimed (`fleet.toml:28-33`). "Seed local memory from the in-repo mirror" names no mirror and is listed under [cannot] | `AGENTS.md:113-114`; `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-cloud-and-scale.md:434-436` |

**Acceptance.** On each node:
- `unattended.sh --claims` answers from the remote;
- `check-wiring.sh`'s check mode is clean;
- the resume tick is listed;
- `unattended.sh --plan dClosedLoop --paths` runs.

**Red test.** Check mode reports the unset merge driver before `--fix`.

## [phase-1]

dTrueNorth runs on node a as the pilot: a spec run, then a build run. Answer 1 splits every build (ER:77-84), the
pilot included. Its build lands before any other chain spec is written, because the coverage and deviation gates must
stand before the first chain spec (FQ:276-278, :302-303).

**Preconditions:** the opening has landed, and the owner has answered R2, D3 and D6.

| Actor | Step | Rests on |
|---|---|---|
| Node a | `git fetch`. The schedule script with `--ref origin/main` shows `a: spec dTrueNorth at 0` | [schedule] |
| Owner, on node a | Create a fresh worktree off `origin/main` on a new branch, open a session there, and type `/unattended dTrueNorth` | PROTOCOL:21-27; `unattended.sh:2929-2938` |
| Spec run | Schedule the keepalive, then `--preflight`, then `/session-kickoff` | `SKILL.md:16-20`, `:63-65` |
| Spec run | **Proof 1.** Preflight prints `spec-audit — opted in by README spec-audit: <date>`. `RUN.md` records `anchor-kind: default-branch` and the pinned `may:` | VERBS:722-728; IR:862-869 |
| Spec run | The rest of the spec run, per [phase-2] | — |
| Spec run | `carries.py --build dTrueNorth --exit`, then the departures report | P0.1, P0.2 |
| Owner | Reads the coverage and departures reports, then starts the build run on the node the script names | [owner] |
| Build run | Builds the six units. The product join takes the instruments' plant suite as its acceptance (D3). The join's configuration cutoff is the opening landing's date, so every chain spec, dTrueNorth's own included, falls on or after it | v2:1764; deviation return, recommendation 3 |
| Build run | Lands. From then on, every node's pre-push bar, every `--close` and remote CI run the product join | `.github/workflows/remote-ci.yml:106` |

**What the pilot proves**, each a first:
1. A README landed on main opts the run into the audit and pins a grant. No run has done either (driver return).
2. The spec-run close by carry-forward, including D6's path for a unit the run adds.
3. A build run on the same slug takes over the terminal claim (STOPS:221), sees the `DEFERRED` units as non-terminal
   (`unattended.sh:4815`) and dispatches them as READY.
4. The build harness called again after a spec run's audit. Whether its audit stage re-audits specs already audited is
   not read here (`unattended-build.js:180-230`); the pilot observes it.
5. The ask carried through both runs and disposed (ASKS:136-143).
6. The product join reds on every plant of P0.1.

**How the product takes over from the instruments without a gap.** Under J, no other chain spec is written before
dTrueNorth's build lands, so no chain spec lands ungated except dTrueNorth's own, which the instruments check by
hand. From that landing, both run together. The product legs run in the bar. The departures report runs the
instruments at every build's close, and any disagreement between the two becomes an ask in dTrueNorth's `BACKLOG.md`.
Each instrument stops being run when the clause that succeeds it lands:

| Instrument, or arm | Retired by | Lands with |
|---|---|---|
| `asbuilt.py` | `cl-dClosedLoop-0006`'s product view, once it renders byte for byte what `asbuilt.py --write` renders on the same records | dTrueNorth |
| `deviations.py`'s risk reading | the widening classifier `cl-dClosedLoop-0066` | dOrderedCharter |
| `deviations.py`'s approval arm | `deviation.approval`, `cl-dClosedLoop-0119` | dDeclaredLoop |
| `carries.py` | `design.coverage`, `cl-dClosedLoop-0398` | dIndexedDesign |
| `deviations.py`'s population and join | `deviation.gate`, `cl-dClosedLoop-0412` | dScopedBuild |

## [phase-2]

### The spec run, from start to landing

| Actor | Step | Rests on |
|---|---|---|
| Node | `git fetch`; `unattended.sh --claims`; the schedule script with `--ref origin/main`. Take the spec run your node holds at time 0 | VERBS:769-774; [coordination] |
| Owner | Fresh worktree off `origin/main`, then `/unattended <slug>` | PROTOCOL:21-27 |
| Run | Keepalive, preflight, kickoff. Keep the preflight's `spec-audit` line | `SKILL.md:16-20`, `:63-65` |
| Run | Read in the [handoffs] order. Run `packet.py --check <slug>`, and re-render and commit the packet if it is stale | P0.3 |
| Run | The build harness, with `specAudit` set to the pinned date and with `base`, `scratch`, `roles` and `efforts`; each unit's `specBriefPath` is the packet. It runs SPEC (writers author every `MISSING` spec), then AUDIT, then DISPOSAL | VERBS:722-748; `unattended-build.js:6-8`, `:169-178` |
| Spec writers | Each spec carries `**Carries:** cl-…@<hash8> whole` (or `part k/n`), the owned nodes it builds, and its fork marks | `carries.py:7-12`; TEMPLATE-SPEC:155-160 |
| Run | For each unit: `--rescope <slug> --act defer --item <unit> --reason "specced; built by this build's build run"` | VERBS:703-710; STOPS:705-706 |
| Run | For each spec: status `DEFERRED`, with `advances <the ask>` in the header tail | TEMPLATE-SPEC:61-82; STOPS:700-709 |
| Run | In the build's `BACKLOG.md`, the ask's `DEFERRED … until <the build run>` row, so `asks-disposed` reads it as held | ASKS:136-143 |
| Run | For a unit the harness promoted or the run adopted: D6 | STOPS:703-704 |
| Run | `carries.py --build <slug> --exit`. Before dTrueNorth lands, `deviations.py` too | P0.1; deviation return, limit 4 |
| Run | The closing review over the spec commits, recorded with `--review <slug> --subject <slug> …` | METHOD:251-265; VERBS:778; PROTOCOL:352 |
| Run | `deviations.py --report <slug> --write`, and commit | P0.2 |
| Run | Push the run branch after every pass commit | [coordination] |
| Run | `--phase VERIFYING`, `push-main.sh --prepare`, `--authorization`, `--close` (attesting `keepalive-reaped`, and `parked-decisions-surfaced` with a count that includes the defer rows), `--land`, `--landed` | VERBS:849-947 |
| Driver | Writes the claim `landed` | `unattended.sh:6242-6247` |

### The build run, on whichever node the script names

| Actor | Step | Rests on |
|---|---|---|
| Node | Fetch, then the script. Build runs start only once every parent has landed, which the script derives from the tree | P0.4 |
| Owner | Fresh worktree, then `/unattended <slug>`. The preflight takes the terminal claim over and rotates the spec run's `RUN.md` | STOPS:221; PROTOCOL:153-158 |
| Run | `--plan <slug> --paths` lists every `DEFERRED` unit as non-terminal and READY | VERBS:72-87, :753-760; `unattended.sh:4815` |
| Run | Re-ground each spec against the parents that have just landed by re-running its §10 probe. Revise it before its first `Pass:` commit. Under the product join, a revision past the pinned audited revision is a member, so the run writes its record, approved by its author | `deviations.py:20-27`; v2:1764 (`cl-dClosedLoop-0004`) |
| Run | The harness with the pinned `specAudit` (pilot proof 4) | VERBS:722-731 |
| Run | Per unit: `--brief`, `--dispatch --writes …`, the unit harness, a commit with a `Pass: <unit>` trailer, then `gotchas.py --for-diff HEAD~1..HEAD` | VERBS:697-768 |
| Run | Each unit's header goes `INPROGRESS`, then `CLOSED`. The last unit to close carries `closes <the ask>` | TEMPLATE-SPEC:61-82 |
| Run | The closing review over the build's range. Its findings are promoted and built in this run | METHOD:144, :251-290 |
| Run | The departures report, then the close and the landing as in the spec run | VERBS:849-947 |

### How a fork is settled when nothing may park

Each rung uses only today's driver and the owner's grants. Each resolution is recorded as a §8 mark
(TEMPLATE-SPEC:155-160) and a `Decided:` trailer (METHOD:316-320), and the departures report explains it (P0.2).

1. **v2 answers it.** The spec cites the clause; the mark is `RESOLVED (agent, <date>, delegated)`. This is the close
   table's "a question the default branch already answered" (STOPS:692).
2. **A stated probe decides it**, as a `FACT-QUESTION` (METHOD:100-104).
3. **The mandate delegates it.** The run takes the most feature-rich option that survives the vetoes (METHOD:86-95),
   with veto 2 lifted where the grant covers the change (METHOD:82).
4. **A strictly beneficial discovery** is adopted (PROTOCOL:640-690). In a spec run, the unit this adds falls under D6.
5. **What is left** is veto 3, no surviving option, or the goal (METHOD:81, :93-97). It parks through `--park`, and
   the run goes on with every other unit (VERBS:36-46). At the close, the dependent unit is carried forward
   (`DEFERRED`, a defer row, the build's ask), so the build still lands (STOPS:685, :698-711). D7 asks the owner to
   choose between this and a standing ruling. dOrderedCharter's decision principles (`cl-dClosedLoop-0032`) are the
   product's answer.

Nothing in the driver judges whether a resolution was sound. The spec audit, the closing review and the owner's
reading of the report are what read it.

### What the owner sees at each spec landing

- **The landing diff**, which is `memory/` only: the specs, the audit records, the closing review, the departures
  report and the re-rendered packet. A product path in a spec run's diff means the run built code against the
  README's rule.
- **The coverage report**: `carries.py --report <slug>` inside the departures report until dTrueNorth lands, and the
  README's generated coverage region after it (`cl-dClosedLoop-0003`).
- **Every departure from v2**, with its record, every fork the run settled, and every unit carried forward.

Nothing waits for the owner. The owner's next act is starting the build run when the script names it, so code starts
only after the owner has had the coverage in front of them (ER:79-80).

## [handoffs]

**The packet** is one per build, generated (P0.3) and committed with the opening. It orients any session on any
node; it travels in git because the card never leaves its node (GR:142).

**The per-pass brief** uses today's mechanism:
1. `handoff.py render --build <chain build> --unit <id> --input prompt=<packet>`, which adds the unit's clauses and
   its write set.
2. Record it with `--brief <slug> --unit <id> --path <file>` (VERBS:697-699).

It is rendered only under the chain build, once its folder has landed. Rendered under dClosedLoop, it carries
dClosedLoop's goal (handoffs return, candidate C), and `handoff.py` refuses a build folder that does not exist
(`handoff.py:317-319`).

**What a cold session reads, in order**, on any node, for a run or an attended pickup:
1. Under a mandate, `unattended.sh --status <slug>`; otherwise `git log --oneline -5` (METHOD:240).
2. The build's `RUN.md` whole, when it exists (METHOD:241-242).
3. The README: its roster mapped to clause ids, its build-level rules, `parents:`, `may:` and `spec-audit:`.
4. The packet, with `packet.py --check <slug>` green.
5. METHOD whole (METHOD:243).
6. The current spec whole (METHOD:244).
7. The recall probe, with the terms in that spec's §10 (METHOD:245).

**Keeping a packet current.** A packet goes stale when:
- a deviation record lands in its build's or an ancestor's `build/`;
- a parent's state moves;
- the gap register changes;
- an instrument's blob moves.

The build's own runs re-render it: `--check` at every M7 reground (METHOD:231-246), and on red, re-render and commit
before the next pass. A run never writes another build's packet, since `--close` refuses a commit belonging to
another build (VERBS:860-862).

## [coordination]

**The node loop**, at every landing and whenever a node is free:

| Actor | Step | Rests on |
|---|---|---|
| Node | `git fetch`, then `unattended.sh --claims`, which fetches every claim into the local cache | `unattended.sh:2136` (coordination return); VERBS:769-774 |
| Node | `python build/…-schedule.py --ref origin/main`. It pins every live or held chain claim to its node and derives each build's phase from the specs on `origin/main` | P0.4 |
| Node | The run the table shows on this node at time 0 is this node's next run. With none, the node has no ready chain run | [schedule] |
| Owner | Starts it in a fresh worktree | PROTOCOL:21-27 |
| Run | Pushes its branch after every pass commit, hold and hand-off. The push is ungated | `.githooks/pre-push:1163` |
| Run | Stops with `--hold --code platform-limit` for a quota limit or an outage, and never goes silent past 90 minutes on a live claim | `.unattended.conf:95`; STOPS:198-204 |
| Run | Lands in place. It never merges into local main | VERBS:916-931 |

**Claim rules.**
- **Never preflight a slug whose claim is not terminal.** Preflight takes a foreign stale claim silently (STOPS:220),
  and its holder then meets check 108.
- **A stale claim** is taken over with `--resume <slug> --keepalive-id <new>` only if `git ls-remote origin` shows the
  holder's branch. Otherwise tell the owner (coordination return; `unattended.sh:8856-8904`).
- **Phase comes from the tree.** A claim reading `landed` may mean a spec run, so the phase is read from the specs
  on `origin/main`, never from the claim. This departs from the coordination return's step 1 ([disagreements]).

**Landing.** Every node may land: `LANDING_NODES` is undeclared, which means every node (PROTOCOL:528;
VERBS:23-26). Peak concurrency is three runs, so a landing meets at most two interlopers against three retries
(`push-main.sh:188`). A `--prepare` conflict is reconciled on the branch: run `git merge origin/main`, resolve,
commit, then `--authorization` and `--prepare` again (`push-main.sh:881-882`; VERBS:921-926). Generated files are
re-rendered, never hand-merged (`AGENTS.md:33`).

**Shared records.**
- `DECISIONS.md` and every `BACKLOG.md` merge by rows; `LIVE.md` and the ledgers are re-rendered (`.gitattributes:71-86`).
- `readme-contract.txt` is written once, by the opening, so no chain run touches it (P0.5).
- The hot shared files (`unattended.sh`, `tools/gate-legs.json` and the renders) meet only at the prepare conflict.
  Of 34 unordered build pairs, 3 name a shared path in v2 (coordination return, §2).

**Asks across builds.** A problem in another build is an ask in that build's `BACKLOG.md`, minted under the filer's
own slug and pushed (P0.6). That ask enters the other build's `F` set, so its next close must dispose of it
(ASKS:128-143). A run that has merged `origin/main` checks its own `BACKLOG.md` before `--close`.

**When another node's work is in the way:**
- A live or held claim on the slug: take the next run the script names. Never preflight over it.
- An overlap line at preflight or on the card: if the other ref is a parent, wait; otherwise go on, and the later
  lander reconciles (`unattended.sh:3409`, which always returns 0).
- Foreign commits on local main: `--carry` refuses them, so land from the branch (coordination return).
- Two builds recording contradictory decisions on one key: both rows merge clean (GR:329). The owner arbitrates
  ([cannot]).

## [schedule]

The script was run from the worktree root at HEAD `b6a6c650d`. Its exit code was 0.

```
$ python -B memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 0, builds landed 0
claims cached on chain builds: none live or held
makespan 270 units; with unlimited nodes 197; whole builds after their parents land 276; serial on one node 509

| Build | Stage | Parents | Units | Spec run: node, start-end, slack | Build run: node, start-end, slack |
|---|---|---|---|---|---|
| dTrueNorth | Fidelity | dClosedLoop | 6 | a 0-2, slack 0 | a 2-6, slack 0 |
| dGroundRules | Policy | dTrueNorth | 11 | a 6-10, slack 0 | a 10-17, slack 0 |
| dSafePassage | Supersession | dGroundRules | 13 | d 10-14, slack 3 | d 17-26, slack 4 |
| dOrderedCharter | Foundation | dSafePassage | 37 | a 17-29, slack 0 | a 29-54, slack 0 |
| dFairHearing | Review harness | dSafePassage | 18 | b 17-41, slack 19 | d 41-53, slack 16 |
| dDeclaredLoop | Spine | dOrderedCharter, dFairHearing | 34 | d 53-64, slack 14 | a 64-87, slack 0 |
| dWitnessedBar | Test | dDeclaredLoop | 30 | d 64-74, slack 13 | a 87-107, slack 0 |
| dPlacedRequest | Entry | dDeclaredLoop | 21 | b 64-92, slack 22 | d 92-106, slack 6 |
| dKeptSession | Session | dDeclaredLoop, dPlacedRequest | 28 | d 106-115, slack 11 | a 116-134, slack 7 |
| dBoundRoles | Roles | dDeclaredLoop, dWitnessedBar, dPlacedRequest | 26 | a 107-116, slack 12 | a 134-152, slack 3 |
| dTotalRecall | Memory | dDeclaredLoop, dWitnessedBar, dPlacedRequest | 26 | d 115-124, slack 12 | d 144-161, slack 3 |
| dFurnishedOrders | Orders | dBoundRoles | 20 | b 116-142, slack 41 | a 160-173, slack 30 |
| dWellOiledMachine | Runtime | dBoundRoles, dTotalRecall, dKeptSession | 61 | d 124-144, slack 0 | d 161-202, slack 0 |
| dLinkedLibrary | Library | dTotalRecall | 25 | a 152-160, slack 25 | a 173-190, slack 16 |
| dIndexedDesign | Design | dDeclaredLoop, dTotalRecall, dKeptSession, dBoundRoles, dLinkedLibrary | 16 | a 190-195, slack 28 | a 195-206, slack 16 |
| dRankedPlan | Plan | dDeclaredLoop, dTotalRecall, dBoundRoles | 16 | b 142-163, slack 45 | d 202-213, slack 33 |
| dTendedCadence | Maintain | dWitnessedBar, dRankedPlan, dWellOiledMachine, dIndexedDesign, dFurnishedOrders | 18 | a 206-212, slack 21 | d 213-225, slack 0 |
| dMindYourWords | Lexicon | dWellOiledMachine, dWitnessedBar, dLinkedLibrary, dFurnishedOrders | 17 | b 163-185, slack 47 | a 223-234, slack 12 |
| dCalibratedLens | Review | dTendedCadence, dFairHearing | 17 | a 217-223, slack 6 | d 225-236, slack 0 |
| dShippedRelease | Deploy | dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine, dLinkedLibrary, dFurnishedOrders | 31 | b 185-226, slack 33 | a 234-255, slack 3 |
| dScopedBuild | Build | dIndexedDesign, dWitnessedBar, dWellOiledMachine, dFurnishedOrders | 15 | a 212-217, slack 35 | d 236-246, slack 13 |
| dConvergedCharter | Convergence | dScopedBuild, dShippedRelease, dCalibratedLens, dMindYourWords | 23 | d 246-254, slack 4 | a 255-270, slack 0 |

node a: busy 260 of 270 (96%), work 260 of 509 units, 22 runs: 9 spec, 13 build
node d: busy 208 of 270 (77%), work 208 of 509 units, 16 runs: 7 spec, 9 build
node b: busy 162 of 270 (60%), work 41 of 509 units, 6 runs: 6 spec, 0 build

first wave, each node's first run:
  a: spec dTrueNorth at 0
  d: spec dSafePassage at 10
  b: spec dFairHearing at 17

runs the owner starts, 44, at 38 distinct times, in order (time, node, run):
  0 a spec dTrueNorth · 2 a build dTrueNorth · 6 a spec dGroundRules · 10 a build dGroundRules
  10 d spec dSafePassage · 17 d build dSafePassage · 17 b spec dFairHearing · 17 a spec dOrderedCharter
  29 a build dOrderedCharter · 41 d build dFairHearing · 53 d spec dDeclaredLoop · 64 a build dDeclaredLoop
  64 b spec dPlacedRequest · 64 d spec dWitnessedBar · 87 a build dWitnessedBar · 92 d build dPlacedRequest
  106 d spec dKeptSession · 107 a spec dBoundRoles · 115 d spec dTotalRecall · 116 a build dKeptSession
  116 b spec dFurnishedOrders · 124 d spec dWellOiledMachine · 134 a build dBoundRoles · 142 b spec dRankedPlan
  144 d build dTotalRecall · 152 a spec dLinkedLibrary · 160 a build dFurnishedOrders · 161 d build dWellOiledMachine
  163 b spec dMindYourWords · 173 a build dLinkedLibrary · 185 b spec dShippedRelease · 190 a spec dIndexedDesign
  195 a build dIndexedDesign · 202 d build dRankedPlan · 206 a spec dTendedCadence · 212 a spec dScopedBuild
  213 d build dTendedCadence · 217 a spec dCalibratedLens · 223 a build dMindYourWords · 225 d build dCalibratedLens
  234 a build dShippedRelease · 236 d build dScopedBuild · 246 d spec dConvergedCharter · 255 a build dConvergedCharter

landings of build runs, with the runs in flight then and the surfaces the landing's clauses touch:
     6 dTrueNorth lands; in flight: none; surfaces: spec-format 0001,0002
    17 dGroundRules lands; in flight: none; surfaces: charter 0012; hooks 0011
    26 dSafePassage lands; in flight: spec dOrderedCharter on a, spec dFairHearing on b; surfaces: lander 0025; bar 0026,0029; hooks 0023,0024,0026..
    53 dFairHearing lands; in flight: build dOrderedCharter on a; surfaces: charter 0082; bar 0075,0080,0083..
    54 dOrderedCharter lands; in flight: spec dDeclaredLoop on d; surfaces: driver 0032,0047,0048..; lander 0047; charter 0031,0032,0036..; roles 0051; bar 0047,0048; hooks 0038
    87 dDeclaredLoop lands; in flight: spec dPlacedRequest on b; surfaces: driver 0099,0106,0108..; bar 0092,0102,0115; hooks 0091
   106 dPlacedRequest lands; in flight: build dWitnessedBar on a; surfaces: driver 0120,0123,0134; lander 0129; charter 0121; roles 0130
   107 dWitnessedBar lands; in flight: spec dKeptSession on d; surfaces: driver 0344; lander 0342; bar 0339,0342,0344..; hooks 0342,0344
   134 dKeptSession lands; in flight: spec dFurnishedOrders on b, spec dWellOiledMachine on d; surfaces: driver 0504; charter 0141; hooks 0140,0159
   152 dBoundRoles lands; in flight: spec dRankedPlan on b, build dTotalRecall on d; surfaces: charter 0180,0190; roles 0166,0168,0182..; bar 0188,0190; hooks 0190
   161 dTotalRecall lands; in flight: spec dRankedPlan on b, build dFurnishedOrders on a; surfaces: roles 0215,0220,0223..; bar 0237
   173 dFurnishedOrders lands; in flight: build dWellOiledMachine on d, spec dMindYourWords on b; surfaces: driver 0195; method 0195; roles 0202,0203,0209..; hooks 0197,0201,0205
   190 dLinkedLibrary lands; in flight: build dWellOiledMachine on d, spec dShippedRelease on b; surfaces: driver 0240; spec-format 0500; hooks 0244
   202 dWellOiledMachine lands; in flight: spec dShippedRelease on b, build dIndexedDesign on a; surfaces: driver 0280,0281,0301..; lander 0288,0311,0318..; charter 0320; roles 0310,0320; bar 0288,0318,0322..; hooks 0279,0282,0288..
   206 dIndexedDesign lands; in flight: spec dShippedRelease on b, build dRankedPlan on d; surfaces: spec-format 0383; roles 0397
   213 dRankedPlan lands; in flight: spec dShippedRelease on b, spec dScopedBuild on a; surfaces: hooks 0377
   225 dTendedCadence lands; in flight: spec dShippedRelease on b, build dMindYourWords on a; surfaces: bar 0499
   234 dMindYourWords lands; in flight: build dCalibratedLens on d; surfaces: charter 0278; roles 0270; bar 0270
   236 dCalibratedLens lands; in flight: build dShippedRelease on a; surfaces: charter 0462; roles 0463; bar 0468
   246 dScopedBuild lands; in flight: build dShippedRelease on a; surfaces: spec-format 0400; method 0404
   255 dShippedRelease lands; in flight: none; surfaces: driver 0426; lander 0413,0507,0414..; bar 0431; hooks 0427,0431,0437
   270 dConvergedCharter lands; in flight: none; surfaces: driver 0485,0486,0494..; lander 0485; charter 0479,0486,0490..; roles 0485; bar 0485; hooks 0490

node b's pace swept (makespan; busy share of a, d, b; b's runs):
  b 0.25: 270; a 96% d 77% b 60%; spec dFairHearing 17-41, spec dPlacedRequest 64-92, spec dFurnishedOrders 116-142, spec dRankedPlan 142-163, spec dMindYourWords 163-185, spec dShippedRelease 185-226
  b 0.30: 261; a 97% d 80% b 59%; spec dFairHearing 17-37, spec dPlacedRequest 60-83, spec dFurnishedOrders 112-134, spec dRankedPlan 134-151, build dRankedPlan 153-188, spec dMindYourWords 188-207, spec dScopedBuild 207-224
  b 0.35: 260; a 96% d 81% b 54%; spec dFairHearing 17-34, spec dPlacedRequest 57-77, spec dFurnishedOrders 109-128, spec dRankedPlan 128-143, spec dLinkedLibrary 143-166, spec dMindYourWords 166-182, spec dShippedRelease 182-211
  b 0.40: 253; a 100% d 80% b 53%; spec dFairHearing 17-32, spec dPlacedRequest 55-72, spec dFurnishedOrders 107-123, spec dRankedPlan 123-136, spec dLinkedLibrary 136-157, spec dMindYourWords 157-171, spec dShippedRelease 171-197, spec dScopedBuild 197-209
  b 0.45: 243; a 99% d 80% b 69%; spec dFairHearing 17-30, spec dPlacedRequest 54-69, spec dBoundRoles 77-96, spec dTotalRecall 96-115, spec dRankedPlan 115-127, build dFurnishedOrders 127-156, spec dMindYourWords 156-169, spec dScopedBuild 169-180, spec dTendedCadence 180-193, build dScopedBuild 193-215
  b 0.50: 241; a 98% d 75% b 77%; spec dFairHearing 17-29, spec dDeclaredLoop 29-52, spec dPlacedRequest 54-68, spec dBoundRoles 77-94, spec dTotalRecall 94-111, spec dRankedPlan 111-122, spec dFurnishedOrders 122-135, build dFurnishedOrders 135-162, spec dMindYourWords 162-173, spec dScopedBuild 173-183, spec dTendedCadence 183-195, build dScopedBuild 195-215
  a and d alone: 272
```

**The dispatch rule.** It is the script's model, applied at every landing, and the table is only its forecast at the
assumed speeds. Re-dispatching beat a fixed table under ±60% duration noise, with a median of 290 against 306
(schedule return). The rule:
- a free full-pace node (a before d) takes the ready run with the most downstream work;
- node b takes the ready run with the most slack, among those whose slack covers its slowdown, and never a run
  without slack;
- no build run starts until every parent has landed.

A node reads the rule as "the run the table shows on my node at time 0".

**The first wave.**
- Node a takes dTrueNorth's spec run, then its build run.
- Node d runs phase 0 and its own preparation. Its first chain run is dSafePassage's spec run, once dGroundRules'
  specs close.
- Node b is onboarded, and its first run is dFairHearing's spec run.

**Makespan and load.** The makespan is 270 units, against 276 for whole builds after their parents land and 509 run
serially. Node a is busy 96% of the time, d 77% and b 60%.

**Node b's slice**, with b modelled as eligible for both phases ([settle]). At 0.25, b takes six spec runs and no build
run: 41 of 509 units of work, and none with zero slack. From 0.30 it starts taking build runs with slack. The
makespan falls from 270 to 241 as the pace rises to 0.5, against 272 for a and d alone.

The owner's "smaller slice, preferably non-critical" assigns b the spec runs of six builds with slack at Pro pace:
dFairHearing, dPlacedRequest, dFurnishedOrders, dRankedPlan, dMindYourWords and dShippedRelease. b is never on a run
with zero slack.

**What the owner starts.** 44 runs (22 spec runs and 22 build runs) at 38 distinct moments, each when the script
names it. Nearly every start follows a landing, so the owner is needed at about every landing. Resumes after a hold
are the resume tick's, where it is registered (P0.9).

## [sync-points]

These landings change what the nodes load. The runs in flight at each one are the script's landings list, re-derived
at that landing, and are not typed here. A landing's gates reach every later landing through the in-place merge bar
with no step (PROTOCOL:428-432). What follows is what loads at session start or runs from the worktree.

| Landing | What changes | Every node | A spec run in flight | A build run in flight |
|---|---|---|---|---|
| dTrueNorth | `**Carries:**` lines, the carries join in the spec-tokens leg, the coverage region, deviation records and their join, `@rev-N` pins (`cl-dClosedLoop-0001` to `-0006`) | Nothing to install. Every packet's parent state goes stale | none, under J | none, under J |
| dSafePassage | The upgrade-step kind, and `.agent-cap.conf` retired by a step (`cl-dClosedLoop-0018`) | Run the upgrade steps on each machine | Rotate its session at the next pass boundary | Same |
| dOrderedCharter | The charter re-founded and `AGENTS.md` re-rendered (`cl-dClosedLoop-0032`), including the fork-resolving decision principles | Fresh sessions load the new charter. M7 does not re-read it (METHOD:238-246) | Rotate at the next pass boundary. From here, residual forks resolve by the principles (D7) | Same |
| dDeclaredLoop | The roles stage table moved (`cl-dClosedLoop-0086`); `unattended.sh` re-pointed to `review.max-rounds` (`cl-dClosedLoop-0106`); `deviation.approval` (`cl-dClosedLoop-0119`) | Set the chain's `author-recorded` override where the key now lives. The instruments' approval arm retires | Merge `origin/main` at the next pass boundary, then `--authorization` (VERBS:923-926). The prepare lands it through the new driver | Same |
| dPlacedRequest | Run claims migrated onto leases (`cl-dClosedLoop-0120`) | **A barrier**, per D2 | Per D2 | Per D2 |
| dWitnessedBar | The pre-push hook reads a runner-written verdict (`cl-dClosedLoop-0342`) | The next push goes through the new hook | Lands through it | Lands through it |
| dKeptSession | Named presets (`cl-dClosedLoop-0141`); `mailbox.answer` (`cl-dClosedLoop-0504`) | The chain's two deviation values become overrides on `standard` | Nothing | Nothing |
| dBoundRoles | The role roster and definitions rewritten (`cl-dClosedLoop-0166` onward) | Re-render the role agents | Rotate. `handoff.py harness-args` now prints the new roles | Same |
| dTotalRecall | The README's front-matter schema refuses unknown keys (`cl-dClosedLoop-0215`) | The opening's keys are all known (P0.5) | Nothing | Nothing |
| dFurnishedOrders | The per-pass checklist retired from the method and the Skill (`cl-dClosedLoop-0195`) | None | Picked up at the next reground, since M7 re-reads METHOD | Same |
| dWellOiledMachine | The `next` verb, with `--plan` and `--status` re-pointed (`cl-dClosedLoop-0280`); the unattended kit dissolved, with `/unattended` kept as a client of `run` until dConvergedCharter retires it (`cl-dClosedLoop-0306`); `gov-session` retired (`cl-dClosedLoop-0320`) | **The driver's successor.** Runs started after this landing still start with `/unattended <slug>`, now a client of `run`. Its verbs are the ones the landed kit's usage and its landing record name, which each packet re-renders | Merge `origin/main` and run `--authorization` at the next pass boundary. Its landing goes through the successor, under D1's test | Same |
| dIndexedDesign | The Design-to-Build hand-off (`cl-dClosedLoop-0383`) and `design.coverage` (`cl-dClosedLoop-0398`) | `carries.py` stops being run (phase 1 table) | Closes through the new Design exit | Nothing |
| dRankedPlan | Priority beside `parents:` and the plan view (`cl-dClosedLoop-0369`) | The plan view is the product successor of the schedule script's ordering | Nothing | Nothing |
| dScopedBuild | Built specs frozen (`cl-dClosedLoop-0400`); `deviation.gate` (`cl-dClosedLoop-0412`) | Set the chain's `report` override. The `deviations.py` join stops being run | Nothing | It may not revise a landed unit's spec; it adds a unit instead |
| dShippedRelease | The landing record and the lander (`cl-dClosedLoop-0413`) | Every later landing goes through the new lander | Lands through it | Lands through it |
| dConvergedCharter | Every remaining kit conf key folded into the policy file (`cl-dClosedLoop-0485`), and `/unattended` retired | The chain is done; D5 sets the two deviation keys | none | none |

## [deviations]

**The owner's rule, applied** (ER:121-131). A departure is recorded and explained, and it never waits for the owner:
- Approval is `author-recorded`. The run's own author role signs the record, naming its role.
- The gate is `report`. The join never refuses a landing; it lists.
- The instruments carry the same values until the product keys exist (P0.1), and the product carries them by R2.

**What is recorded where.**
- **A departure from v2 or from a spec past its first pass** is a deviation record in the departing build's `build/`,
  `<date>-build-<unit>-deviation-<n>.md`, with the fields `deviations.py:6-16` names. It is written in the departing
  unit's own commit (`cl-dClosedLoop-0004`).
- **A fork the run settled** is a §8 `RESOLVED` mark and a `Decided:` trailer (METHOD:316-320).
- **A unit carried forward** is a defer row in `RUN.md` (VERBS:703-710).
- **A park** is a park row (VERBS:36-46).

**The end-of-build departures report** (P0.2) is generated at each build's end, before `--close`, from those records,
the computed population and M9's derivation (METHOD:293-305). It lists every member, recorded or not, every fork
settled, and every unit carried. A member the report lists as "recorded by nobody" is given its record by the run
before `--close`. That is a step in the README's rules, and it is not gated (R3).

**The as-built roll-up.** `asbuilt.py --write` runs in each record's own commit, until `cl-dClosedLoop-0006`'s
product view takes over at dTrueNorth's landing. It rolls every amends or supersedes row up across the chain
(`build/…-asbuilt.py:2-14`).

**What still detects strictly.**
- The population is computed from history, never declared (`deviations.py:20-27`).
- The carries join reds a ghost id, an unbound spec, a stale pin, an ambiguous carrier, a dropped clause and an
  uncarried one at a Design exit (`carries.py:15-21`). The run clears each by itself, by re-pinning or by writing a
  `Moved`, `Retired` or `Deferred` line with its own decision (R6).
- From dTrueNorth's landing, the product join runs at every node's pre-push, at every `--close` and in CI.

**What nothing catches.**
- A spec that keeps every token and contradicts its clause. Only the spec audit's lens and the owner's reading see it
  (`carries.py:31-33`; `cl-dClosedLoop-0398`).
- A departure made in code alone, which only the closing review sees (`deviations.py:36-37`).
- Whether a record's reason or risk class is honest.
- Two carriers on two branches, until the merged tree (P0.1, row 9).
- Under `author-recorded`, who actually approved.

**Departures this plan proposes from v2.** These are for the owner, and none is applied:

| Proposed | Departs from | Risk | Because |
|---|---|---|---|
| dTrueNorth's stand-in join reads the chain's values, `report` and any recorded approver, until dDeclaredLoop's and dScopedBuild's keys land | `cl-dClosedLoop-0004@c374ccd0`, which fixes the by-risk table and a red on an approver below the risk | loosening, so the owner's | R2: answer 3 cannot hold otherwise between dTrueNorth's and dDeclaredLoop's landings |
| dTrueNorth's product join takes the instruments' plant suite, P0.1's escapes included, as its acceptance | `cl-dClosedLoop-0002@6acd9ea9` and `cl-dClosedLoop-0004@c374ccd0` | stricter | D3 |
| dPlacedRequest's spec carries "a live claim on another node survives the migration" | `cl-dClosedLoop-0120@5d655f07` | stricter | D2 |
| dWellOiledMachine's spec carries "a `/unattended` run in flight at this landing lands after it" | `cl-dClosedLoop-0306@a3aa83b5` | stricter | D1 |

## [per-node]

**Every node's loop** is [coordination]'s. When blocked, a node takes the case that applies:

| Blocked by | What the node does | Rests on |
|---|---|---|
| A usage limit or an outage | `--hold --code platform-limit` or `platform-unavailable`, with the branch pushed first | VERBS:949-962 |
| A red that is its own | Fixes it | STOPS:107-111 |
| An inherited red | Lands under `INHERITED_RED=land` | `.githooks/gate-env.sh:103` |
| No ready run in the table | Nothing on the chain; waits for the next landing | [schedule] |

**Node a**, `daily-agent` (`fleet.toml:21-26`): 16 cores and 32 GB, one Max plan serving three projects
(`cloud-and-scale.md:434-436`).
- **Setup:** P0.9.
- **First assignment:** dTrueNorth's spec run at 0, then its build run (phase 1).
- **Load:** the critical path through dGroundRules, dOrderedCharter, dDeclaredLoop and dWitnessedBar, at 96% busy.
- **At sync points:** rotate the session as [sync-points] says. Its build run of dDeclaredLoop is a self-rewriting
  build (D1).

**Node d**, `d41ly` (`fleet.toml:42-46`; its `host` is blank, which the claim does not read): 16 cores and 32 GB,
one Max plan serving five projects.
- **Setup:** P0.9, and it runs phase 0 first: the instruments, the opening and the decision rows.
- **First chain run:** dSafePassage's spec run at 10.
- **Load:** dWellOiledMachine's build run is its longest (61 units), and it rewrites the driver (D1). It also carries
  the dPlacedRequest build run, which is the barrier (D2).

**Node b**, `agent5` (`fleet.toml:28-33`): 4 cores and 8 GB, a Pro plan, today working only for inCMS and NicoCares.
- **Setup:** P0.9's onboarding row.
- **First run:** dFairHearing's spec run at 17.
- **Load:** spec runs with slack at Pro pace, and build runs with slack once its measured pace passes 0.3
  ([schedule]).
- **At sync points:** rotation as for a and d. b's slower runs are more often in flight at a landing, so it merges
  `origin/main` at each pass boundary.

## [owner]

| When | The owner's step | Rests on |
|---|---|---|
| Now | Walk this plan. Answer R1 to R6 and rule on D1 to D8 | [defaults] |
| After approval | Let node d's session run phase 0 | [phase-0] |
| Phase 0's end | Read the opening diff (every README, grant, packet and decision row) and ask for its landing | P0.7 |
| Each moment the script names | Start the run, `/unattended <slug>`, on the named node, in a fresh worktree: 44 runs | [schedule]; PROTOCOL:21-27 |
| Each spec landing | Read the build's coverage report and departures report before starting its build run | [phase-2] |
| Each build landing | Read the departures report, and rule on any carried-forward unit (D7) | [deviations] |
| At the barrier and the driver landings | Confirm the drain or the test (D1, D2) | [sync-points] |
| At dDeclaredLoop's and dScopedBuild's landings | Set the chain's override values in the policy file the product built (guarded) | [sync-points] |
| After dConvergedCharter | Set the two deviation keys (D5) | [defaults] |

## [cannot]

Every limit the five returns name, merged where two name the same one. Each is either designed around, with the
section that does it, or listed with its smallest change and that change's kind.

| Limit | Named by | Disposition |
|---|---|---|
| No spec audit unless the owner opts in | driver 1 | Designed around: `spec-audit:` in all 22 landed READMEs (answer 2, P0.5) |
| Governance-carrier and public-surface forks park; `may:` was never exercised | driver 2 | Designed around: the grant (answer 2, R1); proven in phase 1 |
| "Governance carrier" is defined nowhere | driver 2 | **Cannot.** A policy: a decision row defining it |
| No parallelism inside a build; no sharing one build across nodes | driver 3, coordination | Designed around: split phases across builds. Lifting it is a chain build's unit: dPlacedRequest's unit leases (`cl-dClosedLoop-0120`) |
| Builds that rewrite their own driver | driver 4 | Designed around by D1 and the [sync-points] rows |
| A cross-node take-over needs the branch on the remote; no rule says when a branch is pushed | driver 5, coordination, handoffs 6 | Designed around: a policy, push after every pass commit, hold and hand-off (P0.8) |
| The resume tick is not registered on node d | driver 6 | Designed around: a manual step on each node (P0.9) |
| Every chain build pays the bar, and there is no landing queue | driver 7 | Designed around: contention measured at most two interlopers against three retries. A real queue is a chain build's unit (GR:113) |
| Nothing orders builds by their parents; preflight does not refuse a child whose parent has not landed | driver 8, coordination, schedule 2 | Designed around: a manual step, the schedule script at every landing (P0.4). A dependency gate is a dPlacedRequest unit, and the ordering's product is dRankedPlan's (`cl-dClosedLoop-0369`) |
| No Definition-of-Done item compares a spec to the design | driver 9, deviation 1 | Designed around: the instruments by hand, then dTrueNorth's product join (phase 1) |
| No path exclusion between builds | coordination | **Cannot.** A dPlacedRequest unit; until then, pushed branches and the prepare reconcile |
| Preflight silently takes a stale claim | coordination | **Cannot.** A unit of the chain build that owns claims, dPlacedRequest. Until then, a policy: never preflight over a claim |
| `readme-contract.txt` conflicts on concurrent opens | coordination | Designed around: all 22 rows in the one opening (P0.5) |
| No cross-node channel; two builds' contradictory decisions both merge clean | coordination (GR:329, :331) | **Cannot.** A manual step: the owner arbitrates. The channel is dKeptSession's `mailbox.answer` (`cl-dClosedLoop-0504`) |
| "Seed local memory from the in-repo mirror" names no mirror | coordination | **Cannot.** A manual step for node b, and a record fix for the playbook stream (`AGENTS.md:114`) |
| The card never leaves its node | handoffs 1 | Designed around: the packet in git (P0.3) |
| No tool renders or checks a packet's content | handoffs 2 | Designed around: the packet instrument (P0.3). Its product owner is dFurnishedOrders |
| `handoff.py` refuses an unopened build, and renders the wrong scope under dClosedLoop | handoffs 3 | Designed around: a policy, render only under the opened chain build ([handoffs]) |
| A spec may carry another build's clause unrefused | handoffs 4 | Designed around: an instrument fix (P0.1, row 1) |
| A parent's promises are joined only inside one build | handoffs 5 | Designed around: a manual step. The packet lists them and the receiver checks them at its Design exit (P0.3, field 4) |
| The local anchor refuses `spec-audit:` in a `slug` README | handoffs 7 | Designed around: READMEs landed on the default branch (IR:862-869) |
| `handoff.py` drops the `(1)` of a numbered To-do | handoffs 8 | **Cannot.** A chain build's unit in the roles kit (dBoundRoles) |
| A spec-only run cannot close except by carry-forward | schedule 1 | Designed around: a policy ratified by answer 1 ([phase-2]) |
| A unit a spec run adds is never carried forward | this plan (STOPS:703-704) | **Cannot.** A policy, D6, for the chain. The kit's change is a chain build's unit, under dIndexedDesign's Design-to-Build hand-off (`cl-dClosedLoop-0383`) |
| Nothing finds or offers work to a node | schedule 3 | Designed around: a manual step, the script at every landing ([coordination]) |
| Running sessions do not reload the charter, roles or hooks; installs are per node | schedule 4 | Designed around: manual steps at the sync points ([sync-points]) |
| dPlacedRequest's migration while other runs are live | schedule 5 | Designed around by D2 |
| An owner's approval cannot be verified | deviation 2 | Designed around: under `author-recorded` no owner approval is needed during the chain |
| A semantic contradiction or a code-only departure | deviation 3 | **Cannot.** A manual step: the audit on all 22 builds, the owner reading each coverage report, and the closing review |
| A dropped clause after a later edit | deviation 4 | Designed around: an instrument fix (P0.1, row 2), and `carries.py --exit` at each Design exit until `cl-dClosedLoop-0003` |
| No driver mode stops a spec run before code | this plan | **Cannot.** A manual step, the README's rule. The product is `cl-dClosedLoop-0383` |
| A residual fork still parks: veto 3, no survivor, or the goal | this plan | **Cannot.** A policy, D7, until dOrderedCharter's `cl-dClosedLoop-0032` |
| The departures report has no Definition-of-Done item that runs it | this plan (`unattended.sh:12225-12226`) | **Cannot.** A manual step in the README's rules. The product is the landing record (`cl-dClosedLoop-0413`) and the deviation gate (`cl-dClosedLoop-0412`) |
| The owned nodes carry no paths for a grant | this plan | Raised as R1 |

## [defaults]

### The readings in question

The plan applies none of the readings below that it finds wrong, and states its recommendation.

- **R1. Answer 2's grant, "derived from the paths of the nodes it owns" (ER:139-140), has no input.** The owned nodes
  are keys with an owner and no path (P0.5). The options:
  - (a) One decision row, landed with the opening, that grants each chain build the governance-carrier and
    public-surface changes its own `[chain]` clauses name. All 22 `may:` lines cite its id. The run's M3 judges
    coverage (`lib-unattended.sh:1455-1458`).
  - (b) The repo-relative paths among each build's own clause tokens. There are 49 tokens, and 9 builds get none,
    dDeclaredLoop among them, though it rewrites the driver. Five paths would be granted to several builds.
  - (c) Paths typed for each build by the opening's author.

  **Recommended: (a).** It is derived from v2, the owner reads it once in the opening diff, and the grant grammar takes
  ids (`lib-unattended.sh:1440-1443`).
- **R2. Answer 3 does change a clause.** `cl-dClosedLoop-0004` fixes dTrueNorth's stand-in join to the by-risk table
  and to a red on an approver below the risk. The options:
  - (a) Build it as written. Between dTrueNorth's landing and dDeclaredLoop's, a loosening departure then reds the bar
    until the owner approves, which is a park.
  - (b) The proposed deviation in [deviations]: the stand-in reads the chain's values, with the owner's answer quoted
    as the approval.

  **Recommended: (b).**
- **R3. `report` lets an unrecorded departure land, while the owner said departures "are recorded".** The plan applies
  `report`, plus a step that gives every listed member a record before `--close`. That step is not a gate. Should the
  product's stand-in and `deviation.gate` instead refuse until a record exists, which only the run need write? That
  would still never wait for the owner. **Recommended:** keep `report` for the chain, as read.
- **R4. "Nothing is parked or blocked" reaches past what today's driver can do.** Residual forks still park. This is
  answered by D7.
- **R5. Answer 1's close holds only for the units a run started with.** This is answered by D6.
- **R6. The readings leave `design.coverage` unset.** The plan keeps `standard`'s `refuse`, because every coverage red
  is one the run clears itself, by re-pinning or by a `Deferred` or `Moved` line with its own decision. So it never
  waits for the owner. Is that "blocked"? **Recommended:** keep `refuse`.

### Decisions carried as recommended defaults

- **D1. The builds that rewrite their own driver: dDeclaredLoop, dPlacedRequest and dWellOiledMachine.**
  - (a) The units that touch the driver go last in their build, by an `order` verb (TEMPLATE-SPEC:83-89). The build
    run lands through its own new code. If that code refuses the landing, the run hands off `owner-landing` and the
    owner lands it. dWellOiledMachine's spec also carries the in-flight test in [deviations].
  - (b) Always end these three with `--handoff --code owner-landing`.
  - (c) Run the three build runs attended.

  **Recommended: (a).** The build goes through to completion by `/unattended`, and its own landing is the first test of
  the new driver. The owner lands only when that test fails.
- **D2. dPlacedRequest's claim migration.**
  - (a) Its spec carries the test that a live claim on another node survives the migration (the proposed deviation).
  - (b) A drain: no other chain run is live or held when its build run reaches the migrating unit.

  **Recommended: (a)**, with (b) as the fallback if that test cannot be written. (a) costs no idle time, and the
  schedule has dWitnessedBar's build run in flight then.
- **D3. How dTrueNorth's comparison replaces the instruments.**
  - (a) Bootstrap legs first, as an extra derived unit running the instruments from `memory/`.
  - (b) The product absorbs the plant suite as its acceptance.

  **Recommended: (b).** Under J no other chain spec exists before dTrueNorth lands, and a run lands as one landing, so
  bootstrap legs would land at the same moment as the product and cover nothing more. They would also add a unit
  departing from v2, and a leg running code any run can edit (the `TOOL-aStandingWrit-7` class).
- **D4. Who starts each run.**
  - (a) The owner types `/unattended <slug>` on the named node, as protocol §1's owner act (PROTOCOL:21-27).
  - (b) Each node's attended session starts the run the script names, under a standing ruling. This gives up the
    slug narrowing the owner's typing provides (PROTOCOL:97-98).
  - (c) A scheduled task on each node starts runs.

  **Recommended: (a)**, 44 starts.
- **D5. The two deviation keys after the chain.**
  - (a) Back to `standard`'s `refuse` and `by-risk` (v2:1609-1610).
  - (b) Keep `report` and `author-recorded` as overrides.
  - (c) `warn-and-ask` with `by-risk`.

  **Recommended: (a).** The override serves the chain's unattended execution.
- **D6. A spec run that adds units, from a promoted finding or an adopted discovery.**
  - (a) An owner ruling (P0.8): such a run closes with `--close --override build-complete --reason "<the added units,
    built by the build run under ruling <id>>"`. The driver admits that override (`unattended.sh:918`), though the
    verbs say to hand off (VERBS:893-900).
  - (b) Hand off `owner-decision`, and the owner lands the spec run.
  - (c) The spec run builds its added units.

  **Recommended: (a).** It is recorded and surfaced, never waited on, and the build run builds the units.
- **D7. Residual forks, until dOrderedCharter's decision principles land.**
  - (a) Carry the dependent unit forward. The build lands, the departures report lists it, and the owner rules before
    a further run builds it.
  - (b) A standing owner ruling: take the most feature-rich option that fails only veto 3 or the goal bound, recorded
    as a departure.

  **Recommended: (a).** Veto 3 guards security surfaces, which the charter denies by default.
- **D8. Who mints a chain build's roster ids and its carry-forward ask.**
  - (a) The opening, under each chain slug (P0.6).
  - (b) Each spec run.

  **Recommended: (a). It is forced:** a roster minted by the spec run is not the roster that run started with, so
  STOPS:703-704 refuses every carry-forward.

## [disagreements]

| Where | Which the plan follows, and why |
|---|---|
| Whole build per run (driver A, coordination C1) against split phases (schedule) | Split phases: answer 1 chose them. Split is two runs, a landed spec run and a later build run taking over a terminal claim (STOPS:221). It is not the hold-and-resume hand-off coordination's C3 rejected |
| Opting into the audit through `authorized-by: prompt` (handoffs, limit 7) against a `slug` README landed on main (driver A) | Driver A: answer 2 needs `may:`, which prompt mode refuses (`unattended.sh:4160-4163`). The main loop read A's path at IR:862-869 |
| Park loosening and breaking deviations for the owner (deviation, recommendation 2) against answer 3 | Answer 3 binds; the plan follows the readings (ER:121-127) |
| Bootstrap legs as dTrueNorth's first unit (deviation, recommendation 1) | D3 (b), for the reason given there |
| A build is ready when its parents' claims read `landed` (coordination, step 1) | The tree: with split phases a `landed` claim may be a spec run, so phase is read from specs on `origin/main` (P0.4) |
| Stagger landings by owner order (driver, limit 7) against contention being too low to need it (coordination, test 4) | Coordination: it measured at most two interlopers against three retries |
| 262 units (schedule, HEFT) against its own stated rule, "the free node takes the ready phase with the most downstream work" | The stated rule, which a node can apply at a landing without a plan; the script gives 270. HEFT's 262 comes from holding a node for a more critical run about to become ready, which a re-derived table can also do if the owner prefers |
| Node b spec-only (schedule) against "spec and build" (answer 4) | Answer 4: b is eligible for both, and the slack rule keeps it off the critical path |
| "Records-only landings are cheap" (schedule) | Partly: an in-place close runs the bar under `GATE_FULL=1` whatever the diff (PROTOCOL:428-432). A spec run is spared only the self-tests (`.unattended.conf:40`) |
| `BUILD-METHOD` "MUST run concurrently" against a strictly sequential harness (driver) | The code (`unattended-build.js:76-80`) |
| "Claims never age" (GR:323, theme T5) against the code (coordination) | The code: a `live` claim turns `stale` at 5400 s, and only `held` never ages (`unattended.sh:2177-2186`) |
| Several returns: forks the run cannot settle are parked BLOCKED | Answer 3 and its reading: the plan carries the unit forward and lands the build (D7), and states the residue as bad news 2 |
