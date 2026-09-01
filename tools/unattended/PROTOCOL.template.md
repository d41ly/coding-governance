<!-- gov:kit unattended@1.14 -->
# Unattended runs — the protocol

*Two legs byte-compare this file against the template it ships from. **They compare the two copies to
each other, so a claim FALSE IN BOTH is green** — three defects here survived exactly that way. A
parity leg is a copy check, not a truth check; only a reader grades a sentence against the code.*

**Binding.** A session running with no human in the loop follows this document. It is
project-agnostic: every value that differs per repo is a DECLARATION in the repo-root
`.unattended.conf`, never a constant in this text. The driver and the gate leg both read the
declarations rather than restating them, so a phase token or a DoD item written into a script is
itself a defect.

An unattended run is a session that will merge and push without an owner turn between start and
finish. That is the only thing that makes it different, and it is the whole reason this document
exists: the checkpoint the explicit-ask rule provides has to be replaced by something a machine can
check, not merely removed.

## 1. The authorization

The run is authorized by the **build folder itself** — a `<MEMORY_ROOT>/builds/<slug>/README.md`
resolving at the anchor the project declares. On the default-branch anchor that means committed
before the run's branch existed. The owner's act is `/unattended <slug>`, or — where the second
anchor is admitted — an invocation carrying the authorizing parameter, spelled by `AUTH_PARAM` (§8),
whose ARGUMENT is the prose the build is scoped by or a path to a file holding it. They author
nothing per run except a directive waiver's reason text, which `--preflight` records for them (§10),
and on the prompt path the prose plus whatever the agent asks at its single opening turn. Four
properties, all mechanical:

- **It is asserted, never written by the run — on the DEFAULT-BRANCH anchor.** `--preflight` refuses
    if it is absent, and at that anchor a run that could write its own authorization has none. **On
    the second anchor this is weaker, deliberately**: the run may author its own build folder and
    push it, which is cost 1 made USABLE rather than merely conceded. Which anchor authorized a run
    is recorded, and so is the discipline it claimed; neither is a verdict and §9 applies to both.
    **Bounded by MODE**: admissible only for `prompt` and `recipe`, the driver's
    `SECOND_ANCHOR_MODES`. A `slug` README — what an absent `authorized-by:` means — is refused there
    by preflight and by the bar. What this removes is self-authorization by DEFAULT.
- **It is reachable from the pinned BASE.** A build folder introduced on the run's own branch grants
  nothing. Reachability is the machine-checkable form of "somebody with push rights put this here
  before this run branched" — and the run holds push rights by construction, so it is a cost, not a
  proof. The pin comes from the ref name and tip the REMOTE advertises for its own HEAD, never from a
  local ref or the environment. What that removes and leaves is §9.
- **Only its SHAPE is checked.** It resolves at BASE, parses as front matter, and its `slug:` names
  the build. No gate can tell whether the owner meant it.
- **It may declare an authorization MODE, and that declaration is a RECORD rather than a verdict.**
  An `authorized-by:` key in the front matter, over the closed set `prompt` / `slug`; absent is
  `slug`, which is every build folder written before the key existed. `--preflight` reads it from the
  blob at BASE and records it, and the merge bar re-derives it from that same blob independently - so
  a run cannot record a discipline its own authorization did not carry. What this does NOT buy is
  stated here rather than discovered: the key is a byte in a file, and §9's reduction applies to it
  exactly as it applies to every other local input. It says which discipline the run declared it was
  under, not that the declaration was true.
- **Its UNIT SET may not SHRINK under the run — on the DEFAULT-BRANCH anchor only.** The ids in the
  GENERATED `gen:build-units` region are compared across the BASE and the BASE set must be a SUBSET of
  the one at HEAD: additions admitted, removals and renames refused. IDS, never row bytes — a row
  carries the unit's status, rev and date, so a byte comparison would refuse every run that BUILT
  anything, which is the run this exists to permit. A BASE carrying no such region is a refusal from
  `UNITS_REGION_CUTOFF` onward and inherits the old presence-based opt-in before it, because a run's
  BASE is pinned before its own work and the BASE of the run that landed the region cannot carry it.
  INTEGRITY, not a narrowing of the grant. **It does not hold on the second anchor**: there the BASE is
  a tip the run itself pushed, so it can re-satisfy the comparison against its own new bytes.

**A SECOND ANCHOR, when the project declares one.** `ANCHOR_SCOPE="published"` admits the tip the
remote advertises for the run's OWN branch — used only when the README does not resolve at the
merge-base, and only when that tip is an ancestor of HEAD. Absent, blank or misspelled keeps the
strict anchor. Both anchors observe the endpoint the landing push goes to.

**It spends THREE things, all put to the owner and accepted.** The first list carried only the first:

1. **Self-authorization gets cheaper.** A branch push is not gated by the pre-push hook, so a run can
   authorize ITSELF in two commands, where before it could only authorize its successor (cost 4).

   **It reaches one step further, measured rather than reasoned.** A `recipe` run names a playbook
   resolved at BASE, so one the run wrote does not normally resolve. But a run authoring its own
   build folder is the run this anchor moves onto the branch tip, and that tip carries the playbook.
   So a run authoring BOTH halves authors the instructions it is judged by as well as its own
   authorization, unrefused. A run whose build folder predates it keeps the strict anchor and that
   refusal, which is why this is narrow rather than a general hole.
2. **The BAR weakens for adopters who never opt in.** The key gates the DRIVER and cannot gate the
   leg: the conf is a working-tree file the run can commit, so a leg reading it reads its subject's
   answer. The leg's BASE check therefore asks "published on the remote" in every repo.
3. **Roster integrity becomes satisfiable by construction** on the branch anchor, as qualified above.

None of the three is closed. What the design adds is VISIBILITY: the record names the anchor used.

**What this costs, stated because the previous design paid none of it.** The authorization was once a
block naming the build and both authorized actions, compared byte-for-byte across the BASE. Moving it
to the build folder trades these properties:

