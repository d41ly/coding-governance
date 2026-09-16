# TOOL-dDerivedDocket-4 — HELD phase, lease and derived phase

**Status:** SPECCED · rev-4 · 2026-09-16 · node d · Tier-2 · base abac6d59 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md) | spec-audit | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round2.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round2.md) | spec-audit | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |

<!-- /gen:spec-records -->

## 1. Goal

An unattended run that meets a stop it cannot fix — a usage limit, an overloaded API, a degraded
host, an inherited red it may not absorb — has two endings today, ABORTED or a prose handoff, and
both end the run. Add a non-terminal HELD phase that a run enters by a verb, with a code, a release
condition and a generated checkpoint, and that it leaves by `--resume` with no owner answer. Add a
per-slug lease so two sessions cannot drive one slug, and route every phase read through
`derived_phase()`, or `recorded_phase()` where a call site's table row says so, so they cannot
disagree. Built in the first group by owner ruling D12-i11. The same derivation surfaces the
non-terminal records that dead sessions abandoned, which TOOL-aReapedTicket-5 records and the design
lists among this unit's closes.

## 2. Scope (IN)

- **S1** HELD joins `PHASES_CORE` as a non-terminal phase, placed after LANDING. `CORE_FLOOR` in
  gov's `.unattended.conf` and in the kit's conf example moves from `12:12` to `13:12`; the DoD
  half moves later with the asks-disposed unit. Observed by AC9.
- **S2** A verb
  `--hold <slug> --code <c> --until <cond> --reason <text> (--reaped <id> | --keepalive-unreachable <node>)`,
  with a closed code set plus `HOLD_CODES_EXTRA`, and a closed condition grammar. A required,
  shrink-only `HOLD_FLOOR`, declared in gov's conf as the core count and in the kit's conf example,
  is validated by the leg against the driver's `HOLD_CODES_CORE`, as `HALT_FLOOR` is for the halt
  codes.
  `tools/unattended/kit.toml` gains a `hold-floor` hole shaped like `directives-floor`, with its
  discharge probe. Observed by AC1, AC2, AC9, AC11 and AC16.
- **S3** `--hold` refuses, numbered and before any write, unless: the record is live and not HELD;
  the tree is clean and committed; the branch tip is on its remote when `ANCHOR_SCOPE=published`;
  and the keepalive the lease and the `keepalive` fact currently name is either reaped, named by
  `--reaped <id>`, or recorded unreachable by `--keepalive-unreachable <node>`. One exception to the
  published-tip clause: under `--code platform-unavailable`, when the remote does not answer at
  all, `--hold` accepts the unpublished tip and records it as `hold-unpushed: <HEAD sha>`. A remote
  that answers still requires the push, and no other code is excepted. Observed by AC2, AC14 and
  AC15.
- **S4** The checkpoint is DERIVED by `--status` from the hold facts on every read, never stored as
  a second copy. Every gate claim in it is a pointer to a run record. Observed by AC3 and AC15.
- **S5** `--resume` on a HELD record performs, in order:
  1. the condition test;
  2. refusing a missing `--keepalive-id`;
  3. re-verifying authorization at the pinned BASE;
  4. naming interrupted acts;
  5. taking the lease, naming that id;
  6. reaping the run's own orphans, a seam the process-ledger unit fills;
  7. recording the id in the `keepalive` fact;
  8. returning to the held-from phase.

  Every refusal comes before the lease is taken, so a refused resume writes nothing. An unmet
  condition prints `still held` and writes nothing. A missing id prints the `--status` block, then
  refuses, numbered, naming `--keepalive-id`. A stale or leaseless working-phase take-over runs the
  same steps without the condition test. Observed by AC1, AC4, AC6, AC18 and AC21.
- **S6** A lease at `<git-common-dir>/unattended/<slug>.lease`, taken at `--preflight`, at a
  take-over, and by a leaseless working record's holder resuming with its recorded keepalive;
  refreshed by every writing verb past its own write gate; at the start of `run_bounded`, only when
  the lease reads `taken` naming the keepalive its calling verb acts for; and by a `--resume` passing
  the lease's own keepalive id, which is how the keepalive tick refreshes it; released by `--hold`;
  removed at a terminal; rewritten as `released <iso> landed` at an in-place `--landed`'s successful
  observation, with the matrix row that reads it, both of which the derived-terminal unit adds. A
  holder replaces its keepalive with `--resume --keepalive-id <new> --replaces <old>`, which is
  accepted only when `<old>` is the lease's id. Observed by AC6, AC7, AC10, AC17, AC20 and AC22.
- **S7** `presumed-stopped` is derived by `--status` when a working-phase lease is older than the
  bound. It is also derived when a working-phase record has no lease and the newest commit touching
  its build folder is older than the bound. `--resume` then takes the run over. It is announced,
  never a refusal. A leaseless record resumed with the id its `keepalive` fact records is its
  holder's, and takes the lease instead. Observed by AC7, AC19 and AC22.
- **S8** Two phase readers, `derived_phase` and `recorded_phase`. Every read of the `phase` fact
  outside the phase writers goes through one of them, as the call-site table in §4 classifies it.
  `refuse_if_terminal` takes a `--recorded` mode, and only `--landed` passes it, because that verb's
  own postcondition is a terminal. The arm's exemption is the `set_fact <file> phase` line, never the
  function containing it. Observed by AC8.
- **S9** HELD blocks `--close`, `--landed` and `--phase`; only `--resume` leaves it, and only
  `--landed` and `--abort` still write a terminal. HELD is PRODUCER-ONLY: `--phase` refuses it as a
  target, numbered and beside its LANDING refusal, because only `--hold` writes the hold facts.
  `--preflight` over a HELD record refuses, numbered, naming `--resume`. Over a working phase it
  stays the idempotent re-preflight the protocol sanctions after a compaction, and keeps the
  recorded keepalive: it refuses, numbered and naming `--resume`, when the `--keepalive-id` passed
  differs from the recorded one. Observed by AC5, AC10 and AC13.
- **S10** The contract text goes to a new companion guide, `UNATTENDED-STOPS.md`, rendered from the
  kit like the verb carrier; the protocol gains two rows, one in §3 and one in §7. The `unattended`
  dossier claims the new guide key. The Skill's Resume section carries §4's take-over rule, under
  which a take-over whose `--resume` refuses or prints `still held` reaps only the job it scheduled
  and reads the result back. Observed by AC11.
