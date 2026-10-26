# TOOL-dWellOiledMachine-47 — every wait the supervisor holds given its deadline and outcome: the hold ceiling's hand-over, the act ceiling, nested spawns, restarts and `invalid-input`

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 46 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0325@54802c5c whole
**Carries:** node:policy-key.runtime.act-ceiling
**Carries:** node:policy-key.runtime.hold-ceiling
**Carries:** node:policy-key.runtime.restarts

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |

<!-- /gen:spec-records -->

## 1. Goal

Today a run held on a session limit keeps its lease and its wake for as long as the limit lasts: one
weekly-limit stall woke a session 115 times over 4.8 days (layer-runtime.md:401-411, gap-rt-38), and
no supervisor wait has a ceiling, a crash loop restarts without end, and a malformed input only
journals. This unit gives every wait the supervisor holds its deadline and outcome: the session-limit
hold releases every lease the supervisor holds for the build, the build's and each in-flight unit's,
as a hand-over at `runtime.hold-ceiling` and raises an owner item, so a node with quota takes them
over and the wake stops; an admission wait past `runtime.act-ceiling` writes a stall record naming
the holders, and a slot held past it is reclaimed only from an act session the supervisor launched;
every nested spawn draws from its parent's reservation and never queues again; restarts beyond
`runtime.restarts` in an hour stop the supervisor with an owner item; and `invalid-input` raises an
owner item at once (P39, the parked debt's review).

## 2. Scope (IN)

- **S1** — The limit hold as a declared wait. When the supervisor enters TOOL-dWellOiledMachine-6
  S9's limit hold, `tools/runtime/supervise.py` declares `declare_wait("limit-hold", <act>, <slug>,
  on="-", seconds=runtime.hold-ceiling × 3600, outcome="hand-over")` (TOOL-dWellOiledMachine-18 S2),
  the ceiling read through `resolve` (`tools/policy/policy.py:752`); at the limit's reset it runs
  `waits.py close limit-hold <act> <slug>` and launches again. The kind `limit-hold` joins
  `WAIT_KINDS`, and the outcome `hand-over` joins `WAIT_OUTCOMES` marked `holder-only`. Observed by
  AC1, AC4.
- **S2** — The hand-over, `hand_over(slug, act)` in `supervise.py`, the outcome the sweep runs past
  the ceiling on the holding node: for the build lease and every unit lease of the build whose
  `fleet-tag` is this node's, read through `unattended.sh --claims`, `--lease release build <slug>` or
  `--lease release unit <slug> <id>` with no `--as`, the hand-over status `released`
  (TOOL-dPlacedRequest-16 S1); then `raise_owner_item("hold-ceiling", <slug>, ["resume",
  "withdraw"], "resume", key=<act>)` (TOOL-dWellOiledMachine-48 S1); then the `stall` journal line
  with `act=<act>` and `reason=hold-ceiling` through `write_journal_line`
  (TOOL-dWellOiledMachine-16 S3). It prints `hand-over — <slug> · <n> lease(s) released · owner item
  <id>`. The supervisor's own fence read then finds its lease gone and exits
  (TOOL-dWellOiledMachine-6 S7). Observed by AC1, AC2, AC3, AC4.
- **S3** — The wake stops. `verb_resume` (`tools/unattended/unattended.sh:9149`), reached by a resume
  schedule still firing, reads the build lease first: one this node released by a hand-over, its
  newest `released` record carrying this node's fleet tag, prints `resume — <slug> · handed over at
  runtime.hold-ceiling: nothing to resume on this node` and exits 0 having launched, held and
  scheduled nothing, so no wake re-arms another. TOOL-dWellOiledMachine-6 S2 starts no supervisor on
  a `released` lease. Observed by AC1.
- **S4** — The act ceiling, `reap_past_ceiling(slug)` in `supervise.py`, run at each beat: an act
  session the supervisor launched, its pid a row of the slug's process ledger
  (`write_proc_record`, `unattended.sh:1734`), alive longer than `runtime.act-ceiling` hours since its
  `act-launch` line is killed through `reap.py --kill <pid>` (`tools/process-monitor/reap.py:420-470`)
  and journaled `act-killed` with `reason=act-ceiling`; its slots then leave through the release at
  its exit (TOOL-dWellOiledMachine-9). A session with no ledger row, an attended session's, is never
  killed here, and its slots go only by TOOL-dWellOiledMachine-43's liveness sweep. Observed by AC5,
  AC6.
- **S5** — The admission wait's ceiling: at each beat, each ticket `python admission.py status`
  (TOOL-dWellOiledMachine-45 S6) lists as waiting longer than `runtime.act-ceiling` on this node's
  clock, with no slot released for its key in that time, gets one `stall` journal line keyed by its
  act or session, with `waited=<seconds>` and `holders=<act>+<act>`, the acts holding the key's
  slots, and one printed `admission — stalled · waited <s> · holders <acts>`; a second beat writes no
  second line for that ticket. Observed by AC10.
- **S6** — Nested spawns. `admit(call, reservation, wait_s=None)` (TOOL-dWellOiledMachine-45 S1)
  gains its first branch: a call whose environment carries `GOV_ACT=<act>` (TOOL-dWellOiledMachine-6
  S4), made inside an act session, takes no ticket and charges one slot of that act's reservation in
  `tools/runtime/slots.py`, admitted at once; a call past the act's reservation is refused naming the
  act and its declared fan, a declaration error and never a wait. So a nested spawn never queues
  behind the room its own parent holds. Observed by AC7.
- **S7** — Restarts. TOOL-dWellOiledMachine-6 S2's `run_supervisors` appends each start's epoch to
  `<git-common-dir>/gov/supervisors/<slug>.starts` and, before a start, counts the epochs within the
  last 3600 seconds on this node's clock: at more than `runtime.restarts`, read through
  `policy-shim.sh get runtime.restarts`, it starts nothing, prints `supervisor — <slug> · stopped:
  <n> restart(s) in an hour` and raises `raise_owner_item("restarts", <slug>, ["restart", "withdraw"],
  "restart", key=<slug>@<hour>)` once for that hour. Observed by AC8.
- **S8** — `invalid-input`: when `derive_position` answers `invalid-input` (TOOL-dDeclaredLoop-7 S5),
  the supervisor launches nothing and raises `raise_owner_item("invalid-input", <slug>, ["fix-input"],
  "fix-input", key=<the path the answer names>)` at once, printing the path. The kinds `hold-ceiling`,
  `restarts` and `invalid-input` join `OWNER_ITEM_KINDS`. Observed by AC9.
- **S9** — `help/runtime.md` gains a section on the supervisor's waits: the three keys, the hand-over,
  the act ceiling's reach, the nested rule and the stall line. Observed by AC11.
- **S10** — The fixture, `tools/runtime/limits_fixture.py --case <name>`: a bare remote and two clones
  under `%TEMP%` with short names on fleet tags `a` and `b`, a stub `claude` that writes a StopFailure
  limit line into `<git-dir>/unattended/stall.<slug>.log` in `stall-recorder.js`'s shape
  (`tools/unattended/stall-recorder.js:78`) or sleeps, the three keys planted small per case, and the
  slot ledger at a planted limit. It prints the verbs' last lines, the leases' states, the journal's
  `stall` and `act-killed` lines and the owner items posted. Observed by AC1 to AC10.

## 3. Non-goals (OUT)

- No lease renewal during the hold: TOOL-dWellOiledMachine-46 renews a lease on a declared wait inside
  its deadline, this hold among them.
- No relaunch counting and no routing after a reap: TOOL-dWellOiledMachine-46 counts the reaps S4
  journals and routes an instance reaped twice.
- No slot claim, release or liveness sweep: TOOL-dWellOiledMachine-9 and -43's.
- No limit parsing: TOOL-dWellOiledMachine-6 S9 reads the reset time; this unit bounds the hold.
- No deletion of a resume schedule registered in a harness: S3 makes its firing inert, and
  TOOL-dWellOiledMachine-28 dissolves `RESUME_SCHEDULE_*`.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-6` — `supervise.py`, whose limit hold this unit bounds, whose beat gains the act ceiling and the stall line, and whose restarts it caps
