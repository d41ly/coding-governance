# TOOL-dSafePassage-31 — the write lock records its holder's pid namespace, and a holder from another namespace reads unknown

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 7 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-31-deviation-77.md](../build/2026-10-23-build-TOOL-dSafePassage-31-deviation-77.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-32 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 15 to 26
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md`)
confirmed finding **id 13** at HIGH, its item **D-4**. TOOL-dSafePassage-26 S33 keys the lock's
namespace on `platform` and the kernel's `boot_id` (its §4 "Data model", the lock record). Every WSL2
distro and a Docker Desktop container share one kernel `boot_id` and the Windows hostname, while each
has its own pid namespace. This unit's probe on node d, 2026-10-23, read `pid:[4026532221]` from
`readlink /proc/self/ns/pid` in `wsl.exe -d Ubuntu`; the report's skeptic read `pid:[4026532244]` in
`-d docker-desktop` beside it, with one `boot_id` and the hostname `Compeeto` on both. So a run in one
distro judges a lock held from another through a census that cannot see that pid
(TOOL-dSafePassage-2 S7), reads the holder dead, and reclaims a live lock while it writes. This unit
is id 13's promotion: the lock records the identity the judgement needs, the pid namespace itself,
and a holder whose namespace differs reads `unknown`.

## 2. Scope (IN)

- **S1** — The reading. `read_pid_namespace()` in `tools/govkit/upgrade_steps.py` returns
  `os.readlink("/proc/self/ns/pid")` where that link exists, and `""` where it does not, which is
  Windows and macOS. Observed by AC1.
- **S2** — The record. `take_write_lock` (`tools/govkit/govkit.py:7409-7432` at the base) writes
  `pid_ns`, the value `read_pid_namespace` returns, beside the `host` TOOL-dSafePassage-2 S6 adds and
  the `platform` and `boot_id` TOOL-dSafePassage-26 S33 adds. Observed by AC1.
- **S3** — The verdict. `check_holder_dead` applies the rows of §4 "Data model" after
  TOOL-dSafePassage-26 S33's `platform` and `boot_id` rows and before the census. With both of those
  equal, a lock `pid_ns` that differs from this process's reads `unknown`, and so does a lock that
  carries no `pid_ns` while this process's is non-empty. Only an equal `pid_ns` goes on to the
  census test of TOOL-dSafePassage-2 S7. Observed by AC2 and AC3.
- **S4** — The plants. The `lock` family of `python3 "tools/govkit/upgrade_steps.py" fixture` gains
  `lock-foreign-pidns`, a lock carrying this process's `platform` and `boot_id` and another
  namespace's `pid_ns`, and `lock-no-pidns`, a lock carrying no `pid_ns`. Both stub the judge's own
  `read_pid_namespace` to a Linux value inside the fixture process only, so the plants run on
  Windows. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- The verdict for a differing `boot_id` on one host, and for a lock with no namespace field at all:
  finding 44, carried by the minors batch `TOOL-dSafePassage-35`, whose rows run before this unit's.
- The clock the reuse estimate reads: id 37, `TOOL-dSafePassage-32`.
- A census that can see another namespace's pids. None exists, so the judge refuses instead.

### Edges

- **consumes-from** `TOOL-dSafePassage-26` — the lock record's `platform` and `boot_id` and the namespace rows of `check_holder_dead`; without them there is no namespace test to make exact
- **hands-off** `TOOL-dSafePassage-35` — the boot and absent-field rows of the namespace verdict, which run before this unit's row
- **hands-off** `TOOL-dSafePassage-42` — finding 24 of the spec audit of units 27 to 35, the lock record keeping TOOL-dSafePassage-32's `started_boot` beside `pid_ns` in the one `take_write_lock` writer, and finding 17, AC1's WSL probe spelled with the path inside the program text

## 4. Design

### Data model

The lock record after this unit:
`{"pid", "verb", "started", "started_utc", "host", "platform", "boot_id", "pid_ns"}`, `pid_ns` the
link text `pid:[<inode>]` or `""`.

The namespace rows of `check_holder_dead`, this unit's after TOOL-dSafePassage-26 S33's:

| Lock `pid_ns` | This process's | Verdict |
|---|---|---|
| equal | equal | go on to the census test |
| non-empty, differs | any | `unknown` |
| absent or `""` | non-empty | `unknown` |
| absent or `""` | `""` | go on to the census test |

The last row is Windows and macOS, where neither side has a pid namespace to read and the platform
row has already matched.

### Inventory

Minted: `read_pid_namespace` in `tools/govkit/upgrade_steps.py` (cell `py.function`, verb `read`, OK
by `python tools/lexicon/lexicon.py --suggest read_pid_namespace --as py.function` on 2026-10-23); the
lock key `pid_ns`; the plants `lock-foreign-pidns` and `lock-no-pidns`. No conf key, gate leg or
policy key. The verdict is `unknown`, which TOOL-dSafePassage-2 S7 already refuses on, so no new
`raise Refusal` site is added and `tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

Additive. No lock carrying `platform` or `boot_id` exists before this build lands, so the only lock
without `pid_ns` is one an older govkit left after a kill; on Linux it reads `unknown` and refuses,
and the refusal's remedy names the reclaim as TOOL-dSafePassage-2 S6 prints it.

### Rollout

Live at landing. It builds at order 7, after TOOL-dSafePassage-26 (order 6), whose lock keys it
extends.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **The hostname or `boot_id` alone.** Both are shared across the namespaces that matter here, as the
  probe shows.
- **Reading an absent `pid_ns` on Linux as equal.** An older lock from another distro would then be
  judged by a census that cannot see its pid, the hole this unit closes.

## 5. Production-readiness checklist

- security: the reclaim refuses more, never less; no new write path.
- perf / scale: one `readlink` per take and per judgement.
- error / empty / loading states: a `readlink` that fails where the link exists reads `""` only on a
  platform without the link; on Linux an `OSError` is a refusal naming the path.
- observability: the refusal describes the holder as TOOL-dSafePassage-2 S6 prints it, its `pid_ns`
  among the fields.
- risks: a lock left on Linux by a govkit older than this build refuses until an operator clears it;
  that is the cost of never reclaiming a live lock across namespaces.
- testing: the two plants, through §7.
- migration: §4 "Migration".
- user docs: N/A — no operator-visible verb or message changes beyond the holder line.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-dead` runs on
  node d, the lock the take writes carries `pid_ns` as `""`, and a `python -c` probe of
  `read_pid_namespace` under `wsl.exe -d Ubuntu` prints a `pid:[<digits>]` value.
  Red when: the record omits the key, or the reading returns a value off Linux.
  fixture: the WSL half needs a WSL distro on the node; node d has `Ubuntu` and `docker-desktop`
  (read 2026-10-23).
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture lock --plant lock-foreign-pidns`
  runs, the take refuses with the holder `unknown`, the lock file is unchanged, and the run exits 1.
  Red when: a lock whose `pid_ns` differs is judged by the census and reclaimed.
- **AC3** — When the same family runs with `--plant lock-no-pidns`, the take refuses with the holder
  `unknown` and exits 1; with the judge's stub removed, so this process's `pid_ns` is `""`, the plant
  is judged by the census as TOOL-dSafePassage-2's `lock-dead` is, and reclaims.
  Red when: an absent `pid_ns` reads as equal on a Linux judge, or as unknown off Linux.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 AC3 · the self-test calls `upgrade_steps.py fixture lock` with the two plants, its failing case staged by a judge copy that skips the `pid_ns` row · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit of units 15 to 26's
  id 13 (HIGH, item D-4).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-42`; no other section moved.

## 10. Reuse audit

The seam extended is the write lock's record and judge: `take_write_lock`
(`tools/govkit/govkit.py:7409-7432`), TOOL-dSafePassage-2's `check_holder_dead` and
TOOL-dSafePassage-26 S33's namespace rows, the last two specced and unbuilt at the base.
`python tools/codebase-map/reuse_lookup.py "pid namespace identity of a lock holder"` ranked
`holder`, `check_pid_alive` and `read_pid_image` (`tools/unattended/lib-unattended.sh`), none of
which reads a namespace, so no existing seam fits beyond the lock itself.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