1. **Integrity becomes existence.** A README's generated region legitimately moves, so no whole-file
   equality is assertable.
2. **The grant is class-wide.** Every build folder satisfies the predicate; the narrowing is the
   slug the owner types, and chat is not machine-checkable.
3. **It names no ACTIONS** and **cannot be revoked**: a build authorizes both, permanently.
4. **It is self-propagating.** A run whose diff creates a new build README authorizes the NEXT run.
   Unrefused: §9 names the only thing that would.
5. **It approves the SCOPE of every spec inside it.** A unit whose spec is reachable at BASE carries
   the owner act that authorized the run, so a build folder committed with a spec the owner left
   unapproved has approved it. Ratified 2026-08-17. The alternative — only a spec past
   awaiting-approval counts — deadlocks: the method REQUIRES a run to author a missing spec at
   exactly that status, so a run would author a unit it could never build.

All were put to the owner and accepted.

**A unit AWAITING SCOPE APPROVAL has three dispositions and they are not interchangeable.** Reachable
at the pinned BASE: cost 5 already approved it, proceed. Authored by the run itself: the method's
authoring rule governs, nothing is awaited. Present at BASE under a status naming an EXTERNAL
PREREQUISITE: halt with the external-prerequisite code, NOT the scope-approval one — different owner
turns, and conflating them tells a returning owner to approve a scope when the blocker is outside the
repository.

**A fork with no delegated resolver is parked THROUGH THE VERB, and the run continues.** Not noted in
prose, not left for the wrap-up to notice: `--park` is what a gate reads. The run then carries on with
the units that do not depend on that fork. Only when EVERY remaining unit depends on it does the run
halt, with the fork-unresolvable code — a run that can still make progress on something else is not
stuck, and stopping early spends an owner turn that was not needed.

**The build method is a RUN-TIME dependency of this kit.** Every directive is a pointer into a
section of `<MEMORY_ROOT>/guides/BUILD-METHOD.md`, so `--preflight` refuses a tree where it is absent rather than starting a run bound
by a set that resolves to nothing.

Absent or unreachable authorization → the run does not start. There is no override for this one: an
override on the authorization check is the authorization check.

**A SECOND item joined that set**, and the driver holds it as a declared list rather than a name in a
case arm. `pieces-complete` is not overridable either: it is the item that says a `recipe`-mode run
produced what the owner asked for, over content nothing else on the merge bar can grade, so an
override on it is the run certifying its own output. `--abort` is the honest exit when it cannot be
met. The build that introduced the item ratified this as an acceptance criterion and then shipped
without it — found by writing the arms that item had never had.

## 2. The run-state file

`<MEMORY_ROOT>/builds/<slug>/RUN.md`, split mechanically rather than by discipline.

**Generated** — and the marker pair is now EMPTY by contract. The unit list and per-unit status are
DERIVED from the build README on every read, never copied here, and the gate asserts the region holds
no copy.

This inverted an earlier design where the region WAS a copy the gate byte-compared against its
source. That equality was unmaintainable: folding a review bumps a spec rev, which moves the build
index, which makes the copy stale — and the region's only writer was `--preflight`, which refuses
once a run is live. The refusal told the reader to "re-run the driver", naming a path no verb walks,
so a run that hit it could only hand-edit an artifact this document calls generated. Deriving removes
the class instead of adding a verb to service it: one fact, one home.

### A build gets more than one run by ROTATING the finished one

A record that has reached a terminal phase is not something to move, re-open or re-pin, and every
phase writer refuses one. That is right about the RECORD and was wrong as a policy about the BUILD:
a build whose first run aborted could never be carried unattended again.

So `--preflight`, and only `--preflight`, RETIRES a finished record instead of refusing it. The
retired file is renamed to `RUN.<phase>.<blob8>.md` beside the live one — the terminal phase, then
the first 8 hex of that record's own blob hash — and a fresh `RUN.md` is created at `RUNNING`. The
name is DERIVED, never chosen, and it is derived from the BYTES rather than the witness because no
verb here commits: two runs can honestly share a witness, and a name that collided would block every
later run with no way out. Two records with the same content are the same record twice.

What rotation does NOT do: it does not re-open, re-pin, or edit the retired record. Its bytes are
preserved exactly, `git mv` puts both sides in the index in one operation, and the gate leg reads
every archived record as part of its population — an archived record carrying a non-terminal phase
reds. The collision test runs with the other preconditions, so a name that already exists carrying
DIFFERENT bytes refuses over an untouched tree; the rename itself runs after every precondition has
passed, because the rename is what makes the tree dirty.

**Authored**, carrying these facts and nothing else. NO COUNT IS WRITTEN HERE: it was re-derived
once and was still wrong, because the list below omits `mode` and the two keys `--attest` writes. The
set is the driver's `set_fact` keys plus those; count it there. CREATED by `--preflight` and staged;
the owner authors none of it. Nothing in the tree derives any of them, which is the test for
belonging here:

