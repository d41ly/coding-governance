# TOOL-aBoundedVerdict-21 — the landing push is bounded too

**Status:** WONTDO · rev-3 · 2026-08-21 · node c · Tier-2 · base 098bebd9 · streams tooling

## 1. Goal

`TOOL-aBoundedVerdict-13` bounds every remote OBSERVATION the driver makes, and stops at the one
remote operation that matters most: the landing push. A hung `$LANDER` is the same indefinite silent
stall one command later, and it happens after the Definition of Done has passed — the point at which a
run has the least reason to be watched. Bound it, without turning an opaque project declaration into
a command this kit pretends to understand.

## 2. Scope (IN)

- **S1** — the driver bounds the invocation of `$LANDER` with the same wall-clock helper
  `TOOL-aBoundedVerdict-13` introduces, and with a SEPARATE constant: a push legitimately takes longer
  than an advertisement, so reusing the observation bound would convert a working slow push into a
  refused landing.
- **S2** — the bound wraps the lander as an OPAQUE command. No parsing of its output, no assumption
  about its transport, no injected git config — the kit already refuses to read `$LANDER`'s output and
  that refusal is not weakened here. What is added is a deadline, which is the one thing that can be
  imposed on a command whose internals are none of the kit's business.
- **S3** — a bounded-out push is a NAMED refusal that says the push was killed rather than that it
  failed, names the elapsed bound, and does NOT record a terminal phase. A landing whose outcome is
  unknown must not be recorded as landed OR as aborted: the remote may have received the push.
- **S4** — the run-state file records the ATTEMPT before the push and its outcome after, so a resumed
  run can tell "never attempted" from "attempted, outcome unknown". Without this, S3's refusal is
  unrecoverable by the protocol's own post-compaction path, which re-derives state from the record.
- **S5** — the RESUME path handles the unknown-outcome case: a run resuming into it re-observes the
  remote rather than re-pushing, because the push may have succeeded and a second one is either a
  no-op or a conflict, and the driver cannot tell which without looking.
- **S6** — the declared bound is documented where an adopter sets `LANDER`, because a project whose
  lander legitimately takes longer than the default needs to know the knob exists before it fires.

## 3. Non-goals (OUT)

- Not the observation bounds. `TOOL-aBoundedVerdict-13` owns every `ls-remote`, and this unit reuses
  its helper rather than adding a second one.
- Not retries. A bounded-out push whose outcome is unknown is re-OBSERVED, never re-pushed; deciding
  whether to retry a landing is a policy this unit has no evidence to set, and getting it wrong
  duplicates a merge.
- Not parsing `$LANDER`'s output, and not a contract on what it prints.
  `TOOL-aBoundedVerdict-18` adds a declared marker for a different question — whether the lander ran
  at all — and this unit reads nothing.
- Not the pre-push hook's own runtime. That the hook runs the full bar inside the push, and that the
  bar can be slow, is the bar's business; the deadline here is on the push as a whole and the spec
  says so rather than implying it bounds the gate.
- No change to `LANDER`'s value set, to which verb invokes it, or to the bypass ban.

## 4. Design

### Why a separate constant

The observation bound in `TOOL-aBoundedVerdict-13` is sized for an advertisement — single-digit
seconds measured on this fleet, bounded generously. A push carries objects and, under
`.githooks/pre-push`, runs the entire merge bar first: measured on node `a`, 335s serial and ~95s at
width 8, and the bar's own recorded worst case is a timeout on a polluted `TMPDIR`. So the push's
honest bound is an order of magnitude larger, and sharing one constant would either strangle the push
or leave the observations effectively unbounded. Two constants, each sized for its own operation, and
each stated in its own refusal.

### The unknown-outcome problem, which is this unit's real content

Killing a push is not like killing a read. The remote may have received and accepted the objects
before the deadline fired, so three states exist where the observation path has two:

| state | what the record must say | what resume must do |
|---|---|---|
| push not attempted | nothing | push |
| push completed | the landed terminal, with its witness | nothing |
| push killed, outcome UNKNOWN | attempted, outcome unknown | **re-observe the remote**, then decide |

S4 exists because the third row is unrepresentable today: the run-state file records a phase, and
neither `LANDING` nor `LANDED` says "I pushed and do not know whether it worked". S5 exists because
the only safe action in that row is a read. This is the whole reason the unit is Tier 2 rather than a
one-line `timeout` in front of `$LANDER`.

### Inventory

| Concern | Today | After |
|---|---|---|
| a hung `$LANDER` | indefinite, after the DoD has passed | bounded, with a named refusal |
| the bound's size | none | its own constant, sized for a push plus a full bar |
| a killed push | indistinguishable from one never attempted | recorded as attempted, outcome unknown |
| resume after a killed push | would push again | re-observes the remote first |
| the lander's opacity | preserved | preserved — a deadline is not a parse |

### Migration

None on disk. One behavioural change: a push that today hangs forever now refuses, and the run stops
in a state the record can express — which is the point.

### Rollout

