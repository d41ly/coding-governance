# TOOL-aStandingWrit-1 — the run authorizes on a plan it did not write

**Status:** INPROGRESS · rev-6 · 2026-08-11 · node a · Tier-2 · base af6de231 · streams tooling+playbook+kickoff · ratified 2026-08-11

## 1. Goal

Make `/unattended <slug>` the owner's only act by moving the unattended run's authorization off an
owner-authored block inside the file the run writes, and onto the build folder the owner already
creates. The run must still author none of its own inputs, and the driver must be able to say which
step of the build remains without re-reading prose.

The rev-1 draft assumed the anchor that decides "outside the run's reach" was already trustworthy.
The review disproved that against landed code, so this rev's first goal is to make the assumption
true before anything is built on it.

## 2. Scope (IN)

**S0 — the anchor and the dereference. BUILT.** The pinned BASE anchored on
`refs/remotes/origin/<default>` behind a source comment claiming the ref could not move without a
push. It moves offline. S0 replaces the anchor with what the remote advertises for its own HEAD,
demotes `GOV_DEFAULT_BRANCH` to a cross-check that can only refuse, pins every dereference through a
wrapper that disables replace refs and points the graft file away from the repo, records the
observation as evidence, and retracts the false claim in the source, the protocol and the charter.

Verified end to end with live controls on both sides: an honest build is ACCEPTED before and after,
while a forged tracking ref, a `GOV_DEFAULT_BRANCH` naming a branch the run itself pushed to the
remote, and a `git replace` at an honest anchor are each REFUSED. Route 1 is inert rather than
detected — the forged ref is never read. Nine new refusal branches, all armed; the floor moved 31 to
39, re-pinned from the measured report rather than by hand.

What S0 does NOT do, and what rev-1 assumed it would: it does not make the anchor unforgeable. See
the rule above and the protocol's §9.

**S1 — the authorization surface moves to the build README at BASE.** `check_mandate()` is replaced
by `check_authorization()`, which asserts that the build README resolves at the pinned BASE, parses
as build front matter, carries a `slug:` equal to the requested slug, and — when a plan region is
present at BASE — that the region is byte-equal in the working copy. `MAN_OPEN`, `MAN_CLOSE` and
every refusal keyed on them retire.

**S2 — `RUN.md` loses its authored mandate and gains a creating verb.** `--preflight` creates the
run-state file when absent, replacing `fail 15`, and COMMITS it before returning. The authored region
carries four facts. The file keeps an authored region; rev-1's "wholly generated" was wrong.

**S3 — the merge-base-equals-HEAD refusal is scoped by verb, after S0.** It becomes legal at
`--preflight` and stays a refusal at `--close` and in the gate leg. The BASE value for that state is
defined explicitly rather than left to an empty string.

**S4 — `--plan`, MECHANISING the build method's classification rather than inventing one.** A fifth
verb prints per-unit state and names the next step. It reads spec status headers and the review
pointer declared in them; it performs no filename join and no title match, both of which the review
measured wrong on every multi-unit build in this corpus.

The four states are `memory/guides/BUILD-METHOD.md` M2's, spelled exactly — MISSING, THIN, FORKED,
READY — and the RULE for each stays in M2. That document's own governing constraint is that a rule
appearing both in it and in a carrier it points at is a defect IN IT, so this verb may compute the
classification and must not restate it. The eight-state table rev-2 designed is withdrawn: it was
authored before M2 existed and is a second vocabulary for one question.

**S5 — WITHDRAWN, superseded on main.** It proposed a marker-delimited plan region and a
`memory/TEMPLATE-README.md` to document it. `memory/guides/BUILD-METHOD.md` M2 landed first and
answers the same question with no new artifact: the roster is the build README's authored Units table
where one exists, else the conforming specs under the build's `spec/`. It also resolves this scope
item's stated motivation outright — the `ids:` key is a reservation RANGE and not a roster, which is
exactly the ambiguity the backlog row recorded inline as TOOL-aUnmannedHelm-3 cited as its evidence.

Building S5 would add a second roster surface and a template whose content M2 already carries, and
M2's own rule makes the duplicate a defect. The engine change it required — admitting a new file to
hygiene check 3's closed memory-root allowlist, with its four-gate repair set — is avoided entirely.
The withdrawal also retires F5's plan-region requirement, which was the mitigation for
self-propagating authorization; §8 records what replaces it.