1. **The phase**, from the vocabulary in §3, each claim carrying a witness.
2. **The keepalive id**, recorded by `--preflight` from the value the agent hands it (§5).
3. **Parked entries**, whose kinds `park()`'s own kind argument discriminates: a parked DECISION —
   the question, the options seen, and the reason the run refused, because a bare "parked" is
   indistinguishable from "forgotten" — an ABORT reason, a DoD OVERRIDE, an owner directive WAIVER
   (§10), a PROPOSAL, a RESCOPE amendment, a DISPATCH write-set declaration, a REVIEW round and a
   BRIEF. Each names its writer: `--park`, `--abort`, `--close --override`, `--preflight --waive`,
   `--propose`, `--rescope`, `--dispatch`, `--review` and `--brief`. DECISION had no writer for as
   long as this contract has instructed a run to park one, so the instruction could not be obeyed —
   a rule with no route is a rule nobody follows, and a build had to hit it to notice.

   **Every kind belongs to one of two CLASSES, and the classes are not the kinds.** A `surfaced` kind
   the owner must be shown; a `history` kind they need not adjudicate. DECISION, ABORT, OVERRIDE and
   WAIVER are `surfaced`, the waiver included, since §10's waiver entry reaches the owner through the
   same wrap-up.
   Membership is declared on TWO AXES, both the driver's. The KIND axis is `PARK_KINDS_OWED`. The ACT
   axis is `PARK_ACTS_OWED`, naming the `rescope` acts the owner is owed — `retire` and `supersede`,
   because M3 delegates a build's scope RESOLUTION and not its ABANDONMENT, while `add` stays history
   as the declaration it is. `history` is the COMPLEMENT on both axes, so there is no third list to
   keep in step and no row is counted twice. A SECOND constant rather than a `kind:act` grammar inside
   the first: the leg greps this driver for a `park` call site per owed member, and no
   `park "$rel" rescope:retire` site can exist, because the act is a field of the reason. The split
   exists because a count of decisions the owner must adjudicate is worthless once append-only round
   history shares the region. The first `history` kind is `review`: a round carries a verdict and a
   count, not a question. Its shrink-only floor is NOT armed — the sets beside it pin from the project
   conf, and a new key there is a public surface nobody asked for. Said plainly: an unpinned set can
   quietly shrink.

   The PROPOSAL is the only kind owed no ANSWER, and the only one with a further field: the playbook
   STEP it amends, written between item and reason because the reason is line-final and both readers
   match up to it. A run FOLLOWING a playbook may not edit it — one that rewrites the checklist it is
   graded by has no rules left — so what it noticed goes here and the amendment is a separate run.
   Nothing blocks on a proposal, and `--status` counts them apart from the questions.
4. **The run's BASE sha**, pinned once at run start. It is a runtime observation with no
   re-derivable source: a build with N sub-specs has N per-unit bases, none of which is the run's.
5. **The anchor ref name**, as the remote advertised it for its own HEAD at pin time.
6. **The anchor tip sha**, from that same advertisement.
7. **The endpoint URL** it was observed from.
8. **The roster AT LANDING**, frozen by `--landed` alone. While a run is LIVE the unit list derives
   from the build README, which cannot go stale between reads. But a FINISHED record must still say
   which units the run covered, and that README is mutable: a later build adding a unit would change
   a landed run's answer retroactively. Freezing the ids keeps a terminal record a record.

9. **The anchor KIND**, `default-branch` or `run-branch`, recorded by `--preflight`.
10. **The branch ref name**, as the remote advertised it — present only when the second anchor fired.
11. **The branch tip sha**, from that same advertisement, and present under the same condition.
12. **The HALT CODE**, written by `--abort` alone and validated against the effective vocabulary
    before recording. A single `ABORTED` terminal says a run stopped and never why; the parked reason
    is prose for the owner, and this is the field the status line, the resume path and the gate leg
    join on. Present only on an aborted record, under facts 10 and 11's reading.

Facts 10, 11 and 12 are ABSENT on a run that did not reach the condition each records — a
default-branch run for the first two, a run that did not abort for the third. That is legal: the
"nothing else" clause bounds what may appear, not what must. Fact 9 is always written.

**A `<key>-source:` line is ADMITTED beside a fact no verb could write**, and its value states why
none could plus what independently verifies the value. A hand-reconstructed fact carrying no such
line sits outside the "nothing else" clause; a labelled one is inside it. The form exists because
repairs happen — a record whose key predates the verb that would write it, or whose verb refuses a
terminal record, is correctable only by hand — and an UNLABELLED hand edit is indistinguishable from
a value the run earned. Nothing reads these lines and no verb writes one: the label is for the
reader, and writing it is an owner-authorized repair rather than something a run does to its own
history.

Facts 5-7 and 9-11 are EVIDENCE and are never read back as inputs — fact 9 emphatically so. A verb
branching on the recorded anchor kind would take a security decision from a value its subject wrote,
the class this kit has been burned by three times; the derivation is monotone instead. They exist
so a party outside this process can re-derive the pin without trusting a byte the run wrote, which is
the only form of verification §9 concludes actually binds.

The authored half never restates a derivable fact — not a unit status, not a per-unit spec base.
Restating the run's own BASE is not possible, because nothing else holds it.

**The anchor ban.** A dash or pipe row leading with an id ANCHORS that id under this build folder,
which makes the build a claimant of it. A run-state file naturally wants to write cross-build rows —
a parked dependency, a blocked unit elsewhere — and that is exactly the shape that collides. So
authored rows cite ids **inline in prose** and never lead with a dash or a pipe followed by an id. A
sha and a workflow id are safe on both counts. A planned unit is minted as a backlog row before the
run-state file names it, and is NAMED rather than LINKED until its record exists.

**The size budget and the spill rule.** The file is in the index set, carries the tree's index caps,
and is designed to GROW. The authored region is budgeted at 8 KB; at the budget the oldest parked
entries spill into the build's `build/` folder as a dated recording — a name the recording grammar
admits — and the region keeps a one-line pointer. **Waiver entries are not spillable.** Written at
preflight they are permanently the oldest, so the rule would evict them first, after which the leg
check grading them passes by finding nothing. Crossing the cap mid-flight reds the gates, which
blocks `--close`, which leaves the override as the only exit: the spill exists so that never
happens.

## 3. The phase vocabulary

Kit-owned core, in run order:

`PREFLIGHT` · `RESEARCHING` · `TESTING` · `SPECCING` · `REVIEWING` · `FOLDING` · `BUILDING` ·
`RUNNING` · `VERIFYING` · `LANDING` · `LANDED` · `ABORTED`

Named for the build method's PASS kinds:

`SPECCING` · `REVIEWING` · `FOLDING` · `BUILDING`

