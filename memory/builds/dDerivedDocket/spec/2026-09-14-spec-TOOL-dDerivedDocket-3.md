# TOOL-dDerivedDocket-3 — the run's landing path

**Status:** SPECCED · rev-4 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round1.md) | spec-audit | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round2.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g1-round2.md) | spec-audit | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 |

<!-- /gen:spec-records -->

## 1. Goal

`gates-green` is one boolean over `$GATE_CMD` run in the run's own tree, so it grades the branch and
never the merge that actually lands; a branch green alone can land red once merged onto a tip the
remote moved. And the unattended landing still goes through the primary tree and local main. Wire
the in-place lander into the run: a declared lander mode, a Land step that prepares the merge
before the close, a close whose bar grades that prepared merge, records committed on it, and a
landing that cannot complete ending HELD instead of on local main.

## 2. Scope (IN)

- **S1** `LANDER_MODE`, a closed set `primary|in-place` in `.unattended.conf`, blank reading as
  `primary` and announced as a default. Gov's conf sets `in-place`; the kit's conf example documents
  both. The driver and the kit gate validate it. The kit gate prints the effective `LANDER_MODE`
  and whether it was declared or defaulted, and each `SELFTESTS_OWED_PATHS` entry it resolved,
  printing that the list is empty when it is. Observed by AC5, AC9 and AC13.
- **S2** Under `in-place`, `--preflight` runs `$LANDER --carry --slug <slug>` and
  `$LANDER --prepared --slug <slug>` once each, as liveness probes of the declared lander. On either
  probe, an exit of 2 refuses preflight naming `LANDER_MODE`, because the lander rejected a flag it
  does not implement, and an exit of 3 refuses naming the lander's observation failure, never
  `LANDER_MODE`. Exits 0 and 1 both mean a lander that implements the mode. Observed by AC5.
- **S3** Under `in-place`, `gates-green` refuses, numbered, unless `$LANDER --prepared --slug <slug>`
  exits 0, mapping its exits as S2 maps them: 1 names `{{LANDER}} --prepare`, 2 names `LANDER_MODE`,
  and 3 names the lander's observation failure and never `--prepare`; and otherwise runs
  `$GATE_CMD` with `GATE_FULL=1` exported, plus `GATE_SELFTESTS=1` when the landing range touches a
  path the new `SELFTESTS_OWED_PATHS` key lists. It runs before `--close` writes anything. Under
  `in-place`, `gates-green` also refuses, numbered and before
  running, when `git status --porcelain` is non-empty, untracked files included, naming the
  full-green stamp's clean-tree precondition (`tools/run-gates/run-gates.sh:1114-1119` and
  `:1861-1863`). Observed by AC1, AC2, AC10 and AC12.
- **S4** Under `in-place`, `--close` asks `$LANDER --carry --slug <slug>` after the Definition of
  Done evaluates and before any write, and refuses on exit 1 quoting the lander's list. Observed by
  AC6.
- **S5** Under `in-place`, `--close` COMMITS its run-state change on top of the prepared merge with
  the subject `records(<slug>): close — LANDING`, leaving the tree clean, which closes
  TOOL-dUnstalledConvoy-24 for this mode. The push boundary's scoped bar then covers that
  records-only delta, because the full-green stamp at the prepared merge sits in the same git dir.
  Protocol §2's rotation paragraph, the driver comment above `archive_name_of`
  (`tools/unattended/unattended.sh:1680-1681`), and the test comment at
  `tools/unattended/unattended.test.sh:2484` stop giving 'no verb commits' as the reason the archive
  name derives from the bytes. The reason that still holds is that two runs can honestly share a
  witness. A re-close whose write changes no byte commits nothing and says so. Observed by AC3, AC7,
  AC14 and AC15.
- **S6** The Skill's Close and Land sections and protocol §6 carry the in-place sequence —
  attestations and their commit, then `{{LANDER}} --prepare`, then `--close`, then
  `{{LANDER}} --land`, then `--landed` — with reconcile only from the remote's default branch onto
  the run branch, never through local main. A landing the lander could not complete pushes the
  branch and holds with `--reaped` naming the keepalive the close's attestation reaped, and never
  merges into local main. When the remote answers nothing at all, it holds over the unpublished tip
  under `platform-unavailable`. A `--close` refused on the lander's observation failure takes the
  same hold. The Skill's `While it runs` bullet, which at BASE has the main loop run kit work's
  `GATE_SELFTESTS=1` bar by hand at `VERIFYING`, names `--close` as where that bar runs under
  `in-place`, because `gates-green` runs it there. Observed by AC4, AC8 and AC16.
