# DEPL-aTetheredConvoy-4 — the gate-runner declaration, end to end

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 0f0a121d · streams deployer+tooling

## 1. Goal

Build the gate-runner declaration and every consumer of it in one unit: the target-side table, the
writer that produces it, the baseline read that opens `apply`'s hard order, the three-valued state
machine, the two policy knobs that have been written and never read, the hook probe, the leg emitter
that closes the hard order, the CI writer, and the observer that proves an emitted leg EXECUTES. The
declaration is measurably absent — it appears in no shipped file of any kind — and splitting it from
its consumers is what produced two incompatible spellings of it inside one design pass.

## 2. Scope (IN)

- **S1 — the `[gate_runner]` table, ONE vocabulary, owned here.** `kind` is `manifest` or `none`.
  `file`, `grammar` (`json-array`), `dedupe_key` (`name`), `command` (an argv ARRAY, never a shell
  string), `observed_ran`, `observed_failed` and optional `observed_skipped` (literal templates
  carrying the leg name). Plus `[gate_runner.ci]` with `system` (`github-actions`), `file` and `job`.
  `make`, `npm` and `shell` are REFUSED BY NAME with a backlog pointer. `anchor` is refused: it is
  meaningful only for a line grammar this unit does not implement, and a key that parses and is
  ignored looks exactly like one that works.
- **S2 — `intake` writes it and refuses to invent it.** A partial promotion refuses naming the
  missing key. An ABSENT table in a pre-existing descriptor is treated as `none` but prints a
  DIFFERENT line, so "declared none" and "never declared" are two observable states.
- **S3 — the baseline read, twice, under ONE guard regime.** One function parses the runner's output
  into a leg-name-to-verdict map; it runs once before any write and once after the emitter, BOTH with
  the runner's run-everything escape set, because a guarded-unchanged leg scored in one read and not
  the other makes the two maps incomparable.
- **S4 — the three-valued table falls out rather than being declared.** `absent` is "a name in the
  after-map that was not in the before-map". §4 carries the (before, after) decision table and states
  exactly when `apply` FAILS.
- **S5 — the baseline executes target-authored code, and says so before it does.** The command comes
  out of a file committed in the target repo, so anyone with commit access there chooses what runs on
  the operator's machine. `apply` prints the exact argv and the descriptor commit it came from and
  requires confirmation on the first apply, recording the approved argv and that commit in the
  receipt; it re-confirms when either changes. `--no-baseline` exists and records the baseline as
  `declined` — a value that is never green and that no exemption honours, so it mutes nothing.
- **S6 — the two policy knobs get their first readers.** The pre-existing-red knob governs ONLY the
  before-red rows; letting it touch the absent rows turns it into a global mute. The hook knob's
  probe runs the target's own hook without creating a commit, and records a three-valued result
  because "no hook" and "hook refused" share an exit code.
- **S7 — `red_after_land` as a WINDOW, both consumers scoped.** Exempt between land and configure,
  and asserted GREEN after configure. Either consumer alone is the permanent-exemption regression the
  contract already records shipping once.
- **S8 — the leg emitter**, as the last step of the hard order: guards RENDERED against the target's
  prefix and memory root, a dropped guard recorded with its reason, a leg whose guard set empties
  emitted with the guard key OMITTED rather than empty, and idempotency by the declared dedupe key.
- **S9 — the emission's ownership record is written BEFORE the write it authorizes.** An intent
  record naming the legs about to be written, promoted to owned after. A crash between the write and
  the receipt otherwise leaves gov's rows in the target with no receipt claiming them, and the next
  `apply` refuses forever.
- **S10 — a leg row the target EDITED is drift, not something to overwrite.** Ownership of the NAME
  is not ownership of the ROW: before replacing, compare against the argv and guard the receipt
  recorded; a difference reports drift and refuses the replacement.