`TOOL-aBoundedVerdict-13` first, for the helper. Then S4, because the record must be able to express
the state before anything can produce it. Then S1-S3, then S5, then S6's documentation.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the constant, the wrapped invocation, the refusal, the attempt
record, the resume arm) · `tools/unattended/unattended.test.sh` ·
`memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` (the landing
section and the fact list, if S4 adds a fact) · `tools/unattended/.unattended.conf.example` (S6) ·
`.memory-tree.conf` (`ARMS_FLOORS`) · the kit version constant ·
`memory/map/features/unattended.md`.

### Alternatives rejected

- **One shared bound with the observations.** Rejected in §4: the two operations differ by an order of
  magnitude and one constant strangles or loosens whichever it was not sized for.
- **A bare `timeout` in front of `$LANDER` and nothing else.** This is the tempting one-line version
  and it is refused: it creates the unknown-outcome state without giving the record a way to say so,
  which converts an indefinite hang into an unresumable run. Strictly worse than the hang, because the
  hang is at least diagnosable.
- **Retry the push once on a bound-out.** Rejected in §3: the first push may have landed.
- **Record the killed push as ABORTED.** Rejected: abort is terminal and means the run did not land, and
  a push whose outcome is unknown may have landed. A terminal claim that might be false is worse than
  a non-terminal one that is true.
- **Have the lander impose its own deadline.** Rejected: it moves the obligation onto every adopter's
  lander, and the kit already has the helper.

## 5. Production-readiness checklist

- **security** — no new surface; the deadline reads nothing. One note: the kill must not leave a
  partially written run-state file that a later run reads as authoritative, which is why S4 writes the
  attempt BEFORE the push rather than reconstructing it after.
- **perf / scale** — N/A on the happy path.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — the unknown-outcome state IS this unit's error state, and §4's
  table is its specification.
- **observability** — S3's refusal distinguishes killed from failed, which is the distinction an owner
  returning to the run needs first.
- **risks** — the real one is the false positive: a legitimately slow push killed by a bound sized too
  tight, which is why the constant is generous and S6 documents it. Second: S5's re-observation reading
  a remote that is still partitioned, which reduces to `TOOL-aBoundedVerdict-13`'s bound and refusal.
- **testing + left-shift gates** — a fixture whose lander sleeps past the bound, and one whose lander
  succeeds slowly but inside it. The second is the false-positive arm and is the one that proves the
  bound is not merely tight enough to pass the first.
- **migration / rollback** — none; revert is the wrapper.
- **user docs** — S6, plus the map dossier.

## 6. Acceptance criteria

- **AC1** — When a fixture declares a `LANDER` that sleeps past the bound, the driver refuses within
  the bound, its message says the push was KILLED and names the elapsed bound, and the run-state file
  records no terminal phase — asserted on the on-disk effect, not the exit code alone.
- **AC2** — When a fixture's `LANDER` succeeds slowly but inside the bound, the landing completes
  normally; the false-positive arm in `tools/unattended/unattended.test.sh`.
- **AC3** — When the push is killed, the run-state file distinguishes attempted-outcome-unknown from
  never-attempted, and `bash tools/unattended/unattended.sh --status <slug>` reports it.
- **AC4** — When a run resumes into the unknown-outcome state, `--resume` issues a remote OBSERVATION
  and no push — asserted in `tools/unattended/unattended.test.sh` with a fixture whose `LANDER` writes a
  sentinel and fails if called twice, so the arm fails if the resume re-pushes.
- **AC5** — When `grep -c 'LANDER' tools/unattended/unattended.sh` is read, no site parses the
  lander's output; the opacity arm, which fails if the bound was implemented by scraping.
- **AC6** — When the push bound and the observation bound are compared in source, they are two
  distinct constants; `bash tools/unattended/check-unattended.sh` is clean and the protocol pair's
  landing section names the push bound in both halves.

## 7. Gates