— so a run's phase and the pass it is performing are one vocabulary rather than two. The list is a
DECLARATION in the driver and this paragraph is joined to it in both directions, because a phase
added and casually called a pass kind is a claim no row join can see.

**`RESEARCHING` and `TESTING` are POSITIONS, not pass kinds.** The build method closes its pass set
and neither is a member, so a prompt-started run OCCUPIES them while performing the passes that set
does name — the commit boundary and the regrounding points stay exactly where the method puts them. `RUNNING` survives with a stated meaning — a run
between named passes — because the core set is shrink-only and deleting a member lowers the floor.

`LANDED` and `ABORTED` are terminal. `LANDING` is the state a slot-status vocabulary cannot express
— built and reviewed, not yet merged — and it is why the run-state file is deliberately outside the
status-vocabulary check.

A project MAY append members via `PHASES_EXTRA` in `.unattended.conf`. It may NOT delete a core
member: the gate pins a shrink-only COUNT of the core set (`CORE_FLOOR`), because a
deletable core member is a silent, reason-free override of everything keyed on it — and a
membership assertion cannot work here, since the checker composes the effective set FROM core.

**Every phase claim carries a witness** — a sha, a tag, or a workflow id — and the witness must be
PRESENT. Presence is its own refusal, checked separately from whether the witness resolves. The
drift oracle counts a claim with no sha of its own as unjudgeable and skips it, so naming no witness
is otherwise the cheapest way for a run that cannot substantiate a phase to say nothing at all — and
the run is the sole author of that field.

**A claim of a TERMINAL phase carries a sha specifically**, narrowing the three shapes above. At
`LANDED` the ancestry of the witness IS the claim: the gate asserts it lies on the history an anchor
blesses. **There are TWO anchors and the record says which answered.** The remote's advertised tip is
the strong one and is tried first; the local default branch is the fallback, for a build merged
locally that cannot push. `landed-anchor` carries `remote` or `local`, and §9 states what the weaker
one does not buy. A tag or workflow id there is unjudgeable, and a terminal claim is where that costs
most — it is the last thing written and nothing re-examines it.

**Terminal is reached by a verb that evaluates what the phase claims, and never by a phase move.**
`--phase` writes the positions between; `--landed` and `--abort` write the two ends. `LANDING` is
close-only for the same reason: it is the record that the Definition-of-Done set was evaluated, so a
phase move into it would be that claim without the evaluation, and `--landed` accepts a record only
at `LANDING`. A run that is already terminal cannot be moved at all.

**Concurrent runs are PERMITTED; a run is never refused because another build is live.** The driver
ANNOUNCES them at `--preflight`; the leg persists its report to its `gate-logs/` entry, which a GREEN
bar does not echo. Neither fails on the count. It replaced an at-most-one-live-run rule grounded on
"the run" being ill-defined otherwise — nothing keys on it, because every verb is slug-addressed.

**A build folder still carries at most one live record** — one `RUN.md`, and the leg refuses an
ARCHIVED record in a non-terminal phase. That is now the only check grading a phase for it.

**One residual:** two runs CLOSING together in one clone contend on the bar's turnstile, whose queue
wait is charged against the gate bound, so the second can fail `gates-green` for contention.

## 4. The Definition of Done

Twelve kit-owned core items. Each names its checker, because an override budget must not be spent on
something no machine could have checked:

| Item | Checked by | Asserts |
|---|---|---|
| `gates-green` | machine | the project's full merge bar ran on the tip being landed and passed |
| `records-current` | machine | the run-state file's GENERATED region is EMPTY — the unit list is derived from the build README on every read, so "current" is the absence of a second copy rather than a comparison between two — AND both marker pairs are well-formed, the run-state file's own and the build README's. Well-formedness is read from the region reader's EXIT STATUS, not from empty output: a malformed pair prints nothing and exits non-zero, so testing emptiness alone scores a broken pair as SATISFIED, passing loudest when the file is least readable. This cell once described a fresh-render comparison against unit status headers the driver never reads, which made an ordinary spec rev bump block the close with no reachable repair |
| `authorization-reachable` | machine | the build README is reachable from the pinned BASE, parses as build front matter, and names this build |
| `landed-via-lander` | machine, PRE-LANDING | a lander is DECLARED, and that is the whole predicate: the bypass-flag grep it carried duplicated leg check 11 and is gone. It runs inside `--close`, BEFORE the landing it names, so it cannot observe the push nor fail for anything the run did. The observation lives in `--landed`, the only verb after it |
| `build-complete` | machine | the build's authored roster names no unit that is unspecced or unfinished. SIX terms, all required; the generated region must be NON-empty, because "no unit row is non-terminal" is vacuously true over no rows at all |
| `closing-review-recorded` | machine | a TRACKED review record under this build carries a `diff-review` binding line AND names a commit between the pinned BASE and HEAD, decided by git ancestry rather than by a substring. The RANGE is what admits a fold-scoped round, whose base is a descendant of BASE; the KIND is what stops a spec audit standing in for a closing review. It measures TWO things and neither is a judgement about the review's content: that a review of what shipped exists and is bound to THIS run, and that the run's own `--review` loop for the build slug reached one of its three declared exits, with `CONVERGED` implying zero blockers. A review record is a document; a loop that never ended is a run that stopped reviewing, and only the second is readable |
| `pieces-complete` | machine | this run produced the number of pieces its build README asked for at the pinned BASE, each joined to a record by content hash and each recording a PASS for every declared per-piece leg. SCOPED to recipe-mode runs: term zero meets it and announces the skip for any other mode, because `--close` evaluates this set for every run and an item only one mode can satisfy would block the rest of the fleet |
| `set-checks-recorded` | machine | every set-scoped check the playbook declares recorded a PASS for THIS run's set. It reads the VERDICT and not merely its existence — a set check is a declared leg with a binary anchored verdict, unlike the prose review `closing-review-recorded` can only assert the existence of. Same mode scoping |
| `specs-audited` | machine | every unit the generated region carries as CLOSED is named by a TRACKED record under this build whose first twelve unfenced lines carry a `**Serves:**` line of kind `spec-audit`. The id join is WHOLE-TOKEN and expands the `N..M` range the binding grammar admits: a substring join lets `TOOL-x-19` satisfy `TOOL-x-1`, and an unexpanded one blocks a unit that WAS audited. It measures that the pre-code pass left evidence; it does not read what the audit found, whether it ran at the unit's current rev, or whether a WONTDO unit was audited — a LOWER bound, safe as a refusal and useless as a certificate |
| `reuse-probed` | machine | a recall probe actually RAN in this run's tree — the liveness half of `reuse-first`, whose tracked half is whatever the memory kit demands of a spec's reuse section. Five outcomes, three of them MET: the directive was WAIVED, and the item reports the waiver and its reason, which is what stops a waiver being silent; `RECALL_CLI` is blank or unreadable, an announced skip, because a core item no adopter without a recall kit could meet would block every close in their fleet; or queries are recorded, and the count rides the message. UNMET splits the two facts an operator must not confuse: the log is ABSENT, so the item cannot answer, versus the log exists and holds nothing for this tree, so the probe was not run. It is NOT a merge-bar leg and cannot be one — the query log lives in the git common dir, is neither tracked nor pushed, and a leg reading it in a fresh clone could only report DEAD PROBE. What it does not observe: that the probe was run FOR this build rather than earlier in the same worktree |
| `keepalive-reaped` | agent-attested | the scheduled keepalive was deleted — written by `--attest <slug> --item keepalive-reaped` |
| `parked-decisions-surfaced` | agent-attested | every parked entry reached the wrap-up — written by `--attest <slug> --item parked-decisions-surfaced`, which DERIVES the record key (`parked-surfaced:`) so no operator spells one. **The value MAY carry a count** via `--value`, and then `--close` refuses unless it equals the number of `surfaced`-class parked lines — "I surfaced them" becomes "I surfaced N, and the record holds N". Still agent-attested: no machine observes a wrap-up. Omitting the count keeps the old behaviour, so an older record is not retroactively red. The overrides this same `--close` is about to write are excluded, because the DoD is evaluated before they land |