- **S11** A DECISIONS row supersedes `TOOL-aBoundedVerdict-2`'s "never a new phase" for a
  non-terminal, resumable phase, minted by the orchestrator under this build's slug at build time.
  NOT OBSERVED by a criterion: it is a record, and check 13 and the recall floor grade its shape.

## 3. Non-goals (OUT)

- Reaping the run's own processes before a hold, and the orphan count in `--status`. The
  process-ledger unit adds that clause to the `--hold` preconditions this unit names.
- The auto-resume scheduler. The auto-resume unit schedules `/unattended --resume <slug>`; this unit
  only makes that resume correct and refusable.
- Deriving LANDED from the advertised tip and rotating a derived-LANDED record at preflight. The
  derived-terminal unit adds that derivation inside `derived_phase()`.
- The bound stack that turns a kill before `acquired` into `host-degraded`, and the HOST exit.
  Those are the declared-wall and honest-verdicts units; this unit only accepts the codes.
- A pending review runId in the checkpoint. The review-durability unit records it and adds the line.
- Fixing `--status`'s next-unit order (TOOL-aBoundedVerdict-23). The checkpoint names whatever
  `--status` computes; the roster-derivation unit changes that computation.
- Any change to the halt-code vocabulary or to `--abort`.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-1` — the attributed criterion for the unattended suites
  this unit is allowed to run once at its end: `verdict clean`, with every inherited suite filed.
- **hands-off** `TOOL-dDerivedDocket-3` — `derived_phase()` and the HELD refusals, which the landing
  path's `--close` and Land steps rely on, plus the companion guide the landing text may overflow
  into, including `--hold`'s unpublished-tip exception for `platform-unavailable`.
- **hands-off** `TOOL-dDerivedDocket-5` — the lease, the hold facts and the resume contract that a
  scheduled resume invokes.
- **hands-off** `TOOL-dDerivedDocket-22` — `derived_phase()`, inside which the LANDED derivation from
  the advertised tip goes; the call-site table that derivation must respect; and the lease matrix,
  to which that unit adds the `released <iso> landed` row.
- **hands-off** `TOOL-dDerivedDocket-27` — the `host-degraded` code and the `probe gate` condition
  that a kill before `acquired` holds with, and the lease's stale-bound formula, whose first term
  that unit moves to the pinned backstop.
- **hands-off** `TOOL-dDerivedDocket-28` — the named precondition seam in `--hold` where the
  run-owned process reap goes, and the `--status` line the orphan count joins, and the reap step
  inside `--resume`, placed after the lease is held on the take-over and matching-id rows only.
- **hands-off** `TOOL-dDerivedDocket-29` — the checkpoint, which gains the pending review runId.
- **hands-off** `TOOL-dDerivedDocket-16` — `derived_phase()`, through which that unit's preflight
  labels a claiming build terminal or not, report-only.
- **hands-off** `TOOL-dDerivedDocket-24` — the `inherited-red` hold code and the resumable HELD
  stop the park policy ends in.

## 4. Design

### Data model

`--hold` writes these facts in the authored region of `RUN.md`, and one history row:

| Fact | Value |
|---|---|
| `phase` | `HELD` |
| `witness` | HEAD's sha, which the clean-and-committed precondition makes meaningful |
| `held-from` | the working phase the run was in |
| `hold-code` | one member of the effective code set |
| `hold-until` | the condition, verbatim after validation |
| `hold-reason` | free text, stored and printed as a quotation only |
| `held-at` | UTC, ISO-8601 with a trailing `Z` |
| `hold-unpushed` | HEAD's sha; written only when `platform-unavailable` was held while the remote did not answer, absent otherwise |

The history row is `<UTC> hold · code <c> · until <cond> · reaped <id>|unreachable <node>`. It is
history-class, so `--status` counts it as noted rather than owed.

### Codes and conditions

```
HOLD_CODES_CORE = host-degraded platform-limit platform-unavailable host-owner-action inherited-red
condition       = "after " <YYYY-MM-DDTHH:MM:SSZ> | "probe " ("host" | "gate" | "api") | "owner"
```

The hold codes are a SECOND vocabulary beside the halt codes, not an extension of them: a halt code
ends a run and a hold code pauses one, and one list would let a pause be recorded as an ending.

What a condition means at `--resume`:

- `after` is met when the clock has passed it. Unmet, the resume prints `still held` and writes
  nothing, not even the lease.
- `probe host|gate|api` is met on any resume. The resumed run's next act IS the probe; if it fails
  again, the run holds again. This is the only reading a driver can honour: it cannot observe the
  API it runs under, and a host-cost calibration belongs to the honest-verdicts unit.
- `owner` is met on any resume, and the auto-resume unit never schedules one for it. A hold whose
  release needs a human act on the machine is therefore released by whoever restarts it.

Design §21.7 ends a stop HELD only with the branch pushed. In a sustained outage the branch push
fails too, and that rule would then leave only ABORTED or a prose ending. So `platform-unavailable`
alone may hold an unpublished tip, and only when the remote does not answer. The fact names the tip,
`--status` prints it on the checkpoint line, and a take-over prints the push as its first act. A
scheduled resume already refuses while the remote does not answer (the auto-resume unit's rule 4).

`HOLD_FLOOR` is the shrink-only count of core hold codes. It is declared rather than defaulted,
because a pin that quietly defaults is a pin nobody set.

### The lease

One file per slug under the git COMMON dir, so every worktree on the node sees the same one:

```
taken <iso> keepalive <id> host <hostname>
refreshed <iso>
```

or `released <iso> held` after `--hold`. The bound is `max(GATE_BOUND, LEASE_STALE_AFTER)` in this
unit. The declared-wall unit replaces the first term with the record's pinned `gate-backstop` fact
(`TOOL-dDerivedDocket-27` S11), and keeps `GATE_BOUND` as the announced fallback for a record that
carries no such fact. `LEASE_STALE_AFTER` is a new optional conf key defaulting to 7200 seconds,
announced when defaulted. The first term exists because a live bar can hold a session silent for
the whole bar.

`--resume` is two verbs in one today, orientation and take-over, and the lease separates them:

| Record | Lease | `--resume` |
|---|---|---|
| HELD | released, stale or absent | take-over: the steps in S5; with no `--keepalive-id`, prints the `--status` block, then refuses, numbered, naming `--keepalive-id`, and writes nothing |
| HELD | fresh and taken | refuses, numbered: another session already resumed it |
| working phase | fresh, taker equals the `--keepalive-id` passed | orientation, as today; refreshes the lease and reaps the run's orphans at the process-ledger unit's seam |
| working phase | fresh, a different `--keepalive-id` passed | refuses, numbered: a live session drives this slug; unless `--replaces <old>` names the lease's id, which records the new id in the lease and the `keepalive` fact |
| working phase | fresh, no id passed | prints the `--status` block, then refuses, numbered: a live session drives this slug; a session whose own scheduler lists the lease's keepalive passes it as `--keepalive-id`; writes nothing |
| working phase | stale | `presumed-stopped`: take-over; with no `--keepalive-id`, prints the `--status` block, then refuses, numbered, naming `--keepalive-id`, and writes nothing |
| working phase | absent, and the `--keepalive-id` passed equals the record's `keepalive` fact | orientation that TAKES the lease naming that id, whatever the build folder's age: the holder of a run that predates the lease |
| working phase | absent, any other id or none | `presumed-stopped` once the newest commit touching the build folder is older than the bound, announced, and taken over, refusing a missing id as the stale row does; inside the bound, prints the `--status` block, then refuses, numbered, naming that commit's age and `--keepalive-id` |
| terminal | any | unchanged: nothing to resume, and never a re-drive of the lander |

The keepalive id is the identity because the scheduler store is SESSION-scoped: a session can list
its own jobs and no other session's. A resume that passes an id its own scheduler lists is the
session that holds the lease. The row with no id refuses, because `--resume` is the only point at
which a second session can be stopped (KF7; design §22.1 records under D12-i9 that the lease makes a
resume refuse while a live session holds the slug). The refusal prints the `--status` block first,
so a session regrounding by the build method's no-id spelling still reads its phase and witness. It
then resumes with its own keepalive id, which it takes from its own scheduler's listing and never
from the `LEASE` line. Refresh sources: `--preflight`, a take-over, and a leaseless holder's
orientation TAKE the lease, and every writing verb past its own write gate, the start of
`run_bounded` under the rule below, and a `--resume` whose id matches the lease REFRESH it.

A refresh is a WRITE, so it obeys the rule every other write obeys. `run_bounded` refreshes a lease
only when it reads `taken` naming the keepalive the calling verb acts for: that verb's
`--keepalive-id` when it takes one, else the record's `keepalive` fact. A released, absent or foreign
lease is never written by `run_bounded`. Preflight's precondition half runs bounded probes such as
`WIRING_CHECK` before its gate, so a refused preflight cannot renew a lease it does not hold. Every
refresh rewrites only the `refreshed` line.

The keepalive tick refreshes the lease through the matching-id `--resume` row: the Skill names the
tick's first act, once a run-state file exists, as `--resume <slug> --keepalive-id <own id>`. The
driver cannot observe the tick itself. The protocol's resume rule — reap the recorded job, then
schedule a replacement — is kept, and the take-over now records the replacement id instead of
leaving the `keepalive` fact naming the old job.

### Take-over, named acts and authorization

Interrupted acts are NAMED, never repaired: a non-empty index, the newest `<git-dir>/gate-run/`
window with no verdict line, and a turnstile ticket whose pid is dead. Authorization is re-verified
through the same `trusted_base` and `check_authorization` pair `--close` uses, so the two verbs
cannot disagree about which base authorizes the run. A cross-node take-over cannot reap a job in
another node's session, so it accepts `--keepalive-unreachable <node>` and records it.

### The Skill's Resume section and protocol §5

The Skill's Resume section is rewritten; §5's user-docs row names the Skill line. Its BASE paragraph
"The record cannot be corrected in place… costs more than the stale field does." becomes the
take-over rule:

> Run `--status <slug>` first. If your own scheduler lists the keepalive its `LEASE` line names, or,
> when no `LEASE` line prints, the keepalive the record's `keepalive` fact names, you hold the lease:
> resume with `--resume <slug> --keepalive-id <that id>` and do not reap it.
> Otherwise you are taking over: reap the recorded job and read the result back, schedule a new one,
> then run `--resume <slug> --keepalive-id <new id>`, which records the new id. If that resume refuses
> or prints `still held`, reap only the job you just scheduled, read the result back, and stop. Replace
> your own job only through `--resume <slug> --keepalive-id <new> --replaces <old>`.

The refused-take-over sentence is the auto-resume unit's §8 F8, decided for both units. A job left
scheduled after a refused take-over ticks `--resume <slug> --keepalive-id <own id>` (F6), which on a
HELD record takes the take-over row without `--scheduled` and skips that unit's remote-freshness
refusals. `still held` writes nothing and takes no lease, so it leaves the same job firing.

Its `only` is the auto-resume unit's §8 F9, also decided for both units. That unit files a durable
restart for a hold, and its Resume step deletes that restart only after a take-over's `--resume`
succeeds, never before it and never on this branch. Here the reap of the recorded job comes before
`--resume`, so a delete placed beside it would remove the restart whenever a manual resume on an
`after` hold prints `still held`, and leave the run HELD with nothing filed to restart it.

The "reap before schedule" measurement paragraph stays, scoped to the take-over case. The Skill's
keepalive section names the tick's first act, once a run-state file exists, as
`--resume <slug> --keepalive-id <own id>`.

Protocol §5's paragraph saying the new id cannot be recorded (`PROTOCOL.template.md:400-406`)
becomes: "A take-over records the new id. A holder that replaces its own job records the replacement
with `--replaces`. The `keepalive` fact therefore names the live job, and the close attestation
covers that job." Its "reap before schedule" measurement is kept.

### The checkpoint

`--status` on a HELD record prints, after its existing line:

```
held · code <c> · until <cond> · since <iso> · from <phase>
checkpoint · witness <sha8> · next <unit> · last bar <path of the newest gate-logs record> · parked <n>[ · unpushed <sha8>]
reason · "<hold-reason>"
```

The `unpushed` field prints only when the record carries `hold-unpushed`. A take-over over such a
hold prints the branch push of that tip as its first line, before any other output.

The bar is a PATH and never a verdict word. The reason sits on its own line, quoted, and is never
parsed. That is the dCarriedReceipt class: a prose reason there stated a gate verdict, and a reader
took it for one.

### `derived_phase()`

Two readers: `derived_phase`, the effective phase, and `recorded_phase`, the fact as written. At
BASE the `phase` fact is read at the sites below, and this unit routes each one as its row says. The
structural arm in `tools/unattended/check-unattended.sh` takes the `recorded` rows as its
allow-list. `derived_phase` is where later derivations go, starting with the derived-terminal unit's
LANDED.

| Function | Site at BASE | Reads | Why |
|---|---|---|---|
| `refuse_if_terminal` | `unattended.sh:1613` | derived; recorded under `--recorded` | KF15; only `--landed` passes `--recorded` |
| `verb_preflight`, rotation test | `:2568` | derived | KF15 |
| `verb_preflight`, phase-absent guard | `:2749` | direct, exempt | the read shares the line of the `set_fact … phase RUNNING` it guards |
| `verb_resume` | `:2883` | derived | KF15 |
| `verb_status` | `:2795` | derived | KF15, and the derived-terminal unit's S3 |
| `check_single_live` | `:1283`, `:1324` | derived | the driver's twin of leg check 7's exclusion |
| `archive_name_of` | `:1604` | recorded | names the archive by what the bytes it is handed say; the derived-terminal unit's rotation hands it a copy already carrying the terminal, before the write gate |
| `verb_landed` | `:2270`, `:2282` | recorded | its own postcondition is a terminal; `:2282` reads another worktree's uncommitted copy |
| `verb_phase` | new in this unit | derived | HELD's exit refusal (S9) |

The exemption is a LINE, never a function. The arm scans for `set_fact <file> phase` sites, and a
read that shares a line with one is a writer's own guard and is exempt. Everything else is graded:
- Outside `derived_phase` and `recorded_phase`, every other direct read of the `phase` fact reds,
  whatever function contains it. At BASE, `verb_preflight`'s rotation test at `:2568` is such a
  read, inside a function that also writes the phase.
- A call to `recorded_phase` reds unless its function's row names recorded.
- A table row naming a function that no longer reads the phase reds.

Before the arm is wired, its predicate runs over BASE's driver and prints hits and near-misses
(charter §7). `:2568` must appear as a hit.

`derived_phase <file>` is called as a plain command and never inside `$(...)`, which would lose what
it sets (the `status-set-in-a-subshell` class). It sets two globals, the effective phase and a
reason that is empty unless the phase stays LANDING for a stated cause. It returns 0, prints
nothing, never calls `fail`, and never touches the global `status`. `recorded_phase <file>` returns
the fact as written. Both names pass `python tools/lexicon/lexicon.py --suggest` at build time.

### Preflight on a live record

`--preflight` rotates a terminal record. At BASE, on a live non-terminal record, it is a
re-preflight the kit sanctions after a compaction (`PROTOCOL.template.md:572`,
`SKILL.template.md:169`). The anchor triple is pinned once (owner fork 2026-08-16), so only the
`keepalive` and `witness` facts are rewritten, and the keepalive rewrite is
TOOL-aBranchedMandate-8's defect. It now keeps the recorded keepalive. A re-preflight passing the
same id is idempotent and refreshes the lease. One passing a different id refuses, numbered, naming
`--resume`, whose matrix decides whether that session holds the slug. Any preflight over HELD
refuses naming `--resume`, which answers TOOL-aBoundedVerdict-2's measured objection that a
non-terminal phase wedges the next preflight.

### Where the text goes

The protocol stands at 57,815 of its 61,440-byte guide cap, measured at BASE. The contract — codes,
conditions, lease, checkpoint, resume matrix — goes to `UNATTENDED-STOPS.md`, rendered from a new
kit template beside the verb carrier, and joined by the same wiring check. The protocol gains one
§3 row for HELD and one §7 row pointing at the companion.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/PROTOCOL.template.md` · `tools/unattended/VERBS.template.md` ·
`tools/unattended/SKILL.template.md` · a new companion template · `tools/unattended/kit.toml` ·
`tools/unattended/adopt-unattended.sh` · `tools/unattended/.unattended.conf.example` ·
`.unattended.conf` · the rendered guides · `memory/map/features/unattended.md` · `memory/DECISIONS.md`.