- **S7** Under `primary`, every verb behaves as at BASE. Observed by AC9.
- **S8** Arms in `tools/unattended/unattended.test.sh` and `tools/unattended/check-unattended.test.sh`,
  written in this unit's pass and run under attribution at the build's one post-build bar, the run
  the main loop makes at VERIFYING after the last unit. Observed by AC11.

## 3. Non-goals (OUT)

- The lander's own flags and the carry predicate. They are the in-place landing merge unit's, and
  this unit calls them rather than re-spelling them.
- Deriving LANDED from the advertised tip, and `--landed` refusing the local-main arm in `in-place`
  mode (KF4). The derived-terminal unit owns both, and receives this unit's committed LANDING record.
- The charter's §1 sentence recording the unattended landing exception (D12-i3). That text is the
  charter-template unit's; this unit writes the rule where D12-i3 says it lives, in the protocol.
- A relaxed or second stamp kind for a landing over inherited reds (KF2). The inherited-red policy
  unit adds `gate-inherited-green`; this unit only ever writes the ordinary stamp, and only green.
- The bound the landing bar runs under. It stays `GATE_BOUND` until the declared-wall unit derives
  it; the risk that a full bar with self-tests outlasts that bound is stated in §5.
- Attributing a red landing bar leg. The red-attribution unit owns that; here a red bar is unmet.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-1` — the attributed criterion for the unattended suites this
  unit's verification reads: `verdict clean`, with every inherited suite filed.
- **consumes-from** `TOOL-dDerivedDocket-2` — `--prepare`, `--land`, `--carry` and `--prepared`,
  their refusal texts and exit codes, and the definition of a prepared merge, which `gates-green`
  asks `--prepared` about.
- **consumes-from** `TOOL-dDerivedDocket-4` — `derived_phase()` and HELD's refusal of `--close`,
  the `--hold` verb an incomplete landing ends with, and the companion guide the landing text
  overflows into; including its unpublished-tip exception for `platform-unavailable`, the one route
  when the branch push fails too.
- **hands-off** `TOOL-dDerivedDocket-22` — the LANDING record committed on the prepared merge, from
  which that unit derives LANDED once the remote carries it, and the in-place mode `--landed` must
  refuse the local arm under.
- **hands-off** `TOOL-dDerivedDocket-34` — the in-place landing sequence S6 carries, a reconcile from
  the remote's default branch onto the run branch and then `--prepare`, `--close`, `--land` and
  `--landed`, into which the switch-over's landing reconcile puts its steps before `--prepare`.

## 4. Design

### The sequence under `in-place`

```
{{LANDER}} --prepare --slug <slug>            # merge onto the advertised tip, in this worktree
bash {{KIT_DIR}}/unattended.sh --close <slug> # bar on the prepared merge, carry check, commit
{{LANDER}} --land --slug <slug>               # push HEAD to the default branch through the hook
bash {{KIT_DIR}}/unattended.sh --landed <slug>
```

The order is forced by one fact: the full-green stamp is written only by a clean, unmoved run
(`tools/run-gates/run-gates.sh:1861`), so the bar must run on the prepared merge before the close
writes a byte, and the push must reuse that stamp rather than pay a second full bar. The lab showed
the graded merge, its stamp and the push resolving one git dir from the run's own worktree.

### `gates-green`

| Mode | Precondition | Command |
|---|---|---|
| `primary` | none, as at BASE | `$GATE_CMD` |
| `in-place` | `$LANDER --prepared --slug <slug>` exits 0 | `GATE_FULL=1 [GATE_SELFTESTS=1] $GATE_CMD` |

The self-test term is derived, never assumed. The landing range is `<T^1>..HEAD`; when any path it
touches starts with an entry of `SELFTESTS_OWED_PATHS`, the bar gets `GATE_SELFTESTS=1`. Blank means
never, announced, which is the charter's "owed by a DoD only for KIT work" with the kit surface
declared rather than guessed. Gov declares its kit roots. Nothing here runs the unattended kit's
own suites, which live in no manifest; `GATE_SELFTESTS=1` runs only held manifest legs.

At BASE the Skill's `While it runs` bullet, the build method's M6 carrier, tells the main loop to run
the `GATE_SELFTESTS=1` form by hand at `VERIFYING` for kit work, beside the plain bar `--close` runs.
Under `in-place` that form is this derived term inside `gates-green`, so the bullet names `--close`
for it and a landing does not pay the self-test bar twice. Under `primary` the bullet is unchanged.

A refusal of the precondition is a numbered failure, never an unmet item. An unmet `gates-green`
invites an override, and an override here would land an ungraded merge. The refusal is keyed on
`--prepared`'s exit:
- 1 names `{{LANDER}} --prepare`;
- 2 names `LANDER_MODE`;
- 3 names the observation the lander could not make.

A remote outage at close is therefore reported as an outage, and the run takes the incomplete-landing
route below rather than re-preparing into the same failure.

### `--close` under `in-place`

1. Every Definition-of-Done item evaluates, `gates-green` among them. `gates-green` refuses first
   when the tree is not clean in `git status --porcelain`'s full sense, untracked files included,
   because the bar writes its stamp only then and `--prepare`'s own check (`push-main.sh:71`)
   passes `-uno`.
2. `$LANDER --carry --slug <slug>`, bounded by `run_bounded`. Exit 1 refuses, quoting the list. Exit
   2 refuses as a lander that does not implement the mode. Exit 3 refuses as an observation the
   lander could not make.
3. The LANDING phase and its facts are written.
4. When the stage holds a change to the run-state file, it is committed with the subject in S5,
   bounded, and the commit's own hooks run as for any commit. The subject names the slug and no unit
   id, so `build_commit` never takes it for a unit's build commit. When the stage holds no change,
   which happens on a re-close over a record already LANDING after a re-prepare, no commit is made.
   The verb prints that the close record is already committed, naming the commit that last changed
   the run-state file, and exits 0. That is this unit's own read: the derived-terminal unit's shared
   helper, which reads the same commit, is ordered after this one. The prepared merge the bar just
   graded is then HEAD, and `--land` pushes it.

Under `primary`, step 2 does not run and step 4 stays a stage, exactly as at BASE.

### What an incomplete landing does

The lander's `unreachable` and exhausted-race outcomes are not a reason to merge anywhere. The run
pushes its branch, so the prepared merge and the committed close survive the session, then runs
`--hold --code platform-unavailable --until after <now + 30 minutes> --reaped <recorded id>` with the
lander's last line as the reason, naming the keepalive the close's attestation already reaped. When
that branch push fails because the remote does not answer, the same `--hold` is taken over the
unpublished tip, which the HELD unit accepts for this code alone and records. There is no other
route, and no route merges anywhere. The lander's `red` outcome is a red push-boundary bar; it holds
under the same code only when the red is the bound firing, and is otherwise a fix-and-re-prepare,
because a red the run caused is the run's work.

A `--close` refused because `--prepared` exited 3 takes the same route. The prepared merge is
committed and the close wrote nothing, so the branch push and the hold are all that remain.

### Where the text goes

The protocol stands at 60,324 of its 61,440-byte cap at BASE, 1,116 bytes of headroom, and the
build's declared additions do not sum under that figure. So this unit lands NET ZERO OR NEGATIVE on
that carrier and spends none of the shared headroom: it FUNDS its own growth by trimming. §6 is
rewritten in place, not appended to: the two-anchor paragraph stays for the derived-terminal unit,
and the lander paragraph becomes the four-step sequence. That rewrite's GROSS growth is at most 280
bytes, and anything past that moves to the companion guide.

§8's key table gains one row each for `LANDER_MODE` and `SELFTESTS_OWED_PATHS`, at most 239 bytes
together. The rows are OWED and not optional: check 22 of `tools/unattended/check-unattended.sh`
joins that table against `tools/unattended/.unattended.conf.example` and reds on a key declared in
one and missing from the other, so a unit that ships a key without its row reds the bar. A key-table
row cannot overflow into a companion the way §6's prose can, so the rows are the FIXED half of this
unit's growth and the §6 ceiling is the half that gives way — it is 120 bytes lower here than this
spec carried before the rows were priced.

The passages this unit trims, named precisely so that no sibling unit trims the same text:

- §6's closing rationale paragraph, `tools/unattended/PROTOCOL.template.md:433-435`, opening
  "Listing two anchors without ordering them", 265 bytes. The ordering RULE above it stays where it
  is; the paragraph arguing WHY the order is a rule moves to `UNATTENDED-STOPS.md`, the companion
  this unit's landing text already overflows into, which draws on its own cap.
- §7's second paragraph, `tools/unattended/PROTOCOL.template.md:443-445`, opening "The move was a
  BYTE decision and is recorded as one", 274 bytes. It is the kit's own history of an earlier
  externalisation rather than a rule any run follows, so it moves to `tools/unattended/README.md`,
  the kit README, which carries no size row in `tools/template-size-limits.txt` and owns kit prose.
  Neither moved passage carries a kit-path literal, so the shipped-surface ban does not move either.

That is 539 bytes trimmed against at most 519 added — 280 for §6's rewrite and 239 for the two §8
key-table rows — so the protocol and its template each end this unit's pass no larger than they
began it. AC16 reads both files' sizes at the pass rather than
trusting this arithmetic, and reds if either GREW. No cap is raised here: raising one is an owner
turn, and the other units of this build draw on the same 1,116 bytes, which this unit leaves intact.
The Skill's Close section gains the prepare step above its command,
and its Land section carries both modes, because the Skill is one render shared by every adopter
and the mode is a conf value.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/SKILL.template.md` · `tools/unattended/PROTOCOL.template.md` · the companion guide
template · `tools/unattended/.unattended.conf.example` · `.unattended.conf` ·
`tools/unattended/README.md`, which receives §7's trimmed paragraph · the rendered guides
and Skill.

