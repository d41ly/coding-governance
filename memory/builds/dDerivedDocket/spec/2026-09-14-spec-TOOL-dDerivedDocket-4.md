# TOOL-dDerivedDocket-4 — HELD phase, lease and derived phase

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

An unattended run that meets a stop it cannot fix — a usage limit, an overloaded API, a degraded
host, an inherited red it may not absorb — has two endings today, ABORTED or a prose handoff, and
both end the run. Add a non-terminal HELD phase that a run enters by a verb, with a code, a release
condition and a generated checkpoint, and that it leaves by `--resume` with no owner answer. Add a
per-slug lease so two sessions cannot drive one slug, and route every phase reader through one
`derived_phase()` so they cannot disagree. Built in the first group by owner ruling D12-i11.

## 2. Scope (IN)

- **S1** HELD joins `PHASES_CORE` as a non-terminal phase, placed after LANDING. `CORE_FLOOR` in
  gov's `.unattended.conf` and in the kit's conf example moves from `12:12` to `13:12`; the DoD
  half moves later with the asks-disposed unit. Observed by AC9.
- **S2** A verb `--hold <slug> --code <c> --until <cond> --reason <text>`, with a closed code set
  plus `HOLD_CODES_EXTRA`, and a closed condition grammar. Observed by AC1, AC2 and AC11.
- **S3** `--hold` refuses, numbered and before any write, unless: the record is live and not HELD;
  the tree is clean and committed; the branch tip is on its remote when `ANCHOR_SCOPE=published`;
  and the recorded keepalive is either reaped, named by `--reaped <id>`, or recorded unreachable by
  `--keepalive-unreachable <node>`. Observed by AC2 and AC4.
- **S4** The checkpoint is DERIVED by `--status` from the hold facts on every read, never stored as
  a second copy. Every gate claim in it is a pointer to a run record. Observed by AC3.
- **S5** `--resume` on a HELD record performs, in order: the condition test; naming interrupted
  acts; re-verifying authorization at the pinned BASE; accepting a new `--keepalive-id`; returning to
  the held-from phase. An unmet condition prints `still held` and writes nothing. Observed by AC1,
  AC4 and AC6.
- **S6** A lease at `<git-common-dir>/unattended/<slug>.lease`, taken at `--preflight` and at a
  take-over, refreshed by every writing verb and at the start of `run_bounded`, released by
  `--hold`, removed at a terminal. Observed by AC6 and AC7.
- **S7** `presumed-stopped`, derived by `--status` when a working-phase lease is older than the
  bound; `--resume` then takes the run over. Observed by AC7.
- **S8** One `derived_phase()` reader. `refuse_if_terminal`, preflight's rotation test, `--resume`
  and `--status` read the phase through it and through nothing else. Observed by AC8.
- **S9** HELD blocks `--close`, `--landed` and `--phase`; only `--resume` leaves it, and only
  `--landed` and `--abort` still write a terminal. `--preflight` on any live non-terminal record
  refuses and names `--resume`. Observed by AC5 and AC10.
- **S10** The contract text goes to a new companion guide, `UNATTENDED-STOPS.md`, rendered from the
  kit like the verb carrier; the protocol gains two rows, one in §3 and one in §7. The `unattended`
  dossier claims the new guide key. Observed by AC11.
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

- **consumes-from** `TOOL-dDerivedDocket-1` — the "no NEW FAIL" criterion for the unattended suites
  this unit is allowed to run once at its end.
- **hands-off** `TOOL-dDerivedDocket-3` — `derived_phase()` and the HELD refusals, which the landing
  path's `--close` and Land steps rely on, plus the companion guide the landing text may overflow
  into.
- **hands-off** `TOOL-dDerivedDocket-5` — the lease, the hold facts and the resume contract that a
  scheduled resume invokes.
- **hands-off** `TOOL-dDerivedDocket-22` — `derived_phase()`, inside which the LANDED derivation
  from the advertised tip goes.
- **hands-off** `TOOL-dDerivedDocket-27` — the `host-degraded` code and the `probe gate` condition
  that a kill before `acquired` holds with.