- **S11 — the CI writer, write-once.** A workflow that does not exist is created from a template
  whose checkout carries full history iff any emitted leg declares it; a workflow that DOES exist is
  never edited — there is no YAML parser in the standard library and none anywhere in this repo — and
  an order is written instead. Full history is DERIVED from the emitted legs and only ASSERTED
  against any declaration.
- **S12 — `check --observe`.** Runs the declared command once and asserts each owned leg matched an
  `observed_ran` template; a leg matching `observed_failed` REDS, and one matching
  `observed_skipped` reds as WIRED BUT SKIPPED. Default `check` reports presence and says in its own
  message that presence is not execution.
- **S13 — six of unit 1's nine step ids are filled here**, and none is renamed.

## 3. Non-goals (OUT)

- **Gate-runner grammars beyond one.** Refusing three by name and doing one well beats half-writing
  four: a splice into a Makefile or a package manifest that half-works ships a target a leg that never
  runs while the deployer exits 0, which is the silent-green direction. Each refusal names a backlog
  row.
- **Editing an existing CI workflow.** S11's write-once rule, with its reason.
- **Creating a gate runner a target does not have.** Gov's own runner is a registry exemption because
  it sources a permanently exempt directory and exits with zero legs run without it. `kind = "none"`
  emits an order; it never manufactures a runner and never prints a reassuring line and moves on.
- **Rolling back a half-applied install.** `apply` has no rollback; S9 makes the half-applied state
  RECOVERABLE rather than fatal, which is a different and smaller claim. Inventing a rollback here is
  a separate unit.
- **The `[[outcome]]` evaluator.** Unit 5 owns it. This unit's fixtures assert messages and on-disk
  effects, never an adopter's bare exit code.
- **A second guard taxonomy.** `selfcheck`'s existing five-class table grades GOV's own manifest and
  is where the gov-layout drop lives; this unit's renderer grades the descriptors' token-spelled
  guards. They answer different questions about the same word, and §4 says so plainly rather than
  leaving a future reader to look for a class table in the emitter and find none.

**Assumes:** units 1 (step ids, receipt schema, check-state vocabulary), 2 (the `gate-leg` and `ci`
receipt rows this unit fills are refused by name until then) and 3 (the leg correspondence that forces
the two descriptors gaining a leg here to have been claimed).

## 4. Design

### The declaration is absent, and both its halves are new

Measured: the table name appears in zero shipped files of any type. `intake` writes six things and
none of them is it; the loader's only consumers read the install prefix and the answer set. So the
writer and the reader are both new code, and every consumer below hangs off them — which is precisely
why they are one unit. Specced apart, two designs produced two different value vocabularies for
`kind` and two different mechanisms for reading a runner's output, in the same artifact, with nothing
asserting they agree.

### The baseline, and the liveness half that is not the obvious one

The natural liveness half for the before-read is "refuse when the map is empty". That is the wrong
one. Measured on gov's own manifest, most legs carry a guard and a guarded-unchanged leg is marked
skipped before dispatch — so a target whose install touches paths none of its guards name produces a
before-map that is FULL of skipped entries and carries zero green/red information, while an
emptiness check passes. Every after-leg then lands in the `absent` row, which is the row that carries
both exemptions, so a broken or degenerate read silently reroutes the whole install into its most
forgiving branch.

The liveness half is therefore: refuse when the before-map contains zero legs in green-or-red. A map
that is entirely skipped is a DEAD PROBE, which is the doctrine this repo's drift audit already
applies to a signal that cannot move. Both reads run with the run-everything escape set, and the
doubled wall clock is priced in §5 rather than avoided by scoring the two reads differently.

### The state machine

B is the before-map, A the after-map, keys their union.

| B | A | `apply` |
|---|---|---|
| green | green | pass |
| green | red | FAIL, naming the leg: green before this install, red after |
| green | skipped | FAIL: green before and did not execute after — the install broke its guard |
| green | absent from A | FAIL: a leg that vanished is not a leg that passed |
| red | anything | REPORTED, never fatal — the pre-existing-red knob already decided at step 1 |
| skipped | anything | `unmeasured`; never green, fails nothing on its own |
| absent from B | green | pass |
| absent from B | red | FAIL naming the leg, UNLESS exempt |
| absent from B | skipped | FAIL if this run EMITTED that leg; else `unmeasured` |