### Alternatives rejected

- Grading the branch tip and trusting the push boundary to grade the merge. The hook's scoped bar
  would then be the only grader of the merge, and it is scoped by a guard, which is the i28 and i29
  aborts' shape: two green changes that fail together surfacing after the run has closed.
- Re-implementing the carry predicate in the driver. Two spellings of one predicate disagree, and
  the lander is where the landing happens.
- A second full bar at the push (KF2 rules it out); the stamp in the run's git dir makes it
  unnecessary.

## 5. Production-readiness checklist

- security — no new authority: the run still lands only through the lander and the hook, and the
  mandate rules are untouched. The commit at close is the run's own record on the run's own branch.
- perf / scale — one full bar per landing, as F7 rules; the push reuses its stamp. The one extra
  cost is the carry probe, a pair of bounded `rev-list` calls.
- error / empty / loading states — an undeclared mode reads `primary`, announced; a lander that does
  not implement the mode refuses at preflight rather than at landing; a missing prepared merge,
  a foreign carry and a failed commit each refuse with a number and write nothing further.
- observability — `--status` names the mode; the close prints the bar's env, the carry verdict and
  the commit it made; the kit gate's `LANDER_MODE` line and its resolved kit roots.
- risks — until the declared-wall unit lands, the landing bar runs under `GATE_BOUND`, and gov's
  full bar with self-tests may outlast it; the bound's own message then names the kill rather than a
  leg. The derived term `SELFTESTS_OWED_PATHS` can under-declare a kit root; the kit gate reds a
  declared path that resolves to nothing, not one that is missing; AC13 compares gov's own list
  against the kit roots the tree declares.
