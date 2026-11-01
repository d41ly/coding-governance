# TOOL-dFurnishedOrders-26 — presence read inside a run's window: `derive_attended` counts only owner turns after the run started, so the prompt that launched an unattended run never reads as the owner attending

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 5ff43572 · streams tooling · order 21 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-26-deviation-261.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-26-deviation-261.md) | deviation | — |
| [2026-10-28-build-TOOL-dFurnishedOrders-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dFurnishedOrders-1-agent-ledger.md) | journal | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-40 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-43 TOOL-dFurnishedOrders-44 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-47 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-57 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61 |
| [2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dFurnishedOrders-1-parents-crosscheck.md) | research | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61 |
| [2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 20 unit specs
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`)
confirmed finding **id 3 at HIGH**, report item **H1**. Ids 19 and 52 share that item and take
`TOOL-dFurnishedOrders-27` and `TOOL-dFurnishedOrders-28`.

`TOOL-dFurnishedOrders-16` S1 answers attended whenever the session's newest turn was opened by the
owner, read through `scan_owner_turns` (`tools/runlog/extract.py:946-949`), whose `OWNER_VIA` counts
`typed` (`extract.py:52`). An unattended run is launched by the owner's typed prompt, and a keepalive
fires only when the session idles, so every owner question raised before the first fire reads
`owner-turn typed`, and on a host with cron disabled the whole run does. Unit 16's paragraph after "The
attended table" ("an unattended run's turns are opened by keepalive fires") and its Rollout ("nothing
changes for it") are false for that whole stretch. The audit's skeptic reproduced it on this run's own
session: its first event is `owner typed` and every later one `keepalive`.

This unit gives presence a window: the owner attends a run when an owner turn falls after the run's
start, never because of the turn that started it. It repairs `TOOL-dFurnishedOrders-16` and builds one
step after it (order 21); unit 27 hands the run's start to the door on every path the driver asks it,
and unit 28 decides what an unreadable turn means inside a window.

## 2. Scope (IN)

- **S1** — The window. `derive_attended(root, session=None, since=None)` in `tools/roles/roles_lib.py`
  (`TOOL-dFurnishedOrders-16` S1) takes `since`, a UTC stamp. Given, the turn half reads only the
  events whose time is strictly after `since`: an `owner` event among them answers attended, source
  `owner-turn <via> at <utc>`; none answers away, source `away: attendance=<value>, no owner turn since
  <since>`. Not given, unit 16's table stands unchanged. The posture half is read first either way, so
  an `attendance` that adds `ask-live` still answers attended. Observed by AC1, AC2 and AC3.
- **S2** — Times compared as instants. Each event's time and `since` are parsed to UTC instants before
  the compare, so `2026-10-26T17:14:46Z` and `2026-10-26T17:14:46.000Z` are one instant, and an event
  time that does not parse is skipped and counted in the source, ` (<n> unparsed)`. Observed by AC3.
- **S3** — The door's flag. `python tools/roles/handoff.py owner-question --kind <kind> [--session
  <sid>] [--since <utc>]` (`TOOL-dFurnishedOrders-16` S3) passes `since` through. A value that is not a UTC stamp,
  a four-digit year through whole seconds and a trailing `Z`, exits 2 naming `--since` and the value,
  before any read. Observed by AC4.
- **S4** — The docs: `help/roles.md`'s paragraph on the one site, and `tools/roles/README.md`'s door
  line, say that inside a run the owner attends only by a turn after the run started. Observed by AC5.

## 3. Non-goals (OUT)

- Handing the run's start to the door from the driver's `--dispatch` and `--phase`:
  `TOOL-dFurnishedOrders-27`, for id 19.
- What an unreadable turn answers inside a window: `TOOL-dFurnishedOrders-28`, for id 52. Here an
  unreadable turn keeps unit 16's `unread` row.
- The deadline and silence that end a hold: dWellOiledMachine's, as unit 16 §3 states.
- Rewording unit 16's paragraph and Rollout. Its ledger answers the criteria they bear on in the AMENDED
  form, naming units 26 to 28.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-16` — `derive_attended`, the `turns` verb it reads and the `owner-question` door, which S1 to S3 give a window (id 3)
- **hands-off** `TOOL-dFurnishedOrders-27` — `--since`, the door flag the driver passes the run's lease start to on each path it asks the door (ids 3 and 19)
- **hands-off** `TOOL-dFurnishedOrders-28` — `since`, the window whose unreadable-turn row unit 28 decides (ids 3 and 52)
- **hands-off** `TOOL-dFurnishedOrders-37` — S2's time compare and unparsed count, which unit 37 S10 grounds on the `turns` verb's `untimed` line (id 13 of the second audit)

## 4. Design

### The table, with a window

| `attendance` adds `ask-live` | turns after `since` | `attended` | source |
|---|---|---|---|
| yes | any | yes | `attendance=<value>` |
| no | an `owner` event | yes | `owner-turn <via> at <utc>` |
| no | `keepalive` events only, or none | no | `away: attendance=<value>, no owner turn since <since>` |
| no | unreadable | as `TOOL-dFurnishedOrders-28` decides | |

With no `since`, the rows are unit 16's own. A session no run holds passes no `since`, so the owner's
own session reads attended by its newest turn exactly as before.

### Why the run's start and not the newest turn

The launching turn is the one owner turn every unattended run carries, and it is older than the run
by construction: the driver writes `lease-utc` (`tools/unattended/unattended.sh:2406` reads it) inside
the turn the owner typed. An owner who types into the run's session later produces a turn after it,
which is the presence the clause asks the run to honour. A keepalive arm or fire is not used as the
start, because a host with cron disabled has neither.

### Inventory

Minted: the parameter `since`, the door flag `--since`, and the two source strings of S1. No function.

### Migration

None: no answer is stored, and a caller that passes no `since` gets unit 16's table.

### Rollout

Live at landing; inert until `TOOL-dFurnishedOrders-27` passes the window, which follows in the same
order by the dispatch's id sort. `KIT_ROLES_VERSION` moves for the kit epoch leg.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `help/roles.md`

### Alternatives rejected

- **Skip the first owner turn of the session.** A run resumed in a new session, or a session the owner
  used before launching, has its launch turn elsewhere than first; the lease stamp names the start
  wherever it falls.
- **Read the window inside `derive_attended` from the run-state file.** The roles kit would become a
  reader of the driver's record grammar; the driver passes the stamp it already reads.
- **Count only `queued` and `interrupt` turns as presence.** An owner who returns and types a new
  prompt is present, and `typed` is how that arrives.

## 5. Production-readiness checklist

- security — no new write path; the flag is validated at the door before any read (S3).
- perf / scale — one comparison per event already read; no extra subprocess.
- error / empty / loading states — an unparsed event time is skipped and counted in the source; an
  unreadable turn is unit 28's row.
- observability — every answer names its source, including the window and the turn that decided it.
- risks — an owner who watches a run without typing reads away; that is the clause's own line, since
  presence is a turn, and `attendance` sets an attended posture without one.
- testing — AC1 to AC5 by probes over planted transcripts with the environment redirected; the arm of
  §7 at the close.
- migration — none.
- user docs — `help/roles.md`, by S4.

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `roles_lib.derive_attended(root, since=T1)` with
  `CLAUDE_CONFIG_DIR` and `CLAUDE_CODE_SESSION_ID` set to a scratch transcript whose only owner event
  is a `typed` turn at T0, T0 before T1, under `attendance = unattended`, it returns `False` and a
  source naming `no owner turn since` T1; called without `since`, it returns `True` and
  `owner-turn typed`.
  Red when: the launching prompt reads as presence inside a run.
  fixture: a scratch transcripts root under `%TEMP%`, so no live session is read.
- **AC2** — When the AC1 transcript gains a `typed` owner turn after T1, the call with `since=T1`
  returns `True` and a source naming that turn's time.
  Red when: an owner who types into a running session is not seen.
- **AC3** — When the AC1 transcript gains only `keepalive` events after T1, and `since` is spelled with
  milliseconds, `.000Z`, the call returns `False`; an event whose time does not parse adds
  `(1 unparsed)` to the source.
  Red when: keepalive fires read as presence, or two spellings of one instant compare unequal.
- **AC4** — When `python handoff.py owner-question --kind fork --session <sid> --since <T1>` runs in
  the AC1 fixture, it prints the away answer with the AC1 source; with `--since yesterday` it exits 2
  naming `--since`.
  Red when: the door drops the window, or passes an unvalidated stamp to the read.
- **AC5** — When `grep -n "after the run started"` runs over `help/roles.md` and
  `tools/roles/README.md`, each prints a line.
  Red when: a user reading why a run decided a fork finds the old rule.

## 7. Gates

`roles catalogue` · `roles render selftest` · `roles adopter self-test` · `runlog selftest` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 AC3 AC4 · a launch-only transcript, a later owner turn and later keepalives against one window, staged by ignoring `since` · none

## 8. Open questions

- **F1 — What marks a run's start?** Options: (a) the run-state file's `lease-utc`, passed by the
  driver; (b) the session's first owner turn; (c) the most recent keepalive arm. (b) misplaces the start
  on a resumed or reused session; (c) has no value on a host with cron disabled, the case the audit
  names. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the skeptic-judged fix in the report
  and the one value present on every run. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F3 — The unit this one extends is unbuilt.** `TOOL-dFurnishedOrders-16` is specced and unbuilt at
  `5ff43572`. RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on it at the pass and
  stops this unit if a named section is still absent then, rung 1, the brief's rule for unbuilt parents.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 20 unit specs, id 3
  (HIGH, item H1, shared with ids 19 and 52).
- rev-2 · 2026-10-26 · §3 · a hands-off edge to unit 37 (id 13 of the second audit).

## 10. Reuse audit

The seams extended: `derive_attended` and the `owner-question` door (`TOOL-dFurnishedOrders-16` S1 and
S3), and `scan_owner_turns` (`tools/runlog/extract.py:946-949`), whose events already carry their time
`t` (`extract.py:815-817`), so the window needs no new read. `python
tools/codebase-map/reuse_lookup.py "read whether the owner attends from owner turns after the run
started"` ranked `read`, `read_text`, `run`, `run_git` and `read_journal`, none a presence reader, so no
existing seam fits beyond the ones named. The recall probe returned the dBoundRoles ask
TOOL-dBoundRoles-72 on the door's `attended` and the audit's H1 text, neither disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "does the launch prompt of an unattended run
count as owner presence" --terms "attended owner turn typed keepalive launch prompt lease unattended
presence derive_attended hold"`