A project MAY append items via `DOD_EXTRA`. It may NOT delete a core item; the gate pins the core set's
COUNT against the same shrink-only floor, for the reason §3 gives.

`--close` BLOCKS on any unmet item. The override is named (it cites the item), recorded (it writes a
**The two attested items have a VERB, the only way to write one.** `--attest <slug> --item <item>
[--value <text>]` refuses a machine-checked item by reading its declared CHECKER, so a project
declaring its own agent-attested extra gets the verb and one renaming a machine item gets the
refusal. Before it existed the keys had no writer, which made `--abort` — the sole documented exit
from a wedged run, requiring both — reachable only by hand-editing the authored region of a file this
kit calls generated. The verb removes the hand edit, not the trust assumption §9 states.

parked entry), and surfaced in the wrap-up. The two agent-attested items do **not** spend the
override budget: attestation is not a machine verdict, and pretending otherwise makes an override
look like a check that failed.

**`authorization-reachable` has NO override, and this is where a close meets that.** §1 states it at
run START, which is where the rule is decided and not where it is hit — an agent whose close refuses
is reading this section. An override on the authorization check IS the authorization check, so the
verb refuses the pair rather than recording it. There is no waiver, no attestation route and no
project escape: an item the kit will not let a run override is the one item whose absence would make
every other check decorative.

## 5. The keepalive — an AGENT obligation

The scheduling store is in-memory and session-scoped, and deleting a job removes it from that same
store. **No script can reach it.** So the obligation splits by actor, and the split is not a
convenience:

**What this section does NOT say, because it said it for four kit versions and it is measured
false: that the job dies when the agent process exits.** It may not.
`TOOL-aPromptedMandate-11` records a run asserting exactly that about two jobs, twice, while the
scheduler's own listing showed both still firing. Treat a job you did not schedule as ALIVE until a
delete says otherwise. The consequence is section 5's resume rule below, and the reason the reap is an
obligation rather than a formality: the failure mode of assuming death is a keepalive firing forever
under a green `keepalive-reaped` attestation.

- The **agent** schedules the keepalive as the run's **FIRST act**, before any orientation and
  before `--preflight`, on **every** start path — and reaps it before the run reaches a terminal
  phase. It uses the tool calls its own project layer declares — `KEEPALIVE_CREATE` and
  `KEEPALIVE_DELETE` in `.unattended.conf`, because an adopter's harness exposes a different
  scheduler and a kit that hardcodes one repo's spelling is wrong everywhere else.
- **"First act" replaces "before the run leaves `PREFLIGHT`", which was this sentence for four kit
  versions and is the weaker claim.** A run enters `PREFLIGHT` only when `--preflight` writes that
  phase, so the old wording was satisfied by scheduling at preflight time — and two of the four start
  paths do their longest unattended work BEFORE that instant. A prompt-authorized run orients from
  prose, runs the research-then-test loop its `prompt`-scoped directives oblige, writes a build
  folder and pushes a branch, all before its first verb. That stretch is where a run is most likely
  to stall and was the one stretch nothing could wake it from.
- **A run that never STARTS still owns the job it created.** Where a start path refuses — a `--prompt`
  value that does not resolve, an anchor scope that cannot authorize the mode, any of `--preflight`'s
  refusals — the agent reaps the keepalive before it stops. The store is session-scoped, so a job
  left behind by a run that never began is orphaned in exactly the way one left by a run that ended
  is, and there is no run-state file for a later reader to find it through.
- The **driver** RECORDS the id the agent hands it, and later ASSERTS that a reap was recorded. It
  never schedules and never deletes, and it labels the item agent-attested wherever it reports.

A driver verb that claimed to schedule or reap would be claiming an effect it cannot produce.