- testing — driver and kit-gate arms over a scratch repository with a bare remote, each staged RED
  in the pass, and run under attribution at the build's one post-build bar.
- migration — adopters stay `primary` until their own deployer builds adopt the in-place lander.
- user docs — the Skill's Close and Land sections and its `While it runs` bullet, protocol §6 and
  the conf example's two keys.

## 6. Acceptance criteria

- **AC1** — When a fixture branch passes its gate alone and the advertised tip has moved by a commit
  that makes the merged tree fail the same `GATE_CMD`, `--close` under `in-place` reports
  `gates-green` unmet after `--prepare`.
  Red when: the bar grades the bare branch tip, which is green.
- **AC2** — When `--close` runs under `in-place` with HEAD on an unprepared branch tip, it refuses
  with a numbered message naming `--prepare` and writes nothing. With a lander stub whose
  `--prepared` exits 3, it refuses naming the observation failure, not `--prepare`, and writes
  nothing.
  Red when: the missing merge is reported as an unmet item, which an override can then pass; or any
  non-zero `--prepared` exit names `--prepare`, so a remote outage sends the run to re-prepare into
  the same failure.
- **AC3** — When the fixture closes under `in-place` and then lands with `--land`, the push prints
  the hook's `scoped gate` line naming the prepared merge as the full green one commit back.
  Red when: the stamp is written outside the run's git dir, so the hook prints `FULL gate`.
  fixture: a scratch repository with a bare remote, a linked worktree and a two-leg manifest.
  permission: observed by hand in that fixture, per D12-h's method for lander breaks.
- **AC4** — When `bash tools/unattended/check-unattended.sh` grades a Skill render whose Land
  section lacks `--prepare` or `--land`, or names local main as a merge target, it reds; the shipped
  render passes, and the skill-wiring check reds a render that drifted from its template.
  Red when: the arm reads a section the render never emits, so it passes over nothing.
  permission: the staged-break render is the pass's own direct check; the shipped render and the
  skill-wiring check are gate legs, so both are observed at the build's one post-build bar.
- **AC5** — When `--preflight` runs under `in-place` with a lander stub that exits 2 on `--carry`, it
  refuses naming `LANDER_MODE`, and so does a stub that exits 2 on `--prepared`. With a stub exiting
  1 on both, it proceeds. With a stub exiting 3 on either, it refuses naming the observation and not
  `LANDER_MODE`.
  Red when: preflight trusts the declaration, and the first refusal arrives at landing time; or an
  exit of 3 is reported as a mode misdeclaration.