Exempt means: this kit has a hole declaring it blocks a gate AND that hole's discharge probe exits
non-zero RIGHT NOW; or the leg declares the post-land window AND this run skipped that kit's configure
phase. Nothing else exempts.

The exemption is granted by RUNNING the probe, never by reading the flag. The measured defect next
door is exactly that: the blocking-adopt flag is read statically, so a kit is reported inert while its
own hole's probe exits 0 in the landed tree — two spellings of one fact with nothing asserting they
agree, inside the engine built to close that class.

### The window, and why one consumer is not enough

Consumer one is the absent-row exemption above, conjoined with the set of kits whose configure THIS
RUN skipped — a set `apply` builds during the run rather than re-deriving from a flag later, so on a
resume where configure DID run the set is empty, the window is closed, and the leg must be green.
Consumer two is the positive assertion after configure. The contract records that shipping only the
first turned the flag into a permanent exemption under which an all-kits install could land a kit with
both legs red forever and every criterion pass.

### The hook probe, and the flag it refuses

Measured: git's own hook-run subcommand executes the target's hook under its configured hooks path and
creates no commit, but exits non-zero BOTH when the hook refuses and when no hook exists. So the probe
is two steps — resolve the hook path and test existence, then run — and records `no-hook`, `pass`,
`block` with the hook's own output, or `unsupported` on a git too old to have the subcommand. The
ignore-missing flag is REFUSED: it maps missing onto the same exit code as pass, trading a visible
collision for the dangerous one.

### The emitter

Guards are rendered by the existing token substituter — the one whose negative lookbehind was bought
by a failing arm — against the existing target context, which already supplies the install prefix, the
kit path and the memory root. Measured across every shipped leg, every non-empty guard is ALREADY
token-spelled, so rendering is substitution plus a drop test.

The drop test is TRACKED-NESS, not existence, and it runs AFTER the stage step. The runner's own
predicate is a diff over a pathspec, and a pathspec matching nothing diffs clean and exits 0 — so a
guard naming a path that exists but is untracked is kept by an existence test and skips its leg
forever, printing a reassuring line. Measured: at least one adopter's output is left untracked by a
full apply today, which is exactly that state.

A dropped guard whose pathspec is a DESTINATION the same entry declares is a FINDING, not a silent
drop. Measured, one shipped leg guards on a rendered artifact's destination, and rendered artifacts
are produced by adopters — so the leg would be emitted guarded only on its kit directory and would go
blind to the file it exists to compare. Gov knows that path is supposed to exist; dropping it quietly
is the deployed-leg-vacuously-green failure arriving through the mechanism written to prevent it.

An unresolved token in a GUARD drops that pathspec; an unresolved token in an ARGV refuses. The
asymmetry is deliberate: a dropped guard costs an unnecessary run and never a silent skip, while a
leg wired to an unresolved token is broken forever.

The runner file is rewritten with the same serializer settings the shipped structural merger uses,
non-ASCII preserved, through a single shared helper so the two writers cannot diverge — measured, the
obvious spelling escapes non-ASCII and would mutate a target's own leg names on first apply.

### Observation, and the template that must not be one key

An emitted leg's execution is proved by a declared literal template carrying the leg name, because
for gov's runner the strings are measured and for any other runner they are unknowable to gov.
`observed_ran` and `observed_failed` are SEPARATE keys: folding the failure template into the
execution template makes the only product-side observation exit 0 when every emitted leg failed.
Matching is anchored to a whole line, because an unanchored substring is satisfied by a target's own
longer line and by the indented per-leg output a failing runner prints.

### Rollout

1. **S1, S2 and the pre-write validation** — the declaration, its writer, and the refusals, validated
   in the existing pre-write refusal pass so a bad declaration cannot refuse after everything landed.