**RESUME is the third case, and it is the one the actor split does not cover.** A resumed session did
not schedule the job the run-state file names and cannot assume it died with the process that did.
So it REAPS that recorded id first, reads the result back and reports it, and only then schedules a
replacement. `--keepalive-id` is accepted by `--preflight` alone, so the new id cannot be recorded:
the `keepalive` fact keeps naming the old job, the close attestation covers both, and the wrap-up says
which. Ordering matters — reap, then schedule — because the reverse leaves the run holding two jobs
and a record naming neither correctly.

## 6. Landing

The run lands through the project's declared lander (`LANDER` in `.unattended.conf`) and **never**
with a hook-bypass flag. A project whose pre-push hook refuses an un-marked default-branch push has
made the lander mandatory on purpose: it reconciles the remote BEFORE the gate, so the gate never
runs on an already-stale tree. An unattended run that meets that refusal with nobody to interpret it
either stalls or learns to bypass — and bypassing discards the entire bar the mandate leaned on.

`landed-via-lander` is the machine-checked DoD item for this, and the gate greps the close path for
a bypass flag in both directions: the lander must be present, the flag must be absent.

**`LANDED` is reachable on either of two anchors, and the ORDER is the rule.** The remote's own
advertised tip is attempted FIRST: that is an observation of an external party and is the only thing
here a run cannot construct for itself. Only when it fails does the local default branch answer, and
then the arm asserts that the run's OWN BRANCH TIP is an ancestor of it — never that HEAD is, which
on the default branch is a commit compared with itself. The run-state file records which anchor
answered, because a record that cannot tell an observation from an assertion has thrown away the
distinction that matters most.

Listing two anchors without ordering them would permit an implementation that always takes the
cheaper one, retiring the observation while satisfying every word of this section. The ordering is
what preserves the strong claim wherever the strong claim is available.

## 7. The verbs

The eighteen verb entries live in `UNATTENDED-VERBS.md`, installed beside this file from the kit's
`VERBS.template.md` and byte-compared against it by the same leg that compares this pair. Read them
there. Nothing about any verb changed in the move.

The move was a BYTE decision and is recorded as one. This document had reached its cap EXACTLY, and
a contract with no room left to state its next rule has stopped being amendable — which is a
failure mode of the contract, not of whoever wrote the rule that would not fit.

## 8. What a project declares

In the repo-root `.unattended.conf`. Blank or absent turns the corresponding assertion off only
where this document says it may:

| Key | Meaning |
|---|---|
| `MEMORY_ROOT` | the memory tree's root, matching the memory-tree kit's conf |
| `LANDER` | the mandated landing command |
| `BYPASS_BAN` | the flag the close path must never emit |
| `GATE_CMD` | the full merge bar, for `gates-green` |
| `GATE_BOUND` | the wall-clock bound, in seconds, on `GATE_CMD` and `WIRING_CHECK`. OPTIONAL: absent takes the kit default and says so on stderr; non-numeric or zero is a refusal |
| `WIRING_CHECK` | the non-repairing wiring check `--preflight` delegates to |
| `KEEPALIVE_CREATE` · `KEEPALIVE_DELETE` | the agent-facing scheduler tool calls, named for the agent to use |
| `KEEPALIVE_INTERVAL` | the cadence the agent schedules the keepalive at, rendered into the Skill as prose |
| `ANCHOR_SCOPE` | which anchors may authorize a run: the CLOSED set `default-branch` and `published`. Absent, blank or outside the set keeps `default-branch`, so a typo grants nothing. Gates the DRIVER only — §1 cost 2 |
| `AUTH_PARAM` | the token an invocation must carry to start a prompt-mode run, rendered into the Skill at its routing row and its opening fence. BLANK or absent is the kit default, which that render states verbatim rather than this table restating it. Its ARGUMENT is a prompt file path or the prompt itself. A value that is not a hyphen-led flag, or that carries whitespace, a pipe or a backtick, is refused at render time — it is interpolated into a table row and a code span, and each of those three characters ends one of them early. Gates NOTHING at run time: no script sees the invocation, so this is the gesture and never the authorization, which stays the pushed build folder (§1) |
| `CORE_FLOOR` | `<phases>:<dod>`, the shrink-only SIZE of the kit's core sets. MANDATORY: undeclared or malformed leaves both pins unenforced, so both are refusals |
| `DIRECTIVES_EXTRA` | project directive members, appended to the core set |
| `DIRECTIVES_FLOOR` | the shrink-only SIZE of the kit's core directive set. MANDATORY, for the reason `CORE_FLOOR` is |
| `PHASES_EXTRA` | project phase members, appended to the core set |
| `DOD_EXTRA` | project DoD items, appended to the core set |
| `KICKOFF_ENGINE` | the kickoff engine whose hand-back the gate reads; BLANK turns that check off |
| `KICKOFF_EXITS` | a shrink-only floor on how many interactive exits that engine resolves without an owner turn |
| `HALT_CODES_EXTRA` | project halt codes, appended to the core set |
| `HALT_FLOOR` | the shrink-only SIZE of the kit's core halt-code set. MANDATORY, for the reason `CORE_FLOOR` is |
| `LANDER_MARKER` | a bare NAME, resolved by the lander and by `--landed` against `git rev-parse --git-common-dir` — never a tree-relative path, which names a different file in each half and is unwritable in a linked worktree. BLANK asks for no observation |
| `DIRECTIVES_EXTRA_TABLE` | a repo-relative file carrying Skill-shaped rows for whatever `DIRECTIVES_EXTRA` declares. Undeclared is the empty set |
| `PASS_ORDER_CUTOFF` | the date from which a CLOSED unit whose BUILD COMMIT predates a conforming spec reds the `pass-order history` leg. Graded on the README's `opened:` date. BLANK turns the term OFF and the leg announces it |
| `SPEC_THIN_CUTOFF` | the date from which a CLOSED unit whose spec grades THIN — an empty scope, acceptance or gates section — blocks `build-complete`. Graded on the spec's FILENAME date, so no landed spec goes retroactively red. BLANK or absent turns the term OFF and `--close` announces that it did |
| `UNITS_REGION_CUTOFF` | the date at which an absent units-region marker pair becomes a REFUSAL rather than an opt-out |
| `RECALL_CLI` | the repo-relative path to the retrieval CLI whose query log `reuse-probed` reads. OPTIONAL: blank or absent means the recall kit is not adopted, and the item then reports an ANNOUNCED SKIP rather than an unmeetable UNMET, so a project that took this kit and not that one is not wedged by a core item it can never satisfy. A DECLARATION rather than a path in the driver, because a kit literal in shipped bytes resolves to nothing in a tree installed at another prefix — the carried-prefix ratchet reds on exactly that |
| `SHARED_RECORDS` | the records a concurrently dispatched pass may never declare a write under. Blank is the empty set |
| `GENERATED_INDEXES` | `index:generator` pairs. An index ALONE is fine; only the index TOGETHER WITH its generator is refused. Blank turns that half off |
| `LANDED_ANCHOR_CUTOFF` | the date from which a `LANDED` record must name its anchor kind. A record whose first commit predates it is read as `remote`; blank or absent grandfathers every record |