- **hands-off** `TOOL-dDerivedDocket-28` — the named precondition seam in `--hold` where the
  run-owned process reap goes, and the `--status` line the orphan count joins.
- **hands-off** `TOOL-dDerivedDocket-29` — the checkpoint, which gains the pending review runId.
- **hands-off** `TOOL-dDerivedDocket-16` — `derived_phase()`, which that unit reads to decide which
  builds hold a live run.
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

### The lease

One file per slug under the git COMMON dir, so every worktree on the node sees the same one:

```
taken <iso> keepalive <id> host <hostname>
refreshed <iso>
```

or `released <iso> held` after `--hold`. The bound is `max(GATE_BOUND, LEASE_STALE_AFTER)`, where
`LEASE_STALE_AFTER` is a new optional conf key defaulting to 7200 seconds, announced when defaulted.
The first term exists because a live bar can hold a session silent for the whole bar.

`--resume` is two verbs in one today, orientation and take-over, and the lease separates them:

| Record | Lease | `--resume` |
|---|---|---|
| HELD | released, stale or absent | take-over: the five steps in S5 |
| HELD | fresh and taken | refuses, numbered: another session already resumed it |
| working phase | fresh, taker equals the `--keepalive-id` passed | orientation, as today; refreshes the lease |
| working phase | fresh, a different `--keepalive-id` passed | refuses, numbered: a live session drives this slug |
| working phase | fresh, no id passed | orientation, preceded by a `LEASE` line naming the taker's keepalive and age; exit 0 |
| working phase | stale | `presumed-stopped`: take-over |
| terminal | any | unchanged: nothing to resume, and never a re-drive of the lander |

The keepalive id is the identity because the scheduler store is SESSION-scoped: a session can list
its own jobs and no other session's. A resume that passes an id its own scheduler lists is the
session that holds the lease. The row with no id stays exit 0 because the build method's
regrounding step spells `--resume <slug>` with no id, and a live run following its own method must
not be refused by its own lease. The protocol's resume rule — reap the recorded job, then schedule
a replacement — is kept, and the take-over now records the replacement id instead of leaving the
`keepalive` fact naming the old job.

### Take-over, named acts and authorization

Interrupted acts are NAMED, never repaired: a non-empty index, the newest `<git-dir>/gate-run/`
window with no verdict line, and a turnstile ticket whose pid is dead. Authorization is re-verified
through the same `trusted_base` and `check_authorization` pair `--close` uses, so the two verbs
cannot disagree about which base authorizes the run. A cross-node take-over cannot reap a job in
another node's session, so it accepts `--keepalive-unreachable <node>` and records it.

### The checkpoint

`--status` on a HELD record prints, after its existing line:

```
held · code <c> · until <cond> · since <iso> · from <phase>
checkpoint · witness <sha8> · next <unit> · last bar <path of the newest gate-logs record> · parked <n>
reason · "<hold-reason>"
```

The bar is a PATH and never a verdict word. The reason sits on its own line, quoted, and is never
parsed. That is the dCarriedReceipt class: a prose reason there stated a gate verdict, and a reader
took it for one.

### `derived_phase()`

