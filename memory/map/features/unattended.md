# unattended — the run that merges and pushes with no owner turn

```toml
feature = "unattended"
title = "Unattended runs — a mandate on disk, not a block of chat"
status = "shipped"
streams = ["tooling", "playbook", "kickoff", "deployer"]
decisions = []

[claims]
gate-legs = ["unattended kit gate", "unattended skill wiring", "pass-order history", "brief-recorded"]
kits = ["unattended"]
git-hooks = []
workflow-scripts = ["unattended-build.js", "unattended-unit.js"]
skill-engines = ["session-kickoff"]
rendered-skills = ["unattended"]
gotcha-classes = ["reflowed-prompt-string-reads-as-a-deleted-stop.md", "text-mode-read-eats-a-bare-cr.md",
  "assertion-between-two-derived-values.md", "second-implementation-is-not-a-second-opinion.md",
  "inputs-inside-the-subjects-reach.md", "fixture-inherits-ambient-machine-state.md",
  "bounded-through-a-pipe-is-unbounded.md",
  "status-set-in-a-subshell.md", "id-matched-as-a-substring.md", "containment-tested-one-way.md",
  "structured-record-split-on-whitespace.md", "staged-break-substitutes-a-synthetic-value.md",
  "spec-names-code-its-base-lacks.md", "two-guards-one-question-two-answers.md",
  "process-creation-is-the-suite-cost.md", "trace-profile-measures-itself.md",
  "fallback-fabricates-the-passing-value.md", "two-readers-of-one-config-one-re-derived.md",
]
guides = ["UNATTENDED-PROTOCOL.md", "UNATTENDED-VERBS.md", "UNATTENDED-STOPS.md"]
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/unattended/*",
  "memory/guides/UNATTENDED-*.md",
  ".unattended.conf",
]
```

## Constraints & why

**The checkpoint is replaced, not removed.** Every other kit makes a rule enforceable. This one
removes a rule — the explicit ask before a merge and a push — and its burden is to put
something machine-checkable in the vacated slot. That is why the mandate is ASSERTED rather than
written by the run, and why reachability from the pinned BASE is part of the contract: a run that can
author its own authorization has none, and every gate downstream would certify it.

**THE HARNESS BUYS STAGE ORDER AND CANNOT BUY ENFORCEMENT.** `tools/workflows/unattended-build.js`
runs SPEC then AUDIT then DISPOSAL and hands the run an ordered ROSTER it dispatches one `Workflow`
call per unit, so the hand-out is unreachable except through all three and on a TERMINAL `--review`
verdict — control flow, not a rule an agent remembers. It verifies nothing: a Workflow script
has no filesystem, so every observation is a claim its own agent returned; the refusals live below. TWO SHAPES ARE FORCED BY `agent-cap.js`, which denied an
`agent()` in any loop body until `TOOL-dFoldedVerdict-4` admitted a MARKED bounded one: DISPOSAL is
ONE agent over the whole set, and the convergence LOOP sits in the caller while the harness holds
the GATE, its iteration count being data-dependent and so unboundable.

**PASS ORDER IS ENFORCED TWICE: ONE PLACE IS BYPASSABLE.** The method's hard floor
— never build a MISSING or THIN unit — was carried entirely by an agent's memory. `plan_state`, the
M2 classifier, ran at two sites that cannot catch it: `--plan` only reports, and `build-complete`
runs after every commit has landed, by which point a run that built first and specced afterwards has
a spec that is neither missing nor thin. `--dispatch` now REFUSES such a pass at the moment of the
act and is bypassed by not calling the verb; the `pass-order history` leg reads the COMMIT GRAPH,
asserting each CLOSED unit's build commit had a conforming, non-THIN spec at its FIRST PARENT. Only
the graph remembers ORDER, which is why the second exists. The first parent and not the pinned BASE:
the method REQUIRES a run to author a missing spec, so what this refuses is authoring it AFTERWARDS.
`PASS_ORDER_CUTOFF` grandfathers earlier builds, and the leg's liveness line names all three
populations it walks rather than only the two it grades. `--dispatch` also runs the spec-token
checker declared as `SPEC_TOKENS_CLI` over the live tree first: this harness closes each unit spec
in its build commit, so no bar ever grades one (aDeferredBar F3).

**THE DEFINITION OF DONE ASKS ONE QUESTION ABOUT THE WORK AND TWELVE ABOUT THE ARTEFACTS.**
`asks-disposed` grades whether the QUESTIONS a run was pointed at ended somewhere the owner
can accept; every other item grades what it PRODUCED. It folds nothing — status is the
declared `ASKS_CMD` witness's, and what it reads off the tree is filing, a status ROW and a
spec header VERB. Its scope is read BEFORE the witness runs, and its answer freezes into
`asks-at-landing` because ruling D4 makes CLOSED non-absorbing.

