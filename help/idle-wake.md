# The idle-wake's `--wake` tick

**What it is.** An unattended run schedules an idle-wake job as its first act, and each time the
job fires the session runs one cheap verb of the unattended driver, `tools/unattended/unattended.sh`:
`--wake`. It prints one line saying whether the two costly acts, `--resume` and then `--audit`, would
find anything to do. On `HEALTHY` the session ends its turn. On `FULL` it runs both acts exactly as
before. The same line names the cadence the job should run at.

The verbs' full reference is `memory/guides/UNATTENDED-VERBS.md`, section "Before any path — the
idle-wake". This page anchors the verb for [the docs leg](docs-leg.md).

## Running it

`--wake <slug> --keepalive-id <id>` prints one line and exits 0 on either verdict. It writes nothing to the run's record or worktree. <!-- usage: verb:unattended.sh:--wake ef8efa49 -->

```text
unattended-wake: <slug> · HEALTHY · tasks <n> open · cadence <cadence>
unattended-wake: <slug> · FULL · <reason> · tasks <n> open · cadence <cadence>
```

It refuses with exit 1 for a malformed slug, a missing `--keepalive-id` (check 112) and a missing
run-state file (check 10), and exits 2 for a malformed `TASK_STALL_BOUND`, as `--audit` does.

## What `FULL` means

The reason is the first condition that holds, in the order `--resume` takes its own rows:

| Reason | Holds when |
|---|---|
| `phase <p>` | the recorded phase is absent, terminal, `HELD` or `LANDING` |
| `abandoned` | the record carries an `abandoned` fact |
| `asks moved` | the build README's `asks:` line moved since the run pinned it |
| `worktree` | this worktree is not on the run's branch |
| `holder` | `--keepalive-id` is not the record's keepalive |
| `lease` | the lease is not this harness's session and pid |
| `claims unread` | `RUN_CLAIMS` is `on` and the claims could not be read |
| `claim` | `RUN_CLAIMS` is `on` and the holder's claim is due a write, or another session holds it |
| `orphans` | the process ledger names an orphan |
| `clock probe` | a tree clock answered nothing |
| `tree idle` | the newest commit and the newest write are both older than `UNIT_STALL_BOUND` |
| `task probe` | a registered task's heartbeat could not be read |
| `task stalled` | a registered task's heartbeat is older than `TASK_STALL_BOUND` |

Each condition is sufficient, not necessary: a `FULL` can meet a pair that finds nothing to do,
which costs a tick's time and never a verdict. `HEALTHY` holds only when no row does.

## The cadence

`tasks <n> open` counts the registered tasks (`--register-task`) not yet released, or reads
`unknown` when a heartbeat could not be read. The cadence is `KEEPALIVE_INTERVAL` from
`.unattended.conf`, the cadence the run's first act schedules the job at, or `undeclared` when that
is blank. The task count does not move it.

## Example

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
```bash
bash tools/unattended/unattended.sh --wake aBuild --keepalive-id k1
# unattended-wake: aBuild · HEALTHY · tasks 1 open · cadence every 10 minutes (cron 3-59/10 * * * *)
```
