# Execution plan: the chain specced, built and landed on nodes a, b and d under today's gov

**Serves:** research PLAY-dClosedLoop-1

The plan the execution record asked for, written from the five execution returns and the owner's four answers. It
opens nothing and changes nothing. Every step below that writes a chain build's file, a policy line, a decision row
or product code runs only after the owner approves this plan, and the baseline's stop holds until then
(`build/…-execution.md:5-7`). The schedule is not typed here. It is the output of
`build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`, kept beside this record and re-run at every landing.

The owner's answers to the plan's open choices (ER `[answers-2]`, ER:166-286) and to the four points that fold left
open (ER `[answers-3]`, ER:306-350) are folded in, and so is the paired Tier-2 review of the plan at `d82cee1a2`
(`build/…-execution-plan-reviews-compared.md` `[fold]`), with the owner's answers to its two forks (ER `[answers-4]`,
ER:375-404), the second review pair over that fold (`build/…-execution-fold-reviews-compared.md` `[fold]`), and the
owner's walk of the plan (ER `[walk]`, ER:413-542), whose four changes are folded without a further review. Each item
they decide now reads as decided and quotes the answer; the items the owner was not asked are carried as recommended
(ER:272-276).

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
   - the mandate delegates it, with a `may:` grant lifting veto 2 for what the grant names (METHOD:80-97).

   Four kinds of fork would still park: one whose only options widen a security, data or write surface (veto 3); one
   whose only options trip veto 2 outside the grant (a new external dependency or install location, or a
   governance-carrier or public-surface change none of the build's own `[chain]` clauses names); one the goal cannot
   survive (METHOD:81, :93-97); and one with no option left at all. The owner ruled on each:
   - "Standing ruling" (ER:240): where every surviving option passes veto 1 and fails only veto 3 or the goal bound,
     the run takes the most capable of them, in the words of the option, "the most capable option that fails only the security veto or
     the goal bound" (ER:237-238);
   - "Standing ruling takes it (Recommended)" (ER:388): the same rung takes a fork whose only options trip veto 2
     outside the grant, marked `widens: <change>`;
   - "Relax the weakest bound" (ER:328): a fork with no option left has its weakest failing bound dropped, and the run
     builds.

   Each is recorded as a departure, and nothing parks or waits on the owner. The price is that a security, data or
   write surface may widen, an ungranted dependency or carrier change may be made, and a unit's own acceptance may be
   rewritten, unreviewed until the owner reads the build's departures report, where every such choice is listed
   first, beside each choice the grant lifted. dOrderedCharter's fork-resolving decision principles
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
  explains every departure, a widened surface, an ungranted change, a grant-lifted choice or a relaxed bound first,
  and nothing waits for the owner.

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
| A close whose range touches `tools/` owes the flagged bar, `GATE_FULL=1 GATE_SELFTESTS=1`, under a 21600 s wall. `GATE_SELFTESTS=1` runs the bar's held kit legs; the unattended kit's own suites are on no leg and run only on demand, and the kit's Definition of Done has a landing touching it carry their verdict, which a build README may waive, as dAlignedCarrier's did | `.unattended.conf:40`, `:67`; `unattended.sh:10528`; VERBS:851-871; `memory/guides/MERGE-BAR.md:39-41`; `tools/unattended/run-unattended-gates.sh:2`, `:28-31`; `memory/builds/dAlignedCarrier/README.md:28-30` |
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
| An approver written as "owner" passes on a prefix match (`deviations.py:81-87`) | Under the chain's value `author-recorded`, any recorded approver role passes. One naming the owner must cite a decision row the default branch holds that names this record's own departure: P0.8 row 3 for the `cl-dClosedLoop-0004` record, row 1 only for the extra unit's deviation-2 record, row 6 for dPlacedRequest's record, or a row naming the record's Departs-from clause id. Every later departure's approver is the run's author role, citing the ruling, never `owner` | "owner" with no id: red; an owner approver citing only an ER line: red; one citing row 5: red; one citing row 1 for a unit a spec run added: red |
| False red: `AMENDED` read on any spec line (`deviations.py:160`), where the ledger form is `amended rev-N` in journal records (`memory/HYGIENE.md:604-606`) | Read `amended rev-N` from the ledgers | A spec quoting `cl-dClosedLoop-0004`: green; a ledger row with no record: red |
| False red: revisions numbered by commit count (`deviations.py:153-158`), where the header `rev-N` moves only on a material edit (`memory/TEMPLATE-SPEC.md:61-67`) | Address a revision by its header `rev-N` | A status-only commit, then a record at the header's rev-1: green |
| Two specs on two branches each carrying one clause whole are caught only on the merged tree | Placement: the instruments run on the prepared merge, after `--prepare` | The deviation return's two-node plant on the merged tree: red |
| Any run can edit the instruments under `memory/`, the class `TOOL-aStandingWrit-7` names (`memory/builds/aStandingWrit/BACKLOG.md:11`) | Every report and packet prints each instrument's blob hash, and the packet pins it. `packet.py --check`'s pin arm reds a moved blob, and a pin-keeping re-render cannot re-pin it away ([handoffs]). This covers the re-render only: a hand edit of the packet's pin line, or of `packet.py`, can still move a pin, and only the owner's landing-diff check guards that until a chain unit's merge-bar check ([cannot]) | A one-byte edit to `carries.py`, the packet made stale by another cause (an `[owed]` line), and a re-render keeping the pins: the pin arm reds while the byte compare stays green. Two controls, each green on the same plant: `--check` with the pin arm removed, and a `packet.py` variant whose `--write` re-pins |
| `asbuilt.py --check` reds on each new record until `--write` runs (`build/…-asbuilt.py:81`) | Placement: the record's own commit carries the re-rendered view | None owed; it is the instrument working |

**Two more population arms.** `deviations.py` reads rescope `add`, `retire` and `supersede` rows from `RUN.md` and
every rotated `RUN.*.md`, and divergence hand-backs, as members; the planned `defer` rows a spec run writes for its
own roster units are not members. Plants: an add row with no record is listed as unjoined, and so is a hand-back with
no record, while a spec run's routine defer rows are not listed.

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
  ledger `amended` rows, and the rescope rows and divergence hand-backs P0.1's two further arms read;
- the records under `memory/builds/<slug>/build/`;
- the forks the run resolved, as M9 derives them (METHOD:299): every §8 `RESOLVED` mark, every `Decided:` trailer in
  the run's range (below; METHOD:316-320) and every park row;
- the units carried forward;
- the outputs of `carries.py --report <slug>` and `asbuilt.py --check`, while they still run (the retirement table
  in [phase-1] says what the report reads after each retires);
- the paths the run's range writes, and, for a build run, its product paths: the `--dispatch --writes` sets its units
  recorded in `RUN.md` (VERBS:711-721); a spec run has none.

**The run's range**, defined once and used everywhere below. `P` is the prepared merge's first parent, the advertised
`origin/main` tip `check_prepared_merge` reads (`tools/push-main.sh:505-538`). Paths come from `git diff --name-only
P..HEAD`, which keeps paths written in a conflict resolution; trailers come from `git log --format=%B P..HEAD`, which
gives the run's own commits and those stacked on the prepared merge. Neither reads from the run's base: a two-dot
range from the base over the prepared merge would sweep in every commit other builds landed on `origin/main` since.

**The marks it reads.** Every resolution under rung 5 or rung 6 ([phase-2]) declares itself in its §8 mark and its
`Decided:` trailer: the trailer cites the ruling it serves, one of ER:240, ER:388 or ER:328, or P0.8 row 5, and
carries both `widens: <surface or change>|none` and `relaxes: <bound>|none`. A choice that lifts veto 2 through the
build's grant carries `grants: <decision id> <change>` (the review's `veto2-fork-unruled` row). A `none` value is no
entry: only a non-`none` `widens:`, `relaxes:` or `grants:` value orders first or joins a record. A goal-bound-only
choice under ER:240 carries `widens: none` and is listed with the other forks. Each README carries this rule (P0.5,
rule 6).

**What it lists**, in this order:
- first, side by side, each choice with a non-`none` `widens:` (a surface widened, or an ungranted veto-2 change,
  under the standing ruling: ER:240, :284-285, :388), each with a non-`none` `relaxes:` (a bound dropped for a fork
  with no option left: ER:328, :347-348), and each marked `grants:`;
- each member, with its address and hand-off, the record it joins or "recorded by nobody", and the record's reason,
  risk, approver and follow-through; for a relaxed bound its `**Bound:**` and `**Tier:**`, and for a widened surface
  its `**Surface:**`;
- each other fork, with its question, pick, reason and source line;
- each carried unit, with its ask, and each unit a spec run added, from a review or a discovery, and carried to its
  build run;
- every path the run's range writes outside its own build folder and its recorded product paths, an instrument under
  `memory/builds/dClosedLoop/build/` included. The shared renders are not listed: `memory/LIVE.md`, the ledgers, and
  the generated files and regions a landing re-renders ([coordination], shared records), and ask rows the run files
  in another build's or dClosedLoop's `BACKLOG.md` (P0.6, rules 3 and 5).

**Its name** carries the run kind: `memory/builds/<slug>/build/<date>-build-<first unit>-departures-spec.md` for a
spec run, and `-departures-build.md` for a build run or dTrueNorth's whole run, so a same-date build run never
overwrites the spec run's report. README rule 4 and the phase tables use the same names.

**Two checks, run under both `--write` and `--check`.**
- **The byte compare**: `--check` renders the report again and compares the bytes with the written file.
- **The validating arm**, separate from it: it parses the rendered report and exits 1 unless every non-`none`
  `widens:`, `relaxes:` and `grants:` entry comes before every other entry; every `Decided:` trailer in the run's range
  appears; every non-`none` `relaxes:` mark joins a record carrying `**Bound:**`, `**Tier:**` and `**Reason:**`; and
  every non-`none` `widens:` mark joins a record carrying `**Surface:**` and `**Reason:**`. It also exits 1 on a
  trailer citing ER:240, ER:388, ER:328 or P0.8 row 5 that lacks either key; on one citing ER:388 whose `widens:` is
  `none`; and on one citing ER:328 whose `relaxes:` is `none`.

**Acceptance.** `--fixture` lists each population plant of P0.1, P0.1's two further arms' plants included.

**Red tests**, each planted into the sources or a renderer stub, never into the written report:
- a renderer stub that emits a `widens:` choice in source order after a member: the validating arm reds; the same
  stub with the arm removed stays green;
- the same for a `relaxes:` choice and a `grants:` choice, each seen red with the arm and green without it;
- a renderer stub that drops one `Decided:` trailer: the validating arm reds;
- a `relaxes:` record with no `**Tier:**` or no `**Reason:**`, and a `widens:` record with no `**Surface:**`: exit 1;
- trailers citing a ruling: `relaxes:` only, red; `widens:` only, red; `widens: none` citing ER:388, red; `widens: none
  relaxes: none` citing ER:240, green; a rung-6 trailer with `widens: none` and a full `relaxes:` record, green and
  listed first;
- a grant-lifted choice the report omits: red;
- a commit in the run's range writing another build's packet: listed in the outside-paths block; a `LIVE.md`
  re-render: not listed;
- a build-run commit writing a product path outside every recorded `--writes` set: listed;
- another build landing a path in its own folder and a `Decided:` trailer on `origin/main` between this run's base and
  its `--prepare`: neither listed nor required, while the run's own write to another build's packet is listed. The
  plant is seen red first against a `<base>..HEAD` range;
- a report written before a member's record is added: `--check` reds once the record lands;
- a hand edit of the written report: the byte compare reds.

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
9. The `[owed]`, `[open]`, `[enforcement]` and `[policies]` lines that name the build; read from the opened README,
   every roster unit, `**Derived:**` ones included, with P0.8 row 1's id for dTrueNorth's extra unit; and every open
   ask in dClosedLoop's `BACKLOG.md` that names a chain build (P0.6, rule 5), in every packet.
10. Must-not-touch.
11. The coverage report.
12. The reading order ([handoffs]).