**The anchor is an OBSERVATION of the remote, and the kit no longer claims more than that.** Kit 1.0
pinned BASE against `refs/remotes/origin/<default>` and justified it in a source comment claiming the
ref could not move without a push. False — `git update-ref` moves it offline — and it was
reproduced end to end: preflight printed OK over a base the run had authored, the leg agreed silently,
and the push landed. The ref name and tip now come from what the remote advertises for its own HEAD,
and `GOV_DEFAULT_BRANCH` is a cross-check that can only refuse. Both routes are inert, not detected:
neither value is read at all.

**A sha is a NAME, and the dereference is pinned separately.** `git replace` substitutes the object a
sha resolves to and a graft file rewrites the commit graph, both at a perfectly honest anchor, so
neither is closed by any amount of anchor hardening. Every read that turns a sha into bytes or into
ancestry goes through a wrapper pinning `core.useReplaceRefs=false` with `GIT_GRAFT_FILE` pointed
away from the repo. The two suppressions are not interchangeable and only the second stops a graft;
measured, not assumed.

**The boundary is stated rather than implied.** A design panel broke four independent anchor
mechanisms and converged on the reduction that a check under the run's own uid cannot
constitute authorization. The protocol's §9 enumerates what remains reachable — editing the kit,
shimming its tools, skipping the hook layer, relaying through a seeded endpoint, or never creating a
run-state file at all — and names the only control that binds: re-running the same leg in a clone the
run never touched.

**Nothing in a script can reach the scheduler.** The keepalive store is in-memory and session-scoped,
so a driver verb claiming to schedule or reap it claims an effect it cannot produce. The obligation
splits by actor — the agent schedules and reaps, the driver records an id and asserts a recorded
reap — and the reaped item is labelled agent-attested wherever it is reported, so it never spends
the `--close` override budget. The tick runs `--resume --keepalive-id`, which refreshes the
lease, then `--audit`, the unit stall probe.

**A stop the run cannot fix is a PAUSE, not an ending.** `HELD` is non-terminal: entered by
`--hold` with a code, a condition and a witness, left by `--resume` alone. A per-slug LEASE
under the git common dir keys on the session-scoped keepalive id, so a resume tells orientation
from take-over. Every `phase` read routes through `read_derived_phase` or `read_recorded_phase`.
See `UNATTENDED-STOPS.md`.

**Declarations, not constants.** The phase vocabulary, the Definition-of-Done set, the lander, the
bypass flag and the scheduler tool names all live in the repo-root `.unattended.conf`. The driver and
the leg READ them; a phase token or a DoD item spelled into a script is a defect. `AUTH_PARAM` lives
in the same file and is read by NEITHER: it is consumed once, by `adopt-unattended.sh`, at render
time, and its value reaches an agent only through the rendered Skill. The kit owns the
CORE of both sets and the project may only EXTEND them, asserted against a shrink-only floor —
without that floor, deleting an item is a silent, reason-free override of everything keyed on it,
and the fleet has a recorded case of a pin RAISE indistinguishable from a drain.

**The run-state file is split mechanically, not by discipline.** The generated region is EMPTY by
contract and the gate asserts it holds no copy: the unit list is DERIVED from the build README on
every read, so "current" is the absence of a second answer rather than a comparison between two. The authored region holds only the facts nothing in the tree derives, enumerated in the
protocol's own section 2 and deliberately not counted here — three carriers once held three different
counts of them at the same time.

**The template is byte-gated and this feature is kit-conditional.** The unattended rules first landed
in the domain-rules companion (§1) to stay inside the byte ceiling; v3.0 converged that companion into
the charter, so they now live in the charter's `kit:unattended` conditional block in §1 — dropped by
the renderer for a target that did not select the kit. Two amended clauses sit in the unconditional
body, both written to stay true for a non-adopting re-puller. The Skill's `## Resume` section invokes `/session-kickoff`
after the reap and the re-schedule (`TOOL-aReplayedCard-3`), so a session resumed after process
death re-orients and its first commit is not denied on an un-oriented card; `check-unattended.sh`
check 18 keeps the template's FIRST kickoff mention below its first `--preflight`, and the resume
mention sits far under both.

**A run is bound by a set of named directives, and each is a POINTER.** The count lives in the
driver's `DIRECTIVES_CORE` and in nothing else here, because this sentence has already been wrong
about it once. The set is a kit constant the
project may extend but not delete; the rules live in the build method and the contract names zero
handles, because naming them twice is the drift the design exists to avoid. A waiver is the owner's,
taken at preflight and nowhere else — enforced by one branch rather than promised, so a later verb
cannot take an answer and a re-preflight re-issues the recorded set. A waiver relaxes the directive,
never a DoD item and never a gate.