**S6 — the phase vocabulary gains members and a producer, named for PASSES.** The members are
`memory/guides/BUILD-METHOD.md` M6's pass kinds rather than three tokens this spec invented:
`SPECCING`, `REVIEWING`, `FOLDING`, `BUILDING`. M6 defines a pass as exactly one of a spec authored,
a spec reviewed, a review's fixes folded in, a unit built, or the closing diff review — and the last
is already `VERIFYING`. Phases are the unattended protocol's to own (M11 says so), so naming them
after M6's passes aligns the two without either restating the other.

`RUNNING` is retained with an explicit meaning — a run between named passes — because the core set is
shrink-only and deleting it would lower the floor. A `--phase` verb writes a phase with its witness,
and `--preflight` stops unconditionally rewriting one, which today clobbers a resumed run's position.

**S7 — the amendment set**, enumerated by file and by sentence in §4.

**S8 — the roster marker pair, and the integrity check it makes possible.** P1 resolved as option
(b): the build README's Units table — which `memory/guides/BUILD-METHOD.md` M2 already makes the
roster — gets a marker pair, and `check_authorization` compares that region across the pinned BASE.
It introduces no second roster; it makes M2's roster machine-locatable. Locating it structurally
instead was the cheaper option and was refused, because a renamed heading silently empties the
comparison and this repo has a named bug class for a check that passes by finding nothing.

It is OPT-IN by presence, which is F1's ratified shape and what keeps the 26 builds that predate it
authorized. Presence is decided by grepping for the open marker and NOT by the extractor's exit
status, which conflates absent with duplicated — the discarded-signal defect this kit has paid for
once already.

## 3. Non-goals (OUT)

The instruction layer: the prose that tells an agent HOW to write a sub-spec, HOW to conduct the
adversarial review, and what evidence makes a unit built. A parallel session owns it. The review
could not locate that session anywhere in this tree — no branch, worktree, build folder or backlog
row names it — so F7 resolved by narrowing the cut-line instead of asserting one.

The narrowing, stated so the boundary is checkable rather than rhetorical. This build decides
exactly three things the instruction layer must then honour, and they are decided in §4's state
table rather than in prose: that a unit's position is READ from its spec's status header and its
declared pointers, never inferred; that `INPROGRESS` means built-but-not-landed; and that
`BLOCKED`, `DEFERRED` and `WONTDO` are never a `next:` target. Everything else about the work is the
other session's. The dependency is recorded as a backlog row so the parallel session inherits it
rather than rediscovering it.

`tools/hooks/agent-cap.js` and `memory/guides/REVIEW-PROTOCOL.md` are owned by another build.

The keepalive actor split is unchanged.

No adopter migration. Nothing has travelled the adopter path, so a migration would be untested code
for a population of zero.

## 4. Design

### The rule, and what the review did to it

> No input to the authorization comparison can be put outside the run's reach by a check running
> inside the run's own process. S0 removes the two that were free to forge, prices the rest, and
> records what an off-machine verifier needs.

That is rev-4's rule, and it replaces rev-1's absolute one. A design panel built four independent
anchor mechanisms — a network witness, forensic ref provenance, out-of-band attestation, and one
brief to reject the framing — and an adversarial skeptic broke all four. They converged on the same
reduction: a check running under the run's uid reads refs, objects, worktree files and config, and
the run writes all four, so if every input is local the run can construct the passing state exactly.
Both escapes — a secret the run lacks, an observation of an external party — leak for one reason:
what an external party returns is a NAME, and dereferencing a name happens in the subject's own
object store.

The panel also found two levers neither the review nor rev-2 had scoped, both effective at a
PERFECTLY honest anchor and both reproduced here with live controls: `git replace` substitutes the
object a sha resolves to, and a graft file rewrites the commit graph. Neither is closed by any amount
of anchor hardening, and `--no-replace-objects` does not stop the second.

So S0 is not "close the anchor". It is: make the two one-command offline forgeries inert, pin the
dereference, and state the boundary instead of asserting a false one. What that leaves open is
enumerated in the protocol's new §9 and is not a rounding error.

### What the new check is, precisely