2. **S3–S7** — the baseline, the state machine, the policy knobs, the hook probe, the window.
3. **S8–S11** — the emitter, the intent record, the drift refusal, the CI writer.
4. **S12, S13** — the observer and the step ids.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Core | `tools/govkit/govkit.py` | the largest diff of the build |
| Descriptors | the two entries gaining a `[[gate_leg]]` | unit 3's correspondence names them |
| Tests | `tools/govkit/selftest.py` | the fixtures carry a real runner |
| Docs | `skills/deploy-governance/SKILL.md`, `WIRE-INTO-PROJECT.md` | the baseline executes target code; say it in the operator-facing text |
| Map | `memory/map/features/govkit.md` | the emitter and observer seams |

### Alternatives rejected

**Split the baseline from the emitter.** Rejected on measurement: specced apart in one pass, the two
halves produced incompatible vocabularies for `kind` and two independent readers of one runner's
output, in the one artifact both read.

**Let the operator declare full history.** Rejected: deriving it AND letting it be declared is the
two-spellings class. Derive and assert, which is the shape the shipped derived-flag arm already uses.

**Rewrite argv0 to the target's interpreter.** Rejected: gov's runner remaps the launcher name and a
target's may not, but rewriting it is gov guessing the target's interpreter policy. Recorded in the
outbox and the receipt instead.

## 5. Production-readiness checklist

- security — this unit EXECUTES target-authored code, twice per apply plus the hook, and that is the
  sharpest thing in the build. S5's confirmation, its recorded approval and its non-muting decline are
  the controls; the operator-facing docs carry it, not a postmortem.
- perf / scale — the target's full bar runs twice per apply. That is the price of the criterion; the
  decline flag is the escape and it is never green.
- a11y — N/A: a command-line tool.
- i18n — N/A for the interface; NOT N/A for the data — the runner-file serializer preserves non-ASCII
  in a target's own leg names.
- error / empty / loading states — the three-valued verdict, the four-valued hook result and the three
  mutually exclusive emission lines are this line.
- observability — the receipt's baseline, after, emission and ownership records; the observer verb.
- risks — the crash window between emission and receipt, closed by S9's intent record; a target's
  edited leg row, closed by S10; the write-once workflow going stale, which the observer reports and
  nothing repairs; and the fixture proving the observation strings against gov's runner only, so the
  grammar's portability rests on the declaration rather than a measurement.
- testing + left-shift gates — every arm asserts a message or an on-disk effect; the observation arms
  pin the runner's base refs so guards are genuinely live, and carry a control leg, because a runner
  that exited with zero legs run would make every absence assertion pass vacuously.
- migration / rollback — a descriptor with no table is `none` and prints its own line; nothing is
  rewritten.
- user docs — the Skill and the runbook both gain the code-execution disclosure.

## 6. Acceptance criteria

- **AC1** When `python tools/govkit/govkit.py intake --target <fixture>` runs without the gate-runner
  answers, it writes `kind = "none"` with its comment; with a partial promotion it REFUSES naming the
  missing key; and a pre-existing descriptor with no table makes `apply` print a line distinct from
  the declared-none line, asserted separately.
- **AC2** When `apply` runs against a fixture whose declared command is a real runner over a
  throwaway leg manifest, `.governance/install.json` records a baseline map containing exactly that
  manifest's leg names with their verdicts. Liveness: a sibling fixture whose templates match no line
  makes `apply` exit 2 saying the read matched no leg.
- **AC3** When the before-map contains zero legs in green-or-red, `apply` refuses calling it a DEAD
  PROBE — asserted with a fixture whose guards are all unchanged, which is the state an emptiness
  check passes.
- **AC4** When a fixture leg is green at baseline and red after the install, `apply` exits non-zero
  and names it. Liveness: the same fixture left green exits 0 AND the arm asserts the leg name was
  present in the recorded baseline — a pass that never saw the leg is not a pass.