One function returns the effective phase from the recorded `phase` fact. At BASE four callers read
the fact directly (`refuse_if_terminal`, preflight's rotation test, `--resume` and `--status`), and
this unit routes all four through the function. It is where later derivations go, starting with the
derived-terminal unit's LANDED. A structural arm in `tools/unattended/check-unattended.sh` asserts
that outside the writers only `derived_phase()` reads the `phase` fact.

### Preflight on a live record

`--preflight` rotates a terminal record and, at BASE, overwrites a live non-terminal one, losing
the keepalive id and re-pinning the anchor (TOOL-aBranchedMandate-8). It now refuses any live
non-terminal record, HELD included, and names `--resume` and `--abort`. This is also the direct
answer to TOOL-aBoundedVerdict-2's measured objection that a non-terminal phase wedges the next
preflight: the next preflight is not the resumption path, and now says so.

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
- Refusing every `--resume` on a fresh lease. It refuses the live session's own regrounding.

## 5. Production-readiness checklist

- security — no new write surface beyond the run-state file and one lease file under the git common
  dir. The reason text is stored and printed, never interpreted. No command from a record executes.
- perf / scale — one small file read per verb; the lease write is one rename.
- error / empty / loading states — every refusal is numbered and writes nothing; an absent lease
  reads as released; a malformed lease is a numbered refusal naming the file, never a free pass.
- observability — the checkpoint lines, the `LEASE` line and `presumed-stopped` in `--status`.
- risks — a stale-lease take-over while the original session is merely slow. The bound's first term
  covers a live bar; a slower silence than the bound is presumed dead by design and says so.
- testing — `tools/unattended/unattended.test.sh` and `tools/unattended/check-unattended.test.sh`
  arms, each staged RED; run once at the unit's end under `--attribute` against BASE.
- migration — `CORE_FLOOR` moves in gov's conf in the same commit as the phase; adopters move it in
  their own deployer builds. An existing record carries no hold facts and reads exactly as before.
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
  message and writes nothing.
  Red when: `--landed` tests only `is_terminal`, which a non-terminal HELD passes.
- **AC6** — When a HELD fixture's lease was freshly taken by another keepalive and `--resume` runs,
  it refuses; when a working-phase lease names keepalive A and `--resume --keepalive-id B` runs, it
  refuses; with no id it prints a `LEASE` line and exits 0.
  Red when: a take-over proceeds over a fresh lease, so two sessions drive one slug.
- **AC7** — When a working-phase fixture's lease is older than the bound, `--status` prints
  `presumed-stopped`, and `--resume --keepalive-id C` records C and names a staged index left in
  the fixture.
  Red when: staleness is read from the run-state file's mtime or the last commit time instead of the
  lease.
- **AC8** — When `bash tools/unattended/check-unattended.sh` grades a copy of the driver in which
  `--status` reads the `phase` fact directly, it reds naming that call site.
  Red when: the structural arm greps a population that excludes the verbs, so it passes on nothing.
- **AC9** — When `HELD` is deleted from `PHASES_CORE` in a fixture copy of the driver,
  `bash tools/unattended/check-unattended.sh` reds on the `CORE_FLOOR` of `13:12`.
  Red when: the floor stays at 12, so the deletion passes.
- **AC10** — When `--preflight` runs over a live non-terminal fixture record, it refuses, names
  `--resume` and `--abort`, and the keepalive and anchor facts are unchanged.
  Red when: preflight overwrites the live record, as TOOL-aBranchedMandate-8 records.
- **AC11** — When `bash tools/unattended/check-unattended.sh` and the skill-wiring check run over
  the rendered tree, `--hold` is declared in the driver, carried by the verb guide, invoked in the
  Skill, and the companion guide renders byte-identical to its template.
  Red when: the Skill never invokes `--hold`, so no agent following it would ever pause a run.
- **AC12** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once at
  the unit's end, it reports no NEW failure.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: D12-i8 lifts the do-not-run instruction for this unit.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `playbook validity gate` · `memory hygiene` · `codebase-map coverage + freshness` · `kit version markers` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a HELD fixture record with an unmet `after`, a dirty tree, and a fresh foreign lease · none
New arm: `tools/unattended/check-unattended.test.sh` · a driver copy reading the phase fact outside `derived_phase()`, and one with HELD deleted from the core set · the core phase floor, 12 to 13

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
  RESOLVED (agent, 2026-09-14, delegated): the keepalive id, with the matrix in §4.
- **F4 — order against the landing-path unit.** The brief's edge table has the landing path consume
  from this unit while its roster numbers put this unit after it, which the §3 order join refuses.
  RESOLVED (agent, 2026-09-14, delegated): this unit takes `order 3` and the landing path `order 4`.
  No other edge in the roster involves either order value.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Takes `order 3` rather than the roster's 4 (F4). Adds one edge
  the brief's table does not list, consumes-from unit 1, inside this spec's own group.

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
  which its own KF7 amendment replaced with the lease, and this spec follows KF7.
- M12 was not reached: the owner ratified the mechanism.
- Recall terms used: `HELD phase halt-code abort host-degraded platform-limit keepalive resume
  presumed-stopped lease checkpoint CORE_FLOOR phases`