| # | Assertion | Refuses when | Acceptance |
|---|---|---|---|
| 1 | the build README blob resolves at BASE | the folder was created on the run's own branch | AC2 |
| 2 | the blob parses as build front matter | the file exists but is not a build README | AC10 |
| 3 | its `slug:` equals the requested slug | a folder was renamed or a README copied between builds | AC11 |
| 4 | the plan region, when present at BASE, is byte-equal in the working copy | the run rewrote the scope it is executing against | AC4 |

Assertion 4 propagates a malformed-region status on EITHER side as its own refusal. The extractor's
exit code conflates "absent" with "two regions present", and rev-1 left the working-copy side
unstated — which is the discarded-error-signal defect from the prior build, reintroduced.

### What is lost, stated completely

Rev-1 named two losses. The review found three more.

1. **Integrity becomes existence.** The README is a living document whose generated region the run
   re-renders, so no whole-file equality is assertable. Assertion 4 buys integrity back over the plan
   region only.
2. **The grant widens from per-build to class-wide.** Every build folder in the tree satisfies the
   predicate. Ratified by the owner as F0a.
3. **The grant no longer names the ACTIONS.** Both charter statements read "naming the build and both
   actions". A README names no action, so merge-only or push-only becomes unexpressible and every
   build authorizes the maximum. F6 in §8 is the fork for it.
4. **The grant is irrevocable and retroactive.** A mandate could be withdrawn by deleting it. A build
   README cannot be deleted — the hygiene gate and the generated index depend on it — so after this
   lands there is no act meaning "not this build", and every build ever created is eligible.
5. **Authorization becomes self-propagating.** A legitimately authorized run whose diff creates a new
   build README authorizes the NEXT run by bytes a run wrote and landed. The per-run property still
   holds; the system property does not. Under the mandate this required authoring a file whose only
   purpose was authorization, which was conspicuous and tripped the single-live-run rule. Under
   README-existence it is indistinguishable from ordinary work.

Loss 5 changes the shape of the threat model, and no scope item addresses it. F5 in §8 puts it to the
owner rather than burying it.

### Data model

The run-state file's authored region after S2, using the fact names the driver actually reads. Rev-1
listed a `parked:` key that does not exist: the override path appends an unkeyed line and the reader
greps a different key, and the single-value reader takes only the first line.

```
phase: BUILDING
witness: <sha>
base: <sha>
keepalive: <id>
parked-surfaced: yes
```

Parked entries remain unkeyed appended lines, unchanged from the shipped shape.

The plan region in a build README, ORDINAL-keyed:

```
<!-- plan:units -->
1. the run-state file, and the hygiene contract that admits it
2. the protocol document, and the authorization it rests on
<!-- /plan:units -->
```

A spec claims its ordinal in its own status-header tail, which the format contract already reserves
for pointers. The join is therefore DECLARED by the spec, never inferred from a title. The review
measured zero of seven title matches on the prior build, and rev-1's design made the mismatch
unrecoverable: the run would see `SPEC NEEDED` forever and assertion 4 forbids editing the region to
match, so the run could neither converge nor repair.

Ids are not written in the plan region. Rev-1's reason was wrong — a dash-led backlog row DEFINES an
id, and the protocol requires minting one — but the conclusion holds for a different reason: a
numbered list row is not an anchor shape, so an id there would be a citation with no definition, and
the orphan waiver is full at five of five.

### Inventory

`--plan` reads two sources and no filenames.

| Source | Read via | Yields |
|---|---|---|
| planned units | the plan region, tracked, ordinal-keyed | the count and titles the owner intends |
| specs | the status header of each tracked spec | status, rev, the claimed plan ordinal, the review pointer |

Review coverage is read from the spec's own header tail, not from `reviews/` filenames. The review
measured the filename join wrong on 7 of 7 multi-unit builds and correct on none: the spec's sequence
number is a per-build record counter and a review's is "which review is this", the key is not unique
across families, and phase-scoped reviews cover many units at once. The two counters are not the same
quantity, so the join is not repairable.

The derived state per unit:

| Condition | State |
|---|---|
| a planned ordinal with no spec | `SPEC NEEDED` |
| a spec at `OPEN` | `SPEC NEEDED` |
| a spec at `SPECCED` with no review pointer | `REVIEW NEEDED` |
| a spec at `SPECCED` with a review pointer | `BUILD NEEDED` |
| a spec at `INPROGRESS` | `LAND NEEDED` |
| a spec at `BLOCKED` or `DEFERRED` | `PARKED`, never a `next:` target |
| a spec at `CLOSED` | `DONE` |
| a spec at `WONTDO` | `ABANDONED`, never a `next:` target |