**`--write`** re-renders the packet keeping the instrument pins it carries. **`--check <slug>`** renders it again and
compares the bytes. It has completeness arms: every clause id and hash of the build's row, every gap it owns, every
parent, every `[owed]` line naming it, every roster unit of the opened README, and every open ask in dClosedLoop's
`BACKLOG.md` naming a chain build. Each arm is red on a planted omission. It also has a **pin arm**, separate from the
byte compare: for each field-1 instrument it compares the pinned blob with `git rev-parse HEAD:<instrument>` and
exits 1 on a mismatch, whatever the byte compare says, naming the cause "instrument <path> moved" (P0.1, row 10).

**`--repin <instrument>`** is the owner's re-pin. It refuses inside a chain run (a live `RUN.md` in the tree). It is
run by dClosedLoop's session in an owner-asked landing that lands nothing else, and recorded as a decision row; the
retirement steps in [phase-1] use it.

**Acceptance.**
- Rendering dTrueNorth's packet reproduces the handoffs return's worked example: six clauses, with
  `cl-dClosedLoop-0001@83b6b117` through `cl-dClosedLoop-0006@06ceb3cc`; the node `record-kind.deviation`; and the
  gaps gap-design-13, gap-build-07 and gap-mem-47. Field 9 also carries dTrueNorth's extra unit and the decision row
  it derives from, P0.8 row 1, which approves the extra unit's record.
- Once the opening exists in a scratch clone, `handoff.py render --build dTrueNorth --unit <its first unit> --input
  prompt=<packet>` renders, and `handoff.py check` is green on the result.

### P0.4 The schedule script

This record's script: `build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`. Its docstring names its inputs, its
model and what it does not model.

**Acceptance.** It reads v2, the chain builds' specs and the cached claims at a ref. At every landing a node runs
`git fetch; bash tools/unattended/unattended.sh --claims; "$PY" <script> --ref origin/main`, with `$PY` from P0.9,
and starts the run its table shows on that node at time 0. A plain `git fetch` never fills the claim cache the
script reads; `--claims` does.

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
| A cached `live` claim of user `agent5` on dGroundRules, beat now | Its spec run is pinned to node b at 0, and its build run goes to a full-pace node |
| A claim naming user `nobody` | Exit 1: the fleet names no such node |
| A cached `live` claim of user `d41ly` on dGroundRules whose beat is older than `RESUME_STALE_BOUND` (5400 s, read from `.unattended.conf`) | Printed "stale on d: take over per [coordination]", left unpinned, and its table cell marked "take over (stale)"; the same claim with a fresh beat is pinned to d |
| The same stale claim of user `daily-agent` on dTrueNorth | Its table cell and a's first-wave line both read "whole dTrueNorth at 0, take over (stale)" |
| A cached `live` claim of user `d41ly` on dGroundRules with no `beat-utc` line | Pinned to d, and printed "dGroundRules beat unreadable on d: kept pinned" |
| A fresh `live` claim of user `agent5` on dFairHearing | "a and d alone" reads 273, the same as with no claim, from a and d only, and the note says the claim is absent from that run and left unpinned. Seen red on the script before this fold, which put the claim on a hidden pace-1 node and printed 216 |
| A live `agent5` claim on dGroundRules whose specs read done | Printed as a spec-only node's claim on a build run and left unpinned: no build run goes to b |
| A live claim of user `agent-0`, node c, on dGroundRules | Printed "held off-fleet on c": the run stays off every node's table |
| `--b 0.5` | b's lines name twelve spec runs and no build run; with the `SPEC_ONLY` filter removed from the dispatch, the same run gives b two build runs |
| dTrueNorth's six clause specs `CLOSED` and the extra unit's spec `OPEN` | dTrueNorth is not done: its whole run still starts at 0 |

**The done rule, as `tree_state` applies it.** A build is done only when its specs carry every clause of its row and
every spec in its folder, the extra unit's included, is `CLOSED` or `WONTDO`.

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
| `may:` | The grant decision row's id, on all 22; dTrueNorth's line also cites the extra unit's decision row, since the carry-forward condition is a change to a governance carrier (P0.8 row 9's list) no `[chain]` clause names | ER:181; ER:525; `lib-unattended.sh:1440-1478`; METHOD:82 |
| H1 and stage | `# <slug> — the <Stage> build of the dClosedLoop chain` | v2:1762-1785 |
| The five slots | Derived bodies, as the scaffold writes them: the problem slot is the build's owned gaps at the baseline (it is the goal bound); the improvements are its clauses carried and built; the detriments are its gaps left open and its children waiting; the build-level rules are below; the parked decisions are "none" | `gen_build_index.py:122-131`, `:3507-3560` |
| `roster:units` | One unit per clause, in clause order: its id, `cl-dClosedLoop-NNNN@<hash8>`, and the clause's text to its first comma. dTrueNorth's roster adds a seventh row, the extra unit, its carries cell `**Derived:**` from its decision row | v2:1762-1785; `carries.py:11`, `:78-80`; ER:232 |
| Unit family, `roster:` and `streams:` | The build's main stream's family, by the rule below: PLAY, KICK, DEPL or TOOL, one family for the whole build, its roster ids and its ask. `roster:` is that family and `streams:` its discipline, the pairing `.memory-tree.conf` declares; a unit's spec header `streams` still names every discipline it serves | ER:438; `.memory-tree.conf:42`; TEMPLATE-SPEC:56-77 |
| Driver-changing builds | The set the rule below derives, each README carrying rule 8 | ER:476 |
| `BACKLOG.md`, one ask, for every build but dTrueNorth | "build every roster unit of this build from its spec", filed for the spec run's carry-forward, with its `SEV` row. dTrueNorth runs whole and closes without carry-forward, so it gets none | STOPS:707-709; ASKS:92-100; ER:232 |
| Packet | P0.3 | above |
| `readme-contract.txt` rows | 22 bound rows (bare paths); the exempt pin is unchanged | `memory/project/readme-contract.txt:1-29`; `.unattended.conf:383-405` |

**Build-level rules each README carries:**
1. dTrueNorth's README: one whole run specs, audits, builds and lands every unit (ER:232). Every other README: a run
   is this build's spec run when the build's `BACKLOG.md` at the run's baseline commit holds an open ask (the
   opening's carry-forward ask, which dTrueNorth never gets) and its starting roster has a unit `MISSING`. It specs
   every unit, runs the audit, defers every unit and closes by carry-forward, every unit it added included, from a
   review or a discovery, each specced, audited and recorded as a departure (ER:314-320). Any other run is the build
   run, and it builds every carried unit, never deferring an added one again. The phase is read from the tree, never
   typed (METHOD:39-42; VERBS:72-87), and the extra unit's driver reads the same test ([phase-1]).
2. The reading order ([handoffs]), and `packet.py --check <slug>` green before the first pass. A packet red on a
   moved instrument blob is a stop, never re-rendered away ([handoffs]).
3. Push the run branch after every pass commit, hold and hand-off.
4. **The close sequence**, after `--phase VERIFYING` and the final successful `push-main.sh --prepare`, on the
   prepared merge: run `deviations.py --report <slug>`; write a deviation record for each member it lists "recorded by
   nobody"; run `--report <slug> --write` and commit the report, named `…-departures-spec.md` for a spec run and
   `…-departures-build.md` for a build run or the whole run (P0.2); run `--report <slug> --check`; then
   `--authorization` and `--close`. The prepared merge stays valid under single-parent commits stacked on it
   (`tools/push-main.sh:505-538`). After any reconcile and re-prepare, the sequence runs again.
5. The chain's deviation values are `report` and `author-recorded` (ER:121-127; ER:255).
6. Forks are settled as [phase-2] says. Every resolution under rung 5 or 6 carries, in its §8 mark and its `Decided:`
   trailer, the ruling it serves, one of ER:240, ER:388 or ER:328, or P0.8 row 5, and both `widens: <surface or
   change>|none` and `relaxes: <bound>|none`. A `none` value is no entry. A non-`none` `relaxes:` joins a record
   carrying `**Bound:**`, `**Tier:**` and `**Reason:**`, and a non-`none` `widens:` one carrying `**Surface:**` and
   `**Reason:**`. A choice that lifts veto 2 through this build's grant carries `grants: <decision id> <change>`
   (P0.2).
7. A run writes only under its own `memory/builds/<slug>/`, and in a build run the product paths its units recorded
   with `--dispatch --writes`. Outside them it writes only an ask row in another build's `BACKLOG.md` (P0.6, rule 3)
   and the shared renders a landing re-renders, `memory/LIVE.md`, the ledgers and the generated files and regions
   ([coordination]). No gate refuses a run's own commit to another build's paths; the departures report lists every
   such path (P0.2) and the closing review reads it.
8. In a driver-changing build's README only, dAlignedCarrier's rule as its README states it
   (`memory/builds/dAlignedCarrier/README.md:28-30`): "The unattended kit's own self-test suites are WAIVED for this
   build's landing (owner, 2026-10-20, walk answer 5). A criterion they would observe is amended citing this rule;
   their clean reading is owed with <the ask id>." The ask is one the opening files for each driver-changing build in
   dClosedLoop's own `BACKLOG.md`, under dClosedLoop's slug (P0.6, rule 1), as dAlignedCarrier's clean reading was
   owed with another build's ask. What the rule waives is the on-demand verdict of
   `tools/unattended/run-unattended-gates.sh --selftests` that the kit's Definition of Done would otherwise have the
   landing report carry (`tools/unattended/run-unattended-gates.sh:2`, `:28-31`; the DoD comment at
   `.githooks/gate-env.sh:25`). Those suites are on no leg of the bar (`memory/guides/MERGE-BAR.md:39-41`), and the
   owner's standing instruction of 2026-08-23 runs them only when the owner asks
   (`memory/guides/SESSION-KICKOFF.md:136-138`). In their place a criterion they would observe is proved by a targeted
   probe or the unit's own planted test, and each acceptance ledger says which suite's run was not observed, as
   dAlignedCarrier's did (`memory/builds/dAlignedCarrier/build/2026-09-30-build-TOOL-dAlignedCarrier-1-1-acceptance-ledger.md:10`).
   The close is unchanged: like every close whose range touches `tools/`, it exports `GATE_FULL=1 GATE_SELFTESTS=1`,
   the flagged bar the driver owes (`unattended.sh:10528`; VERBS:851-871), and `GATE_SELFTESTS=1` runs the bar's held
   kit legs, not the unattended kit's suites.