- **AC6** — When the lander stub's `--carry` exits 1 listing a sha, `--close` under `in-place`
  refuses, quotes that sha, and leaves the run-state file unchanged.
  Red when: the carry probe runs after the phase write, leaving a LANDING record that cannot land.
- **AC7** — When `--close` succeeds under `in-place`, `git status --porcelain` is empty, the newest
  commit's subject is `records(<slug>): close — LANDING`, and `build_commit` in
  `tools/unattended/lib-unattended.sh` returns the same commit per unit as before the close.
  Red when: the close stages without committing, which is TOOL-dUnstalledConvoy-24's defect.
- **AC8** — When the lander stub reports `unreachable`, the Skill's documented next act is a branch
  push and a `--hold` under `platform-unavailable` that passes `--reaped`. That includes the case
  where the branch push fails. The rendered Skill documents the same next act for a `--close`
  refused because `--prepared` exited 3. No rendered sentence in the Land section directs a merge
  into local main. The rendered `While it runs` bullet names `--close` as where an `in-place` run's
  `GATE_SELFTESTS=1` bar runs.
  Red when: the fallback text survives from the primary path, which lands through local main; or
  the Land section gives a failed branch push no next act; or the Land section's `--hold` omits
  `--reaped`, so the HELD unit refuses the run at its only ending; or a close refused on the
  lander's observation failure has no documented next act, so S6's route exists only in this spec;
  or that bullet still sends an `in-place` run's main loop to run the `GATE_SELFTESTS=1` bar by hand
  at `VERIFYING`, so kit work pays the self-test bar twice.
- **AC9** — When `LANDER_MODE` is blank, `--close` and `gates-green` over the fixture produce the
  BASE driver's output and exit, including no commit and no carry probe.
  Red when: an in-place branch runs in primary mode.
- **AC10** — When the landing range touches a path under a declared `SELFTESTS_OWED_PATHS` entry, a
  fixture `GATE_CMD` that prints its environment shows `GATE_SELFTESTS=1`; when it touches none, it
  does not; and in both cases it shows `GATE_FULL=1`.
  Red when: the term is exported unconditionally or never; or `GATE_FULL=1` is not exported, so
  gov's guarded manifest grades the landing merge by guard, which is the i28 and i29 shape.
- **AC11** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs at the
  build's one post-build bar, its attribution summary reads `verdict clean`: no NEW FAIL, no `DEAD PROBE at L` and
  no `OVER BUDGET at L`. Every suite it reports with INHERITED lines or `DEAD PROBE at R` is named by
  its file path in a filed backlog row or ask that is not CLOSED, as
  `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'` shows.
  Red when: an arm this unit added fails, or an existing arm newly fails because of it; or the run is
  read by its NEW count alone, so a suite this unit's change aborted before its first FAIL line, or
  pushed past its budget, reads as clean; or an inherited failure is attributed away with no record
  filing it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: the run drives the unattended self-test suites, which `memory/guides/BUILD-METHOD.md`
  M6 keeps out of a unit pass, so it is the run the main loop makes at VERIFYING, after the
  last unit: the attributed `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>`
  made beside that run's `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, which
  carries no leg for these suites at any flag setting. This folds the conservative reading of
  the parked ruling conflict and decides nothing.
- **AC12** — When `--close` runs under `in-place` over a prepared merge with one untracked file in
  the tree, `gates-green` refuses with a numbered message naming the stamp precondition, and no bar
  runs.
  Red when: the only cleanliness test is `--prepare`'s `-uno` check, so the bar runs GREEN and
  writes no stamp, and the push then pays a second full bar or scopes against an older stamp.
- **AC13** — When `bash tools/unattended/check-unattended.sh` runs on the real tree after this unit,
  it prints `LANDER_MODE in-place` as declared, and prints a non-empty list of
  `SELFTESTS_OWED_PATHS` entries, each resolving to a tracked path. Two populations are compared
  against that list:
  - the directory of every file `git ls-files 'tools/*/kit.toml'` lists;
  - every path `git grep -h '^sentinel = ' -- 'tools/govkit/entries/*.kit.toml'` names.

  Each member of both starts with some printed entry.
  Red when: gov's conf leaves `LANDER_MODE` blank, so the in-place path ships inert in the one
  repository that dogfoods it while every fixture criterion stays green; or the key is blank or
  misses a kit root, so an in-place landing of kit work runs without `GATE_SELFTESTS=1`, the kit DoD
  `AGENTS.md` states.
  permission: the leg runs over the real tree rather than a fixture, so it is observed at the
  build's one post-build bar.
