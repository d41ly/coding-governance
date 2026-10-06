---
name: unattended
description: Start, resume, or close a run that will merge and push with NO owner turn between start and finish. Use when the owner wants a committed build carried to landing unattended, when a previous unattended run needs resuming after compaction or process death, or when one needs closing. Do NOT use for ordinary work where the explicit ask before a merge and a push still applies — that is the default, and this skill is the narrow exception to it.
---
<!-- gov:kit unattended@1.88 -->

# Unattended runs

The contract is `memory/guides/UNATTENDED-PROTOCOL.md` with
`memory/guides/UNATTENDED-VERBS.md`. This Skill is a ROUTER: pick a path below, then follow
its steps in that verbs file's section `The paths, in order`, which wins any difference. Every
`unattended.sh` here is `bash tools/unattended/unattended.sh`.

## Before any path — schedule the idle-wake NOW

First act, before orienting: `CronCreate` at every 10 minutes (cron 3-59/10 * * * *); keep the id. Each tick
runs `unattended.sh --resume <slug> --keepalive-id <id>`, then `unattended.sh --audit <slug>`. A
background task's starter runs `unattended.sh --register-task <slug> --task <name> --heartbeat <path>`,
later `unattended.sh --release-task <slug> --task <name>`. Readers share
`unattended.sh --liveness <slug>`. A run that never starts still reaps it.

## Which path

A value mixing a slug and ids is refused before any verb.

| You were handed | Path | Declares |
|---|---|---|
| a build folder naming its units, or carrying `asks:` | Start a run | `slug` |
| prose or a prompt file, as `--prompt <value>`, no build folder | Start a run from a PROMPT | `prompt` |
| an existing PLAYBOOK and a number of pieces | Start a PLAYBOOK run | `recipe` |
| a topic and no playbook, handed the same way | Author a PLAYBOOK | `prompt` |
| ids, a prompt naming ids, or a FILING HOME's slug | Ids go through the scaffold | nothing: the OWNER lands the README |

## Start a run

0. **Read `memory/guides/BUILD-METHOD.md` WHOLE, before anything else.** Each directive
   binding this run names a rule and the section of it stating the rule:

| Handle | What it names | Carrier | Scope | From |
|---|---|---|---|---|
| `minimal-prose` | the transcript rule under a mandate | M10 | all | D1 |
| `sub-specced` | one mechanism per spec, and sub-spec agreement | M2 | all | D2 |
| `forks-resolved` | when open questions are settled | M3 | all | D3 |
| `specs-reviewed` | the spec audit that precedes code, when the build or its project declares it | M4 | all | D4 |
| `reuse-first` | the recall and reuse obligation | M5 | all | D5 |
| `parallel-when-disjoint` | the parallelism obligation | M6 | all | D6 |
| `passes-committed` | the commit boundary | M6 | all | D8 |
| `diff-reviewed` | the closing review of the cumulative diff | M8 | all | D7 |
| `land-once-done` | when a build may land | M8 | all | D8 |
| `conflicts-reconciled` | merge-conflict disposition | M8 | all | D8 |
| `wrap-up-derived` | how the wrap-up is composed | M9 | all | D8 |
| `discoveries-adopted` | a beneficial discovery joins the running build, decided at once | M10 | all | D12 |
| `passes-harnessed` | M6's pass sequence, DRIVEN as one program per protocol section 12 | M6 | all | D13 |
| `researched` | the candidate search when no seam fits | M12 | all | D9 |
| `solution-tested` | testing candidates before the pick | M12 | all | D10 |
| `playbook-followed` | the pass loop and its regrounding rule | M7 | recipe | D11 |
| `pieces-recorded` | the wrap-up derivation, over the pieces | M9 | recipe | D11 |

   **`Scope`**: `all` binds every run; a mode binds only a run whose README declared that
   `authorized-by:` value, and waiving its handle on another mode's run is REFUSED.
1. The build folder authorizes at this project's anchor, `published`; read it, it is the roster.
2. Only if a handle to waive was named: ONE `AskUserQuestion`, default-deny.
3. **Preflight:** `bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id <id>`, plus
   `--waive <handle> --reason "<why>"` per confirmed pair. Keep its spec-audit line.
4. Then `/session-kickoff`, if the project ships it — after preflight, never before.
5. A README carrying `asks:`: read `memory/guides/UNATTENDED-ASKS.md` whole first.
6. A pre-flip BASE is parked with `tools/memory-tree/migrate_backlog.py --recipe`, never relocated.

## Ids go through the scaffold

`unattended.sh --preflight "<the value>" --keepalive-id <id>` refuses and prints the
scaffold recipe: relay it to the owner verbatim, reap the keepalive, and stop.

## Start a run from a PROMPT

Only when the invocation carries `--prompt`, and only under the `published` anchor; this
project declares `published`. A prompt naming ids takes the scaffold route.

1. **Orient from the prose**; RUN the orientation probes before step 3.
2. **Decide whether to ask, ONCE**: One `AskUserQuestion`, every gap in it.
3. **Write the build folder**, `memory/builds/<slug>/README.md`, with `authorized-by: prompt`.
4. **Commit, then PUSH THE BRANCH.** In that order.
5. **Preflight**, as on the slug path.
6. **The kickoff hand-back**, at the slug path's step 4.

