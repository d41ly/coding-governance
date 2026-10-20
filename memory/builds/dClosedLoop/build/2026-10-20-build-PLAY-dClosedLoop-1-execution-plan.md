# Execution plan: the chain specced, built and landed on nodes a, b and d under today's gov

**Serves:** research PLAY-dClosedLoop-1

The plan the execution record asked for, written from the five execution returns and the owner's four answers. It
opens nothing and changes nothing. Every step below that writes a chain build's file, a policy line, a decision row
or product code runs only after the owner approves this plan, and the baseline's stop holds until then
(`build/…-execution.md:5-7`). The schedule is not typed here. It is the output of
`build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`, kept beside this record and re-run at every landing.

The owner's answers to the plan's open choices (ER `[answers-2]`, ER:166-286) and to the four points that fold left
open (ER `[answers-3]`, ER:306-350) are folded in. Each item they decide now reads as decided and quotes the answer;
the items the owner was not asked are carried as recommended, for the walk (ER:272-276).

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

   Three kinds of fork would still park: one whose only options widen a security, data or write surface (veto 3),
   one with no surviving option, and one the goal cannot survive (METHOD:81, :93-97). The owner chose a standing
   ruling for them: "Standing ruling" (ER:240). The run takes the most capable option that fails only veto 3 or the
   goal bound, and records it as a departure. For a fork with no option left at all, the owner chose "Relax the
   weakest bound" (ER:328): the run drops the least important failing criterion or non-goal, records it as a
   departure, and builds. Nothing waits on the owner. The price is that a security, data or write surface may widen,
   and a unit's own acceptance may be rewritten, unreviewed until the owner reads the build's departures report,
   where both kinds of choice are listed first. dOrderedCharter's fork-resolving decision principles
   (`cl-dClosedLoop-0032`) are the product's answer.
3. Today's carry-forward close refuses every unit a run adds (STOPS:703-704; `unattended.sh:5177-5184`), and every
   confirmed review finding is promoted to a unit (METHOD:144, :274). The owner called that refusal a bug for
   review-promoted units (ER:196-197), and chose to fix it in dTrueNorth: "dTrueNorth's extra unit (Recommended)"
   (ER:232). Then, for a discovery a spec run adopts: "Carry it too (Recommended)" (ER:320). dTrueNorth runs as one
   whole run, spec and build together, so it needs no carry-forward itself, and it carries one unit beyond v2 that
   lets a spec run carry ANY unit it adds, from a review or an adopted discovery, forward to its own build run, once.
   Every later spec run closes with it. Until it lands, nothing but dTrueNorth runs.
4. Two readings of the owner's first answers did not hold as written, and the owner has settled both: the `may:`
   grant is one decision row (ER:181), and the departure from `cl-dClosedLoop-0004` is a deviation the owner
   approves (ER:189).
5. Node b buys little, and the owner chose "Spec runs only" for it (ER:219). At Pro pace (0.25 of a or d) the chain
   takes 271 units with b and 273 without it. b gets six spec runs and 41 of 510 units of work ([schedule]).
6. Three builds rewrite the driver they run under: dDeclaredLoop (`cl-dClosedLoop-0106`), dPlacedRequest
   (`cl-dClosedLoop-0120`) and dWellOiledMachine (`cl-dClosedLoop-0306`). Every run still in flight at one of those
   landings then lands through the new code. The driver runs from the worktree, and the prepare merges the new tip
   in (`.claude/skills/unattended/SKILL.md:9-12`; PROTOCOL:575-576; `tools/push-main.sh:873-884`).
7. The owner starts 43 runs, at 37 distinct moments, nearly one per landing ([schedule]), and chose to type every
   one: "You type it (Recommended)" (ER:270). Nothing picks the next run or offers it to a node (GR:337, :340).
8. No driver mode stops a run once its specs are written. A spec run stops because its README's rule says so, and
   nothing refuses one that goes on to build (`tools/workflows/unattended-build.js:6-8`; VERBS:753-762).

**The plan in brief.**
- **Phase 0, node d, records only, one owner landing.** dClosedLoop's session hardens the three instruments, adds a
  departures report, builds the packet instrument, commits the schedule script and opens all 22 builds in one
  landing the owner makes. It also records the ratified policies as decision rows and prepares nodes a, b and d.
- **Phase 1, node a.** dTrueNorth runs as one whole run: it specs, audits, builds and lands its six clauses and its
  extra unit. It proves the landed-README opt-in and the grant, the product comparison that replaces the instruments,
  and the carry-forward condition every later spec run closes with.
- **Phase 2, the chain.** Every other build gets a spec run, then a build run. Each runs on the node the schedule
  script names when re-run at each landing; node b takes spec runs only. Policy J holds: a spec starts once
  dTrueNorth has landed, its parents' specs have closed and its grandparents have landed; a build starts once its
  parents have landed. dGroundRules' spec run is the first spec run, and the first to close by carry-forward.
- **Deviations.** A departure is recorded by the run that makes it and approved by its author; the owner has
  approved the plan's own departures from v2 in advance ([deviations]). A report generated at each build's end
  explains every departure, a widened surface or a relaxed bound first, and nothing waits for the owner.

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
| The second term refuses every unit the run added, a review-promoted or adopted one included, until dTrueNorth's extra unit changes it | `unattended.sh:5156`, `:5177-5184`; STOPS:703-704 |
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

**What it lists**, in this order:
- first, side by side, each choice that widens a security, data or write surface under the owner's standing ruling
  (ER:240, :284-285), and each bound a run relaxed for a fork with no option left (ER:328, :347-348). The run marks
  the first kind by writing `widens: <surface>` and the second by writing `relaxes: <bound>`, in its §8 mark and in
  its `Decided:` trailer, a rule each README carries (P0.5);
- each member, with its address and hand-off, the record it joins or "recorded by nobody", and the record's reason,
  risk, approver and follow-through;
- each other fork, with its question, pick, reason and source line;
- each carried unit, with its ask, and each unit a spec run added, from a review or a discovery, and carried to its
  build run.

`--write` writes it as `memory/builds/<slug>/build/<date>-build-<first unit>-departures.md`, and `--check` renders it
again and compares the bytes.

**Acceptance.** `--fixture` lists each population plant of P0.1.

**Red tests.**
- A planted `Decided:` trailer missing from the written report reds `--check`.
- A planted `widens:` choice listed anywhere but first reds `--check`.
- A planted `relaxes:` choice listed anywhere but first reds `--check`.
- A planted `relaxes:` choice whose record names no tier and no reason for the bound it dropped reds `--check`
  ([phase-2], rung 6).
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
  gaps gap-design-13, gap-build-07 and gap-mem-47. Field 9 also carries dTrueNorth's extra unit, the decision row it
  derives from, and the two owner-approved records its run writes ([deviations]).
- Once the opening exists in a scratch clone, `handoff.py render --build dTrueNorth --unit <its first unit> --input
  prompt=<packet>` renders, and `handoff.py check` is green on the result.

### P0.4 The schedule script

This record's script: `build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`. Its docstring names its inputs, its
model and what it does not model.

**Acceptance.** It reads v2, the chain builds' specs and the cached claims at a ref. At every landing a node runs
`python <script> --ref origin/main` after `git fetch` and starts the run its table shows on that node at time 0.

