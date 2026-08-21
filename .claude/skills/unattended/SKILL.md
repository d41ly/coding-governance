---
name: unattended
description: Start, resume, or close a run that will merge and push with NO owner turn between start and finish. Use when the owner wants a committed build carried to landing unattended, when a previous unattended run needs resuming after compaction or process death, or when one needs closing. Do NOT use for ordinary work where the explicit ask before a merge and a push still applies — that is the default, and this skill is the narrow exception to it.
---
<!-- gov:kit unattended@1.7 -->

# Unattended runs

The binding contract is `memory/guides/UNATTENDED-PROTOCOL.md`. This is the operating
summary; where they differ, the protocol wins and the difference is a bug in this render.

**The one thing to understand first.** An unattended run does not remove the checkpoint before a
merge and a push — it REPLACES it with something a machine can check. If the replacement is not
checkable, the run is not unattended, it is unsupervised. Everything below exists to keep that
distinction real.

## Which path

**Four start paths, and picking the wrong one costs a refusal you cannot answer.** Read the row that
matches what you were handed. The last cell is the `authorized-by:` value the build folder declares,
which is the key the merge bar re-derives and the driver records.

| You were handed | Path | Declares |
|---|---|---|
| a build folder that already exists and names its units | [Start a run](#start-a-run) | `slug` |
| prose, plus the authorizing parameter, and no build folder | [Start a run from a PROMPT](#start-a-run-from-a-prompt) | `prompt` |
| a PLAYBOOK that already exists, and a number of pieces to make from it | [Start a PLAYBOOK run](#start-a-playbook-run) | `recipe` |
| a topic and no playbook — the playbook is what you are to produce | [Author a PLAYBOOK](#author-a-playbook--creation-and-owner-instructed-amendment) | `prompt` |

**The fourth row is the one a reader gets wrong.** Arriving with a topic and no playbook, the
playbook-run path is the one that looks right and it is the one that cannot work: preflight refuses a
`playbook:` that does not resolve at BASE, so a no-playbook start never reaches preflight at all.
Making a playbook and following one are two acts with two authorizations.

**A fifth path exists and it is not on this list, because it is not a run**: producing pieces from a
playbook ATTENDED, with an owner in the loop. It writes no run-state file and calls no driver verb.
It is [below](#produce-pieces-attended), after the unattended paths it shares its records with.

## Start a run

0. **Read `memory/guides/BUILD-METHOD.md` WHOLE, before anything else.** Not conditionally.
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
   | `playbook-followed` | the pass loop and its regrounding rule | M7 | recipe | D11 |
   | `pieces-recorded` | the wrap-up derivation, over the pieces | M9 | recipe | D11 |

   **`Scope`** is which runs a directive binds. `all` binds every unattended run; a scope naming a
   mode binds only a run whose build README declared that `authorized-by:` value. `prompt` scopes
   research and a solution test, which are obligations of a build whose solution was not given.
   `recipe` scopes the two rows above, which are obligations of a build whose instructions were
   given: following them to the letter, and recording what came out. A waiver of a scoped handle is
   REFUSED on a run of another mode rather than recorded, since it would relax a rule that never
   bound it.

   **Neither `recipe` row states its rule, and that is deliberate.** Following a declared procedure
   to the letter IS the pass loop and its regrounding rule, and recording what was produced IS the
   wrap-up derivation. Both sections already exist and both are already re-read; a section written
   per directive is how a method grows until nobody re-reads it, which is what its own budget exists
   to prevent.

   Two rows carry a consequence worth knowing before you waive them. **`reuse-first` — recommend
   against.** Waiving it is SILENT: the bar stays green over a build that skipped the reuse probes,
   because nothing machine-checks a spec's reuse section for content. A waived run's spec §10 must
   NAME the waiver, or the skip leaves no trace at all. **`land-once-done`** — waiving it does not
   remove the Definition-of-Done item that observes completeness; that still owes an override at
   close.
1. **The build folder IS the authorization, and what makes it one is the ANCHOR it resolves at.** A
   `memory/builds/<slug>/README.md` that resolves at the anchor this project declares is the
   whole precondition. **This project's anchor scope is `published`.**
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
   `CronCreate`, at the cadence this project declares — every 10 minutes (cron 3-59/10 * * * *). Keep the
   id it returns.
4. **Preflight**, handing over that id and any waiver pairs step 2 confirmed:

   ```bash
   bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id <id>
   bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id <id> --waive <handle> --reason "<why>"
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

**This project's anchor scope is `published`, and this path needs `published`.** Under
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
3. **Write the build folder.** `memory/builds/<slug>/README.md`. **Front matter needs ALL
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

## Start a PLAYBOOK run

**A playbook already exists and the owner wants N pieces from it.** The run FOLLOWS that playbook to
the letter and produces the number asked for. It declares `authorized-by: recipe`, and that value is
what turns on everything below: the playbook resolution at BASE, the two piece-scoped
Definition-of-Done items, and the two `recipe`-scoped directives in the table above.

**CHECK, and there is no machine half — say it out loud before you start.** This mode is for
producing DECLARED CONTENT: the pieces a playbook describes, landing where its `outputs` globs say.
**An ordinary code build uses the slug or the prompt path**, and using this one for code would put a
diff nothing in this kit is shaped to grade under a mode whose whole vocabulary is about pieces. The
refusal that was to enforce this was withdrawn unbuilt, so on BOTH entry points — unattended and
attended — this is prose you keep and not a gate you lean on. A reader who mistakes it for
enforcement will be wrong in the expensive direction.

The steps are ORDERED and the order is the point, exactly as on the prompt path: everything before
the push is provably older than the commit that authorizes the run.

0. **Read `memory/guides/BUILD-METHOD.md` WHOLE**, and read the PLAYBOOK whole. Then read it
   again per piece — it is segmented for that, and a pass that carries the last piece's reading
   forward is the failure mode segmentation exists to answer.

   **Where you are writing the build folder yourself, this path needs `published`**, for the reason
   the prompt path states, and this project declares `published`. Where the owner landed the
   build folder before handing you the run, either anchor works and you skip the push in step 4.

1. **Orient from the playbook.** It answers most of what would otherwise be asked: what one piece IS,
   where pieces land, which checks run over one and which over all N. What it does not answer is
   usually just the COUNT and, where its `outputs` globs admit more than one location, which.

2. **Decide whether to ask, ONCE.** Same rule and same limit as the prompt path — one
   `AskUserQuestion`, every gap in it, and from step 4 onward there is nobody to answer. The field
   set is narrower here, so the ordinary case is no question at all.

3. **Write the build folder.** `memory/builds/<slug>/README.md`, with the six required keys
   and the generated-region marker pair, plus THREE more:

   - **`authorized-by: recipe`** — the mode.
   - **`playbook: <repo-relative path>`** — resolved at the pinned BASE, not at HEAD. A playbook this
     run wrote is not one anything committed before it can vouch for.
   - **`pieces: <n>`** — the count the close is measured against. Absent, non-numeric or zero is a
     refusal, because a defaulted count would put a number nobody wrote into the record.

4. **Commit, then PUSH THE BRANCH**, in that order, where you authored the build folder.

5. **Preflight.** It resolves the playbook at BASE and refuses if the playbook declares no output
   globs, no piece grain or no declaration block — all three are read from the blob at BASE, so fix
   them in the playbook and land that, never in the working tree.

6. **The kickoff hand-back**, at the slug path's step 5 and for its reason.

**While the pieces are made, RECORD each one.** A verdict that exists only in the transcript is a
verdict the merge bar cannot read, and the two piece-scoped Definition-of-Done items read the records
rather than the transcript:

```bash
bash tools/unattended/unattended.sh --record-piece <slug> --path <piece> --leg <name> --verdict PASS
bash tools/unattended/unattended.sh --record-set <slug> --leg <name> --verdict PASS
```

Each piece record is hash-joined to the piece, so editing a piece after recording makes its record
STALE rather than silently stale-and-passing. The SET record is written once, over all N, and its
identity is the ordered list of this run's piece hashes — derived, because a caller that named its
own set could name a set it did not produce.

**What you may NOT do is edit the playbook.** A run that rewrites the checklist it is graded by has
no rules left. What you would change goes on the record with `--propose`, joined to the step that
provoked it; the amendment is a separate authoring run.

## Author a PLAYBOOK — creation, and owner-instructed amendment

**A run that MAKES a playbook is not a run that FOLLOWS one, and it uses the PROMPT path above, not
`recipe`.** It has no playbook to name, so a `recipe`-mode preflight refuses it outright; and its
whole diff lands outside any declared output glob, which is the shape a content run is scoped to
avoid. There is no third mode here and no new discipline: the loop a playbook is written by is the
build method's research-then-test-then-choose section, which this path's two scoped directives
already bind. What this section adds is the ROUTING and one ordering property.

**Arriving with no playbook and a topic is this path, not an error.** Research the subject and the
code the pieces must relate to, decide what one piece IS, then write the playbook from
`memory/guides/PLAYBOOK-TEMPLATE.md` — its canon is closed, and the gate grades against the
template's own section table rather than a list typed somewhere else.

```bash
bash tools/unattended/check-playbook.sh
```

The gate grades **every tracked file carrying a declaration block**, whether or not a build README
names it. So a playbook you commit is graded from that commit forward, and a playbook that does not
validate cannot land — which is what lets a later run name it without re-validating anything.

**THE ORDERING PROPERTY: the playbook must be older than the BASE of the run that follows it.** Two
acts, two authorizations. A single run that authored its own instructions and then followed them has
no external check on either half, and every gate downstream would be grading a document that run
wrote for itself.

- **Whenever your build folder was committed before your run**, this has a machine half under either
  anchor. The BASE is then a merge-base you cannot move, a playbook you committed yourself does not
  resolve there, and preflight refuses with *a recipe-mode build README names a playbook that does not
  resolve at the pinned BASE*. The scope value does not change this: the second anchor is reached only
  when the build folder itself fails to resolve at the merge-base.
- **The one unprotected state is a run that authors BOTH halves** — its own build folder and its own
  playbook — under `published`, which this project declares (`published`). Its BASE is the tip
  it pushed, that tip carries the playbook it just wrote, and nothing refuses it. This is the
  `published` anchor's declared cost reaching one step further than the protocol spells out: a run
  that can author its own authorization can author the instructions it is judged against too.
  So this is a CHECK you keep, stated plainly rather than dressed up as a derivation: **land the
  playbook in its own earlier run, then start the run that follows it.**

**Amendment rides this same path.** Proposals accumulate on the run-state files of the runs that
found them, and acting on them is a later, owner-instructed run that reads the surfaced proposals,
edits the playbook and lands it. That is why a piece-producing run may not edit its own playbook and
needs no exception to say so.

- CHECK, not a gate: **cite the proposals you acted on**, and say which you declined and why. No gate
  can check this without reading intent, and a proposal already carries the step it amends, so the
  join survives even when the citation does not — but the owner reading the amendment is entitled to
  know which of their run's findings survived it.

## Produce pieces ATTENDED

**Not a run, and this section is here because it shares the RECORDS with the paths above and nothing
else.** An owner is in the loop, so there is no run to authorize, no run-state file, no phase, no
keepalive and no Definition of Done. Every check in the kit gate that is keyed on a run-state file
sees nothing here, and that is what "not the driver" means.

**What the merge bar still sees is what you PRODUCED.** The per-piece records and the set record are
tracked files, hash-joined to the pieces, and the playbook leg reads them without knowing who wrote
them or how. So the honest sentence is this one: **the attended path is gated on what it produced,
the unattended path on that plus how it ran.**

Both writers take a records ROOT instead of a slug — one function, two callers, never two
implementations:

```bash
bash tools/unattended/unattended.sh --record-piece - --records-root <root> --path <piece> --leg <name> --verdict PASS --run <label>
bash tools/unattended/unattended.sh --record-set - --records-root <root> --leg <name> --verdict PASS --set <hash,hash>
```

The root is the playbook's own `records` declaration — read it from the playbook rather than choosing
one, or the leg reads a different directory from the one you wrote. `--run` labels the batch so a
later reader can tell one sitting's pieces from another's; on the unattended path the slug fills that
in.

**The CHECK about code builds binds here too, and here it has no machine half at all** — not even a
withdrawn one. The refusal that was to enforce it reads a recorded mode and a run's commit set, and
both exist only through the driver. An attended path is outside it by construction, which is the kind
of thing worth knowing before you rely on a gate to catch you.

**No entry in the kickoff engine's exit list, deliberately.** That list enumerates the interactive
exits an UNATTENDED run has to resolve with nobody to ask. An attended path has an owner by
definition, so the absence is a decision and not an oversight.

## While it runs

- Keep the phase honest, and give every phase claim a WITNESS — a sha, a tag, a run id. A claim with
  no witness is skipped by the oracle that would have judged it, so an unwitnessed phase is the
  cheapest possible lie and you are the only author of that field.
- Park what you refuse to decide, with the question, the options you saw, and why you refused. A
  bare "parked" is indistinguishable from "forgotten", and the wrap-up is where the owner gets the
  turn you did not take. There is a verb for it, and it is the only route a gate reads:

  ```bash
  bash tools/unattended/unattended.sh --park <slug> --item "<the question>" --reason "<the options seen, and why you refused>"
  ```

  Re-running it with the same question and reason is a no-op, so a resumed run that re-derives the
  same refusal does not duplicate the row. It is refused on a finished record — an abort is the verb
  for a decision that stops the run.
- A playbook you are FOLLOWING is not a playbook you may edit. A run that rewrites the checklist it
  is graded by has no rules left, so what you would change goes on the record joined to the step that
  provoked it, and the amendment is a separate authoring run the owner starts:

  ```bash
  bash tools/unattended/unattended.sh --propose <slug> --item "<the amendment>" --step "<the step it applies to>" --reason "<what you saw that provoked it>"
  ```

  Nothing blocks on a proposal and `--status` counts them apart from the questions, so recording one
  costs the run nothing. The same amendment against two steps is two rows, because it is two edits.
- Record a verdict where a check ran over content rather than over code — one piece at a time, and
  once over the whole set, which is the population a per-piece pass structurally cannot see:

  ```bash
  bash tools/unattended/unattended.sh --record-piece <slug> --path <piece> --leg <name> --verdict PASS
  bash tools/unattended/unattended.sh --record-set <slug> --leg <name> --verdict PASS
  ```
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

It prints each tracked spec's id, status and classification, and names the next unit. It also joins
the build README's roster region against the tracked specs, so a planned unit nobody has specced
is reported as MISSING rather than silently omitted — and a roster whose markers are malformed is
a named refusal rather than a complete-looking list.

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

Write each with the VERB, never by editing the record:

```bash
bash tools/unattended/unattended.sh --attest <slug> --item keepalive-reaped
bash tools/unattended/unattended.sh --attest <slug> --item parked-decisions-surfaced
```

It derives the record KEY, which is not always the item name, and stages what it wrote. It refuses a
machine-checked item, so it cannot be used to certify anything the driver checks itself.

If you must override a blocked item, name it and give a reason:

```bash
bash tools/unattended/unattended.sh --close <slug> --override <item> --reason "<why>"
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
