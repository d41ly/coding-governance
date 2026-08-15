---
name: unattended
description: Start, resume, or close a run that will merge and push with NO owner turn between start and finish. Use when the owner wants a committed build carried to landing unattended, when a previous unattended run needs resuming after compaction or process death, or when one needs closing. Do NOT use for ordinary work where the explicit ask before a merge and a push still applies — that is the default, and this skill is the narrow exception to it.
---

# Unattended runs

The binding contract is `memory/guides/UNATTENDED-PROTOCOL.md`. This is the operating
summary; where they differ, the protocol wins and the difference is a bug in this render.

**The one thing to understand first.** An unattended run does not remove the checkpoint before a
merge and a push — it REPLACES it with something a machine can check. If the replacement is not
checkable, the run is not unattended, it is unsupervised. Everything below exists to keep that
distinction real.

## Start a run

0. **Read `memory/guides/BUILD-METHOD.md` WHOLE, before anything else.** Not conditionally.
   Every directive below is a POINTER into a section of that file, so a run that has not read it is
   bound by a set that resolves to nothing. `--preflight` refuses a tree where it is absent.

   **The directives this run is bound by.** Each NAMES a rule and points at the section that states
   it; none of them restates one, and a cell here that grew into a rule would be a defect in this
   table rather than a second source of truth.

   | Handle | What it names | Carrier | From |
   |---|---|---|---|
   | `minimal-prose` | the transcript rule under a mandate | M10 | D1 |
   | `sub-specced` | one mechanism per spec, and sub-spec agreement | M2 | D2 |
   | `forks-resolved` | when open questions are settled | M3 | D3 |
   | `specs-reviewed` | the spec audit that precedes code | M4 | D4 |
   | `reuse-first` | the recall and reuse obligation | M5 | D5 |
   | `parallel-when-disjoint` | the parallelism default under a mandate | M6 | D6 |
   | `passes-committed` | the commit boundary | M6 | D8 |
   | `diff-reviewed` | the closing review of the cumulative diff | M8 | D7 |
   | `land-once-done` | when a build may land | M8 | D8 |
   | `conflicts-reconciled` | merge-conflict disposition | M8 | D8 |
   | `wrap-up-derived` | how the wrap-up is composed | M9 | D8 |

   Two rows carry a consequence worth knowing before you waive them. **`reuse-first` — recommend
   against.** Waiving it is SILENT: the bar stays green over a build that skipped the reuse probes,
   because nothing machine-checks a spec's reuse section for content. A waived run's spec §10 must
   NAME the waiver, or the skip leaves no trace at all. **`land-once-done`** — waiving it does not
   remove the Definition-of-Done item that observes completeness; that still owes an override at
   close.
1. **The build folder IS the authorization — you do not write one, and neither does the owner.** A
   `memory/builds/<slug>/README.md` committed before your branch existed is the whole
   precondition. Preflight refuses a build folder you created, because a run that authorizes itself
   has no authorization. You also do not create the run-state file: preflight does that.
2. **Schedule the keepalive yourself.** This is your half and no script can do it: the scheduling
   store is in-memory and session-scoped, reachable only through your own tool calls. Use
   `CronCreate`, at the cadence this project declares — every 10 minutes (cron 3-59/10 * * * *). Keep the
   id it returns.
3. **Preflight**, handing over that id:

   ```bash
   bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id <id>
   ```

   It refuses on a dirty tree, on the default branch, on an unwired repo, when the build README is
   absent at the pinned BASE or does not name this build, when the remote does not answer or
   advertises no default branch of its own, and when a second run is already live. It writes nothing until every one of those
   passes. Read the refusal it prints — each one names itself.

## While it runs

- Keep the phase honest, and give every phase claim a WITNESS — a sha, a tag, a run id. A claim with
  no witness is skipped by the oracle that would have judged it, so an unwitnessed phase is the
  cheapest possible lie and you are the only author of that field.
- Park what you refuse to decide, with the question, the options you saw, and why you refused. A
  bare "parked" is indistinguishable from "forgotten", and the wrap-up is where the owner gets the
  turn you did not take.
- Check yourself with `bash tools/unattended/unattended.sh --status <slug>`.

## While the work runs

Move the phase as each pass ends, and give it a witness. The members are named for the build method's
pass kinds, so the run's position and the pass it is performing are one vocabulary rather than two:

```bash
bash tools/unattended/unattended.sh --phase <slug> BUILDING --witness $(git rev-parse HEAD)
```

Ask what is left instead of re-reading prose for it:

```bash
bash tools/unattended/unattended.sh --plan <slug>
```

It prints each tracked spec's id, status and classification, and names the next unit. It cannot see a
planned unit that has no spec yet, and says so on every run rather than printing a complete-looking
list.

## Resume

```bash
bash tools/unattended/unattended.sh --resume <slug>
```

Read the run-state file before doing anything else. It survived compaction and process death; your
context did not.

## Close

```bash
bash tools/unattended/unattended.sh --close <slug>
```

It BLOCKS on any unmet Definition-of-Done item. Two of them are yours to attest, because no script
can observe them: that you reaped the keepalive (`CronDelete`), and that every parked
decision reached the wrap-up. Record them honestly — attestation is not a machine verdict, and the
gate says so wherever it reports them.

If you must override a blocked item, name it and give a reason:

```bash
bash tools/unattended/unattended.sh --close <slug> --override <item> --reason "<why>"
```

The override is written into the run-state file as a parked entry and surfaces in the wrap-up. An
override nobody can read afterwards is just a skipped check.

**The pair REPEATS — one `--override <item> --reason <text>` per unmet item.** Two unmet items need
two pairs in one invocation, and a reason belongs to the flag that precedes it. This matters because
you are the only reader: supplying one pair for two unmet items leaves the second overridden on a
reason written about the first, and the close records that as a decision somebody made.

## Land

```bash
bash tools/push-main.sh
```

Never with a hook-bypass flag. The lander is mandatory because it reconciles the remote BEFORE the
gate, so the bar never runs on an already-stale tree. If it refuses, read why and fix it — bypassing
discards the entire bar the authorization leaned on, and the gate greps your run-state file for the flag.

## Mark it landed — the run is not finished until you do

```bash
bash tools/unattended/unattended.sh --landed <slug>
```

**Run this AFTER the lander returns, not before.** It re-observes the remote and refuses unless HEAD
is an ancestor of the tip the remote advertises, so it is the one phase claim you cannot simply
assert — which is the point. Then commit the record it writes and land that commit too; until it is
committed, every later run still counts yours as live and the bar reds on the second one.

`--close` moves you to `LANDING`, and nothing else may: a phase move into it would claim the
Definition of Done was evaluated without evaluating it.

## If it cannot finish

```bash
bash tools/unattended/unattended.sh --abort <slug> --reason "<what stopped it, and what you refused to decide>"
```

The reason is required and lands in the parked region, because an abort with no recorded reason is
indistinguishable from a run that simply stopped. You still owe both attestations first — reap the
keepalive and surface the parked decisions — since an aborted run orphans exactly the same job and
leaves exactly the same decisions unseen. An abort does not merge and does not push.

## Reap

Delete the keepalive with `CronDelete` before you finish. Nothing else can: when your
process exits, an unreaped job is orphaned in a store no later run can see.