`INPROGRESS` means built-but-not-landed in this tree, which the prior build's README states outright.
Rev-1's four-state table mapped it to `BUILD NEEDED` and would have told five live units to rebuild
what is already built.

A spec with no parseable status header is invisible to the collector. Five exist. `--plan` reports
them by path as `UNPARSEABLE` rather than silently omitting them, because reporting `SPEC NEEDED` for
a spec on disk makes the run write a duplicate.

### Migration

No live run-state file exists, so there is nothing to migrate at runtime. The migration is textual and
larger than rev-1 claimed. The explicit-ask rule is spelled in seven places, not four: `AGENTS.md`;
`parallel-coding-governance.template.md` in three sites plus its version marker;
`parallel-coding-governance.customize.md`'s conditional-sections row; `.claude/SESSION-KICKOFF.md`;
`WIRE-INTO-PROJECT.md`; `tools/memory-tree/HYGIENE.template.md` with its render; and the check-7
exemption comment in `tools/memory-tree/check-memory-hygiene.sh`, whose stated justification is that
the mandate is verbatim prose — a reason S2 deletes.

### Rollout

Two landings, not one. S0 lands first as its own series, because it repairs a live defect and must
not wait on a design the owner has not approved. S1 through S7 land after.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/unattended.sh` | S0, S1, S2, S3, S4, S6 |
| `tools/unattended/unattended.test.sh` | arms; and the source-grep arm keyed on the literal `check_mandate "` must move with the rename, or it passes by matching nothing |
| `tools/unattended/check-unattended.sh` | S0, S1; check 9 relaxes with the driver, not against it |
| `tools/unattended/check-unattended.test.sh` | arms, including all three prior attacks re-aimed |
| `tools/unattended/PROTOCOL.template.md` | S7, §1 §2 §3 §4 §6 §7 |
| `tools/unattended/SKILL.template.md` | S7 |
| `tools/unattended/.unattended.conf.example` | `CORE_FLOOR`; today it ships a value nothing compares against the driver |
| `.unattended.conf` | `CORE_FLOOR` to `9:6` |
| `memory/guides/UNATTENDED-PROTOCOL.md` | S7, the same six sections |
| `memory/TEMPLATE-README.md` | new, S5 |
| `tools/memory-tree/check-memory-hygiene.sh` | check 3's closed memory-root allowlist; the check-7 comment |
| `tools/memory-tree/HYGIENE.template.md` | the documented set; the live copy is a RENDER and is never hand-edited |
| `memory/HYGIENE.md` | re-rendered |
| `KIT_MEMORY_TREE_VERSION` | the verdict-epoch gate requires it to move with the engine |
| `.memory-tree.conf` | `ARMS_FLOORS` for both unattended scripts and for the hygiene engine |
| `parallel-coding-governance.template.md` + archive snapshot | three clause sites and the version marker |
| `parallel-coding-governance.customize.md`, `WIRE-INTO-PROJECT.md`, `AGENTS.md` | S7 |
| `.claude/SESSION-KICKOFF.md` | S7 and the ratchet re-stamp |
| `skills/session-kickoff/SKILL.md` | Step 5b; the leg asserts a literal exit count of exactly six against a floor of six |
| `.claude/skills/unattended/SKILL.md` | re-rendered |
| `memory/map/features/unattended.md` | constraints and gaps both change |

### Alternatives rejected

**A conf-declared policy key, or a README front-matter key.** Both rejected by the owner as F0a. They
preserved a genuine per-build opt-in and named both actions.

**Keeping the mandate and generating it.** A mandate the toolchain produces is self-authorization
with an extra step.

**Repairing the filename join.** Rejected on measurement, not taste. The two sequence numbers are
different quantities.

**Calling `gen_build_index.py` from the driver.** Refuted by a shipped, armed assertion at
`tools/unattended/unattended.test.sh:384-388` that refuses any python launcher in the driver. The
driver is bash, the module exposes no machine-readable mode, and the two kits install independently.
S4 therefore parses the status header in the driver's own language, and §10 records the cost.

## 5. Production-readiness checklist

