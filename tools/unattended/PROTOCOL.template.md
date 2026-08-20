<!-- gov:kit unattended@1.7 -->
# Unattended runs — the protocol

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
that resolves at the anchor the project declares. On the default-branch anchor that means committed
before the run's branch existed. The owner's act is `/unattended <slug>`, or — where the project
admits the second anchor — an invocation carrying the authorizing parameter and the prose the build
is scoped by. They author nothing per run except the reason text of a directive waiver, which
`--preflight` records on their behalf (§10), and on the prompt path the prose itself plus whatever
the agent asks at its single opening turn. Four properties, all mechanical:

- **It is asserted, never written by the run — on the DEFAULT-BRANCH anchor.** `--preflight` refuses
    if it is absent, and at that anchor a run that could write its own authorization has none. **On
    the second anchor this property is weaker, deliberately**: the run may author its own build folder
    and push it, which is cost 1 below made USABLE rather than merely conceded. Which anchor
    authorized a run is recorded, and so is the discipline it claimed — neither is a verdict, and §9's
    reduction applies to both.
- **It is reachable from the pinned BASE.** A build folder introduced by a commit on the run's own
  branch grants nothing. Reachability is the machine-checkable form of "somebody with push rights put
  this here before this run branched" — and the run holds push rights by construction, so it is a
  cost, not a proof. The pin is taken from the ref name and tip the REMOTE advertises for its own
  HEAD, never from a local ref and never from the environment. What that removes, and what it leaves,
  is §9.
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
2. **The BAR weakens for adopters who never opt in.** The key gates the DRIVER and cannot gate the
   leg: the conf is a working-tree file the run can commit, so a leg reading it would be reading its
   subject's answer. The leg's BASE check therefore asks "published on the remote" in every repo.
3. **Roster integrity becomes satisfiable by construction** on the branch anchor, as qualified above.

None of the three is closed. What the design adds is VISIBILITY: the record names the anchor used.

**What this costs, stated because the previous design paid none of it.** The authorization was once a
block naming the build and both authorized actions, compared byte-for-byte across the BASE. Moving it
to the build folder trades these properties:

1. **Integrity becomes existence.** A README's generated region legitimately moves, so no whole-file
   equality is assertable.
2. **The grant is class-wide.** Every build folder in the tree satisfies the predicate; the narrowing
   is the slug the owner types, and chat is not machine-checkable.
3. **It names no ACTIONS** and **cannot be revoked**: a build authorizes both, permanently.
4. **It is self-propagating.** A run whose diff creates a new build README authorizes the NEXT run.
   Unrefused: §9 names the only thing that would.

All were put to the owner and accepted.

**The build method is a RUN-TIME dependency of this kit.** Every directive is a pointer into a
section of `<MEMORY_ROOT>/guides/BUILD-METHOD.md`, so `--preflight` refuses a tree where it is absent rather than starting a run bound
by a set that resolves to nothing.

Absent or unreachable authorization → the run does not start. There is no override for this one: an
override on the authorization check is the authorization check.

## 2. The run-state file

`<MEMORY_ROOT>/builds/<slug>/RUN.md`, split mechanically rather than by discipline.

**Generated** — and the marker pair is now EMPTY by contract. The unit list and per-unit status are
DERIVED from the build README on every read, never copied here, and the gate asserts the region holds
no copy.

This inverted an earlier design in which the region WAS a copy the gate byte-compared against its
source. That equality was unmaintainable in the ordinary case: folding a review bumps a spec rev,
which moves the build index, which makes the copy stale — and the region's only writer was
`--preflight`, which refuses once a run is live. The refusal told the reader to "re-run the driver",
naming a path no verb walks. A run that hit it could only hand-edit an artifact this document calls
generated. Deriving removes the class instead of adding a verb to service it, and the invariant is
the same one stated as emptiness: one fact, one home.

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

**Authored**, carrying exactly eleven facts and nothing else. The file is CREATED by `--preflight`
and staged; the owner authors none of it. Nothing in the tree derives any of them,
which is the test for belonging here:

1. **The phase**, from the vocabulary in §3, each claim carrying a witness.
2. **The keepalive id**, recorded by `--preflight` from the value the agent hands it (§5).
3. **Parked entries**, of four kinds, which `park()`'s own kind argument already discriminates: a
   parked DECISION — the question, the options seen, and the reason the run refused, because a bare
   "parked" is indistinguishable from "forgotten" — an ABORT reason, a recorded DoD OVERRIDE, and an
   owner directive WAIVER (§10). Each kind names the verb that writes it: `--park`, `--abort`,
   `--close --override` and `--preflight --waive` respectively. DECISION had no writer for as long as
   this contract has instructed a run to park one, so the instruction could not be obeyed — a rule
   with no route is a rule nobody follows, and it took a build hitting it to notice.
4. **The run's BASE sha**, pinned once at run start. It is a runtime observation with no
   re-derivable source: a build with N sub-specs has N per-unit bases, none of which is the run's.
5. **The anchor ref name**, as the remote advertised it for its own HEAD at pin time.
6. **The anchor tip sha**, from that same advertisement.
7. **The endpoint URL** it was observed from.
8. **The roster AT LANDING**, frozen by `--landed` and by nothing else. While a run is LIVE the unit
   list is derived from the build README, which cannot go stale between reads. But a FINISHED record
   must still answer which units the run covered, and that README is mutable: a later build adding a
   unit would otherwise change a landed run's answer retroactively. Freezing the ids at the moment of
   landing is what keeps a terminal record a record rather than a live query.

9. **The anchor KIND**, `default-branch` or `run-branch`, recorded by `--preflight`.
10. **The branch ref name**, as the remote advertised it — present only when the second anchor fired.
11. **The branch tip sha**, from that same advertisement, and present under the same condition.

Facts 10 and 11 are ABSENT on a default-branch run, legally: the "nothing else" clause bounds what
may appear, not what must. Fact 9 is always written.

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

**The size budget and the spill rule.** The file is in the index set, so it carries the tree's index
caps, and it is designed to GROW. The authored region is budgeted at 8 KB. When the budget is
reached the oldest parked entries spill into the build's own `build/` folder as a dated recording —
a name the recording grammar already admits — and the authored region keeps a one-line pointer.
**Waiver entries are not spillable.** Written at preflight they are permanently the OLDEST entries,
so the rule would evict them first — after which the leg check that grades them passes by finding
nothing.
Crossing the cap mid-flight makes the gates red, which blocks `--close`, which makes the override
the only exit: the spill exists so that never happens.

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
`LANDED` the ancestry of the witness IS the claim: the gate asserts that it lies on the history the
anchor blesses, which is what makes the landing an observation rather than an assertion. A tag or a
workflow id there is unjudgeable, and a terminal claim is exactly where an unjudgeable witness costs
the most — it is the last thing written and nothing later re-examines it.

**Terminal is reached by a verb that evaluates what the phase claims, and never by a phase move.**
`--phase` writes the positions between; `--landed` and `--abort` write the two ends. `LANDING` is
close-only for the same reason: it is the record that the Definition-of-Done set was evaluated, so a
phase move into it would be that claim without the evaluation, and `--landed` accepts a record only
at `LANDING`. A run that is already terminal cannot be moved at all.

**At most one run-state file in the tree may be in a non-terminal phase.** Otherwise "the run" is
not well-defined, and anything keying on it must either OR the phases together (a tree-wide false
deny) or pick one arbitrarily (nondeterminism, which is the worst property a gate can have).

## 4. The Definition of Done

Eight kit-owned core items. Each names its checker, because an override budget must not be spent on
something no machine could have checked:

| Item | Checked by | Asserts |
|---|---|---|
| `gates-green` | machine | the project's full merge bar ran on the tip being landed and passed |
| `records-current` | machine | every unit's status header and every generated region match a fresh render |
| `authorization-reachable` | machine | the build README is reachable from the pinned BASE, parses as build front matter, and names this build |
| `landed-via-lander` | machine, PRE-LANDING | the run-state record names no bypass flag. It is checked BEFORE the landing it is named for, so it is a record check, not an observation of the push — the honest limit, stated rather than implied by the label |
| `build-complete` | machine | the build's authored roster names no unit that is unspecced or unfinished. Five terms, all required; the generated region must be NON-empty, because "no unit row is non-terminal" is vacuously true over no rows at all |
| `closing-review-recorded` | machine | a TRACKED review record under this build carries a `diff-review` binding line AND names a commit between the pinned BASE and HEAD, decided by git ancestry rather than by a substring. The RANGE is what admits a fold-scoped round, whose base is a descendant of BASE; the KIND is what stops a spec audit standing in for a closing review. It measures that a review of what shipped exists and is bound to THIS run, never what the review concluded |
| `keepalive-reaped` | agent-attested | the scheduled keepalive was deleted — written by `--attest <slug> --item keepalive-reaped` |
| `parked-decisions-surfaced` | agent-attested | every parked entry reached the wrap-up — written by `--attest <slug> --item parked-decisions-surfaced`, which DERIVES the record key (`parked-surfaced:`) so no operator spells one |

A project MAY append items via `DOD_EXTRA`. It may NOT delete a core item; the gate pins the core set's
COUNT against the same shrink-only floor, for the reason §3 gives.

`--close` BLOCKS on any unmet item. The override is named (it cites the item), recorded (it writes a
**The two attested items have a VERB, and it is the only way to write one.** `--attest <slug> --item
<item> [--value <text>]` refuses a machine-checked item by reading the item's declared CHECKER, so a
project that declares its own agent-attested extra gets the verb and one that renames a machine item
still gets the refusal. Before it existed the keys had no writer at all, which made `--abort` — the
documented sole exit from a wedged run, and the verb that REQUIRES both — reachable only by
hand-editing the authored region of a file this kit calls generated. An attestation is still an
attestation: the verb removes the hand edit, not the trust assumption §9 states.

parked entry), and surfaced in the wrap-up. The two agent-attested items do **not** spend the
override budget: attestation is not a machine verdict, and pretending otherwise makes an override
look like a check that failed.

## 5. The keepalive — an AGENT obligation

The scheduling store is in-memory and session-scoped. The job is gone when the agent process exits,
and deleting it removes it from that same store. **No script can reach it.** So the obligation
splits by actor, and the split is not a convenience:

- The **agent** schedules the keepalive before the run leaves `PREFLIGHT`, and reaps it before the
  run reaches a terminal phase. It uses the tool calls its own project layer declares —
  `KEEPALIVE_CREATE` and `KEEPALIVE_DELETE` in `.unattended.conf`, because an adopter's harness
  exposes a different scheduler and a kit that hardcodes one repo's spelling is wrong everywhere
  else.
- The **driver** RECORDS the id the agent hands it, and later ASSERTS that a reap was recorded. It
  never schedules and never deletes, and it labels the item agent-attested wherever it reports.

A driver verb that claimed to schedule or reap would be claiming an effect it cannot produce.

## 6. Landing

The run lands through the project's declared lander (`LANDER` in `.unattended.conf`) and **never**
with a hook-bypass flag. A project whose pre-push hook refuses an un-marked default-branch push has
made the lander mandatory on purpose: it reconciles the remote BEFORE the gate, so the gate never
runs on an already-stale tree. An unattended run that meets that refusal with nobody to interpret it
either stalls or learns to bypass — and bypassing discards the entire bar the mandate leaned on.

`landed-via-lander` is the machine-checked DoD item for this, and the gate greps the close path for
a bypass flag in both directions: the lander must be present, the flag must be absent.

## 7. The verbs