### Alternatives rejected

- A halt code instead of a phase (TOOL-aBoundedVerdict-2's ruling). A code on a terminal record
  cannot resume, and the stops this unit exists for are the ones that need to.
- A HELD checkpoint rendered into the run-state file's generated region. `records-current` requires
  that region empty, so a stored checkpoint would block the close it exists to lead to.
- Conf-declared probe commands evaluated at `--resume`. It adds a command-execution surface at a
  moment no one watches, for a question the resumed run answers by retrying.
- Refusing every `--resume` on a fresh lease whatever id it passes. It refuses the holder's own
  resume, which the matching-id row orients instead.
- An exit-0 orientation for a no-id resume over a fresh lease (rev-1). It admits any session that
  follows the Skill's Resume step, which is the double-drive KF7 exists to stop.

## 5. Production-readiness checklist

- security — no new write surface beyond the run-state file and one lease file under the git common
  dir. The reason text is stored and printed, never interpreted. No command from a record executes.
- perf / scale — one small file read per verb; the lease write is one rename.
- error / empty / loading states — every refusal is numbered and writes nothing; an absent lease
  reads as released on a HELD record; on a working phase it follows the matrix's two absent rows; a
  malformed lease is a numbered refusal naming the file, never a free pass.
- observability — the checkpoint lines, the `LEASE` line and `presumed-stopped` in `--status`.
- risks — a stale-lease take-over while the original session is merely slow. The bound's first term
  covers a live bar; a slower silence than the bound is presumed dead by design and says so. A
  `platform-unavailable` hold over an unpublished tip lives only on this node until the take-over's
  first push; the checkpoint names it. `--replaces` trusts the caller to name its own job, as the id
  itself does. The lease prevents an accidental second driver, not a malicious one.
- testing — `tools/unattended/unattended.test.sh` and `tools/unattended/check-unattended.test.sh`
  arms, each staged RED; run once at the unit's end under `--attribute` against BASE.
- migration — `CORE_FLOOR` moves in gov's conf in the same commit as the phase; adopters move it in
  their own deployer builds. An existing record carries no hold facts. A working record in flight
  when this unit lands has no lease, and its holder's first `--resume` passing the recorded
  keepalive takes one.
- user docs — the companion guide, the two protocol rows, the verb carrier entry and the Skill line.

## 6. Acceptance criteria

- **AC1** — When `--resume` runs on a HELD fixture whose `hold-until` is `after` a future instant,
  it prints `still held`, exits 0, and the run-state file and the lease file are byte-unchanged.
  Red when: the lease or phase is written before the condition is evaluated.
- **AC2** — When `--hold` runs on a dirty fixture tree, it refuses with a numbered message and the
  run-state file is unchanged.
  Red when: the clean check runs after the phase write, leaving a HELD record over uncommitted work.
- **AC3** — When `--hold --reason` carries the words `gates GREEN`, `--status` prints them only on
  the quoted `reason ·` line, and the `checkpoint ·` line's bar field is a path.
  Red when: the checkpoint composes a gate verdict from the reason or from anything but a record.
- **AC4** — When a HELD fixture is resumed from a second clone with `--keepalive-unreachable nodeX`
  and a new `--keepalive-id`, the take-over records both and returns to the held-from phase.
  Red when: the take-over refuses because the recorded job cannot be reaped from this node.
- **AC5** — When `--landed` or `--close` runs on a HELD fixture, each refuses with a numbered
  message and writes nothing; and `--phase <working phase>` on a HELD fixture refuses with a
  numbered message and writes nothing.
  Red when: `--landed` or `--phase` tests only `is_terminal`, which a non-terminal HELD passes, so
  `--phase` skips the take-over's condition test and authorization step.
- **AC6** — When a HELD fixture's lease was freshly taken by another keepalive and `--resume` runs,
  it refuses; when a working-phase lease names keepalive A and `--resume --keepalive-id B` runs, it
  refuses; with no id it prints the `--status` block and then refuses with a numbered message naming
  `--keepalive-id`, and the run-state file and the lease file are byte-unchanged.
  Red when: a take-over proceeds over a fresh lease, or a no-id resume over a fresh working-phase
  lease exits 0, so a second session following the Skill drives the slug.
- **AC7** — When a working-phase fixture's lease is older than the bound, `--status` prints
  `presumed-stopped`, and `--resume --keepalive-id C` records C and names a staged index left in
  the fixture.
  Red when: staleness is read from the run-state file's mtime or the last commit time instead of the
  lease, for a record that has one.
- **AC8** — When `bash tools/unattended/check-unattended.sh` grades a copy of the driver in which
  `--status` reads the `phase` fact directly, it reds naming that call site. It also reds naming the
  site for a copy whose `verb_preflight` rotation test reads the fact directly although that
  function writes the phase. A copy in which `verb_resume` calls `recorded_phase` reds naming the
  function, and so does a copy whose allow-list names a function that no longer reads the phase.
  Red when: the structural arm greps a population that excludes the verbs, so it passes on nothing;
  or the allow-list has no staleness test, so a stale row silently widens it; or the exemption
  covers a whole writer function, so five of the table's nine rows can read the fact directly and
  never red.
- **AC9** — When `HELD` is deleted from `PHASES_CORE` in a fixture copy of the driver,
  `bash tools/unattended/check-unattended.sh` reds on the `CORE_FLOOR` of `13:12`; and when
  `inherited-red` is deleted from `HOLD_CODES_CORE` in a fixture copy, the leg reds on `HOLD_FLOOR`.
  Red when: the floor stays at 12, so the deletion passes; or the hold vocabulary has no floor, so
  dropping a code a sibling routes to passes.
- **AC10** — When `--preflight` runs twice with the same `--keepalive-id` over a working-phase
  fixture record, with the record committed between the two runs, the second run exits 0 and the
  `keepalive` and anchor facts are unchanged. With a different `--keepalive-id` it refuses with a
  numbered message naming `--resume`; the `keepalive` fact is unchanged, and so is the lease file,
  byte for byte, although the fixture conf's `WIRING_CHECK` stub ran through `run_bounded` in
  preflight's precondition half. Over a HELD fixture whose lease reads `released … held`, it refuses
  naming `--resume`, and the lease file is byte-unchanged.
  Red when: a re-preflight rewrites the `keepalive` fact, as TOOL-aBranchedMandate-8 records, or a
  HELD record is re-preflighted; or `run_bounded` refreshes any lease it finds, so a refused
  preflight renews a dead session's lease and that session's own `--resume` is refused for the whole
  bound.
- **AC11** — When `bash tools/unattended/check-unattended.sh` and the skill-wiring check run over
  the rendered tree, `--hold` is declared in the driver, carried by the verb guide, invoked in the
  Skill, and the companion guide renders byte-identical to its template; the Skill's Resume section
  passes `--keepalive-id` on every `--resume` it spells, its take-over branch removes nothing before
  that resume but the recorded job and, when that resume refuses or prints `still held`, reaps only
  the job it scheduled and reads the result back, and its keepalive section names
  `--resume <slug> --keepalive-id` as the tick's first act. The verb guide's `--hold` entry lists
  `--reaped` and `--keepalive-unreachable`.
  Red when: the Skill never invokes `--hold`, so no agent following it would ever pause a run; or
  the Skill's Resume step still spells `--resume <slug>` with no id, so every holder is refused and
  every follower of the Skill takes the refusal for a stop; or the synopsis omits the keepalive
  flags, so a route spelled from it is refused at its only ending; or a refused take-over stops with
  its new job still scheduled, so that job keeps ticking `--resume` on the HELD record and takes it
  over unwatched once the refusal or the unmet condition clears, with none of the scheduled-resume
  refusals in front of it; or the take-over branch removes anything besides the recorded job before
  its `--resume`, or besides the job it scheduled once that resume refuses or prints `still held`,
  so once the auto-resume unit files a restart under the slug's name, a manual resume before an
  `after` hold's instant deletes that restart and leaves the run HELD with nothing to restart it.
- **AC12** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once at the
  unit's end, its attribution summary reads `verdict clean`: no NEW FAIL, no `DEAD PROBE at L` and
  no `OVER BUDGET at L`. Every suite it reports with INHERITED lines or `DEAD PROBE at R` is named by
  its file path in a filed backlog row or ask that is not CLOSED, as
  `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'` shows.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it; or the run is
  read by its NEW count alone, so a suite this unit's change aborted before its first FAIL line, or
  pushed past its budget, reads as clean; or an inherited failure is attributed away with no record
  filing it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: D12-i8 lifts the do-not-run instruction for this unit.
- **AC13** — When `--phase <slug> HELD --witness <sha>` runs on a working-phase fixture, it refuses
  with a numbered message and the run-state file is byte-unchanged. When
  `bash tools/unattended/check-unattended.sh` grades a driver copy in which `verb_phase` accepts a
  literal phase that another verb's `set_fact … phase` site writes, other than `--preflight`'s
  initial `RUNNING`, it reds naming that phase.
  Red when: `verb_phase` refuses only the terminals and LANDING, so one phase move produces a HELD
  record with no `held-at`, `hold-until`, `hold-code` or `held-from`.
- **AC14** — When `--hold` runs on an already-HELD fixture, on a fixture whose branch tip is not on
  its answering remote under `ANCHOR_SCOPE=published`, and on a fixture whose recorded keepalive is
  neither named by `--reaped` nor recorded unreachable, each call refuses with a numbered message
  and the run-state file is unchanged.
  Red when: a `--hold` on a HELD record overwrites `held-from` with HELD, or a hold is taken over an
  unpublished tip the remote could have received, or over a keepalive still firing.
- **AC15** — When `--hold --code platform-unavailable` runs under `ANCHOR_SCOPE=published` on a
  fixture whose `origin` names a missing path, it holds and records `hold-unpushed` naming HEAD. The
  same call with `--code host-degraded` refuses, and with an answering remote and an unpushed tip it
  refuses naming the push. `--status` on that record prints `unpushed` with HEAD's short sha on its
  `checkpoint ·` line. `--resume --keepalive-id C` taking it over prints the branch push of that tip
  as its first line.
  Red when: the published-tip clause stays unconditional, so a sustained outage has no clean end;
  or the exception reaches another code, or a remote that answers; or the checkpoint omits the
  unpushed tip, so the one signal that held work exists only on this node is hidden.
- **AC16** — When `--hold` runs with `--code bogus`, and again with `--until 'after tomorrow'`, each
  refuses with a numbered message and writes nothing; a code declared in `HOLD_CODES_EXTRA` is
  accepted.
  Red when: an unvalidated condition reaches the auto-resume unit's fire-instant computation, or a
  pause is recorded under a code outside the effective hold set.
- **AC17** — When `tools/unattended/unattended.test.sh` runs `--preflight` on a fixture, the lease
  file reads `taken` with the preflight's keepalive. Then, in order:
  1. `--resume --keepalive-id <that id>` advances `refreshed`, leaves the `taken` line and the
     run-state file byte-unchanged, and exits 0;
  2. `--phase` advances `refreshed` again;
  3. `--hold` rewrites the file to `released … held`;
  4. `--abort` removes it.

  The first step is staged RED by dropping the refresh from the matching-id row.
  Red when: a verb in that sequence skips its lease write, so a live working-phase record reads as
  released or `presumed-stopped` to a second session; or the holder's own orientation does not
  refresh, so an idle holder's lease goes stale and a second session takes the slug over while its
  holder is alive.
- **AC18** — When `--resume` runs on a HELD fixture whose mandate no longer verifies at the pinned
  BASE, it refuses with a numbered message, and the run-state file and the lease file are
  byte-unchanged.
  Red when: the take-over skips `trusted_base` and `check_authorization`, so a revoked mandate keeps
  being driven by unwatched scheduled sessions until `--close`.
- **AC19** — Take a leaseless BUILDING fixture whose `keepalive` fact names A. When `--status` runs
  over it with its newest build-folder commit older than the bound, it prints `presumed-stopped` and
  names that the record had no lease, and `--resume --keepalive-id C` takes it over and records C.
  With that commit inside the bound, `--resume --keepalive-id C` refuses with a numbered message
  naming the age.
  Red when: a leaseless working record is taken over with no age test, or never surfaced at all,
  which is the population the backlog row records.
- **AC20** — When a fixture session holding the lease runs `--resume --keepalive-id B --replaces A`,
  A being the lease's id, the lease and the `keepalive` fact then name B; `--hold --reaped A`
  refuses and `--hold --reaped B` is accepted; and `--replaces X`, X not the lease's id, refuses and
  writes nothing.
  Red when: only a take-over records a new id, so after the first in-session replacement the lease
  and the `keepalive` fact name a reaped job, and `--reaped` accepts the stale id while the live one
  keeps firing into the HELD run.
- **AC21** — When `--resume` with no `--keepalive-id` runs on a HELD fixture whose `hold-until`
  condition is met, and again on a working-phase fixture whose lease is stale, each prints the
  `--status` block and refuses with a numbered message naming `--keepalive-id`. The run-state file
  and the lease file are byte-unchanged.
  Red when: a take-over row accepts a missing id and writes `taken <iso> keepalive` with a blank id,
  so the session's own later `--resume --keepalive-id <id>` meets the fresh different-id row,
  `--replaces` cannot name a blank id, and nobody can drive the slug until the lease goes stale.
- **AC22** — Take a leaseless BUILDING fixture whose newest build-folder commit is inside the bound
  and whose `keepalive` fact names A. `--resume --keepalive-id A` exits 0 and the lease file then
  reads `taken … keepalive A`. The same fixture resumed with `--keepalive-id B` prints the `--status`
  block and refuses, with a numbered message naming the commit's age and `--keepalive-id`, and the
  run-state file stays byte-unchanged with no lease file created.
  Red when: the absent row cannot tell the holder from a second session, so every run in flight when
  this unit lands stalls for the whole bound and the Resume rule sends its holder down the take-over
  path to reap its own keepalive.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `playbook validity gate` · `memory hygiene` · `codebase-map coverage + freshness` · `kit version markers` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a HELD fixture record with an unmet `after`, a dirty tree, and a fresh foreign lease · none
New arm: `tools/unattended/check-unattended.test.sh` · a driver copy reading the phase fact outside `derived_phase()`, one whose writer function `verb_preflight` reads it directly at its rotation test, one with HELD deleted from the core set, and a driver copy whose `verb_phase` accepts HELD; the predicate first run over BASE's driver with hits and near-misses printed, `unattended.sh:2568` a live hit · the core phase floor, 12 to 13

## 8. Open questions

- **F1 — may the kit add a new phase at all, given TOOL-aBoundedVerdict-2?** That record ruled a
  halt a code and never a phase, on three measured grounds; the owner then ratified the kit-stop
  design, including the HELD phase, and ordered it built first.
  RESOLVED (owner, 2026-09-13): D12-i and D12-i11 ratify HELD as a non-terminal phase; a DECISIONS
  row supersedes the earlier record for this case, and AC10 answers its preflight objection.
- **F2 — what does `--resume` evaluate for `probe` and `owner`?** Options: conf-declared probe
  commands; or met on any resume, with the run retrying and re-holding. The first adds an execution
  surface and an open question about who writes the commands.
  RESOLVED (agent, 2026-09-14, delegated): met on any resume; only `after` is evaluated.
- **F3 — how does a resume tell the lease holder from a second session?** Options: refuse every
  resume on a fresh lease; a token stored in the record; the session's own keepalive id. The first
  breaks regrounding, the second is readable by any session.
  RESOLVED (agent, 2026-09-14, delegated): the keepalive id, with the matrix in §4. A resume that
  passes no id over a fresh lease prints the `--status` block and then refuses with a numbered code,
  as KF7 specifies and as design §22.1 records under owner ruling D12-i9; the rev-1 exit-0 row for
  that case is withdrawn.
- **F4 — order against the landing-path unit.** The brief's edge table has the landing path consume
  from this unit while its roster numbers put this unit after it, which the §3 order join refuses.
  RESOLVED (agent, 2026-09-14, delegated): this unit takes `order 3` and the landing path `order 4`.
  No other edge in the roster involves either order value.
- **F5 — what does `--preflight` do over a live record?** Options: (a) own-slug re-preflight stays
  idempotent and keeps the recorded keepalive, refusing over HELD and on a different id, naming
  `--resume`; (b) refuse every live re-preflight, and rewrite the protocol's waiver paragraph and the
  Skill's re-preflight line, removing the pin-once branches. (b) retires a flow the kit sanctions in
  five places for no property (a) lacks. RESOLVED (agent, 2026-09-14, delegated): (a), with
  TOOL-aBranchedMandate-8's hand-off arm, the keepalive surviving two preflights, as AC10.
- **F6 — does the keepalive tick refresh the lease?** KF7 names it a refresh source, but the driver
  cannot observe a harness tick, and the tick fires only while the session is idle. Options: (a) the
  Skill names the tick's first act as `--resume <slug> --keepalive-id <own id>`, whose matching-id
  row refreshes the lease; (b) no tick refresh, with the bound's first term covering the silence.
  RESOLVED (agent, 2026-09-14, delegated): (a). It delivers KF7's refresh source through a row that
  already exists, and it adds no driver surface. Because that tick goes down the take-over row on a
  HELD record, a take-over that refuses or prints `still held` reaps the job it scheduled, as unit 5
  §8 F8 decides for both units, and removes nothing else, as unit 5 §8 F9 decides for both (§4).
- **F7 — may a hold be taken over an unpublished tip?** Design §21.7 requires the branch pushed
  before HELD. Options: (a) never; (b) for `platform-unavailable` only, when the remote does not
  answer, recording the tip; (c) for any code. (a) leaves a sustained outage with no clean end,
  which is the ending HELD exists to replace; (c) holds unpublished work for reasons that do not stop
  the push. RESOLVED (agent, 2026-09-14, delegated): (b). §21.7 is a design rule, not an owner
  ruling, and the relaxation is recorded in §9.
- **F8 — what does a working-phase record with no lease read as?** Options: (a) `presumed-stopped`
  by the age of the newest commit touching its build folder, announced, with a refusal inside the
  bound; (b) released, so a take-over is immediate; (c) left open. (b) takes over a session that
  predates the lease, and (c) leaves an undefined cell. RESOLVED (agent, 2026-09-14, delegated):
  (a), never a refusal outside the bound, per TOOL-aUnblockedFleet-1.
- **F9 — how does the lease holder record a replacement keepalive?** Options: (a)
  `--resume --keepalive-id <new> --replaces <old>`, accepted when `<old>` is the lease's id; (b)
  only a take-over records an id. Under (b), the protocol's kept resume rule, which reaps and
  reschedules, leaves the lease naming a reaped job. RESOLVED (agent, 2026-09-14, delegated): (a).
- **F10 — does the hold vocabulary carry a floor?** Options: (a) a required, shrink-only
  `HOLD_FLOOR`; (b) none, with a reason. Every other conf-extendable core set in the kit carries one.
  RESOLVED (agent, 2026-09-14, delegated): (a).
- **F11 — how does the holder of a run that predates the lease resume?** Options:
  - (a) a matrix row: a leaseless working record resumed with the id its `keepalive` fact records
    takes the lease as an orientation, and the Resume rule reads that fact when no `LEASE` line
    prints;
  - (b) the holder re-preflights to take the lease;
  - (c) the holder waits out the bound, like any leaseless record.

  (c) stalls every run in flight at landing for up to 7200 s, this build's own run included. (b) is
  not what the Skill's Resume rule routes to, so a holder following it still reaps its own keepalive.
  RESOLVED (agent, 2026-09-16, delegated): (a). The identity is the same session-scoped keepalive id
  the lease already keys on, and taken from the session's own scheduler, so it widens nothing F3
  rejected.
- **F12 — what does a take-over row do without `--keepalive-id`?** Options:
  - (a) refuse, numbered and before any write, after printing the `--status` block;
  - (b) take the lease with a blank keepalive, for the first ticking resume to fill in.

  (b) wedges the slug: the fresh different-id row refuses the holder's own next resume, and
  `--replaces` cannot name a blank id. RESOLVED (agent, 2026-09-16, delegated): (a). It is the
  fresh no-id row's behaviour, so the parked BUILD-METHOD M7 fallback in `RUN.md` now holds on every
  row a regrounding resume can reach. Unit 5's scheduled prompt passes the session's own id.
- **F13 — when does `run_bounded` refresh the lease?** Options:
  - (a) whenever it starts;
  - (b) only after the calling verb's own write gate;
  - (c) only when the lease reads `taken` naming the keepalive the calling verb acts for.

  (a) lets a refused verb's bounded probes renew a dead session's lease. (b) never refreshes during
  the bar `--close` runs while evaluating its DoD, before its write gate, and that bar is the long
  silence the refresh source exists for. RESOLVED (agent, 2026-09-16, delegated): (c).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Takes `order 3` rather than the roster's 4 (F4). Adds one edge
  the brief's table does not list, consumes-from unit 1, inside this spec's own group.
- rev-2 · 2026-09-14 · §1 · §2 S2 S3 S5 S6 S7 S8 S9 · §3 · §4 · §5 · §6 AC5 to AC11, AC13 to AC20 ·
  §7 · §8 F3 F5 to F10 · §10 · round-1 spec-audit fold (G1 B1, H1, H2, H3, M1, M3, M6 to M10, M23
  to M27, L1; G3 H4). KF7 is restored: a no-id `--resume` over a fresh lease prints the status block
  and refuses (AC6). That reverses rev-1's exit-0 row, which contradicted design §22.1's D12-i9
  consequence; F3's mark is updated, and the keepalive tick refreshes the lease through the
  matching-id row (F6). The lease bound's first term becomes the pinned backstop in the
  declared-wall unit. HELD is producer-only in `--phase` (AC13). `--hold` accepts an unpublished tip
  for `platform-unavailable` when the remote does not answer (F7, AC15), which relaxes design
  §21.7. S5 runs every refusal before the lease is taken and reaps after it, diverging from DR U26's
  order. Own-slug re-preflight stays idempotent and keeps the keepalive (F5, AC10). A leaseless
  working record reads `presumed-stopped` by build-folder commit age (F8, AC19), citing
  TOOL-aReapedTicket-5. `--replaces` records a holder's replacement keepalive (F9, AC20). Every
  phase read is classified as `derived_phase` or `recorded_phase` per call site (AC8), and §1 says
  so. `HOLD_FLOOR` is added (F10). AC14 and AC16 to AC18 cover `--hold`'s preconditions, the code
  set, the lease lifecycle, and re-authorization at a take-over. G3 H4: hands-off 16's reason is now
  that unit's report-only claim label.
- rev-3 · 2026-09-16 · spec-audit round 2 fold.
  - G1 M1 (4): the structural arm exempts the `set_fact … phase` line, not the function, and the
    `:2749` guard row reads direct and exempt (§4 table, S8, AC8, §7).
  - G1 M2 (5): a leaseless working record resumed with its recorded keepalive takes the lease, and
    the Resume rule reads that fact (§4 matrix, S6, S7, F11, AC22, §5).
  - G1 M5 (27): every take-over row refuses a missing `--keepalive-id` before any write (S5, F12,
    AC21).
  - G1 M6 (44): `run_bounded` refreshes only a `taken` lease naming the calling verb's keepalive
    (§4 The lease, S6, F13, AC10).
  - G1 M7 (13): AC17 observes the matching-id refresh.
  - G1 L4 (14): the checkpoint carries `unpushed`, and a take-over prints the push first (S4, AC15).
  - G1 L3 (36): S2's synopsis lists `--reaped` and `--keepalive-unreachable` (AC11).
  - G1 M3 (6, 29) and B1 (40): S6, the §3 hands-off edge to unit 22 and the `archive_name_of` row
    agree with unit 22's lease rewrite and rotation order.
  - G1 H1 (2, 24): AC12 reads `verdict clean`, and the §3 consumes-from edge to unit 1 is updated.
  - Fold verification, following M2 and M6: AC19's fixture pins its `keepalive` fact to A, and both
    its resumes pass C, so the new leaseless-holder row cannot read either as the holder. §4 The
    lease's refresh-sources sentence states S6's write-gate and `run_bounded` conditions, and §5
    names the matrix's two absent rows.
- rev-4 · 2026-09-16 · round-2 fold, second pass. The verifier problem on units 5 and 4, a
  keepalive left firing after a refused take-over, decided by the orchestrator as option (a) and
  recorded as unit 5 §8 F8: §4 The Skill's Resume section's take-over rule reaps the job it
  scheduled and reads the result back when that resume refuses or prints `still held`, with a
  paragraph cross-referencing that fork, which F6's mark also names; S10 names the rule; AC11
  checks the rendered Skill for it. Fold verification: §8 F6's added sentence says the tick goes
  down the take-over row on a HELD record, not that every tick takes one over. Spec-audit round 2
  fold, third pass, from the second pass's verifier problem on units 5 and 4, a manual resume on an
  `after` hold deleting the owed schedule, decided by the orchestrator as option (a) and recorded as
  unit 5 §8 F9: §4's take-over rule reaps only the job it scheduled on a refusal or `still held`,
  and a new paragraph after it says the restart a hold owes is deleted only after a take-over's
  `--resume` succeeds; S10 says `only`; AC11 and its `Red when:` read that the branch removes
  nothing else; §8 F6's mark sentence cites unit 5 §8 F9.

## 10. Reuse audit

- The seams are the driver's own: the phase writer and `is_terminal`, `refuse_if_terminal`,
  `run_bounded`, the `trusted_base` and `check_authorization` pair `--close` uses, the halt-code
  validation pattern `--abort` uses for a closed vocabulary, and the keepalive record protocol §5
  already defines. The companion-guide mechanism is the verb carrier's, `VERBS.template.md` rendered
  to `UNATTENDED-VERBS.md`. The probe `reuse_lookup.py "hold a run in a non-terminal paused phase and
  resume it later"` returned only name-stem matches and reports `unscanned layers: .sh`, so it is
  blind to the shell driver; the seams above were found by reading it. Recall returned
  TOOL-aBoundedVerdict-2, the ruling F1 supersedes, and TOOL-aUnmannedHelm-8. Where the design
  record and the source disagree: the record puts the keepalive-gone test in `presumed-stopped`,
  which its own KF7 amendment replaced with the lease, and this spec follows KF7. The design lists
  TOOL-aReapedTicket-5 among U26's closes. At BASE its population is two BUILDING records with no
  lease, `memory/builds/aClosedDocket/RUN.md` and `memory/builds/aUnblockedFleet/RUN.md`, which the
  absent-lease row surfaces.
- M12 was not reached: the owner ratified the mechanism.
- Recall terms used: `HELD phase halt-code abort host-degraded platform-limit keepalive resume
  presumed-stopped lease checkpoint CORE_FLOOR phases`
