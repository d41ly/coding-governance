---
name: unattended
description: Start, resume, or close a run that will merge and push with NO owner turn between start and finish. Use when the owner has committed a standing mandate for a build and wants it carried to landing unattended, when a previous unattended run needs resuming after compaction or process death, or when one needs closing. Do NOT use for ordinary work where the explicit ask before a merge and a push still applies — that is the default, and this skill is the narrow exception to it.
---

# Unattended runs

The binding contract is `{{MEMORY_ROOT}}/guides/UNATTENDED-PROTOCOL.md`. This is the operating
summary; where they differ, the protocol wins and the difference is a bug in this render.

**The one thing to understand first.** An unattended run does not remove the checkpoint before a
merge and a push — it REPLACES it with something a machine can check. If the replacement is not
checkable, the run is not unattended, it is unsupervised. Everything below exists to keep that
distinction real.

## Start a run

1. **Find the mandate. Do not write one.** The owner authors a mandate block in the build's run-state
   file and commits it BEFORE the run starts. If there is none, stop and say so — a mandate you
   wrote authorizes nothing, and the preflight will refuse it anyway by comparing against the pinned
   BASE.
2. **Schedule the keepalive yourself.** This is your half and no script can do it: the scheduling
   store is in-memory and session-scoped, reachable only through your own tool calls. Use
   `{{KEEPALIVE_CREATE}}`. Keep the id it returns.
3. **Preflight**, handing over that id:

   ```bash
   bash {{KIT_DIR}}/unattended.sh --preflight <slug> --keepalive-id <id>
   ```

   It refuses on a dirty tree, on the default branch, on an unwired repo, on an absent or edited
   mandate, and when a second run is already live. It writes nothing until every one of those
   passes. Read the refusal it prints — each one names itself.

## While it runs

- Keep the phase honest, and give every phase claim a WITNESS — a sha, a tag, a run id. A claim with
  no witness is skipped by the oracle that would have judged it, so an unwitnessed phase is the
  cheapest possible lie and you are the only author of that field.
- Park what you refuse to decide, with the question, the options you saw, and why you refused. A
  bare "parked" is indistinguishable from "forgotten", and the wrap-up is where the owner gets the
  turn you did not take.
- Check yourself with `bash {{KIT_DIR}}/unattended.sh --status <slug>`.

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
discards the entire bar the mandate leaned on, and the gate greps your run-state file for the flag.

## Reap

Delete the keepalive with `{{KEEPALIVE_DELETE}}` before you finish. Nothing else can: when your
process exits, an unreaped job is orphaned in a store no later run can see.
