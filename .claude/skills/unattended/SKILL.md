---
name: unattended
description: Start, resume, or close a run that will merge and push with NO owner turn between start and finish. Use when the owner wants a committed build carried to landing unattended, when a previous unattended run needs resuming after compaction or process death, or when one needs closing. Do NOT use for ordinary work where the explicit ask before a merge and a push still applies — that is the default, and this skill is the narrow exception to it.
---
<!-- gov:kit unattended@1.14 -->

# Unattended runs

The binding contract is `memory/guides/UNATTENDED-PROTOCOL.md`. This is the operating
summary; where they differ, the protocol wins and the difference is a bug in this render.

**The one thing to understand first.** An unattended run does not remove the checkpoint before a
merge and a push — it REPLACES it with something a machine can check. If the replacement is not
checkable, the run is not unattended, it is unsupervised. Everything below exists to keep that
distinction real.

## Before any path — schedule the keepalive NOW

**This is the run's first act, and it comes before you read anything else.** Not before preflight:
before ORIENTING. Use `CronCreate`, at the cadence this project declares —
every 10 minutes (cron 3-59/10 * * * *) — and keep the id it returns, because `--preflight` refuses without it.

```
CronCreate  ->  keep the id
```

**Why it is here and not inside a path.** It used to be step 3 of the slug path and nowhere else, so
three of the four paths below never reached it: the two that start from prose or a playbook orient,
research, choose a solution, write a build folder and push a branch BEFORE their first verb, and that
is the longest unattended stretch a run has. A run that stalls in it has no keepalive, nothing wakes
it, and nothing records why. A step written inside one path is a step the other three do not execute,
which is why this one sits above the table instead.

**One path below is NOT covered by this section, and it is named rather than left out**: `Resume`.
A resumed session inherits a job it did not schedule and must PRESUME IT ALIVE — the intuition that
the store went with the process is measured false, and `## Resume` says so with the measurement. That
section therefore reaps before it schedules and carries its own instruction; this one cannot bind it.
Every other path routes through the table below.

**If the run never starts, reap it anyway.** Every path below can refuse — a value that does not
resolve, an anchor scope that cannot authorize the mode, any of `--preflight`'s refusals. The store
is session-scoped, so a job left by a run that never began is orphaned exactly like one left by a run
that ended, and there is no run-state file for a later reader to find it through. Delete it with
`CronDelete` before you stop.

## Which path

**Four start paths, and picking the wrong one costs a refusal you cannot answer.** Read the row that
matches what you were handed. The last cell is the `authorized-by:` value the build folder declares,
which is the key the merge bar re-derives and the driver records.