- **consumes-from** `TOOL-dWellOiledMachine-16` — `write_journal_line`, with the `deadline-passed` and `stall` classes; the `stall` class S2 and S5 write
- **consumes-from** `TOOL-dWellOiledMachine-45` — `admit`, whose held calls S5 gives a ceiling and which S6 gives the nested branch
- **consumes-from** `TOOL-dWellOiledMachine-9` — `slots.py`, the act's reservation S6 charges a nested spawn against
- **consumes-from** `TOOL-dWellOiledMachine-18` — `wait —`, the declared wait the limit hold is, with the `hand-over` outcome this unit adds
- **consumes-from** `TOOL-dWellOiledMachine-48` — `raise_owner_item`, raised at the hold ceiling, past the restarts cap and at `invalid-input`
- **hands-off** `TOOL-dWellOiledMachine-46` — `runtime.act-ceiling`, the reaps S4 journals, which that unit counts per instance
- **consumes-from** external — TOOL-dPlacedRequest-1's `--claims` and `--lease`, -16's hand-over, and TOOL-dDeclaredLoop-7's `invalid-input` answer

## 4. Design

### Evidence

- The hold has no ceiling: `run_hold` (`tools/unattended/unattended.sh:6848`) files the slug under
  `resume_schedule_name` (:1191), and `HOLD_CODES_CORE` (:1029) names `platform-limit` with no bound.