## Start a PLAYBOOK run

For declared content, and there is no machine half to that limit: an ordinary code build takes the
slug or the prompt path. Record each piece and the set:
`unattended.sh --record-piece <slug> --path <piece> --leg <name> --verdict PASS|FAIL|NA` and
`unattended.sh --record-set <slug> --leg <name> --verdict PASS`.

## Author a PLAYBOOK — creation, and owner-instructed amendment

The prompt path: write from `memory/guides/PLAYBOOK-TEMPLATE.md`, validate with
`bash tools/unattended/check-playbook.sh`, and land it before the run that follows it.

## Produce pieces ATTENDED

Not a run: the same two record verbs, with `-` for the slug and `--records-root <root>`.

## While it runs

- **A process not in the ledger is never killed**, whatever its command line says: it is reported
  and left to a person, never killed by name, age or spin rate (`UNATTENDED-STOPS.md` §14).
- No merge bar and no self-test suite inside a pass.

```bash
unattended.sh --phase <slug> BUILDING --witness $(git rev-parse HEAD)
unattended.sh --park <slug> --item "<the question>" --reason "<options, and why refused>"
unattended.sh --propose <slug> --item "<amendment>" --step "<step>" --reason "<why>"
unattended.sh --brief <slug> --unit <unit-id> --path <the brief file>
unattended.sh --rescope <slug> --act retire|supersede|add|defer --item <unit-id> --reason "<why>"
unattended.sh --dispatch <slug> --pass <unit-id> --writes <path> --writes <path>
unattended.sh --plan <slug> --paths
unattended.sh --status <slug>
unattended.sh --claims  # RUN_CLAIMS on
unattended.sh --beat <slug>
unattended.sh --review <slug> --subject <id-or-slug> --verdict <verdict> --blockers <N>
python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD
```

A pass commit's `Pass: <unit-id>` trailer is graded by `unattended.sh --check-commit "$1"`. Drive by
`scriptPath`: `tools/workflows/unattended-build.js`, then `tools/workflows/unattended-unit.js`.

## Resume

`unattended.sh --status <slug>`, then `unattended.sh --resume <slug> --keepalive-id <id>`. A take-over
reaps with `CronDelete` before scheduling, and runs `delete_scheduled_task` only after.

## Close

`unattended.sh --phase <slug> VERIFYING --witness <sha>`, commit, then `unattended.sh --close <slug>`,
under `in-place` after `bash tools/push-main.sh --prepare --slug <slug>` and
`unattended.sh --authorization <slug>`. Attest with `unattended.sh --attest <slug> --item keepalive-reaped|parked-decisions-surfaced`.

**TWO items have NO override, and this is where you will meet them: `authorization-reachable` and
`pieces-complete`.** An override on the
authorization check IS the authorization check, so the verb refuses the pair rather than recording
it; and `pieces-complete` is the item saying a recipe-mode run produced what the owner asked for over
content nothing else on the bar can grade, so an override on it is the run certifying its own output.

**A `hold ·` line from `gates-green` is your next step, whatever its code.** The item prints one
when the bar ended for a reason that is not this run's to fix: `host-degraded` until `probe gate`
when the bar was killed at its backstop before it acquired the repository, `host-degraded` until
`probe host` when the runner exited HOST, and `inherited-red` until `probe gate` for an inherited red
the policy parks. Take it in this order: commit the staged records, which carry the `gates-run` fact
and any ask the item filed; push the branch; reap the keepalive; then run `--hold` with the code and
the condition the line names, its reason, and `--reaped <id>`. `--hold` refuses a dirty tree, and
under `ANCHOR_SCOPE=published` an unpublished tip, so it comes last. When that branch push fails
because the remote answers nothing at all, take the hold as `platform-unavailable` instead, the one
code `--hold` accepts over an unpublished tip.

Other blocked items: `unattended.sh --close <slug> --override <item> --reason "<why>"`, per item.

## Record the run

`python tools/runlog/runlog.py record <slug> --write`, where that file exists.

## Land

Under `primary`, `bash tools/push-main.sh`; under `in-place`, after the close's `--prepare`,
`bash tools/push-main.sh --land --slug <slug>`. Never with a hook-bypass flag.

## Mark it landed

After the lander returns; the run is not finished until you do:

```bash
unattended.sh --landed <slug>
unattended.sh --version   # which kit build
```

## If it cannot continue YET — hold it

`unattended.sh --hold <slug> --code <code> --until <cond> --reason "<why>" --reaped <id>`, then file
the restart it prints: `delete_scheduled_task`, then `create_scheduled_task`.

## Hand it off

Sound work the owner lands or decides:
`unattended.sh --handoff <slug> --code owner-landing|owner-decision --reason "<why>" --reaped <id>`,
never `--abort` (DISCARD). Once landed: `unattended.sh --settle <slug>`.

## If it cannot finish

`unattended.sh --abort <slug> --code <halt-code> --reason "<what stopped it>"`

## Reap

`CronDelete` the idle-wake before you finish, and attest `keepalive-reaped`.