- **AC14** — When `grep -c 'verb here commits' tools/unattended/PROTOCOL.template.md` runs, it
  prints 0 (1 at BASE, where the premise wraps after `because no`), and so does
  `grep -c 'NO driver verb commits' tools/unattended/unattended.sh`; the rotation paragraph still
  names a shared witness as the reason.
  Red when: the shipped protocol keeps a premise the committing close falsifies in gov's own mode.
- **AC15** — The fixture closes under `in-place`, the lander stub's push reports `red`, the fixture
  commits a fix and re-runs `--prepare`, and `--close` then runs again over the LANDING record. The
  second close exits 0 and names the existing close commit. `git rev-parse HEAD` equals the
  re-prepared merge, and `git status --porcelain` is empty.
  Red when: step 4 commits unconditionally, so the re-close refuses on an empty commit after
  `gates-green` has already paid a full bar, and both documented re-prepare paths wedge.
- **AC16** — When `git cat-file -s` reads `memory/guides/UNATTENDED-PROTOCOL.md` at this unit's
  build commit and at that commit's first parent, the build-commit size is NOT GREATER than the
  parent's and is below the 61440-byte guide cap declared in
  `tools/memory-tree/check-memory-hygiene.sh`. The same two readings hold for
  `tools/unattended/PROTOCOL.template.md`. Both trims are taken and both landed:
  `grep -c 'Listing two anchors' tools/unattended/PROTOCOL.template.md` and
  `grep -c 'The move was a BYTE decision' tools/unattended/PROTOCOL.template.md` each count 1 at the
  parent and 0 at the build commit, the first paragraph's text is present in `UNATTENDED-STOPS.md`
  and the second's in `tools/unattended/README.md`. Both owed key-table rows arrived:
  `grep -c 'LANDER_MODE' tools/unattended/PROTOCOL.template.md` and
  `grep -c 'SELFTESTS_OWED_PATHS' tools/unattended/PROTOCOL.template.md` each count 0 at the parent
  and 1 or more at the build commit. The companion guide `UNATTENDED-STOPS.md`, which receives the
  first trimmed paragraph and this unit's landing overflow, is read the same way at the build commit
  and is below the same 61440-byte guide cap.
  Red when: §6 is appended to rather than rewritten in place, so the paragraph this unit replaces
  survives beside its successor and one unit spends the 1,116 bytes the build's units share; or the
  size is read against the figure written in this spec rather than against the parent commit, so a
  sibling's landing hides this unit's overspend; or the trim is taken and the text lands in no
  destination, which DELETES a rule's reasoning rather than moving it; or the cap is raised to make
  the edit fit, which is an owner turn and not this unit's; or a conf key this unit declares in
  `tools/unattended/.unattended.conf.example` reaches §8's key table in no row, which reds check 22
  of `tools/unattended/check-unattended.sh` on the next bar; or the companion is measured only in prose, so text pushed out of the
  protocol lands in a carrier nobody reads the size of.
  permission: a read, a byte count and four greps, no gate leg and no suite.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `pass-order history` · `memory hygiene` · `kit version markers` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a fixture branch green alone and red once merged onto a moved tip, and a lander stub whose carry probe exits 1 · the driver suite's executed-assertion floor
New arm: `tools/unattended/check-unattended.test.sh` · a Skill render missing `--prepare`, and an invalid `LANDER_MODE` · the leg suite's executed-assertion floor

## 8. Open questions

- **F1 — how does the driver know the DoD owes the self-tests?** Options: always export
  `GATE_SELFTESTS=1`; never; derive it from the landing range against a declared path list. The
  first charges every records-only landing a self-test bar; the second lands kit work unverified.
  RESOLVED (agent, 2026-09-14, delegated): derive it, over `SELFTESTS_OWED_PATHS`.
- **F2 — the design's criterion that a Skill missing either flag reds check 26.** Check 26 grades
  the driver's verbs, not a lander's flags, and the unit that teaches it flags is sequenced after
  this one, so the criterion would rest on work this unit does not build.
  RESOLVED (agent, 2026-09-14, delegated): this unit adds its own kit-gate arm for the Land section
  (AC4) and does not cite check 26.
- **F3 — order against the HELD unit.** This unit consumes that unit's refusals and verb, while the
  brief's roster numbers put it first; the §3 order join refuses a consumer ordered before its
  producer. RESOLVED (agent, 2026-09-14, delegated): this unit takes `order 4`, the HELD unit
  `order 3`; no other edge in the roster involves either value.
- **F4 — the landing shape and the charter exception.** RESOLVED (owner, 2026-09-13): D12-i1 in
  place; D12-i3 keeps the charter's attended rule and puts the unattended exception's rule in the
  protocol.