**Every remote observation is BOUNDED, and the bound is a file constant.** The kit makes remote
round-trips on the authorization path — the default-branch HEAD advertisement, the per-branch tip
under the published anchor, and the leg's own two — and until 2026-08-20 not one of them had a
deadline. A partitioned endpoint therefore turned `--close` into an indefinite silent wait, and the
same calls inside the leg turned a `git push` into a HUNG push rather than a red one, because the leg
runs under `.githooks/pre-push`. The tracked incident is a driver selftest that produced zero output
at 240 s and wedged the whole bar.

Three bounds, because no single mechanism covers every transport: an outer wall clock for blackholed
packets, `http.lowSpeed{Limit,Time}` for a server that ACCEPTS and then stalls — which no wall clock
can distinguish from a slow success — and `ssh -o ConnectTimeout` for the handshake. The credential
path is closed separately: `GIT_TERMINAL_PROMPT=0` bounds git's OWN prompt and never reaches a
configured helper, so `credential.interactive=never` is passed too, with `-c` so it is scoped to the
observation and cannot disable credentials for the landing push.

**The load-bearing detail is the CAPTURE, not the deadline.** `out=$(timeout N cmd)` does not bound
the clock: the substitution reads until EOF, EOF arrives only when the last inherited write end
closes, and a surviving descendant holds the pipe while `timeout` reports 124 on schedule. Measured
on node `c` inside the suite that grades it — 8 s through a substitution against a declared 1 s
bound, 0 s through a file. So the helper redirects to a file and reads it after `timeout` returns,
with `-k` for the child that ignores SIGTERM. The gate runner carries the identical fix for the
identical reason, discovered independently days apart, which is why the arm that proves it MEASURES
elapsed time rather than asserting a message.

Two consequences worth knowing before extending this. The helper cannot call the driver's own `GIT()`
wrapper — `timeout` needs an external command and `GIT()` is a shell function — so the dereference
pins live in named constants that both expand, and the arm checks the constants' VALUES as well as
their expansion, because an indirection is otherwise a way to weaken a pin while a one-line grep
stays green. And a transport failure is no longer reported as a semantic answer: the per-branch query
used to collapse git's 128 into "the remote advertises no tip", so a network fault told the operator
to push a branch that was already pushed.

**What the bound does NOT buy, stated so a green suite is not misread.** No arm drives a blackholed
endpoint for the full declared bound — that would add the bound to the wall clock of the slowest leg
on the bar, in a suite whose historical failure mode is a leg that takes too long — so the deadline is
graded by the mechanism arm plus an elapsed assertion on the terminal-record path, and the refusal
path is driven by a stub exiting the status `timeout` itself returns. The `http.lowSpeed*` and
`ConnectTimeout` options are asserted BY INSPECTION only: exercising them needs a server that
authenticates, stalls mid-transfer, and speaks ssh, and no fixture here has one.

**The kit reads the evidence it already records, from `TOOL-aGradedMandate`.** Four Definition-of-Done
terms were added or tightened, and every one of them consumes a fact the driver was already writing
and nothing was reading. `closing-review-recorded` gained a second term: the LAST `--review` round
whose subject is the build slug must carry a terminal token, and `CONVERGED` must name zero blockers.
Two runs in this tree had reached `LANDED` with that item MET while their closing loop stopped at
BLOCKED with blockers standing, and the incentive was inverted — recording one more round could oblige
a run to promote every blocker into a built unit, while recording nothing owed nothing. `specs-audited`
is an eleventh core item joining every CLOSED unit to a tracked `spec-audit` binding line, whole-token
and expanding the `N..M` range form eighteen tracked records use. `build-complete` gained a sixth term
over `plan_state`'s THIN grade, which `verb_plan` used to compute and overwrite one line later.

**The parked split has TWO axes and the history side subtracts both.** `PARK_ACTS_OWED` names the acts
of the `rescope` kind the owner is owed, so a retirement reaches the wrap-up while an addition stays a
declaration. A `kind:act` member grammar inside `PARK_KINDS_OWED` was tried and REFUSED: the gate leg
greps the driver for a `park` call site per owed member, and no `park "$rel" rescope:retire` site can
exist, because the act is a field of the reason. The history complement subtracts the owed acts too —
without that a retire row matches both alternations and `--status` reports one row as a decision AND
as a note.

**The leg second-opinions the ask mandate from inputs the run cannot move.** `asks:` against the
README at BASE, P5 from the home BACKLOG blob at `m-base:`, and `m-base:` as the merge-base of the
pinned `anchor-sha:` and HEAD at preflight, never `base:`. Check 37 bans a foreign anchor in the
run's folder by the recall kit's own `anchor_at`, reached through `RECALL_CLI`. `asks-ready:` and
the freeze are re-derived by re-running `ASKS_CMD` until the record is published.

