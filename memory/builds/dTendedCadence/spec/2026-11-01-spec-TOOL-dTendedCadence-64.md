# TOOL-dTendedCadence-64 — the record push takes the claim-push lock and stands down while the lander's marker is set, as a claim push does

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 22 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-64-deviation-641.md](../build/2026-11-01-build-TOOL-dTendedCadence-64-deviation-641.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 5 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, which shares item H2 with ids 26 (TOOL-dTendedCadence-65) and 37 (TOOL-dTendedCadence-66). Unit
49 S2 pushes `refs/gov/maintain-record/<key>` "as `write_claim` pushes" but leaves out the guards
around that push: `write_claim` takes `<git-dir>/claim-push.lock` and refuses while
`<git-dir>/push-main-active` exists (`tools/unattended/unattended.sh:2399-2416`), because every push
runs `.githooks/pre-push`, which clears the lander's three verdict files on every run
(`.githooks/pre-push:494`). A walk landing its record while `push-main.sh` lands from the same git dir
erases the lander's verdict. This unit gives the record push the same two guards.

## 2. Scope (IN)

- **S1** — The lock. `write_record_landing` (unit 49 S1) takes `<git-dir>/claim-push.lock`, `<git-dir>`
  being `git rev-parse --absolute-git-dir`, through `write_push_lock(lock, token)` in
  `tools/drift-audit/maintenance.py` before it tests the marker, and holds it until its push returns.
  The protocol is `write_claim_push_lock`'s (`unattended.sh:2331-2353`): `os.mkdir` of the lock
  directory; its `until` file holds the epoch deadline, now plus the push's 30 s bound plus 10; its
  `owner` file holds the caller's token, `<pid>.<random>`. Observed by AC1.
- **S2** — The stale break. A lock it cannot make is broken only when `check_push_lock_stale(lock)`
  reads it stale, a deadline already passed or none and a directory older than 120 s, and only by the
  writer that makes the guard `<lock>.break`; holding the guard it re-reads the rule, then clears and
  re-makes the lock. A guard older than 60 s is cleared and the call reports busy. These are the rules
  of `check_claim_push_lock_stale` and `write_claim_push_lock` (`unattended.sh:2325-2353`), so either
  writer breaks the other's stale lock. A busy lock raises `maintain — refused: a push from this git
  dir is in flight; retry once it ends: <lock>`. Observed by AC1.
- **S3** — The marker. With the lock held, `<git-dir>/push-main-active` existing raises `maintain —
  refused: push-main is landing from this git dir, so a record push now would clear its verdict files:
  <marker>`, before any object is pushed. Observed by AC2.
- **S4** — The release. `remove_push_lock(lock, token)` clears the lock only while its `owner` reads
  the caller's token, in a `finally` on every path out of the push, a raise included, as
  `remove_claim_push_lock` (`unattended.sh:2355-2359`). Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- How the push names its remote and reads the hook's verdict: TOOL-dTendedCadence-65.
- The fixture with the tracked hooks installed: TOOL-dTendedCadence-66.
- The health events `write_claim_push_lock` appends on a self-heal: drift-audit carries no health log
  (§5 risks).
- A writer in another git dir: it takes another lock, as `write_claim`'s header states
  (`unattended.sh:2324`).

### Edges

- **consumes-from** `TOOL-dTendedCadence-49` — `write_record_landing`'s push (S2), which this unit wraps in the lock and the marker test
- **hands-off** `TOOL-dTendedCadence-66` — the lock and the marker refusal, whose cases that unit's fixture plants with the tracked hooks installed
- **hands-off** `TOOL-dTendedCadence-65` — the held lock, inside which that unit clears the refusal file and pushes

## 4. Design

```
write_record_landing(...):
    lock  = <git-dir>/claim-push.lock ; token = "<pid>.<random>"
    write_push_lock(lock, token)            busy  -> raise (S2)
    try:
        <git-dir>/push-main-active exists   -> raise (S3)
        build, clear the refusal file, push (unit 49, TOOL-dTendedCadence-65)
    finally:
        remove_push_lock(lock, token)       (S4)
```

The lock comes first and the marker test second, as `write_claim` orders them, because `push-main.sh`
touches its marker first and then waits for no live lock (`check_claim_push_clear`,
`tools/push-main.sh:304-318`); whichever side moves second sees the other. The lander reads only
`until` (`push-main.sh:308-310`), so the deadline written must be the real one: the push's 30 s bound
plus 10, as `write_claim_push_lock` writes `REMOTE_BOUND + 10` (`unattended.sh:2347`).

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `write_push_lock` | function, `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `check_push_lock_stale` | function, `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `remove_push_lock` | function, `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1 to S4
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **Call `unattended.sh`'s helpers.** drift-audit is copy-installed and an adopter may not carry the
  unattended kit; the lock is a directory protocol, so a port reads and writes the same bytes.
- **Test the marker only.** The marker test can pass a moment before the lander clears its verdict
  files; the lock closes that window (TOOL-aGraftedHelix-36 S10, cited at `unattended.sh:2381-2385`).

## 5. Production-readiness checklist

- security — deny by default: no lock, or a lander's marker, means no push.
- perf / scale — two `mkdir` calls and two small writes per record push.
- error / empty / loading states — busy and marker each raise with their line, so the walk exits 1
  and the lease is handed over (unit 49 S4); the lock is released on every path.
- observability — each refusal names the lock or the marker path.
- risks — the self-heal writes no health event, a `ponytail:` ceiling: drift-audit has no health log,
  and the upgrade is a line on the walk's own output. A host clock stepped forward breaks a live lock,
  the limit `write_claim`'s header states (`unattended.sh:2322-2323`).
- testing — the criteria of §6, in the arm of §7.
- migration — N/A — no record push exists at base.
- user docs — N/A — the guard is internal; the page names no lock.

## 6. Acceptance criteria

The fixture is TOOL-dTendedCadence-49's scratch repository with its bare remote, as
TOOL-dTendedCadence-66 installs the tracked hooks in it.

- **AC1** — When `write_record_landing` runs with a directory `claim-push.lock` planted in the
  fixture's git dir, its `until` an epoch 60 s ahead, it raises naming the lock and `git -C <bare>
  for-each-ref refs/gov/` prints nothing; with `until` 60 s past, it breaks the lock, pushes, and the
  lock directory is absent afterwards; after a run whose push is made to fail, the lock directory is
  absent too.
  Red when: a live lock is ignored, a stale one wedges every wake, or a raise leaves the lock behind.
- **AC2** — When `write_record_landing` runs with `push-main-active` planted in the fixture's git dir,
  it raises naming the marker, no ref is pushed, and the lock directory is absent afterwards.
  Red when: a record push proceeds while the lander lands.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · a planted live lock, a planted stale lock, a failing push and a planted lander marker, staged against a push that tests neither · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 5 (HIGH, item H2) of the round-1 spec
  audit of units 49 to 59.

## 10. Reuse audit

The seam is the claim-push lock protocol, `write_claim_push_lock`, `check_claim_push_lock_stale` and
`remove_claim_push_lock` (`tools/unattended/unattended.sh:2305-2359`), and the lander's wait that reads
its `until` (`check_claim_push_clear`, `tools/push-main.sh:304-318`). This unit ports the protocol
to Python, same bytes on disk, because the copy-installed kit cannot call the shell helpers; it is the second
writer of one directory protocol, not a second protocol. `python tools/codebase-map/reuse_lookup.py
"take a lock before pushing from a git dir"` ranked name stems only (`git`, `before`,
`resolve_kit_dir`, `run_git`), no Python lock writer. A grep for `claim-push.lock` or
`push-main-active` over `tools` and `.githooks` names `push-main.sh`, `unattended.sh`, the pre-push
hook, their tests, the hook's bar selftest and the unattended README, and no Python writer of the
lock, so no existing seam fits beyond the protocol.

Recall terms used: `python tools/memory-recall/query.py "how does a push from a governed git dir avoid
clearing the lander's verdict files" --terms "claim-push lock push-main-active marker verdict files
pre-push refusal lander write_claim stale break"`