- **security** — the build is one security property, and the honest verdict is that it is raised
  rather than met. S0 makes two one-command offline forgeries inert and prices the rest; the protocol
  §9 enumerates what stays reachable, including three things no scope item here closes — a run that
  edits this kit, one that shims the tools it calls, and one that skips the hook layer. AC12 proves
  what S0 does buy. The control that actually binds is an off-machine re-run of the same leg in a
  clone the run never touched, and it is a backlog row, not a scope item.
- **perf / scale** — one extra tracked-file pass per build. Immaterial.
- **a11y** — N/A — a shell driver with no user interface.
- **i18n** — N/A — the repo is single-locale by charter.
- **error / empty / loading states** — six cases need defined answers: no plan region; an empty plan
  region; an empty `spec/`; no `reviews/` directory (nine builds); a spec with no parseable header
  (five specs); and a build with no specs at all. Rev-1 covered three.
- **observability** — `--status` gains the derived position. Every refusal names itself.
- **risks (concurrency, data-loss, rollback hazards)** — four.
  - **The leg goes blind on an untracked run-state file.** Every leg check is keyed on tracked files.
    Under S2 the run creates the file, so it is untracked until committed, and seven checks vanish
    silently. This is why S2 commits it, and why the single-live-run rule would otherwise let two
    concurrent preflights each see zero live runs.
  - **The ARMS floor is a per-gate NET count.** S1 deletes six named guards and adds four. If the net
    lands at or above the pin, nothing reds and six guards disappear unnoticed. The per-gate design
    stops cross-gate masking and cannot stop within-gate masking, which is this build's exact shape.
    The floors are re-measured and re-pinned in the same commit, and AC13 asserts the count.
  - **The drift signal has zero headroom.** `non_terminal_specs_cited_by_product_source` sits at its
    pin, and six of S7's seven targets are inside its globs. A single comment citing this spec's id
    while it is non-terminal reds the bar.
  - **Data loss.** Reduced. No owner bytes live in the file the driver splices.
- **testing + left-shift gates** — every branch added or moved needs a positive assertion naming its
  own failure text. Two arms are keyed on literal strings this build changes: the source grep for
  `check_mandate "`, and the kickoff leg's exit count.
- **migration / rollback** — no runtime state; rollback is a revert. S0 reverts independently.
- **user docs** — the rendered skill and the protocol. Note the limit honestly: the wiring check
  compares the render to its template and the parity leg compares the two protocol copies to each
  other. Neither compares any of them to the driver's actual behaviour, so a stale claim that lives
  in BOTH copies is invisible to every gate.

## 6. Acceptance criteria

**AC1** — When a build's README is committed on the default branch and a run branches from it and
invokes `--preflight` having authored nothing, preflight succeeds and creates and commits the
run-state file.

**AC2** — When a run creates a build folder and README on its own branch and invokes `--preflight`,
preflight refuses, naming that the README does not resolve at the pinned BASE.

**AC3** — When the merge-base equals HEAD, `--preflight` proceeds with an explicitly defined BASE and
`--close` refuses, with the close refusal text unchanged.

**AC4** — When a plan region present at BASE differs in the working copy, or is malformed on either
side, `--preflight` refuses, with the malformed case its own named refusal.

**AC5** — When `--plan` runs over a fixture carrying one `CLOSED` unit, one `SPECCED` unit with no
review pointer, one `INPROGRESS` unit and one planned ordinal with no spec, it prints four rows
reading `DONE`, `REVIEW NEEDED`, `LAND NEEDED` and `SPEC NEEDED`, in plan-ordinal order, and a
`next:` line naming the review. The case runs in `unattended.test.sh`.

**AC6** — When `PHASES_CORE` holds nine members and `.unattended.conf` declares a phase floor below
nine, a leg refuses. This is a NEW check: the shipped one fires only when the core set shrinks below
the floor, so a stale floor is silently legal and rev-1's AC asserted the comparison backwards.

**AC7** — When each of the three prior attacks is re-aimed at the new surface, `--preflight` refuses
in all three and `check-unattended.sh` refuses independently in all three.

**AC8** — When the adopter check runs after the render, it exits 0 and the render carries no surviving
placeholder.

**AC9** — When the codebase-map coverage gate runs, every inventory this build moves is claimed and
the generated artifacts byte-compare against a fresh render.

**AC10** — When the blob at BASE is not parseable build front matter, `--preflight` refuses.