**The unit family, derived** (walk answer 1: "Family by stream", ER:438). The owner's rule reads "PLAY for charter
and playbook builds, KICK for session and kickoff, DEPL for deploy, TOOL otherwise" (ER:435-436). `open.py` applies it
to two cells each build's v2 row already holds, its Stage and its slug's noun (the slug's last capitalised word), and
matches the owner's words in that order, whole words only: `charter` or `playbook` gives PLAY, `session` or `kickoff`
gives KICK, `deploy` gives DEPL, and a build matching none is TOOL. `open.py --families` prints the table below, and
the per-build summary carries each build's family; this is the plan writer's run of the same rule at `a93477abc`
(`exec/d219/family2.py` in the writer's scratch folder):

```
| Build | Stage | Slug noun | Word matched | Family |
|---|---|---|---|---|
| dTrueNorth | Fidelity | North | none | TOOL |
| dGroundRules | Policy | Rules | none | TOOL |
| dSafePassage | Supersession | Passage | none | TOOL |
| dOrderedCharter | Foundation | Charter | Charter | PLAY |
| dFairHearing | Review harness | Hearing | none | TOOL |
| dDeclaredLoop | Spine | Loop | none | TOOL |
| dPlacedRequest | Entry | Request | none | TOOL |
| dKeptSession | Session | Session | Session | KICK |
| dBoundRoles | Roles | Roles | none | TOOL |
| dFurnishedOrders | Orders | Orders | none | TOOL |
| dTotalRecall | Memory | Recall | none | TOOL |
| dLinkedLibrary | Library | Library | none | TOOL |
| dMindYourWords | Lexicon | Words | none | TOOL |
| dWellOiledMachine | Runtime | Machine | none | TOOL |
| dWitnessedBar | Test | Bar | none | TOOL |
| dRankedPlan | Plan | Plan | none | TOOL |
| dIndexedDesign | Design | Design | none | TOOL |
| dScopedBuild | Build | Build | none | TOOL |
| dShippedRelease | Deploy | Release | Deploy | DEPL |
| dTendedCadence | Maintain | Cadence | none | TOOL |
| dCalibratedLens | Review | Lens | none | TOOL |
| dConvergedCharter | Convergence | Charter | Charter | PLAY |
```

Counting the clauses that name each stream's surface was tried first and dropped: it put dOrderedCharter, 12 of 37
clauses naming the charter, below any natural cut, and made dSafePassage, whose upgrade steps name adopters, a deploy
build. The owner reads every family in the per-build summary before the landing (P0.7).

**The driver-changing builds, derived** (walk answer 5: "Waive in each README", ER:476). A build is driver-changing
when one of its v2 clauses names a path or surface of the unattended kit: `unattended.sh`, `check-unattended.sh`,
`tools/unattended/`, the `/unattended` command, "the unattended kit", unattended's verbs (`--plan`, `--status`) or run
claims; "the driver" alone is left out, since in v2 it names the loop's driver role. `open.py --driver-builds`
applies that predicate, and dTrueNorth joins by its extra unit, which edits the kit. The plan writer's probe of the
same predicate (`exec/d219/driver.py`) finds seven:

| Build | Clauses that touch the kit |
|---|---|
| dTrueNorth | its extra unit, the carry-forward condition in `unattended.sh` ([phase-1]) |
| dOrderedCharter | `cl-dClosedLoop-0047` (`unattended.sh`'s drift-audit and runlog calls), `cl-dClosedLoop-0048` (`check-unattended.sh`'s `RECALL_CLI` probe) |
| dDeclaredLoop | `cl-dClosedLoop-0106` (`unattended.sh` and `check-unattended.sh` re-pointed to `review.max-rounds`) |
| dPlacedRequest | `cl-dClosedLoop-0120` and `cl-dClosedLoop-0134` (run claims migrated onto leases, and their tombstones) |
| dWitnessedBar | `cl-dClosedLoop-0344` (the held-CI reader moved out of the unattended kit) |
| dWellOiledMachine | `cl-dClosedLoop-0280` (`--plan` and `--status` re-pointed), `cl-dClosedLoop-0281` (unattended's verbs), `cl-dClosedLoop-0306` (the kit dissolved) |
| dConvergedCharter | `cl-dClosedLoop-0485`, `cl-dClosedLoop-0486`, `cl-dClosedLoop-0494` and `cl-dClosedLoop-0496` (`unattended.sh` folded and the kit retired) |

**The per-build summary** (walk answer 2, ER:446). `open.py --summary` prints one row per build, from the files the
opening writes, for the owner's read (P0.7): its slug; its stage; its `parents:`; its unit count, roster rows
(`**Derived:**` ones included); its family and `streams:`; its carry-forward ask id, or "none: whole run" for
dTrueNorth; its packet's size in bytes and `packet.py --check` result; its `may:` line verbatim; its `spec-audit:`
date; whether it is driver-changing, so carries README rule 8, and if so the id of its clean-reading ask in
dClosedLoop's `BACKLOG.md`; and whether its `readme-contract.txt` row is present
and bound. `open.py --check` reds a summary row that disagrees with the files it summarises, seen red on a planted
README whose family differs from its row.

**The `may:` grant, decided.** The owner: "One decision row (Recommended)" (ER:181). One `DECISIONS.md` row, landed
with the opening, grants each chain build the governance-carrier and public-surface changes its own `[chain]` clauses
name, and all 22 `may:` lines cite its id. A governance carrier is a path on P0.8 row 9's list (walk answer 10,
ER:525), so the grant reads against that list: a change to a listed path that the build's own clauses name is
granted, and the run's M3 judges whether a change is covered (`lib-unattended.sh:1455-1458`). It replaces the
derivation answer 2 first read, which had no input: v2's owned nodes are keys with an `owner` relation and no path
(`carries.py:104-113`; the plan writer's probe of every namespace of `build/…-map.py`'s `derive()`).

### P0.6 The two opening hazards

**Bare dTrueNorth ids.** `gen_build_index.py`'s `rosters()` reads every tracked text file under `memory/`, `.py`
included, and joins each id to the build its slug names (`gen_build_index.py:767-805`). A `missing:` id joins
nothing (`:820-828`). The predicate is the generator's own grammar, never a second one: `tree_lib.scan_missing_citations`
(`tools/memory-tree/tree_lib.py:182`) through `gen_build_index.build_roster_id_re` and `extract_roster_ids`
(`gen_build_index.py:806-828`), run over the tracked files under `memory/` and filtered to the 22 chain slugs. An id
behind a colon that is not the `missing:` form still joins, so the earlier `grep` that skipped every id after `:` was
too loose. Run over the tree at `8d33694d7`, and again at `d26d19a8e` with the same result, it finds 25 citations on 22
lines in 7 files, all of them dTrueNorth ids:

- `build/…-deviations.py`: lines 178, 180, 181, 183, 184, 185, 189, 191, 193 and 197;
- `build/…-asbuilt.py`: lines 106 and 107;
- IR: lines 7, 776 and 789;
- `build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md`: line 24483;
- `build/…-execution-plan-reviews-compared.md`: line 170;
- `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-plan-a.md`: lines 275, 277 and
  312;
- `memory/builds/dClosedLoop/reviews/2026-10-20-review-PLAY-dClosedLoop-1-execution-plan-b.md`: lines 202 and 235.

Once dTrueNorth's folder exists, `--write` joins all of them into its `ids:`. Phase 0 runs the predicate again just
before the opening, since every record written until then can add to the population.

**The fix** marks each with `missing:`, in both the fixture strings and the verbatim copies. Afterwards, each
instrument's `--fixture` and every `--plant` must give the same verdicts as before.

**The red test.** In a scratch clone, create `memory/builds/dTrueNorth/README.md` and run `gen_build_index.py
--write`:
- before the fix, the README's `ids:` gains the fixture ids;
- after it, it gains none;
- the predicate prints nothing; a planted bare id makes it print one line, and so does a planted id behind a
  colon (`x:` followed by a dTrueNorth id).

**Who may mint in a chain build.** The rule follows the claims, because two nodes share the tag letter `d` in all 22
slugs:
1. The opening (dClosedLoop's session) mints each build's roster ids, dTrueNorth's extra unit included, and the one
   carry-forward ask of each build but dTrueNorth, under that build's slug and in its derived family (P0.5). It also
   files, in dClosedLoop's own `BACKLOG.md` under dClosedLoop's slug, one ask per driver-changing build owing the
   unattended kit's clean self-test reading that build's README rule 8 waives. It mints them once, in one landing, before
   any claim exists. A session's ids are its own, and the later merge re-mints unmerged ones (HYGIENE.md:172-187).
   This departs from minting one slug per session; it is D8, carried as recommended for the owner's walk (ER:276).
2. After the opening, only the run holding a slug's claim mints under that slug (`unattended.sh:2284-2301`), in the
   one family the opening derived for that build (P0.5). Its next id is the build's highest id in that family plus one
   (HYGIENE.md:177-179).
3. A run filing an ask about another build mints it under its own build's slug and files it in the other build's
   `BACKLOG.md` (coordination return), only while that build's build run has not landed ([coordination]). Any other
   row about a foreign ask stays in its own file (ASKS:167-168).
4. An attended session takes a fresh slug of its own, never a chain slug (HYGIENE.md:174-176).
5. **The owner's "no".** When the owner rejects a departure a report lists, dClosedLoop's session records the "no"
   first as a decision row under dClosedLoop's slug, naming the choice it rejects and superseding P0.8 row 5 (or the
   row the choice cited) for that choice alone. Then it mints an ask carrying that row's id, also under dClosedLoop's
   slug, and files it as a foreign-ask row with its `SEV` row in the departing build's `BACKLOG.md`, as rule 3 does.
   `asks-disposed` scopes every ask in that build's `BACKLOG.md`, so the build's next close must dispose of it
   (ASKS:128-143). If the build's build run has already landed, the ask goes in dClosedLoop's own `BACKLOG.md`, and
   every chain packet carries it in field 9 (P0.3), so the next chain run on any node reads it.

### P0.7 The opening's gates, and its one landing

| Actor | Step | Rests on |
|---|---|---|
| Node d's session | Commit P0.1 to P0.6 and the opening on a branch | the charter's `[land]`, `AGENTS.md:31` |
| Node d's session | `open.py --check`; `packet.py --check` for all 22; `gen_build_index.py --check` and `--check-format` (the contract, both directions); the memory hygiene gate; the generator-grammar bare-id predicate (P0.6), which must print nothing; `carries.py` (exit 2 expected); `deviations.py` printing 0 members, as P0.1's acceptance names, not merely exit 0, which `--policy report` makes constant; `asbuilt.py --check` (0) | `readme-contract.txt:2-5`; `gen_build_index.py:2341-2344` |
| Node d's session | Red tests: a one-byte README edit reds `open.py --check`; a roster missing one clause reds the arm that reads every clause in exactly one row; a `parents:` typo raises; a removed contract row reds `--check-format` | as above |
| Owner | Reads in full the decision rows (P0.8, nine of them), the grant row among them, and dTrueNorth's README and packet; for the other 21 builds, reads `open.py --check`'s output and `open.py --summary`'s rows (P0.5). "Rows + dTrueNorth (Recommended)" (ER:446) | ER:441-446 |
| Owner | Asks for the landing | the charter's `[land]`, `AGENTS.md:31` |
| Node d's session | Lands through `bash tools/push-main.sh`. The pre-push bar takes the doc-only class, because the diff is `memory/` only | `.githooks/pre-push:1215-1223`; `.githooks/gate-env.sh:106-108` |

### P0.8 The policies the answers ratify, as decision rows

One `memory/DECISIONS.md` row each, minted under dClosedLoop's slug (`missing:PLAY-dClosedLoop-2` onward) and landed
with the opening. Each row cites its source:

1. The spec-run close by carry-forward (ER:84), and the owner's choice of where the units a spec run adds go:
   "dTrueNorth's extra unit (Recommended)" (ER:232) and "Carry it too (Recommended)" (ER:320). This row is the
   decision dTrueNorth's extra unit is `**Derived:**` from, and it records the owner's approval of that unit as a
   departure from v2 ([deviations]), the starting-roster reading [phase-1] specifies included.
2. The grant: "One decision row (Recommended)" (ER:181). This row is the one all 22 `may:` lines cite.
3. The chain's deviation values, `report` and `author-recorded`, applied to every run and to the instruments
   (ER:103-104, :121-127, :255), and the owner's approval of the departure from `cl-dClosedLoop-0004`: "A deviation,
   your values (Recommended)" (ER:189). The build that adds each key sets the chain's value in its own landing: "The
   adding build (Recommended)" (ER:396). dDeclaredLoop's spec carries `deviation.approval = author-recorded` and
   dScopedBuild's carries `deviation.gate = report`, each recorded as a departure citing this row; nothing waits on
   the owner.
4. Node b: "Spec runs only" (ER:219), as the schedule script's rule.
5. The standing ruling for residual forks: "Standing ruling" (ER:240), taking the most capable option where every
   surviving option passes veto 1 and fails only veto 3 or the goal bound (ER:237-238); "Standing ruling takes it
   (Recommended)" (ER:388), the same for a fork whose only options trip veto 2 outside the grant; and for a fork with
   no option left, "Relax the weakest bound" (ER:328). Each choice is recorded as a departure and marked as README
   rule 6 says; every choice with a non-`none` `widens:` or `relaxes:`, and every `grants:` choice, is listed first in
   the build's departures report (ER:284-285, :347-348, :383-384).
6. The driver-rewriting builds land through their own new code (ER:248), dPlacedRequest's migration carries its
   test (ER:264), and the owner types every start (ER:270). Each driver-changing build (P0.5's derived set) waives
   the unattended kit's own on-demand self-test suites for its landing in its README, in dAlignedCarrier's form, its
   driver changes proved by targeted probes and its own planted tests: "Waive in each README" (ER:476), at the scope
   the walk's correction states (ER:544-557). Its close still runs the flagged bar, `GATE_FULL=1 GATE_SELFTESTS=1`.
7. The coordination rules: push after every pass, never preflight over a claim, re-run the schedule at every landing,
   and reconcile at a prepare conflict ([coordination]).
8. The unit family: "Family by stream" (ER:438). Each build's roster ids and ask take its main stream's family, PLAY,
   KICK, DEPL or TOOL, by the rule and table in P0.5, which `open.py --families` prints.
9. The governance carrier: "Define it in Phase 0 (Recommended)" (ER:525). A governance carrier is a tracked path on
   the list `open.py --carriers` derives from the tree at the opening commit, and the row quotes that list. The grant
   (row 2) reads against it. The list's selectors, each with where the records bound it:
   - the routed product paths, `tools/`, `skills/`, `coding-governance-agents.template.md` and `WIRE-INTO-PROJECT.md`
     (`.memory-tree.conf:9`): at `a93477abc`, the 17 kits under `tools/` with a `kit.toml`, `tools/govkit`,
     `tools/lib` and the root-level gate scripts and their lists under `tools/` (`tools/gate-legs.json` and
     `tools/push-main.sh` among them), and `skills/session-kickoff` and `skills/deploy-governance`. The records bound
     the method's template as a carrier (`memory/builds/aClosedDocket/README.md:40`) and a kit's protocol key table as
     one (`tools/unattended/README.md:336`);
   - the git hooks, the 11 tracked files under `.githooks/`, which `core.hooksPath` wires (`tools/check-wiring.sh`);
   - the agent and role files under `.claude/`: the 9 agent definitions, `roles.json`, the 7 skills, `settings.json`
     with its hooks, and `rules/product.md`;
   - the charter: the template and its renders `AGENTS.md` and `CLAUDE.md`, which the records bound as "the
     governance carrier" (`memory/DECISIONS.md:204`);
   - the method's guides, the ten files under `memory/guides/`: BUILD-METHOD bound at
     `memory/builds/aRatifiedRulings/README.md:46` and `memory/builds/aEvidencedLens/README.md:55`,
     UNATTENDED-PROTOCOL at `memory/builds/aPrimedKeepalive/README.md:39-41`, REVIEW-PROTOCOL at
     `memory/builds/aSightedSkeptic/README.md:45`;
   - the root confs whose keys a kit's protocol tables: `.unattended.conf`, `.memory-tree.conf`, `.codebase-map.conf`,
     `.lexicon.conf`, `.process-monitor.conf`, `.gitattributes` and `.governance/deploy.toml`.

   Nothing else is a carrier: the build records, `DECISIONS.md`, the backlogs and the root `README.md` are records,
   not rules a run is held to. `open.py --carriers --check` reds a tracked path under a selector that the row's list
   omits, seen red on a planted new kit directory.

**Acceptance.** Every row quotes its answer in ER `[answers]`, `[answers-2]`, `[answers-3]`, `[answers-4]` or
`[walk]`, or names the `[defaults]` item it carries for the owner's walk.

**Not checked.** No gate reads what a row says. Each is tested where a run applies it, in phase 1.

### P0.9 Each node's preparation

| Actor | Step | Rests on |
|---|---|---|
| Each node | Exactly one remote, and `git remote set-head origin -a` | `unattended.sh:2099-2102`; `push-main.sh:180-186` |
| Each node | `bash tools/check-wiring.sh --fix`, which sets `core.hooksPath` and both merge drivers | `check-wiring.sh:1198-1215`; `.gitattributes:69-86` |
| Each node | The kickoff skill's junction | `AGENTS.md:90` |
| Each node | Register the resume tick and confirm it with `schtasks /query /tn gov-resume-tick`. Node d answered "cannot find" | `tools/unattended/README.md:211`; driver return |
| Each node | `. tools/lib/resolve-python.sh && PY=$(resolve_python) && "$PY" --version`, requiring a non-empty launcher; every schedule invocation runs `"$PY" <script>`. Sourcing the file alone only defines the function and exits 0 | `tools/lib/resolve-python.sh`; Facts: Toolchain |
| Each node | `USERNAME` must equal the fleet row's `user`, because a claim's `node:` is that variable and the schedule script maps it through the fleet | `unattended.sh:2410`; `tools/playbook/fleet.toml:21-46` |
| Node b, onboarding | Clone gov to its primary tree, then every step above. Its tag `b` is already claimed (`fleet.toml:28-33`). "Seed local memory from the in-repo mirror" names no mirror and is listed under [cannot] | `AGENTS.md:113-114`; `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-cloud-and-scale.md:434-436` |

**Acceptance.** On each node:
- `unattended.sh --claims` answers from the remote;
- `check-wiring.sh`'s check mode is clean;
- the resume tick is listed;
- `unattended.sh --plan dClosedLoop --paths` runs.

**Red tests.** Check mode reports the unset merge driver before `--fix`. The Python step is seen red with every
Python stripped from `PATH`.

## [phase-1]

dTrueNorth runs on node a as the pilot, as ONE whole run: it specs, audits, builds, reviews and lands all seven of
its units. The owner chose it: "dTrueNorth's extra unit (Recommended)", whose option reads "dTrueNorth runs as one
whole run, spec and build together, and adds the fix as one unit, a departure from v2 the owner approves" (ER:224-232).
Its run lands before any other chain spec is written, because the coverage and deviation gates must stand before the
first chain spec (FQ:276-278, :302-303). Being whole, its run closes without carry-forward, and the owner sees its
coverage in its departures report after its code, not before: the price of that choice.

**Its units.** The six clauses of its v2 row, `cl-dClosedLoop-0001` to `-0006`, and the extra unit.

**The extra unit**, a departure from v2 the owner approved (ER:232, widened at ER:320; [deviations]). It changes the
carry-forward term's second condition (`unattended.sh:5156`, `:5177-5184`; STOPS:703-704), and the starting-roster
reading that condition rests on, so that:
- **a spec run** is the README's rule (P0.5, rule 1) read by the driver: a run whose build's `BACKLOG.md` at the run's
  baseline commit holds an open ask, which the opening files in every chain build but dTrueNorth (P0.5), and whose
  starting roster, read by `baseline_units` at the run's start, has a unit `MISSING`. The ask test applies first and is
  read at the baseline commit, so an ask the run files itself does not count, and dTrueNorth's whole run, whose roster
  is all `MISSING` at its start, never qualifies. Whether a run closes a unit plays no part, since a build run that
  closes nothing would meet that test too;
- a spec run may carry forward a `DEFERRED` unit it added, whether its own spec audit or its own closing diff review
  promoted it (METHOD:144, :274) or the run adopted it as a discovery (PROTOCOL:640-690), to its own build's next run,
  once. The owner: "Carry it too (Recommended)", whose option reads "widen dTrueNorth's extra unit so any unit a spec
  run adds carries forward to its own build run once" (ER:314-320);
- **once** has a witness: the spec run's add and defer rows, read only from a rotated `RUN.<phase>.<blob8>.md` of the
  same build whose phase is the landed one, which preflight keeps (PROTOCOL:153-158). An aborted run's rows do not
  count. At the close the driver refuses a `DEFERRED` unit an earlier landed run of the same build carried, and names
  it. The build run must build it;
- a unit added by a build run or a whole run is refused as today: it is built in that run;
- **the starting roster** is read, when the generated `gen:build-units` region at the spec run's baseline commit names
  no unit, from the authored `roster:units` pair at that same commit. The fallback goes inside `baseline_units`
  (`tools/unattended/lib-unattended.sh:1950-2018`), so all three of its callers take it:
  - `unattended.sh:5173`, the carry-forward close's condition 2: under the fallback it reads the authored roster and
    carries every roster unit;
  - `unattended.sh:13257`, the driver's `--rescope --act add` arm (fail 48, no fallback commit): under the fallback
    the starting roster can be derived, so an add of a unit the generated region already carries is accepted as a LATE
    record instead of failing 48 "cannot be derived" (red case 12);
  - `tools/unattended/check-unattended.sh:3907`, check 24, the checker: under the fallback its ADD arm reads the
    authored roster, so a unit added without an `add` row fails 24 instead of being skipped (red case 11), and the
    checker and the driver agree.

  Without it, every chain spec run fails `build-complete` at `--close`, since its build has no spec at its start and
  the generated region is rendered from specs. This is inside the owner's approval of the extra unit: it is the
  reading the approved condition needs to work at all (ER:232, :320).

The other carry-forward terms are unchanged, so an added unit carries forward only with spec status `DEFERRED`, a
defer row, and a header that advances the build's ask (STOPS:700-711). The spec run specs and audits every unit it
adds, through the harness's audit scoped to the added ids (`unattended-build.js:180-183`), and records each as a
departure, with follow-through "new unit <id>" (ER:315-316). The unit's spec re-renders STOPS §15's second term and the
verbs' close rule 9 from their templates. Its red cases, each seen red before the change and as stated after it:
1. a spec-run fixture with one review-promoted `DEFERRED` unit: refused before, carried after;
2. a spec-run fixture with one adopted discovery's `DEFERRED` unit: refused before, carried after;
3. the build run, with the spec run's `RUN.md` rotated, deferring either carried unit again: refused;
4. a unit added and deferred by a build run that closed a unit: refused, before and after;
5. a base README with `roster:units` rows and no spec, its opening ask filed. The plant, in a scratch clone, opens one
   build as P0.5 specifies and follows README rule 1 in full: it specs every roster unit, defers each with a
   `DEFERRED` spec carrying `advances <the opening's ask>` and a defer row, then runs `--close`. Before the change the
   close fails term 2 with "the roster this run started with … cannot be read", naming the units it read as added;
   after it, the carry-forward term is met with every unit in `BC_CARRIED`. It is seen red with the fallback removed.
   The fixture is kept standing in the unattended kit's own test suite, which runs only on demand
   (`tools/unattended/run-unattended-gates.sh:2`) and which README rule 8 waives for this landing; dTrueNorth's run
   runs it, and every red case here, as a targeted probe. It also runs check 24
   over the same scratch-clone run and requires it to agree with the driver. A one-unit variant is a separate case with its own stated verdict;
6. a build-run fixture that closes zero units and defers a unit it added: refused, before and after;
7. a build run that closes no unit and re-defers a unit the spec run carried: refused;
8. a whole-run fixture, no open ask at its baseline and every authored unit `MISSING` at its start, whose closing
   review promotes a unit it then defers: refused, before and after;
9. a spec run aborted after its defer rows, rotated, then run again, which defers the same units: carried, since an
   aborted run's rows are no witness;
10. red case 5's fixture plus one unit the spec run added: the spec run carries it as an added unit, not a roster
    unit, and the build run that then re-defers it is refused;
11. check 24 with an empty generated region at base, an authored roster naming units, and one unit added without an
    `add` row: skipped before the change, fail 24 after;
12. `--rescope --act add` of a unit absent from the authored roster but present in today's generated region: fail 48
    "cannot be derived" before, accepted as a LATE record after;
13. a build with an empty generated region and an empty or absent authored roster: check 24's ADD arm still skips.

It edits `tools/unattended/`, so the `VERIFYING` notice owes the flagged bar, and its close exports `GATE_FULL=1
GATE_SELFTESTS=1` (`.unattended.conf:40`; `unattended.sh:10528`). dTrueNorth is a driver-changing build, and its
README waives the unattended kit's own on-demand suites for this landing (P0.5, rule 8; "Waive in each README",
ER:476): the thirteen red cases and the unit's targeted probes are what prove the driver change. It is
a driver-touching unit, so under the owner's "Land through new code (Recommended)" (ER:248) it goes last in the run,
and dTrueNorth lands through it.

**Preconditions:** the opening has landed, with the three decision rows dTrueNorth reads (P0.8, rows 1, 2 and 3).

| Actor | Step | Rests on |
|---|---|---|
| Node a | `git fetch; bash tools/unattended/unattended.sh --claims; "$PY" <schedule script> --ref origin/main` shows `a: whole dTrueNorth at 0` | [schedule]; P0.4; P0.9 |
| Owner, on node a | Create a fresh worktree off `origin/main` on a new branch, open a session there, and type `/unattended dTrueNorth` | PROTOCOL:21-27; `unattended.sh:2929-2938`; ER:270 |
| Run | Schedule the keepalive, then `--preflight`, then `/session-kickoff` | `SKILL.md:16-20`, `:63-65` |
| Run | **Proof 1.** Preflight prints `spec-audit — opted in by README spec-audit: <date>`. `RUN.md` records `anchor-kind: default-branch` and the pinned `may:`, the grant row's id and the extra unit's | VERBS:722-728; IR:862-869 |
| Run | Read in the [handoffs] order; `packet.py --check dTrueNorth` | P0.3 |
| Run | The build harness with the pinned `specAudit`: SPEC authors the seven specs, then AUDIT, then DISPOSAL | VERBS:722-748; `unattended-build.js:6-8` |
| Spec writer | The spec carrying `cl-dClosedLoop-0004` writes the owner-approved deviation record in its own commit; the extra unit's spec carries `**Derived:** <its decision row>` and its own record ([deviations]) | v2:1764; `carries.py:11`; ER:189, :232 |
| Run | At its Design exit, `carries.py --build dTrueNorth --exit` and `deviations.py --policy refuse`, by hand, since nothing in the bar runs them yet. `refuse` exits 1 on an unjoined member or an approver below its risk; the chain's runs keep `report` | P0.1; deviation return, limit 4 |
| Run | Builds the units one at a time, the extra unit last. The product join takes the instruments' plant suite as its acceptance (D3, carried). Its configuration cutoff is the opening landing's date, so every chain spec, dTrueNorth's own included, falls on or after it | VERBS:697-768; v2:1764; deviation return, recommendation 3 |
| Run | The closing review over the whole range; its promoted units are built in this run, as M4 rules | METHOD:144, :251-290 |
| Run | `--phase VERIFYING`, `--prepare`, then the close sequence of README rule 4 on the prepared merge (`--report dTrueNorth`, a record for each member "recorded by nobody", `--report --write` as `…-departures-build.md` and commit, `--report --check`), then `--authorization`, `--close` under `GATE_FULL=1 GATE_SELFTESTS=1`, the flagged bar the driver owes; the unattended kit's own on-demand suites are waived for this landing by README rule 8, so the landing report carries no `--selftests` verdict; then `--land`, `--landed` | VERBS:849-947; `unattended.sh:10528`; P0.5, rules 4 and 8; ER:476 |
| Owner | Reads the departures report and the coverage it carries. A "no" to a listed departure takes P0.6 rule 5: a decision row recording it, then, since dTrueNorth's whole run has landed, an ask in dClosedLoop's `BACKLOG.md`, which every chain packet carries in field 9 (P0.3) | [owner]; P0.6 |
| Every node | From this landing, the product join runs in every pre-push bar, every `--close` and remote CI, and every new worktree carries the new carry-forward condition | `.github/workflows/remote-ci.yml:106`; `SKILL.md:9-12` |

**What the pilot proves**, each a first:
1. A README landed on main opts the run into the audit and pins a grant. No run has done either (driver return).
2. A run that changes the driver lands through its own new code, the rule the owner set for the three driver
   builds (ER:248).
3. The product join reds on every plant of P0.1.
4. The carry-forward condition's thirteen red cases.

**What it no longer proves.** Being whole, it does not exercise the spec-run close, the build run's pickup of a
terminal claim (STOPS:221) and its `DEFERRED` units (`unattended.sh:4815`), the ask carried through both runs
(ASKS:136-143), or the harness called again after a spec run's audit (`unattended-build.js:180-230`). dGroundRules'
two runs, which node a starts next, are the first to do each.

**How the product takes over from the instruments without a gap.** Under J, no other chain spec is written before
dTrueNorth's build lands, so no chain spec lands ungated except dTrueNorth's own, which the instruments check by
hand. From that landing, both run together. The product legs run in the bar. The departures report runs the
instruments still in service at every build's close. A disagreement between an instrument and the product becomes an
ask in the `BACKLOG.md` of the build that lands that instrument's successor in the table below, dOrderedCharter,
dDeclaredLoop, dIndexedDesign or dScopedBuild, whose next close disposes of it (ASKS:128-143); that build has not
landed while its instrument still runs. Each instrument stops being run when the clause that succeeds it lands, and
the table says what the departures report and the packet read from then on. The inventory was taken by value, from
every plan line naming `carries.py`, `asbuilt.py` or `deviations.py`.

**The report-switch step.** Switching what `--report` reads is an edit to `deviations.py`, an instrument every packet
pins, so no run makes it. At the landing the table names, the landing build files an ask in dClosedLoop's
`BACKLOG.md` (P0.6, rule 3). Under that ask, dClosedLoop's session edits `deviations.py --report` to read the
successor, or to stop running the retired instrument, and re-pins every packet with `packet.py --repin
deviations.py` (P0.3). The edit and the re-pin land together in an owner-asked landing that lands nothing else,
recorded as a decision row, so no packet goes red between them. Until that landing, `--report` keeps reading the
instrument it read.

| Instrument, or arm | Retired by | Lands with | What the report and the packet read from then on |
|---|---|---|---|
| `asbuilt.py` | `cl-dClosedLoop-0006`'s product view, once it renders byte for byte what `asbuilt.py --write` renders on the same records | dTrueNorth | The product as-built view, after the report-switch step at dTrueNorth's landing and its re-pin of `deviations.py`. The packet keeps `asbuilt.py`'s pin, as every re-render keeps the pins it carries ([handoffs]) |
| `carries.py --report` inside the report | `cl-dClosedLoop-0003`'s coverage region in each README | dTrueNorth | The README's coverage region, after the same step at dTrueNorth's landing. Only dTrueNorth's own report reads `carries.py --report` |
| `deviations.py`'s risk reading | the widening classifier `cl-dClosedLoop-0066` | dOrderedCharter | The classifier's risk class, after the report-switch step at dOrderedCharter's landing and its re-pin |
| `deviations.py`'s approval arm | `deviation.approval`, `cl-dClosedLoop-0119` | dDeclaredLoop | The key's approver verdict, at the chain's `author-recorded`, after the step at dDeclaredLoop's landing and its re-pin |
| `carries.py` | `design.coverage`, `cl-dClosedLoop-0398` | dIndexedDesign | The product join's output, after the step at dIndexedDesign's landing and its re-pin of `deviations.py`. The packet keeps `carries.py`'s pin |
| `deviations.py`'s population and join | `deviation.gate`, `cl-dClosedLoop-0412` | dScopedBuild | `deviation.gate`'s output, at the chain's `report`, after the step at dScopedBuild's landing and its re-pin |
| The `--report` mode itself, README rule 4's close sequence, and `deviations.py`'s pin in each packet | nothing in the chain | — | They outlive the join: the report's blocks for the marked choices, the forks, the carried units and the outside paths have no product successor, so `--report` keeps running through dConvergedCharter, reading the successors above |

## [phase-2]

### The spec run, from start to landing

| Actor | Step | Rests on |
|---|---|---|
| Node | `git fetch; bash tools/unattended/unattended.sh --claims; "$PY" <schedule script> --ref origin/main`. Take the spec run your node holds at time 0 | VERBS:769-774; P0.4; P0.9; [coordination] |
| Owner | Fresh worktree off `origin/main`, then `/unattended <slug>` | PROTOCOL:21-27 |
| Run | Keepalive, preflight, kickoff. Keep the preflight's `spec-audit` line | `SKILL.md:16-20`, `:63-65` |
| Run | Read in the [handoffs] order. Run `packet.py --check <slug>`. If it is red on a moved instrument blob, stop: that is never re-rendered away. If it is stale for any other cause, re-render it keeping the instrument pins it carries, and commit | P0.3; [handoffs] |
| Run | The build harness, with `specAudit` set to the pinned date and with `base`, `scratch`, `roles` and `efforts`; each unit's `specBriefPath` is the packet. It runs SPEC (writers author every `MISSING` spec), then AUDIT, then DISPOSAL | VERBS:722-748; `unattended-build.js:6-8`, `:169-178` |
| Spec writers | Each spec carries `**Carries:** cl-…@<hash8> whole` (or `part k/n`), the owned nodes it builds, and its fork marks | `carries.py:7-12`; TEMPLATE-SPEC:155-160 |
| Run | For each unit: `--rescope <slug> --act defer --item <unit> --reason "specced; built by this build's build run"` | VERBS:703-710; STOPS:705-706 |
| Run | For each spec: status `DEFERRED`, with `advances <the ask>` in the header tail | TEMPLATE-SPEC:61-82; STOPS:700-709 |
| Run | In the build's `BACKLOG.md`, the ask's `DEFERRED … until <the build run>` row, so `asks-disposed` reads it as held | ASKS:136-143 |
| Run | A unit the run adds, promoted by the spec audit or the closing review or adopted as a discovery, is specced, audited through the harness's audit scoped to the added ids, recorded as a departure, deferred with `advances <the ask>` and carried forward like the rest, under the condition dTrueNorth's extra unit added | phase 1; ER:232, :314-320; `unattended-build.js:180-183`; PROTOCOL:640-690 |
| Run | `carries.py --build <slug> --exit` at its Design exit, while `carries.py` is in service (the retirement table in [phase-1]) | P0.1; deviation return, limit 4 |
| Run | The closing review over the spec commits, recorded with `--review <slug> --subject <slug> …` | METHOD:251-265; VERBS:778; PROTOCOL:352 |
| Run | Push the run branch after every pass commit | [coordination] |
| Run | `--phase VERIFYING`, then `push-main.sh --prepare` | VERBS:849-862 |
| Run | The close sequence of README rule 4, on the prepared merge: `deviations.py --report <slug>`; a record for each member "recorded by nobody"; `--report <slug> --write` as `…-departures-spec.md`, and commit; `--report <slug> --check`. After any reconcile and re-prepare, again | P0.2; P0.5, rule 4; `push-main.sh:505-538` |
| Run | `--authorization`, `--close` (attesting `keepalive-reaped`, and `parked-decisions-surfaced` with a count that includes the defer rows), `--land`, `--landed` | VERBS:849-947 |
| Driver | Writes the claim `landed` | `unattended.sh:6242-6247` |

### The build run, on whichever node the script names

| Actor | Step | Rests on |
|---|---|---|
| Node | `git fetch; bash tools/unattended/unattended.sh --claims; "$PY" <schedule script> --ref origin/main`. Build runs start only once every parent has landed, which the script derives from the tree | P0.4; P0.9 |
| Owner | Fresh worktree, then `/unattended <slug>`. The preflight takes the terminal claim over and rotates the spec run's `RUN.md` | STOPS:221; PROTOCOL:153-158 |
| Run | `--plan <slug> --paths` lists every `DEFERRED` unit as non-terminal and READY | VERBS:72-87, :753-760; `unattended.sh:4815` |
| Run | Re-ground each spec against the parents that have just landed by re-running its §10 probe. Revise it before its first `Pass:` commit. Under the product join, a revision past the pinned audited revision is a member, so the run writes its record, approved by its author | `deviations.py:20-27`; v2:1764 (`cl-dClosedLoop-0004`) |
| Run | The harness with the pinned `specAudit`. How its audit stage treats specs the spec run already audited is first observed in dGroundRules' build run | VERBS:722-731; `unattended-build.js:180-230` |
| Run | Per unit: `--brief`, `--dispatch --writes …`, the unit harness, a commit with a `Pass: <unit>` trailer, then `gotchas.py --for-diff HEAD~1..HEAD` | VERBS:697-768 |
| Run | Each unit's header goes `INPROGRESS`, then `CLOSED`. A unit the spec run added and carried is built; deferring it again is refused. The last unit to close carries `closes <the ask>` | TEMPLATE-SPEC:61-82; phase 1 |
| Run | The closing review over the build's range. Its findings are promoted and built in this run | METHOD:144, :251-290 |
| Run | `--phase VERIFYING`, `--prepare`, the close sequence of README rule 4 with the report named `…-departures-build.md`, then `--authorization`, `--close`, `--land` and `--landed`, as in the spec run | VERBS:849-947; P0.5, rule 4 |

### How a fork is settled when nothing may park

Each rung uses only today's driver and the owner's grants. Each resolution is recorded as a §8 mark
(TEMPLATE-SPEC:155-160) and a `Decided:` trailer (METHOD:316-320), and the departures report explains it (P0.2).

1. **v2 answers it.** The spec cites the clause; the mark is `RESOLVED (agent, <date>, delegated)`. This is the close
   table's "a question the default branch already answered" (STOPS:692).
2. **A stated probe decides it**, as a `FACT-QUESTION` (METHOD:100-104).
3. **The mandate delegates it.** The run takes the most feature-rich option that survives the vetoes (METHOD:86-95),
   with veto 2 lifted where the grant covers the change (METHOD:82). A choice the grant lifted carries `grants:
   <decision id> <change>` and is listed first in the departures report (P0.2).
4. **A strictly beneficial discovery** is adopted (PROTOCOL:640-690). In a spec run its unit is specced, audited,
   recorded as a departure and carried to the build run: "Carry it too (Recommended)" (ER:320).
5. **The owner's standing ruling**: "Standing ruling" (ER:240), and "Standing ruling takes it (Recommended)"
   (ER:388). Where every surviving option passes veto 1 and fails only veto 3, the goal bound, or veto 2 outside the
   grant (a new external dependency or install location, or a governance-carrier or public-surface change none of the
   build's own `[chain]` clauses names), the run takes the most capable of them, the one meeting the most stated
   acceptance criteria (METHOD:86-97), and records it as a departure. The option's own words are "the most capable
   option that fails only the security veto or the goal bound" (ER:237-238), and ER:388 adds the veto-2 case. An
   option that also fails veto 1 goes to rung 6 first. A choice that widens a surface or makes a veto-2 change carries
   `widens: <surface or change>` and is listed first in the build's departures report (ER:284-285, :383-384; P0.2); a
   goal-bound-only choice carries `widens: none` and is listed with the other forks.
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
  README's rule. Any path under `memory/builds/dClosedLoop/build/*.py`, or any changed pin line in a `*-packet.md`, in
  any chain run's diff means it edited an instrument or a pin: the owner's check stands in for the gate no phase-0
  record can add ([cannot]).
- **The coverage report**: the README's generated coverage region (`cl-dClosedLoop-0003`), which every spec landing
  has, since dTrueNorth's whole run lands it first.
- **Every departure from v2**, with its record; every fork the run settled, the `widens:`, `relaxes:` and `grants:`
  choices first; every unit the spec run added, from a review or a discovery, and carried to the build run; and every
  path the run wrote outside its own build folder.

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
- an ask lands in dClosedLoop's `BACKLOG.md` naming a chain build (P0.3, field 9).

The build's own runs re-render it: `--check` at every M7 reground (METHOD:231-246), and on red for any cause but a
moved instrument blob, re-render and commit before the next pass. `--write` keeps the instrument pins the packet
already carries, and `--check`'s pin arm reds a moved blob whatever the byte compare says (P0.3). A packet red on a
moved instrument blob is a stop and is never re-rendered: a pin-keeping re-render cannot re-pin a moved blob away.
Only the owner's re-pin moves a pin: `packet.py --repin <instrument>`, refused inside a chain run, run by
dClosedLoop's session in an owner-asked landing that lands nothing else, recorded as a decision row. A hand edit of
the packet's pin line, or of `packet.py`, can still move a pin; until a chain unit's merge-bar check, the only guard
is the owner's landing-diff check ([owner]; [cannot]). A run must not
write another build's packet or any other path outside its own build folder (P0.5, rule 7). No gate refuses a run's
own commit to another build's paths: the `--close` refusal of another build's commit grades only commits carried
through local main (fail 66, `unattended.sh:10540`), so the README rule forbids it, the departures report lists it,
and the closing review reads it.

## [coordination]

**The node loop**, at every landing and whenever a node is free:

| Actor | Step | Rests on |
|---|---|---|
| Node | `git fetch`, then `unattended.sh --claims`, which fetches every claim into the local cache | `unattended.sh:2136` (coordination return); VERBS:769-774 |
| Node | `"$PY" build/…-schedule.py --ref origin/main`, with `$PY` from P0.9. It pins every held chain claim, and every live one within `RESUME_STALE_BOUND`, to its node; prints a stale one and marks its run "take over (stale)", which the node takes over under the stale-claim rule below, never starting it in a fresh worktree; keeps an off-fleet one off every table; pins a b claim only to a spec run; and derives each build's phase from the specs on `origin/main` | P0.4 |
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
commit, then `--authorization` and `--prepare` again (`push-main.sh:881-882`; VERBS:921-926), and then README rule
4's close sequence again on the new prepared merge. Generated files are re-rendered, never hand-merged
(`AGENTS.md:33`).

**Shared records.**
- `DECISIONS.md` and every `BACKLOG.md` merge by rows; `LIVE.md` and the ledgers are re-rendered (`.gitattributes:71-86`).
- `readme-contract.txt` is written once, by the opening, so no chain run touches it (P0.5).
- The hot shared files (`unattended.sh`, `tools/gate-legs.json` and the renders) meet only at the prepare conflict.
  Of the 34 build pairs the chain does not order, at least 3 name a shared path in v2 (a lower bound: rows mostly
  name keys, not files; coordination return, §2).

**Asks across builds.** A problem in another build is an ask in that build's `BACKLOG.md`, minted under the filer's
own slug and pushed (P0.6). It may be filed only in a build whose build run has not landed, since only a later close
disposes of it: the ask enters that build's `F` set, so its next close must dispose of it (ASKS:128-143). A problem
in a build that has already landed is an ask in the finding run's own `BACKLOG.md`, naming that build, which its own
close disposes of. A run that has merged `origin/main` checks its own `BACKLOG.md` before `--close`.

**When another node's work is in the way:**
- A live or held claim on the slug: take the next run the script names. Never preflight over it.
- An overlap line at preflight or on the card: if the other ref is a parent, wait; otherwise go on, and the later
  lander reconciles (`unattended.sh:3409`, which always returns 0).
- Foreign commits on local main: `--carry` refuses them, so land from the branch (coordination return).
- Two builds recording contradictory decisions on one key: both rows merge clean (GR:329). The owner arbitrates
  ([cannot]).

## [schedule]

The script was run from the worktree root at HEAD `d26d19a8e`, after both review folds, with `$PY` resolved as P0.9
says (it resolved to `python3` on node d). Its exit code was 0. The folds changed only how the script reads claims: a
stale live claim, an off-fleet claim and a node-b claim on a build run are not pinned; a stale run is marked "take over
(stale)"; an unreadable beat is printed and kept pinned; and a claim on a node a figure leaves out is left unpinned
(P0.4). They did not change the model's runs, durations or precedences, and no claim on a chain build is cached on
node d, so the output is the same bytes as before either fold.

```
$ . tools/lib/resolve-python.sh && PY=$(resolve_python) && "$PY" -B memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py
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
| dTrueNorth | `**Carries:**` lines, the carries join in the spec-tokens leg, the coverage region, deviation records and their join, `@rev-N` pins (`cl-dClosedLoop-0001` to `-0006`); and its extra unit, the carry-forward condition in `tools/unattended/` (ER:232) | Nothing to install: every new worktree runs the new driver from its own tree (`SKILL.md:9-12`). Every packet's parent state goes stale. From here every spec run closes with the new condition. The report-switch step follows this landing: an ask in dClosedLoop's `BACKLOG.md`, then dClosedLoop's edit of `deviations.py --report` and `packet.py --repin deviations.py` in one owner-asked landing ([phase-1], the retirement table). A driver-changing build: its README waives the unattended kit's own on-demand suites for its build run's landing, which still closes under `GATE_FULL=1 GATE_SELFTESTS=1` (P0.5, rule 8; ER:476) | none: nothing else runs before it | none |
| dSafePassage | The upgrade-step kind, and `.agent-cap.conf` retired by a step (`cl-dClosedLoop-0018`) | Run the upgrade steps on each machine | Rotate its session at the next pass boundary | Same |
| dOrderedCharter | The charter re-founded and `AGENTS.md` re-rendered (`cl-dClosedLoop-0032`), including the fork-resolving decision principles | Fresh sessions load the new charter. M7 does not re-read it (METHOD:238-246). The report-switch step follows this landing: an ask in dClosedLoop's `BACKLOG.md`, then dClosedLoop's edit of `deviations.py --report` and `packet.py --repin deviations.py` in one owner-asked landing ([phase-1], the retirement table). A driver-changing build: its README waives the unattended kit's own on-demand suites for its build run's landing, which still closes under `GATE_FULL=1 GATE_SELFTESTS=1` (P0.5, rule 8; ER:476) | Rotate at the next pass boundary. From here, residual forks resolve by the principles, which take over from the owner's standing ruling (ER:240) | Same |
| dDeclaredLoop | The roles stage table moved (`cl-dClosedLoop-0086`); `unattended.sh` re-pointed to `review.max-rounds` (`cl-dClosedLoop-0106`); `deviation.approval` (`cl-dClosedLoop-0119`) | None: dDeclaredLoop's own landing sets `deviation.approval = author-recorded`, carried by its spec under P0.8 row 3 and recorded as a departure: "The adding build (Recommended)" (ER:396). The instruments' approval arm retires. The report-switch step follows this landing: an ask in dClosedLoop's `BACKLOG.md`, then dClosedLoop's edit of `deviations.py --report` and `packet.py --repin deviations.py` in one owner-asked landing ([phase-1], the retirement table). A driver-changing build: its README waives the unattended kit's own on-demand suites for its build run's landing, which still closes under `GATE_FULL=1 GATE_SELFTESTS=1` (P0.5, rule 8; ER:476) | Merge `origin/main` at the next pass boundary, then `--authorization` (VERBS:923-926). The prepare lands it through the new driver | Same |
| dPlacedRequest | Run claims migrated onto leases (`cl-dClosedLoop-0120`) | Its spec carries the test that a live claim on another node survives the migration (ER:264); a drain, no other chain run live or held, only if that test could not be written. A driver-changing build: its README waives the unattended kit's own on-demand suites for its build run's landing, which still closes under `GATE_FULL=1 GATE_SELFTESTS=1` (P0.5, rule 8; ER:476) | Its claim survives, by the test | Same |
| dWitnessedBar | The pre-push hook reads a runner-written verdict (`cl-dClosedLoop-0342`) | The next push goes through the new hook. A driver-changing build: its README waives the unattended kit's own on-demand suites for its build run's landing, which still closes under `GATE_FULL=1 GATE_SELFTESTS=1` (P0.5, rule 8; ER:476) | Lands through it | Lands through it |
| dKeptSession | Named presets (`cl-dClosedLoop-0141`); `mailbox.answer` (`cl-dClosedLoop-0504`) | Named presets make an override on `standard` expressible; the `author-recorded` value dDeclaredLoop already set is carried as that override. The `report` value waits for `deviation.gate` at dScopedBuild | Nothing | Nothing |
| dBoundRoles | The role roster and definitions rewritten (`cl-dClosedLoop-0166` onward) | Re-render the role agents | Rotate. `handoff.py harness-args` now prints the new roles | Same |
| dTotalRecall | The README's front-matter schema refuses unknown keys (`cl-dClosedLoop-0215`) | The opening's keys are all known (P0.5) | Nothing | Nothing |
| dFurnishedOrders | The per-pass checklist retired from the method and the Skill (`cl-dClosedLoop-0195`) | None | Picked up at the next reground, since M7 re-reads METHOD | Same |
| dWellOiledMachine | The `next` verb, with `--plan` and `--status` re-pointed (`cl-dClosedLoop-0280`); the unattended kit dissolved, with `/unattended` kept as a client of `run` until dConvergedCharter retires it (`cl-dClosedLoop-0306`); `gov-session` retired (`cl-dClosedLoop-0320`) | **The driver's successor.** Runs started after this landing still start with `/unattended <slug>`, now a client of `run`. Its verbs are the ones the landed kit's usage and its landing record name, which each packet re-renders. A driver-changing build: its README waives the unattended kit's own on-demand suites for its build run's landing, which still closes under `GATE_FULL=1 GATE_SELFTESTS=1` (P0.5, rule 8; ER:476) | Merge `origin/main` and run `--authorization` at the next pass boundary. Its landing goes through the successor, under the in-flight test dWellOiledMachine's spec carries | Same |
| dIndexedDesign | The Design-to-Build hand-off (`cl-dClosedLoop-0383`) and `design.coverage` (`cl-dClosedLoop-0398`) | `carries.py` stops being run; the departures report reads the product join's output (the retirement table in [phase-1]). The report-switch step follows this landing: an ask in dClosedLoop's `BACKLOG.md`, then dClosedLoop's edit of `deviations.py --report` and `packet.py --repin deviations.py` in one owner-asked landing ([phase-1], the retirement table) | Closes through the new Design exit | Nothing |
| dRankedPlan | Priority beside `parents:` and the plan view (`cl-dClosedLoop-0369`) | The plan view is the product successor of the schedule script's ordering | Nothing | Nothing |
| dScopedBuild | Built specs frozen (`cl-dClosedLoop-0400`); `deviation.gate` (`cl-dClosedLoop-0412`) | None: dScopedBuild's own landing sets `deviation.gate = report`, carried by its spec under P0.8 row 3 and recorded as a departure (ER:396). The `deviations.py` join stops being run; the `--report` mode reads `deviation.gate`'s output and keeps running (the retirement table in [phase-1]). The report-switch step follows this landing: an ask in dClosedLoop's `BACKLOG.md`, then dClosedLoop's edit of `deviations.py --report` and `packet.py --repin deviations.py` in one owner-asked landing ([phase-1], the retirement table) | Nothing | It may not revise a landed unit's spec; it adds a unit instead |
| dShippedRelease | The landing record and the lander (`cl-dClosedLoop-0413`) | Every later landing goes through the new lander | Lands through it | Lands through it |
| dConvergedCharter | Every remaining kit conf key folded into the policy file (`cl-dClosedLoop-0485`), and `/unattended` retired | The chain is done; D5 sets the two deviation keys. A driver-changing build: its README waives the unattended kit's own on-demand suites for its build run's landing, which still closes under `GATE_FULL=1 GATE_SELFTESTS=1` (P0.5, rule 8; ER:476) | none | none |

## [deviations]

**The owner's rule, applied** (ER:103-104, :121-131). A departure is recorded and explained, and it never waits for
the owner:
- Approval is `author-recorded`. The run's own author role signs the record, naming its role.
- The gate is `report`: "Report, as read (Recommended)" (ER:255). The join never refuses a landing; it lists, and a
  step before the close gives each listed member a record.
- The instruments carry the same values until the product keys exist (P0.1), and dTrueNorth's stand-in carries them
  by the owner-approved departure below (ER:189).
- A residual fork is settled by the owner's standing ruling (ER:240), which also takes a fork whose only options
  trip veto 2 outside the grant (ER:388), and a fork with no option left by relaxing its weakest bound (ER:328); each
  is recorded as a departure and marked ([phase-2], rungs 5 and 6; P0.5, rule 6).
- Each build's value for the two deviation keys is set by the build that adds the key, in its own landing, as a
  departure under P0.8 row 3: "The adding build (Recommended)" (ER:396).
- Every unit a spec run adds, from a review or a discovery, is recorded as a departure (ER:315-316).

**What is recorded where.**
- **A departure from v2 or from a spec past its first pass** is a deviation record in the departing build's `build/`,
  `<date>-build-<unit>-deviation-<n>.md`, with the fields `deviations.py:6-16` names. A `relaxes:` choice's record
  also carries `**Bound:**` and `**Tier:**`, and a `widens:` choice's record `**Surface:**`, each beside `**Reason:**`,
  in `deviations.py`'s bold-key form. It is written in the departing unit's own commit (`cl-dClosedLoop-0004`).
- **A fork the run settled** is a §8 `RESOLVED` mark and a `Decided:` trailer (METHOD:316-320).
- **A unit carried forward** is a defer row in `RUN.md` (VERBS:703-710).
- **A park** is a park row (VERBS:36-46).

**The end-of-build departures report** (P0.2) is generated at each run's end by README rule 4's close sequence, after
the final successful `--prepare` and on the prepared merge, from those records, the computed population and M9's
derivation (METHOD:293-305). It lists first, side by side, every choice marked `widens:` (a widened surface or an
ungranted veto-2 change), `relaxes:` or `grants:` (ER:284-285, :347-348, :383-384), then every member, recorded or
not, every other fork settled, every unit carried, and every path written outside the run's own build folder. The
sequence runs `--report`, then a record for each member it lists "recorded by nobody", then `--report --write` and
`--report --check`, before `--authorization` and `--close`. No gate makes the run write those records, as the owner
chose (ER:255); the report shows any member still unrecorded. Nothing checks the report's base against the final
prepared merge until the landing record (`cl-dClosedLoop-0413`), and the sequence runs again after any reconcile.

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
- A surface or an ungranted veto-2 change the standing ruling took, or a unit's acceptance a relaxed bound rewrote,
  until the owner reads the report. The validating arm reds a ruling trailer that lacks either key, or whose key is
  `none` where its ruling requires a value (P0.2). What it cannot see is a veto-3 choice under ER:240 marked `widens:
  none`, since a goal-bound-only choice is legitimately marked so, and a choice that cites no ruling at all.
- An instrument a run edits under `memory/builds/dClosedLoop/build/`: a pin-keeping re-render cannot re-pin it away,
  and `--check`'s pin arm reds it (P0.1, row 10), but a hand edit of the packet's pin line, or of `packet.py`, can
  move the pin. The owner's landing-diff check is the only guard, and no merge-bar check compares an instrument's blob
  with its blob at the opening ([cannot]).
- Whether the bound a run relaxed was in truth the least important. Only a reader checks the tier against the
  record's own citation; within a tier it is the run's judgement and its written reason.
- Under `author-recorded`, who actually approved.

**The departures the owner has approved, where each is recorded, and when.** None is applied by this plan.

| Departure | Departs from | The owner's approval | Recorded where | When |
|---|---|---|---|---|
| dTrueNorth's stand-in join reads the chain's values, `report` and any recorded approver, until dDeclaredLoop's and dScopedBuild's keys land | `cl-dClosedLoop-0004@c374ccd0`, which fixes the by-risk table and a red on an approver below the risk | "A deviation, your values (Recommended)" (ER:189), quoting answer 3 of `[answers]` (ER:103-104) | **Deviation record 1**: `memory/builds/dTrueNorth/build/<date>-build-<that unit>-deviation-1.md`. Cause: owner ruling; risk: loosening; approver: owner, citing P0.8's row 3, the decision row that records ER:189, as P0.1 row 6 requires | Approval: the decision row, in the opening landing. Record: dTrueNorth's whole run, in the commit that writes that unit's spec, as `cl-dClosedLoop-0004` itself asks |
| dTrueNorth's extra unit: the carry-forward condition for every unit a spec run adds, from a review or a discovery, once, and the starting-roster reading it rests on ([phase-1]) | dTrueNorth's v2 row, which plans six units (v2:1764) | "dTrueNorth's extra unit (Recommended)" (ER:232), after the owner's "that sounds like a bug" (ER:196-197), widened by "Carry it too (Recommended)" (ER:320) | **The decision row**, P0.8's row 1, which the unit's spec cites as `**Derived:**`; and **deviation record 2**: `memory/builds/dTrueNorth/build/<date>-build-<the extra unit>-deviation-2.md`, hand-off design-to-spec, follow-through "new unit <its id>". Approver: owner, citing ER:232, ER:320 and P0.8's row 1, the decision row P0.1 row 6 requires | Row: the opening landing. Unit: minted on dTrueNorth's roster in the opening (P0.5). Record: dTrueNorth's whole run, in the extra unit's spec commit |
| Each later departure a run makes under the owner's rulings: a unit a spec run adds (ER:315-316), a choice under the standing ruling (ER:240, :388), a relaxed bound (ER:328), or a deviation key's chain value set by the build that adds the key (ER:396) | The clause or spec it departs from | The rulings themselves, landed as P0.8's rows 1, 3 and 5 | A deviation record in the departing build's `build/`, approver the run's author role citing the ruling, under `author-recorded`; never `owner` (P0.1, row 6) | In the departing unit's own commit, in the run that makes it |
| dPlacedRequest's spec carries "a live claim on another node survives the migration", with a drain as the fallback | `cl-dClosedLoop-0120@5d655f07` | "Test in its spec (Recommended)" (ER:264) | A deviation record in `memory/builds/dPlacedRequest/build/`, risk stricter, approver owner citing P0.8's row 6, the decision row that records ER:264 | dPlacedRequest's spec run, in the migrating unit's spec commit |

**Not owner-approved: dWellOiledMachine's in-flight test.** Its spec carries "a `/unattended` run in flight at this
landing lands after it", a stricter departure from `cl-dClosedLoop-0306@a3aa83b5` that no answer of the owner's
covers. Its spec run records it in `memory/builds/dWellOiledMachine/build/`, in that unit's spec commit, with the
run's author role as approver under `author-recorded`, citing P0.8 row 6 as the ruling it serves (ER:248). A stricter
departure needs no owner turn under the chain's approval value (ER:103-104).

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
| Done | The plan took two independent Tier-2 reviews, compared and folded: "Review twice, then approve (Recommended)" (ER:343) | `build/…-execution-plan-reviews-compared.md` |
| Done | The fold took one more paired review over its own commit, compared and folded: "Review the fold, then approve (Recommended)" (ER:404) | `build/…-execution-fold-reviews-compared.md` |
| Done | Walked the plan section by section, and chose four changes, folded here without a further review (ER:413-542) | [defaults] |
| Now | Start phase 0 in a new session, from the fully oriented handoff this session writes: "Fold, then give me a fully oriented hand off to start phase 0 in a new session." (ER:533). Four items stay carried as recommended (R6, D3, D5, D8); the one question the fold raised is closed ([defaults]) | [phase-0] |
| Phase 0's end | Read in full the nine decision rows, the grant row among them, and dTrueNorth's README and packet; for the other 21 builds, read `open.py --check`'s output and `open.py --summary`'s rows, families included; then ask for the landing: "Rows + dTrueNorth (Recommended)" (ER:446) | P0.5; P0.7 |
| Each moment the script names | Type the run, `/unattended <slug>`, on the named node, in a fresh worktree: 43 runs (ER:270) | [schedule]; PROTOCOL:21-27 |
| dTrueNorth's landing | Read its departures report, which is also the first look at its coverage, since it ran whole | [phase-1] |
| Each spec landing | Read the build's coverage report and departures report before typing its build run, and check the landing diff for any path under `memory/builds/dClosedLoop/build/*.py` and any changed pin line in a `*-packet.md`. A "no" to a listed departure takes P0.6 rule 5: a decision row recording it, then an ask in that build's `BACKLOG.md`, which its build run must dispose of | [phase-2]; P0.6 |
| Each build landing | Read the departures report, the `widens:`, `relaxes:` and `grants:` choices first, and check the landing diff for any instrument path and any changed pin line in a `*-packet.md`. Nothing waits on the owner's reading (ER:240, :328, :388). A "no" takes P0.6 rule 5; since that build's build run has landed, its ask goes in dClosedLoop's `BACKLOG.md`, and every packet carries it in field 9 (P0.3) | [deviations]; P0.6 |
| At dTrueNorth's, dOrderedCharter's, dDeclaredLoop's, dIndexedDesign's and dScopedBuild's landings | Ask for the report-switch step's landing: dClosedLoop's edit of `deviations.py --report` and `packet.py --repin deviations.py`, landed together and alone, recorded as a decision row | [phase-1], the retirement table |
| At the barrier and the driver landings | Watch dPlacedRequest's test, or call the drain if it could not be written (ER:264); a driver build whose new code refuses its own landing hands it to the owner to land (ER:248) | [sync-points] |
| At dDeclaredLoop's and dScopedBuild's landings | Nothing to set: each build sets its key's chain value in its own landing, carried by its spec under P0.8 row 3: "The adding build (Recommended)" (ER:396). The value shows in that build's departures report | [sync-points]; P0.8 |
| After dConvergedCharter | Set the two deviation keys (D5) | [defaults] |

## [cannot]

Every limit the five returns name, merged where two name the same one. Each is either designed around, with the
section that does it, or listed with its smallest change and that change's kind.

| Limit | Named by | Disposition |
|---|---|---|
| No spec audit unless the owner opts in | driver 1 | Designed around: `spec-audit:` in all 22 landed READMEs (answer 2, P0.5) |
| Governance-carrier and public-surface forks park; `may:` was never exercised | driver 2 | Designed around: one grant decision row every `may:` cites (ER:181); proven in phase 1 |
| "Governance carrier" is defined nowhere | driver 2 | Designed around: a policy, P0.8 row 9, lists the carriers as `open.py --carriers` derives them from the tree at the opening, and the grant reads against that list (ER:525) |
| No parallelism inside a build; no sharing one build across nodes | driver 3, coordination | Designed around: split phases across builds. Lifting it is a chain build's unit: dPlacedRequest's unit leases (`cl-dClosedLoop-0120`) |
| Builds that rewrite their own driver | driver 4 | Designed around: they land through their own new code, the owner landing only if it refuses (ER:248), and the [sync-points] rows |
| A cross-node take-over needs the branch on the remote; no rule says when a branch is pushed | driver 5, coordination, handoffs 6 | Designed around: a policy, push after every pass commit, hold and hand-off (P0.8) |
| The resume tick is not registered on node d | driver 6 | Designed around: a manual step on each node (P0.9) |
| Every chain build pays the bar, and there is no landing queue | driver 7 | Designed around: contention measured at most two interlopers against three retries. A real queue is a chain build's unit (GR:113) |
| Nothing orders builds by their parents; preflight does not refuse a child whose parent has not landed | driver 8, coordination, schedule 2 | Designed around: a manual step, the schedule script at every landing (P0.4). A dependency gate is a dPlacedRequest unit, and the ordering's product is dRankedPlan's (`cl-dClosedLoop-0369`) |
| No Definition-of-Done item compares a spec to the design | driver 9, deviation 1 | Designed around: the instruments by hand, then dTrueNorth's product join (phase 1) |
| No path exclusion between builds | coordination | **Cannot.** A dPlacedRequest unit; until then, pushed branches, the prepare reconcile, README rule 7, and the departures report's block of paths written outside the run's own build folder as the interim check (P0.2) |
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
| A residual fork still parks: veto 3, veto 2 outside the grant, the goal, or no option left | this plan | Designed around: policies, the owner's standing ruling for veto 3 and the goal bound (ER:240) and for veto 2 outside the grant (ER:388), and relaxing the weakest bound for a fork with no option left (ER:328), each recorded as a departure and marked, until dOrderedCharter's `cl-dClosedLoop-0032` |
| The departures report has no Definition-of-Done item that runs it | this plan (`unattended.sh:12225-12226`) | **Cannot.** A manual step in the README's rules, its close sequence. Nothing checks the report's base against the final prepared merge either. The product is the landing record (`cl-dClosedLoop-0413`) and the deviation gate (`cl-dClosedLoop-0412`) |
| No merge-bar check outside `memory/` compares each instrument's blob with its blob at the opening landing commit | the review (`instrument-pin-rerendered`) | **Cannot** in phase 0, which writes no product code. A manual step until a chain unit adds the check: the owner checks every landing diff for a path under `memory/builds/dClosedLoop/build/*.py` and every changed pin line in a `*-packet.md`, and a packet red on a moved blob is a stop ([handoffs]) |
| A run edits its own packet's pin line, or `packet.py`, to move a pin | the fold review (`pin-overclaim`) | **Cannot**: `--check`'s pin arm compares the pin the packet carries, so a hand-edited pin matching the moved blob reads green. Phase 0 tries it once and records the result here, expected green; it is never planted as a red. A manual step until a chain unit's merge-bar check: the owner's landing-diff check of every changed pin line |
| A run's own commit to another build's paths is refused by no gate; `--close`'s cross-build refusal grades only commits carried through local main | the review (`close-cross-build-unrefused`; `unattended.sh:10540`) | Designed around: README rule 7, the departures report's outside-paths block, and the closing review. A gate is the path-exclusion row's dPlacedRequest unit |
| The owned nodes carry no paths for a grant | this plan | Designed around: one decision row (ER:181) |

## [defaults]

### Decided by the owner

Each quotes the owner's answer in ER `[answers-2]`, `[answers-3]` or `[answers-4]`; the options offered are recorded
there.

- **R1, the grant.** "One decision row (Recommended)" (ER:181). One row grants each chain build the
  governance-carrier and public-surface changes its own `[chain]` clauses name, and all 22 `may:` lines cite it
  (P0.5, P0.8). In the walk the owner held the rows as quoted: "Hold, on to Phase 1 (Recommended)" (ER:461).
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
- **D7, residual forks.** "Standing ruling" (ER:240). Where every surviving option passes veto 1 and fails only
  veto 3 or the goal bound, the run takes the most capable of them, "the most capable option that fails only the
  security veto or the goal bound" (ER:237-238), and records it as a departure. A choice that widens a surface
  carries `widens:` and the report lists it first (ER:284-285); a goal-bound-only choice carries `widens: none` and is
  listed with the other forks. An option that also fails veto 1 goes to rung 6 first.
- **Veto 2 outside the grant.** "Standing ruling takes it (Recommended)" (ER:388). Rung 5 takes the most capable
  option whose only failure is veto 2 outside the grant, records it as a departure marked `widens: <change>`, and the
  report lists it first (ER:383-384). A choice that lifts veto 2 through the grant is marked `grants: <decision id>
  <change>` and listed first too.
- **The deviation keys' chain values.** "The adding build (Recommended)" (ER:396). dDeclaredLoop sets
  `deviation.approval = author-recorded` and dScopedBuild sets `deviation.gate = report`, each in its own landing,
  carried by its spec under P0.8 row 3 and recorded as a departure; nothing waits on the owner.
- **D9, a discovery a spec run adopts.** "Carry it too (Recommended)" (ER:320). The extra unit admits any unit a
  spec run adds, from a review or a discovery, carried to its own build run once; the build run must build it and
  never defer it again. The spec run specs and audits it and records it as a departure (ER:314-316). The plan's
  file-an-ask route is dropped.
- **D10, a fork with no option left.** "Relax the weakest bound" (ER:328). The run drops the least important failing
  criterion or non-goal, judged by the tiers in [phase-2], rung 6, records it as a departure and builds. The choice
  is listed first in its build's departures report, beside the surface-widening choices (ER:347-348). P0.2's
  validating arm, separate from its byte compare, checks that ordering and reds on its planted cases.
- **The two records' placement and wording.** "Yes, as planned (Recommended)" (ER:336): approval in decision rows at
  the opening, each record written in the unit's own spec commit, naming the owner as approver and citing the
  decision row that records the answer, as P0.1 row 6 requires ([deviations]).
- **Before phase 0.** "Review twice, then approve (Recommended)" (ER:343): two independent Tier-2 reviews of this
  plan, compared and folded. Then "Review the fold, then approve (Recommended)" (ER:404): one more paired review over
  the fold's commit, compared and folded. The owner then chose to walk the plan before approving it: "Walk it first"
  (ER:424).
- **Node b.** "Spec runs only" (ER:219), the script's rule.
- **The unit family.** "Family by stream" (ER:438), over the recommended "TOOL for all": each build's family follows
  its main stream, PLAY for charter and playbook builds, KICK for session and kickoff, DEPL for deploy, TOOL otherwise.
  P0.5 derives it from each build's Stage and slug noun; P0.8 row 8 records it. Two PLAY, one KICK, one DEPL and
  eighteen TOOL builds.
- **The opening read.** "Rows + dTrueNorth (Recommended)" (ER:446): the decision rows, the grant row, and dTrueNorth's
  README and packet in full; for the other 21, `open.py --check`'s output and the per-build summary P0.5 defines
  (P0.7).
- **The self-test suites in driver builds.** "Waive in each README" (ER:476), over the recommended "Run at those
  closes": each of the seven driver-changing builds P0.5 derives waives the unattended kit's own on-demand suites for
  its landing in its README, in dAlignedCarrier's form, and proves its driver changes by targeted probes and its own
  planted tests (README rule 8; P0.8 row 6). The walk's correction sets the scope (ER:544-557): the suites are on no
  leg of the bar, so the waiver covers the `--selftests` verdict the kit's Definition of Done owes a landing, and every
  close touching `tools/` still exports `GATE_FULL=1 GATE_SELFTESTS=1`.
- **The governance carrier.** "Define it in Phase 0 (Recommended)" (ER:525): P0.8 row 9 lists the carriers,
  derived from the tree at the opening, and the grant reads against it.
- **After the walk.** "Fold, then give me a fully oriented hand off to start phase 0 in a new session." (ER:533). The
  walk's four changes are folded without a further review, and phase 0 starts in a new session from that handoff.

### Closed after the walk

- **Self-tests at the close of a build that is not driver-changing.** The writer asked whether every build touching
  `tools/` should waive the self-tests too. The question has no subject: `GATE_SELFTESTS=1` runs the bar's held kit
  legs, and no leg runs the unattended kit's suites (`memory/guides/MERGE-BAR.md:39-41`;
  `tools/unattended/run-unattended-gates.sh:2`). A build touching `tools/` without changing the driver owes the
  flagged bar and no unattended suite, so it needs no waiver (the walk's correction, ER:544-557).

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
| "Records-only landings are cheap" (schedule) | Partly: an in-place close runs the bar under `GATE_FULL=1` whatever the diff (PROTOCOL:428-432). A spec run, whose range touches no `tools/` path, is spared only the held kit legs `GATE_SELFTESTS=1` adds (`.unattended.conf:40`) |
| `BUILD-METHOD` "MUST run concurrently" against a strictly sequential harness (driver) | The code (`unattended-build.js:76-80`) |
| "Claims never age" (GR:323, theme T5) against the code (coordination) | The code: a `live` claim turns `stale` at 5400 s, and only `held` never ages (`unattended.sh:2177-2186`) |
| Several returns: forks the run cannot settle are parked BLOCKED | The owner's rulings: the run settles them itself, by the standing ruling (ER:240), which also takes veto 2 outside the grant (ER:388), or by relaxing the weakest bound (ER:328), and records each as a departure. Nothing parks |
| Both review runs' fixes for a fork whose only options trip veto 2 outside the grant: it parks (reviews-compared, `veto2-fork-unruled`) | The owner: "Standing ruling takes it (Recommended)" (ER:388). Rung 5 takes it |
| The plan's own D6, an `--override build-complete` under a ruling, against the owner's view that the refusal is a bug for review-promoted units (ER:196-197) | The owner: the condition is fixed in product, by dTrueNorth's extra unit (ER:232). The override is dropped |
| The plan's D9, a spec run filing a discovery as an ask, and its D10, carrying a no-option unit forward | The owner chose otherwise: "Carry it too (Recommended)" (ER:320) and "Relax the weakest bound" (ER:328). Both of the plan's routes are dropped |
