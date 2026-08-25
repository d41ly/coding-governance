# unattended — the run that merges and pushes with no owner turn

```toml
feature = "unattended"
title = "Unattended runs — a mandate on disk, not a block of chat"
status = "shipped"
streams = ["tooling", "playbook", "kickoff", "deployer"]
decisions = []

[claims]
gate-legs = ["unattended kit gate", "unattended skill wiring"]
kits = ["unattended"]
git-hooks = []
workflow-scripts = []
skill-engines = ["session-kickoff"]
rendered-skills = ["unattended"]
gotcha-classes = ["text-mode-read-eats-a-bare-cr.md",
  "assertion-between-two-derived-values.md", "second-implementation-is-not-a-second-opinion.md",
  "inputs-inside-the-subjects-reach.md", "fixture-inherits-ambient-machine-state.md",
  "bounded-through-a-pipe-is-unbounded.md",
  "status-set-in-a-subshell.md", "id-matched-as-a-substring.md", "containment-tested-one-way.md",
  "structured-record-split-on-whitespace.md", "staged-break-substitutes-a-synthetic-value.md",
  "spec-names-code-its-base-lacks.md", "two-guards-one-question-two-answers.md",
  "process-creation-is-the-suite-cost.md", "trace-profile-measures-itself.md",
  "fallback-fabricates-the-passing-value.md", "two-readers-of-one-config-one-re-derived.md",
]
guides = ["UNATTENDED-PROTOCOL.md"]
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/unattended/*",
  "memory/guides/UNATTENDED-PROTOCOL.md",
  ".unattended.conf",
]
```

## Constraints & why

**The checkpoint is replaced, not removed.** Every other kit here makes a rule enforceable. This one
removes a rule — the explicit ask before a merge and a push — and its whole burden is to put
something machine-checkable in the vacated slot. That is why the mandate is ASSERTED rather than
written by the run, and why reachability from the pinned BASE is part of the contract: a run that can
author its own authorization has none, and every gate downstream would certify it.

**The anchor is an OBSERVATION of the remote, and the kit no longer claims more than that.** Kit 1.0
pinned BASE against `refs/remotes/origin/<default>` and justified it in a source comment claiming the
ref could not move without a push. That was false — `git update-ref` moves it offline — and it was
reproduced end to end: preflight printed OK over a base the run had authored, the leg agreed silently,
and the push landed. The ref name and tip now come from what the remote advertises for its own HEAD,
and `GOV_DEFAULT_BRANCH` is a cross-check that can only refuse. Both routes are inert rather than
detected: neither value is read at all.

**A sha is a NAME, and the dereference is pinned separately.** `git replace` substitutes the object a
sha resolves to and a graft file rewrites the commit graph, both at a perfectly honest anchor, so
neither is closed by any amount of anchor hardening. Every read that turns a sha into bytes or into
ancestry goes through a wrapper pinning `core.useReplaceRefs=false` with `GIT_GRAFT_FILE` pointed
away from the repo. The two suppressions are not interchangeable and only the second stops a graft —
measured, not assumed.

**The boundary is stated rather than implied.** A design panel broke four independent anchor
mechanisms and converged on the reduction that a check running under the run's own uid cannot
constitute authorization. The protocol's §9 enumerates what remains reachable — editing the kit,
shimming its tools, skipping the hook layer, relaying through a seeded endpoint, or never creating a
run-state file at all — and names the only control that binds: re-running the same leg in a clone the
run never touched.

**Nothing in a script can reach the scheduler.** The keepalive store is in-memory and session-scoped,
so a driver verb claiming to schedule or reap it claims an effect it cannot produce. The obligation
therefore splits by actor — the agent schedules and reaps, the driver records an id and asserts a
recorded reap — and the reaped item is labelled agent-attested wherever it is reported, so it never
spends the `--close` override budget.

**Declarations, not constants.** The phase vocabulary, the Definition-of-Done set, the lander, the
bypass flag, the scheduler tool names and the token that authorizes a prompt-mode run all live in the
repo-root `.unattended.conf`. The driver and
the leg READ them; a phase token or a DoD item spelled into a script is a defect. The kit owns the
CORE of both sets and the project may only EXTEND them, asserted against a shrink-only floor —
without that floor, deleting an item is a silent, reason-free override of everything keyed on it,
and the fleet already has a recorded case of a pin RAISE being indistinguishable from a drain.

**The run-state file is split mechanically, not by discipline.** The generated region is
byte-compared against a fresh render; the authored region holds only the facts nothing in the
tree derives — seven of them, enumerated in the protocol's own section 2 rather than counted here. The precedent is in this repo: one build's hand-kept status file still reads
IN-PROGRESS while the generated region of the same build's README correctly reads CLOSED. The
authored half rotted and the derived half did not.