| You were handed | Path | Declares |
|---|---|---|
| a build folder that already exists and names its units | [Start a run](#start-a-run) | `slug` |
| prose or a prompt file, handed as `--prompt <value>`, and no build folder | [Start a run from a PROMPT](#start-a-run-from-a-prompt) | `prompt` |
| a PLAYBOOK that already exists, and a number of pieces to make from it | [Start a PLAYBOOK run](#start-a-playbook-run) | `recipe` |
| a topic and no playbook, handed the same way and bound by the same fence — the playbook is what you are to produce | [Author a PLAYBOOK](#author-a-playbook--creation-and-owner-instructed-amendment) | `prompt` |

**The fourth row is the one a reader gets wrong.** Arriving with a topic and no playbook, the
playbook-run path is the one that looks right and it is the one that cannot work: preflight refuses a
`playbook:` that does not resolve at BASE, so a no-playbook start never reaches preflight at all.
Making a playbook and following one are two acts with two authorizations.

**A fifth path exists and it is not on this list, because it is not a run**: producing pieces from a
playbook ATTENDED, with an owner in the loop. It writes no run-state file and calls no driver verb.
It is [below](#produce-pieces-attended), after the unattended paths it shares its records with.
It schedules no keepalive, and the section above does not bind it: there is an owner in the loop.

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
   | `parallel-when-disjoint` | the parallelism obligation | M6 | all | D6 |
   | `passes-committed` | the commit boundary | M6 | all | D8 |
   | `diff-reviewed` | the closing review of the cumulative diff | M8 | all | D7 |
   | `land-once-done` | when a build may land | M8 | all | D8 |
   | `conflicts-reconciled` | merge-conflict disposition | M8 | all | D8 |
   | `wrap-up-derived` | how the wrap-up is composed | M9 | all | D8 |
   | `discoveries-adopted` | a beneficial discovery joins the running build, decided at once | M10 | all | D12 |
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

   Two rows carry a consequence worth knowing before you waive them. **`reuse-first`** — waiving it
   is no longer silent, and both halves that made it so are closed. The `reuse-probed` item reports
   the waiver and its recorded reason at `--close`, and where the project sets a reuse-evidence
   cutoff the memory gate refuses a spec whose §10 is missing EITHER the recall terms or a probe
   result — either one absent is a refusal, not only both. A waived run's spec §10 should still NAME the waiver — that is one of the things the gate
   accepts as a finding, so naming it is also how the spec lands. **`land-once-done`** — waiving it
   does not remove the Definition-of-Done item that observes completeness; that still owes an
   override at close.
1. **The build folder IS the authorization, and what makes it one is the ANCHOR it resolves at.** A
   `memory/builds/<slug>/README.md` that resolves at the anchor this project declares is the
   whole precondition. **This project's anchor scope is `published`.**
   On the **default-branch** anchor that means committed before your branch existed, and preflight
   REFUSES a build folder you created — a run that authorizes itself has no authorization. Where the
   project declares **published**, the tip the remote advertises for your OWN branch also counts, so a
   run may author its build folder and push it — but only where the build folder declares
   `authorized-by: prompt` or `recipe`. A `slug` folder, which is what NO `authorized-by:` key means,
   is refused on that anchor; protocol section 1 states what the anchor costs, and the
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

   Say what the waiver costs, for the two handles that have a consequence: `reuse-first` surfaces at
   close through the `reuse-probed` item and still owes its spec §10 a named waiver, and
   `land-once-done` still owes an override at close.

   **From the next command onward there is nobody to ask.** The driver enforces that rather than
   trusting it — `--waive` is accepted by `--preflight` alone, and only while no run-state file
   exists or the requested set matches the recorded one. So a later verb cannot take an answer, and
   a re-preflight after a compaction re-issues the recorded set rather than opening a new turn.

3. **Preflight**, handing over the keepalive id you already hold and any waiver pairs step 2
   confirmed:

   ```bash
   bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id <id>
   bash tools/unattended/unattended.sh --preflight <slug> --keepalive-id <id> --waive <handle> --reason "<why>"
   ```

   It refuses on a dirty tree, on the default branch, on an unwired repo, when the build README is
   absent at the pinned BASE or does not name this build, when the remote does not answer or
   advertises no default branch of its own. It writes nothing until every one of those
   passes. It does NOT refuse because another build is live — it announces the concurrent runs and
   continues. Read the refusal it prints — each one names itself.

4. **If this project ships `/session-kickoff`, invoke it now — after preflight, never before.**
   The engine's unattended hand-back fires only when a run-state file already exists in a
   non-terminal phase, and `--preflight` is the only thing that creates one. Invoked first it
   halts at the READY card waiting for a confirmation nobody is present to give; invoked here it
   emits the card and continues. That ordering is the whole reason this step is numbered rather
   than mentioned.

   It buys the orientation preflight does not: the manifest audit, the pointer map, the tier rule,
   and the dated corrections and environment traps that repo has front-loaded. Skip it silently if
   the project has no such skill — that is legal, and this kit states none of what it carries.

## Start a run from a PROMPT

**Only when the invocation carries `--prompt`.** Prose alone is not an unattended build,
however unattended it sounds — the parameter IS the authorization gesture, and inferring it from
wording would let a description of a build start one. No `--prompt`, no prompt path; use the
slug path above or do ordinary attended work. The fourth routing row above is this path too, so this
fence binds a playbook-authoring start exactly as it binds a code one.

**THE VALUE IS THE BUILD.** `--prompt` takes one argument, and it is everything after the token
to the end of the invocation line, with one layer of surrounding quotes stripped before any test. It
is either a path to a file holding the prompt, or the prompt itself. Test for the FILE FIRST — a
relative path resolves against the repository root and never against wherever this session happens to
be standing.

| The value | What it is | What you do |
|---|---|---|
| no whitespace, names a readable file | a path | read it; the FILE'S CONTENT is the prompt |
| no whitespace, names nothing readable | a refusal | say the path did not resolve, and stop |
| has whitespace, names nothing readable | the prompt itself | take it verbatim |
| has whitespace AND names a readable file | a refusal | say the value is ambiguous, and stop |

The file test runs first because the whitespace rule is not symmetric. A prompt is multi-word in
every case; a PATH is not single-word in every case, because a quoted path containing a space arrives
as one argument with whitespace in it. Reading that as a prompt would make a real file silently
become the whole scope of the build, so the ambiguous case is a refusal rather than a guess.

**This project's anchor scope is `published`, and this path needs `published`.** Under
`default-branch` there is no anchor a build folder you author can resolve at, so every step below
would end in the refusal step 1 names, with its remedy inert. If the value above is not `published`,
say so and stop — do not start, and do not write a build folder nothing can authorize.

**And `authorized-by: prompt` in step 3 is not bookkeeping.** The second anchor is admissible per
MODE: omit that key and the folder reads as `slug`, which is refused on this anchor because `slug`
means a folder that already existed. The refusal arrives AFTER the push, where there is no owner turn
left to ask about it.

The steps are ORDERED and the order is the point. Everything before the push is provably older than
the commit that authorizes the run; everything after it is contemporaneous with a run already
authorized. That is what makes "the owner was asked at the start" a property of the commit graph
rather than a claim in a transcript nobody reads.

1. **Orient from the prose**, in the `/session-kickoff` manner — steps 0 to 4 of that engine. Derive
   every field you can from the prose, the memory tree and the code. Do not ask yet.

   **RUN the orientation probes HERE, before step 3 writes the roster.** Step 4 of that engine names
   WHICH they are and this step does not restate them; what it adds is WHEN. The hand-back at step 6
   runs the same engine, but by then the roster is written, pushed and comparable — so a seam the
   reuse probe would have found, or a prior record recall would have surfaced, arrives after the
   decision it was meant to inform, and re-deciding costs a commit and a push. The probes cost
   seconds. "In the manner of" is a posture a reader can satisfy without running anything, which is
   why the timing is stated as its own instruction rather than left inside the pointer.
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
   there is no owner turn left to ask about it.

   **The prompt itself goes to a RECORD, never into this README.** Write it under
   `memory/builds/<slug>/prompts/`, which is where this memory tree sanctions prompt-kind
   files, carrying its `**Serves:**` line and — where the value was a path — the path it came from.
   The bytes travel rather than the reference: the build folder IS the authorization, so it may not
   point at a file that can be edited after the run starts. Three reasons it is not the README, and
   none of them is tidiness. That file's heading canon is CLOSED and its slots carry byte ceilings,
   so a prompt under a heading of its own is a refusal. That file is PARSED for the marker pair
   above, by a matcher that reads column 1 and is blind to fencing, so a prompt quoting
   `<!-- gen:build-index -->` plants a second marker and the refusal lands after the push. And a
   malformed record reds the memory gate HERE, at step 3, where you can still fix it. The README
   states the build in its own words and points at the record; clarifications and their answers ride
   the record too. The roster
   may be provisional: a roster that grows after preflight draws no refusal on this anchor, because
   your own push re-satisfies the comparison.
4. **Commit, then PUSH THE BRANCH.** Both, in that order. Skip the push and preflight refuses with
   `the remote advertises no tip for the branch this run is on, so nothing published authorizes it`
   — read here so you do not have to diagnose it there.
5. **Preflight**, exactly as the slug path does. It records the mode from the file you just pushed.
6. **The kickoff hand-back**, at the slug path's step 4 and for its reason.

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

6. **The kickoff hand-back**, at the slug path's step 4 and for its reason.

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
tracked files, hash-joined to the pieces, and the playbook leg reads both without knowing who wrote
them or how. So the honest sentence is this one: **the attended path is gated on what it produced,
the unattended path on that plus how it ran.**

**And read the split exactly, because it is narrower than it sounds.** The leg CLASSIFIES and reports
— verified, failed, stale, unrecorded, unchecked, orphan, and whether a declared set check has a
verdict at all. What BLOCKS on any of it is `--close`, which the attended path never calls. So on this
path those counts are evidence a human must read, and the only thing that reds the bar for you is a
record whose shape the leg refuses. An earlier revision of this paragraph said the leg read the set
record when nothing in it opened one; the reader who believed that stopped looking for a gate that
was not there.

Both writers take a records ROOT instead of a slug — one function, two callers, never two
implementations:

```bash
bash tools/unattended/unattended.sh --record-piece - --records-root <root> --path <piece> --leg <name> --verdict PASS --run <label>
bash tools/unattended/unattended.sh --record-set - --records-root <root> --leg <name> --verdict PASS --run <label> --set <hash,hash>
```

The root is the playbook's own `records` declaration — read it from the playbook rather than choosing
one, or the leg reads a different directory from the one you wrote. `--run` labels the batch so a
later reader can tell one sitting's pieces from another's; on the unattended path the slug fills that
in.

**`--set` is WEAKER here than on the unattended path, and the difference is worth knowing.** There
the set identity is DERIVED from the run's own piece records, because a caller that names its own set
could name a set it did not produce. Here you name it, so it is a claim rather than a derivation —
which is the same trade the whole attended path makes, one field further down. Take the hashes from
the piece records you just wrote, not from memory.

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
- **And what you may NOT park: a STRICTLY BENEFICIAL discovery.** Protocol section 11 is the rule and
  is not restated here. The shape of it: a discovery that makes an observable this repo already
  MEASURES strictly better, makes nothing it measures worse, and survives M3's vetoes is ADOPTED into
  this build — now, by you — with `--rescope --act add`. One that fails the first two clauses is a
  BACKLOG row; one that trips a veto is a park. A BLOCKER between you and your own landing is a
  discovery, and it is the one most often mistaken for a question. Parking a discovery that qualifies
  is not caution: the reader you are deferring to is the one who left, so the finding is discarded
  and the record makes the discarding look careful.
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
- **When building uncovers what speccing could not, AMEND — do not stall.** M3 delegates this build's
  own scope and M2 names the three acts: RETIRE a unit, SUPERSEDE it, or ADD one the build turns out
  to need. Every amendment owes a row, and this is the verb that writes it:

  ```bash
  bash tools/unattended/unattended.sh --rescope <slug> --act retire|supersede|add --item <unit-id> [--successor <unit-id>] --reason "<what building uncovered>"
  ```

  Two bounds, and they are the whole of your authority here. The build README's GOAL statement is
  what you may not amend, and the delegation does not reach a governance carrier's own stated
  constraints. An id already in the units region may never LEAVE it — retiring is a status flip to
  `WONTDO` with a successor or reason in the header tail, never a deletion, because the
  authorization compares BASE against HEAD as a subset and refuses a removal.
- **Before dispatching two passes at once, DECLARE what each will write.** The build method requires
  both path lists written down first, and this verb is what reads one:

  ```bash
  bash tools/unattended/unattended.sh --dispatch <slug> --pass <unit-id> --writes <path> --writes <path>
  ```

  `--writes` is REPEATABLE and each occurrence is ONE path. Two of the method's three disjointness
  clauses are decided here and refused on the spot: two passes claiming one file, and a pass claiming
  a shared mutable record. A generated index ALONE is fine — every pass changes a spec header it is
  rendered from — and only the index together with its GENERATOR is refused. The third clause, whether
  a file is a contract the sibling reads, is a judgement no verb can make, and it says so rather than
  pretending. If a pass discovers it needs another file, re-declare with the WIDER set BEFORE the
  commit; narrowing is refused, because narrowing after the fact is how a write gets hidden.
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

It takes its unit SET and ORDER from the generated units region, so its "next" and `--status`'s
are the same unit by construction. It prints each unit's id, status and classification, and names
the next one. It also joins
the build README's roster region against the tracked specs, so a planned unit nobody has specced
is reported as MISSING rather than silently omitted — and a roster whose markers are malformed is
a named refusal rather than a complete-looking list.

## Record each review round, and let the loop end itself

A review that keeps coming back BLOCKED is the fault this kit was built to remove, and the remedy is
not a round cap — over the tracked corpus the clean exit the method names occurs ZERO times, so a cap
would only move the stall earlier. Record every round and the verb tells you what the loop is doing:

```bash
bash tools/unattended/unattended.sh --review <slug> --subject <id-or-slug> --verdict <verdict> --blockers <N>
```

`--subject` is the spec document for a spec audit and the BUILD SLUG for the closing diff review.
`--verdict` is one of exactly three: `CLEAN`, `CLEAN WITH FIXES`, `BLOCKED`. `--blockers` is the
confirmed-blocker count for THIS round, as a plain integer.

It answers with one of four states, and the state is what you act on:

- **CONVERGING** — this round's count is strictly smaller than the round before. Fold and go again.
- **CONVERGED** — zero blockers. The loop is done for that subject.
- **NON-CONVERGENT** — the count did not shrink. **The loop STOPS**, and every blocker still standing
  becomes a UNIT of this build: specced at its tier, built, closed. Not parked, not waived, and not
  re-reviewed — a promoted unit is audited as a SPEC, which is what makes promotion terminate.
- **CEILING** — the runaway backstop fired, which means the convergence predicate did not terminate.
  That is a defect in the predicate, not a routine outcome. The run promotes and lands anyway, and you
  record it in the build README, because a fact that lives only in a transcript is a fact nobody reads.

Strictly smaller, not merely different: a sequence that oscillates 2, 1, 2 satisfies "the count
changed" forever. A subject whose loop already ended does not take another round.

## Which kit version is installed

```bash
bash tools/unattended/unattended.sh --version
```

It prints the engine identity and exits. Worth one line here because it is a dispatched entry point
like any other, and a verb no surface names is a verb the documentation join treats as missing.

## Resume

```bash
bash tools/unattended/unattended.sh --resume <slug>
```

Read the run-state file before doing anything else. It survived compaction and process death; your
context did not.

**Then REAP the recorded id, and only then schedule a replacement.** In that order, and the order is
the whole point. The intuition is that a resumed session's keepalive died with its process because
the store is session-scoped — and that intuition is MEASURED FALSE: a run asserted it twice about two
jobs and `CronCreate`'s own listing showed both still firing. So issue
`CronDelete` against the `keepalive` id the run-state file already names, read the result
back, and say what it returned. Assume a surviving job, not a dead one; the failure mode of assuming
dead is a keepalive firing forever with a green `keepalive-reaped` attestation over it.

Then schedule the new one. This is the only exception to "read the record first": read it, reap,
schedule, and then do the work.

**The record cannot be corrected in place, and you must know that rather than discover it.**
`--keepalive-id` is accepted by `--preflight` alone, so a resumed session has nowhere to write the
new id. The `keepalive` fact keeps naming the old job, so your `keepalive-reaped` attestation at close
covers BOTH — the one you deleted here and the one you scheduled — and the wrap-up says so, with what
the delete returned. Re-preflighting to record the new id is NOT the remedy: it refuses on a dirty
tree and re-pins the anchor, which costs more than the stale field does.

## Close

```bash
bash tools/unattended/unattended.sh --close <slug>
```

**The bar it runs is BOUNDED.** `GATE_BOUND` seconds, declared by the project or defaulted by the
kit — and when it is the DEFAULT, said so on stderr, because a bound nobody set should not
be invisible. A bar that does not answer within it is KILLED, and
`gates-green` is then unmet with a message saying the bar never RETURNED rather than that a leg
FAILED. Those are different facts, and an operator who confuses them spends an hour hunting a
failing leg that does not exist. The same bound covers the wiring check `--preflight` runs.

It BLOCKS on any unmet Definition-of-Done item. Two of them are yours to attest, because no script
can observe them: that you reaped the keepalive (`CronDelete`), and that every parked
decision reached the wrap-up. Record them honestly — attestation is not a machine verdict, and the
gate says so wherever it reports them.

**One item has NO override, and this is where you will meet it.** `authorization-reachable` cannot be
overridden, waived or attested around: an override on the authorization check IS the authorization
check, so the verb refuses the pair rather than recording it. If a close blocks on that item, the
answer is never a flag — it is that this run cannot show what authorized it, and the remedy is
outside the close.

Write each with the VERB, never by editing the record:

```bash
bash tools/unattended/unattended.sh --attest <slug> --item keepalive-reaped
bash tools/unattended/unattended.sh --attest <slug> --item parked-decisions-surfaced
bash tools/unattended/unattended.sh --attest <slug> --item parked-decisions-surfaced --value "yes, <n> surfaced"
```

**The parked-decisions attestation may carry a COUNT, and if you give one it is CHECKED.** `--close`
refuses unless that integer equals the number of `surfaced`-class parked lines in the record, so the
claim stops being unfalsifiable — "I surfaced them" becomes "I surfaced four, and the record holds
four". Omit the number and the older, weaker form still stands; it is not a machine verdict either
way, and the gate says so wherever it reports it. Two things the count does NOT include: a `history`
kind, which the owner need not adjudicate, and the overrides this same `--close` is about to write,
because the Definition of Done is evaluated before they land.

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
bash tools/unattended/unattended.sh --version   # which build of this kit am I talking to
bash tools/unattended/unattended.sh --landed <slug>
```

**Run this AFTER the lander returns, not before.** It re-observes the remote and takes the tip the
remote advertises whenever your work is on it — the one phase claim you cannot simply assert, which
is the point. **When that fails it falls back to the LOCAL default branch**, so a build you merged
locally but cannot push still has a terminal to reach instead of an abort. The fallback asserts your
own BRANCH TIP is an ancestor of local main, never that HEAD is; on the default branch HEAD is that
ref, and a commit is its own ancestor.

Two facts land in the record and you do not write either: `landed-anchor`, which says `remote` or
`local`, and `unpushed-at-landing`, which counts what local main carries that the remote does not.
Read the second before you believe the first — a local landing sits on top of whatever else is on
that branch. What the weaker anchor does not buy is protocol section 9, and it is not repeated here.

**AND DO NOT COMMIT BETWEEN THE PUSH AND THIS VERB.** Where the project declares a lander marker, the
lander writes the commit it pushed and this verb requires the marker to name HEAD **exactly**. That is
equality, not ancestry: one more commit after the push — even the record commit — and `--landed`
refuses. The refusal names both shas, the one it wanted and the one the marker holds, so a stale
marker and a moved HEAD are distinguishable. Then commit the record it writes and land that commit too; until it is
committed, every later run still counts yours as live — which no longer reds anyone's bar, but does
put your unfinished run in every later run's concurrency report.

`--close` moves you to `LANDING`, and nothing else may: a phase move into it would claim the
Definition of Done was evaluated without evaluating it.

## If it cannot finish

```bash
bash tools/unattended/unattended.sh --abort <slug> --code <halt-code> --reason "<what stopped it, and what you refused to decide>"
```

**Both are required, and they are for different readers.** The reason is prose for the owner and
lands in the parked region, because an abort with no recorded reason is indistinguishable from a run
that simply stopped. The CODE is the field everything else joins on — the status line, the resume
path and the gate leg all read it by key — because a single `ABORTED` terminal says a run stopped and
never says why. It is validated against a closed vocabulary, and the refusal names the legal set, so
you do not have to read source to find it. There is no catch-all member: if nothing fits, take the
closest code and put the specifics in the reason, and say so — a mismatch worth a backlog row is
better than a vocabulary with a hole in it. You still owe both attestations first — reap the
keepalive and surface the parked decisions — since an aborted run orphans exactly the same job and
leaves exactly the same decisions unseen. An abort does not merge and does not push.

## Reap

Delete the keepalive with `CronDelete` before you finish. Nothing else can: when your
process exits, an unreaped job is orphaned in a store no later run can see.