- **AC5** When a fixture leg is red before the install, `apply` exits 0, records the verdict red, and
  says pre-existing. Liveness: flipping the knob to refuse exits 2 AND leaves
  `.governance/install.json` ABSENT — the on-disk half proves it refused before writing.
- **AC6** When an emitted leg is red after the install, `apply` fails naming it; with an undischarged
  gate-blocking hole it does not. Liveness: discharge that hole in the same fixture, re-run
  `apply --resume`, and the leg now FAILS — the exemption must be observed CLOSING.
- **AC7** When a kit's configure was skipped by a blocking hole, a red post-land-window leg does not
  fail the install; after `apply --resume` configures the kit, a still-red leg DOES. Both halves in one
  fixture — that pair IS the window.
- **AC8** When `apply` runs against a fixture with a refusing pre-commit hook, the install COMPLETES,
  the receipt exists, and an order carries the hook's own output. Liveness: the same fixture with NO
  hook records `no-hook`, asserted on the recorded STRING — measured, both cases exit non-zero from
  the probe.
- **AC9** When the baseline command or its source commit differs from the approved one recorded in
  the receipt, `apply` re-prompts before running it; with `--no-baseline` the run records `declined`
  and no exemption honours that value, asserted by an absent-row red leg still failing the install.
- **AC10** When `apply` emits a leg into a fixture's runner and that runner is then run, the rendered
  `observed_ran` template for that leg appears in its output. Liveness, three halves: the same command
  before `apply` does not contain it; a pre-existing control leg is observed in BOTH runs; and the
  assertion is on the string, never the exit code.
- **AC11** When a guard renders to a path that exists but is UNTRACKED in the target, it is DROPPED
  and the leg is emitted with no `guard` key at all — asserted as key absence, not an empty list — and
  the leg is then observed executing. Liveness: a counterfactual leg carrying the unrendered guard is
  observed SKIPPED at exit 0, reproducing the silent-green this prevents.
- **AC12** When a dropped guard's pathspec is a destination the same entry declares, `apply` reports
  a FINDING naming the leg and the destination rather than dropping it quietly.
- **AC13** When `prefix` and `memory_root` are non-default, every emitted guard renders under
  them and no emitted string in the runner file contains a brace.
- **AC14** When `apply` runs twice, the runner file is BYTE-IDENTICAL and the row count unchanged.
  Liveness: the first apply strictly INCREASED the row count over the seed manifest — otherwise
  byte-identical is satisfied by an emitter that does nothing. A target leg name carrying non-ASCII
  survives both runs unescaped.
- **AC15** When a runner row's name collides with an emitted leg and the receipt does not claim it,
  `apply` exits non-zero naming the leg and the file, and the runner file is byte-identical
  afterwards. When the receipt DOES claim it but its recorded argv or guard differ from the row on
  disk, `apply` reports drift and refuses the replacement.
- **AC16** When `apply` is killed between the runner write and the receipt write, the NEXT `apply`
  recovers rather than refusing — asserted with an env-gated abort — and `check` on that half-written
  target does not report it NOT LANDED.
- **AC17** When a selection contains a `history_depth = "full"` leg, the created workflow's checkout carries the
  full-history setting; a selection with none produces a workflow without it; and a declaration
  contradicting the derived value REFUSES naming the leg that decided it.
- **AC18** When a workflow already exists, `apply` writes an order naming the job and the setting and
  the existing file is byte-identical afterwards — asserted on the bytes, not the message.
- **AC19** When `kind = "none"` and when the table is ABSENT, both write an order containing the
  specific leg name and its rendered argv, and `apply` prints DIFFERENT lines for the two, asserted
  separately.
- **AC20** When `python tools/govkit/govkit.py check --observe --target <fixture>` runs, it exits
  non-zero naming any owned leg that matched an `observed_failed` or `observed_skipped` template, and
  0 only when every owned leg matched `observed_ran`. Liveness: a fixture where every emitted leg
  fails exits non-zero and names each — the arm that a single combined template would pass.