**The template is byte-gated and this feature is kit-conditional.** The unattended rules first landed
in the domain-rules companion (§1) to stay inside the byte ceiling; v3.0 converged that companion into
the charter, so they now live in the charter's `kit:unattended` conditional block in §1 — dropped by
the renderer for a target that did not select the kit. Two amended clauses sit in the unconditional
body, both written to stay true for a non-adopting re-puller. A new universal-core section for an
opt-in kit was rejected on both counts.

**A run is bound by eleven named directives, and each is a POINTER.** The set is a kit constant the
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

## Reuse affordance

seam: `.unattended.conf` — the project declaration surface. Anything that needs to know this repo's
lander, merge bar, wiring check, bypass ban, scheduler tool names or authorizing token reads it from
here rather than
re-deriving or hardcoding. `AUTH_PARAM` is the second key whose BLANK declaration means the kit
default rather than "off" (`ANCHOR_SCOPE` is the first): the literal lives once, in
`adopt-unattended.sh`, and the rendered Skill is where a reader learns it. `PHASES_EXTRA` and `DOD_EXTRA` are the sanctioned extension points; the
core sets are not editable from the project layer.

## Gaps

*Re-derived 2026-08-20 against the tree rather than carried forward. The authored region
carries twelve facts — it said seven here, and eleven in the protocol pair, and five in the driver's own
resume comment, all at the same time. Three carriers, three values, none of them counted by any gate:
that is what an ungated count does, and it is why the unit that added the twelfth fact enumerated the
carriers by path rather than trusting a builder to find them. Dossier prose is ungated — only the
claims tables above are — so this section rots silently and is worth re-deriving whenever the feature
is touched.*

- **A run has been driven end to end, and it exposed two defects rather than confirming the
  design.** `aSealedCaravan` preflighted, built, and landed at `7a4f904` with the full bar green.
  It then could not be CLOSED, and its record sat non-terminal for three days. Both causes are
  fixed in `cFinalBerth`: no verb produced a terminal phase at all, and `--close` refused every run
  whose HEAD was already published. What a live run proved was that the pieces refusing correctly
  in fixtures did not add up to a lifecycle.
- **The junction arm of the adopter e2e is SKIPPED on node `a`**, which lacks the privilege to
  create a symlink. It reports the skip loudly rather than passing, but the shape this fleet
  actually installs with is therefore unexercised here and needs a run on a node that can link.
- **No adopter has installed this kit.** The path exists and is gated; nothing has travelled it.
- **A bug class this build DISCOVERED is now catalogued but only gated in one place.**
  `assertion-between-two-derived-values` was found here, in this kit's own leg, and the arm that
  proves it is this kit's. The class is general — any checker that composes both sides of a
  comparison has it — and nothing sweeps for it repo-wide.
- **The gate leg still recomputes BASE against a live local ref.** The driver's anchor is observed;
  the leg's is not. It reads `GOV_DEFAULT_BRANCH` and `refs/remotes/origin/<d>`, so handed a tree
  with a forged tracking ref it recomputes the same wrong value and agrees. The driver refuses such a
  run before a run-state file exists, so the reachable damage is bounded, but the leg's own
  independence is not what it claims. Open as `TOOL-aStandingWrit-6`.

- **Check 9's three silent exits were specced and never landed.** The `aMooredAnchor` spec's S4
  scoped a named refusal for each — the default branch is unresolvable, no candidate ref resolves,
  and a candidate resolves but the merge-base fails — and its rev-4 rebase note lists four items
  carried forward with S4 absent from them. The spec closed anyway. So on a clone with no
  `origin/HEAD` and no environment override, the whole `if [ -n "$d" ]` block is skipped in silence,
  and check 15's ancestry half inherits that. This is an ABSENT ref, distinct from the forged one
  above, and it was owned by nobody until this dossier row.

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
- **Both Definition-of-Done items shipped.** `build-complete` is a five-term conjunction over the
  authored roster and the run-state file's copied region; `closing-review-recorded` joins the pinned
  BASE to a tracked review record. `CORE_FLOOR` is `10:8`. The base needle is SEVEN characters, not
  eight: git abbreviates to seven here, 29 of 48 tracked records spell it that way, and the
  eight-char form shipped briefly and matched none of them — an item clearable only by an override
  the run wrote for itself.
- **Nothing binds the executing kit to kit code an owner approved.** A run may edit these scripts and
  commit them; the parity legs compare two files the same run can change together. This bounds every
  property above and is the reason the protocol names an off-machine verifier as the real control.
- **The keepalive half is unenforceable by construction.** Two DoD items are agent-attested because
  no script can reach the scheduling store. They are labelled everywhere they appear, and they are
  still the softest part of the contract.