`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.sh` +
`check-unattended.test.sh` · `bash tools/unattended/adopt-unattended.sh --check` ·
`.githooks/pre-push.test.sh` and `tools/push-main.test.sh` (the lander and the hook are both in the
path this unit wraps) · `python tools/memory-tree/check-arms.py` ·
`tools/check-testsuite-counts.sh` · `tools/check-kit-versions.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none - every fork below is RESOLVED in place, each naming the resolver and the authority.
This line is the machine-read one; the bullets carry the reasoning.

- **F1 — what is the push bound, in seconds?** It must exceed a full bar run plus an object transfer:
  measured 335s serial and ~95s at width 8 on node `a`, with a recorded timeout case above ten
  minutes on a polluted `TMPDIR`. **Recommendation: 900s**, generous by design, on the reasoning
  `TOOL-aBoundedVerdict-13` F1 already used — the failure being guarded is a hang, not slowness, and a
  tight bound converts a working push into a new stall.
  RESOLVED (agent, 2026-08-19, delegated): 900s, stated in the refusal so it is discoverable without
  reading source. Mechanism-only fork.

- **F2 — does S4's attempt record become a new authored FACT, or a parked line?** A fact is a per-run
  singleton read by key, which is what "did I attempt the push" is; a parked line is append-only
  history. **Recommendation: a FACT**, on the same shape argument `TOOL-aBoundedVerdict-2` used for the
  halt code — and it moves whatever ordinal the region's pin currently states, read at build time
  rather than spelled here, for the reason that spec's rev-6 records.
  RESOLVED (agent, 2026-08-20, delegated): a FACT. Mechanism-only on its own terms, and the
  feature-rich survivor: S5's resume path must READ "did I attempt the push" by key, and a parked
  line is append-only prose no reader can join on — the same argument `TOOL-aBoundedVerdict-5` F1
  used to keep an id OUT of a parked line. The build README's cross-unit rule said the authored
  region's fact pin moves EXACTLY ONCE in this build; that rule predates this unit, which the
  owner's resolution of `TOOL-aBoundedVerdict-13` F3 created, and the README is corrected in the
  same commit rather than left disagreeing with a spec. The rule's real content — a fact is added
  only for a per-run SINGLETON, and whoever moves the pin moves every spelling of it — is unchanged
  and this unit is bound by it. The pin is READ at build time, never spelled here.

- **F3 — OWNER, not delegated. Should a bounded-out push with an unknown outcome be surfaced
  immediately rather than left for the resume path?** S5 makes a resumed run safe, but an unattended
  run that bounds out at the push has finished its work and cannot tell whether it landed — arguably
  the one state worth waking someone for. Options: leave it to resume, as specced; or treat it as a
  notify-and-stop. The options differ in whether this unit gains an owner-notification mechanism at
  all, so it goes up.
  RESOLVED (agent, 2026-08-20, delegated): left to the resume path, AS SPECCED — and by VETO
  rather than by choice. Only one option survives M3's vetoes — notify-and-stop needs an owner-notification
  mechanism this kit does not have, which is veto 2, a new public surface. Declining to WIDEN scope
  is not exercising the scope authority a run does not hold; taking the notify option would have
  been. **The vetoed option is PARKED to the owner** in this run's run-state file and reaches them
  at the wrap-up, so a fork answered by a veto is not a fork quietly dropped.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Created by the owner's resolution of `TOOL-aBoundedVerdict-13`
  F3: the landing push IS bounded, in a follow-up unit rather than inside the unit scoped to
  observations, because wrapping a project-declared command changes a contract every adopter reads.
  The unit is Tier 2 not for the deadline — that is one line — but for the unknown-outcome state the
  deadline creates, which the run-state file cannot express today and which makes the naive one-line
  version strictly worse than the hang it replaces. F1 and F2 resolved under the delegated fork rule;
  F3 raised to the owner because it would add an owner-notification mechanism this kit does not have.

- rev-2 · 2026-08-20 · M3 fork sweep, before any code. F2 RESOLVED as recommended, a FACT, on S5's
  grounds rather than on shape alone — the resume path READS it by key and a parked line cannot be
  joined on. That resolution contradicts the build README's "the fact pin moves exactly once" rule,
  which was written before this unit existed; the README is corrected in the same commit and the
  rule's real content is kept. **F3 was the owner's and is resolved by VETO, not by an agent picking
  between the owner's options:** notify-and-stop adds an owner-notification mechanism this kit does
  not have, veto 2 discards it, and one option survives. The vetoed option is parked to the owner so
  the turn this run did not take is still theirs. §8's first non-blank line is now the machine-legal
  `none` form, which is what lets this unit reach terminal at all.

- rev-3 · 2026-08-21 · **WONTDO, and the reason is an M3 veto rather than a judgement about
  value.** This unit would bound the landing push the way `TOOL-aBoundedVerdict-13` bounds every
  observation. The mechanism fork has no survivor the run may pick: the lander is MANDATED and
  project-declared, so bounding its push means either editing a command the project owns or
  wrapping it in the kit, and choosing between those changes what an adopter's `LANDER` means.
  M3 reserves that to the owner, and an unattended run may not resolve a fork by preferring one
  option. Parked with both options and this reason; the spec stays for whoever answers it.

  Recorded as WONTDO rather than left SPECCED because a non-terminal unit blocks `build-complete`,
  and blocking the close on a question nobody is present to answer is the stall this whole build
  exists to remove. WONTDO says the run declined it; it does not say the idea was rejected.

## 10. Reuse audit

The seam is `TOOL-aBoundedVerdict-13`'s bounded-observation helper, extended with a second constant
rather than copied — that unit's own §4 argues against two spellings of one bound, and this unit is
the second caller that argument anticipated.

The second seam is the run-state fact writer and `refuse_if_terminal`: S4 adds a fact through the
existing writer and S3 deliberately does NOT record a terminal, so nothing about the terminal set or
its guard changes. `$LANDER` itself stays what it is — a project declaration invoked opaquely — and
AC5 is the arm that keeps it that way.

`tools/push-main.sh` is read, not changed: it is this repo's declared lander and the fixture for AC2's
slow-but-successful arm is modelled on it rather than on a stub, so the false-positive arm is measured
against something shaped like a real lander.

Recall terms used, at the SET level for this build: `closing review round cap blocked verdict
adversarial diff fold unattended close build-complete DoD stall halt`.