- The resume tick skips a HELD run (`tools/unattended/resume-tick.sh`, `run_tick`, the `HELD` case
  after :295), so the wakes come from the durable schedule `--hold` printed, which only a session can
  reap; an inert `--resume` is the one place every such wake passes.
- The three keys are rows: `runtime.act-ceiling` (`tools/policy/catalogue.toml:437`, 1.5 hours),
  `runtime.hold-ceiling` (:444, 6 hours) and `runtime.restarts` (:465, 3), each `raise-loosens`.
- A limit signal exists: `stall-recorder.js` writes a StopFailure line to the slug's stall sidecar
  (`tools/unattended/stall-recorder.js:55`, `:78`), which TOOL-dWellOiledMachine-6 S9 reads.

### The waits and their outcomes

| Wait | Deadline | Outcome | Where |
|---|---|---|---|
| the session-limit hold | `runtime.hold-ceiling` | hand-over of every lease held for the build, owner item | S1, S2 |
| an admission ticket | `runtime.act-ceiling` | one stall line naming the holders | S5 |
| a slot held by a launched act | `runtime.act-ceiling` | the act's tree killed, its slots released | S4 |
| a slot held by an attended session | its session's liveness | TOOL-dWellOiledMachine-43's sweep | none here |
| a supervisor restart | `runtime.restarts` an hour | stopped, owner item | S7 |
| `invalid-input` | none: at once | owner item | S8 |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `hand_over` | function | `hand`, none |
| `reap_past_ceiling` | function | `reap`, OK |
| `limit-hold` | wait kind | none |
| `hand-over` | wait outcome, holder-only | none |
| `hold-ceiling`, `restarts`, `invalid-input` | owner-item kinds | none |
| `<slug>.starts` | node-local start list | none |
| `limits_fixture.py` | fixture script | none |

### Files touched (estimate)

- `tools/runtime/supervise.py`: S1, S2, S4, S5 and S8
- `tools/runtime/admission.py`: S6's nested branch in `admit`
- `tools/runtime/waits.py`: the `limit-hold` kind and the `hand-over` outcome
- `tools/runtime/owner_items.py`: the three kinds
- `tools/unattended/resume-tick.sh`: S7's count in `run_supervisors`
- `tools/unattended/unattended.sh`: S3's read in `verb_resume`
- `tools/runtime/limits_fixture.py`: the fixture
- `help/runtime.md`: the section

### Alternatives rejected

- **The supervisor judging its own hold ceiling in process.** A supervisor killed during a weekly hold
  would restart its count, and no other node could tell the hold existed; the declared wait sits on a
  ref every node reads.
- **Refusing a nested spawn past the free room.** A child would then wait on room its own parent
  holds, the deadlock six acts with fans of two meet at saturation.

## 5. Production-readiness checklist

- security — the hand-over writes only leases this node holds, through the record door; the act
  ceiling kills only process trees the supervisor's ledger names.
- perf / scale — one ledger read and one `status` read per beat; the hand-over is one write per lease.
- error / empty / loading states — a lost lease write prints `lease not written` and the hand-over is
  retried at the next sweep, the wait staying `raised` once its outcome has run.
- observability — the `stall` and `act-killed` lines, the `hand-over —` line and the owner items.
- risks — a long-running act legitimately past 1.5 hours is killed; the key is the owner's to raise.
- testing — the fixture cases under AC1 to AC10 and the arm in §7.
- migration — none: holds in flight keep their schedules, which S3 makes inert once their build is
  handed over.
- user docs — `help/runtime.md`.

## 6. Acceptance criteria

Each case runs `python limits_fixture.py --case <name>` in its scratch clones.

- **AC1** — When `--case wake-loop` holds `fx` on a weekly limit with `runtime.hold-ceiling` planted
  at `0.0003`, sweeps past it, then replays 115 firings of `unattended.sh --resume fx` and the node
  tick on clone `a`, the build lease reads `released`, every firing prints `handed over`, and no
  `act-launch` line and no new hold is written.
  Red when: the 115-wake limit loop replayed leaves the lease still held, or the tick fires a launch
  again past the ceiling.
- **AC2** — When `--case mid-unit` plants the limit while clone `a` holds `fx`'s unit lease for
  `TOOL-fx-1`, the hand-over writes that unit lease `released` too, and `--lease acquire unit fx
  TOOL-fx-1` on clone `b` succeeds within one tick.
  Red when: a limit planted mid-unit leaves its unit lease still held.
- **AC3** — When `--case take-over` runs the hand-over and then `--lease acquire build fx` on clone
  `b`, clone `b` holds the lease at the next epoch.
  Red when: the hand-over leaves a lease no second node can take.
- **AC4** — When `--case ceiling-item` passes the ceiling, exactly one `owner item hold-ceiling fx
  <act>` is posted, and a second sweep posts none.
  Red when: a ceiling is passed with no owner item raised, or with two.