**The owner's answers in the model.** dTrueNorth is one whole run of seven units, its six clauses and the extra
unit (ER:232), and node b is offered spec runs only (ER:219). Both are declared in the script as `WHOLE`, `EXTRA`
and `SPEC_ONLY`, each citing its answer, because no file the script reads holds them yet.

**Red tests**, observed on 2026-10-20 in a `--shared` clone in the plan writer's scratch folder, with the script as
the answers changed it; phase 0 runs them again before the landing:

| Plant | Result |
|---|---|
| `cl-dClosedLoop-0509` dropped from v2 | Exit 1: "holds 22 builds and 508 clause ids … not 22 and 509" |
| Two dTrueNorth specs carrying `cl-dClosedLoop-0001` to `-0006`, at `DEFERRED` | Its whole run still starts at 0: a whole run is done only when it lands |
| The same specs at `CLOSED` | dTrueNorth reads `done`; dGroundRules' spec run starts at 0 |
| A cached `live` claim of user `agent5` on dGroundRules | Its spec run is pinned to node b at 0, and its build run goes to a full-pace node |
| A claim naming user `nobody` | Exit 1: the fleet names no such node |

**Not checked.** The extra unit carries no clause, so the tree state cannot see its spec; dTrueNorth reads landed
once its six clauses' specs are closed (the script's docstring says so).

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
| `may:` | The grant decision row's id, on all 22; dTrueNorth's line also cites the extra unit's decision row, since the carry-forward condition is a change to a governance carrier no `[chain]` clause names | ER:181; `lib-unattended.sh:1440-1478`; METHOD:82 |
| H1 and stage | `# <slug> — the <Stage> build of the dClosedLoop chain` | v2:1762-1785 |
| The five slots | Derived bodies, as the scaffold writes them: the problem slot is the build's owned gaps at the baseline (it is the goal bound); the improvements are its clauses carried and built; the detriments are its gaps left open and its children waiting; the build-level rules are below; the parked decisions are "none" | `gen_build_index.py:122-131`, `:3507-3560` |
| `roster:units` | One unit per clause, in clause order: its id, `cl-dClosedLoop-NNNN@<hash8>`, and the clause's text to its first comma. dTrueNorth's roster adds a seventh row, the extra unit, its carries cell `**Derived:**` from its decision row | v2:1762-1785; `carries.py:11`, `:78-80`; ER:232 |
| Unit family | TOOL for every unit; a unit's spec header `streams` records the disciplines it serves | `.memory-tree.conf:42`; TEMPLATE-SPEC:56-77 |
| `BACKLOG.md`, one ask, for every build but dTrueNorth | "build every roster unit of this build from its spec", filed for the spec run's carry-forward, with its `SEV` row. dTrueNorth runs whole and closes without carry-forward, so it gets none | STOPS:707-709; ASKS:92-100; ER:232 |
| Packet | P0.3 | above |
| `readme-contract.txt` rows | 22 bound rows (bare paths); the exempt pin is unchanged | `memory/project/readme-contract.txt:1-29`; `.unattended.conf:383-405` |

**Build-level rules each README carries:**
1. dTrueNorth's README: one whole run specs, audits, builds and lands every unit (ER:232). Every other README: a run
   that finds any roster unit `MISSING` is this build's spec run. It specs every unit, runs the audit, defers every
   unit and closes by carry-forward, every unit it added included, from a review or a discovery, each specced,
   audited and recorded as a departure (ER:314-320). A run that finds none `MISSING` is the build run, and it builds
   every carried unit, never deferring an added one again. The phase is read from the tree, never typed
   (METHOD:39-42; VERBS:72-87).
2. The reading order ([handoffs]), and `packet.py --check <slug>` green before the first pass.
3. Push the run branch after every pass commit, hold and hand-off.
4. Before `--close`, write the departures report with `deviations.py --report <slug> --write`.
5. The chain's deviation values are `report` and `author-recorded` (ER:121-127; ER:255).
6. Forks are settled as [phase-2] says. A choice taken under the standing ruling that widens a security, data or
   write surface carries `widens: <surface>` in its §8 mark and its `Decided:` trailer (ER:240, :284-285); a bound
   relaxed for a fork with no option left carries `relaxes: <bound>`, with its tier and reason (ER:328).

