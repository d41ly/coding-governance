---
name: unattended
description: Start, resume, or close a run that will merge and push with NO owner turn between start and finish. Use when the owner wants a committed build carried to landing unattended, when a previous unattended run needs resuming after compaction or process death, or when one needs closing. Do NOT use for ordinary work where the explicit ask before a merge and a push still applies — that is the default, and this skill is the narrow exception to it.
---
<!-- gov:kit unattended@1.7 -->

# Unattended runs

The binding contract is `{{MEMORY_ROOT}}/guides/UNATTENDED-PROTOCOL.md`. This is the operating
summary; where they differ, the protocol wins and the difference is a bug in this render.

**The one thing to understand first.** An unattended run does not remove the checkpoint before a
merge and a push — it REPLACES it with something a machine can check. If the replacement is not
checkable, the run is not unattended, it is unsupervised. Everything below exists to keep that
distinction real.

## Start a run

0. **Read `{{MEMORY_ROOT}}/guides/BUILD-METHOD.md` WHOLE, before anything else.** Not conditionally.
   Every directive below is a POINTER into a section of that file, so a run that has not read it is
   bound by a set that resolves to nothing. `--preflight` refuses a tree where it is absent.

   **The directives this run is bound by.** Each NAMES a rule and points at the section that states
   it; none of them restates one, and a cell here that grew into a rule would be a defect in this
   table rather than a second source of truth.

   | Handle | What it names | Carrier | Scope | From |
   |---|---|---|---|---|
   | `minimal-prose` | the transcript rule under a mandate | M10 | all | D1 |
   | `sub-specced` | one mechanism per spec, and sub-spec agreement | M2 | all | D2 |
   | `forks-resolved` | when open questions are settled | M3 | all | D3 |
   | `specs-reviewed` | the spec audit that precedes code | M4 | all | D4 |
   | `reuse-first` | the recall and reuse obligation | M5 | all | D5 |
   | `parallel-when-disjoint` | the parallelism default under a mandate | M6 | all | D6 |
   | `passes-committed` | the commit boundary | M6 | all | D8 |
   | `diff-reviewed` | the closing review of the cumulative diff | M8 | all | D7 |
   | `land-once-done` | when a build may land | M8 | all | D8 |
   | `conflicts-reconciled` | merge-conflict disposition | M8 | all | D8 |
   | `wrap-up-derived` | how the wrap-up is composed | M9 | all | D8 |
   | `researched` | the candidate search when no seam fits | M12 | prompt | D9 |
   | `solution-tested` | testing candidates before the pick | M12 | prompt | D10 |

   **`Scope`** is which runs a directive binds. `all` binds every unattended run; `prompt` binds only
   a run whose build README declared `authorized-by: prompt`, because research and a solution test
   are obligations of a build whose solution was not given. A waiver of a `prompt`-scoped handle is
   REFUSED on a slug-authorized run rather than recorded, since it would relax a rule that never
   bound it.

   Two rows carry a consequence worth knowing before you waive them. **`reuse-first` — recommend
   against.** Waiving it is SILENT: the bar stays green over a build that skipped the reuse probes,
   because nothing machine-checks a spec's reuse section for content. A waived run's spec §10 must
   NAME the waiver, or the skip leaves no trace at all. **`land-once-done`** — waiving it does not
   remove the Definition-of-Done item that observes completeness; that still owes an override at
   close.
1. **The build folder IS the authorization, and what makes it one is the ANCHOR it resolves at.** A
   `{{MEMORY_ROOT}}/builds/<slug>/README.md` that resolves at the anchor this project declares is the
   whole precondition. **This project's anchor scope is `{{ANCHOR_SCOPE}}`.**
   On the **default-branch** anchor that means committed before your branch existed, and preflight
   REFUSES a build folder you created — a run that authorizes itself has no authorization. Where the
   project declares **published**, the tip the remote advertises for your OWN branch also counts, so a
   run may author its build folder and push it; protocol section 1 states what that costs, and the
   run-state file records which anchor was used. You still do not create the run-state file:
   preflight does that.
   **If the build is not on the default branch, PUSH YOUR BRANCH FIRST.** Where the project declares
   `ANCHOR_SCOPE="published"`, a build folder that does not resolve at the merge-base is looked for
   at the tip the remote advertises for the branch you are on — so an unpushed commit authorizes
   nothing, and the refusal you would otherwise meet names the branch the remote does not advertise.
   Where the project declares nothing, or anything else, only the default-branch anchor counts and
   the build has to be landed first. This is a weaker anchor and the run-state file records which one
   authorized it; the protocol's section 1 states what it costs.
   **A build that has already been run once is not closed to you.** If its `RUN.md` reached a
   terminal phase, preflight RETIRES that record to `RUN.<phase>.<blob8>.md` beside it and starts you
   a fresh one — it says so on stdout, naming both paths. You do not move, edit or delete a finished
   record yourself; the retired bytes stay exactly as the previous run left them.
   **READ it, though — it is also the ROSTER.** M2 makes the README's authored Units table the
   roster for the whole build, and its Start-here section carries the state, the
   classification and the next action. Asserting the file as authorization and never opening
   it leaves you executing a build whose scope you have not read.