**AC11** — When the blob's `slug:` does not equal the requested slug, `--preflight` refuses.

**AC12** — When the anchor ref is moved with `git update-ref` to a commit the run authored, and again
when `GOV_DEFAULT_BRANCH` names a manufactured tracking ref, `--preflight` refuses and
`check-unattended.sh` refuses. Both arms carry a live control that passes on an honest anchor.

**AC13** — When the harness meta-gate runs, the re-measured branch and armed counts for both
unattended scripts equal their re-pinned floors, and the count is asserted rather than inferred from
the gate's silence.

## 7. Gates

The full bar at the push boundary. Legs this build MOVES rather than merely keeps green: both
unattended legs and their two self-tests, the adopter check and its e2e, the harness meta-gate against
re-pinned floors, the memory hygiene engine, the verdict-epoch gate, the kit-version pair, the
kit/dogfood parity leg, the hygiene-parity floor, the template size gate, the kickoff-manifest ratchet,
the codebase-map coverage gate, and the drift-audit records leg. Rev-1 claimed no leg moves; twelve do.

No new gate leg is added. `--plan` is exercised by the driver self-test, which is itself a leg.

## 8. Open questions

none — every fork below is RESOLVED, the owner ratified each on 2026-08-11, and P1 in the build
README resolved with them.

**F1 — is assertion 4 a hard precondition or an opt-in?** Rev-1 recommended opt-in with the template
shipping the region. The review showed those two halves contradict: an empty region is a refusal, so a
scaffolded build refuses until the owner hand-fills it, which is the per-build authoring F0a removed.
RESOLVED (owner, 2026-08-11): opt-in, and the template ships the region COMMENTED OUT with one line
saying what filling it buys. No build refuses, and filling it is a choice with a stated benefit.

**F2 — does the recorded-BASE assertion relax from equality to ancestry?** The review refuted rev-1's
defence of this — the defence was assertion 4, which F1 makes conditional, so a run reaching back past
the region's introduction escapes both. It also found rev-1's premise wrong: the mandated lander
refuses to run off the default branch, so it cannot move the run's branch.
RESOLVED (owner, 2026-08-11): keep equality. Relaxing a guard for a hazard nobody has reproduced is
how the anchor bypass survived for two reviews.

**F3 — does `--plan` read tracked files only?** RESOLVED (owner, 2026-08-11): tracked only. The
filename-join question this fork disclaimed in rev-1 is resolved in §4 by deleting the join.

**F4 — is the widening recorded as a decision row?** RESOLVED (owner, 2026-08-11): yes, naming all
five losses rather than the class grant alone. Written as the first of two rows recorded for this
build in `memory/DECISIONS.md`.

**F5 — is self-propagating authorization acceptable?** A run that lands a new build README authorizes
the next run. Options were: accept it; refuse a build README whose introducing commit is authored by
an unattended run; or require the plan region for any build created after this lands.
RESOLVED (owner, 2026-08-11): require the plan region for any build created after this lands. It is
the cheapest of the three, it is mechanical, and it makes assertion 4 non-vacuous for exactly the
population that can propagate. The 26 builds that predate this keep existence-only authorization,
and that grandfathering is deliberate: they were created before any run could have authored them.

RE-ANSWERED at rev-5, because S5 withdrew the artifact this resolution named. The build method's M2
makes the README's authored Units table the roster, and that table is what a build README already
carries here — so the integrity comparison binds to the Units table rather than to a plan region
nobody now builds. The property is unchanged and the ratified intent is honoured; only the surface
moved, and it moved onto one that already exists. Where a README carries no Units table, M2 falls
back to the specs under `spec/`, and a build with neither is not a build a run can execute anyway.

**F6 — how are the ACTIONS named, now that the README names none?** Options were: accept that every
build authorizes both; declare the pair once in the conf, which F0a rejected; or let the plan region
carry an optional actions line. RESOLVED (owner, 2026-08-11): accept that a build authorizes both,
and say so in the amended charter sentence rather than leaving the old wording to mean something new.
The replacement wording is written in §4's Migration and is a scope item, not a paraphrase.

**F7 — where is the parallel session owning the instruction layer?** The review could not find it.
RESOLVED (owner, 2026-08-11): the layer stays out of scope and the cut-line is NARROWED instead, in
§3, to the three decisions §4's state table actually makes. A backlog row records the dependency so
the parallel session inherits it. If that session proves not to exist, the row is what surfaces it.