## Shared seams

- `memory/guides/REVIEW-PROTOCOL.md` — the structural precedent for a BINDING guide: charter-cited,
  in the hygiene index set, entry-budget exempt, enforced by a leg rather than by its own prose.
- `tools/push-main.sh` + `.githooks/pre-push` — the mandated lander and the marker that makes it
  mandatory. The kit names it through `LANDER`, never by hardcoded path.
- `tools/check-wiring.sh --check` — the non-repairing wiring probe preflight delegates to. The
  repairing mode is deliberately out of reach.
- `tools/memory-tree/check-memory-hygiene.sh` — supplies the run-state file's legality (check 4's
  whitelist), its size cap (check 6 via `index_set`), its prose exemption (check 7's `ex7`) and,
  by deliberate omission, leaves phase-vocabulary validation to this kit's own leg.
- `tools/memory-tree/gen_build_index.py` `apply_region()` — the generated-region splice contract,
  reused verbatim rather than re-implemented.
- `tools/drift-audit/drift_report.py` — the judgeability discipline, reused for witness RESOLUTION
  and deliberately NOT for witness PRESENCE, which is its own refusal here.
- `tools/settings-merge.py --fragment` + `tools/check-hook-destinations.sh` — wire `gate-guard.js`,
  this kit's `PreToolUse` hook denying the flagged bar and every suite before `VERIFYING`, keyed to
  the branch by `run-branch:`. Its `buildCommandView` is COPIED from `tools/hooks/scratch-guard.js`:
  a `require` of a sibling kit is a literal the install-prefix ban refuses (`TOOL-aDeferredBar-3`).

## Reuse affordance

seam: `.unattended.conf` — the project declaration surface. Anything that needs to know this repo's
lander, merge bar, wiring check, bypass ban, scheduler tool names or authorizing token reads it from
here rather than
re-deriving or hardcoding. `AUTH_PARAM` is the second key whose BLANK declaration means the kit
default rather than "off" (`ANCHOR_SCOPE` is the first): the literal lives once, in
`adopt-unattended.sh`, and the rendered Skill is where a reader learns it. `PHASES_EXTRA` and `DOD_EXTRA` are the sanctioned extension points; the
core sets are not editable from the project layer.

## Gaps

*Re-derived 2026-08-20 against the tree, not carried forward. Dossier prose is ungated and rots
silently; re-derive this section whenever the feature is touched.*

- **The junction arm of the adopter e2e is SKIPPED on node `a`**, which lacks the privilege to
  create a symlink. It reports the skip loudly rather than passing, but the shape this fleet
  actually installs with is therefore unexercised here and needs a run on a node that can link.
- **A bug class this build DISCOVERED is now catalogued but only gated in one place.**
  `assertion-between-two-derived-values` was found here, in this kit's own leg, and the arm that
  proves it is this kit's. The class is general — any checker that composes both sides of a
  comparison has it — and nothing sweeps for it repo-wide.
- **The ask-mandate second opinions (`TOOL-dDerivedDocket-18`) have two named holes.** A producer
  that cannot run, breaches the bound or answers in a refused shape is UNANSWERED, so a forged
  `asks-ready:` or freeze behind a broken `ASKS_CMD` passes; and a record already on the advertised
  default tip is never re-derived. Both are in the leg's header. Re-derived 2026-09-21: the two
  check-9 rows this replaced are closed — the leg reads no local ref on the BASE path any more, and
  an unobserved remote fails check 9 closed by name.

- **The DIRECTIVE LAYER is gated on both halves.** The registry is joined to the Skill's table in
  both directions by check 16, every cited method section resolves, and the protocol's own §3 phase
  list, §4 DoD table and the count sentence above it are joined to the driver's constants by arms D
  and E. Check 17 grades the parked waiver record: a declared handle, a non-empty reason, and the
  whole line present in the run-state file's FIRST committed blob. Its green control's waiver is
  written by `--preflight --waive` rather than by hand, which is the cross-component arm
  `TOOL-aStandingWrit-8` asked for. Two exemptions are deliberate and each carries its reason in
  source: the handle-membership test is skipped on a TERMINAL record, because a frozen waiver graded
  against a moving directive set is a red wedge no verb can repair, and the git join is silent when
  the record has no committed blob.
- **Nothing binds the executing kit to kit code an owner approved.** A run may edit these scripts and
  commit them; the parity legs compare two files the same run can change together. This bounds every
  property above and is the reason the protocol names an off-machine verifier as the real control.
- **The keepalive half is unenforceable by construction.** Two DoD items are agent-attested because
  no script can reach the scheduling store. They are labelled everywhere they appear, and they are
  still the softest part of the contract.