- **AC21** When each refused value is supplied — the three refused kinds, a wrong grammar, a wrong
  dedupe key, a present anchor, a wrong CI system, a full-history value outside its vocabulary — the
  message carries the offending VALUE and `.governance/install.json` was not created. Liveness: the
  supported values exit 0 and write the runner file.
- **AC22** When `plan` and `apply` run over one fixture and selection, the gate-leg and CI
  destinations `plan` prints equal the set `apply` records — asserted as SETS from both runs, through
  unit 1's single expansion.

## 7. Gates

`bash tools/run-gates.sh` green at the push boundary; `GATE_FULL=1` for the DoD. No new leg: every arm
rides `govkit selftest`, and unit 3's deployability leg grades the emitter against every entry.

Unit 3's leg correspondence reds until the two descriptors gaining a `[[gate_leg]]` here have theirs,
which is the ratchet working as designed.

The kit version constant moves.

Before review: `python tools/memory-tree/gotchas.py --for-diff 0f0a121d..HEAD`. `subprocess-resolves-a-
different-shell` is live — this unit launches a target's runner and git's hook subcommand from Python.

## 8. Open questions

- **F1 — does the first-apply baseline confirmation block an unattended install?**
  RECOMMENDATION: the committed target descriptor IS the approval, and `apply` records the argv and
  the descriptor commit it approved; a CHANGE to either re-prompts, and an unattended run with a
  changed command refuses rather than prompting. That keeps the standing-authorization property the
  descriptor exists for while making a silent change to what runs on the operator's machine impossible.
  Owner call, because it is a security posture rather than a mechanism.
- **F2 — should `check --observe` be the default?** RECOMMENDATION: no. It runs the target's whole
  bar, and a verb whose cost is the target's full test suite should be asked for. The default's message
  says what it measured, which is the honest limit; a hurried reader can still misread it and that is
  stated rather than designed away.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. Grounded on a twelve-agent audit that measured the declaration
  absent from every shipped file, the baseline phase absent from `apply` and from BOTH of the engine's
  own lists of what it cannot do, and the runner's skip-on-absent-guard behaviour reproduced at exit 0.
  Six design decisions came from the adversarial pass rather than the design pass and are folded here:
  ONE vocabulary for `kind`; both baseline reads under one guard regime with a dead-probe liveness half
  rather than an emptiness check; the ownership record written before the write it authorizes; a leg
  row the target edited treated as drift; the failure template split from the execution template; and
  the guard drop keyed on tracked-ness rather than existence, re-evaluated after staging.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py` for the emitter, the baseline read and the observer.

The token substituter and the target context ARE the guard renderer: the context already supplies the
install prefix, the kit path and the memory root, so two of the contract's guard classes need no new
code, and the substituter already returns the missing names rather than emitting a brace — which is
exactly the drop-versus-refuse decision.

`needed_answers` already harvests tokens from a leg's argv and guard. That harvest was written for a
consumer that never arrived; this unit is it, and no new intake question machinery is needed.

The planner's unresolved-destination refusal supplies the message shape and the POSITION for an
unresolved argv token: name the key, refuse before any write.

The pre-write refusal pass is where the declaration is validated. Legs are emitted last, so a bad
declaration discovered at emission time would refuse after everything landed.

The hole-probe loop is the shape the exemption reuses verbatim, including its four failure directions
— it is already this repo's proof that a probe which cannot launch is a finding rather than a pass.

The structural merger's serializer settings are shared through one helper rather than respelled.

No seam exists for parsing a runner's output, for the declaration or its reader, for the three-valued
verdict, for the hook probe, or for any YAML. Each is named with the measurement proving nothing
exists to extend: the runner's status strings are spelled in exactly one place and that place PRINTS
them; the declaration has zero occurrences; the verdict has no data structure; git's hook subcommand
is wrapped nowhere; and this repo contains no workflow file at all, so the CI template is written from
nothing rather than copied.