An empty declaration is a refusal, not a pass: a vocabulary with no members and a DoD set with no
items would both make every check keyed on them vacuously true.

## 9. The boundary this kit claims

**The local landing anchor is a new instance of exactly this, and not a new kind of thing.** A local
ref is inside the run's reach: one `update-ref` moves it, with no network and no push, which is the
same lever this kit already records as a reproduced bypass against a remote-tracking ref. So a
`local`-anchored `LANDED` is a RECORD that a merge happened, never an OBSERVATION that it did. The
remote arm stays first and stays an observation; the recorded anchor kind is what keeps the two from
being read as one claim. This is stated rather than fixed, because refusing the local arm is what
would restore the deadlock it exists to remove — a build merged locally with no reachable terminal.

Nothing a script running under the run's own uid constitutes authorization. Four independent
mechanisms were designed for the anchor and all four were broken by adversarial review; they
converged on one reduction. A check running as the run reads refs, objects, worktree files and
config, and the run writes all four — so if every input is local, the run can construct the passing
state exactly. The escapes are a secret the run lacks, or an observation of an external party, and
both leak here for the same reason: what an external party returns is a NAME, and dereferencing a
name happens in the subject's own object store.

This kit therefore makes an unauthorized landing require a visibly deliberate act, and records which
act was taken. It does not prevent one.

**What it closes.** Two one-command offline forgeries that used to pass every check silently: a
rewritten remote-tracking ref, and a default-branch name supplied through the environment. Both are
now inert rather than detected — neither value is read at all. Two more are neutralised for this
kit's own reads and named where they sit: an object-substitution ref and a graft file, either of
which rewrites what a sha MEANS at a perfectly honest anchor — and both are ALSO refused by their
mere PRESENCE, because suppressing them makes only THIS kit's reads honest and binds no other tool
reading the same objects.

**What the second anchor changes here.** It opens no new class — §1 cost 4 already granted
successor-authorization. It lowers that price to two commands and widens the leg's BASE check for
every adopter. Neither is closed; what survives is what survived before, the leg re-run in a clone
the run never touched.

**What it does not close, stated so no reader has to discover it.** A run that edits this kit and
commits it — nothing binds the executing code to code an owner approved. A run that shims the
ordinary tools this kit calls. A run that skips the hook layer, by `--no-verify`, by pointing
`core.hooksPath` at an empty directory, or by overriding the gate command. A run that relays through
an endpoint it seeded, which satisfies every URL comparison with one URL and one config source. A
run that simply never creates a run-state file, since every leg check iterates over the tracked ones.
And a run that gets one push past all of that, after which the remote's advertisement is genuine.

**What actually binds.** None of those levers travels with a push. The same leg, re-run in a clone
the run never touched by a party the run cannot execute code as — a required status check, or a
second node — is immune to the whole class, provided the run's own push credential cannot alter the
required-check ruleset. This kit can neither install that nor substitute for it, and no document here
may imply otherwise.

## 10. The default directive set

A run is bound by a set of named DIRECTIVES. Each is a POINTER into a section of the project's build
method at `<MEMORY_ROOT>/guides/BUILD-METHOD.md`, never a copy of the rule it points at — the method's own M1 forbids a rule appearing both
there and in a carrier it points at, and this contract is a carrier.

**Kit-owned, and the project may only EXTEND.** The core set is a constant in the driver, read by the
gate leg through the same parse it uses for the phase and Definition-of-Done sets. `DIRECTIVES_EXTRA`
is where a project adds; the core is not deletable from the project layer, and `DIRECTIVES_FLOOR`
pins its size shrink-only for the reason §3 and §4 give for theirs. A conf key holding the whole set
was rejected: a project could then declare zero directives, which is a global waiver carrying no
name, no reason and no record.

**A directive may be SCOPED.** A registry entry is `<handle>:<section>[:<scope>]` over the closed set
`all` / `prompt`. An absent third field is `all`, so every entry written before scopes existed keeps
its meaning exactly. `all` binds every unattended run; `prompt` binds only a run whose build README
declared `authorized-by: prompt`, because research and a solution test are obligations of a build
whose solution was not given — imposing them on a run whose specs already chose one would be
ceremony, not rigour.

The scope is KIT-OWNED for the reason the set itself is: a project-selectable scope is a narrowing of
the core wearing another name. A waiver of a `prompt`-scoped handle on a run that is not
prompt-authorized is REFUSED rather than recorded, since a waiver relaxes a rule that never bound
that run. That refusal is evaluated where the mode EXISTS — after the authorization read, not beside
the other waiver checks — and an underivable mode refuses rather than grants.