- **F5 — what does a re-close after a re-prepare do?** Options:
  - (a) commit only a non-empty stage, and otherwise report the existing close commit and exit 0;
  - (b) state that a re-prepared landing skips `--close` and goes straight to `--land`.

  (b) lands a re-prepared merge that no `gates-green` graded, which is the ungraded merge this unit
  exists to prevent. RESOLVED (agent, 2026-09-16, delegated): (a).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Takes `order 4` rather than the roster's 3 (F3). Adds one edge
  the brief's table does not list, consumes-from unit 1, inside this spec's own group. Replaces the
  design's check-26 criterion with its own arm (F2).
- rev-2 · 2026-09-14 · §2 S1 S2 S3 S5 S6 · §3 · §4 · §5 · §6 AC5 AC8 AC10 AC12 AC13 AC14 · §10 ·
  round-1 spec-audit fold (G1 M1, M11, M13, M15, M21, M22, L3, L4). An incomplete landing whose
  branch push also fails holds over the unpublished tip under `platform-unavailable`; this relaxes
  design §21.7's push-before-HELD rule for that code alone, as the HELD unit's F7 records.
  `gates-green` asks the lander's `--prepared` rather than re-deriving the merge, and refuses a tree
  that is not porcelain-clean before the bar (AC12). AC10 also asserts `GATE_FULL=1`. AC13 reads
  gov's own `LANDER_MODE` and kit roots on the real tree. Lander exits 2 and 3 are mapped apart. S5
  retires the protocol's 'no verb here commits' premise (AC14); AC14's protocol grep keys on the
  premise's unwrapped half, because the full phrase wraps at BASE and would print 0 before any edit.
  S6 names AC8, which observes its new unpublished-tip clause. The kit version marker leaves Files
  touched, because the build's one move is the held-suite baseline unit's.
- rev-3 · 2026-09-16 · spec-audit round 2 fold.
  - G1 M9 (43): §4 step 4 commits only a non-empty stage, and a re-close after a re-prepare reports
    the existing close commit (S5, F5, AC15). Fold verification: step 4 names that commit as the one
    that last changed the run-state file, not through the derived-terminal unit's helper, which is
    ordered after this unit.
  - G1 M13 (11): AC13 requires a non-empty `SELFTESTS_OWED_PATHS` covering every `kit.toml`
    directory and govkit sentinel. S1 prints an empty list, and §5 is updated.
  - G1 L1 (18, 37): S2 probes `--prepared` too. S3 and §4 map `--prepared`'s exits 1, 2 and 3 as
    `--carry`'s are mapped, and an observation failure at close takes the incomplete-landing route
    (S6, AC2, AC5). Fold verification: AC8 also observes that route in the rendered Skill, since
    S6 names AC8 and no other criterion read it.
  - G1 L3 (36): the route and the Land section pass `--reaped` (S6, AC8).
  - G1 H1 (2, 24): AC11 reads `verdict clean` and the inherited-suite filing, and the §3
    consumes-from edge to unit 1 is updated.
  - G5 round-2 H1 (21, 36, 52), unit-3 end: §3 hands-off 34 names the in-place sequence the
    switch-over's landing reconcile runs before `--prepare`.