2. **If — and only if — the invocation named a directive to waive: THIS IS THE LAST OWNER TURN.**
   Skip this step entirely when no handle was named, which is the ordinary case.

   Ask **once**, with a single `AskUserQuestion` covering every named handle together. Not one call
   per handle: the owner is trying to walk away, and a three-round conversation at that moment is
   the thing this whole kit exists to remove. More than four handles go in groups of four, because
   that is the call's own limit.

   **DEFAULT-DENY. A handle named on the invocation line but not confirmed WITH A REASON is not
   waived.** The flag requests the question; the answer grants the waiver. An agent that mis-parses
   the line and invents a handle gets a question, not a silent relaxation. Carry each confirmed pair
   into step 3 as `--waive <handle> --reason "<text>"`, repeatable.

   Say what the waiver costs, for the two handles that have a consequence: `reuse-first` is silent
   and is recommended against, and `land-once-done` still owes an override at close.

   **From the next command onward there is nobody to ask.** The driver enforces that rather than
   trusting it — `--waive` is accepted by `--preflight` alone, and only while no run-state file
   exists or the requested set matches the recorded one. So a later verb cannot take an answer, and
   a re-preflight after a compaction re-issues the recorded set rather than opening a new turn.

3. **Schedule the keepalive yourself.** This is your half and no script can do it: the scheduling
   store is in-memory and session-scoped, reachable only through your own tool calls. Use
   `{{KEEPALIVE_CREATE}}`, at the cadence this project declares — {{KEEPALIVE_INTERVAL}}. Keep the
   id it returns.
4. **Preflight**, handing over that id and any waiver pairs step 2 confirmed:

   ```bash
   bash {{KIT_DIR}}/unattended.sh --preflight <slug> --keepalive-id <id>
   bash {{KIT_DIR}}/unattended.sh --preflight <slug> --keepalive-id <id> --waive <handle> --reason "<why>"
   ```

   It refuses on a dirty tree, on the default branch, on an unwired repo, when the build README is
   absent at the pinned BASE or does not name this build, when the remote does not answer or
   advertises no default branch of its own, and when a second run is already live. It writes nothing until every one of those
   passes. Read the refusal it prints — each one names itself.

5. **If this project ships `/session-kickoff`, invoke it now — after preflight, never before.**
   The engine's unattended hand-back fires only when a run-state file already exists in a
   non-terminal phase, and `--preflight` is the only thing that creates one. Invoked first it
   halts at the READY card waiting for a confirmation nobody is present to give; invoked here it
   emits the card and continues. That ordering is the whole reason this step is numbered rather
   than mentioned.

   It buys the orientation preflight does not: the manifest audit, the pointer map, the tier rule,
   and the dated corrections and environment traps that repo has front-loaded. Skip it silently if
   the project has no such skill — that is legal, and this kit states none of what it carries.

## Start a run from a PROMPT

**Only when the invocation carries the authorizing parameter.** Prose alone is not an unattended
build, however unattended it sounds — the parameter IS the authorization gesture, and inferring it
from wording would let a description of a build start one. No parameter, no prompt path; use the slug
path above or do ordinary attended work.

**This project's anchor scope is `{{ANCHOR_SCOPE}}`, and this path needs `published`.** Under
`default-branch` there is no anchor a build folder you author can resolve at, so every step below
would end in the refusal step 1 names, with its remedy inert. If the value above is not `published`,
say so and stop — do not start, and do not write a build folder nothing can authorize.

The steps are ORDERED and the order is the point. Everything before the push is provably older than
the commit that authorizes the run; everything after it is contemporaneous with a run already
authorized. That is what makes "the owner was asked at the start" a property of the commit graph
rather than a claim in a transcript nobody reads.

1. **Orient from the prose**, in the `/session-kickoff` manner — steps 0 to 4 of that engine. Derive
   every field you can from the prose, the memory tree and the code. Do not ask yet.