**This section names no handle.** The list an agent reads is the table in the rendered Skill, and
naming it twice is the drift the pointer design exists to avoid. The leg joins the two in both
directions, so a handle in one and not the other is a refusal rather than a discrepancy nobody sees.

**A waiver is the owner's, taken once, at preflight.** `--waive <handle> --reason <text>` is accepted
by `--preflight` and by no other verb, and only while no run-state file exists or the requested set
equals the recorded one. That single refusal is what makes the owner turn provably the LAST one: no
later verb can take an answer, and a re-preflight after a compaction re-issues the recorded set
rather than opening a new turn. A waiver with no reason is refused, because one that records no
reason is indistinguishable from one nobody meant.

**What a waiver reaches, and what it does not.** It is recorded as a parked entry of the `waiver`
kind, so the wrap-up derivation surfaces it with the other parked kinds. It relaxes the DIRECTIVE for
that run only. It is **never a Definition-of-Done override** — the two are separate acts with
separate records, and `--override` remains the only route to a DoD item. And it **never removes a
GATE**: a directive relaxed here does not relax any check the merge bar performs, so a waiver whose
directive has a machine-enforced consequence still meets that consequence at the bar.

## 11. The adoption rule — a discovery joins the running build

An attended run hands a discovery to the owner. An unattended run has no owner to hand it to, and a
discovery filed as a question for an absent reader is not preserved — it is discarded, with a record
that makes the discarding look careful. So under a mandate the disposition changes: **a strictly
beneficial discovery is ADOPTED into the running build and decided in its favour at the moment it is
found.**

**A DISCOVERY is anything the run learns that it was not looking for.** A defect in a path it read, a
measurement that contradicts a record, a cheaper mechanism for something the tree already does — and
a BLOCKER standing between the run and its own landing, which is the case a run is most likely to
mistake for an owner's question. Most discoveries happen in ORIENTATION, before the spec set exists,
which is why this rule binds from the run's first act rather than from its first pass.

**STRICTLY BENEFICIAL is a TEST, not an adjective.** A discovery qualifies when all three hold:

1. it makes an observable this repo ALREADY measures strictly better — a gate that reds where it
   should, a leg that costs less wall clock, a record that stops being false — and the improvement is
   MEASURED rather than argued;
2. nothing this repo measures gets worse: no acceptance criterion, no gate leg, no declared budget or
   shrink-only pin, no security, data or write surface;
3. it survives the build method's M3 vetoes unchanged.

**Three dispositions, and choosing between them is not a judgement call.** Passes all three → ADOPT,
now, by the run that found it. Fails 1 or 2 → a BACKLOG row naming what was seen and why it was
declined, which is a decision the run TOOK. Trips a veto → PARK, with the question, the options and
the refusal, which is a decision the run REFUSED. **Veto 2 is the one that bites**: a discovery
needing a new external dependency, a new install location, a new public surface, or a change to a
governance carrier is an owner turn and is parked.

**Adoption is the M2 ADD act and introduces no authority.** M3 already delegates a build's own scope
to a standing mandate through M2's amendment acts; what was missing was the instruction to use it.
Record it with `--rescope <slug> --act add --item <unit-id> --reason "<what the run found>"`, spec the
unit at its tier, and build it like any other. The build README's GOAL statement is NOT amended — a
unit is added beside the goal, never in place of it — and on a project whose `ANCHOR_SCOPE` is
`published` a grown roster is committed AND PUSHED before the next authorization read.

**Decide AT ONCE.** A discovery adopted late costs a second pass over the same code; a discovery
deferred costs the whole finding. The corpus is unambiguous on this: a run that recorded a measured
sixteen-fold improvement, parked it, was told to proceed, and parked it a second time. "Write it down
and move on" is not a stable state under a mandate, because the reader it defers to is the one who
left.

**What this does NOT license.** It is not permission to widen a build with work that is merely good.
A refactor nobody measured, a rename, a "while we are here" is not a discovery — it is taste, and
taste is the owner's. Clause 1's operative word is MEASURED: a run that cannot state the measurement
has not made a discovery, and a run that adopts on preference has taken the owner's turn rather than
substituted for it.

**THERE IS NO MACHINE HALF, and this section says so rather than implying otherwise.** Nothing in
this kit can observe a discovery a run did not record, so no gate can tell an adopted discovery from
one silently dropped. What IS observable afterwards is the trail each disposition leaves: an adopted
one leaves a `--rescope` row, a spec and a unit in the roster; a declined one leaves a backlog row; a
parked one leaves a parked entry the wrap-up surfaces. That is the property parking-everything
destroyed, and it is the closest thing to enforcement this rule has.

## 12. The pass sequence is DRIVEN, not remembered

Nothing carried a build's pass order but the agent performing it, and across a compaction that agent
is a different reader. The failure is what you would predict: a unit built before it was specced, the
spec written afterwards, and no record of what the builder was handed.

**The route is the kit's build harness**, taken in `prompt` and `slug` mode. It drives SPEC, AUDIT
and BUILD as stages of ONE program, so BUILD is unreachable except through both and on a TERMINAL
`--review` verdict. Recipe mode does not take it: its pieces are not specs.

**TWO LIMITS, as rules rather than caveats, because a reader who assumes them away trusts the harness
for what it cannot do.** It buys ORDER and never ENFORCEMENT — a Workflow script has no filesystem,
so every observation it makes is a claim its own agent returned, and what refuses is `--dispatch` at
the moment of the act and the pass-order leg over the commit graph. And it does not cover
orientation, preflight, the owner turn, closing, landing or the keepalive: those are main-loop acts,
and the run-state file joins the two halves.

**A build pass owes a recorded BRIEF** (`--brief`), so "which instructions produced this diff" has an
answer on disk, **and is DECLARED through `--dispatch`**, which makes the refusal reachable on a
sequential pass and not only a concurrent one — a rule enforced only where two passes race misses
every ordinary build.