**F8 — does S0 land as its own series, ahead of any decision on S1 through S7?**
RESOLVED (owner, 2026-08-11): yes. It repairs a live bypass in merged code and depends on none of the
design questions above. Its mechanism is settled by a dedicated design panel rather than by this
author's first instinct, because the first instinct is what shipped the bypass.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft. Two owner forks resolved at kickoff as F0a and F0b; four opened.
- rev-2 · 2026-08-11 · folded review-aStandingWrit-1, which returned do-not-build. Added S0 for the
  anchor bypass the review reproduced in landed code. Deleted the filename join and the title match
  from S4 in favour of declared pointers. Replaced the four-state table with an eight-state one that
  can express built-but-not-landed. Corrected seven factual claims. Expanded the amendment set from
  four files to seven and the moved-leg count from zero to twelve. Named three further losses and
  opened F5 through F8. Status returned to OPEN.
- rev-3 · 2026-08-11 · all eight forks RESOLVED by the owner, every one as recommended. F5 adds the
  plan-region requirement for builds created after this lands, with the existing 26 grandfathered.
  F6's replacement charter wording becomes a scope item rather than a paraphrase. F7 narrows §3's
  cut-line to the three decisions the state table makes, instead of asserting an owner for the rest.
  Two decision rows recorded. Status SPECCED; S0's mechanism is pending a dedicated design panel.
- rev-4 · 2026-08-11 · the panel returned and S0 is BUILT. Its verdict refuted this spec's central
  design rule, which is rewritten in §4 rather than quietly dropped: the hole is not closable by a
  check inside the run's own process, and two further levers were found that defeat the mandate
  comparison at a perfectly honest anchor. The protocol gains a §9 stating the boundary, and the
  charter's claim is amended to match. Status INPROGRESS: S0 landed, S1 through S7 not started.
- rev-6 · 2026-08-11 · S8 arrives from P1's resolution: the roster marker pair and the integrity
  check bound to it. F5 is REWRITTEN rather than re-answered again — it was ratified as "refuse
  self-propagating authorization" and no option on the table ever did that; what its mechanism
  restored was the integrity property, and saying so is the only honest version. §8's first line is
  made machine-legal, because hygiene check 12 reads that line and nothing else and would have redded
  this spec the moment its status went terminal.
- rev-5 · 2026-08-11 · reconciled against `memory/guides/BUILD-METHOD.md`, which landed on main while
  S0 was building and is the instruction layer F7 recorded as unlocatable. S5 is WITHDRAWN: M2
  answers the roster question with no new artifact and resolves the `ids:` ambiguity that was S5's
  stated motivation. S4 is rescoped to MECHANISE M2's four states rather than carry the eight-state
  vocabulary rev-2 invented, which is now a second spelling of one question. S6's phase members are
  renamed for M6's pass kinds. F5's mitigation moved with S5 and is re-answered in §8. Nothing about
  S1, S2, S3 or S7 changed — the authorization half of this build never overlapped that document.

## 10. Reuse audit

The reuse lookup returns `parse_spec` and `derive_status` in `tools/memory-tree/gen_build_index.py`,
and `.unattended.conf` as this kit's affordance seam.

**The obvious reuse is unavailable, and rev-1 claimed it anyway.** `tools/unattended/unattended.test.sh:384-388`
is a shipped, armed assertion that the driver invokes no python launcher, on the stated ground that a
bare launcher in that file would be an unresolved one. The driver is bash; the module exposes only
`--check`, `--write` and `--selftest`, all of which print prose; and the two kits copy-install
independently, so a spelled sibling path assumes another kit's prefix in an adopter tree. There is no
seam, and rev-1's §10 asserted one.

S4 therefore reimplements the status-header parse in the driver's own language, and this spec records
the cost rather than hiding it: two parsers now read one header, which is the shape that agrees until
it does not. The mitigation is that the header grammar is FROZEN by a published format contract and a
gate already enforces it, so both parsers read against a specification rather than against each other.
The alternative — adding a machine-readable mode to `gen_build_index.py` and a conf key naming it —
was rejected because F0a ratified that this kit gains no declaration.

`.unattended.conf` is read for the memory root and the core floor, and gains no key.