2. **Decide whether to ask, ONCE.** The field set is the kickoff checker's, not this file's:
   `bash <check-script> --task-skeleton` prints it. **ACCEPTANCE and GATES are disqualifying** — a
   unit with no observable that proves it is not Ready, and no run can split it. Any other gap is
   askable, and askable once.

   **THIS IS THE ONLY OWNER TURN THERE IS.** One `AskUserQuestion`, every gap in it, four options
   maximum per call because that is the call's own limit. Not one call per gap: the owner is trying
   to walk away. From step 3 onward there is nobody to answer, and no verb will take an answer.

   If ACCEPTANCE or GATES is still missing after the ask, **stop without writing anything**. No run
   has started, so there is no run to abort: `--abort` and `--park` both refuse with no run-state
   file, and the kickoff engine's Step 5b exit 5 does not reach here — it is scoped to a run already
   started. Nothing staged, nothing committed, nothing to clean up.
3. **Write the build folder.** `{{MEMORY_ROOT}}/builds/<slug>/README.md`. **Front matter needs ALL
   SIX required keys** — `slug`, `node`, `opened`, `streams`, `roster`, `ids` — plus
   **`authorized-by: prompt`**, the key recording which discipline bound this run, which the merge
   bar re-derives from this same file. **And the body needs the generated-region marker pair**,
   `<!-- gen:build-index -->` and its close, or preflight refuses at step 5 with *the build README's
   generated markers are malformed*: the unit list is DERIVED from that region, so an unpaired marker
   is not something the driver guesses around. Every one of these is checked AFTER the push, where
   there is no owner turn left to ask about it. Carry the
   owner's prose VERBATIM under its own heading, and every clarification with its answer. The roster
   may be provisional: a roster that grows after preflight draws no refusal on this anchor, because
   your own push re-satisfies the comparison.
4. **Commit, then PUSH THE BRANCH.** Both, in that order. Skip the push and preflight refuses with
   `the remote advertises no tip for the branch this run is on, so nothing published authorizes it`
   — read here so you do not have to diagnose it there.
5. **Preflight**, exactly as the slug path does. It records the mode from the file you just pushed.
6. **The kickoff hand-back**, at the slug path's step 5 and for its reason.

**After any later roster change, commit AND PUSH before the next authorization read.** The roster
comparison holds on this anchor only because you re-push; a roster grown and committed but not pushed
is the ordinary state after research, and it blocks `--close` on `authorization-reachable` with no
override available and nobody to interpret it.

**The research and test obligations bind this path and not the slug path** — `researched` and
`solution-tested` in the directive table are scoped `prompt`. They point at the build method's M12,
which is where the loop is stated.

## While it runs

- Keep the phase honest, and give every phase claim a WITNESS — a sha, a tag, a run id. A claim with
  no witness is skipped by the oracle that would have judged it, so an unwitnessed phase is the
  cheapest possible lie and you are the only author of that field.
- Park what you refuse to decide, with the question, the options you saw, and why you refused. A
  bare "parked" is indistinguishable from "forgotten", and the wrap-up is where the owner gets the
  turn you did not take. There is a verb for it, and it is the only route a gate reads:

  ```bash
  bash {{KIT_DIR}}/unattended.sh --park <slug> --item "<the question>" --reason "<the options seen, and why you refused>"
  ```

  Re-running it with the same question and reason is a no-op, so a resumed run that re-derives the
  same refusal does not duplicate the row. It is refused on a finished record — an abort is the verb
  for a decision that stops the run.
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

It prints each tracked spec's id, status and classification, and names the next unit. It also joins
the build README's roster region against the tracked specs, so a planned unit nobody has specced
is reported as MISSING rather than silently omitted — and a roster whose markers are malformed is
a named refusal rather than a complete-looking list.

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

Write each with the VERB, never by editing the record:

```bash
bash {{KIT_DIR}}/unattended.sh --attest <slug> --item keepalive-reaped
bash {{KIT_DIR}}/unattended.sh --attest <slug> --item parked-decisions-surfaced
```

It derives the record KEY, which is not always the item name, and stages what it wrote. It refuses a
machine-checked item, so it cannot be used to certify anything the driver checks itself.

If you must override a blocked item, name it and give a reason:

```bash
bash {{KIT_DIR}}/unattended.sh --close <slug> --override <item> --reason "<why>"
```

The override is written into the run-state file as a parked entry and surfaces in the wrap-up. An
override nobody can read afterwards is just a skipped check.

**The pair REPEATS — one `--override <item> --reason <text>` per unmet item.** Two unmet items need
two pairs in one invocation, and a reason belongs to the flag that precedes it. This matters because
you are the only reader, and neither way of getting it wrong is silent: a `--override` left without
its own `--reason` is REFUSED before anything is written, and an item you never named at all simply
keeps blocking the close. Nothing is recorded on a reason that was written about a different item.

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