- **AC5** — When `--case leaked-slot` plants a launched act session that sleeps past
  `runtime.act-ceiling` planted at `0.0003` while holding two slots, one beat kills it, journals
  `act-killed` with `reason=act-ceiling`, and the slot ledger then counts 0 for it.
  Red when: the planted leaked act slot is still held after the beat.
- **AC6** — When `--case attended-workflow` plants an attended session's Workflow holding three slots
  past the act ceiling with no process-ledger row, the beat leaves its slots counted and its process
  alive.
  Red when: an attended Workflow past the act ceiling loses its slots.
- **AC7** — When `--case nested-fan` runs six acts under a limit of six, each with a declared fan of
  two and each spawning two nested agents, all twelve nested spawns are admitted with no ticket and
  every act exits 0; a seventh nested spawn in one act is refused naming its fan.
  Red when: a nested spawn queues, as an `admit` without its nested branch shows by deadlocking.
- **AC8** — When `--case crash-loop` kills the supervisor four times within one planted hour under
  `runtime.restarts` 3, the fourth restart prints `stopped: 4 restart(s) in an hour`, starts nothing
  and posts one `owner item restarts fx` item.
  Red when: the planted crash loop restarts a fourth time, or stops with no owner item.
- **AC9** — When `--case invalid-input` plants a README whose status header does not parse, the beat
  posts one `owner item invalid-input fx <path>` item at once and launches nothing.
  Red when: the `invalid-input` only journals.
- **AC10** — When `--case admission-stall` leaves a ticket waiting past `runtime.act-ceiling` behind
  two holding acts, one `stall` line names `holders=<act>+<act>` and a second beat writes none.
  Red when: the wait past the ceiling writes no stall record, or one per beat.
- **AC11** — When `grep -n "runtime.hold-ceiling" runtime.md` runs over the help page, it names the
  section, and the page names `runtime.act-ceiling`, `runtime.restarts` and `invalid-input`.
  Red when: any of the four is absent.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

The broad guard `{prefix}/` leaves the line by the checker's floor. The unattended kit's self-test
suites are waived for this build's landing (README rule 8).

New arm: tools/runtime/limits_fixture.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 · each planted case staged against a supervisor with its hand-over, ceiling reap and restart count removed and an `admit` with no nested branch · none

## 8. Open questions

- **F1 — Who judges the hold ceiling?** (a) TOOL-dWellOiledMachine-18's sweep over a declared wait,
  its outcome holder-only; (b) the supervisor in process. (b) loses the count at a restart and is
  invisible to other nodes, and the layer calls the hold "a declared wait inside its deadline"
  (layer-runtime.md:401-404). Rung 1. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none ·
  relaxes: none
- **F2 — How does the wake stop when a harness schedule cannot be reaped from the shell?** (a)
  `verb_resume` made inert for a build this node handed over; (b) a session-side reap of the schedule
  by name. (b) needs a session to run, which is what a stopped wake no longer has. Rung 3. RESOLVED
  (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F3 — What does a nested spawn past its parent's reservation get?** (a) Refused naming the
  declared fan; (b) queued. (b) is the deadlock the clause's red case plants, and an act spawning
  past its declared fan has broken its declaration. Rung 1: "never queueing again" (v2:1777, the
  clause). RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.

## 10. Reuse audit

The seams extended are the supervisor (TOOL-dWellOiledMachine-6's `supervise.py` and
`run_supervisors`), the admission call (TOOL-dWellOiledMachine-45's `admit`) and the slot ledger
(TOOL-dWellOiledMachine-9's `slots.py`), the declared wait and its sweep (TOOL-dWellOiledMachine-18),
the owner item (TOOL-dWellOiledMachine-48), the lease hand-over (TOOL-dPlacedRequest-16 S1), the
process ledger's `write_proc_record` (`tools/unattended/unattended.sh:1734`), `reap.py --kill`
(`tools/process-monitor/reap.py:420-470`) and `verb_resume` (`unattended.sh:9149`). The probe `python
tools/codebase-map/reuse_lookup.py "hold a run on a session limit and release its lease after a
ceiling"` ranked `run`, `run_git` and `resolveLease` by stem; `resolveLease`
(`tools/unattended/run-lease.js`) resolves a session's run lease for its sidecars and releases nothing,
so no existing seam fits the hand-over. Scout A's row cites `run_hold` at `:6848`, `HOLD_CODES_CORE` at
`:1029` and `reap.py:345 run_sweep`, each holding at this base.

Recall terms used: `python tools/memory-recall/query.py "what bounds a session-limit hold and a crash
loop in the supervisor" --terms "hold ceiling act ceiling restarts hand-over lease release stall
holders nested spawn reservation invalid-input wake"`