- rev-4 · 2026-09-16 · regrounded on fb07ca25 (origin/main). Line citations moved with the landed
  code: S3's stamp condition to `run-gates.sh:1861-1863`, and §4's to `:1861`, after
  aRatifiedRulings added the no-ceiling kill branch; S5's driver comment to `unattended.sh:1680-1681`
  and its test comment to `unattended.test.sh:2484`. §4 Where the text goes reads the protocol at
  60,324 bytes, after fact 13, three conf rows and a longer cutoff row landed, and bounds this
  unit's growth by what HELD's rows leave. aDeferredBar's Skill bullet has the main loop run the
  `GATE_SELFTESTS=1` bar by hand at `VERIFYING` for kit work, so S6, §4 `gates-green`, §5 user docs
  and AC8 name `--close` for that bar under `in-place`. AC11's unit-end suite run meets
  aDeferredBar's M6 rule and `gate-guard.js` refusal before `VERIFYING`, which contradicts owner
  rulings D12-h and D12-i8; that is reported to the orchestrator, and AC11 is unchanged. §10
  describes the new base.
  Extended 2026-09-20, regrounding consolidation, folding the conservative reading of that parked
  conflict and not deciding it. AC11 now reads the attributed run at the build's one post-build
  bar, the run the main loop makes at VERIFYING after the last unit, and S8, the §3 consumes-from
  edge and §5 testing follow it; AC4 and AC13 gain `permission:` lines separating the pass's
  staged-break checks from the leg runs over the real tree. §4 states the 400-byte MAXIMUM this
  unit adds to the protocol and new AC16 reads the file's size at the pass against the 61440-byte
  guide cap; no cap is raised. Re-priced to NET ZERO on the same date, on the orchestrator's
  ruling that a unit adding bytes to a capped carrier funds them itself: §4 now names the two
  passages this unit trims — §6's closing rationale paragraph, 265 bytes, to `UNATTENDED-STOPS.md`,
  and §7's second paragraph, 274 bytes, to `tools/unattended/README.md` — and AC16 reds if either
  carrier grew against this unit's parent commit rather than allowing 400 bytes of growth.
  Both §7 `New arm:` lines name their suite's executed-assertion
  floor instead of `none`, because `tools/unattended/unattended.test.sh` and
  `tools/unattended/check-unattended.test.sh` each pin one. AC14's two greps were re-run at
  fb07ca25 and count 1 each, so neither is a could-not-fail phrase.
  Extended again on 2026-09-20, closing pass. The orchestrator ruled that a unit declaring a conf
  key owes that key a §8 key-table row, because check 22 reds without one, so §4 now prices the
  `LANDER_MODE` and `SELFTESTS_OWED_PATHS` rows at 239 bytes inside the same 539-byte trim and drops
  §6's rewrite ceiling from 400 to 280 to pay for them — a key-table row cannot overflow into the
  companion guide and §6's prose can. AC16 witnesses both rows arriving and reds on a declared key
  that reaches no row, and reads the companion guide's own size at the pass, which is what a
  carrier with more than 2048 bytes free owes under the same ruling. The orchestrator also ratified
  Rule 1's narrow reading, under which a gate
  leg's command over a FIXTURE or a staged break stays in the unit pass and the same command over
  the real or rendered tree defers, so AC3's and AC4's lines stand as written and nothing moved.
  Closing verifier, same pass and rev: the `permission:` line of the criterion that reads the
  attributed run now names that run in the orchestrator's own terms, because
  `tools/gate-legs.json` carries no leg for `tools/unattended/unattended.test.sh` or
  `tools/unattended/check-unattended.test.sh` at any flag setting, so "the build's one
  post-build bar" alone would have read as a bar that covers them.

## 10. Reuse audit

- The seams are the driver's `gates-green` item and its `run_bounded` wrapper, the close path's
  existing write gate, and the lander's own `--carry`, which exists so this unit asks rather than
  re-derives. The Skill's `{{LANDER}}` token is reused for all three lander calls, so
  `landed-via-lander` keeps grading the same spelling. The probe `reuse_lookup.py "land a merge onto
  the remote default branch tip and push it"` returned name-stem matches only, and its coverage line
  reads `unscanned layers: .sh`; the driver, the lander and the hook are all shell, so the lookup is
  blind here and the seams were found by reading `tools/unattended/unattended.sh` at BASE. Recall
  returned TOOL-dUnstalledConvoy-38 and TOOL-aPacedTurnstile-15 beside the aHoistedPass landing
  record. Where the design record and the source disagree: its line citations for `gates-green` sit
  within a few lines of BASE's, and its check-26 criterion names a check that grades verbs (F2).
  The DECISIONS clause of TOOL-dClosedLexicon-11, 'no verb here commits', is superseded for
  `in-place`. The archive name's derivation is unchanged.
- BASE is `fb07ca25`, the origin/main tip this branch merged; the spec was written at `abac6d59`.
  The lander and the pre-push hook are byte-identical between the two, `gates-green` still runs
  `$GATE_CMD` through `run_bounded` inside `--close`, TOOL-dUnstalledConvoy-24 is still OPEN, and
  AC14's two greps still print 1 each. Nothing on main adds `LANDER_MODE`, `SELFTESTS_OWED_PATHS` or
  a committing close. What moved: the driver grew by 280 lines (aDeferredBar's `run-branch` fact,
  aProbedUnit's `--audit` and bound keys), so the cited driver and test lines moved; the
  protocol render is 60,324 bytes; the Skill gained the `While it runs` bullet this unit qualifies,
  the `--audit` keepalive tick and the resume kickoff step, none of which touches the Close or Land
  sections. `tools/unattended/gate-guard.js` denies `run-unattended-gates.sh` at command position
  while the branch's run record is before `VERIFYING`, which reached AC11's run at the unit's end
  before the 2026-09-20 consolidation moved it to the build's one post-build bar;
  the driver's own `GATE_FULL=1` export inside `--close` is not a tool-call command and is not
  seen by the hook.
- M12 was not reached: the owner ratified the mechanism and the lab measured it.
- Recall terms used: `push-main lander in-place landing merge remote-tip carry-set foreign-commit
  pre-push marker full-green-stamp reconcile local-main`