**The `may:` grant, decided.** The owner: "One decision row (Recommended)" (ER:181). One `DECISIONS.md` row, landed
with the opening, grants each chain build the governance-carrier and public-surface changes its own `[chain]` clauses
name, and all 22 `may:` lines cite its id; the run's M3 judges whether a change is covered
(`lib-unattended.sh:1455-1458`). It replaces the derivation answer 2 first read, which had no input: v2's owned nodes
are keys with an `owner` relation and no path (`carries.py:104-113`; the plan writer's probe of every namespace of
`build/…-map.py`'s `derive()`).

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
1. The opening (dClosedLoop's session) mints each build's roster ids, dTrueNorth's extra unit included, and the one
   carry-forward ask of each build but dTrueNorth, under that build's slug. It mints them once, in one landing, before
   any claim exists. A session's ids are its own, and the later merge re-mints unmerged ones (HYGIENE.md:172-187).
   This departs from minting one slug per session; it is D8, carried as recommended for the owner's walk (ER:276).
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
| Owner | Reads the opening diff: every README, its `may:` line, every packet and every decision row | ER:181 |
| Owner | Asks for the landing | the charter's `[land]`, `AGENTS.md:31` |
| Node d's session | Lands through `bash tools/push-main.sh`. The pre-push bar takes the doc-only class, because the diff is `memory/` only | `.githooks/pre-push:1215-1223`; `.githooks/gate-env.sh:106-108` |

### P0.8 The policies the answers ratify, as decision rows

One `memory/DECISIONS.md` row each, minted under dClosedLoop's slug (`missing:PLAY-dClosedLoop-2` onward) and landed
with the opening. Each row cites its source:

1. The spec-run close by carry-forward (ER:84), and the owner's choice of where the units a spec run adds go:
   "dTrueNorth's extra unit (Recommended)" (ER:232) and "Carry it too (Recommended)" (ER:320). This row is the decision dTrueNorth's extra unit is
   `**Derived:**` from, and it records the owner's approval of that unit as a departure from v2 ([deviations]).
2. The grant: "One decision row (Recommended)" (ER:181). This row is the one all 22 `may:` lines cite.
3. The chain's deviation values, `report` and `author-recorded`, applied to every run and to the instruments
   (ER:103-104, :121-127, :255), and the owner's approval of the departure from `cl-dClosedLoop-0004`: "A deviation,
   your values (Recommended)" (ER:189).
4. Node b: "Spec runs only" (ER:219), as the schedule script's rule.
5. The standing ruling for residual forks: "Standing ruling" (ER:240), and for a fork with no option left, "Relax the
   weakest bound" (ER:328). Each choice is recorded as a departure; a widened surface and a relaxed bound are listed
   first in the build's departures report (ER:284-285, :347-348).
6. The driver-rewriting builds land through their own new code (ER:248), dPlacedRequest's migration carries its
   test (ER:264), and the owner types every start (ER:270).
7. The coordination rules: push after every pass, never preflight over a claim, re-run the schedule at every landing,
   and reconcile at a prepare conflict ([coordination]).

**Acceptance.** Every row quotes its answer in ER `[answers]` or `[answers-2]`, or names the `[defaults]` item it
carries for the owner's walk.

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

dTrueNorth runs on node a as the pilot, as ONE whole run: it specs, audits, builds, reviews and lands all seven of
its units. The owner chose it: "dTrueNorth's extra unit (Recommended)", whose option reads "dTrueNorth runs as one
whole run, spec and build together, and adds the fix as one unit, a departure from v2 the owner approves" (ER:224-232).
Its run lands before any other chain spec is written, because the coverage and deviation gates must stand before the
first chain spec (FQ:276-278, :302-303). Being whole, its run closes without carry-forward, and the owner sees its
coverage in its departures report after its code, not before: the price of that choice.

**Its units.** The six clauses of its v2 row, `cl-dClosedLoop-0001` to `-0006`, and the extra unit.

**The extra unit**, a departure from v2 the owner approved (ER:232; [deviations]). It changes the carry-forward
term's second condition (`unattended.sh:5156`, `:5177-5184`; STOPS:703-704) so that:
- a spec run, a run that closes no unit, may carry forward a DEFERRED unit it added, whether its own spec audit or
  its own closing diff review promoted it (METHOD:144, :274) or the run adopted it as a discovery (PROTOCOL:640-690),
  to its own build's next run, once. The owner: "Carry it too (Recommended)", whose option reads "widen dTrueNorth's
  extra unit so any unit a spec run adds carries forward to its own build run once" (ER:314-320);
- that next run must build it: deferring it a second time is refused, at the close, naming the unit;
- a unit added by a run that closes a unit, a build run or a whole run, is refused as today: it is built in that run.

The other four terms are unchanged, so an added unit carries forward only with spec status `DEFERRED`, a defer row,
and a header that advances the build's ask (STOPS:700-711). The spec run specs and audits every unit it adds, through
the harness's audit scoped to the added ids (`unattended-build.js:180-183`), and records each as a departure, with
follow-through "new unit <id>" (ER:315-316). Its spec states how the driver tells a run that closes no unit and a unit
the run added, from the starting roster and the defer and add rows (`unattended.sh:5177-5184`; VERBS:703-710), and
re-renders STOPS §15's second term and the verbs' close rule 9 from their templates. Its red cases, each seen red
before the change and as stated after it:
1. a spec-run fixture with one review-promoted DEFERRED unit: refused before, carried after;
2. a spec-run fixture with one adopted discovery's DEFERRED unit: refused before, carried after;
3. the next run deferring either carried unit again: refused;
4. a unit added and deferred by a run that closed a unit: refused, before and after.

It edits `tools/unattended/`, so dTrueNorth's close owes the flagged bar with its self-tests (`.unattended.conf:40`).
It is a driver-touching unit, so under the owner's "Land through new code (Recommended)" (ER:248) it goes last in
the run, and dTrueNorth lands through it.

**Preconditions:** the opening has landed, with the two decision rows dTrueNorth reads (P0.8, rows 1 and 3).

| Actor | Step | Rests on |
|---|---|---|
| Node a | `git fetch`. The schedule script with `--ref origin/main` shows `a: whole dTrueNorth at 0` | [schedule] |
| Owner, on node a | Create a fresh worktree off `origin/main` on a new branch, open a session there, and type `/unattended dTrueNorth` | PROTOCOL:21-27; `unattended.sh:2929-2938`; ER:270 |
| Run | Schedule the keepalive, then `--preflight`, then `/session-kickoff` | `SKILL.md:16-20`, `:63-65` |
| Run | **Proof 1.** Preflight prints `spec-audit — opted in by README spec-audit: <date>`. `RUN.md` records `anchor-kind: default-branch` and the pinned `may:`, the grant row's id and the extra unit's | VERBS:722-728; IR:862-869 |
| Run | Read in the [handoffs] order; `packet.py --check dTrueNorth` | P0.3 |
| Run | The build harness with the pinned `specAudit`: SPEC authors the seven specs, then AUDIT, then DISPOSAL | VERBS:722-748; `unattended-build.js:6-8` |
| Spec writer | The spec carrying `cl-dClosedLoop-0004` writes the owner-approved deviation record in its own commit; the extra unit's spec carries `**Derived:** <its decision row>` and its own record ([deviations]) | v2:1764; `carries.py:11`; ER:189, :232 |
| Run | At its Design exit, `carries.py --build dTrueNorth --exit` and `deviations.py`, by hand, since nothing in the bar runs them yet | P0.1; deviation return, limit 4 |
| Run | Builds the units one at a time, the extra unit last. The product join takes the instruments' plant suite as its acceptance (D3, carried). Its configuration cutoff is the opening landing's date, so every chain spec, dTrueNorth's own included, falls on or after it | VERBS:697-768; v2:1764; deviation return, recommendation 3 |
| Run | The closing review over the whole range; its promoted units are built in this run, as M4 rules | METHOD:144, :251-290 |
| Run | The departures report, then `--phase VERIFYING`, `--prepare`, `--authorization`, `--close` under `GATE_FULL=1 GATE_SELFTESTS=1`, `--land`, `--landed` | VERBS:849-947 |
| Owner | Reads the departures report and the coverage it carries | [owner] |
| Every node | From this landing, the product join runs in every pre-push bar, every `--close` and remote CI, and every new worktree carries the new carry-forward condition | `.github/workflows/remote-ci.yml:106`; `SKILL.md:9-12` |

**What the pilot proves**, each a first:
1. A README landed on main opts the run into the audit and pins a grant. No run has done either (driver return).
2. A run that changes the driver lands through its own new code, the rule the owner set for the three driver
   builds (ER:248).
3. The product join reds on every plant of P0.1.
4. The carry-forward condition's four red cases.

**What it no longer proves.** Being whole, it does not exercise the spec-run close, the build run's pickup of a
terminal claim (STOPS:221) and its `DEFERRED` units (`unattended.sh:4815`), the ask carried through both runs
(ASKS:136-143), or the harness called again after a spec run's audit (`unattended-build.js:180-230`). dGroundRules'
two runs, which node a starts next, are the first to do each.

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
| Run | A unit the run adds, promoted by the spec audit or the closing review or adopted as a discovery, is specced, audited through the harness's audit scoped to the added ids, recorded as a departure, deferred with `advances <the ask>` and carried forward like the rest, under the condition dTrueNorth's extra unit added | phase 1; ER:232, :314-320; `unattended-build.js:180-183`; PROTOCOL:640-690 |
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
| Run | The harness with the pinned `specAudit`. How its audit stage treats specs the spec run already audited is first observed in dGroundRules' build run | VERBS:722-731; `unattended-build.js:180-230` |
| Run | Per unit: `--brief`, `--dispatch --writes …`, the unit harness, a commit with a `Pass: <unit>` trailer, then `gotchas.py --for-diff HEAD~1..HEAD` | VERBS:697-768 |
| Run | Each unit's header goes `INPROGRESS`, then `CLOSED`. A unit the spec run added and carried is built; deferring it again is refused. The last unit to close carries `closes <the ask>` | TEMPLATE-SPEC:61-82; phase 1 |
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
4. **A strictly beneficial discovery** is adopted (PROTOCOL:640-690). In a spec run its unit is specced, audited,
   recorded as a departure and carried to the build run: "Carry it too (Recommended)" (ER:320).
5. **The owner's standing ruling**: "Standing ruling" (ER:240). Where the only options fail veto 3 or the goal bound
   (METHOD:81, :93-97), the run takes the most capable of them, the one meeting the most stated acceptance criteria
   (METHOD:86), and records it as a departure. A choice that widens a security, data or write surface carries
   `widens: <surface>` and is listed first in the build's departures report (ER:284-285; P0.2).
6. **A fork with no option left**, every option failing an acceptance criterion or a non-goal (veto 1, METHOD:93-97).
   The owner: "Relax the weakest bound" (ER:328), whose option reads "the run drops the least important failing
   criterion or non-goal, records it as a departure, and builds" (ER:325-326). The run relaxes one bound at a time
   and runs M3 again over the options, until one survives (METHOD:86-97). Nothing parks.

   **How "weakest" is judged.** The records rank a bound by where it comes from, and the run relaxes the lowest tier
   that fails first:
   - **strongest**, a bound the unit's carried clause states, in its text or its "seen red on" cases (v2:1762-1785),
     or a ruling of the owner the spec quotes. v2 is the owner's baseline, and any change to a clause is itself a
     departure (v2:1809-1811). Relaxing one is a departure from the clause, risk loosening;
   - **middle**, a bound a v2 principle or a policy key's value sets (v2:847, :1125), which the spec cites;
   - **weakest**, a bound the spec writer added beyond its clause, a criterion or non-goal no clause token, principle
     or ruling backs. The records do not rank bounds within a tier: TEMPLATE-SPEC orders a spec's sections, not its
     criteria (TEMPLATE-SPEC:134-145), and M3 counts criteria without weighing them (METHOD:86).

   Within a tier the run judges for itself, and writes into the departure record which bound it dropped, its tier,
   the options it unblocked and why this bound was the least important. The spec is revised to drop it, a rev bump
   with its §9 line (METHOD:55-56), and the choice carries `relaxes: <bound>` in its §8 mark and `Decided:` trailer, so
   the departures report lists it first, beside the surface-widening choices (ER:347-348; P0.2). A relaxed bound that
   is itself a security, data or write constraint also carries `widens:`. A relaxed clause-tier bound stays named in
   the spec's §8 mark, so the carries join's token arm still finds the clause's names in its carrier
   (`carries.py:233-236`) and the departure, not a coverage red, is what records the drop. dOrderedCharter's decision
   principles (`cl-dClosedLoop-0032`) are the product's answer to both rungs 5 and 6.

Nothing in the driver judges whether a resolution was sound. The spec audit, the closing review and the owner's
reading of the report are what read it.

### What the owner sees at each spec landing

- **The landing diff**, which is `memory/` only: the specs, the audit records, the closing review, the departures
  report and the re-rendered packet. A product path in a spec run's diff means the run built code against the
  README's rule.
- **The coverage report**: `carries.py --report <slug>` inside the departures report until dTrueNorth lands, and the
  README's generated coverage region after it (`cl-dClosedLoop-0003`).
- **Every departure from v2**, with its record; every fork the run settled, a widened surface or a relaxed bound
  first; and every unit the spec run added, from a review or a discovery, and carried to the build run.

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

The script was run from the worktree root at HEAD `8d4db98a3`, with the owner's answers of `[answers-2]` in its model
(P0.4). Its exit code was 0. `[answers-3]` changes what a spec run may carry and how a fork is settled, neither of
which the model's run counts, durations or precedences read, so the script is unchanged; re-run at HEAD `54c76bb24`
it prints the same bytes.

```
$ python -B memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py
read at HEAD: 22 builds, 509 clauses; s=0.33, node b at pace 0.25; specs done 0, builds landed 0
claims cached on chain builds: none live or held
makespan 271 units; with unlimited nodes 198; whole builds after their parents land 277; serial on one node 510 (v2's 509 and 1 unit beyond it)

| Build | Stage | Parents | Units | Spec run: node, start-end, slack | Build run: node, start-end, slack |
|---|---|---|---|---|---|
| dTrueNorth | Fidelity | dClosedLoop | 7 | one whole run, in the next column | a 0-7, slack 0 |
| dGroundRules | Policy | dTrueNorth | 11 | a 7-11, slack 0 | a 11-18, slack 0 |
| dSafePassage | Supersession | dGroundRules | 13 | d 11-15, slack 3 | d 18-27, slack 4 |
| dOrderedCharter | Foundation | dSafePassage | 37 | a 18-30, slack 0 | a 30-55, slack 0 |
| dFairHearing | Review harness | dSafePassage | 18 | b 18-42, slack 19 | d 42-54, slack 16 |
| dDeclaredLoop | Spine | dOrderedCharter, dFairHearing | 34 | d 54-65, slack 14 | a 65-88, slack 0 |
| dWitnessedBar | Test | dDeclaredLoop | 30 | d 65-75, slack 13 | a 88-108, slack 0 |
| dPlacedRequest | Entry | dDeclaredLoop | 21 | b 65-93, slack 22 | d 93-107, slack 6 |
| dKeptSession | Session | dDeclaredLoop, dPlacedRequest | 28 | d 107-116, slack 11 | a 117-135, slack 7 |
| dBoundRoles | Roles | dDeclaredLoop, dWitnessedBar, dPlacedRequest | 26 | a 108-117, slack 12 | a 135-153, slack 3 |
| dTotalRecall | Memory | dDeclaredLoop, dWitnessedBar, dPlacedRequest | 26 | d 116-125, slack 12 | d 145-162, slack 3 |
| dFurnishedOrders | Orders | dBoundRoles | 20 | b 117-143, slack 41 | a 161-174, slack 30 |
| dWellOiledMachine | Runtime | dBoundRoles, dTotalRecall, dKeptSession | 61 | d 125-145, slack 0 | d 162-203, slack 0 |
| dLinkedLibrary | Library | dTotalRecall | 25 | a 153-161, slack 25 | a 174-191, slack 16 |
| dIndexedDesign | Design | dDeclaredLoop, dTotalRecall, dKeptSession, dBoundRoles, dLinkedLibrary | 16 | a 191-196, slack 28 | a 196-207, slack 16 |
| dRankedPlan | Plan | dDeclaredLoop, dTotalRecall, dBoundRoles | 16 | b 143-164, slack 45 | d 203-214, slack 33 |
| dTendedCadence | Maintain | dWitnessedBar, dRankedPlan, dWellOiledMachine, dIndexedDesign, dFurnishedOrders | 18 | a 207-213, slack 21 | d 214-226, slack 0 |
| dMindYourWords | Lexicon | dWellOiledMachine, dWitnessedBar, dLinkedLibrary, dFurnishedOrders | 17 | b 164-186, slack 47 | a 224-235, slack 12 |
| dCalibratedLens | Review | dTendedCadence, dFairHearing | 17 | a 218-224, slack 6 | d 226-237, slack 0 |
| dShippedRelease | Deploy | dWitnessedBar, dTotalRecall, dBoundRoles, dWellOiledMachine, dLinkedLibrary, dFurnishedOrders | 31 | b 186-227, slack 33 | a 235-256, slack 3 |
| dScopedBuild | Build | dIndexedDesign, dWitnessedBar, dWellOiledMachine, dFurnishedOrders | 15 | a 213-218, slack 35 | d 237-247, slack 13 |
| dConvergedCharter | Convergence | dScopedBuild, dShippedRelease, dCalibratedLens, dMindYourWords | 23 | d 247-255, slack 4 | a 256-271, slack 0 |

node a: busy 261 of 271 (96%), work 261 of 510 units, 21 runs: 8 spec, 12 build, 1 whole
node d: busy 208 of 271 (77%), work 208 of 510 units, 16 runs: 7 spec, 9 build, 0 whole
node b: busy 162 of 271 (60%), work 41 of 510 units, 6 runs: 6 spec, 0 build, 0 whole

first wave, each node's first run:
  a: whole dTrueNorth at 0
  d: spec dSafePassage at 11
  b: spec dFairHearing at 18

runs the owner starts, 43, at 37 distinct times, in order (time, node, run):
  0 a whole dTrueNorth · 7 a spec dGroundRules · 11 a build dGroundRules · 11 d spec dSafePassage
  18 d build dSafePassage · 18 b spec dFairHearing · 18 a spec dOrderedCharter · 30 a build dOrderedCharter
  42 d build dFairHearing · 54 d spec dDeclaredLoop · 65 a build dDeclaredLoop · 65 b spec dPlacedRequest
  65 d spec dWitnessedBar · 88 a build dWitnessedBar · 93 d build dPlacedRequest · 107 d spec dKeptSession
  108 a spec dBoundRoles · 116 d spec dTotalRecall · 117 a build dKeptSession · 117 b spec dFurnishedOrders
  125 d spec dWellOiledMachine · 135 a build dBoundRoles · 143 b spec dRankedPlan · 145 d build dTotalRecall
  153 a spec dLinkedLibrary · 161 a build dFurnishedOrders · 162 d build dWellOiledMachine · 164 b spec dMindYourWords
  174 a build dLinkedLibrary · 186 b spec dShippedRelease · 191 a spec dIndexedDesign · 196 a build dIndexedDesign
  203 d build dRankedPlan · 207 a spec dTendedCadence · 213 a spec dScopedBuild · 214 d build dTendedCadence
  218 a spec dCalibratedLens · 224 a build dMindYourWords · 226 d build dCalibratedLens · 235 a build dShippedRelease
  237 d build dScopedBuild · 247 d spec dConvergedCharter · 256 a build dConvergedCharter

landings of build and whole runs, with the runs in flight then and the surfaces the landing's clauses touch:
     7 dTrueNorth lands; in flight: none; surfaces: spec-format 0001,0002
    18 dGroundRules lands; in flight: none; surfaces: charter 0012; hooks 0011
    27 dSafePassage lands; in flight: spec dOrderedCharter on a, spec dFairHearing on b; surfaces: lander 0025; bar 0026,0029; hooks 0023,0024,0026..
    54 dFairHearing lands; in flight: build dOrderedCharter on a; surfaces: charter 0082; bar 0075,0080,0083..
    55 dOrderedCharter lands; in flight: spec dDeclaredLoop on d; surfaces: driver 0032,0047,0048..; lander 0047; charter 0031,0032,0036..; roles 0051; bar 0047,0048; hooks 0038
    88 dDeclaredLoop lands; in flight: spec dPlacedRequest on b; surfaces: driver 0099,0106,0108..; bar 0092,0102,0115; hooks 0091
   107 dPlacedRequest lands; in flight: build dWitnessedBar on a; surfaces: driver 0120,0123,0134; lander 0129; charter 0121; roles 0130
   108 dWitnessedBar lands; in flight: spec dKeptSession on d; surfaces: driver 0344; lander 0342; bar 0339,0342,0344..; hooks 0342,0344
   135 dKeptSession lands; in flight: spec dFurnishedOrders on b, spec dWellOiledMachine on d; surfaces: driver 0504; charter 0141; hooks 0140,0159
   153 dBoundRoles lands; in flight: spec dRankedPlan on b, build dTotalRecall on d; surfaces: charter 0180,0190; roles 0166,0168,0182..; bar 0188,0190; hooks 0190
   162 dTotalRecall lands; in flight: spec dRankedPlan on b, build dFurnishedOrders on a; surfaces: roles 0215,0220,0223..; bar 0237
   174 dFurnishedOrders lands; in flight: build dWellOiledMachine on d, spec dMindYourWords on b; surfaces: driver 0195; method 0195; roles 0202,0203,0209..; hooks 0197,0201,0205
   191 dLinkedLibrary lands; in flight: build dWellOiledMachine on d, spec dShippedRelease on b; surfaces: driver 0240; spec-format 0500; hooks 0244
   203 dWellOiledMachine lands; in flight: spec dShippedRelease on b, build dIndexedDesign on a; surfaces: driver 0280,0281,0301..; lander 0288,0311,0318..; charter 0320; roles 0310,0320; bar 0288,0318,0322..; hooks 0279,0282,0288..
   207 dIndexedDesign lands; in flight: spec dShippedRelease on b, build dRankedPlan on d; surfaces: spec-format 0383; roles 0397
   214 dRankedPlan lands; in flight: spec dShippedRelease on b, spec dScopedBuild on a; surfaces: hooks 0377
   226 dTendedCadence lands; in flight: spec dShippedRelease on b, build dMindYourWords on a; surfaces: bar 0499
   235 dMindYourWords lands; in flight: build dCalibratedLens on d; surfaces: charter 0278; roles 0270; bar 0270
   237 dCalibratedLens lands; in flight: build dShippedRelease on a; surfaces: charter 0462; roles 0463; bar 0468
   247 dScopedBuild lands; in flight: build dShippedRelease on a; surfaces: spec-format 0400; method 0404
   256 dShippedRelease lands; in flight: none; surfaces: driver 0426; lander 0413,0507,0414..; bar 0431; hooks 0427,0431,0437
   271 dConvergedCharter lands; in flight: none; surfaces: driver 0485,0486,0494..; lander 0485; charter 0479,0486,0490..; roles 0485; bar 0485; hooks 0490

node b's pace swept (makespan; busy share of a, d, b; b's runs):
  b 0.25: 271; a 96% d 77% b 60%; spec dFairHearing 18-42, spec dPlacedRequest 65-93, spec dFurnishedOrders 117-143, spec dRankedPlan 143-164, spec dMindYourWords 164-186, spec dShippedRelease 186-227
  b 0.30: 265; a 97% d 80% b 51%; spec dFairHearing 18-38, spec dPlacedRequest 61-84, spec dFurnishedOrders 113-135, spec dRankedPlan 135-152, spec dMindYourWords 157-176, spec dShippedRelease 176-210
  b 0.35: 261; a 96% d 81% b 54%; spec dFairHearing 18-35, spec dPlacedRequest 58-78, spec dFurnishedOrders 110-129, spec dRankedPlan 129-144, spec dLinkedLibrary 144-167, spec dMindYourWords 167-183, spec dShippedRelease 183-212
  b 0.40: 254; a 100% d 80% b 53%; spec dFairHearing 18-33, spec dPlacedRequest 56-73, spec dFurnishedOrders 108-124, spec dRankedPlan 124-137, spec dLinkedLibrary 137-158, spec dMindYourWords 158-172, spec dShippedRelease 172-198, spec dScopedBuild 198-210
  b 0.45: 247; a 100% d 81% b 58%; spec dFairHearing 18-31, spec dPlacedRequest 55-70, spec dBoundRoles 78-97, spec dTotalRecall 97-116, spec dRankedPlan 116-128, spec dLinkedLibrary 128-146, spec dMindYourWords 146-158, spec dShippedRelease 158-181, spec dScopedBuild 181-192
  b 0.50: 243; a 99% d 76% b 70%; spec dFairHearing 18-30, spec dDeclaredLoop 30-53, spec dPlacedRequest 55-69, spec dBoundRoles 78-95, spec dTotalRecall 95-112, spec dRankedPlan 112-123, spec dFurnishedOrders 123-136, spec dMindYourWords 144-155, spec dShippedRelease 155-175, spec dScopedBuild 175-185, spec dTendedCadence 185-197, spec dCalibratedLens 197-208
  a and d alone: 273
```

**The dispatch rule.** It is the script's model, applied at every landing, and the table is only its forecast at the
assumed speeds. Re-dispatching beat a fixed table under ±60% duration noise, with a median of 290 against 306
(schedule return). The rule:
- dTrueNorth is one whole run, and every other chain run waits for it (ER:232);
- a free full-pace node (a before d) takes the ready run with the most downstream work;
- node b takes only spec runs: the ready spec run with the most slack, among those whose slack covers its slowdown,
  and never one without slack. The owner: "Spec runs only" (ER:219), over "Spec and build, but … preferably
  non-critical" (ER:113-114);
- no build run starts until every parent has landed.

A node reads the rule as "the run the table shows on my node at time 0".

**The first wave.**
- Node a takes dTrueNorth's whole run, then dGroundRules' spec run.
- Node d runs phase 0 and its own preparation. Its first chain run is dSafePassage's spec run, once dGroundRules'
  specs close.
- Node b is onboarded, and its first run is dFairHearing's spec run.

**Makespan and load.** The makespan is 271 units, against 277 for whole builds after their parents land and 510 run
serially; each counts dTrueNorth's extra unit. Node a is busy 96% of the time, d 77% and b 60%.

**Node b's slice**, at Pro pace: six spec runs with slack and no run with zero slack, 41 of 510 units of work. As
b's pace rises to 0.5 it takes more spec runs and the makespan falls from 271 to 243, against 273 for a and d alone.
It never takes a build run.

**What the owner starts.** 43 runs (dTrueNorth's whole run, 21 spec runs and 21 build runs) at 37 distinct moments,
each when the script names it; the owner types each one (ER:270). Nearly every start follows a landing, so the owner
is needed at about every landing. Resumes after a hold are the resume tick's, where it is registered (P0.9).

## [sync-points]

These landings change what the nodes load. The runs in flight at each one are the script's landings list, re-derived
at that landing, and are not typed here. A landing's gates reach every later landing through the in-place merge bar
with no step (PROTOCOL:428-432). What follows is what loads at session start or runs from the worktree.

| Landing | What changes | Every node | A spec run in flight | A build run in flight |
|---|---|---|---|---|
| dTrueNorth | `**Carries:**` lines, the carries join in the spec-tokens leg, the coverage region, deviation records and their join, `@rev-N` pins (`cl-dClosedLoop-0001` to `-0006`); and its extra unit, the carry-forward condition in `tools/unattended/` (ER:232) | Nothing to install: every new worktree runs the new driver from its own tree (`SKILL.md:9-12`). Every packet's parent state goes stale. From here every spec run closes with the new condition | none: nothing else runs before it | none |
| dSafePassage | The upgrade-step kind, and `.agent-cap.conf` retired by a step (`cl-dClosedLoop-0018`) | Run the upgrade steps on each machine | Rotate its session at the next pass boundary | Same |
| dOrderedCharter | The charter re-founded and `AGENTS.md` re-rendered (`cl-dClosedLoop-0032`), including the fork-resolving decision principles | Fresh sessions load the new charter. M7 does not re-read it (METHOD:238-246) | Rotate at the next pass boundary. From here, residual forks resolve by the principles, which take over from the owner's standing ruling (ER:240) | Same |
| dDeclaredLoop | The roles stage table moved (`cl-dClosedLoop-0086`); `unattended.sh` re-pointed to `review.max-rounds` (`cl-dClosedLoop-0106`); `deviation.approval` (`cl-dClosedLoop-0119`) | Set the chain's `author-recorded` override where the key now lives. The instruments' approval arm retires | Merge `origin/main` at the next pass boundary, then `--authorization` (VERBS:923-926). The prepare lands it through the new driver | Same |
| dPlacedRequest | Run claims migrated onto leases (`cl-dClosedLoop-0120`) | Its spec carries the test that a live claim on another node survives the migration (ER:264); a drain, no other chain run live or held, only if that test could not be written | Its claim survives, by the test | Same |
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

**The owner's rule, applied** (ER:103-104, :121-131). A departure is recorded and explained, and it never waits for
the owner:
- Approval is `author-recorded`. The run's own author role signs the record, naming its role.
- The gate is `report`: "Report, as read (Recommended)" (ER:255). The join never refuses a landing; it lists, and a
  step before the close gives each listed member a record.
- The instruments carry the same values until the product keys exist (P0.1), and dTrueNorth's stand-in carries them
  by the owner-approved departure below (ER:189).
- A residual fork is settled by the owner's standing ruling (ER:240), and a fork with no option left by relaxing its
  weakest bound (ER:328); each is recorded as a departure ([phase-2], rungs 5 and 6).
- Every unit a spec run adds, from a review or a discovery, is recorded as a departure (ER:315-316).

**What is recorded where.**
- **A departure from v2 or from a spec past its first pass** is a deviation record in the departing build's `build/`,
  `<date>-build-<unit>-deviation-<n>.md`, with the fields `deviations.py:6-16` names. It is written in the departing
  unit's own commit (`cl-dClosedLoop-0004`).
- **A fork the run settled** is a §8 `RESOLVED` mark and a `Decided:` trailer (METHOD:316-320).
- **A unit carried forward** is a defer row in `RUN.md` (VERBS:703-710).
- **A park** is a park row (VERBS:36-46).

**The end-of-build departures report** (P0.2) is generated at each build's end, before `--close`, from those records,
the computed population and M9's derivation (METHOD:293-305). It lists first, side by side, every choice that widened
a security, data or write surface under the standing ruling and every bound a run relaxed for a fork with no option
left (ER:284-285, :347-348), then every member, recorded or not, every other fork settled, and every unit carried.
A member the report lists as "recorded by nobody" is given its record by the run before `--close`. That is a step in the README's rules, and it is not gated, as the owner chose (ER:255).

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
- A surface the standing ruling widened, or a unit's acceptance a relaxed bound rewrote, until the owner reads the
  report; and either choice the run did not mark `widens:` or `relaxes:`, which the report cannot put first, since only
  the mark tells it.
- Whether the bound a run relaxed was in truth the least important. Only a reader checks the tier against the
  record's own citation; within a tier it is the run's judgement and its written reason.
- Under `author-recorded`, who actually approved.

**The departures the owner has approved, where each is recorded, and when.** None is applied by this plan.

| Departure | Departs from | The owner's approval | Recorded where | When |
|---|---|---|---|---|
| dTrueNorth's stand-in join reads the chain's values, `report` and any recorded approver, until dDeclaredLoop's and dScopedBuild's keys land | `cl-dClosedLoop-0004@c374ccd0`, which fixes the by-risk table and a red on an approver below the risk | "A deviation, your values (Recommended)" (ER:189), quoting answer 3 of `[answers]` (ER:103-104) | **Deviation record 1**: `memory/builds/dTrueNorth/build/<date>-build-<that unit>-deviation-1.md`. Cause: owner ruling; risk: loosening; approver: owner, citing ER:189 and P0.8's row 3 | Approval: the decision row, in the opening landing. Record: dTrueNorth's whole run, in the commit that writes that unit's spec, as `cl-dClosedLoop-0004` itself asks |
| dTrueNorth's extra unit: the carry-forward condition for every unit a spec run adds, from a review or a discovery, once | dTrueNorth's v2 row, which plans six units (v2:1764) | "dTrueNorth's extra unit (Recommended)" (ER:232), after the owner's "that sounds like a bug" (ER:196-197), widened by "Carry it too (Recommended)" (ER:320) | **The decision row**, P0.8's row 1, which the unit's spec cites as `**Derived:**`; and **deviation record 2**: `memory/builds/dTrueNorth/build/<date>-build-<the extra unit>-deviation-2.md`, hand-off design-to-spec, follow-through "new unit <its id>". Approver: owner, citing ER:232 and ER:320 | Row: the opening landing. Unit: minted on dTrueNorth's roster in the opening (P0.5). Record: dTrueNorth's whole run, in the extra unit's spec commit |
| Each later departure a run makes under the owner's rulings: a unit a spec run adds (ER:315-316), a choice under the standing ruling (ER:240) or a relaxed bound (ER:328) | The clause or spec it departs from | The rulings themselves, landed as P0.8's rows 1 and 5 | A deviation record in the departing build's `build/`, approver the run's author role citing the ruling, under `author-recorded` | In the departing unit's own commit, in the run that makes it |
| dPlacedRequest's spec carries "a live claim on another node survives the migration", with a drain as the fallback | `cl-dClosedLoop-0120@5d655f07` | "Test in its spec (Recommended)" (ER:264) | A deviation record in `memory/builds/dPlacedRequest/build/`, risk stricter, approver owner citing ER:264 and P0.8's row 6 | dPlacedRequest's spec run, in the migrating unit's spec commit |
| dWellOiledMachine's spec carries "a `/unattended` run in flight at this landing lands after it" | `cl-dClosedLoop-0306@a3aa83b5` | "Land through new code (Recommended)" (ER:248) | A deviation record in `memory/builds/dWellOiledMachine/build/`, risk stricter, approver owner citing ER:248 | dWellOiledMachine's spec run, in that unit's spec commit |

**Carried, not asked, for the owner's walk** (ER:272-276): dTrueNorth's product join takes the instruments' plant
suite, P0.1's escapes included, as its acceptance (D3). That is stricter than `cl-dClosedLoop-0002@6acd9ea9` and
`cl-dClosedLoop-0004@c374ccd0`, so dTrueNorth's run records it with its author as approver, under `author-recorded`,
unless the owner's walk rules otherwise.

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
- **First assignment:** dTrueNorth's whole run at 0 (phase 1), then dGroundRules' spec and build runs, the first
  split pair.
- **Load:** the critical path through dGroundRules, dOrderedCharter, dDeclaredLoop and dWitnessedBar, at 96% busy.
- **At sync points:** rotate the session as [sync-points] says. Its build run of dDeclaredLoop is a self-rewriting
  build (D1).

**Node d**, `d41ly` (`fleet.toml:42-46`; its `host` is blank, which the claim does not read): 16 cores and 32 GB,
one Max plan serving five projects.
- **Setup:** P0.9, and it runs phase 0 first: the instruments, the opening and the decision rows.
- **First chain run:** dSafePassage's spec run at 11.
- **Load:** dWellOiledMachine's build run is its longest (61 units), and it rewrites the driver (D1). It also carries
  the dPlacedRequest build run, which is the barrier (D2).

**Node b**, `agent5` (`fleet.toml:28-33`): 4 cores and 8 GB, a Pro plan, today working only for inCMS and NicoCares.
- **Setup:** P0.9's onboarding row.
- **First run:** dFairHearing's spec run at 18.
- **Load:** spec runs only, each with slack: "Spec runs only" (ER:219). Six at Pro pace ([schedule]).
- **At sync points:** rotation as for a and d. b's slower runs are more often in flight at a landing, so it merges
  `origin/main` at each pass boundary.

## [owner]

| When | The owner's step | Rests on |
|---|---|---|
| Now | The plan takes two independent Tier-2 reviews, compared and folded: "Review twice, then approve (Recommended)" (ER:343) | [defaults] |
| After the reviews' fold | Walk this plan and approve it. Every choice is answered (ER:166-350); four items are carried for the walk (R6, D3, D5, D8) | [defaults] |
| After approval | Let node d's session run phase 0 | [phase-0] |
| Phase 0's end | Read the opening diff (every README, the grant row every `may:` cites, every packet and every decision row) and ask for its landing | P0.7 |
| Each moment the script names | Type the run, `/unattended <slug>`, on the named node, in a fresh worktree: 43 runs (ER:270) | [schedule]; PROTOCOL:21-27 |
| dTrueNorth's landing | Read its departures report, which is also the first look at its coverage, since it ran whole | [phase-1] |
| Each spec landing | Read the build's coverage report and departures report before typing its build run | [phase-2] |
| Each build landing | Read the departures report, the widened surfaces and relaxed bounds first. Nothing waits on the owner's reading (ER:240, :328) | [deviations] |
| At the barrier and the driver landings | Watch dPlacedRequest's test, or call the drain if it could not be written (ER:264); a driver build whose new code refuses its own landing hands it to the owner to land (ER:248) | [sync-points] |
| At dDeclaredLoop's and dScopedBuild's landings | Set the chain's override values in the policy file the product built (guarded) | [sync-points] |
| After dConvergedCharter | Set the two deviation keys (D5) | [defaults] |

## [cannot]

Every limit the five returns name, merged where two name the same one. Each is either designed around, with the
section that does it, or listed with its smallest change and that change's kind.

| Limit | Named by | Disposition |
|---|---|---|
| No spec audit unless the owner opts in | driver 1 | Designed around: `spec-audit:` in all 22 landed READMEs (answer 2, P0.5) |
| Governance-carrier and public-surface forks park; `may:` was never exercised | driver 2 | Designed around: one grant decision row every `may:` cites (ER:181); proven in phase 1 |
| "Governance carrier" is defined nowhere | driver 2 | **Cannot.** A policy: a decision row defining it |
| No parallelism inside a build; no sharing one build across nodes | driver 3, coordination | Designed around: split phases across builds. Lifting it is a chain build's unit: dPlacedRequest's unit leases (`cl-dClosedLoop-0120`) |
| Builds that rewrite their own driver | driver 4 | Designed around: they land through their own new code, the owner landing only if it refuses (ER:248), and the [sync-points] rows |
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
| A spec run cannot carry forward a unit it adds, from a review or an adopted discovery | this plan (STOPS:703-704) | Designed around: a chain build's unit, dTrueNorth's extra unit, a departure the owner approved (ER:232, :320; phase 1) |
| Nothing finds or offers work to a node | schedule 3 | Designed around: a manual step, the script at every landing ([coordination]) |
| Running sessions do not reload the charter, roles or hooks; installs are per node | schedule 4 | Designed around: manual steps at the sync points ([sync-points]) |
| dPlacedRequest's migration while other runs are live | schedule 5 | Designed around: its spec carries the survival test, with a drain as the fallback (ER:264) |
| An owner's approval cannot be verified | deviation 2 | Designed around: under `author-recorded` no owner approval is needed during the chain |
| A semantic contradiction or a code-only departure | deviation 3 | **Cannot.** A manual step: the audit on all 22 builds, the owner reading each coverage report, and the closing review |
| A dropped clause after a later edit | deviation 4 | Designed around: an instrument fix (P0.1, row 2), and `carries.py --exit` at each Design exit until `cl-dClosedLoop-0003` |
| No driver mode stops a spec run before code | this plan | **Cannot.** A manual step, the README's rule. The product is `cl-dClosedLoop-0383` |
| A residual fork still parks: veto 3, no survivor, or the goal | this plan | Designed around: policies, the owner's standing ruling for veto 3 and the goal bound (ER:240) and relaxing the weakest bound for a fork with no option left (ER:328), each recorded as a departure, until dOrderedCharter's `cl-dClosedLoop-0032` |
| The departures report has no Definition-of-Done item that runs it | this plan (`unattended.sh:12225-12226`) | **Cannot.** A manual step in the README's rules. The product is the landing record (`cl-dClosedLoop-0413`) and the deviation gate (`cl-dClosedLoop-0412`) |
| The owned nodes carry no paths for a grant | this plan | Designed around: one decision row (ER:181) |

## [defaults]

### Decided by the owner

Each quotes the owner's answer in ER `[answers-2]` or `[answers-3]`; the options offered are recorded there.

- **R1, the grant.** "One decision row (Recommended)" (ER:181). One row grants each chain build the
  governance-carrier and public-surface changes its own `[chain]` clauses name, and all 22 `may:` lines cite it
  (P0.5, P0.8).
- **R2, `cl-dClosedLoop-0004`.** "A deviation, your values (Recommended)" (ER:189). Deviation record 1
  ([deviations]); the interim check reads `report` and `author-recorded` for the chain.
- **R3, report or refuse.** "Report, as read (Recommended)" (ER:255).
- **D1, the builds that rewrite their own driver.** "Land through new code (Recommended)" (ER:248). Driver-touching
  units go last, the build lands through its own new code, and the owner lands it only if that code refuses.
  dTrueNorth's extra unit is the first such case.
- **D2, dPlacedRequest's claim migration.** "Test in its spec (Recommended)" (ER:264), with a drain as the fallback.
- **D4, who starts each run.** "You type it (Recommended)" (ER:270): 43 starts.
- **D6, replaced: the units a spec run adds.** The owner: "Why does carry-forward close refuses new units? It should
  not refuse any new units that come from the reviews (either spec or closing diff), that sounds like a bug."
  (ER:196-197); then "dTrueNorth's extra unit (Recommended)" (ER:232). dTrueNorth runs whole and carries the
  condition (phase 1). The `--override build-complete` route is dropped.
- **D7, residual forks.** "Standing ruling" (ER:240). The run takes the most capable option that fails only veto 3 or
  the goal bound, recorded as a departure, a widened surface first in its departures report (ER:284-285).
- **D9, a discovery a spec run adopts.** "Carry it too (Recommended)" (ER:320). The extra unit admits any unit a
  spec run adds, from a review or a discovery, carried to its own build run once; the build run must build it and
  never defer it again. The spec run specs and audits it and records it as a departure (ER:314-316). The plan's
  file-an-ask route is dropped.
- **D10, a fork with no option left.** "Relax the weakest bound" (ER:328). The run drops the least important failing
  criterion or non-goal, judged by the tiers in [phase-2], rung 6, records it as a departure and builds. The choice
  is listed first in its build's departures report, beside the surface-widening choices (ER:347-348), and P0.2's
  red cases cover that ordering.
- **The two records' placement and wording.** "Yes, as planned (Recommended)" (ER:336): approval in decision rows at
  the opening, each record written in the unit's own spec commit, naming the owner as approver and citing the answer
  ([deviations]).
- **Before phase 0.** "Review twice, then approve (Recommended)" (ER:343): two independent Tier-2 reviews of this
  plan, compared and folded, before the owner approves it.
- **Node b.** "Spec runs only" (ER:219), the script's rule.

### Carried as recommended, not asked, for the owner's walk (ER:272-276)

- **R6.** `design.coverage` stays `refuse`; the run always clears a coverage red itself.
- **D3.** dTrueNorth's product join absorbs the instruments' planted cases as its acceptance.
- **D5.** After the chain, the two deviation keys return to `standard`'s `refuse` and `by-risk` (v2:1609-1610).
- **D8.** The opening mints every roster id and carry-forward ask, which the carry-forward rules force (P0.6).

## [disagreements]

| Where | Which the plan follows, and why |
|---|---|
| Whole build per run (driver A, coordination C1) against split phases (schedule) | Split phases: answer 1 chose them. Split is two runs, a landed spec run and a later build run taking over a terminal claim (STOPS:221). It is not the hold-and-resume hand-off coordination's C3 rejected |
| Opting into the audit through `authorized-by: prompt` (handoffs, limit 7) against a `slug` README landed on main (driver A) | Driver A: answer 2 needs `may:`, which prompt mode refuses (`unattended.sh:4160-4163`). The main loop read A's path at IR:862-869 |
| Park loosening and breaking deviations for the owner (deviation, recommendation 2) against answer 3 | Answer 3 binds; the plan follows the readings (ER:121-127) |
| Bootstrap legs as dTrueNorth's first unit (deviation, recommendation 1) | D3, carried as recommended: under J no other chain spec exists before dTrueNorth lands, so bootstrap legs would cover nothing more |
| A build is ready when its parents' claims read `landed` (coordination, step 1) | The tree: with split phases a `landed` claim may be a spec run, so phase is read from specs on `origin/main` (P0.4) |
| Stagger landings by owner order (driver, limit 7) against contention being too low to need it (coordination, test 4) | Coordination: it measured at most two interlopers against three retries |
| 262 units (schedule, HEFT) against its own stated rule, "the free node takes the ready phase with the most downstream work" | The stated rule, which a node can apply at a landing without a plan; the script gave 270 then and gives 271 with dTrueNorth whole and its extra unit. HEFT's 262 comes from holding a node for a more critical run about to become ready, which a re-derived table can also do if the owner prefers |
| Node b spec-only (schedule) against "spec and build" (answer 4) | The owner's later "Spec runs only" (ER:219), which agrees with the schedule return |
| "Records-only landings are cheap" (schedule) | Partly: an in-place close runs the bar under `GATE_FULL=1` whatever the diff (PROTOCOL:428-432). A spec run is spared only the self-tests (`.unattended.conf:40`) |
| `BUILD-METHOD` "MUST run concurrently" against a strictly sequential harness (driver) | The code (`unattended-build.js:76-80`) |
| "Claims never age" (GR:323, theme T5) against the code (coordination) | The code: a `live` claim turns `stale` at 5400 s, and only `held` never ages (`unattended.sh:2177-2186`) |
| Several returns: forks the run cannot settle are parked BLOCKED | The owner's rulings: the run settles them itself, by the standing ruling (ER:240) or by relaxing the weakest bound (ER:328), and records each as a departure. Nothing parks |
| The plan's own D6, an `--override build-complete` under a ruling, against the owner's view that the refusal is a bug for review-promoted units (ER:196-197) | The owner: the condition is fixed in product, by dTrueNorth's extra unit (ER:232). The override is dropped |
| The plan's D9, a spec run filing a discovery as an ask, and its D10, carrying a no-option unit forward | The owner chose otherwise: "Carry it too (Recommended)" (ER:320) and "Relax the weakest bound" (ER:328). Both of the plan's routes are dropped |
