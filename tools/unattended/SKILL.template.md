---
name: unattended
description: Start, resume, or close a run that will merge and push with NO owner turn between start and finish. Use when the owner wants a committed build carried to landing unattended, when a previous unattended run needs resuming after compaction or process death, or when one needs closing. Do NOT use for ordinary work where the explicit ask before a merge and a push still applies — that is the default, and this skill is the narrow exception to it.
---

# Unattended runs

The binding contract is `{{MEMORY_ROOT}}/guides/UNATTENDED-PROTOCOL.md`. This is the operating
summary; where they differ, the protocol wins and the difference is a bug in this render.

**The one thing to understand first.** An unattended run does not remove the checkpoint before a
merge and a push — it REPLACES it with something a machine can check. If the replacement is not
checkable, the run is not unattended, it is unsupervised. Everything below exists to keep that
distinction real.

## Start a run

0. **Read the build method first, if this project ships one:** `{{MEMORY_ROOT}}/guides/BUILD-METHOD.md`.
   It is the memory-tree kit's, not this one's, so it may be absent — that is legal, and this kit
   states none of what it carries.
1. **The build folder IS the authorization — you do not write one, and neither does the owner.** A
   `{{MEMORY_ROOT}}/builds/<slug>/README.md` committed before your branch existed is the whole
   precondition. Preflight refuses a build folder you created, because a run that authorizes itself
   has no authorization. You also do not create the run-state file: preflight does that.
2. **Schedule the keepalive yourself.** This is your half and no script can do it: the scheduling
   store is in-memory and session-scoped, reachable only through your own tool calls. Use
   `{{KEEPALIVE_CREATE}}`, at the cadence this project declares — {{KEEPALIVE_INTERVAL}}. Keep the
   id it returns.
3. **Preflight**, handing over that id:

   ```bash
   bash {{KIT_DIR}}/unattended.sh --preflight <slug> --keepalive-id <id>
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
- Check yourself with `bash {{KIT_DIR}}/unattended.sh --status <slug>`.

## While the work runs

Move the phase as each pass ends, and give it a witness. The members are named for the build method's
pass kinds, so the run's position and the pass it is performing are one vocabulary rather than two:

```bash
bash {{KIT_DIR}}/unattended.sh --phase <slug> BUILDING --witness $(git rev-parse HEAD)
```

Ask what is left instead of re-reading prose for it:

```bash
bash {{KIT_DIR}}/unattended.sh --plan <slug>
```

It prints each tracked spec's id, status and classification, and names the next unit. It cannot see a
planned unit that has no spec yet, and says so on every run rather than printing a complete-looking
list.

## Resume

```bash
bash {{KIT_DIR}}/unattended.sh --resume <slug>
```

Read the run-state file before doing anything else. It survived compaction and process death; your
context did not.

## Close

```bash
bash {{KIT_DIR}}/unattended.sh --close <slug>
```

It BLOCKS on any unmet Definition-of-Done item. Two of them are yours to attest, because no script
can observe them: that you reaped the keepalive (`{{KEEPALIVE_DELETE}}`), and that every parked
decision reached the wrap-up. Record them honestly — attestation is not a machine verdict, and the
gate says so wherever it reports them.

If you must override a blocked item, name it and give a reason:

```bash
bash {{KIT_DIR}}/unattended.sh --close <slug> --override <item> --reason "<why>"
```

The override is written into the run-state file as a parked entry and surfaces in the wrap-up. An
override nobody can read afterwards is just a skipped check.

## Land

```bash
{{LANDER}}
```

Never with a hook-bypass flag. The lander is mandatory because it reconciles the remote BEFORE the
gate, so the bar never runs on an already-stale tree. If it refuses, read why and fix it — bypassing
discards the entire bar the authorization leaned on, and the gate greps your run-state file for the flag.

## Mark it landed — the run is not finished until you do

```bash
bash {{KIT_DIR}}/unattended.sh --landed <slug>
```

**Run this AFTER the lander returns, not before.** It re-observes the remote and refuses unless HEAD
is an ancestor of the tip the remote advertises, so it is the one phase claim you cannot simply
assert — which is the point. Then commit the record it writes and land that commit too; until it is
committed, every later run still counts yours as live and the bar reds on the second one.

`--close` moves you to `LANDING`, and nothing else may: a phase move into it would claim the
Definition of Done was evaluated without evaluating it.

## If it cannot finish

```bash
bash {{KIT_DIR}}/unattended.sh --abort <slug> --reason "<what stopped it, and what you refused to decide>"
```

The reason is required and lands in the parked region, because an abort with no recorded reason is
indistinguishable from a run that simply stopped. You still owe both attestations first — reap the
keepalive and surface the parked decisions — since an aborted run orphans exactly the same job and
leaves exactly the same decisions unseen. An abort does not merge and does not push.

## Reap

Delete the keepalive with `{{KEEPALIVE_DELETE}}` before you finish. Nothing else can: when your
process exits, an unreaped job is orphaned in a store no later run can see.