- `--preflight` — asserts the authorization, pins the BASE, CREATES and stages the run-state file,
  accepts `--waive <handle> --reason <text>` and no other verb does (§10),
  records the keepalive id the agent hands it,
  refuses on a dirty tree, on the default branch, and on an unwired repo, and writes the run-state
  file. It OBSERVES the anchor from the remote rather than reading a local ref, and refuses when the
  remote does not answer or advertises no default branch of its own. Failing closed there costs
  nothing real: a run that cannot reach the remote cannot land on it either. It delegates wiring to the project's **check** mode, never the repairing one: a repairing
  mode rewrites tracked bytes and sets git config, and the run's first act must not be the mode
  whose past over-firing is the cautionary case this protocol cites.
- `--phase` — writes a phase and its witness. Without it the vocabulary is decorative: only
  `--preflight` and `--close` ever wrote one, so every member between them could enter the file only
  by an agent hand-editing an artifact this kit calls generated.
- `--plan` — prints each tracked spec's id, status and the build method's M2 classification, and
  names the next unit. It COMPUTES that vocabulary and does not define it; M2 does. It joins the build README's roster region
  against the tracked specs, so a planned unit nobody has specced is reported as MISSING, and a
  roster whose markers are malformed is a named refusal rather than a complete-looking list.
- `--status` — prints one line naming the current phase and the first non-terminal unit.
- `--resume` — re-enters the run from the run-state file and must agree with `--status`.
- `--close` — evaluates the DoD set, blocks on any unmet item, and records any override. It is the
  only writer of `LANDING`, and it runs BEFORE the landing it authorises, so it cannot observe one.
- `--landed` — the sole producer of `LANDED`, and an OBSERVATION rather than a claim. It accepts a
  record only at `LANDING`, re-observes the anchor, and refuses unless HEAD is an ancestor of the tip
  the remote advertises. It does not refuse the default branch, because the mandated lander refuses
  every other one, so landing happens exactly where that guard would otherwise fire.
- `--abort` — the sole producer of `ABORTED`. It requires a recorded reason and both agent-attested
  items, and no machine item: an aborted run landed nothing, so the machine items assert obligations
  it does not have, while the keepalive is still orphaned and the parked decisions still unseen.

## 8. What a project declares

In the repo-root `.unattended.conf`. Blank or absent turns the corresponding assertion off only
where this document says it may:

| Key | Meaning |
|---|---|
| `MEMORY_ROOT` | the memory tree's root, matching the memory-tree kit's conf |
| `LANDER` | the mandated landing command |
| `BYPASS_BAN` | the flag the close path must never emit |
| `GATE_CMD` | the full merge bar, for `gates-green` |
| `WIRING_CHECK` | the non-repairing wiring check `--preflight` delegates to |
| `KEEPALIVE_CREATE` · `KEEPALIVE_DELETE` | the agent-facing scheduler tool calls, named for the agent to use |
| `KEEPALIVE_INTERVAL` | the cadence the agent schedules the keepalive at, rendered into the Skill as prose |
| `ANCHOR_SCOPE` | which anchors may authorize a run: the CLOSED set `default-branch` and `published`. Absent, blank or outside the set keeps `default-branch`, so a typo grants nothing. Gates the DRIVER only — §1 cost 2 |
| `CORE_FLOOR` | `<phases>:<dod>`, the shrink-only SIZE of the kit's core sets. MANDATORY: undeclared or malformed leaves both pins unenforced, so both are refusals |
| `DIRECTIVES_EXTRA` | project directive members, appended to the core set |
| `DIRECTIVES_FLOOR` | the shrink-only SIZE of the kit's core directive set. MANDATORY, for the reason `CORE_FLOOR` is |
| `PHASES_EXTRA` | project phase members, appended to the core set |
| `DOD_EXTRA` | project DoD items, appended to the core set |
| `KICKOFF_ENGINE` | the kickoff engine whose hand-back the gate reads; BLANK turns that check off |
| `KICKOFF_EXITS` | a shrink-only floor on how many interactive exits that engine resolves without an owner turn |

An empty declaration is a refusal, not a pass: a vocabulary with no members and a DoD set with no
items would both make every check keyed on them vacuously true.

## 9. The boundary this kit claims

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
